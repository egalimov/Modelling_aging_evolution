#!/bin/bash -l
#$ -l h_rt=12:00:00
#$ -l mem=2G
#$ -l tmpfs=10G
#$ -t 1
#$ -N save_res8
#$ -wd /home/ucbtega/Scratch/1_work1/8_var
#$ -o /home/ucbtega/Scratch/1_work1/8_var/sgelog
#These are optional flags but you problably want them in all jobs
#$ -j y
#The code you want to run now goes here.

hostname
date

cd /home/ucbtega/Scratch/1_work1/8_var
module load python3/3.6

python3 save_res.py















