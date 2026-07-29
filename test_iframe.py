from selenium.webdriver.common.by import By


def test_iframe_page(driver):
    driver.get("https://the-internet.herokuapp.com/iframe")

    iframe = driver.find_element(By.ID, "mce_0_ifr")
    driver.switch_to.frame(iframe)

    body = driver.find_element(By.ID, "tinymce")

    assert body is not None

    driver.switch_to.default_content()

    heading = driver.find_element(By.TAG_NAME, "h3").text
    assert "An iFrame containing" in heading