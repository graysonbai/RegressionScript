from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
import time


def retry( log ):
    def currentFunction( function ):
        def warps( *args ):

            for n in range(0, 6):
                print( args[0].label + log )

                if isVisible( log, args[0].Locator ):
                    return function( *args )

                else:
                    if n > 6:
                        raise ( "not ready" )
                    else:
                        sleep(3)
                        print( "" )
        return warps
    return currentFunction


def sleep( t ):
    for s in range(0, t):
        time.sleep(1)
        print( "Sleep second(%s)s" % (s + 1) )


def isVisible( log, element ):
    try:

        if log == " > tap":
            EC.element_to_be_clickable( element() )
            return True

        else:
            EC.visibility_of( element() )
            return True

    except NoSuchElementException:
        return False

    except ElementNotVisibleException:
        return False

    except WebDriverException:
        return  False