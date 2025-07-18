
# Selenium Login Tests

Этот репозиторий содержит автоматизированные тесты для проверки формы входа на сайте с использованием библиотеки Selenium.

## Описание

Проект предназначен для демонстрации использования Selenium для автоматизации тестирования веб-форм. В проекте используется ChromeDriver для взаимодействия с браузером Google Chrome.

## Структура проекта

1. **tests/** - директория с тестами.
   - **test_login.py** - тесты для проверки входа на сайт с правильными и неправильными данными.
2. **conftest.py** - настройки для тестов, включая драйвер и другие параметры.
3. **requirements.txt** - список зависимостей для проекта.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/rasiga1/selenium-login-tests.git


2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```
3. Убедитесь, что у вас установлен Chrome и подходящий ChromeDriver.

## Запуск тестов

Для запуска тестов используйте команду:

```bash
pytest -v
```

## Примечания

* Для тестов используется явное ожидание элементов на странице.
* В случае ошибок, связанных с отсутствием элемента на странице, тесты будут завершаться с ошибкой.
* Пожалуйста, убедитесь, что браузер и драйвер совместимы.

## Ожидаемые результаты

1. **test\_successful\_login**:

   * При успешном вводе правильных данных ("admin" и "password") должен быть произведен вход и отображено сообщение о успешном входе.

2. **test\_invalid\_login**:

   * При введении неверных данных ("wrong" и "wrong") должно появиться сообщение об ошибке.

## Тестовые данные

* Валидные:

  * Логин: `admin`
  * Пароль: `password`
* Невалидные:

  * Любые другие комбинации (например, `admin` / `wrongpass`)

## Возможные проблемы

1. Сайт не открывается — проверьте интернет и доступность демо-страницы.
2. Chrome и ChromeDriver несовместимы — обновите один из них.
3. Хотите видеть, как проходят тесты:

   * Откройте `conftest.py`.
   * Удалите или закомментируйте `--headless` в настройках браузера. 
