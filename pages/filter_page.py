from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class FilterPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://aliexpress.ru/'
        super().__init__(web_driver, url)

    search_input = WebElement(
        xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/input')

    headphones = WebElement(
        xpath='/html/body/div[1]/div/div[4]/div[2]/div[1]/div/div[3]/div/div[4]/ul/li[2]/div/ul/li[1]/a')
    
    goods = ManyWebElements(
        class_name="product-snippet_ProductSnippet__name__1ettdy")
