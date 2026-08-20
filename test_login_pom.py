from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def test_valid_login_with_pom(driver):
    login_page = LoginPage(driver)
    secure_page = SecurePage(driver)

    login_page.login("tomsmith", "SuperSecretPassword!")

    assert secure_page.is_loaded()
    assert "You logged into a secure area!" in secure_page.get_flash_message()


def test_invalid_login_with_pom(driver):
    login_page = LoginPage(driver)

    login_page.login("wronguser", "SuperSecretPassword!")

    assert "Your username is invalid!" in login_page.get_flash_message()