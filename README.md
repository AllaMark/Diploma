# skypro_final_kinopoisk

# Ссылка на отчёт - https://catizuoshka.yonote.ru/share/a6f10a4b-1497-4458-812e-549ae04fde03

# Ссылка на документацию - https://kinopoiskapiunofficial.tech/documentation/api/#/

# Автоматизация UI- и API‑тестов для Кинопоиска

Проект содержит набор автоматизированных тестов для проверки функциональности веб‑сайта Кинопоиска через UI и API.

### Получение API‑ключа для тестов

Для запуска API‑тестов требуется действительный API‑ключ сервиса Кинопоиск.

#### Как получить ключ:

1. Перейдите на портал: `https://kinopoiskapiunofficial.tech/documentation/api/#/`.
2. Пройдите авторизацию (https://kinopoiskapiunofficial.tech).
3. Найдите поле **API Key** или **Token**.
4. Скопируйте значение ключа. 
5. Вставить ключ в .env.

#### Настройка в проекте

1. Создать свой файл .env в корне проекта и заполнить данными по аналогии с example.env.

## Структура проекта

DIPLOMA/
page
    main_pages.py # Методы для ui
test
    test_ui.py # UI‑тесты
    test_api.py # API‑тесты
requirements.txt # Зависимости
README.md # Эта документация
pytest.ini
.gitignore
conftest.py

# Запуск тестов
## Все тесты - bash
pytest
## Только UI‑тесты - bash
pytest -m ui 
## Только API‑тесты - bash
pytest -m api 
## С подробной информацией - bash
pytest -v 

# Запуск с Allure отчетом
pytest --alluredir=allure-results -v
allure serve allure-results 

# Особенности реализации
Page Object Model — для UI‑тестов используется шаблон Page Object (pages.py).
Вспомогательные методы — API‑запросы централизованы в api_helper.py.
Allure‑отчёты — все тесты снабжены Allure‑разметкой для наглядных отчётов.
Конфигурация — тестовые данные вынесены в config.py для удобства поддержки.