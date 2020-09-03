#!/usr/bin/env python
# Copyright (C) <2020> PMBL;South China Agricultural University. All rights reserved
__author__ = "Write by Fangping Li"
__version__ = '0.1.0'


import sys
import os

goc1 = sys.argv[1]
goc2 = sys.argv[2]
gocout = sys.argv[3]


def Gathergoc(goc1n,goc2n,gooutn):
    goc1 =open(goc1n,"r")
    goc1line = list(goc1.readlines())
    goc1.close()
    goc2 =open(goc2n,"r")
    goc2line = list(goc2.readlines())
    goc2.close()
    goout =open(gooutn,"w")
    cumlength = 0
    dicchr = {}
    dic1 ={}
    dic2 = {}
    if goc1line[0].startswith("OrgID"):
        stro = goc1line[1].split()[0].strip()
    else:
        stro = goc1line[0].split()[0].strip()
    print(stro)
    for j in goc1line:
        if j.find("Org") == -1:
            dic1[j.split()[0].strip()] = j
            
    for j in goc2line:
        if j.find("Org") == -1:
            dic1[j.split()[0].strip()] =j

    for j in goc1line:
        dicchr[j.split()[1].strip()] = []
        
    for i in dicchr.keys():
        os.system("cat "+goc1n+" | grep -v 'Org' | grep '"+i+"'| awk '{print $1,$2,$3,$4,$5,$6,$7}' > temp1.fi")
        os.system("cat "+goc2n+" | grep 'Org' | grep '"+i+"' > temp2.fi")
        os.system("cat temp1.fi temp2.fi | sort -n -k 3 > temp.fi")
        outfi = open("temp.fi"+i,"w")#middle file tempchrxxx
        print("OrgID"+"	"+"Chr"+"	"+"Start1"+"	"+"end1"+"	"+"Start2"+"	"+"end2"+"	"+"length", file = outfi)
        tempfi = open("temp.fi","r")
        tempfif = list(tempfi.readlines())
        tempfi.close()
        cumlengh = 0
        #print(i)
        for j in tempfif:
            
            if j.find(i) != -1:
                #print(j)
                if j.find("Org") != -1:
                    n = j.split()[0][3:]
                    print(dic1[n].strip(),file = outfi)
                    cumlengh = cumlengh + int(j.split()[6].strip()) 
                    orginlen = int(j.split()[6].strip()) 
                    #print(cumlengh)
                else:
                    n = j.split()[0]
                    p = dic1[n].split()
                    
                    if "more" in dic1[stro].split():
                        print(j)
                        print(p[0]+"	"+p[1],end = "	", file = outfi)
                        if "more" in p:
                            for m in p[2:p.index("more")]:
                                print(int(m)+cumlengh-orginlen,end = "	", file = outfi)
                            print(p[-1].strip(), file = outfi)
                        else:
                            for m in p[2:-1]:
                                print(int(m)+cumlengh-orginlen,end = "	", file = outfi)
                            print(p[6].strip(), file = outfi)
                    else:
                        print(p[0]+"	"+p[1]+"	"+str(int(p[2])+cumlengh)+"	"+str(int(p[3])+cumlengh)+"	"+str(int(p[4])+cumlengh)+"	"+str(int(p[5])+cumlengh)+"	"+p[6].strip(), file = outfi)
                    #print(j)
                stro = j.split()[0].replace("Org","")
                
        outfi.close()

    goout = open(gooutn,"w") 
    cumlength
    #intergrate of tempchrxxxx
    for i in dicchr.keys():
        gofi = open("temp.fi"+i,"r")#goin temp.fichr01
        gofif = list(gofi.readlines())
        gofi.close()
        for f in gofif:
            if f.find("Org") == -1:
                dic2[f.split()[0].strip()] =f
            
        infi = open("temp.fi"+i,"r")
        infif = list(infi.readlines())
        infi.close()
        for j in range(len(infif)):
            if len(infif[j].split())>7:
                t = infif[j].split()
                m = infif[j+1].split()
                if infif[j+1].find("more") != -1:
                    loc = m.index("more")
                    t[2] = ""
                    for v in m[2:loc-1]:
                        t[2] += "	"+str(v).strip() 
                    t[2] = t[2][1:]    
                    t[3] = ""
                else:
                    loc = t.index("more")+1#three genome only in this way
                    t[2] = dic2[t[loc]].split()[2]+"	"+dic2[t[loc]].split()[3] 
                    t[3] = dic2[t[loc]].split()[4]+"	"+dic2[t[loc]].split()[5]
                    t[6] = int(dic2[t[loc]].split()[5])-int(dic2[t[loc]].split()[4]) + int(t[6])+1
                for p in t:
                    if p == "":
                        continue
                    else:
                        print(p,end ="	",file = goout)
                print("",file = goout)
                
            else:
                if len(infif[j-1].split())>7:
                    continue
                else:
                    print(infif[j].strip(),file = goout)
    goout.close()

                
                    
            
           
Gathergoc(goc1,goc2,gocout)  
























