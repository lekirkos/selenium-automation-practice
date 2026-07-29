# Selenium Automation Practice

This is a Selenium WebDriver + pytest practice project.

## Covered topics

- Selenium WebDriver setup
- pytest test runner
- pytest fixtures with conftest.py
- Explicit waits
- Login form automation
- Checkbox handling
- JavaScript alerts
- iframe handling
- Multiple windows/tabs
- Logging
- Screenshot on failure

## Project structure

```text
selenium_automation_practice/
  conftest.py
  test_alerts.py
  test_checkbox.py
  test_example.py
  test_iframe.py
  test_window.py
  utils/
    screenshot_utils.py
  pytest.ini
  requirements.txt
 ```


How to install: pip install -r requirements.txt

How to run all tests : pytest

How to run one test file : pytest test_alerts.py

How to run one specific testn : pytest test_alerts.py::test_alerts_page

Screenshots are automatically saved on test failure in the screenshots/ folder.

Logs are saved in test_run.log.