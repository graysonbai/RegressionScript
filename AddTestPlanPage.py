from component.BasicTextField import *
from component.SelectWindow import *
from component.BasicButton import *


class AddTestPlanPage:

    def __init__( self, browser ):
        self.browser = browser
        self.label = "AddTestPlanPage"

    def planNameAndroid( self ):
        return BasicTextField( self.label + " > planNameAndroid", lambda : self.browser.find_element_by_id( "name" ) )

    def dscription( self, build, link ):
        return BasicTextField( self.label + " > description", lambda : self.browser.find_element_by_id( "description" ) ).input(
            "- " + build + " branch: \n"
            "" + link + "\n\n"
            "- 請使用 branch debug build "
            "- 請使用 白名單手機 \n"
            "- Live 訊息發送、Listen With 請改用內網測試 (PEAP, mac-auth) \n"
        )

    def prodDescription( self, build, link ):
        return BasicTextField( self.label + " > description", lambda : self.browser.find_element_by_id( "description" ) ).input(
            "- " + build + " branch: \n"
            "" + link + "\n\n"
            "- 請使用 branch Prod build \n"
            "- 請使用 白名單手機 \n"
            "- Live 訊息發送、Listen With 請改用內網測試 (PEAP, mac-auth) \n"
        )

    def addTestSuiteButton( self ):
        return BasicButton( self.label + " > addTestSuiteButton", lambda : self.browser.find_element_by_id( "sidebar-plans-addsuite" ) )

    def selectAddTestSuite( self ):
        return SelectWindow( self.label + " > selectAddTestSuite", lambda : self.browser.find_element_by_id( "choose_suite_id" ) )

    def selectAddTestSuiteOkButton( self ):
        return BasicButton( self.label + " > selectAddTestSuiteOkButton", lambda : self.browser.find_element_by_id( "chooseSuiteDialogSubmit" ) )

    def testPlanSelectCasesButton( self ):
        return BasicButton( self.label + " > testPlanSelectCasesButton", lambda : self.browser.find_element_by_xpath( "(//a[contains(text(),'select cases')])[1]" ) )

    def testPlanSelectCasesButton2( self ):
        return BasicButton( self.label + " > testPlanSelectCasesButton2", lambda : self.browser.find_element_by_xpath( "(//a[contains(text(),'select cases')])[3]" ) )

    def testPlanSelectCasesButton3( self ):
        return BasicButton( self.label + " > testPlanSelectCasesButton3", lambda : self.browser.find_element_by_xpath( "(//a[contains(text(),'select cases')])[5]" ) )

    def renamePlanTitle( self, number):
        return BasicButton( self.label + " > renamePlanTitle", lambda : self.browser.find_element_by_xpath( "//*[@id='entries']/div[" + number + "]/div[1]/div/div[2]/div[1]/a/div" ) )

    def editPlanName( self, Device, Plan, Tag, Branch, Environment, build ):
        return BasicTextField( self.label + " > editPlanName", lambda : self.browser.find_element_by_id( "editName" ) ).input(
            "" +Device+ " / " +Plan+ " / " +Tag+ " / UtaPass " +Branch+ " branch / " +Environment+ " / "+build+"#  / yyyy-mm-dd (your name) "
        )

    def editConfirm( self ):
        return  BasicButton( self.label + " > editConfirm", lambda : self.browser.find_element_by_xpath( "//*[@id='editNameForm']/div[2]/button" ) )

    def acceptTestCasePaln( self ):
        return BasicButton( self.label + " > acceptTestCasePaln", lambda : self.browser.find_element_by_id( "accept" ) )
