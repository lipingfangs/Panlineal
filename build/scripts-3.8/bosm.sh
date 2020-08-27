#!/bin/bash
Bowtie=$1
ref=$2
samtools=$3
in1=$4
in2=$5
outname=$6
theard=$7
echo "${Bowtie}bowtie2 -p ${theard} -x ${ref} -1 ${in1} -2 ${in2} -S ${outname}.sam;"
${Bowtie}bowtie2 -p ${theard} -x ${ref} -1 ${in1} -2 ${in2} -S ${outname}.sam;
echo "${samtools}samtools view  -@ ${theard} -S ${outname}.sam -b -o ${outname}.bam;"
${samtools}samtools view  -@ ${theard} -S ${outname}.sam -b -o ${outname}.bam;
echo "${samtools} sort  -@ ${theard}  ${outname}.bam ${outname}.sort;"
${samtools}samtools sort  -@ ${theard} -o ${outname}.sort.bam ${outname}.bam
${samtools}samtools index ${outname}.sort.bam
