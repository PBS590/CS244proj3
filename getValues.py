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
values = set()
f = open(filename, "r")

output_file = "output.txt"
os.system("rm output.txt")
out = open(output_file, "a+")
out.write("Column: " + str(column)+ " \n")

def getValues():
	numValues = 0
	with open(filename) as f:
		line = f.readline()
		while line != '' and numValues < 10000:
			columns = line.strip().split(",")
			out.write(str(columns[column]) + "\n") 
			line = f.readline()
			numValues += 1

getValues()
start = time.time()
#os.system("mongo < getValues.js")
end = time.time()	
	
	

	
