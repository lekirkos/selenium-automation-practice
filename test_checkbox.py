from selenium.webdriver.common.by import By


def test_checkbox_page(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')

    checkbox1 = checkboxes[0]
    checkbox2 = checkboxes[1]

    if not checkbox1.is_selected():
        checkbox1.click()

    assert checkbox2.is_selected()

    if checkbox2.is_selected():
        checkbox2.click()

    assert checkbox2.is_selected() == False