"""Тексты политики конфиденциальности Dots RPG (языки игры: en, ru).

Только данные; страницы собирает build_legal.py. Раздел про рекламу за награду
(Unity Ads) — флаг DR_ADS в build_legal.py. При изменениях данных — обновить
все языки и дату.
"""

# Порядок и названия — как в переключателе языка в игре.
LANGS = {'en': 'English', 'ru': 'Русский'}

# {app} {unity} {mail} {un_privacy} {fb_privacy} — подставляются.
T = {
'en': dict(
    title='Privacy Policy', dev='Developer', date='Effective October 16, 2026',
    intro='This policy explains how the mobile game {app} (the “Game”) handles user information.',
    h_short='In short',
    short='<b>The Game does not collect personal data</b> such as your name, e-mail, contacts or location. With your permission it sends <b>anonymous statistics</b> and <b>crash reports</b> so we can improve the Game and fix bugs. Without an internet connection nothing is sent and the Game works as usual.',
    short_ads=' The Game can show a <b>short video ad</b>, but only when you tap a button to get a reward (for example, double experience); the ad network may process technical data about your device as described below.',
    h_stored='What is stored on your device',
    stored=['settings (language, sound, vibration, on-board hints, your statistics and crash-report choices) and player names, if you entered them;',
            'an unfinished game, so you can continue it later;',
            'statistics of games against the computer opponent (wins, losses, draws), your experience and level in “Adventure”, the tricks you chose and which tips you have already seen.'],
    stored_p='This data never leaves your device. You can delete it: reset statistics in settings, clear the app data in Android settings, or uninstall the Game. If Android backup is turned on for your device, the system may include this data in your device backup to your Google account; we have no access to it.',
    h_sent='Statistics and crash reports',
    sent_intro='We use Google’s <b translate="no">Firebase</b> service (Firebase Analytics and Firebase Crashlytics).',
    sent=['<b>Anonymous statistics</b> — only if you allowed it on first launch or in settings: which modes, boards and maps are chosen, how long a game lasts and how it ends.',
          '<b>Crash reports</b> — on by default, can be turned off in settings: a technical description of the error, device model, Android and Game version.',
          'A random identifier of this Game installation is sent along with them. It is not linked to your name, account or advertising ID.'],
    sent_p='This data is encrypted in transit, used only to improve the Game, never sold and never used for advertising. Google keeps it for a limited time under its own rules: {fb_privacy}.',
    h_ads='Ads for a reward',
    ads1='The Game has no banners and no ads between games. A video ad is shown <b>only when you choose to watch it</b> by tapping a button with a reward: double experience after a win, replaying the last moves after losing to the computer, or a move hint. Ads are never shown in a game for two players on one phone, and refusing an ad changes nothing else in the Game.',
    ads2='Ads are served by {unity} (Unity Technologies Inc. and its affiliates). We ask Unity to show only <b>non-personalized</b> ads to all users. To show and measure ads and to prevent fraud, the SDK may still collect: the device advertising identifier (Google Advertising ID) and other device identifiers, device model and OS version, language, IP address and approximate location derived from it, information about ad views and clicks, and technical diagnostics. This data is processed by Unity under its privacy policy: {un_privacy}.',
    ads3='You can reset or delete your advertising ID or opt out of ad personalization in your Android settings (<i>Settings → Google → Ads</i> or <i>Settings → Privacy → Ads</i>).',
    h_not='What the Game does not do',
    nots=['no registration; it never asks for your name, e-mail or other contact details;',
          'no access to location (GPS), camera, microphone, contacts or files;',
          'no in-app purchases.'],
    not_ads_noads='no advertising ID and no ads;',
    not_ads='we do not sell your data;',
    h_children='Children',
    children='The Game is not directed at children under 13 and does not knowingly collect data about them.',
    h_changes='Changes',
    changes='If future versions add features involving data (for example, in-app purchases), we will update this page before such a version is released and change the effective date.',
    h_contact='Contact', contact='Questions about this policy: {mail}.',
),
'ru': dict(
    title='Политика конфиденциальности', dev='Разработчик', date='Действует с 16 октября 2026 г.',
    intro='Эта политика описывает, как мобильная игра {app} («Игра») обращается с информацией пользователей.',
    h_short='Коротко',
    short='<b>Игра не собирает личные данные</b> — имя, e-mail, контакты, местоположение. С вашего разрешения она отправляет <b>анонимную статистику</b> и <b>отчёты о сбоях</b>, чтобы мы могли улучшать Игру и исправлять ошибки. Без интернета ничего не отправляется, а Игра работает как обычно.',
    short_ads=' Игра может показать <b>короткий рекламный ролик</b>, но только когда вы сами нажали кнопку, чтобы получить награду (например, двойной опыт); рекламная сеть может обрабатывать технические данные об устройстве, как описано ниже.',
    h_stored='Что хранится на устройстве',
    stored=['настройки (язык, звук, вибрация, подсказки на поле, ваш выбор о статистике и отчётах о сбоях) и имена игроков, если вы их указали;',
            'незаконченная партия, чтобы её можно было продолжить;',
            'статистика партий против компьютерного соперника (победы, поражения, ничьи), ваш опыт и уровень в «Приключении», выбранные приёмы и отметки о том, какие подсказки вы уже видели.'],
    stored_p='Эти данные не покидают устройство. Их можно удалить: сбросить статистику в настройках, очистить данные приложения в настройках Android или удалить Игру. Если на устройстве включено резервное копирование Android, система может включить эти данные в резервную копию устройства в вашем аккаунте Google; у нас к ней доступа нет.',
    h_sent='Статистика и отчёты о сбоях',
    sent_intro='Для этого используется сервис <b translate="no">Firebase</b> компании Google (Firebase Analytics и Firebase Crashlytics).',
    sent=['<b>Анонимная статистика</b> — только если вы разрешили её при первом запуске или в настройках: какие режимы, поля и карты выбирают, сколько длится партия, чем она закончилась.',
          '<b>Отчёты о сбоях</b> — включены по умолчанию, отключаются в настройках: техническое описание ошибки, модель устройства, версия Android и Игры.',
          'Вместе с ними передаётся случайный идентификатор установки Игры. Он не связан с вашим именем, аккаунтом или рекламным идентификатором.'],
    sent_p='Эти данные передаются в зашифрованном виде, используются только для улучшения Игры, не продаются и не используются для рекламы. Google хранит их ограниченное время согласно своим правилам: {fb_privacy}.',
    h_ads='Реклама за награду',
    ads1='В Игре нет баннеров и рекламы между партиями. Рекламный ролик показывается <b>только если вы сами решили его посмотреть</b>, нажав кнопку с наградой: двойной опыт после победы, переиграть последние ходы после проигрыша компьютеру или подсказка хода. В игре вдвоём на одном телефоне реклама не показывается никогда, а отказ от ролика больше ничего в Игре не меняет.',
    ads2='Рекламу предоставляет {unity} (Unity Technologies Inc. и аффилированные лица). Мы просим Unity показывать всем пользователям только <b>неперсонализированную</b> рекламу. Чтобы показывать и учитывать рекламу и защищаться от мошенничества, SDK всё же может собирать: рекламный идентификатор устройства (Google Advertising ID) и другие идентификаторы устройства, модель устройства и версию ОС, язык, IP-адрес и примерное местоположение, определённое по нему, сведения о показах и нажатиях на рекламу, а также техническую диагностику. Эти данные обрабатывает Unity согласно своей политике конфиденциальности: {un_privacy}.',
    ads3='Сбросить или удалить рекламный идентификатор либо отключить персонализацию рекламы можно в настройках Android (<i>Настройки → Google → Реклама</i> или <i>Настройки → Конфиденциальность → Реклама</i>).',
    h_not='Чего Игра не делает',
    nots=['не требует регистрации и не просит имя, e-mail или другие контакты;',
          'не определяет местоположение (GPS) и не обращается к камере, микрофону, контактам и файлам;',
          'не содержит покупок внутри приложения.'],
    not_ads_noads='не использует рекламный идентификатор и не показывает рекламу;',
    not_ads='мы не продаём ваши данные;',
    h_children='Дети',
    children='Игра не предназначена для детей младше 13 лет и сознательно не собирает о них данные.',
    h_changes='Изменения',
    changes='Если в будущих версиях появятся функции, связанные с данными (например, покупки внутри приложения), мы обновим эту страницу до выхода такой версии и изменим дату вступления в силу.',
    h_contact='Контакты', contact='Вопросы по этой политике: {mail}.',
),
}
