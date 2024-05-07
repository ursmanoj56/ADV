from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.ConfigPage import ConfigPage


class HomePage(BasePage):
    USER_ICON = (By.XPATH, "(//div[@class='menu-item'])[6]")
    ADDUSER_ICON = (By.XPATH, "(//button[@type='button'])[1]")
    EMAIL = (By.NAME, "email")
    NAME = (By.NAME, "name")
    FIRST_NAME = (By.NAME, "first_name")
    LAST_NAME = (By.NAME, "last_name")
    SUMIT_BUTTON = (By.XPATH, "(//button[@type='submit'])[1]")
    ERROR_MESSAGE = (By.XPATH, "//span[text()='Email already Available']")
    LIST_USER = (By.XPATH, "(//div[@class='d-flex flex-column'])[2]")
    SELECT = (By.ID, "react-select-2-input")
    REVIEWER_BUTTON = (By.XPATH, "//input[@value='Reviewer']")
    CONFIG_ICON =(By.XPATH, "//span[text()='Configuration']")

    def __init__(self, driver):
        super().__init__(driver)

    def submit_adminform(self, email, name, firstname, lastname):
        self.click_button(self.USER_ICON)
        self.click_button(self.ADDUSER_ICON)
        self.text_input(self.EMAIL, email)
        self.text_input(self.NAME, name)
        self.text_input(self.FIRST_NAME, firstname)
        self.text_input(self.LAST_NAME, lastname)
        self.scroll_into_view(self.SUMIT_BUTTON)
        self.click_button(self.SUMIT_BUTTON)

    def search_user(self):

        return self.get_text(self.LIST_USER)

    def submit_reviewver(self,email,name,firstname,lastname,input):
        self.click_button(self.USER_ICON)
        self.click_button(self.ADDUSER_ICON)
        self.text_input(self.EMAIL, email)
        self.text_input(self.NAME, name)
        self.text_input(self.FIRST_NAME, firstname)
        self.text_input(self.LAST_NAME, lastname)
        self.click_button(self.REVIEWER_BUTTON)
        self.scroll_into_view(self.SUMIT_BUTTON)
        self.click_button(self.SELECT)
        self.text_inputs(self.SELECT,input)
        self.press_enter()
        self.click_button(self.SUMIT_BUTTON)

    def warn_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def config_icon_displayed(self):
        self.is_diplayed(self.CONFIG_ICON)

    def click_config_icon(self):
        self.click_button(self.CONFIG_ICON)
        return ConfigPage(self.driver)
