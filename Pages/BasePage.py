from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def text_input(self, locator,text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.clear()
        element.send_keys(text)

    def text_inputs(self, locator,text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.send_keys(text)

    def click_button(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def get_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def is_diplayed(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.is_displayed()

    def scroll_into_view(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def select_dropdown_option_by_visible_text(self, locator, option_text):
        dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        dropdown_select = Select(dropdown)
        dropdown_select.select_by_visible_text(option_text)

    def select_dropdown_option_by_index(self, locator, index):
        dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        dropdown_select = Select(dropdown)
        dropdown_select.select_by_index(index)

    def select_dropdown_option_by_value(self, locator, value):
        dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        dropdown_select = Select(dropdown)
        dropdown_select.select_by_value(value)

    def press_enter(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()