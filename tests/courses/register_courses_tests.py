from pages.courses.register_courses_page import RegisterCoursesPage
import unittest
import pytest
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "5105105105105100", "12/25", "123"), ("Learn Python 3 from scratch", "5105105105105100", "12/25", "123"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.selectCourseToEnroll(courseName=courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        failureMessage = "Your card was declined. Your request was in live mode, but used a known test card."
        result = self.courses.verifyEnrollFail(failureMessage)
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment failed due to invalid CC number")
        self.courses.clickAllCourses()


