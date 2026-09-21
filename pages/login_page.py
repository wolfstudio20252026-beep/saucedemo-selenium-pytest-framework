from .base_page import BasePage
from selenium.webdriver.common.by import By
from allure import step

login_selector = (By.CSS_SELECTOR, 'input[data-qa="login-email"]')
password_selector = (By.CSS_SELECTOR, 'input[data-qa="login-password"]')
button_selector = (By.CLASS_NAME, 'btn-default')
error_selector = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/p')

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        with step('Open browser'):
            self.driver.get('https://www.automationexercise.com/login')

    def login(self):
        return self.find(login_selector)

    def button_login(self):
        return self.find(button_selector)

    def password(self):
        return self.find(password_selector)

    @property
    def login_is_displayed(self):
        with step('Check the login is displayed'):
            return self.login().is_displayed()

    @property
    def button_login_is_displayed(self):
        with step('Check the button login is displayed'):
            return self.button_login().is_displayed()

    def button_login_click(self):
        with step('Click the button login'):
            self.button_login().click()

    @property
    def password_is_displayed(self):
        with step('Check the password is displayed'):
            return self.password().is_displayed()
    
    def set_text_login(self, text: str):
        with step('Set text in login'):
            self.login().send_keys(text)

    def set_text_password(self, text: str):
        with step('Set text in password'):
            self.password().send_keys(text)

    @property
    def error_text(self):
        with step('Get error text'):
            return self.find(error_selector).text


    