from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys
from pages.filter_page import FilterPage


def test_filter(web_browser):

    page = FilterPage(web_browser)

    page.search_input.send_keys('xiaomi')

    page.search_input.send_keys(Keys.ENTER)

    sleep(2)

    page.headphones.click()

    sleep(2)

    for good in page.goods.get_text():
        msg = 'Wrong product in filter "{}"'.format(good)

        assert 'наушники' in good.lower(), msg
