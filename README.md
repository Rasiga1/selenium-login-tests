# Selenium UI-тесты для сайта авторизации

## 📌 Описание

UI-тесты для сайта: https://berpress.github.io/selenium-login-demo/  
Используется Python + Selenium + pytest.  

## ✅ Тесты

- Успешный вход с логином `admin` и паролем `password`
- Ошибка при неверном логине
- Ошибка при неверном пароле

## 🚀 Установка и запуск

```bash
git clone https://github.com/ВАШ_НИК/selenium-login-tests.git
cd selenium-login-tests
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## 🔐 Валидные данные

- Логин: `admin`
- Пароль: `password`
