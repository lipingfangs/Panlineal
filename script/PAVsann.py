
#!/usr/bin/env python
# Copyright (C) <2020> PMBL;South China Agricultural University. All rights reserved
__author__ = "Write by Fangping Li"
__version__ = '0.1.0'


import sys
import os

hapc = sys.argv[1]#hapc or goc
gtf = sys.argv[2]#gtf or gff3
gocout = sys.argv[3]

hapcr =open(hapc,"r")
hapcline = list(hapcr.readlines())
hapcr.close()

gtfr =open(gtf,"r")
gtfline = list(gtfr.readlines())
gtfr.close()

goout =open(gocout,"w")
print(hapcline[0].strip()+"	"+"RefGene",file = goout)
c = 0
for i in hapcline[1:]:
    j = i.split()
    for k in gtfline:
        l = k.split()
        if l[2] == "transcript" or l[2] == "gene":

            if l[0] == j[0].split("-")[2]:
                
                if l[4]<j[2]<l[3] or l[4]>j[2]>l[3]:
                    print(l[9])
                    temp = "	"+l[9]
                    break
                else:
                    temp= "	"+"NA"
    c += 1
    print(c)                
    print(i.strip(),end = "",file = goout)
    print(temp,file = goout)
    
goout.close()    
