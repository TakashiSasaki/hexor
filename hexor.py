#!/usr/bin/python3
import sys

class Hexor:
    def __init__(self):
        self.hexs = []

    def addFile(self, filename):
        f = open(filename, mode='r')
        lines = f.readlines()     
        for line in lines:
            fields = line.split()
            if len(fields) != 2:
                raise "Each line should have exact two fields."
            else:
                hexstring = fields[0]
                self.hexs.append(hexstring)

    def getXor(self):
        if len(self.hexs) == 0:
            raise "At least one file should be given."
        hexLength = len(self.hexs[0])
        accum = "0" * hexLength
        for hex in self.hexs:
            if len(hex) != hexLength:
                raise "All hex string should have the same length."
            accum = xorHexs(accum, hex)
        return accum

    def getHexs(self):
        return self.hexs

def xorHexs(xx, yy):
    result = ""
    for i in range(len(xx)):
        result += xorChars(xx[i], yy[i]) 
    return result


def xorChars(x, y):
    pass

if __name__ == "__main__":
    args = sys.argv
    filenames = args[1:]
    hexor = Hexor()
    for filename in filenames:
        hexor.addFile(filename)

    print(hexor.getHexs())

