#!/usr/bin/python3
import sys

class Hexor:
    def __init__(self):
        self.hexstrings = []
        self.filenames = []

    def addFile(self, filename):
        f = open(filename, mode='r')
        lines = f.readlines()     
        for line in lines:
            fields = line.split()
            if len(fields) != 2:
                raise "Each line should have exact two fields."
            else:
                hexstring = fields[0]
                filename = fields[1]
                self.hexstrings.append(hexstring)
                self.filenames.append(filename)

    def getXor(self):
        if len(self.hexstrings) == 0:
            raise "At least one file should be given."
        hexLength = len(self.hexstrings[0])
        accum = "0" * hexLength
        for hex in self.hexstrings:
            if len(hex) != hexLength:
                raise "All hex string should have the same length."
            accum = xorHexstrings(accum, hex)
        assert len(accum) == hexLength
        return accum

def xorHexstrings(xx, yy):
    result = ""
    for i in range(len(xx)):
        result += xorChars(xx[i], yy[i]) 
    return result

def xorChars(x, y):
    assert len(x) == 1 and len(y) == 1
    intX = int(x,16)
    intY = int(y,16)
    intZ = intX ^ intY
    z = format(intZ, "x")
    assert len(z) == 1
    return z

import argparse
import json

if __name__ == "__main__":
    args = sys.argv

    p = argparse.ArgumentParser()
    p.add_argument("-j", "--json", action="store_true", help="output as JSON")
    p.add_argument("file", action="append", nargs="*", help="input file")
    a = p.parse_args()
    #print(a.file)

    filenames = args[1:]
    filenames = a.file[0]
    hexor = Hexor()
    for filename in filenames:
        hexor.addFile(filename)

    #print(hexor.getHexs())
    if a.json == True:
        print(json.dumps({
            "xor" : hexor.getXor(),
            "filenames" : hexor.filenames,
            "hexstrings" : hexor.hexstrings
            }, indent=2))
    else:
        print(hexor.getXor())

