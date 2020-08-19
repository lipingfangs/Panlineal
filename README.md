##Panlineal
Here is a pipeline to generate lineal pan-genome
--------------------


#Install  

git clone https://github.com/lipingfangs/Panlineal.git
cd Panlineal
python setup.py install

#Attention 
This Pipeline rely on Mummer Lastz and svmu
This pipeline only support one-line .fasta format

Support this:

>1dna_chromosomechromosome_IRGSP-1.0_1_1_43270923_1REF
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

But not this

>1dna_chromosomechromosome_IRGSP-1.0_1_1_43270923_1REF
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

Script goone.py in this package is able to convey these format
usage:
python goone.py <in.fasta> <out.fasta>

#Usage for this pipeline：
multiple.py -h for help
--------------------

##Enter files format:
1.  example.pair.cfg:
<ref.chromosome1> <query.Homologous.chromosome1>
<ref.chromosome2> <query.Homologous.chromosome2>
.
.
.

example:

Chr1	chr01

Chr2	chr02

Chr3	chr03

2.  location.lg

Mummer=<Dir of software mummer>
  
Lastz=<Dir of software lastz> 
  
svmu=<Dir of software svmu>
  
example:

Mummer=/home/lfp/soft/mummer-4.0.0beta2/

Lastz=/home/lfp/soft/lastz-master/src/

svmu=/home/lfp/soft/svmu/

  


