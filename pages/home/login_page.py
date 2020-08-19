from utilities import custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = ".//a[text()='Sign In']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "input[value='Login']"

    # ------------- Actions ---------------------------------

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="css")

    # ------------- Functionality -----------------------------

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def clearFields(self):
        emailField = self.getElement(self._email_field)
        emailField.clear()
        passwordField = self.getElement(self._password_field)
        passwordField.clear()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(".//button[@id='dropdownMenu1']/img",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        self.waitForElement(".//span[@class='dynamic-text help-block']", locatorType="xpath")
        result = self.isElementPresent(".//span[@class='dynamic-text help-block']",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Google")
