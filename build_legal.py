#!/usr/bin/env python3
"""Политика конфиденциальности Chrono Blocks на всех 13 языках приложения.

Текст — ниже, по языкам; страницы: legal/chrono-blocks/index.html (en)
и legal/chrono-blocks/<язык>/index.html. Запуск: python3 build_legal.py
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent / 'legal' / 'chrono-blocks'
BASE = 'https://bobr-studio.github.io/legal/chrono-blocks/'
MAIL = 'bobrstudio.dev@gmail.com'

# Порядок и названия — как в переключателе языка в приложении.
LANGS = {
    'en': 'English', 'ru': 'Русский', 'uk': 'Українська', 'pl': 'Polski',
    'cs': 'Čeština', 'de': 'Deutsch', 'fr': 'Français', 'es': 'Español',
    'pt': 'Português', 'tr': 'Türkçe', 'ja': '日本語', 'ko': '한국어', 'zh': '中文',
}

# {app} {ads} {sdk} {gp} {mail} {ya_privacy} {ya_terms} {g_privacy} — подставляются ниже.
T = {
'en': dict(
    title='Privacy Policy', dev='Developer', date='Effective October 9, 2026',
    intro='This policy explains how the mobile app {app} (the “App”), a timer that splits talks, meetings, workouts and interviews into blocks, handles user information.',
    h_short='In short',
    short='<b>We do not collect personal data</b>: no registration, no name, e-mail, contacts or files. Your templates and settings stay on your device. The free version shows <b>ads</b> provided by {ads}; the ad network may process technical data about your device as described below. You can remove ads with a one-time purchase.',
    h_stored='What is stored on your device',
    stored=['your templates (names, blocks, durations, red-zone and signal settings) and the selected template;',
            'the app language, if you chose it in the App;',
            'whether you bought “Remove ads”.'],
    stored_p='This data is not sent to us. You can delete it by removing templates in the App, clearing the app data in Android settings, or uninstalling the App.',
    h_notif='Notifications',
    notif='If the App is in the background during a timer run, it schedules <b>local notifications</b> on your device to signal the end of each block. They are created and shown by your phone; nothing is sent over the internet.',
    h_ads='Advertising (free version)',
    ads1='Ads are shown on the home and results screens — never on the timer screen. They are served by {sdk} (YANDEX LLC and its affiliates). To show and measure ads, the SDK may collect: the device advertising identifier (Google Advertising ID), device model and OS version, language, IP address and approximate location derived from it, and information about ad views and clicks. The SDK includes the AppMetrica component (also by Yandex), which collects technical diagnostics such as crash reports. Users in the EEA, the UK and Switzerland are shown only non-personalized ads.',
    ads2='You can reset or delete your advertising ID or opt out of ad personalization in your Android settings (<i>Settings → Google → Ads</i> or <i>Settings → Privacy → Ads</i>). Yandex privacy policy: {ya_privacy}; Yandex Mobile Ads terms: {ya_terms}.',
    h_purch='Purchases',
    purch='“Remove ads” is sold through {gp}. Payment is processed by Google; we never receive your card or payment details — only a confirmation that the purchase was made. See the {g_privacy}.',
    g_privacy='Google Privacy Policy',
    h_not='What the App does not do',
    nots=['no account and no registration;',
          'no access to location (GPS), camera, microphone, contacts or files;',
          'we do not sell data and do not use analytics services of our own.'],
    h_children='Children',
    children='The App is not directed at children under 13 and does not knowingly collect data about them.',
    h_changes='Changes',
    changes='If future versions add features involving data, we will update this page before such a version is released and change the effective date.',
    h_contact='Contact', contact='Questions about this policy: {mail}.',
),
'ru': dict(
    title='Политика конфиденциальности', dev='Разработчик', date='Действует с 9 октября 2026 г.',
    intro='Эта политика описывает, как мобильное приложение {app} («Приложение») — таймер, который делит выступления, встречи, тренировки и собеседования на блоки, — обращается с информацией пользователей.',
    h_short='Коротко',
    short='<b>Мы не собираем персональные данные</b>: нет регистрации, мы не спрашиваем имя, e-mail, контакты или файлы. Ваши шаблоны и настройки хранятся на устройстве. В бесплатной версии показывается <b>реклама</b> от {ads}; рекламная сеть может обрабатывать технические данные об устройстве, как описано ниже. Рекламу можно убрать разовой покупкой.',
    h_stored='Что хранится на устройстве',
    stored=['ваши шаблоны (названия, блоки, длительность, красная зона и сигналы) и выбранный шаблон;',
            'язык приложения, если вы выбрали его в Приложении;',
            'отметка о покупке «Убрать рекламу».'],
    stored_p='Эти данные нам не передаются. Удалить их можно, удалив шаблоны в Приложении, очистив данные приложения в настройках Android или удалив Приложение.',
    h_notif='Уведомления',
    notif='Если во время работы таймера Приложение свёрнуто, оно ставит <b>локальные уведомления</b> на устройстве, чтобы подать сигнал в конце каждого блока. Их создаёт и показывает сам телефон; через интернет ничего не передаётся.',
    h_ads='Реклама (бесплатная версия)',
    ads1='Реклама показывается на главном экране и экране итогов — никогда на экране таймера. Её предоставляет {sdk} (ООО «ЯНДЕКС» и аффилированные лица). Чтобы показывать рекламу и учитывать показы, SDK может собирать: рекламный идентификатор устройства (Google Advertising ID), модель устройства и версию ОС, язык, IP-адрес и примерное местоположение, определённое по нему, а также сведения о показах и нажатиях на рекламу. В SDK входит компонент AppMetrica (тоже Яндекса), который собирает техническую диагностику, например отчёты о сбоях. Пользователям из ЕЭЗ, Великобритании и Швейцарии показывается только неперсонализированная реклама.',
    ads2='Сбросить или удалить рекламный идентификатор либо отключить персонализацию рекламы можно в настройках Android (<i>Настройки → Google → Реклама</i> или <i>Настройки → Конфиденциальность → Реклама</i>). Политика конфиденциальности Яндекса: {ya_privacy}; условия Yandex Mobile Ads: {ya_terms}.',
    h_purch='Покупки',
    purch='«Убрать рекламу» продаётся через {gp}. Оплату обрабатывает Google; мы не получаем данные карты и платежей — только подтверждение, что покупка совершена. См. {g_privacy}.',
    g_privacy='Политику конфиденциальности Google',
    h_not='Чего Приложение не делает',
    nots=['нет аккаунта и регистрации;',
          'нет доступа к местоположению (GPS), камере, микрофону, контактам и файлам;',
          'мы не продаём данные и не используем собственных сервисов аналитики.'],
    h_children='Дети',
    children='Приложение не предназначено для детей младше 13 лет и сознательно не собирает данные о них.',
    h_changes='Изменения',
    changes='Если в будущих версиях появятся функции, связанные с данными, мы обновим эту страницу до выхода такой версии и изменим дату вступления в силу.',
    h_contact='Контакты', contact='Вопросы по этой политике: {mail}.',
),
'uk': dict(
    title='Політика конфіденційності', dev='Розробник', date='Діє з 9 жовтня 2026 р.',
    intro='Ця політика описує, як мобільний застосунок {app} («Застосунок») — таймер, що ділить виступи, зустрічі, тренування й співбесіди на блоки, — поводиться з інформацією користувачів.',
    h_short='Коротко',
    short='<b>Ми не збираємо персональні дані</b>: немає реєстрації, ми не питаємо ім’я, e-mail, контакти чи файли. Ваші шаблони й налаштування зберігаються на пристрої. У безкоштовній версії показується <b>реклама</b> від {ads}; рекламна мережа може обробляти технічні дані про пристрій, як описано нижче. Рекламу можна прибрати разовою покупкою.',
    h_stored='Що зберігається на пристрої',
    stored=['ваші шаблони (назви, блоки, тривалість, червона зона й сигнали) та вибраний шаблон;',
            'мова застосунку, якщо ви вибрали її в Застосунку;',
            'позначка про покупку «Прибрати рекламу».'],
    stored_p='Ці дані нам не передаються. Видалити їх можна, видаливши шаблони в Застосунку, очистивши дані застосунку в налаштуваннях Android або видаливши Застосунок.',
    h_notif='Сповіщення',
    notif='Якщо під час роботи таймера Застосунок згорнуто, він ставить <b>локальні сповіщення</b> на пристрої, щоб подати сигнал наприкінці кожного блоку. Їх створює й показує сам телефон; через інтернет нічого не передається.',
    h_ads='Реклама (безкоштовна версія)',
    ads1='Реклама показується на головному екрані та екрані підсумків — ніколи на екрані таймера. Її надає {sdk} (YANDEX LLC та афілійовані особи). Щоб показувати рекламу й враховувати покази, SDK може збирати: рекламний ідентифікатор пристрою (Google Advertising ID), модель пристрою й версію ОС, мову, IP-адресу та приблизне місцезнаходження, визначене за нею, а також відомості про покази й натискання на рекламу. До SDK входить компонент AppMetrica (теж від Yandex), який збирає технічну діагностику, наприклад звіти про збої. Користувачам з ЄЕЗ, Великої Британії та Швейцарії показується лише неперсоналізована реклама.',
    ads2='Скинути чи видалити рекламний ідентифікатор або вимкнути персоналізацію реклами можна в налаштуваннях Android (<i>Налаштування → Google → Реклама</i> або <i>Налаштування → Конфіденційність → Реклама</i>). Політика конфіденційності Yandex: {ya_privacy}; умови Yandex Mobile Ads: {ya_terms}.',
    h_purch='Покупки',
    purch='«Прибрати рекламу» продається через {gp}. Оплату обробляє Google; ми не отримуємо дані картки й платежів — лише підтвердження, що покупку здійснено. Див. {g_privacy}.',
    g_privacy='Політику конфіденційності Google',
    h_not='Чого Застосунок не робить',
    nots=['немає акаунта й реєстрації;',
          'немає доступу до місцезнаходження (GPS), камери, мікрофона, контактів і файлів;',
          'ми не продаємо дані й не використовуємо власних сервісів аналітики.'],
    h_children='Діти',
    children='Застосунок не призначений для дітей до 13 років і свідомо не збирає дані про них.',
    h_changes='Зміни',
    changes='Якщо в майбутніх версіях з’являться функції, пов’язані з даними, ми оновимо цю сторінку до виходу такої версії й змінимо дату набрання чинності.',
    h_contact='Контакти', contact='Питання щодо цієї політики: {mail}.',
),
'pl': dict(
    title='Polityka prywatności', dev='Deweloper', date='Obowiązuje od 9 października 2026 r.',
    intro='Niniejsza polityka wyjaśnia, jak aplikacja mobilna {app} („Aplikacja”) — minutnik dzielący prezentacje, spotkania, treningi i rozmowy kwalifikacyjne na bloki — postępuje z informacjami użytkowników.',
    h_short='W skrócie',
    short='<b>Nie zbieramy danych osobowych</b>: nie ma rejestracji, nie pytamy o imię, e-mail, kontakty ani pliki. Twoje szablony i ustawienia pozostają na urządzeniu. Wersja bezpłatna wyświetla <b>reklamy</b> dostarczane przez {ads}; sieć reklamowa może przetwarzać dane techniczne o urządzeniu, jak opisano poniżej. Reklamy można usunąć jednorazowym zakupem.',
    h_stored='Co jest przechowywane na urządzeniu',
    stored=['Twoje szablony (nazwy, bloki, czas trwania, ustawienia czerwonej strefy i sygnałów) oraz wybrany szablon;',
            'język aplikacji, jeśli wybrano go w Aplikacji;',
            'informacja o zakupie „Usuń reklamy”.'],
    stored_p='Te dane nie są do nas wysyłane. Możesz je usunąć, usuwając szablony w Aplikacji, czyszcząc dane aplikacji w ustawieniach Androida lub odinstalowując Aplikację.',
    h_notif='Powiadomienia',
    notif='Jeśli podczas odliczania Aplikacja działa w tle, planuje na urządzeniu <b>powiadomienia lokalne</b>, aby zasygnalizować koniec każdego bloku. Tworzy je i wyświetla telefon; nic nie jest wysyłane przez internet.',
    h_ads='Reklamy (wersja bezpłatna)',
    ads1='Reklamy są wyświetlane na ekranie głównym i ekranie podsumowania — nigdy na ekranie minutnika. Dostarcza je {sdk} (YANDEX LLC i podmioty powiązane). Aby wyświetlać reklamy i mierzyć ich skuteczność, SDK może zbierać: identyfikator reklamowy urządzenia (Google Advertising ID), model urządzenia i wersję systemu, język, adres IP i określoną na jego podstawie przybliżoną lokalizację oraz informacje o wyświetleniach i kliknięciach reklam. SDK zawiera komponent AppMetrica (również od Yandex), który zbiera diagnostykę techniczną, np. raporty o awariach. Użytkownikom z EOG, Wielkiej Brytanii i Szwajcarii wyświetlane są wyłącznie reklamy niespersonalizowane.',
    ads2='Identyfikator reklamowy możesz zresetować lub usunąć albo wyłączyć personalizację reklam w ustawieniach Androida (<i>Ustawienia → Google → Reklamy</i> lub <i>Ustawienia → Prywatność → Reklamy</i>). Polityka prywatności Yandex: {ya_privacy}; warunki Yandex Mobile Ads: {ya_terms}.',
    h_purch='Zakupy',
    purch='„Usuń reklamy” jest sprzedawane przez {gp}. Płatność obsługuje Google; nigdy nie otrzymujemy danych karty ani płatności — tylko potwierdzenie dokonania zakupu. Zobacz {g_privacy}.',
    g_privacy='Politykę prywatności Google',
    h_not='Czego Aplikacja nie robi',
    nots=['nie ma konta ani rejestracji;',
          'brak dostępu do lokalizacji (GPS), aparatu, mikrofonu, kontaktów i plików;',
          'nie sprzedajemy danych i nie używamy własnych usług analitycznych.'],
    h_children='Dzieci',
    children='Aplikacja nie jest skierowana do dzieci poniżej 13 lat i świadomie nie zbiera danych na ich temat.',
    h_changes='Zmiany',
    changes='Jeśli przyszłe wersje dodadzą funkcje związane z danymi, zaktualizujemy tę stronę przed wydaniem takiej wersji i zmienimy datę obowiązywania.',
    h_contact='Kontakt', contact='Pytania dotyczące tej polityki: {mail}.',
),
'cs': dict(
    title='Zásady ochrany soukromí', dev='Vývojář', date='Platné od 9. října 2026',
    intro='Tyto zásady vysvětlují, jak mobilní aplikace {app} („Aplikace“) — časovač, který dělí přednášky, schůzky, tréninky a pohovory na bloky — nakládá s informacemi uživatelů.',
    h_short='Stručně',
    short='<b>Neshromažďujeme osobní údaje</b>: žádná registrace, neptáme se na jméno, e-mail, kontakty ani soubory. Vaše šablony a nastavení zůstávají v zařízení. Bezplatná verze zobrazuje <b>reklamy</b> od {ads}; reklamní síť může zpracovávat technické údaje o zařízení, jak je popsáno níže. Reklamy lze odstranit jednorázovým nákupem.',
    h_stored='Co se ukládá v zařízení',
    stored=['vaše šablony (názvy, bloky, délky, nastavení červené zóny a signálů) a vybraná šablona;',
            'jazyk aplikace, pokud jste jej v Aplikaci zvolili;',
            'informace, zda jste koupili „Odstranit reklamy“.'],
    stored_p='Tyto údaje se nám neodesílají. Smazat je můžete odstraněním šablon v Aplikaci, vymazáním dat aplikace v nastavení Androidu nebo odinstalováním Aplikace.',
    h_notif='Oznámení',
    notif='Pokud je Aplikace během běhu časovače na pozadí, naplánuje v zařízení <b>místní oznámení</b>, která signalizují konec každého bloku. Vytváří a zobrazuje je telefon; přes internet se nic neodesílá.',
    h_ads='Reklamy (bezplatná verze)',
    ads1='Reklamy se zobrazují na hlavní obrazovce a obrazovce výsledků — nikdy na obrazovce časovače. Poskytuje je {sdk} (YANDEX LLC a přidružené společnosti). K zobrazování a měření reklam může SDK shromažďovat: reklamní identifikátor zařízení (Google Advertising ID), model zařízení a verzi systému, jazyk, IP adresu a z ní odvozenou přibližnou polohu a informace o zobrazeních a kliknutích na reklamy. Součástí SDK je komponenta AppMetrica (rovněž od Yandexu), která shromažďuje technickou diagnostiku, například hlášení o pádech. Uživatelům z EHP, Spojeného království a Švýcarska se zobrazují pouze nepersonalizované reklamy.',
    ads2='Reklamní identifikátor můžete resetovat nebo smazat, případně vypnout personalizaci reklam v nastavení Androidu (<i>Nastavení → Google → Reklamy</i> nebo <i>Nastavení → Soukromí → Reklamy</i>). Zásady ochrany soukromí Yandexu: {ya_privacy}; podmínky Yandex Mobile Ads: {ya_terms}.',
    h_purch='Nákupy',
    purch='„Odstranit reklamy“ se prodává přes {gp}. Platbu zpracovává Google; nikdy nedostáváme údaje o kartě ani platbě — pouze potvrzení, že nákup proběhl. Viz {g_privacy}.',
    g_privacy='Zásady ochrany soukromí Google',
    h_not='Co Aplikace nedělá',
    nots=['žádný účet a žádná registrace;',
          'žádný přístup k poloze (GPS), fotoaparátu, mikrofonu, kontaktům ani souborům;',
          'neprodáváme data a nepoužíváme vlastní analytické služby.'],
    h_children='Děti',
    children='Aplikace není určena dětem mladším 13 let a vědomě o nich neshromažďuje údaje.',
    h_changes='Změny',
    changes='Pokud budoucí verze přidají funkce týkající se dat, aktualizujeme tuto stránku před vydáním takové verze a změníme datum platnosti.',
    h_contact='Kontakt', contact='Dotazy k těmto zásadám: {mail}.',
),
'de': dict(
    title='Datenschutzerklärung', dev='Entwickler', date='Gültig ab 9. Oktober 2026',
    intro='Diese Erklärung beschreibt, wie die mobile App {app} (die „App“), ein Timer, der Vorträge, Meetings, Trainings und Vorstellungsgespräche in Blöcke aufteilt, mit Nutzerinformationen umgeht.',
    h_short='Kurz gesagt',
    short='<b>Wir erheben keine personenbezogenen Daten</b>: keine Registrierung, kein Name, keine E-Mail, keine Kontakte oder Dateien. Ihre Vorlagen und Einstellungen bleiben auf Ihrem Gerät. Die kostenlose Version zeigt <b>Werbung</b> von {ads}; das Werbenetzwerk kann technische Daten über Ihr Gerät verarbeiten, wie unten beschrieben. Die Werbung lässt sich mit einem einmaligen Kauf entfernen.',
    h_stored='Was auf Ihrem Gerät gespeichert wird',
    stored=['Ihre Vorlagen (Namen, Blöcke, Dauer, Einstellungen für rote Zone und Signale) und die ausgewählte Vorlage;',
            'die App-Sprache, falls Sie sie in der App gewählt haben;',
            'ob Sie „Werbung entfernen“ gekauft haben.'],
    stored_p='Diese Daten werden nicht an uns gesendet. Sie können sie löschen, indem Sie Vorlagen in der App entfernen, die App-Daten in den Android-Einstellungen löschen oder die App deinstallieren.',
    h_notif='Benachrichtigungen',
    notif='Läuft die App während eines Timers im Hintergrund, plant sie <b>lokale Benachrichtigungen</b> auf Ihrem Gerät, um das Ende jedes Blocks zu signalisieren. Sie werden vom Telefon erstellt und angezeigt; nichts wird über das Internet gesendet.',
    h_ads='Werbung (kostenlose Version)',
    ads1='Werbung erscheint auf dem Start- und dem Ergebnisbildschirm — niemals auf dem Timer-Bildschirm. Sie wird von {sdk} (YANDEX LLC und verbundene Unternehmen) ausgeliefert. Um Werbung anzuzeigen und zu messen, kann das SDK erheben: die Werbe-ID des Geräts (Google Advertising ID), Gerätemodell und Betriebssystemversion, Sprache, IP-Adresse und daraus abgeleiteten ungefähren Standort sowie Informationen zu Anzeigenaufrufen und -klicks. Das SDK enthält die Komponente AppMetrica (ebenfalls von Yandex), die technische Diagnosedaten wie Absturzberichte erhebt. Nutzern im EWR, im Vereinigten Königreich und in der Schweiz wird nur nicht personalisierte Werbung angezeigt.',
    ads2='Sie können Ihre Werbe-ID zurücksetzen oder löschen oder personalisierte Werbung in den Android-Einstellungen deaktivieren (<i>Einstellungen → Google → Werbung</i> oder <i>Einstellungen → Datenschutz → Werbung</i>). Datenschutzerklärung von Yandex: {ya_privacy}; Nutzungsbedingungen von Yandex Mobile Ads: {ya_terms}.',
    h_purch='Käufe',
    purch='„Werbung entfernen“ wird über {gp} verkauft. Die Zahlung wird von Google abgewickelt; wir erhalten niemals Ihre Karten- oder Zahlungsdaten — nur eine Bestätigung, dass der Kauf erfolgt ist. Siehe {g_privacy}.',
    g_privacy='Datenschutzerklärung von Google',
    h_not='Was die App nicht tut',
    nots=['kein Konto und keine Registrierung;',
          'kein Zugriff auf Standort (GPS), Kamera, Mikrofon, Kontakte oder Dateien;',
          'wir verkaufen keine Daten und nutzen keine eigenen Analysedienste.'],
    h_children='Kinder',
    children='Die App richtet sich nicht an Kinder unter 13 Jahren und erhebt wissentlich keine Daten über sie.',
    h_changes='Änderungen',
    changes='Wenn künftige Versionen Funktionen mit Datenbezug hinzufügen, aktualisieren wir diese Seite vor der Veröffentlichung einer solchen Version und ändern das Gültigkeitsdatum.',
    h_contact='Kontakt', contact='Fragen zu dieser Erklärung: {mail}.',
),
'fr': dict(
    title='Politique de confidentialité', dev='Développeur', date='En vigueur depuis le 9 octobre 2026',
    intro='Cette politique explique comment l’application mobile {app} (l’« Application »), un minuteur qui découpe exposés, réunions, entraînements et entretiens en blocs, traite les informations des utilisateurs.',
    h_short='En bref',
    short='<b>Nous ne collectons pas de données personnelles</b> : pas d’inscription, ni nom, ni e-mail, ni contacts, ni fichiers. Vos modèles et réglages restent sur votre appareil. La version gratuite affiche des <b>publicités</b> fournies par {ads} ; le réseau publicitaire peut traiter des données techniques sur votre appareil, comme décrit ci-dessous. Vous pouvez supprimer les publicités par un achat unique.',
    h_stored='Ce qui est stocké sur votre appareil',
    stored=['vos modèles (noms, blocs, durées, réglages de zone rouge et de signaux) et le modèle sélectionné ;',
            'la langue de l’application, si vous l’avez choisie dans l’Application ;',
            'si vous avez acheté « Supprimer les pubs ».'],
    stored_p='Ces données ne nous sont pas envoyées. Vous pouvez les supprimer en supprimant des modèles dans l’Application, en effaçant les données de l’application dans les réglages Android ou en désinstallant l’Application.',
    h_notif='Notifications',
    notif='Si l’Application est en arrière-plan pendant un minutage, elle programme des <b>notifications locales</b> sur votre appareil pour signaler la fin de chaque bloc. Elles sont créées et affichées par votre téléphone ; rien n’est envoyé sur Internet.',
    h_ads='Publicité (version gratuite)',
    ads1='Les publicités apparaissent sur l’écran d’accueil et l’écran des résultats — jamais sur l’écran du minuteur. Elles sont diffusées par {sdk} (YANDEX LLC et ses sociétés affiliées). Pour afficher et mesurer les publicités, le SDK peut collecter : l’identifiant publicitaire de l’appareil (Google Advertising ID), le modèle de l’appareil et la version du système, la langue, l’adresse IP et la localisation approximative qui en est déduite, ainsi que des informations sur les affichages et les clics. Le SDK comprend le composant AppMetrica (également de Yandex), qui collecte des diagnostics techniques tels que les rapports de plantage. Les utilisateurs de l’EEE, du Royaume-Uni et de la Suisse ne voient que des publicités non personnalisées.',
    ads2='Vous pouvez réinitialiser ou supprimer votre identifiant publicitaire ou désactiver la personnalisation des annonces dans les réglages Android (<i>Paramètres → Google → Annonces</i> ou <i>Paramètres → Confidentialité → Annonces</i>). Politique de confidentialité de Yandex : {ya_privacy} ; conditions de Yandex Mobile Ads : {ya_terms}.',
    h_purch='Achats',
    purch='« Supprimer les pubs » est vendu via {gp}. Le paiement est traité par Google ; nous ne recevons jamais vos données de carte ou de paiement — seulement la confirmation que l’achat a été effectué. Voir les {g_privacy}.',
    g_privacy='Règles de confidentialité de Google',
    h_not='Ce que l’Application ne fait pas',
    nots=['pas de compte ni d’inscription ;',
          'aucun accès à la localisation (GPS), à l’appareil photo, au micro, aux contacts ou aux fichiers ;',
          'nous ne vendons pas de données et n’utilisons pas nos propres services d’analyse.'],
    h_children='Enfants',
    children='L’Application ne s’adresse pas aux enfants de moins de 13 ans et ne collecte pas sciemment de données les concernant.',
    h_changes='Modifications',
    changes='Si de futures versions ajoutent des fonctions liées aux données, nous mettrons à jour cette page avant leur sortie et modifierons la date d’entrée en vigueur.',
    h_contact='Contact', contact='Questions sur cette politique : {mail}.',
),
'es': dict(
    title='Política de privacidad', dev='Desarrollador', date='Vigente desde el 9 de octubre de 2026',
    intro='Esta política explica cómo la aplicación móvil {app} (la «Aplicación»), un temporizador que divide charlas, reuniones, entrenamientos y entrevistas en bloques, trata la información de los usuarios.',
    h_short='En resumen',
    short='<b>No recopilamos datos personales</b>: sin registro, sin nombre, correo, contactos ni archivos. Tus plantillas y ajustes se quedan en tu dispositivo. La versión gratuita muestra <b>anuncios</b> de {ads}; la red publicitaria puede tratar datos técnicos de tu dispositivo, como se describe abajo. Puedes quitar los anuncios con una compra única.',
    h_stored='Qué se guarda en tu dispositivo',
    stored=['tus plantillas (nombres, bloques, duraciones, ajustes de zona roja y señales) y la plantilla seleccionada;',
            'el idioma de la aplicación, si lo elegiste en la Aplicación;',
            'si compraste «Quitar anuncios».'],
    stored_p='Estos datos no se nos envían. Puedes borrarlos eliminando plantillas en la Aplicación, borrando los datos de la aplicación en los ajustes de Android o desinstalando la Aplicación.',
    h_notif='Notificaciones',
    notif='Si la Aplicación está en segundo plano durante un temporizador, programa <b>notificaciones locales</b> en tu dispositivo para avisar del final de cada bloque. Las crea y muestra tu teléfono; no se envía nada por internet.',
    h_ads='Publicidad (versión gratuita)',
    ads1='Los anuncios aparecen en la pantalla principal y en la de resultados — nunca en la pantalla del temporizador. Los sirve {sdk} (YANDEX LLC y sus filiales). Para mostrar y medir anuncios, el SDK puede recopilar: el identificador publicitario del dispositivo (Google Advertising ID), el modelo y la versión del sistema, el idioma, la dirección IP y la ubicación aproximada derivada de ella, e información sobre impresiones y clics. El SDK incluye el componente AppMetrica (también de Yandex), que recopila diagnósticos técnicos como informes de fallos. A los usuarios del EEE, el Reino Unido y Suiza solo se les muestran anuncios no personalizados.',
    ads2='Puedes restablecer o eliminar tu identificador publicitario o desactivar la personalización de anuncios en los ajustes de Android (<i>Ajustes → Google → Anuncios</i> o <i>Ajustes → Privacidad → Anuncios</i>). Política de privacidad de Yandex: {ya_privacy}; condiciones de Yandex Mobile Ads: {ya_terms}.',
    h_purch='Compras',
    purch='«Quitar anuncios» se vende a través de {gp}. El pago lo procesa Google; nunca recibimos los datos de tu tarjeta o pago — solo la confirmación de que la compra se realizó. Consulta la {g_privacy}.',
    g_privacy='Política de privacidad de Google',
    h_not='Lo que la Aplicación no hace',
    nots=['no hay cuenta ni registro;',
          'no accede a la ubicación (GPS), la cámara, el micrófono, los contactos ni los archivos;',
          'no vendemos datos ni usamos servicios de análisis propios.'],
    h_children='Menores',
    children='La Aplicación no está dirigida a menores de 13 años y no recopila datos sobre ellos de forma consciente.',
    h_changes='Cambios',
    changes='Si futuras versiones añaden funciones relacionadas con datos, actualizaremos esta página antes de publicarlas y cambiaremos la fecha de vigencia.',
    h_contact='Contacto', contact='Preguntas sobre esta política: {mail}.',
),
'pt': dict(
    title='Política de Privacidade', dev='Desenvolvedor', date='Em vigor desde 9 de outubro de 2026',
    intro='Esta política explica como o aplicativo móvel {app} (o “Aplicativo”), um timer que divide palestras, reuniões, treinos e entrevistas em blocos, trata as informações dos usuários.',
    h_short='Em resumo',
    short='<b>Não coletamos dados pessoais</b>: sem cadastro, sem nome, e-mail, contatos ou arquivos. Seus modelos e configurações ficam no seu dispositivo. A versão gratuita exibe <b>anúncios</b> fornecidos pelo {ads}; a rede de anúncios pode processar dados técnicos do seu dispositivo, como descrito abaixo. Você pode remover os anúncios com uma compra única.',
    h_stored='O que fica salvo no seu dispositivo',
    stored=['seus modelos (nomes, blocos, durações, configurações de zona vermelha e sinais) e o modelo selecionado;',
            'o idioma do aplicativo, se você o escolheu no Aplicativo;',
            'se você comprou “Remover anúncios”.'],
    stored_p='Esses dados não são enviados para nós. Você pode apagá-los excluindo modelos no Aplicativo, limpando os dados do aplicativo nas configurações do Android ou desinstalando o Aplicativo.',
    h_notif='Notificações',
    notif='Se o Aplicativo estiver em segundo plano durante um timer, ele agenda <b>notificações locais</b> no seu dispositivo para sinalizar o fim de cada bloco. Elas são criadas e exibidas pelo seu celular; nada é enviado pela internet.',
    h_ads='Publicidade (versão gratuita)',
    ads1='Os anúncios aparecem na tela inicial e na tela de resultados — nunca na tela do timer. Eles são exibidos pelo {sdk} (YANDEX LLC e afiliadas). Para exibir e medir anúncios, o SDK pode coletar: o identificador de publicidade do dispositivo (Google Advertising ID), o modelo e a versão do sistema, o idioma, o endereço IP e a localização aproximada derivada dele, além de informações sobre visualizações e cliques. O SDK inclui o componente AppMetrica (também da Yandex), que coleta diagnósticos técnicos, como relatórios de falhas. Usuários do EEE, do Reino Unido e da Suíça veem apenas anúncios não personalizados.',
    ads2='Você pode redefinir ou excluir seu ID de publicidade ou desativar a personalização de anúncios nas configurações do Android (<i>Configurações → Google → Anúncios</i> ou <i>Configurações → Privacidade → Anúncios</i>). Política de privacidade da Yandex: {ya_privacy}; termos do Yandex Mobile Ads: {ya_terms}.',
    h_purch='Compras',
    purch='“Remover anúncios” é vendido pelo {gp}. O pagamento é processado pelo Google; nunca recebemos os dados do seu cartão ou pagamento — apenas a confirmação de que a compra foi feita. Veja a {g_privacy}.',
    g_privacy='Política de Privacidade do Google',
    h_not='O que o Aplicativo não faz',
    nots=['não há conta nem cadastro;',
          'não acessa localização (GPS), câmera, microfone, contatos ou arquivos;',
          'não vendemos dados e não usamos serviços de análise próprios.'],
    h_children='Crianças',
    children='O Aplicativo não é destinado a menores de 13 anos e não coleta dados sobre eles intencionalmente.',
    h_changes='Alterações',
    changes='Se versões futuras adicionarem recursos que envolvam dados, atualizaremos esta página antes do lançamento dessa versão e mudaremos a data de vigência.',
    h_contact='Contato', contact='Dúvidas sobre esta política: {mail}.',
),
'tr': dict(
    title='Gizlilik Politikası', dev='Geliştirici', date='Yürürlük tarihi: 9 Ekim 2026',
    intro='Bu politika, sunumları, toplantıları, antrenmanları ve iş görüşmelerini bloklara bölen bir zamanlayıcı olan {app} mobil uygulamasının (“Uygulama”) kullanıcı bilgilerini nasıl işlediğini açıklar.',
    h_short='Kısaca',
    short='<b>Kişisel veri toplamıyoruz</b>: kayıt yok; ad, e-posta, kişiler veya dosyalar istenmez. Şablonlarınız ve ayarlarınız cihazınızda kalır. Ücretsiz sürüm {ads} tarafından sağlanan <b>reklamlar</b> gösterir; reklam ağı, aşağıda açıklandığı gibi cihazınızla ilgili teknik verileri işleyebilir. Reklamları tek seferlik bir satın alma ile kaldırabilirsiniz.',
    h_stored='Cihazınızda saklananlar',
    stored=['şablonlarınız (adlar, bloklar, süreler, kırmızı bölge ve sinyal ayarları) ve seçili şablon;',
            'Uygulamada seçtiyseniz uygulama dili;',
            '“Reklamları kaldır” satın alınıp alınmadığı.'],
    stored_p='Bu veriler bize gönderilmez. Uygulamada şablonları silerek, Android ayarlarından uygulama verilerini temizleyerek veya Uygulamayı kaldırarak bunları silebilirsiniz.',
    h_notif='Bildirimler',
    notif='Zamanlayıcı çalışırken Uygulama arka plandaysa, her bloğun sonunu bildirmek için cihazınızda <b>yerel bildirimler</b> planlar. Bunları telefonunuz oluşturur ve gösterir; internet üzerinden hiçbir şey gönderilmez.',
    h_ads='Reklamlar (ücretsiz sürüm)',
    ads1='Reklamlar ana ekranda ve sonuç ekranında gösterilir — zamanlayıcı ekranında asla. Reklamları {sdk} (YANDEX LLC ve bağlı şirketleri) sunar. Reklam göstermek ve ölçmek için SDK şunları toplayabilir: cihazın reklam kimliği (Google Advertising ID), cihaz modeli ve işletim sistemi sürümü, dil, IP adresi ve buna göre belirlenen yaklaşık konum ile reklam gösterimleri ve tıklamalarına ilişkin bilgiler. SDK, kilitlenme raporları gibi teknik tanılama verilerini toplayan AppMetrica bileşenini (yine Yandex’e ait) içerir. AEA, Birleşik Krallık ve İsviçre’deki kullanıcılara yalnızca kişiselleştirilmemiş reklamlar gösterilir.',
    ads2='Reklam kimliğinizi sıfırlayabilir veya silebilir ya da reklam kişiselleştirmeyi Android ayarlarından kapatabilirsiniz (<i>Ayarlar → Google → Reklamlar</i> veya <i>Ayarlar → Gizlilik → Reklamlar</i>). Yandex gizlilik politikası: {ya_privacy}; Yandex Mobile Ads şartları: {ya_terms}.',
    h_purch='Satın almalar',
    purch='“Reklamları kaldır” {gp} üzerinden satılır. Ödemeyi Google işler; kart veya ödeme bilgilerinizi asla almayız — yalnızca satın almanın yapıldığına dair bir onay alırız. Bkz. {g_privacy}.',
    g_privacy='Google Gizlilik Politikası',
    h_not='Uygulamanın yapmadıkları',
    nots=['hesap ve kayıt yok;',
          'konuma (GPS), kameraya, mikrofona, kişilere veya dosyalara erişim yok;',
          'veri satmıyoruz ve kendi analiz hizmetlerimizi kullanmıyoruz.'],
    h_children='Çocuklar',
    children='Uygulama 13 yaşından küçük çocuklara yönelik değildir ve onlar hakkında bilerek veri toplamaz.',
    h_changes='Değişiklikler',
    changes='Gelecek sürümler veriyle ilgili özellikler eklerse, bu sayfayı söz konusu sürüm yayınlanmadan önce günceller ve yürürlük tarihini değiştiririz.',
    h_contact='İletişim', contact='Bu politika hakkında sorular: {mail}.',
),
'ja': dict(
    title='プライバシーポリシー', dev='開発者', date='施行日：2026年10月9日',
    intro='本ポリシーは、プレゼン・会議・トレーニング・面接をブロックに分けて計るタイマーアプリ {app}（以下「本アプリ」）が、ユーザー情報をどのように扱うかを説明するものです。',
    h_short='概要',
    short='<b>個人データは収集しません</b>。登録はなく、名前・メールアドレス・連絡先・ファイルも求めません。テンプレートと設定は端末内に保存されます。無料版では {ads} による<b>広告</b>が表示され、広告ネットワークが下記のとおり端末の技術データを処理することがあります。広告は1回限りの購入で削除できます。',
    h_stored='端末に保存されるもの',
    stored=['テンプレート（名前、ブロック、時間、レッドゾーンと通知音の設定）と選択中のテンプレート',
            '本アプリで選択した場合はアプリの言語',
            '「広告を削除」を購入したかどうか'],
    stored_p='これらのデータが当方に送信されることはありません。本アプリでテンプレートを削除する、Androidの設定でアプリのデータを消去する、または本アプリをアンインストールすることで削除できます。',
    h_notif='通知',
    notif='タイマー実行中に本アプリがバックグラウンドにある場合、各ブロックの終了を知らせるために端末上で<b>ローカル通知</b>を予約します。通知は端末自身が作成・表示し、インターネット経由で送信されるものはありません。',
    h_ads='広告（無料版）',
    ads1='広告はホーム画面と結果画面にのみ表示され、タイマー画面には表示されません。広告は {sdk}（YANDEX LLC およびその関連会社）によって配信されます。広告の表示と効果測定のため、SDKは次の情報を収集する場合があります：端末の広告ID（Google Advertising ID）、端末モデルとOSバージョン、言語、IPアドレスとそこから推定されるおおよその位置、広告の表示・クリックに関する情報。SDKには、クラッシュレポートなどの技術的な診断情報を収集するAppMetricaコンポーネント（同じくYandex製）が含まれます。EEA、英国、スイスのユーザーには、パーソナライズされていない広告のみが表示されます。',
    ads2='広告IDのリセット・削除や広告のパーソナライズの無効化は、Androidの設定（<i>設定 → Google → 広告</i> または <i>設定 → プライバシー → 広告</i>）から行えます。Yandexのプライバシーポリシー：{ya_privacy}、Yandex Mobile Adsの利用規約：{ya_terms}。',
    h_purch='購入',
    purch='「広告を削除」は {gp} を通じて販売されます。支払いはGoogleが処理し、当方がカード情報や支払い情報を受け取ることはありません（購入が完了したという確認のみを受け取ります）。{g_privacy}をご覧ください。',
    g_privacy='Googleのプライバシーポリシー',
    h_not='本アプリが行わないこと',
    nots=['アカウントや登録はありません',
          '位置情報（GPS）、カメラ、マイク、連絡先、ファイルにはアクセスしません',
          'データを販売せず、独自の分析サービスも使用しません'],
    h_children='子どもについて',
    children='本アプリは13歳未満の子どもを対象としておらず、子どもに関するデータを意図的に収集することはありません。',
    h_changes='変更',
    changes='今後のバージョンでデータに関わる機能を追加する場合は、そのバージョンの公開前に本ページを更新し、施行日を変更します。',
    h_contact='お問い合わせ', contact='本ポリシーに関するご質問：{mail}',
),
'ko': dict(
    title='개인정보처리방침', dev='개발자', date='시행일: 2026년 10월 9일',
    intro='이 방침은 발표·회의·운동·면접을 블록으로 나누어 시간을 재는 타이머 앱 {app}(이하 “앱”)이 사용자 정보를 어떻게 처리하는지 설명합니다.',
    h_short='요약',
    short='<b>개인정보를 수집하지 않습니다</b>. 가입이 없으며 이름, 이메일, 연락처, 파일을 요구하지 않습니다. 템플릿과 설정은 기기에 저장됩니다. 무료 버전에는 {ads}에서 제공하는 <b>광고</b>가 표시되며, 광고 네트워크는 아래 설명과 같이 기기에 관한 기술 데이터를 처리할 수 있습니다. 광고는 1회 구매로 제거할 수 있습니다.',
    h_stored='기기에 저장되는 정보',
    stored=['템플릿(이름, 블록, 시간, 레드존 및 알림 설정)과 선택한 템플릿',
            '앱에서 선택한 경우 앱 언어',
            '“광고 제거” 구매 여부'],
    stored_p='이 데이터는 저희에게 전송되지 않습니다. 앱에서 템플릿을 삭제하거나, Android 설정에서 앱 데이터를 지우거나, 앱을 삭제하면 지울 수 있습니다.',
    h_notif='알림',
    notif='타이머 실행 중 앱이 백그라운드에 있으면, 각 블록의 종료를 알리기 위해 기기에 <b>로컬 알림</b>을 예약합니다. 알림은 휴대폰이 직접 만들고 표시하며, 인터넷으로 전송되는 것은 없습니다.',
    h_ads='광고(무료 버전)',
    ads1='광고는 홈 화면과 결과 화면에만 표시되며 타이머 화면에는 절대 표시되지 않습니다. 광고는 {sdk}(YANDEX LLC 및 계열사)가 제공합니다. 광고를 표시하고 성과를 측정하기 위해 SDK는 다음 정보를 수집할 수 있습니다: 기기 광고 ID(Google Advertising ID), 기기 모델과 OS 버전, 언어, IP 주소와 이를 통해 추정한 대략적인 위치, 광고 노출 및 클릭 정보. SDK에는 충돌 보고서 등 기술 진단 정보를 수집하는 AppMetrica 구성 요소(역시 Yandex 제공)가 포함되어 있습니다. EEA, 영국, 스위스 사용자에게는 개인 맞춤이 아닌 광고만 표시됩니다.',
    ads2='광고 ID 재설정·삭제 또는 광고 개인 맞춤 해제는 Android 설정(<i>설정 → Google → 광고</i> 또는 <i>설정 → 개인정보 보호 → 광고</i>)에서 할 수 있습니다. Yandex 개인정보처리방침: {ya_privacy}, Yandex Mobile Ads 약관: {ya_terms}.',
    h_purch='구매',
    purch='“광고 제거”는 {gp}를 통해 판매됩니다. 결제는 Google이 처리하며, 저희는 카드 또는 결제 정보를 받지 않습니다. 구매가 완료되었다는 확인만 받습니다. {g_privacy}을 참고하세요.',
    g_privacy='Google 개인정보처리방침',
    h_not='앱이 하지 않는 일',
    nots=['계정과 가입이 없습니다',
          '위치(GPS), 카메라, 마이크, 연락처, 파일에 접근하지 않습니다',
          '데이터를 판매하지 않으며 자체 분석 서비스를 사용하지 않습니다'],
    h_children='아동',
    children='앱은 13세 미만 아동을 대상으로 하지 않으며, 아동에 관한 데이터를 고의로 수집하지 않습니다.',
    h_changes='변경',
    changes='향후 버전에 데이터와 관련된 기능이 추가되면, 해당 버전 출시 전에 이 페이지를 업데이트하고 시행일을 변경합니다.',
    h_contact='문의', contact='이 방침에 관한 문의: {mail}',
),
'zh': dict(
    title='隐私政策', dev='开发者', date='生效日期：2026年10月9日',
    intro='本政策说明移动应用 {app}（以下简称“本应用”）——一款将演讲、会议、训练和面试分成若干时间块的计时器——如何处理用户信息。',
    h_short='简要说明',
    short='<b>我们不收集个人数据</b>：无需注册，不索取姓名、电子邮件、联系人或文件。您的模板和设置保存在设备上。免费版会显示由 {ads} 提供的<b>广告</b>；广告网络可能会按下文所述处理有关您设备的技术数据。您可以通过一次性购买移除广告。',
    h_stored='设备上保存的内容',
    stored=['您的模板（名称、时间块、时长、红色区域和提示音设置）以及所选模板；',
            '应用语言（如果您在本应用中选择了语言）；',
            '是否已购买“移除广告”。'],
    stored_p='这些数据不会发送给我们。您可以在本应用中删除模板、在 Android 设置中清除应用数据或卸载本应用来删除这些数据。',
    h_notif='通知',
    notif='如果计时过程中本应用在后台运行，它会在设备上安排<b>本地通知</b>，在每个时间块结束时提醒您。通知由手机自行创建和显示，不会通过互联网发送任何内容。',
    h_ads='广告（免费版）',
    ads1='广告仅显示在主屏幕和结果屏幕上，绝不会出现在计时屏幕上。广告由 {sdk}（YANDEX LLC 及其关联公司）提供。为展示和衡量广告，SDK 可能会收集：设备广告标识符（Google Advertising ID）、设备型号和系统版本、语言、IP 地址及据此推断的大致位置，以及广告展示和点击信息。SDK 包含 AppMetrica 组件（同样来自 Yandex），用于收集崩溃报告等技术诊断信息。欧洲经济区、英国和瑞士的用户只会看到非个性化广告。',
    ads2='您可以在 Android 设置中重置或删除广告 ID，或关闭广告个性化（<i>设置 → Google → 广告</i> 或 <i>设置 → 隐私 → 广告</i>）。Yandex 隐私政策：{ya_privacy}；Yandex Mobile Ads 条款：{ya_terms}。',
    h_purch='购买',
    purch='“移除广告”通过 {gp} 销售。付款由 Google 处理；我们绝不会收到您的银行卡或付款信息，只会收到购买已完成的确认。请参阅{g_privacy}。',
    g_privacy='Google 隐私权政策',
    h_not='本应用不会做的事',
    nots=['没有账户，无需注册；',
          '不访问位置（GPS）、相机、麦克风、联系人或文件；',
          '我们不出售数据，也不使用自有的分析服务。'],
    h_children='儿童',
    children='本应用不面向 13 岁以下儿童，也不会有意收集有关儿童的数据。',
    h_changes='变更',
    changes='如果未来版本增加涉及数据的功能，我们会在该版本发布前更新本页面并修改生效日期。',
    h_contact='联系我们', contact='有关本政策的问题：{mail}。',
),
}

CSS = """  body { margin: 0; background: #FAFAF8; color: #222; font: 16px/1.6 -apple-system, "Segoe UI", Roboto, "Noto Sans", sans-serif; }
  main { max-width: 720px; margin: 0 auto; padding: 32px 20px 64px; }
  h1 { font-size: 28px; margin-bottom: 4px; }
  h1 span, h2 { color: #D9661C; }
  h2 { font-size: 20px; margin-top: 32px; }
  .meta { color: #666; font-size: 14px; }
  a { color: #D9661C; }
  .lang { font-size: 14px; margin-bottom: 8px; line-height: 1.9; }
  .lang a, .lang b { white-space: nowrap; margin-right: 10px; }
  .lang b { color: #222; }"""


def url(lang):
    return BASE if lang == 'en' else f'{BASE}{lang}/'


def link(href, text):
    return f'<a href="{href}">{html.escape(text)}</a>'


def page(lang):
    t = T[lang]
    yandex = 'yandex.ru' if lang == 'ru' else 'yandex.com'
    subs = {
        'app': '<b translate="no">Chrono Blocks</b>',
        'ads': '<b translate="no">Yandex Mobile Ads</b>',
        'sdk': '<b translate="no">Yandex Mobile Ads SDK</b>',
        'gp': '<b translate="no">Google Play</b>',
        'mail': link(f'mailto:{MAIL}', MAIL),
        'ya_privacy': link(f'https://{yandex}/legal/confidential/', f'{yandex}/legal/confidential'),
        'ya_terms': link(f'https://{yandex}/legal/mobileads_sdk_agreement/', f'{yandex}/legal/mobileads_sdk_agreement'),
        'g_privacy': link(f'https://policies.google.com/privacy?hl={lang}', t['g_privacy']),
    }
    f = lambda s: s.format(**subs)
    langs = ' '.join(
        f'<b lang="{code}">{name}</b>' if code == lang
        else f'<a lang="{code}" href="{url(code)}">{name}</a>'
        for code, name in LANGS.items())
    alternates = '\n'.join(
        f'<link rel="alternate" hreflang="{code}" href="{url(code)}">' for code in LANGS)
    lis = lambda items: '\n'.join(f'  <li>{f(i)}</li>' for i in items)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Chrono Blocks — {t['title']}</title>
<link rel="canonical" href="{url(lang)}">
{alternates}
<link rel="alternate" hreflang="x-default" href="{BASE}">
<style>
{CSS}
</style>
</head>
<body>
<main>
<p class="lang" translate="no">{langs}</p>
<h1><span translate="no">Chrono Blocks</span> — {t['title']}</h1>
<p class="meta">{t['dev']}: <span translate="no">Bobr Studio</span> · {t['date']}</p>

<p>{f(t['intro'])}</p>

<h2>{t['h_short']}</h2>
<p>{f(t['short'])}</p>

<h2>{t['h_stored']}</h2>
<ul>
{lis(t['stored'])}
</ul>
<p>{f(t['stored_p'])}</p>

<h2>{t['h_notif']}</h2>
<p>{f(t['notif'])}</p>

<h2>{t['h_ads']}</h2>
<p>{f(t['ads1'])}</p>
<p>{f(t['ads2'])}</p>

<h2>{t['h_purch']}</h2>
<p>{f(t['purch'])}</p>

<h2>{t['h_not']}</h2>
<ul>
{lis(t['nots'])}
</ul>

<h2>{t['h_children']}</h2>
<p>{f(t['children'])}</p>

<h2>{t['h_changes']}</h2>
<p>{f(t['changes'])}</p>

<h2>{t['h_contact']}</h2>
<p>{f(t['contact'])}</p>
</main>
</body>
</html>
"""


assert list(T) == list(LANGS), 'языки в T и LANGS должны совпадать'
keys = set(T['en'])
for lang, t in T.items():
    assert set(t) == keys, (lang, keys ^ set(t))
    out = ROOT / ('index.html' if lang == 'en' else f'{lang}/index.html')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(lang))
print('ok', len(T), 'languages →', ROOT.relative_to(ROOT.parent.parent))
