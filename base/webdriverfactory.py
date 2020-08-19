"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on the browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    """
        Set Chrome driver and iexplorer environment based on OS
        
        chromedriver = "C:/.../chromedriver.exe
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        
        PREFERRED: Set the path on the machine to where the browser will be executed
    """
    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseUrl = "https://courses.letskodeit.com/"
        if self.browser == "iexplorer":
            # Set IE driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)
        return driver
