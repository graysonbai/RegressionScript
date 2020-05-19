from component.BasicButton import *
from component.SelectWindow import SelectWindow


class SelectCasePage:


    def __init__( self, browser ):
        self.browser = browser
        self.label = "SelectCasePage"


    def licenseLabelButton( self ):
        return BasicButton( self.label + " > licenseLabelButton", lambda :self.browser.find_element_by_link_text( "License Label" ) )

    def selectPremium500Plan( self ):
        return SelectWindow( self.label + " > selectPremium500Plan", lambda :self.browser.find_element_by_xpath( "//*[@id='filter-cases:custom_uta_license']/div[2]/select" ) )

    def selectSpPPlan( self ):
        return SelectWindow( self.label + " > selectSpPPlan", lambda :self.browser.find_element_by_xpath( "//*[@id='filter-cases:custom_uta_license']/div[2]/select" ) )

    def selectHighTierPlan( self ):
        return SelectWindow( self.label + " > selectHighTierPlan", lambda :self.browser.find_element_by_xpath( "//*[@id='filter-cases:custom_uta_license']/div[2]/select" ) )

    def platformsButton( self ):
        return BasicButton( self.label + " > platformsButton", lambda : self.browser.find_element_by_link_text( "Platforms" ) )

    def selectAndroidPlatforms( self ):
        return BasicButton( self.label + " > selectAndroidPlatforms", lambda : self.browser.find_element_by_xpath( "(//option[@value='1'])[5]" ) )

    def selectiOSPlatforms( self ):
        return BasicButton( self.label + " > selectiOSPlatforms", lambda : self.browser.find_element_by_xpath( "(//option[@value='4'])[4]" ) )

    def priorityButton( self ):
        return BasicButton( self.label + " > priorityButton", lambda : self.browser.find_element_by_link_text( "Priority" ) )

    def selectCriticalPriority( self ):
        return BasicButton( self.label + " > selectCriticalPriority", lambda : self.browser.find_element_by_xpath( "(//option[@value='5'])[5]" ) )

    def testPurposeButton( self ):
        return BasicButton( self.label + " > testPurposeButton", lambda : self.browser.find_element_by_link_text( "Test Purpose" ) )

    def typeButton( self ):
        return BasicButton( self.label + " > typeButton", lambda : self.browser.find_element_by_link_text( "Type" ) )

    def selectAcceptance( self ):
        return BasicButton( self.label + " > selectAcceptance", lambda: self.browser.find_element_by_xpath( "(//option[@value='1'])[13]" ) )

    def selectFastTag( self ):
        # Fast tag
        return BasicButton( self.label + " > selectFastTag", lambda : self.browser.find_element_by_xpath( "(//option[@value='13'])[3]" ) )

    def selectRATTag( self ):
        # RAT tag
        return BasicButton( self.label + " > selectRATTag", lambda : self.browser.find_element_by_xpath( "(//option[@value='12'])[3]" ) )

    def setSelectionButton( self ):
        return BasicButton( self.label + " > setSelectionButton", lambda : self.browser.find_element_by_id( "selectCasesFilterApply" ) )

    def selectCasesSubmit( self ):
        return BasicButton( self.label + " > selectCasesSubmit", lambda : self.browser.find_element_by_id( "selectCasesSubmit" ) )

