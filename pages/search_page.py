from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class SearchPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://aliexpress.ru/'
        super().__init__(web_driver, url)

    search_input = WebElement(
        xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/input')

    goods = ManyWebElements(
        class_name="product-snippet_ProductSnippet__content__1ettdy")
