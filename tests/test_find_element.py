from pages.find_element_page import FindElementPage
import allure

@allure.feature('FindElementPage')
@allure.title('Check find element buttons')
def test_find_exist(driver):
    find = FindElementPage(driver)
    find.open()
    assert find.search_is_is_displayed and find.button_is_is_displayed

@allure.feature('FindElementPage')
@allure.title('Set text find element')
def test_set_find(driver):
    find = FindElementPage(driver)
    find.open()

    find.set_text_search("Blue top")
    find.click_button()
    with allure.step('Check current url'):
        assert driver.current_url == 'https://www.automationexercise.com/products?search=Blue%20top'