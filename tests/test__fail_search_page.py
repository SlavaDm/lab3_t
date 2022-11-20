from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys
from pages.search_page import SearchPage


def test_fail_search(web_browser):

    page = SearchPage(web_browser)

    page.search_input.send_keys('xiaomi')

    page.search_input.send_keys(Keys.ENTER)

    assert page.goods.count() != 0

    sleep(2)

    for good in page.goods.get_text():
        msg = 'Wrong product in search "{}"'.format(good)
        assert 'apple' not in good.lower(), msg
