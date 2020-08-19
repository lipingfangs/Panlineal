#!/bin/bash
mummer=$1
lastz=$2
svmu=$3
goin1ref=$4
goin2query=$5
goout=$6
thread=$7
filter=$8
echo "${mummer}nucmer --threads ${thread} --prefix=${goout} ${goin1ref} ${goin2query}";
${mummer}nucmer --threads ${thread} --prefix=${goout} ${goin1ref} ${goin2query};
echo "${lastz}lastz ${goin1ref} ${goin2query}  --chain  --format=general:name1,strand1,start1,end1,name2,strand2,start2,end2 > ${goout}_lastz.txt";
${lastz}lastz ${goin1ref} ${goin2query}  --chain  --format=general:name1,strand1,start1,end1,name2,strand2,start2,end2 > ${goout}_lastz.txt;
echo "${svmu}svmu ${goout}.delta  ${goin1ref} ${goin2query} h ${goout}_lastz.txt  ${goout}";
${svmu}svmu ${goout}.delta  ${goin1ref} ${goin2query} h ${goout}_lastz.txt ${goout};
filter=1000; #default 1000
nine=9;
zero=0;
echo "cat sv.${goout}.txt | grep "INS" | awk '"$nine">"$filter"{print "$zero"}' > ${goout}.${filter}.txt;";
cat sv.${goout}.txt | grep "INS" | awk '"$nine">"$filter"{print "$zero"}' > ${goout}.${filter}.txt;
