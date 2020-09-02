from pages.courses.register_courses_page import RegisterCoursesPage
import unittest
import pytest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enrollCourse(course="JavaScript", num="5105105105105100", exp="12/25", cvv="123")
        failureMessage = "Your card has been declined."
        result = self.courses.verifyEnrollFail(failureMessage)
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment failed due to invalid CC number")

