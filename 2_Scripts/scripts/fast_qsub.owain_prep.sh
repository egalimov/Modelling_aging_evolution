#!/bin/bash -l
#$ -l h_rt=12:00:00
#$ -l mem=2G
#$ -l tmpfs=10G
#$ -t 1-4500
#$ -N main_8
#$ -wd /home/ucbtega/Scratch/1_work1/8_var
#$ -o /home/ucbtega/Scratch/1_work1/8_var/sgelog
#These are optional flags but you problably want them in all jobs
#$ -j y
hostname
date

cd /home/ucbtega/Scratch/1_work1/8_var
module load python3/3.6
p1=`cat 1_parameters_1_100.txt | head -$SGE_TASK_ID | tail -1 | cut -f $SGE_TASK_ID -d " "`
p2=`cat 1_parameters_2_100.txt | head -$SGE_TASK_ID | tail -1 | cut -f $SGE_TASK_ID -d " "`


python3 run3_fast.py $p1 $p2



