from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys
from pages.add_to_basket_page import BasketPage


def test_fail_add_to_bascket(web_browser):
    page = BasketPage(web_browser)

    page.search_input.send_keys('xiaomi')

    page.search_input.send_keys(Keys.ENTER)

    sleep(2)

    page.good1.delete_target()

    page.good1.click()

    sleep(2)

    page.add_to_basket_btn.click()

    page.basket_icon.click()

    sleep(2)

    assert page.goods.count() != 2
