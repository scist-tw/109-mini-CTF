#!/bin/bash
for dir in $(ls -d */); do
  echo
  echo $dir
  ./$dir/solve*
done
