# Selenium Automation Practice

This repository contains Selenium automation practice tests written in Python with pytest.

The project was created while learning Selenium basics, pytest fixtures, browser interactions, screenshots on failure, Page Object Model, and simple data-driven testing with CSV.

## Technologies Used

- Python
- Selenium WebDriver
- pytest
- webdriver-manager

## Project Structure

```text
selenium_automation_practice/
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── secure_page.py
├── test_data/
│   └── login_data.csv
├── utils/
├── screenshots/
├── conftest.py
├── test_alerts.py
├── test_checkbox.py
├── test_example.py
├── test_iframe.py
├── test_login_ddt.py
├── test_login_pom.py
├── test_window.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Test Coverage

This project includes practice tests for common Selenium actions and browser behavior.

Covered examples include:

- Basic page navigation
- Element selection
- Form input
- Checkboxes
- Alerts
- Iframes
- Browser windows
- Screenshots on test failure
- Login testing with Page Object Model
- Data-driven login testing with CSV

## Page Object Model Practice

The project includes a simple Page Object Model structure:

```text
pages/
├── base_page.py
├── login_page.py
└── secure_page.py
```

### `base_page.py`

Contains common reusable Selenium helper methods, such as:

- click
- type text
- get text
- check element visibility

### `login_page.py`

Contains the login page locators and login actions for:

```text
https://the-internet.herokuapp.com/login
```

### `secure_page.py`

Contains checks for the secure area after a successful login.

This keeps Selenium locators and page actions separate from the test files.

## Data-Driven Testing Practice

The project also includes a simple CSV-based data-driven login test.

Test data is stored in:

```text
test_data/login_data.csv
```

Example scenarios:

- Valid login
- Invalid username
- Invalid password

The same test logic runs with multiple username and password combinations from the CSV file.

## How to Install

Create and activate a virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run Tests

Run all tests:

```bash
pytest
```

Run only the Page Object Model login tests:

```bash
pytest test_login_pom.py
```

Run only the data-driven login tests:

```bash
pytest test_login_ddt.py
```

Run both new Module 6 practice tests:

```bash
pytest test_login_pom.py test_login_ddt.py
```

## Example Successful Run

```text
test_login_pom.py .. 
test_login_ddt.py ...

5 passed
```

## What This Project Demonstrates

This repository shows practice with Selenium automation concepts, including:

- Selenium WebDriver basics
- pytest fixtures
- Browser setup with webdriver-manager
- Screenshots on failed tests
- Page Object Model basics
- Explicit waits
- Reusable page methods
- CSV-based data-driven testing
- Basic project organization

## Notes

This is a learning/practice project, not a full production automation framework.

The following folders/files are excluded from Git using `.gitignore`:

```text
.venv/
__pycache__/
.pytest_cache/
.idea/
screenshots/
*.log
```