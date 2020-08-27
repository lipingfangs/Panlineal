#!/usr/bin/env python
# Copyright (C) <2020> PMBL;South China Agricultural University. All rights reserved
__author__ = "Write by Fangping Li"
__version__ = '0.1.0'


import sys
import os

goc1 = sys.argv[1]
chrs = sys.argv[2]

goc1 =open(goc1n,"r")
goc = list(goc1.readlines())
goc1.close()

temp1fi =open("temp1.fi","w")
for i in goc:
    if i.find("Org") == -1:
        if i.find(chrs) != -1:
            if len(i.split()) == 7:
                j = i.split()
                print(j[0]+"	"+j[1]+"	"+j[4]+"	"+j[5]+"	"+j[2]+"	"+j[3]+"	"+j[6],file = temp1fi)
                
            if len(i.split()) > 7:
                j = j.split()
                loc = j.index("more")
                print(j[0]+"	"+j[1]+"	"+j[loc-3]+"	"+j[loc-2]+"	"+j[2]+"	"+j[3]+"	"+j[loc-1])
                
temp1fi.close()            
