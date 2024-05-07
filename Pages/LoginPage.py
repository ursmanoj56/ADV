from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    USER_NAME=(By.NAME,"email")
    PASSWORD=(By.NAME,"password")
    LOGIN_BUTTON=(By.ID,"kt_sign_in_submit")
    ERROR_MESSAGE=(By.XPATH,"//p[text()='Please, enter valid credentials.']")

    def __init__(self,driver):
        super().__init__(driver)


    def login(self,username,password):
        self.text_input(self.USER_NAME,username)
        self.text_input(self.PASSWORD,password)
        self.click_button(self.LOGIN_BUTTON)
        return HomePage(self.driver)

    def error_message(self):

        return self.get_text(self.ERROR_MESSAGE)