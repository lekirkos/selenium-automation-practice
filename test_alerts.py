import logging
from utils.screenshot_utils import take_screenshot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

def test_alerts_page(driver):
    wait = WebDriverWait(driver, 15)

    try:

        logger.info("test starts")
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        JSAlert = driver.find_element(By.CSS_SELECTOR, 'button[onclick="jsAlert()"]')

        JSAlert.click()

        logger.info("click JSAlert button")

        alert = wait.until(EC.alert_is_present())
        logger.info("accept the alert")

        assert "I am a JS Alert" in alert.text
        alert.accept()

        assert "You successfully clicked an alert" in driver.find_element(By.ID, "result").text

    except Exception as e:
        screenshot = take_screenshot(driver, "test_alerts_page")
        logger.error(f"Test failed. Screenshot saved: {screenshot}")
        raise e
