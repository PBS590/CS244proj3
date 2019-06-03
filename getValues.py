#! /usr/bin/env python

import random
import sys
import time
import os

filename = "./smallkv/5GB/data_0.csv"

if len(sys.argv) != 2:
    print("Usage: './workload <column_num>'")
    exit(-1)

column = int(sys.argv[1])
values = list()
f = open(filename, "r")

output_file = "output.txt"
os.system("rm output.txt")
out = open(output_file, "a+")
#out.write("Column: " + str(column)+ " \n")

def getValues():
    numValues = 0
    with open(filename) as f:
        with open("zipf.txt") as zipf:
      	    rows = zipf.readlines()
      	    rows = [int(x) for x in rows]
            rows.sort()
	    rowsIndex = 0;
            valuesIndex = 0;
            for line in f:
               while(rowsIndex < len(rows) and valuesIndex == rows[rowsIndex]):
                   columns = line.strip().split(",")
                   print("Adding: " + str(rows[rowsIndex]))
		   values.append(columns[column])
                   rowsIndex += 1
	       valuesIndex += 1
getValues()

random.shuffle(values,)
for v in values:
    out.write(str(v) + "\n")
	
	
