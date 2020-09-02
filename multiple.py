#!/usr/bin/env python
# Copyright (C) <2020> PMBL;South China Agricultural University. All rights reserved
__author__ = "Write by Fangping Li"
__version__ = '0.1.0'

import argparse
import sys
import os

def get_options():
    example = "./multiple.py -1 ref.fa -2 query.fa -p example.pair.cfg -t 20 -all yes -o refquery -f 1000 -l location.lg" 
    description = "Create one-by-one read-pairs and sv compare  example: " + example
    parser = argparse.ArgumentParser(description = description,prog = 'multiple.py')
    parser.add_argument('-1', '--reference', action='store',type=str,help='input your reference .fasta')
    parser.add_argument('-2', '--query', action='store',type=str,help='input your query .fasta') 
    parser.add_argument('-p', '--pairguide', action='store',type=str,help='input your pairguide file')
    parser.add_argument('-t', '--threads', action='store',type=int,help='how many thread do you want to use')
    parser.add_argument('-all', '--runall', action='store',default="no",choices=('yes','no'),
                        type=str,
                        help='if yes: run multiple sequence of whole process, generate the pan genome file; if no:just splice')
    parser.add_argument('-o', '--output', action='store',type=str,
                         help='name of the  pan-genome output: <-o>.fasta',default="output")
    parser.add_argument('-f', '--flitersize', action='store',type=int,
                         help='fliter size of SV',default=1000)
    parser.add_argument('-r', '--rangefliter', action='store',type=int,help='SVs distance between red and query',default=1000000)
    parser.add_argument('-l', '--location', action='store',type=str,
                         help='location of software "mummer" "lastz" and "svmu"',default=1000)
    parser.add_argument('-clean', '--clean', action='store',type=str,choices=('yes','no'),
                             help='Clean all of the middle file!"',default="no")
    
    
    parser.add_argument('--version', action='version',version='%(prog)s '+__version__+" "+__author__)
    
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
rangefliter = gosome.rangefliter
print(seq1)
print(seq2)
seqdic1 = seqfileread(seq1)
seqdic2 = seqfileread(seq2)

print("Sequence read done!")

pairfile = open(gosome.pairguide,"r")#sys.argv[3]#svguidefile
pairfileline = list(pairfile.readlines())

location = gosome.location

pairfile.close()
parame = open(location,"r") #mum lastz svmu location
parameline = list(parame.readlines())
mum = parameline[0].split("=")[1]
lastz = parameline[1].split("=")[1]
svmu = parameline[2].split("=")[1]
parame.close()



golist = open("golist","w")

count = 0
for i in pairfileline:#for SVs mining
    count += 1
    print(i)
    i = i.split()
    print(i)
    os.system("mkdir panchr"+ str(count))
    go1 = open("panchr"+ str(count)+"/Refchr"+str(count),"w")
    tempref = "panchr"+ str(count)+"/Refchr"+str(count)
    print(">"+ i[0].strip(),file = go1 )
    print(seqdic1[i[0].strip()],file = go1)
    go2 = open("panchr"+ str(count)+"/Quechr"+str(count),"w")
    tempquery = "panchr"+ str(count)+"/Quechr"+str(count)
    print(">"+ i[1].strip(),file = go2 )
    print(seqdic2[i[1].strip()],file = go2)
    go1.close()
    go2.close()
    print("bash mumlastzsvmu.sh "+mum.strip()+" "+lastz.strip()+" "+svmu.strip()+" "+tempref.strip()+" "+tempquery.strip()+" "+gosome.output+str(count)+" "+str(gosome.threads)+" "+str(gosome.flitersize), file = golist)
    

golist.close()

na = os.system("parallel --jobs "+str(gosome.threads)+" < golist")
if na == 0:
    print("Splice done!")
else:
    print("error!")

if gosome.runall == "yes":#begin to generate the lineal pan-genome
    goout = gosome.output+str(count)
    fliter = str(gosome.flitersize)
    
    print("-all yes; Go to create lineal pangenome!")
    count = 0
    for i in pairfileline:
        count += 1
        goout = gosome.output
        svguide = goout+str(count)+"."+fliter+".txt"#svguide temp1.fasta1.1000.txt
        print(svguide)
        command = "creatpangenome.py -1 "+"panchr"+ str(count)+"/Refchr"+str(count)+" -2 "+"panchr"+str(count)+"/Quechr"+str(count)+" -g "+svguide+" -o XXXXoutput"+str(count)+" -r "+str(rangefliter)
        print(command)
        os.system(command)
        
    os.system("cat XXXXoutput*.fasta > "+goout)#gather and create the final file
    os.system("cat XXXXoutput*.goc > "+goout+".goc")#gather and create the final file
    os.system("rm XXXXoutput*")
    print("Your output is "+goout+"pan.genome.fasta")
    print("finish")
    
else:
    print("finish")
    
if gosome.clean == "yes":
    os.system("rm *txt")
    os.system("rm -rf panchr*")
    os.system("rm *.fi")
    os.system("rm *delta")
    os.system("rm *.fichr01")














