#!/bin/bash
samtools=$1
goin=$2
chr=$3
pos1=$4
pos2=$5
echo "${samtools}samtools view ${goin} ${chr}:${pos1}-${pos2} -b -o ${goin}_${chr}_${pos1}_${pos2}.bam"
${samtools}samtools view ${goin} ${chr}:${pos1}-${pos2} -b -o ${goin}_${chr}_${pos1}_${pos2}.bam
echo "${samtools}samtools depth ${goin}_${chr}_${pos1}_${pos2}.bam > ${goin}_${chr}_${pos1}_${pos2}.bam.depth"
${samtools}samtools depth ${goin}_${chr}_${pos1}_${pos2}.bam > ${goin}_${chr}_${pos1}_${pos2}.bam.depth
