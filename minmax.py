#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
array = [int(a),int(b),int(c),int(d),int(e)]
sortedArray = sorted(array)
max = 0
min = 0
for i in range(len(array)-1):
    min += sortedArray[i]
for i in range(len(array)-1, 0, -1):
    max += sortedArray[i]
print "%d %d" %(min, max)