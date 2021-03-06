#!/home/lfp/miniconda3/bin/python
# Copyright (C) <2020> PMBL;South China Agricultural University. All rights reserved
__author__ = "Write by Fangping Li"
__version__ = '0.1.0'

import argparse
import sys
import os
def get_options():
    description = "Create lineal pangenome"
    parser = argparse.ArgumentParser(description = description,prog = 'creatpangenome.py')
    parser.add_argument('--version', action='version',version='%(prog)s '+__version__+" "+__author__)  
    parser.add_argument('-1', '--reference', action='store',type=str,help='input your reference .fasta')
    parser.add_argument('-2', '--query', action='store',type=str,help='input your query .fasta')    
    parser.add_argument('-g', '--svguide', action='store',type=str,help='input your sv file generated by svmu')
    parser.add_argument('-o', '--output', action='store',type=str,help='name of the  pan-genome output: <-o>.fasta;<-o>.fasta.goc',default="output")
    return parser.parse_args()


def seqfileread(file):#readfa
    file = open(file,"r")
    lines = list(file.readlines())
    dic={}
    temp = ""
    for i in lines:
        if i.startswith(">"):
            temp = i.strip()[1:]
            dic[temp] = ""
            #print(temp)
        else:
            i = i.strip()
            dic[temp] = dic[temp] + i
    file.close()
    return dic

gosome = get_options()
seq1 = gosome.reference#sys.argv[1] #Firstgenome
seq2 = gosome.query#sys.argv[2] #Secondgenome

seqdic1 = seqfileread(seq1)
seqdic2 = seqfileread(seq2)


svfile = open(gosome.svguide,"r")#sys.argv[3]#svguidefile
svfileline = list(svfile.readlines())
svfile.close()
cumlength = 0
ids = 0
outputloc = open(gosome.output+".goc","w")
roundcount = open("roundcount","r")
roundcountn = int(list(roundcount.readlines())[0])
roundcount.close() 
if roundcountn = 1:
    for i in svfileline:
        j = i.split()
        a = int(j[1]) + cumlength
        b = int(j[2]) + cumlength
        c = int(j[5])-1 
        d = int(j[6])-1 
        seqdic1[j[0]] = seqdic1[j[0]][:b] + seqdic2[j[4]][c:d+1] + seqdic1[j[0]][b:]
        cumlength += int(j[6])-int(j[5])
        orglength = int(j[6])-int(j[5])
        ids += 1
        locin = str(ids)+ "	" + j[0] + "	" +str(a) + "	" + str(b) + "	" + str(b+1) + "	" +str(b+orglength) + "	" +str(orglength)
        locout= str("Org"+str(ids))+ "	"+ j[0] + "	" +j[1] + "	" + j[2] + "	" + j[5] + "	" +j[6] + "	" +j[8]
        print(locin,file = outputloc)
        print(locout,file = outputloc)
        
if roundcountn > 1:
    for i in svfileline:
        j = i.split()
        a = int(j[1]) + cumlength
        b = int(j[2]) + cumlength
        c = int(j[5])-1 
        d = int(j[6])-1 
        orglength = int(j[6])-int(j[5])
        tempgocf = open("temp.fasta.goc","r")
        tempgoc = list(tempgocf.readlines())
        tempgoclenc = 0
        for k in tempgoc:
            if i.find("Org")==-1:
                tempgoclenc += 1
                k = k.split()
                if int(k[2])+ orglength >a and b <int(k[5])+ orglength:
                    f = int(k[5]) + cumlength
                    seqdic1[j[0]] = seqdic1[j[0]][:f] + seqdic2[j[4]][c:d+1] + seqdic1[j[0]][f:]
                    cumlength += int(j[6])-int(j[5])
                    
                    ids += 1
                    idk = str(roundcountn)+"-"+str(ids)
                    locin = str(idk)+ "	" + j[0] + "	" +str(a) + "	" + str(f) + "	" + str(f+1) + "	" +str(f+orglength) + "	" +str(orglength)+"	"+"more"+"	"+k[0]
                    locout= str("Org"+str(ids))+ "	"+ j[0] + "	" +j[1] + "	" + j[2] + "	" + j[5] + "	" +j[6] + "	" +j[8]
                    print(locin,file = outputloc)
                    print(locout,file = outputloc)
                    break

                if tempgoclenc == len(tempgoc)/2:#weather the cycle will be end means not in same position
                    seqdic1[j[0]] = seqdic1[j[0]][:b] + seqdic2[j[4]][c:d+1] + seqdic1[j[0]][b:]
                    cumlength += int(j[6])-int(j[5])
                    orglength = int(j[6])-int(j[5])
                    ids += 1
                    idk = str(roundcountn)+"-"+str(ids)
                    locin = str(idk)+ "	" + j[0] + "	" +str(a) + "	" + str(b) + "	" + str(b+1) + "	" +str(b+orglength) + "	" +str(orglength)
                    locout= str("Org"+str(ids))+ "	"+ j[0] + "	" +j[1] + "	" + j[2] + "	" + j[5] + "	" +j[6] + "	" +j[8]
                    print(locin,file = outputloc)
                    print(locout,file = outputloc)
          
outputloc.close()

outputfile = open(gosome.output+".fasta","w")    
for i in seqdic1.keys():
    print(">"+i,file = outputfile)
    print(seqdic1[i], file = outputfile)
    
outputfile.close()
    
    


    
