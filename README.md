PanLineal: A new concept and pipeline of constructing and utilization linear pan-genome from de novo assembled genome
--------------------


**Install** 

git clone https://github.com/lipingfangs/Panlineal.git

cd Panlineal

python setup.py install

**Attention**

This Pipeline rely on Mummer, Lastz, bowtie2, samtools and svmu; Users need to write path of these at file location.lg   

This pipeline only support one-line .fasta format

For example 

Support this:

>1dna_chromosomechromosome_IRGSP-1.0_1_1_43270923_1REF
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

But not this

>1dna_chromosomechromosome_IRGSP-1.0_1_1_43270923_1REF
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

Script goone.py in this package is able to convey these format

***usage:***

python goone.py <in.fasta> <out.fasta>

***Usage for this programme:***
These programme was divided into Pan-genome forming(Panlineal.py) and SVs mapping(mappingtools.py). Create a optimal reference genome based on short reads from pan-genome (bestref.py) 

>Panlineal.py -h ;for help
```
usage: Panlineal.py [-h] [-p PAIRGUIDE] [-t THREADS] [-all {yes,no}]
                    [-o OUTPUT] [-f FLITERSIZE] [-l LOCATION] [-r RANGEFLITER]
                    [-merge {yes,no}] [-clean {yes,no}] [--version]

Create one-by-one read-pairs and sv compare example: Panlineal.py -l location.lg -p example.pair.cfg -t 20 -all yes -o refquery -f 1000 -clean yes

optional arguments:
  -h, --help            show this help message and exit
  -p PAIRGUIDE, --pairguide PAIRGUIDE
                        input your pairguide file                    
  -t THREADS, --threads THREADS
                        how many thread do you want to use                    
  -all {yes,no}, --runall {yes,no}
                        if yes: run multiple sequence of whole process,
                        generate the pan genome file; if no:just splice;
                        default yes             
  -o OUTPUT, --output OUTPUT
                        name of the pan-genome output: <-o>.fasta                     
  -f FLITERSIZE, --flitersize FLITERSIZE
                        fliter size of SV; default 1000                
  -l LOCATION, --location LOCATION
                        location of software "mummer" "lastz" and "svmu                 
  -r RANGEFLITER, --rangefliter RANGEFLITER
                        SVs distance between red and query; default 1000000                   
  -merge {yes,no}, --merge {yes,no}
                        merge .goc and generate the final location file;
                        default yes                   
  -clean {yes,no}, --clean {yes,no}
                        Clean all of the middle file!; default no                  
  --version             show program's version number and exit
```
>mappingtools.py -h ;for help

```
usage: mappingtools.py [-h] [-i INPAN] [-t THREADS] [-b INBASE] [-1 PAIREND1]
                       [-2 PAIREND2] [-l LOCATION] [-g GOCGUIDE] [-o OUTPUT]
                       [-c COVFLITER] [-clean {yes,no}] [-create {yes,no}]

Create one-by-one mapping and pav example: mappingtools.py -i pangenome.fa -1
illnumina_R1.fq.gz -2 illnumina_R3.fq.gz -g guide.goc -l location.lg -o
outputcov -c 5

optional arguments:
  -h, --help            show this help message and exit
  -i INPAN, --inpan INPAN
                        input your reference .fasta
  -t THREADS, --threads THREADS
                        how many thread do you want to use
  -b INBASE, --inbase INBASE
                        how many base-pair will you consider it as a total
                        insertion rather than a replace
  -1 PAIREND1, --pairend1 PAIREND1
                        input your pairend1 .fastq
  -2 PAIREND2, --pairend2 PAIREND2
                        input your pairend2 .fastq
  -l LOCATION, --location LOCATION
                        location of software "mummer" "lastz" and
                        "svmu","samtools","bowtie"
  -g GOCGUIDE, --gocguide GOCGUIDE
                        input your .goc file generated by multiple.py
  -o OUTPUT, --output OUTPUT
                        name of the pan-genome coverage output
  -c COVFLITER, --covfliter COVFLITER
                        coverage fliter
  -clean {yes,no}, --clean {yes,no}
                        Clean all of the middle file!
  -create {yes,no}, --createfasta {yes,no}
                        Create a optimal reference genome for short read
```

>bestref.py -h ;for help

```
usage: bestref.py [-h] [-i INPAN] [-o OUTPUT] [-g GOCGUIDE] [-hap HAPCGUIDE]

Create a optimal reference genome based on short reads from pan-genome:
bestref.py -i pangenome.fa -hap goin.hapc -g guide.goc -l location.lg -o
output

optional arguments:
  -h, --help            show this help message and exit
  -i INPAN, --inpan INPAN
                        input your reference .fasta
  -o OUTPUT, --output OUTPUT
                        name of the pan-genome coverage output
  -g GOCGUIDE, --gocguide GOCGUIDE
                        input your .goc file generated by mappingtools.py
  -hap HAPCGUIDE, --hapcguide HAPCGUIDE
                        input your .hapc file generated by mappingtools.py

```
Hapmerge.py module is able to intergrate the hapc file 
>Hapmerge.py -h 
```
usage: Hapmerge.py [-h] [-l HAPLIST] [-o OUTPUT] [--version]

Merge .hapc file; example: Hapmerge -l merge.li -o haplistmergeout.hapcs

optional arguments:
  -h, --help            show this help message and exit
  -l HAPLIST, --haplist HAPLIST
                        list file of .hapc files ready to be merged
  -o OUTPUT, --output OUTPUT
                        name of output .hapn file
  --version             show program's version number and exit

```

**.cfg and .lg file is necessary for this programme** 

**Enter files format:**

1.  example.pair.cfg:
<ref.chromosome1> <query.Homologous.chromosome1>  
<ref.chromosome2> <query.Homologous.chromosome2>
...

example:

>Chr1	chr01  
Chr2	chr02  
Chr3	chr03  

2.  location.lg

Mummer=<Dir of software mummer>  
Lastz=<Dir of software lastz>   
svmu=<Dir of software svmu>    
bowtie2=<Dir of software bowtie2>   
samtools=<Dir of software samtools>    
ref=<reference sequence .fasta>  
query=<query1 sequence .fasta>,<query2 sequence .fasta>,......  

example:

>Mummer=/home/lfp/soft/mummer-4.0.0beta2/  
Lastz=/home/lfp/soft/lastz-master/src/  
svmu=/home/lfp/soft/svmu/  
bowtie2=/home/lfp/miniconda3/bin/  
samtools=/home/lfp/miniconda3/bin/  
ref=Oryza_IRGSP-1.0_genome.1m.fasta  
query=Oryza_HJX74_top_level_v2.2.1m.fa,Oryza_R498_Chr.1m.fa  

When need to merge the .hapc:
merge.li format is necessary for Hapmerge.py input

<1.hapc>,<2.hapc>,<3.hapc>...

for example:
>P133-DSW43038-S_L1-pan.cov.hapc,P208-DSW43111-S_L4-pan.cov.hapc,P229-DSW43149-S_L5-pan.cov.hapc,P236-DSW43156-S_L5-pan.cov.hapc,P54-DSW42960-S_L7-pan.cov.hapc.P91-DSW42997-S_L1-pan.cov.hapc


Result files explaination
-----------------------------

**xxx.fasta (Pan-genome after Panlineal.py alignment and Vgs based Linearized integration)**

For example:
```
>chr10
TAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTTAAC
ACGTTCTGAATATATGTTTCATATATTATCTATATTTTTATTATTTTCAGAAGTTTTTTAAAATTCAAAACATATTTTTAG
TGTGTTCTCCTTATTTTCTAACTATTTTAATGATTTTAAGTTGAAATTATATAAATATAAATTCTATAAGATTCTAAACATTGTAAATAGATCATTCACGTATTATCTATACTTTAGTTTTTAATGTATTATTTTTATTATGCAATGTATTACTTTTAATTTTTA
```

**xxx.goc (file for recording corresponding Vgs Multidirectional branch information of Pan-genome(xxx.fasta) after Panlineal.py alignment and Vgs based Linearized integration)**
File format:

OrgID<the ID of SVs location>	Chr<chromosome>	Start1<PAV1 start location>	end1<PAV1 end location>	Start2<PAV2 or more start location>	end2<PAV2 or more end location>	length<total insertion length> if "more" appears in the row mean this locus has more than 2 kinds of PAVs locus 

For example:
```
OrgID	Chr	Start1	end1	Start2	end2	length
1-1-chr10	chr10	81013	81013	81014	84495	3482
1-2-chr10	chr10	171843	171843	171844	172376	533
2-1-chr10	chr10	172379	172379	172380	173876	1497
2-2-chr10	chr10	213521	213616	213617	215808	2192
2-3-chr10	chr10	217433	217433	217434	218610	1177
2-4-chr10	chr10	243894	246549	246550	252770	6221
1-3-chr10	chr10	268308	268309	268310	268925	616
2-5-chr10	chr10	276199	276632	276633	277254	622
2-6-chr10	chr10	279697	280326	280327	282045	1719
2-7-chr10	chr10	365487	365487	365488	366046	559
2-8-chr10	chr10	395016	395016	395017	399115	4099
2-13-chr10	chr10	1338940	1339015	1339016	1343068	1343069	1344198	5183	more	1-17-chr10

```

























