# Import modules
import base64

def decryptPassword(encyptedPassword):
    return base64.b64decode(encyptedPassword)

