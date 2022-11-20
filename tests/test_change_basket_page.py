from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys
from pages.change_basket_page import ChangeBasketPage


def test_change_bascket(web_browser):
    page = ChangeBasketPage(web_browser)
    page.search_input.send_keys('xiaomi')
    page.search_input.send_keys(Keys.ENTER)
    sleep(2)

    page.good1.delete_target()
    page.good1.click()
    sleep(2)

    page.add_to_basket_btn.click()
    page.go_back()
    sleep(2)

    page.good2.delete_target()
    page.good2.click()
    sleep(2)
    page.add_to_basket_btn.click()

    sleep(2)
    page.basket_icon.click()
    sleep(2)

    page.delete_btn2.click()

    sleep(1)
    page.confirm_delete_btn2.click()
    sleep(2)

    assert page.goods.count() == 1
    page.add_count_good1.click()
    sleep(1)

    page.add_count_good1.click()
    sleep(1)

    assert page.input_good1.get_value_attribute() == '3'

    page.delete_count_good1.click()
    sleep(1)

    page.delete_count_good1.click()
    sleep(1)

    assert page.input_good1.get_value_attribute() == '1'
