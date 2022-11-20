from time import sleep
import pytest
from pages.auth_page import AuthPage


def test_authorisation(web_browser):

    page = AuthPage(web_browser)

    page.email.send_keys('mylogin')

    page.password.send_keys("mypassword")

    page.btn.click()

    sleep(2)

    assert page.get_current_url() == 'https://aliexpress.ru/'
