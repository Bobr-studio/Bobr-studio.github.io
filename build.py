"""Сборка сайта Bobr Studio из шаблонов и переводов.

    python3 build.py

templates/*.html — разметка с {{ключами}}; i18n/<язык>.json — тексты.
Английский — в корне сайта, остальные языки — в папках /<язык>/.
Новый язык: добавить i18n/<код>.json и строку в LANGS.
Новая игра: шаблон templates/game-<имя>.html и строка в PAGES.
Новое приложение: строка в PAGES (шаблон app.html) и в APPS, тексты <ключ>_… в i18n.
"""
import json
import pathlib
import re

SITE = 'https://bobr-studio.github.io/'
ROOT = pathlib.Path(__file__).parent

# Код языка → название на самом языке. Первый — язык по умолчанию (в корне).
LANGS = {
    'en': 'English', 'ru': 'Русский', 'uk': 'Українська', 'pl': 'Polski',
    'cs': 'Čeština', 'de': 'Deutsch', 'fr': 'Français', 'es': 'Español',
    'pt': 'Português', 'tr': 'Türkçe', 'ja': '日本語', 'ko': '한국어', 'zh': '中文',
}
DEFAULT = 'en'

# Путь страницы внутри языковой папки → шаблон.
PAGES = {
    'index.html': 'index.html',
    'dots-rpg/index.html': 'game-dots-rpg.html',
    'chrono-blocks/index.html': 'app.html',
    'score-night/index.html': 'app.html',
}

# Страницы приложений (один шаблон app.html, стиль студии — вариант B, 2026-10-17).
# key — префикс текстов в i18n (cb_intro, sn_f1…); картинки — из магазина приложения
# (docs/store/…), сжатые в JPG; где нет своего языка — английские.
APPS = {
    'chrono-blocks/index.html': {
        'key': 'cb', 'name': 'Chrono Blocks', 'slug': 'chrono-blocks',
        'accent': '#F07A2B', 'accent2': '#3FAF6E',
        'banner': {}, 'banner_default': 'assets/chrono-blocks-banner.jpg',
        'video': 'https://youtu.be/x7e0hL__VO8',
        'shots': 'assets/chrono-shots/', 'shot_count': 6, 'cols': 3,
    },
    'score-night/index.html': {
        'key': 'sn', 'name': 'Score Night', 'slug': 'score-night',
        'accent': '#B9561E', 'accent2': '#F2A23A',
        'banner': {l: f'assets/score-night-banner-{l}.jpg' for l in ('ru', 'de', 'es', 'fr', 'pl')},
        'banner_default': 'assets/score-night-banner-en.jpg',
        'video': 'https://youtu.be/VabiI_kATD4',
        'shots': 'assets/score-shots/', 'shot_count': 8, 'cols': 4,
    },
}
APP_TEXTS = ['h1_hand', 'intro', 'tagline', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'video_lead', 'shots_lead']

# Политики конфиденциальности — в этом же репозитории: legal/<приложение>/ (en в корне,
# остальные языки приложения — в подпапках; Chrono Blocks — build_legal.py).
# Ссылка с сайта — на политику Dots RPG.
PRIVACY = {'ru': 'https://bobr-studio.github.io/legal/dots-rpg/ru/'}
PRIVACY_DEFAULT = 'https://bobr-studio.github.io/legal/dots-rpg/'
# Баннер Dots RPG: свой — где есть баннер магазина на языке игры (en, ru).
BANNER = {'ru': 'assets/dotsrpg-banner-ru.png'}
BANNER_DEFAULT = 'assets/dotsrpg-banner.png'
# Скриншоты игры (как в Google Play): в игре только en и ru.
SHOTS = {'ru': 'assets/dots-shots/ru/'}
SHOTS_DEFAULT = 'assets/dots-shots/en/'

# Тизеры будущих проектов: процент готовности и картинка (необязательно;
# путь от корня сайта, например 'assets/next-game.png'). Без картинки — заглушка.
TEASERS = {
    # Scrap Siege (рабочее название) — роботы, модификации, захват зданий.
    'teaser_next_game': {'percent': 15, 'image': 'assets/scrap-siege-teaser.png', 'style': 'fog',
                         'title': 'next_title', 'text': 'next_text'},
    # Chrono Blocks (~/IdeaProjects/BobrStudio/apps/chrono-blocks) — таймер по блокам.
    # Название уже не секрет: вместо «Секретный проект» — «Скоро».
    'teaser_chrono': {'percent': 95, 'image': 'assets/chrono-blocks-teaser.png', 'style': 'fog',
                      'name': 'Chrono Blocks', 'label': 'chip_soon', 'href': 'chrono-blocks/index.html'},
    # Score Night (~/IdeaProjects/BobrStudio/apps/score-night) — калькуляторы очков настольных игр.
    'teaser_score_night': {'percent': 90, 'image': 'assets/score-night-teaser.png', 'style': 'fog',
                           'name': 'Score Night', 'label': 'chip_soon', 'href': 'score-night/index.html'},
    # Easer Life (~/IdeaProjects/BobrStudio/apps/easer-life) — вечерний ритуал паузы; % по реестру задач.
    'teaser_first_app': {'percent': 23, 'image': 'assets/easer-life-teaser.png', 'style': 'fog',
                         'title': 'next_app_title', 'text': 'app_soon_text'},
}
LOGS_TOTAL = 8  # брёвен в плотине при 0%


def teaser_html(cfg, t, root):
    """Плитка будущего проекта на всю карточку. Снизу картинку закрывает
    плотина из брёвен ('dam', для игр) или туман ('fog', для приложений) —
    ровно на (100 - percent)%; надписи поверх. С 'href' плитка — ссылка на страницу проекта."""
    p = max(0, min(100, cfg['percent']))
    cover = 100 - p
    stage = t['stage_early'] if p < 50 else t['stage_shape'] if p < 80 else t['stage_almost']
    img = f'<img src="{root}{cfg["image"]}" alt="">' if cfg['image'] else ''
    big = ''
    if cfg['style'] == 'dam':
        logs = max(1 if cover else 0, round(LOGS_TOTAL * cover / 100))
        # Внизу 72px заняты прогрессом: табличка — по центру плотины выше них,
        # а на низкой плотине — над верхним бревном.
        sign = (f'<div class="sign" style="top:calc((100% - 72px) / 2)">' if cover >= 45
                else '<div class="sign top">') + f'{p}%<small>{t["ready"]}</small></div>'
        # Почти закрытая плитка: бобр садится на бревно, а не уходит за край.
        gnaw = '<span class="gnaw" style="transform:translateY(-10%)">🦫</span>' if cover > 88 else '<span class="gnaw">🦫</span>'
        cover_html = (f'<div class="dam" style="height:{cover}%">{gnaw}'
                      + '<div class="log"></div>' * logs + sign + '</div>') if logs else ''
    else:
        cover_html = f'<div class="fog" style="height:{cover}%"></div>' if cover else ''
        big = f'<div class="big"><b>{p}%</b><span>{t["ready"]}</span></div>'
    tag, href = ('a', f' href="{cfg["href"]}"') if cfg.get('href') else ('div', '')
    return (f'<{tag} class="card teaser"{href}>{img}{cover_html}'
            f'<div class="over"><div><small>{t[cfg.get("label", "secret_project")]}</small>'
            + _teaser_title(cfg, t) + '</div>'
            f'{big or "<div></div>"}'
            f'<div><div class="bar"><i style="width:{p}%"></i></div>'
            f'<div class="pct"><span>{stage}</span><span>{p}% {t["ready"]}</span></div></div></div></{tag}>')


def _teaser_title(cfg, t):
    """Заголовок плитки: имя проекта как есть ('name', не переводится)
    или ключ перевода ('title')."""
    if cfg.get('name'):
        return f'<h3 translate="no">{cfg["name"]}</h3>'
    return f'<h3>{t[cfg["title"]]}</h3>' if cfg.get('title') else ''


LANG_CSS = """
  .langs { position: relative; }
  .langs summary { list-style: none; cursor: pointer; padding: 5px 14px; border-radius: 999px;
    border: 2px solid rgba(247,241,232,.35); color: #F7F1E8; font: 500 15px Rubik, sans-serif; }
  .langs summary::-webkit-details-marker { display: none; }
  .langs[open] summary { background: rgba(247,241,232,.12); }
  .langs .menu { position: absolute; right: 0; top: calc(100% + 8px); z-index: 10; background: #fff;
    border-radius: 16px; padding: 8px; box-shadow: 0 14px 34px rgba(0,0,0,.25);
    display: grid; grid-template-columns: repeat(2, minmax(120px, 1fr)); gap: 2px; }
  .langs .menu a { display: block; padding: 7px 12px; border-radius: 10px; color: #1E2A2F;
    text-decoration: none; font: 500 15px Rubik, sans-serif; white-space: nowrap; }
  .langs .menu a:hover { background: #F7F1E8; }
  .langs .menu a.current { background: #FFF0E0; color: #A85A0E; font-weight: 700; }
"""


def app_values(cfg, lang, t, root):
    """Значения {{app_…}} для шаблона app.html: тексты приложения на языке и картинки."""
    shots_dir = root + cfg['shots'] + (lang if (ROOT / cfg['shots'] / lang).is_dir() else DEFAULT) + '/'
    key = cfg['key']
    note = t.get(f'{key}_note')
    values = {f'app_{name}': t[f'{key}_{name}'] for name in APP_TEXTS}
    values.update(
        app_name=cfg['name'], app_accent=cfg['accent'], app_accent2=cfg['accent2'], app_cols=str(cfg['cols']),
        app_meta=t[f'{key}_tagline'],
        app_icon=f'{root}assets/{cfg["slug"]}-icon.png',
        app_banner=root + cfg['banner'].get(lang, cfg['banner_default']),
        app_thumb=f'{root}assets/{cfg["slug"]}-video.jpg', app_video=cfg['video'],
        app_privacy=f'{SITE}legal/{cfg["slug"]}/{lang_dir(lang)}',
        app_note=f'<p class="note">{note}</p>' if note else '',
        app_shots_h=t['app_shots_h'],
        app_shots='\n      '.join(
            f'<li><img src="{shots_dir}{i}.jpg" alt="{cfg["name"]} — {t["app_shots_h"]} {i}" '
            f'loading="lazy" width="540" height="960"></li>' for i in range(1, cfg['shot_count'] + 1)),
    )
    return values


def lang_dir(lang):
    return '' if lang == DEFAULT else f'{lang}/'


def build():
    strings = {
        lang: json.loads((ROOT / 'i18n' / f'{lang}.json').read_text('utf-8'))
        for lang in LANGS
    }
    count = 0
    for page, template in PAGES.items():
        source = (ROOT / 'templates' / template).read_text('utf-8')
        for lang in LANGS:
            path = lang_dir(lang) + page
            depth = path.count('/')
            root = '../' * depth
            values = dict(strings[lang])
            values.update(
                lang=lang,
                root=root,
                home=root + lang_dir(lang) + 'index.html',
                game_url='dots-rpg/index.html',
                privacy_url=PRIVACY.get(lang, PRIVACY_DEFAULT),
                banner=root + BANNER.get(lang, BANNER_DEFAULT),
                shots=root + SHOTS.get(lang, SHOTS_DEFAULT),
                langcss=LANG_CSS,
                **{key: teaser_html(cfg, strings[lang], root) for key, cfg in TEASERS.items()},
                **(app_values(APPS[page], lang, strings[lang], root) if page in APPS else {}),
                hreflang='\n'.join(
                    [f'<link rel="canonical" href="{url(lang, page)}">']
                    + [f'<link rel="alternate" hreflang="{code}" href="{url(code, page)}">' for code in LANGS]
                    + [f'<link rel="alternate" hreflang="x-default" href="{url(DEFAULT, page)}">']
                ),
                langmenu=(
                    f'<details class="langs"><summary>🌐 {LANGS[lang]}</summary>'
                    '<div class="menu">'
                    + ''.join(
                        f'<a href="{root}{lang_dir(code)}{page}"'
                        f'{" class=\"current\"" if code == lang else ""}>{name}</a>'
                        for code, name in LANGS.items()
                    )
                    + '</div></details>'
                ),
            )

            def fill(match):
                key = match.group(1)
                if key not in values:
                    raise KeyError(f'{lang}: нет перевода для «{key}» ({template})')
                return values[key]

            html = re.sub(r'\{\{(\w+)\}\}', fill, source)
            out = ROOT / path
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(html, 'utf-8')
            count += 1
    print(f'Собрано страниц: {count} ({len(LANGS)} языков × {len(PAGES)} страниц)')
    write_sitemap()


def url(lang, page):
    return SITE + lang_dir(lang) + page.removesuffix('index.html')


def write_sitemap():
    """sitemap.xml (все страницы сайта и политики legal/) и robots.txt — для Google и Яндекса."""
    urls = [url(lang, page) for page in PAGES for lang in LANGS]
    urls += sorted(SITE + str(p.parent.relative_to(ROOT)) + '/' for p in (ROOT / 'legal').rglob('index.html'))
    (ROOT / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + ''.join(f'  <url><loc>{u}</loc></url>\n' for u in urls)
        + '</urlset>\n', 'utf-8')
    (ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n', 'utf-8')
    print(f'sitemap.xml: {len(urls)} адресов')


if __name__ == '__main__':
    build()
