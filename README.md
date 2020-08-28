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
These programme was divided into Pan-genome forming(Panlineal.py) and SVs mapping(mappingtools.py);

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
                       [-c COVFLITER] [-clean {yes,no}]
Create one-by-one mapping and pav example: mappingtools.py -i pangenome.fa -1 illnumina_R1.fq.gz -2 illnumina_R3.fq.gz -g guide.goc -l location.lg -o  outputcov -c 5
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
                        Clean all of the middle file!"
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

  


