# Saucedemo Selenium Pytest Framework

Автоматизація UI-тестування для навчального інтернет-магазину [SauceDemo](https://saucedemo.com) з використанням Python, Selenium WebDriver та тестового фреймворку Pytest.

## 🚀 Стек технологій
* **Мова програмування:** Python 3.x
* **Тестування UI:** Selenium WebDriver
* **Фреймворк тестування:** Pytest
* **Паттерн проектування:** Page Object Model (POM)
* **Звітність:** Allure Report (allure-pytest)

## 📁 Структура проекту
```text
saucedemo-selenium-pytest-framework/
│
├── pages/          # Класи сторінок (Page Objects), що інкапсулюють логіку UI
├── tests/          # Тест-кейси та сценарії перевірки функціоналу
├── conftest.py     # Конфігурація Pytest: ініціалізація та налаштування драйвера
├── .gitignore      # Виключення системних файлів та логів з Git
└── README.md       # Документація проекту
```

## 🛠️ Встановлення та запуск

### 1. Клонування репозиторію
```bash
git clone https://github.com
cd saucedemo-selenium-pytest-framework
```

### 2. Налаштування віртуального оточення
```bash
# Створення оточення
python -m venv venv

# Активація оточення (Windows)
venv\Scripts\activate

# Активація оточення (Linux/macOS)
source venv/bin/activate
```

### 3. Встановлення залежностей
Переконайтеся, що у вас встановлені `pytest`, `selenium` та `allure-pytest`:
```bash
pip install pytest selenium allure-pytest
```

### 4. Запуск тестів із генерацією Allure-звітів
Запустіть тести та вкажіть папку для збору артефактів Allure:
```bash
pytest --alluredir results
```

### 5. Перегляд звіту
Для візуалізації результатів тестів (необхідно мати локально встановлений Allure CLI):
```bash
allure serve results
```
