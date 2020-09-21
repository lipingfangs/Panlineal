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
haplist = open(haplist.strip(),"r")
haplistl = list(haplist.readlines())[0].split(",")
haplist.close()

dicg = collections.OrderedDict()
name = ""
for i in haplistl:
    name += i+"	"
    hapf = open(i.strip(),"r")
    for j in list(hapf.readlines())[1:]:
        j = j.split()
        if j[0] in list(dicg.keys()):
            for k in j:
                dicg[j[0]].append(k)
        else:
            dicg[j[0]] = []
            for k in j:
                dicg[j[0]].append(k)
    hapf.close()
            
outfile = open(gosome.output,"w")     
print("ID	PanPosition	RefPosition	"+name.strip(),file = outfile)

for i in list(dicg.keys()):
    print(dicg[i][0],end = "	",file = outfile)
    print(dicg[i][1],end = "	",file = outfile)
    print(dicg[i][2],end = "	",file = outfile)
    for j in dicg[i]:
        if j.find("Hap") != -1:
            print(j, end = "	",file = outfile)
    print("",file = outfile)

outfile.close()
print("merge done !")

if gosome.ann != "no":
    gff = gosome.ann
    command = "python PAVsann.py "+gosome.output +" "+gff+" "+gosome.output+".ann" 
    annout = os.system(command)
    if annout = 0:
        print("annotation done!")
        
