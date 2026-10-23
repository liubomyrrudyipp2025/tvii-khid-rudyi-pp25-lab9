# Твій Хід — ЛР8

Навчальний frontend-прототип підбору настільних ігор.
Автор: Рудий Л. Д., ПП-25. Лабораторна робота №8: Git, GitHub та деплой.

## Демонстрація

- GitHub Pages: https://liubomyrrudyipp2025.github.io/tvii-khid-rudyi-pp25-lab8/
- Netlify: https://tvii-khid-rudyi-pp25-lab8.netlify.app/

## Технології та запуск

Семантичний HTML5, CSS, JavaScript, Tailwind CSS 3.4.17.
Для збірки потрібен Node.js >=18; у Netlify використовується Node.js 22.

```bash
npm ci
npm run package:dist
python -m http.server 5503 --directory dist
```

Відкрийте http://127.0.0.1:5503/. Для тестів потрібен Python >=3.11:

```bash
python -m unittest discover -s tests -v
```

Перевірка перед push: тести Python, npm run package:dist та git status.

## Публікація

GitHub Pages: main /root, без обробки Jekyll (.nojekyll).
Netlify: main, команда npm run package:dist, каталог dist (netlify.toml).
Пакувальник scripts/package-dist.cjs копіює лише runtime-ресурси.
Шляхи відносні: сайт працює також під префіксом назви репозиторію.
Time.is працює в opaque sandbox allow-scripts allow-popups; Netlify _headers
зберігає правильний MIME для widgets/clock.shtml.

## Межі демонстрації

Доступний лише початок квізу: вибір компанії або подарунка.
Замовлення, оплата, доставка та підписка не реалізовані. Карта — демонстраційна
локація, а не адреса магазину; автор YouTube-відео не є партнером проєкту.
Hero починається з фото; відео завантажується лише після вибору «Відео».

## Ресурси й приватність

Навчальні графічні та відеоматеріали успадковані з попередніх лабораторних.
Ліцензії сторонніх шрифтів та іконок збережені поряд з відповідними assets.
Звіти, чати, приватні джерела та облікові дані не входять до репозиторію.

## Навчальний Git workflow

Гілки та конфлікт README демонструються одним автором у контрольованому
навчальному сценарії. Два власні клони показують справжній push/pull;
це не твердження про спільну роботу з одногрупниками.

Після push у main обидва хостинги автоматично публікують нову версію.
