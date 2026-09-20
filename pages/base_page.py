from selenium import webdriver
class BasePage:
    def __init__(self, driver : webdriver.Chrome):
        self.driver = driver

    def find(self, args):
        return self.driver.find_element(*args)