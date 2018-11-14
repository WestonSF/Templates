#-------------------------------------------------------------
# Name:                 Encrypt Password
# Purpose:              Encrypts a password entered by a user, which
#                       can be copied and used in another script.
# Author:               Shaun Weston (shaun_weston@eagle.co.nz)
# Date Created:         14/11/2018
# Last Updated:         14/11/2018
# Python Version:       2.7.x
#--------------------------------

# Import modules
import sys
import base64

def encryptPassword(password):    
    return base64.b64encode(password)

password = raw_input("Enter password: ")
# Encrypt the password
encryptedPassword = encryptPassword(password)
print "Encrypted password is:"
print encryptedPassword
raw_input("Copy the above password into the Credentials.py file and press Enter...")
# Compile credentials script
import Credentials
print "Copy Credentials.pyc and DecryptPassword.pyc files to your project and use the following code to get the password:"
print "import Credentials"
print "import DecryptPassword"
print "print DecryptPassword.decryptPassword(Credentials.password)"
raw_input("Press Enter to close...")



