import clr
clr.AddReference('TivaComm')
from TivaComm import WandComm


class WandCommPy:
    def __init__(self):
        self.wand = WandComm()
        self.wand.Start().Wait()
        print ("WandComm initialized")
    
    def runCommand(self, command):
        resp= self.wand.Send(command).Result

        if 'Failed' in resp:
            raise Exception(resp)
        else:
            return resp

    def endSession(self):
        self.wand.Stop().Wait()


