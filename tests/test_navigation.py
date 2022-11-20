from time import sleep
import pytest
from pages.navigation_page import NavigationPage


def test_navigation(web_browser):
    page = NavigationPage(web_browser)
    page.products.click()
    assert page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000001/food.html')
    sleep(2)
    page.go_back()
    page.appliances.click()
    sleep(2)
    assert page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000005/home-appliances.html')
    page.go_back()
    page.computers.click()
    sleep(2)
    assert page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000006/computer-office.html')
    page.go_back()
    page.build.click()
    sleep(2)
    assert page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000007/home-improvement.html')
    page.go_back()
    page.home.click()
    sleep(2)
    assert page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000008/home-garden.html')
    page.go_back()
    page.sport.click()
    sleep(2)
    assert page.get_current_url().startswith(
        'https://aliexpress.ru/category/202000010/sports-entertainment.html')
