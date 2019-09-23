#!/bin/bash
if [ `ulimit -v` -le 2500000 ] ; then
  echo "build does not work on `hostname`: not enough memory"
  exit 1
fi

