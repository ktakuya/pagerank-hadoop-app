#!/bin/sh

input=""
output=""
error_msg="Usage: pagerank.sh [-i input] [-o output]"

while getopts "i:o:" option
do
  case $option in
    i)
      input="$OPTARG"
      ;;
    o)
      output="$OPTARG"
      ;;
    \?)
      echo "$error_msg" 1>&2
      exit 1
      ;;
  esac
done

if [ "$input" = "" ]; then
  echo "$error_msg" 1>&2
  exit 1
fi
if [ "$output" = "" ]; then
  echo "$error_msg" 1>&2
  exit 1
fi
cat "$input" | python src/mapreduce/job3/mapper.py | sort -n -r > "$output"

