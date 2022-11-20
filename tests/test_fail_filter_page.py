from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys
from pages.filter_page import FilterPage


def test_fail_filter(web_browser):

    page = FilterPage(web_browser)

    page.search_input.send_keys('xiaomi')

    page.search_input.send_keys(Keys.ENTER)

    sleep(5)

    page.headphones.click()

    for good in page.goods.get_text():
        msg = 'Wrong product in filter "{}"'.format(good)

        assert 'игровая приставка' not in good.lower(), msg
