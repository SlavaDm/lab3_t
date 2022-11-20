from time import sleep
import pytest
from pages.navigation_page import NavigationPage


def test_navigation(web_browser):

    page = NavigationPage(web_browser)

    page.games.click()

    sleep(2)

    assert not page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000001/food.html')

    assert not page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000001/food.html')

    assert not page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000005/home-appliances.html')

    assert not page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000006/computer-office.html')

    assert not page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000007/home-improvement.html')

    assert not page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000008/home-garden.html')

    assert not page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000010/sports-entertainment.html')
