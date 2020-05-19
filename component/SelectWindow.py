from selenium.webdriver.support.select import Select


from Retry import *

class SelectWindow():

    def __init__( self, label ,Locator ):
        self.Locator = Locator
        self.label = label

    def elementLocator( self ):
        return self.Locator()

    @retry( " > select" )
    def select( self, text ):
        Select( self.elementLocator() ).select_by_visible_text( text )

    @retry( " > Deselect All" )
    def deselectAll( self ):
        Select( self.elementLocator() ).deselect_all()

    def isVisible( self ):
        return isVisible( " > check Visible", self.elementLocator  )


    def assertVisiable( self ):
        if self.isVisible():
            raise ( "Button not Visible" )


    def assertInVisiable( self ):
        if not self.isVisible():
            raise ( "ButtonVisible" )
