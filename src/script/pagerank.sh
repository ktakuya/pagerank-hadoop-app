#!/bin/sh

itern=0
errormsg="Usage: pagerank.sh [-n]"

while getopts "n:" option
do
  case $option in
    n)
      itern="$OPTARG"
      ;;
    \?)
      echo "$errormsg" 1>&2
      exit 1
      ;;
  esac
done

if [ $itern -eq 0 ]; then
  echo "$errormsg" 1>&2
  exit 1
fi

command="hadoop jar /usr/local/Cellar/hadoop/2.7.0/libexec/share/hadoop/tools/lib/hadoop-streaming-2.7.0.jar -mapper mapper.py -reducer reducer.py -file src/mapreduce/job2/mapper.py -file src/mapreduce/job2/reducer.py -input /line/iter"$itern" -output /line/iter"$(expr "$itern" + 1)""

$command
