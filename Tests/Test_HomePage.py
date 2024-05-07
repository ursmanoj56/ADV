import time

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest


class TestHomePage(BaseTest):
    def test_adminRegister(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.login("admin@admin.com", "admin@123")
        homepage=self.loginpage.login("admin@admin.com", "admin@123")
        homepage.submit_adminform("vijay@gmail.com","vijay","prasad","pras")
        time.sleep(10)
        message=homepage.search_user()
        assert message.__contains__("vijay@gmail.com")

    def test_dubplicate_admin(self):
        self.test_adminRegister()
        self.homepage=HomePage(self.driver)
        message=self.homepage.warn_message()
        assert message.__contains__("Email already Available")

    def test_reviwer_reg(self):
        self.loginpage=LoginPage(self.driver)
        homepage = self.loginpage.login("admin@admin.com", "admin@123")
        homepage.submit_reviewver("siva@gmail.com","siva","sivakumar","kumar","PROJECT0002")
        time.sleep(10)
        message=homepage.search_user()
        assert message.__contains__("siva@gmail.com")

    def test_duplicate_reviwer(self):
        self.test_reviwer_reg()
        self.homepage=HomePage(self.driver)
        message = self.homepage.warn_message()
        assert message.__contains__("Email already Available")

    def test_config_displayed(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.login("admin@admin.com", "admin@123")
        homepage.config_icon_displayed()




