from Retry import *


class BasicTextField():

    def __init__( self, label, Locator ):
        self.Locator = Locator
        self.label = label

    def elementLocator( self ):
        return self.Locator()

    @retry( " > tap" )
    def tap( self ):
        self.elementLocator().click()

    @retry( " > clear" )
    def clear( self ):
        self.elementLocator().clear()

    @retry( " > input" )
    def input( self, text  ):
        self.clear()
        self.tap()
        self.elementLocator().send_keys( text )

    def isVisible( self ):
        return isVisible( " > check Visible", self.elementLocator )


    def assertVisiable( self ):
        if self.isVisible():
            raise ( "Button not Visible" )


    def assertInVisiable( self ):
        if not self.isVisible():
            raise ( "ButtonVisible" )
