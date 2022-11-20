from pages.base import WebPage
from pages.elements import WebElement


class NavigationPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://aliexpress.ru/'
        super().__init__(web_driver, url)

    products = WebElement(
        xpath='/html/body/div/div/div[7]/div/div/div/div[1]/div/ul/li[2]/a'
    )

    appliances = WebElement(
        xpath='/html/body/div/div/div[7]/div/div/div/div[1]/div/ul/li[3]/a')

    computers = WebElement(
        xpath='/html/body/div/div/div[7]/div/div/div/div[1]/div/ul/li[4]/a')

    build = WebElement(
        xpath='/html/body/div/div/div[7]/div/div/div/div[1]/div/ul/li[5]/a')

    home = WebElement(
        xpath='/html/body/div/div/div[7]/div/div/div/div[1]/div/ul/li[6]/a')

    sport = WebElement(
        xpath='/html/body/div/div/div[7]/div/div/div/div[1]/div/ul/li[7]/a')

    games = WebElement(
        xpath='/html/body/div/div/div[7]/div/div/div/div[1]/div/ul/li[9]/a')

