from pages.login_page import LoginPage
import allure

@allure.feature('LoginPage')
@allure.title('Check login buttons')
def test_login_exist(driver):
    login = LoginPage(driver)
    login.open()
    assert login.password_is_displayed and login.login_is_displayed and login.button_login_is_displayed

@allure.feature('LoginPage')
@allure.title('Set text in login')
def test_send_login(driver):
    login = LoginPage(driver)
    login.open()
    login.set_text_login("test@gmail.com")
    login.set_text_password("test123")
    login.button_login_click()
    with allure.step('Check result'):
        assert login.error_text == 'Your email or password is incorrect!'