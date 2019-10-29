#!/bin/bash -l
jobid=$(qsub fast_qsub.owain_prep.sh)
echo $jobid

jobid2=$(echo $jobid | cut -d. -f1)
echo $jobid2
jobid22=$(echo $jobid2 | cut -d ' ' -f3)
echo $jobid22
jobid3=$(qsub -hold_jid $jobid22 2.sh)
echo $jobid3
jobid4=$(echo $jobid3 | cut -d. -f1)
echo $jobid4
jobid5=$(echo $jobid4 | cut -d ' ' -f3)
echo $jobid5
jobid6=$(qsub -hold_jid $jobid5 3.sh)
echo $jobid6

