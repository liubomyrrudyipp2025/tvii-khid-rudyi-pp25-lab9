# Твій Хід — ЛР9

Рудий Л. Д., ПП-25. Навчальна адаптивна форма зворотного зв’язку та клієнтська валідація. Окрема копія перевіреної ЛР8.

## Реалізовано

Семантичні HTML-поля, mobile-first Tailwind CSS 3.4.17, п’ять чистих валідаторів, normal/focus/error/success, blur/input/change/submit та IME. Нативний success dialog підтримує Tab/Shift+Tab, Escape, повернення фокуса та reset. Статичні слоти повідомлень запобігають зсуву цілі кліку.

## Локальний запуск

Потрібні Node.js >=18 із npm та Python >=3.11. Потрібен браузер з `Intl.Segmenter` і нативним `dialog.showModal()`. Фактично перевірено Chromium 156.0.8078.48 (Brave); старіші браузери не перевірялися. У VS Code налаштовано Live Server на порт 5509. Для зібраного результату:

```bash
npm ci
npm run package:dist
python -m http.server 5509 --bind 127.0.0.1 --directory dist
```

Відкрити `http://127.0.0.1:5509/#feedback`.

```bash
python -m unittest discover -s tests -v
node --test tests/validation.test.cjs
```

Пакувальник копіює лише runtime-allowlist, зокрема `js/validation.js`. Звіти, чати, джерела методички й приватні докази не входять до сайту.

## Правила та приватність

Ім’я: 2–100 видимих Unicode-символів; email: ASCII dot-atom із перевіркою структури й довжини; телефон: буквально `+380` і дев’ять ASCII-цифр без trim чи маски; повідомлення: 10–2000 видимих символів; згода обов’язкова. Ім’я й повідомлення рахуються графемами, а не UTF-16 одиницями.

Використовуйте тільки вигадані дані. Немає backend/API, надсилання, зберігання чи журналювання введених значень. Успішний діалог прямо повідомляє, що дані не надсилалися; поля очищуються. Для майбутнього справжнього сервісу клієнтська перевірка не замінює серверну.

Успадкований квіз має лише початковий вибір; замовлення, оплата, доставка й підписка відсутні. Карта, YouTube та Time.is — окремі сторонні embeds із власними мережевими запитами, а не submission форми. Sandbox годинника не послаблено. Ліцензії ресурсів збережені в assets.

## Публікація

Публічний репозиторій: https://github.com/liubomyrrudyipp2025/tvii-khid-rudyi-pp25-lab9

Production-сайт: https://tvii-khid-rudyi-pp25-lab9.vercel.app/

Vercel підключено до гілки `main` цього репозиторію. Налаштування: Application Preset `Other`, Root Directory `./`, Install Command `npm ci`, Build Command `npm run package:dist`, Output Directory `dist`. Публікується лише runtime-allowlist; документація, тести та приватні матеріали не є частиною сайту. Для оновлення production використовується Git push із наступною успішною збіркою.
