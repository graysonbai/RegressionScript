from component.BasicButton import *


class TestRunAndTestResult:

    def __init__( self, browser ):
        self.browser = browser
        self.label = "TestRunAndTestResult"

    def addTestPlan( self ):
        return BasicButton( self.label + " > addTestPlan", lambda :self.browser.find_element_by_xpath( "//a[@id='navigation-plans-add']/span" ) )

    def testRunAndTestResultLink(self):
        return BasicButton( self.label + " > testRunAndTestResultLink", lambda :"navigation-runs" )