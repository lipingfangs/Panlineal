#!/usr/bin/env python
# Copyright (C) <2020> PMBL;South China Agricultural University. All rights reserved
__author__ = "Write by Fangping Li"
__version__ = '0.1.0'

import argparse
import sys
import os

def get_options():
    example = "Panlineal.py -l location.lg  -p example.pair.cfg -t 20 -all yes -o refquery -f 1000 -clean yes " 
    description = "Create one-by-one read-pairs and sv compare  example: " + example
    parser = argparse.ArgumentParser(description = description,prog = 'Panlineal.py')
    parser.add_argument('-p', '--pairguide', action='store',type=str,help='input your pairguide file')
    parser.add_argument('-t', '--threads', action='store',type=int,help='how many thread do you want to use')
    parser.add_argument('-all', '--runall', action='store',default="yes",choices=('yes','no'),
    type=str,help='if yes: run multiple sequence of whole process, generate the pan genome file; if no:just splice; default yes')
    parser.add_argument('-o', '--output', action='store',type=str,
                         help='name of the  pan-genome output: <-o>.fasta',default="output")
    parser.add_argument('-f', '--flitersize', action='store',type=int,
                         help="fliter size of SV; default 1000",default=1000)
    parser.add_argument('-l', '--location', action='store',type=str,
                         help='location of software "mummer" "lastz" and "svmu',default="location.lg")
    parser.add_argument('-r', '--rangefliter', action='store',type=int,help='SVs distance between red and query; default 3000000',default=3000000)   
    parser.add_argument('-merge', '--merge', action='store',type=str,choices=('yes','no'),
                             help='merge .goc and generate the final location file; default yes',default="yes")
    parser.add_argument('-clean', '--clean', action='store',type=str,choices=('yes','no'),
                             help='Clean all of the middle file!; default no',default="no")
    parser.add_argument('--version', action='version',version='%(prog)s '+__version__+" "+__author__)
    
    return parser.parse_args()

gosome = get_options()
location = gosome.location
parame = open(location,"r") #mum lastz svmu samtools bowtie2 location
parameline = list(parame.readlines())
parame.close()

pairguide = gosome.pairguide
threads = gosome.threads
runall = gosome.runall
output = gosome.output
flitersize = gosome.flitersize
clean = gosome.clean
rangefliter = gosome.rangefliter
#sys.argv[2] #Secondgenome

ref = parameline[5].split("=")[1].strip()#sys.argv[1] #Firstgenome
print(ref)
querylist = parameline[6].split("=")[1].strip().split(",")
roundcountn = 0
roundcount = open("roundcount","w")
print(roundcountn)
print(str(roundcountn) ,file = roundcount)
roundcount.close()


if len(querylist) > 1:
    for query in querylist:
        roundcount = open("roundcount","w")
        roundcountn += 1
        print(roundcountn,file = roundcount)
        roundcount.close() 
        commandpair = "awk '{print $1,$"+str(roundcountn+1)+"}' "+ pairguide+"> "+pairguide+".cyc" 
        print(commandpair)
        os.system(commandpair)
        pairguidec = pairguide+".cyc" 
        command = "multiple.py -1 "+ref+" -2 "+query+" -p "+pairguidec+" -t "+str(threads)+" -all "+runall+" -o temp"+str(roundcountn)+".fasta -f "+str(flitersize)+" -t "+str(threads)+" -l "+ location+" -clean "+ clean +" -r "+str(rangefliter)
        print(command)
        os.system(command)
        ref = "temp"+str(roundcountn)+".fasta"

        
    os.system("mv temp"+str(roundcountn)+".fasta "+output+".fasta")
    
        
else:
    print(querylist)
    query=querylist[0]
    roundcount = open("roundcount","w")
    roundcountn += 1
    command = "multiple.py -1 "+ref+" -2 "+query+" -p "+pairguide+" -t "+str(threads)+" -all "+runall+" -o temp"+str(roundcountn)+".fasta -f "+str(flitersize)+" -t "+str(threads)+" -l "+ location+" -clean "+ clean +" -r "+str(rangefliter)
    os.system(command)
    print(roundcountn,file = roundcount)
    roundcount.close() 

    
if gosome.merge ==  "yes":
    print("Auto merge!")
    roundcount = open("roundcount","r")
    roundcountn = list(roundcount.readlines())[0]
    roundcount.close()
    k = int(roundcountn)
    for i in range(k-1):
        if i == 0:
            f = i
            p = i + 1
            o = i + 2
            goin1 = "temp"+str(p)+".fasta.goc"
            goin2 = "temp"+str(o)+".fasta.goc"
            goout = "temp"+str(f)+"temp.fasta.goc"
            commandgather = "Gathergoc.py "+goin1+" "+goin2+" "+goout
            print(commandgather)
            os.system(commandgather)

            
        else:
            f = i
            goin1 = goout
            goout = "temp"+str(f)+"temp.fasta.goc"
            o = i + 2
            goin2 = "temp"+str(o)+".fasta.goc"
            commandgather = "Gathergoc.py "+goin1+" "+goin2+" "+goout
            print(commandgather)
            os.system(commandgather)
            
        
        
    
    
    
    
os.system("mv  temp"+str(i)+"temp.fasta.goc "+output+".fasta.goc")
   
    
print("Your output is "+output+".fasta") 
print("Your output is "+output+".fasta.goc")     
