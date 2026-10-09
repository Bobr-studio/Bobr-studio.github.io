"""Сборка сайта Bobr Studio из шаблонов и переводов.

    python3 build.py

templates/*.html — разметка с {{ключами}}; i18n/<язык>.json — тексты.
Английский — в корне сайта, остальные языки — в папках /<язык>/.
Новый язык: добавить i18n/<код>.json и строку в LANGS.
Новая игра: шаблон templates/game-<имя>.html и строка в PAGES.
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

# Шаблон → путь страницы внутри языковой папки.
PAGES = {
    'index.html': 'index.html',
    'game-dots-rpg.html': 'dots-rpg/index.html',
}

# Политики конфиденциальности — в этом же репозитории: legal/<приложение>/ (en в корне,
# остальные языки приложения — в подпапках; Chrono Blocks — build_legal.py).
# Ссылка с сайта — на политику Dots RPG.
PRIVACY = {'ru': 'https://bobr-studio.github.io/legal/dots-rpg/ru/'}
PRIVACY_DEFAULT = 'https://bobr-studio.github.io/legal/dots-rpg/'

# Тизеры будущих проектов: процент готовности и картинка (необязательно;
# путь от корня сайта, например 'assets/next-game.png'). Без картинки — заглушка.
TEASERS = {
    # Scrap Siege (рабочее название) — роботы, модификации, захват зданий.
    'teaser_next_game': {'percent': 5, 'image': 'assets/scrap-siege-teaser.png', 'style': 'fog',
                         'title': 'next_title', 'text': 'next_text'},
    # Chrono Blocks (~/IdeaProjects/BobrStudio/apps/chrono-blocks) — таймер по блокам.
    # Название уже не секрет: вместо «Секретный проект» — «Скоро».
    'teaser_chrono': {'percent': 80, 'image': 'assets/chrono-blocks-teaser.png', 'style': 'fog',
                      'name': 'Chrono Blocks', 'label': 'chip_soon'},
    # Easer Life (~/IdeaProjects/BobrStudio/apps/easer-life) — вечерний ритуал паузы; % по реестру задач.
    'teaser_first_app': {'percent': 23, 'image': 'assets/easer-life-teaser.png', 'style': 'fog',
                         'title': 'next_app_title', 'text': 'app_soon_text'},
}
LOGS_TOTAL = 8  # брёвен в плотине при 0%


def teaser_html(cfg, t, root):
    """Плитка будущего проекта на всю карточку. Снизу картинку закрывает
    плотина из брёвен ('dam', для игр) или туман ('fog', для приложений) —
    ровно на (100 - percent)%; надписи поверх."""
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
    return (f'<div class="card teaser">{img}{cover_html}'
            f'<div class="over"><div><small>{t[cfg.get("label", "secret_project")]}</small>'
            + _teaser_title(cfg, t) + '</div>'
            f'{big or "<div></div>"}'
            f'<div><div class="bar"><i style="width:{p}%"></i></div>'
            f'<div class="pct"><span>{stage}</span><span>{p}% {t["ready"]}</span></div></div></div></div>')


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


def lang_dir(lang):
    return '' if lang == DEFAULT else f'{lang}/'


def build():
    strings = {
        lang: json.loads((ROOT / 'i18n' / f'{lang}.json').read_text('utf-8'))
        for lang in LANGS
    }
    count = 0
    for template, page in PAGES.items():
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
                langcss=LANG_CSS,
                **{key: teaser_html(cfg, strings[lang], root) for key, cfg in TEASERS.items()},
                hreflang='\n'.join(
                    f'<link rel="alternate" hreflang="{code}" '
                    f'href="{SITE}{lang_dir(code)}{page.removesuffix("index.html")}">'
                    for code in LANGS
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


if __name__ == '__main__':
    build()
