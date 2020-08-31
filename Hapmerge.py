#!/usr/bin/env python
# Copyright (C) <2020> PMBL;South China Agricultural University. All rights reserved
__author__ = "Write by Fangping Li"
__version__ = '0.1.0'

import argparse
import sys
import os
import collections

def get_options():
    example = "Hapmerge -l merge.li -o haplistmergeout.hapcs " 
    description = "Merge .hapc file;  example: " + example
    parser = argparse.ArgumentParser(description = description,prog = 'Hapmerge.py')
    parser.add_argument('-l', '--haplist', action='store',type=str,
                         help='list file of .hapc files ready to be merged',default="merge.li")
    parser.add_argument('-o', '--output', action='store',type=str,
                         help='name of output .hapn file',default="merge.li")
    parser.add_argument('--version', action='version',version='%(prog)s '+__version__+" "+__author__)
    
    return parser.parse_args()
    
gosome = get_options()
haplist = gosome.haplist
haplist = open(haplist,"r")
haplistl = list(haplist.readlines())[0].split(",")
haplist.close()

dicg = collections.OrderedDict()

for i in haplist1:
    hapf = open(i,"r")
    for j in list(hapf.readlines()):
        j = j.split()
        if j[0] in list(dicg.keys()):
            for k in j[1:]:
                dicg[j[0]].append(k)
        else:
            dicg[j[0]] = []
    hapf.close()
            
outfile = open(gosome.output,"w")            
for i in list(dicg.keys()):
    print(dicg[i][0],end = "	",file = outfile)
    print(dicg[i][1],end = "	",file = outfile)
    print(dicg[i][2],end = "	",file = outfile)
    for j in dicg[i]:
        if i.find("Hap") != -1:
            print(j, end = "	")

outfile.close()
print("merge done !")
        
        
        