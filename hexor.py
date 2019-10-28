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

    def getHexs(self):
        return self.hexs

if __name__ == "__main__":
    args = sys.argv
    filenames = args[1:]
    hexor = Hexor()
    for filename in filenames:
        hexor.addFile(filename)

    print(hexor.getHexs())

