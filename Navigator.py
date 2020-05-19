from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


from LoginPage import *
from AddTestPlanPage import *
from SelectCasePage import *
from TestRunAndTestResult import *

class Navigator:
    __loginPage = None
    __addTestPlanPage = None
    __selectCasePage = None
    __testRunAndTestResult = None


    def __init__( self, browser ):
        self.browser = browser

    def loginPage(self):
        if self.__loginPage == None:
            return LoginPage( self.browser )

        return self.__loginPage

    def addTestPlanPage(self):
        if self.__addTestPlanPage == None:
            return AddTestPlanPage( self.browser )

        return self.__addTestPlanPage

    def selectCasePage(self):
        if self.__selectCasePage == None:
            return SelectCasePage( self.browser )

        return self.__selectCasePage

    def testRunAndTestResult(self):
        if self.__testRunAndTestResult == None:
            return TestRunAndTestResult( self.browser )

        return self.__testRunAndTestResult