import csv
import pytest
from pages.login_page import LoginPage


def read_login_data():
    test_data = []

    with open("test_data/login_data.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            test_data.append((
                row["username"],
                row["password"],
                row["expected_message"]
            ))

    return test_data


@pytest.mark.parametrize("username,password,expected_message", read_login_data())
def test_login_with_csv_data(driver, username, password, expected_message):
    login_page = LoginPage(driver)

    login_page.login(username, password)

    assert expected_message in login_page.get_flash_message()