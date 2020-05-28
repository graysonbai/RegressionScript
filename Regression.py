import unittest
from Navigator import *
from webdriver_manager.chrome import ChromeDriverManager


class Regression( unittest.TestCase ):

    def setUp(self):
        self.browser = webdriver.Chrome( ChromeDriverManager().install() )
        self.navigator = Navigator( self.browser )
        self.browser.get( "https://kkstream.testrail.net/index.php?/runs/overview/30" )
        self.navigator.loginPage().userName().input()
        self.navigator.loginPage().passWord().input()
        self.navigator.loginPage().submitButton().tap()

    def test_RegressionDay1(self):
        self.navigator.testRunAndTestResult().addTestPlan().tap()
        self.navigator.addTestPlanPage().planNameAndroid().input( "[Sprint ][Android] Regression Day 1" )
        self.navigator.addTestPlanPage().dscription( "Release", "https://utapass-jenkins.kkinternal.com/view/Android/job/UtaPassAndroidRelease/" )
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuite().select( "Utapass APP" )
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton().tap()
        self.navigator.selectCasePage().licenseLabelButton().tap()
        self.navigator.selectCasePage().selectPremium500Plan().select( "Premium-500" )
        self.navigator.selectCasePage().platformsButton().tap()
        self.navigator.selectCasePage().selectAndroidPlatforms().tap()
        self.navigator.selectCasePage().priorityButton().tap()
        self.navigator.selectCasePage().selectCriticalPriority().tap()
        self.navigator.selectCasePage().testPurposeButton().tap()
        self.navigator.selectCasePage().selectFastTag().tap()
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton2().tap()
        self.navigator.selectCasePage().selectSpPPlan().deselectAll()
        self.navigator.selectCasePage().selectSpPPlan().select( "SmartPass-Premium(SpP)" )
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton3().tap()
        self.navigator.selectCasePage().selectSpPPlan().deselectAll()
        self.navigator.selectCasePage().selectHighTierPlan().select( "HighTier-980" )
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "1" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "Galaxy S6 edge (7.0)", "500 Plan", "F-C", "Release", "Stg", "Release" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "2" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "Galaxy S7 Edge (8.0)", "SpP Plan", "F-C", "Release", "Stg", "Release"  )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "3" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "Galaxy S8 (9.0)", "HighTier Plan", "F-C", "Release", "Stg", "Release"  )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().acceptTestCasePaln().tap()

    def test_RegressionDa2(self):
        self.navigator.testRunAndTestResult().addTestPlan().tap()
        self.navigator.addTestPlanPage().planNameAndroid().input( "[Sprint ][Android] Regression Day 2" )
        self.navigator.addTestPlanPage().dscription( "Release", "https://utapass-jenkins.kkinternal.com/view/Android/job/UtaPassAndroidRelease/" )
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuite().select( "Utapass APP" )
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton().tap()
        self.navigator.selectCasePage().licenseLabelButton().tap()
        self.navigator.selectCasePage().selectPremium500Plan().select( "Premium-500" )
        self.navigator.selectCasePage().platformsButton().tap()
        self.navigator.selectCasePage().selectAndroidPlatforms().tap()
        self.navigator.selectCasePage().priorityButton().tap()
        self.navigator.selectCasePage().selectCriticalPriority().tap()
        self.navigator.selectCasePage().testPurposeButton().tap()
        self.navigator.selectCasePage().selectFastTag().tap()
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton2().tap()
        self.navigator.selectCasePage().selectSpPPlan().deselectAll()
        self.navigator.selectCasePage().selectSpPPlan().select( "SmartPass-Premium(SpP)" )
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton3().tap()
        self.navigator.selectCasePage().selectSpPPlan().deselectAll()
        self.navigator.selectCasePage().selectHighTierPlan().select( "HighTier-980" )
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "1" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "Galaxy S6 edge (7.0)", "500 Plan", "F-C", "Release", "Stg", "Release" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "2" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "Galaxy S7 Edge (8.0)", "SpP Plan", "F-C", "Release", "Stg", "Release" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "3" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "Galaxy S8 (9.0)", "HighTier Plan", "F-C", "Release", "Stg","Release" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().acceptTestCasePaln().tap()


    def test_FinalCheck(self):
        self.navigator.testRunAndTestResult().addTestPlan().tap()
        self.navigator.addTestPlanPage().planNameAndroid().input( "[Sprint ][Android] FinalCheck" )
        self.navigator.addTestPlanPage().dscription( "Master", "https://utapass-jenkins.kkinternal.com/view/Android/job/UtaPassAndroidMaster/" )
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuite().select( "Utapass APP" )
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton().tap()
        self.navigator.selectCasePage().licenseLabelButton().tap()
        self.navigator.selectCasePage().selectPremium500Plan().select( "Premium-500" )
        self.navigator.selectCasePage().platformsButton().tap()
        self.navigator.selectCasePage().selectAndroidPlatforms().tap()
        self.navigator.selectCasePage().typeButton().tap()
        self.navigator.selectCasePage().selectAcceptance().tap()
        self.navigator.selectCasePage().setSelectionButton()
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuite().select( "Utapass APP" )
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton2().tap()
        self.navigator.selectCasePage().selectSpPPlan().deselectAll()
        self.navigator.selectCasePage().selectPremium500Plan().select( "SmartPass-Premium(SpP)" )
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuite().select( "Utapass APP" )
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton3().tap()
        self.navigator.selectCasePage().selectSpPPlan().deselectAll()
        self.navigator.selectCasePage().selectPremium500Plan().select( "HighTier-980" )
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "1" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "Galaxy S6 edge (7.0)", "500 Plan", "AT", "Master", "Prod", "Master" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "2" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "Galaxy S7 Edge (8.0)", "SpP Plan", "AT", "Master", "Prod", "Master" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "3" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "Galaxy S8 (9.0)", "HighTier Plan", "AT", "Master", "Prod", "Master" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().acceptTestCasePaln().tap()

    def test_RegressionDay1_iOS(self):
        self.navigator.testRunAndTestResult().addTestPlan().tap()
        self.navigator.addTestPlanPage().planNameAndroid().input( "[Sprint ][iOS] Regression Day 1" )
        self.navigator.addTestPlanPage().dscription( "Release", "https://utapass-jenkins.kkinternal.com/view/iOS/job/UtaPassiOSRelease/" )
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuite().select( "Utapass APP" )
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton().tap()
        self.navigator.selectCasePage().licenseLabelButton().tap()
        self.navigator.selectCasePage().selectPremium500Plan().select( "Premium-500" )
        self.navigator.selectCasePage().platformsButton().tap()
        self.navigator.selectCasePage().selectiOSPlatforms().tap()
        self.navigator.selectCasePage().priorityButton().tap()
        self.navigator.selectCasePage().selectCriticalPriority().tap()
        self.navigator.selectCasePage().testPurposeButton().tap()
        self.navigator.selectCasePage().selectFastTag().tap()
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton2().tap()
        self.navigator.selectCasePage().selectSpPPlan().deselectAll()
        self.navigator.selectCasePage().selectSpPPlan().select( "SmartPass-Premium(SpP)" )
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton3().tap()
        self.navigator.selectCasePage().selectSpPPlan().deselectAll()
        self.navigator.selectCasePage().selectHighTierPlan().select( "HighTier-980" )
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "1" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "iPhone (12.4.1)", "500 Plan", "F-C", "Release", "Stg", "Release" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "2" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "iPhone (11.4)", "SpP Plan", "F-C", "Release", "Stg", "Release" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "3" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "iPhone (13.3.1)", "HighTier Plan", "F-C", "Release", "Stg", "Release" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().acceptTestCasePaln().tap()

    def test_RegressionDay2_iOS(self):

        self.navigator.testRunAndTestResult().addTestPlan().tap()
        self.navigator.addTestPlanPage().planNameAndroid().input( "[Sprint ][iOS] Regression Day 2" )
        self.navigator.addTestPlanPage().dscription( "Release", "https://utapass-jenkins.kkinternal.com/view/iOS/job/UtaPassiOSRelease/" )
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuite().select( "Utapass APP" )
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton().tap()
        self.navigator.selectCasePage().licenseLabelButton().tap()
        self.navigator.selectCasePage().selectPremium500Plan().select( "Premium-500" )
        self.navigator.selectCasePage().platformsButton().tap()
        self.navigator.selectCasePage().selectiOSPlatforms().tap()
        self.navigator.selectCasePage().priorityButton().tap()
        self.navigator.selectCasePage().selectCriticalPriority().tap()
        self.navigator.selectCasePage().testPurposeButton().tap()
        self.navigator.selectCasePage().selectFastTag().tap()
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton2().tap()
        self.navigator.selectCasePage().selectSpPPlan().deselectAll()
        self.navigator.selectCasePage().selectSpPPlan().select( "SmartPass-Premium(SpP)" )
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton3().tap()
        self.navigator.selectCasePage().selectSpPPlan().deselectAll()
        self.navigator.selectCasePage().selectHighTierPlan().select( "HighTier-980" )
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "1" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "iPhone (12.4.1)", "500 Plan", "F-C", "Release", "Stg", "Release" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "2" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "iPhone (11.4)", "SpP Plan", "F-C", "Release", "Stg", "Release" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "3" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "iPhone (13.3.1)", "HighTier Plan", "F-C", "Release", "Stg","Release" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().acceptTestCasePaln().tap()

    def test_FinalCheck_iOS(self):
        self.navigator.testRunAndTestResult().addTestPlan().tap()
        self.navigator.addTestPlanPage().planNameAndroid().input( "[Sprint ][iOS] FinalCheck" )
        self.navigator.addTestPlanPage().dscription( "Master", "https://utapass-jenkins.kkinternal.com/view/iOS/job/UtaPassiOSMaster/" )
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuite().select( "Utapass APP" )
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton().tap()
        self.navigator.selectCasePage().licenseLabelButton().tap()
        self.navigator.selectCasePage().selectPremium500Plan().select( "Premium-500" )
        self.navigator.selectCasePage().platformsButton().tap()
        self.navigator.selectCasePage().selectiOSPlatforms().tap()
        self.navigator.selectCasePage().typeButton().tap()
        self.navigator.selectCasePage().selectAcceptance().tap()
        self.navigator.selectCasePage().setSelectionButton()
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuite().select( "Utapass APP" )
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton2().tap()
        self.navigator.selectCasePage().selectSpPPlan().deselectAll()
        self.navigator.selectCasePage().selectPremium500Plan().select( "SmartPass-Premium(SpP)" )
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().addTestSuiteButton().tap()
        self.navigator.addTestPlanPage().selectAddTestSuite().select( "Utapass APP" )
        self.navigator.addTestPlanPage().selectAddTestSuiteOkButton().tap()
        self.navigator.addTestPlanPage().testPlanSelectCasesButton3().tap()
        self.navigator.selectCasePage().selectSpPPlan().deselectAll()
        self.navigator.selectCasePage().selectPremium500Plan().select( "HighTier-980" )
        self.navigator.selectCasePage().setSelectionButton().tap()
        self.navigator.selectCasePage().selectCasesSubmit().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "1" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "Galaxy S6 edge (7.0)", "500 Plan", "AT", "Master", "Prod", "Master" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "2" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "Galaxy S7 Edge (8.0)", "SpP Plan", "AT", "Master", "Prod", "Master" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().renamePlanTitle( "3" ).tap()
        self.navigator.addTestPlanPage().editPlanName( "Galaxy S8 (9.0)", "HighTier Plan", "AT", "Master", "Prod", "Master" )
        self.navigator.addTestPlanPage().editConfirm().tap()
        self.navigator.addTestPlanPage().acceptTestCasePaln().tap()

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()