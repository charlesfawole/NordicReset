import csv,os.path
import numpy as np

class DataSaver():
    def __init__(self,filename,headers):
        self.file_o = None
        self.csv_o = None
        if (not (os.path.exists(filename))):
            self.csv_o,self.file_o=self.createCSV(filename)
            self.writeCSV_Header(headers)
        else:
            self.csv_o, self.file_o = self.createCSV(filename)
    def createCSV(self,filename):
        file_o = open(filename, "w")
        csv_o = csv.writer(file_o,delimiter=',')
        return csv_o,file_o

    def writeCSV_Header(self,headers):
        self.writeRowToCSV(headers)
    def writeRowToCSV(self,row):
        self.csv_o.writerow(row)
    def writeListToCSV(self,array):
        num_of_rows = len(array)
        for i in range(0,num_of_rows,1):
            self.writeRowsToCSV(array[i])
    def writeTransposedListToCSV (self, array):
        ta = NotImplemented.transpose(array)
        self.writeListToCSV(ta)

    def flush(self):
        self.file_o.flush()
    def closeCSV(self):
        self.file_o.close()