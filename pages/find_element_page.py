from .base_page import BasePage
from selenium.webdriver.common.by import By

search_selector = (By.ID, 'search_product')
button_selector = (By.ID, 'submit_search')

class FindElementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://www.automationexercise.com/products')

    @property
    def search(self):
        return self.find(search_selector)
    
    @property
    def search_is_is_displayed(self):
        return self.search.is_displayed()

    @property
    def button(self):
        return self.find(button_selector)
    
    @property
    def button_is_is_displayed(self):
        return self.button.is_displayed()

    def set_text_search(self, text : str):
        self.search.send_keys(text)

    def click_button(self):
        self.button.click()    