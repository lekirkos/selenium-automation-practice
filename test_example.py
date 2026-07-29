from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_example_page(driver):
    wait = WebDriverWait(driver, 15)


    driver.get("https://the-internet.herokuapp.com/login")
    assert driver.current_url == "https://the-internet.herokuapp.com/login"
    assert driver.title == "The Internet"

    username = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )

    login =  wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )


    username.clear()
    username.send_keys("tomsmith")

    password.clear()
    password.send_keys("SuperSecretPassword!")

    login.click()


    wait.until(
        EC.url_to_be("https://the-internet.herokuapp.com/secure")
    )
    assert driver.current_url == "https://the-internet.herokuapp.com/secure"
    wait.until(
        EC.text_to_be_present_in_element((By.ID, "flash"), "You logged into a secure area!"
        )
    )
    message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in message
