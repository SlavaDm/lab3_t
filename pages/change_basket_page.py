from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class ChangeBasketPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://aliexpress.ru/'
        super().__init__(web_driver, url)

    search_input = WebElement(
        xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/input')
    good1 = WebElement(
        xpath='//*[@id="__aer_root__"]/div/div[4]/div[2]/div[2]/div/div/div/div[1]/div/div/a')
    good2 = WebElement(
        xpath='/html/body/div[1]/div/div[4]/div[2]/div[2]/div/div/div/div[2]/div/div/a')

    add_to_basket_btn = WebElement(
        xpath='/html/body/div[1]/div/div[8]/div[2]/div/div/div[3]/div[3]/div/div/div[1]/div[1]/div/button')

    goods = ManyWebElements(
        class_name='ShoppingcartItemList_ShoppingcartItemList__storeList__tbcus')

    basket_icon = WebElement(
        xpath='/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/div/nav/ul/li[3]/a')

    delete_btn2 = WebElement(
        xpath='/html/body/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div[4]/div[1]/div/button[2]')

    confirm_delete_btn2 = WebElement(
        xpath='/html/body/div[4]/div/div[2]/div[2]/button[1]')


    add_count_good1 = WebElement(xpath='/html/body/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div/div[3]/div/div[4]/div[2]/div[1]/div/div/button[2]')

    input_good1 = WebElement(xpath='/html/body/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div/div[3]/div/div[4]/div[2]/div[1]/div/div/input')
    
    delete_count_good1 = WebElement(xpath='/html/body/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div/div[3]/div/div[4]/div[2]/div[1]/div/div/button[1]')