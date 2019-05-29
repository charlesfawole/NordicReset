
import os
import sys
import clr
import time,datetime
from WandCommPy import WandCommPy
from DataSaver import DataSaver



clr.AddReference('TivaComm')

logFile = ("C:\\Users\\charles.fawole\\Box Sync\\RF IPG\\Misc Data\\Nordic Reset\\nordic_reset "+str((int)(time.time()))+".csv")
   
header = ['Index','TimeStamp','reboot_counter_arm','reboot_counter','softerrors','reboot_occurred','reboot_timestamp','version','exception_index']

logFile = DataSaver(logFile,header)

wand = WandCommPy()

index = 0
exception_count = 0
wand.runCommand('a')
wand.runCommand('e')
wand.runCommand('boot')
wand.runCommand('a')
wand.runCommand('e')
wand.runCommand('v')
print(wand.runCommand('fcall 0 0x115 2'))


def main():
    index = 0
    exception_index = 0
    while True:
        try:
            (wand.runCommand('a'))
            (wand.runCommand('e'))
            wand.runCommand('boot')
            wand.runCommand('a')
            wand.runCommand('e')
            version = wand.runCommand('v')
            print (version)
            (wand.runCommand('fcall 0 0x116 8 240 30 1'))

            reboot_timestamp = wand.runCommand('readx 0 0x1904 4')
            reboot_occurred = wand.runCommand('readx 0 0x1900 1')
            softerrors=wand.runCommand('readx 0 0x18D0 4')
            reboot_counter=wand.runCommand('readx 0 0x18D4 4')
            reboot_counter_arm = wand.runCommand('readx 0 0x18D8 4')
            print("reboot counter: {} arm reboot counter {}".format(reboot_counter, reboot_counter_arm))
            logFile.writeRowToCSV([index,datetime.datetime.now(),reboot_counter_arm,reboot_counter,softerrors,reboot_occurred,reboot_timestamp,version,exception_index])
            logFile.flush()
            time.sleep(300)
            index = index+1
        except Exception as ex:
            print (ex)
            exception_index = exception_index + 1
        finally:
            print ("At exception number "+str(exception_index))

    logFile.closeCSV()
   
main()