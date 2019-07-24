
import os
import sys
import clr
import time,datetime
from WandCommPy import WandCommPy
from DataSaver import DataSaver
from IPG_DevKitControl import IPG_DevKitControl
from MSP_FW_Loader import MSP_FW_Loader
from FW_From_SVN import FW_From_SVN
from Nordic_FW_Loader import Nordic_FW_Loader



#clr.AddReference('TivaComm')

#wand = WandCommPy()



def main():

    fw_svn = FW_From_SVN()
    mspFW_loader = MSP_FW_Loader()
    nordicLoader = Nordic_FW_Loader()


    fw_svn.getTopOfTrunkFW()
    latestBuildNumber = fw_svn.getLatestFWBuildNumber()
    latestRevisionNumber = fw_svn.getLatestRevisionNumber()

    mspFW_loader.programMSP(latestBuildNumber)
    nordicLoader.programNordic(NordicFWFolder=latestBuildNumber)

    while True:
        if (latestBuildNumber == fw_svn.getLatestFWBuildNumber()):

            fw_svn.getTopOfTrunkFW()
            latestBuildNumber = fw_svn.getLatestFWBuildNumber()
            latestRevisionNumber = fw_svn.getLatestRevisionNumber()


            mspFW_loader.programMSP(latestBuildNumber)
            nordicLoader.programNordic(NordicFWFolder=latestBuildNumber)
        
            print ("\r\n\r\n")
            print("loaded firmware is latest from SVN")
    
        else:
             print ("\r\n\r\n")
             print("loaded firmware is not latest from SVN")

    #dev_kit = IPG_DevKitControl("COM3")
    #mspFW_loader = MSP_FW_Loader()
    
    #nordicLoader = Nordic_FW_Loader()

    #fw_svn.getTopOfTrunkFW()
    #fw_svn.getLatestFWBuildNumber()

    #print(dev_kit._execute_command('reboot'))
    #mspFW_loader.programMSP()
    #nordicLoader.programNordic()

    #dev_kit.closePort()

    

   
main()