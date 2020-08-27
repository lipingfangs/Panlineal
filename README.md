Panlineal:A pipeline to generate lineal pan-genome
--------------------


**Install** 

git clone https://github.com/lipingfangs/Panlineal.git

cd Panlineal

python setup.py install

**Attention**

This Pipeline rely on Mummer, Lastz, bowtie2, samtools and svmu; User need to write path of these at file location.lg   

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
>mappingtools.py -h ;for help

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

  


