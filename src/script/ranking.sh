#!/bin/sh

iter_n=0
error_msg="Usage: pagerank.sh [-n]"

while getopts "n:" option
do
  case $option in
    n)
      iter_n="$OPTARG"
      ;;
    \?)
      echo "$error_msg" 1>&2
      exit 1
      ;;
  esac
done

if [ $iter_n -eq 0 ]; then
  echo "$error_msg" 1>&2
  exit 1
fi

command="hadoop jar /usr/local/Cellar/hadoop/2.7.0/libexec/share/hadoop/tools/lib/hadoop-streaming-2.7.0.jar -mapper mapper.py -reducer NONE -file src/mapreduce/job3/mapper.py -input /line/iter"$iter_n" -output /line/output"

$command
