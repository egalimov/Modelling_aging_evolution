#source activate pandas

while read p; do

while read p2; do
  #echo $p $p2
  python3 main2.py $p $p2

done <1_parameters_2.txt
done <1_parameters_1.txt

afplay ~/music/music.mp3
