from utilities import custom_logger as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _search_box = "//form[@id='search']//input[@id='search']"
    _search_button = "//form[@id='search']//button[@class='find-course search-course']"
    _course_tile = "//h4[contains(text(),'{0}')]/.." #needs .format() to insert course name title
    _enroll_in_course_button = "//button[@data-uniqid='1595290194536']"
    _all_courses_link = "//div[@id='navbar-inverse-collapse']/ul//a[@href='/courses']"
    _cc_num = "//input[@name='cardnumber']"
    _card_number_frame = "__privateStripeFrame8155"
    _cc_exp = "//input[@name='exp-date']"
    _expiry_date_frame = "__privateStripeFrame8157"
    _cc_cvv= "//input[@name='cvc']"
    _security_code_frame = "__privateStripeFrame8156"
    _country_select = "//select[@name='country-list']"
    _buy_button = "//div[@class='panel payment-panel']/div/div[1]/div[@class='row']/div[@class='col-xs-12']/button[1]"
    _declined_message = "//form[@id='checkout-form']//div[@class='panel payment-panel']/div//div[@class='card-errors has-error']/ul[@class='list-unstyled']/li[@class='card-no cvc expiry text-danger']/span"

    # For work in iFrames
    # self.driver.switch_to.frame(frame_reference=self.driver.find_element_by_xpath(x‌​path="//iframe[@__privateStripeFrame5']"))

    # ------------- Actions ---------------------------------

    def enterCourseName(self, course):
        self.sendKeys(course, self._search_box, locatorType="xpath")

    def clickSearchButton(self):
        self.elementClick(self._search_button, locatorType="xpath")

    def clickCourseToEnroll(self, coursename):
        tileElement = self._course_tile.format(coursename)
        self.elementClick(tileElement, locatorType="xpath")

    def clickEnrollButton(self):
        self.elementClick(self._enroll_in_course_button, locatorType="xpath")

    def enterCardNum(self, num):
        # self.switchToFrame(name=self._card_number_frame)
        self.switchToFrame(index=0)
        self.sendKeys(num, self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        # self.switchToFrame(name=self._expiry_date_frame)
        self.switchToFrame(index=1)
        self.sendKeys(exp, self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(name=self._security_code_frame)
        self.switchToFrame(index=2)
        self.sendKeys(cvv, self._cc_cvv, locatorType="xpath")
        self.switchToDefaultContent()

    def selectCountry(self, country):
        self.selectValue(country, self._country_select, locatorType="xpath")

    def clickBuyButton(self):
        self.elementClick(self._buy_button, locatorType="xpath")

    def clickAllCourses(self):
        self.elementClick(self._all_courses_link, locatorType="xpath")

    # ------------- Functionality -----------------------------

    def enterCreditCardInfo(self, num, exp, cvv, country):
        self.selectCountry(country)
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        time.sleep(2)

    def selectCourseToEnroll(self, courseName=""):
        self.enterCourseName(courseName)
        self.clickSearchButton()
        time.sleep(2)
        self.clickCourseToEnroll(courseName)

    def enrollCourse(self, num="", exp="", cvv="", country="United States"):
        self.clickEnrollButton()
        self.webScroll("down")
        self.enterCreditCardInfo(num, exp, cvv, country)
        self.clickBuyButton()

    def verifyEnrollFail(self, message):
        self.isElementDisplayed(self._declined_message, locatorType="xpath")
        text = self.getText(self._declined_message, locatorType="xpath")
        if message in text:
            return True
        else:
            return False




