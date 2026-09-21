from .base_page import BasePage
from selenium.webdriver.common.by import By
from allure import step

search_selector = (By.ID, 'search_product')
button_selector = (By.ID, 'submit_search')

class FindElementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        with step('Open browser'):
            self.driver.get('https://www.automationexercise.com/products')

    @property
    def search(self):
        return self.find(search_selector)
    
    @property
    def search_is_is_displayed(self):
        with step('Check the search is displayed'):
            return self.search.is_displayed()

    @property
    def button(self):
        return self.find(button_selector)
    
    @property
    def button_is_is_displayed(self):
        with step('Check the button is displayed'):
            return self.button.is_displayed()

    def set_text_search(self, text : str):
        with step('Set text in search'):
            self.search.send_keys(text)

    def click_button(self):
        with step('Click the button'):
            self.button.click()