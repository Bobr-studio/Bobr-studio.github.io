# Bobr Studio — сайт студии

Сайт: https://bobr-studio.github.io/ (GitHub Pages, репозиторий `Bobr-studio.github.io`).

## Как устроено

- `templates/` — разметка страниц с `{{ключами}}` (лендинг студии, страницы игр);
- `i18n/<язык>.json` — тексты на 13 языках (en — по умолчанию, в корне сайта);
- `assets/` — картинки;
- `build.py` — собирает готовые страницы: `python3 build.py`.

Сгенерированные `index.html`, `dots-rpg/`, `ru/`, `de/` … — результат сборки,
их руками не правим: правим шаблон или перевод и пересобираем.

## Как добавить

- **Язык:** `i18n/<код>.json` (скопировать `en.json` и перевести) + строка в `LANGS` в `build.py`.
- **Игру:** шаблон `templates/game-<имя>.html` (по образцу Dots RPG), строка в `PAGES`,
  карточка в `templates/index.html` и тексты в `i18n/*.json`.
- **Ссылку на Google Play** (после выхода): в `templates/game-dots-rpg.html` заменить
  кнопку «coming soon» на ссылку из комментария рядом с ней.
