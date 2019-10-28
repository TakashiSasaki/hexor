#!/usr/bin/python3
for x in range(16):
    for y in range(16):
        z = x ^ y
        print (hex(x)[2], hex(y)[2], hex(z)[2])
