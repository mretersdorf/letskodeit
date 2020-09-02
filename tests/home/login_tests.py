from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        result1 = self.lp.verifyPageTitle()
        self.ts.mark(result1, "Title Verification Failed")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was not successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        result = self.lp.verifyLoginFailed()
        assert result == True
