#-------------------------------------------------------------
# Name:                 #
# Purpose:              #
# Author:               Shaun Weston (sweston@doc.govt.nz)
# Date Created:         01/01/2021
# Last Updated:         01/01/2021
# ArcGIS Version:       ArcGIS API for Python 1.8.0+
# Python Version:       3.6.9+ (Anaconda Distribution)
#--------------------------------

# Import libraries
import os
import sys
import logging
import arcgis
# Create new data folder if does not exist
dataFolder = os.path.join(os.path.dirname('__file__'),"data")
if not os.path.exists(dataFolder):
    os.mkdir(dataFolder)
    
# Set global parameters
logFile = os.path.join(dataFolder,"Logging.log")
# Set Logging
logger = logging.getLogger(os.path.basename('__file__'))
logger.setLevel(logging.DEBUG)
# Setup log message handler
logMessage = logging.FileHandler(logFile)
# Setup the log formatting
logFormat = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s", "%d/%m/%Y - %H:%M:%S")
# Add formatter to log message handler
logMessage.setFormatter(logFormat)
# Add log message handler to logger
logger.addHandler(logMessage)


# FUNCTION - Print message
def printMessage(message,type):
    # Print message
    print(message)        
    if (type.lower() == "warning"):
        # Log message
        logger.warning(message)     
    elif (type.lower() == "error"):
        # Log message
        logger.error(message)   
    else:
        # Log message
        logger.info(message)

# Main function
def main():
    printMessage("Process started...","info")
    
main()
