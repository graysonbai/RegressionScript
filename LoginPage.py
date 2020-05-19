from component.BasicTextField import *

class LoginPage:

    def __init__( self, browser ):
        self.browser = browser
        self.label = "LoginPage"

    def userName( self ):
        return BasicTextField(  self.label + " > userName", lambda : self.browser.find_element_by_id( "name" ) )

    def passWord( self ):
        return BasicTextField(  self.label + " > passWord", lambda : self.browser.find_element_by_id( "password" ) )

    def submitButton( self ):
        return BasicTextField(  self.label + " > submitButton", lambda : self.browser.find_element_by_id( "button_primary" ) )