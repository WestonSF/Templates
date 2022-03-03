import fme
import fmeobjects
import arcpy
logger = fmeobjects.FMELogFile() 

# Template Class Interface
# Use within code to print and log messages - self.printMessage("xxx","info"), self.printMessage("xxx","warning"), self.printMessage("xxx","error")
class mainClass(object):
    # Called once at start
    def __init__(self):
        self.printMessage("Python script started...","info")      
        
    # Called for each feature that comes into the input
    def input(self,feature):
        self.pyoutput(feature)
    
    # Called once, after all features are processed    
    def close(self):
        self.printMessage("Python script finished...","info")   
        
    # Start of print and logging message function
    def printMessage(self,message,type):  
        if (type.lower() == "warning"):
            logger.logMessageString(message,1)    
        elif (type.lower() == "error"):
            logger.logMessageString(message,2)
        else:
            logger.logMessageString(message,0)             
    # End of print and logging message function
