#-------------------------------------------------------------
# Name:       #
# Purpose:    #         
# Author:     Shaun Weston (shaun.weston@splicegroup.co.nz)
# Date Created:    01/01/2013
# Last Updated:    01/01/2013
# Copyright:   (c) Splice Group
# ArcGIS Version:   10.1/10.2
# Python Version:   2.7
#--------------------------------

# Import modules and enable data to be overwritten
import os
import sys
import datetime
import smtplib
import arcpy
arcpy.env.overwriteOutput = True

# Set variables
logInfo = "false"
logFile = r""
sendEmail = "false"
output = None

# Start of main function
def mainFunction(*argv): # Get parameters from ArcGIS Desktop tool by seperating by comma e.g. (var1 is 1st parameter,var2 is 2nd parameter,var3 is 3rd parameter)  
    try:
        # Log start
        if logInfo == "true":
            loggingFunction(logFile,"start","")

        # --------------------------------------- Start of code --------------------------------------- #        

        # --------------------------------------- End of code --------------------------------------- #  
            
        # If called from gp tool return the arcpy parameter   
        if __name__ == '__main__':
            # Return the output if there is any
            if output:
                arcpy.SetParameterAsText(1, output)
        # Otherwise return the result          
        else:
            # Return the output if there is any
            if output:
                return output      
        # Log start
        if logInfo == "true":
            loggingFunction(logFile,"end","")        
        pass
    # If arcpy error
    except arcpy.ExecuteError:
        # Log error
        if logInfo == "true":  
            loggingFunction(logFile,"error",arcpy.GetMessages(2))
    # If python error
    except Exception as e:
        # Log error
        if logInfo == "true":         
            loggingFunction(logFile,"error",e.args[0])
# End of main function

# Start of logging function
def loggingFunction(logFile,result,info):
    # Show the message
    arcpy.AddMessage(info)
    
    #Get the time/date
    setDateTime = datetime.datetime.now()
    currentDateTime = setDateTime.strftime("%d/%m/%Y - %H:%M:%S")
    
    # Open log file to log message and time/date
    if result == "start":
        with open(logFile, "a") as f:
            f.write("---" + "\n" + "Process started at " + currentDateTime)
    if result == "end":
        with open(logFile, "a") as f:
            f.write("\n" + "Process ended at " + currentDateTime + "\n")
            f.write("---" + "\n")        
    if result == "error":
        with open(logFile, "a") as f:
            f.write("\n" + "Process ended at " + currentDateTime + "\n")
            f.write("There was an error: " + info + "\n")        
            f.write("---" + "\n")
        # Send an email
        if sendEmail == "true":
            arcpy.AddMessage("Sending email...")
            # Receiver email address
            to = ''
            # Sender email address and password
            gmail_user = ''
            gmail_pwd = ''
            # Server and port information
            smtpserver = smtplib.SMTP("smtp.gmail.com",587) 
            smtpserver.ehlo()
            smtpserver.starttls() 
            smtpserver.ehlo
            # Login
            smtpserver.login(gmail_user, gmail_pwd)
            # Email content
            header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Error \n'
            msg = header + '\n' + '' + '\n' + '\n' + info
            # Send the email and close the connection
            smtpserver.sendmail(gmail_user, to, msg)
            smtpserver.close()                
# End of logging function    

# This test allows the script to be used from the operating
# system command prompt (stand-alone), in a Python IDE, 
# as a geoprocessing script tool, or as a module imported in
# another script
if __name__ == '__main__':
    # Arguments are optional - If running from ArcGIS Desktop tool, parameters will be loaded into *argv
    argv = tuple(arcpy.GetParameterAsText(i)
        for i in range(arcpy.GetArgumentCount()))
    mainFunction(*argv)
    
