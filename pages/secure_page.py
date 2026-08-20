from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SecurePage(BasePage):
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".button.secondary.radius")
    FLASH_MESSAGE = (By.ID, "flash")

    def is_loaded(self):
        try:
            self.wait.until(EC.url_contains("/secure"))
            self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON))
            return True
        except Exception:
            return False

    def get_flash_message(self):
        return self.get_text(self.FLASH_MESSAGE)