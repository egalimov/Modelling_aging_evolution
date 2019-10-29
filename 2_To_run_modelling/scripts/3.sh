#!/bin/bash -l
#$ -l h_rt=12:00:00
#$ -l mem=2G
#$ -l tmpfs=10G
#$ -t 1
#$ -N analyse8
#$ -wd /home/ucbtega/Scratch/1_work1/8_var
#$ -o /home/ucbtega/Scratch/1_work1/8_var/sgelog
#These are optional flags but you problably want them in all jobs
#$ -j y
#The code you want to run now goes here.


pwd1=`pwd`
path1="$pwd1/run3_fast.py" 
a="$( bash <<EOF
echo $(grep -rnw $path1 -e 'ct2=')
EOF
)"


b="$( bash <<EOF
echo $(echo $a | cut -d'=' -f2-)
EOF
)"
echo $b 
path_to_copy=$pwd1/result/$b
path_to_copy+='_csv'
echo $path_to_copy


cp analyse_repilcas_uni_adul+L2S-max.py $path_to_copy
cp 0_pictures.py $path_to_copy 
cp 2_pictures.py $path_to_copy
cp run3_fast.py $path_to_copy


cd $path_to_copy

module load python3/3.6
while read p; do
  python3 analyse_repilcas_uni_adul+L2S-max.py $p 100
done <list_files.csv


python3 0_pictures.py '/tables'
python3 0_pictures.py '/tables_no0'

python3 2_pictures.py '/tables'
python3 2_pictures.py '/tables_no0'













