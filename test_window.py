from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_window_page(driver):
    wait = WebDriverWait(driver, 15)

    driver.get("https://the-internet.herokuapp.com/windows")

    main_window = driver.current_window_handle

    driver.find_element(By.XPATH, '//*[text()="Click Here"]').click()

    wait.until(EC.number_of_windows_to_be(2))

    all_handles = driver.window_handles

    new_window = [handle for handle in all_handles if handle != main_window][0]

    driver.switch_to.window(new_window)

    assert "New Window" in driver.title

    driver.close()

    driver.switch_to.window(main_window)