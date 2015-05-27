#!/bin/bash

cat input.txt| python3 ../src/mapreduce/job1/mapper.py|sort|python3 ../src/mapreduce/job1/reducer.py|python3 ../src/mapreduce/job2/mapper.py|sort|python3 ../src/mapreduce/job2/reducer.py|python3 ../src/mapreduce/job3/mapper.py|sort -nr|diff - output.txt > diff.out
if [ -s diff.out ]; then
  echo "Failed"
  cat diff.out
else
  echo "Passed"
fi
