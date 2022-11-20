from time import sleep
import pytest
from pages.auth_page import AuthPage


def test_fail_authorisation(web_browser):

    page = AuthPage(web_browser)

    page.email.send_keys('user555')

    page.password.send_keys("user555")

    page.btn.click()

    sleep(2)

    assert page.get_current_url() != 'https://aliexpress.ru/'
