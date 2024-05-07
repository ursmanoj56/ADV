import pytest

from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtilities import get_data_from_excel


class TestLogin(BaseTest):
    def test_valid_login(self):
        self.loginpage= LoginPage(self.driver)
        self.loginpage.login("admin@admin.com","admin@123")

    @pytest.mark.parametrize("username,password",get_data_from_excel("TestFiles/ADVlogin.xlsx", "LoginTest"))
    def test_invalid_login(self,username,password):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login(username,password)
        message=self.loginpage.error_message()
        assert message.__contains__("Please, enter valid credentials.")