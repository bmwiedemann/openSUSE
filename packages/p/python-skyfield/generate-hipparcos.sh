#!/bin/sh
# Get truncated Hipparcos catalog for testing
# Truncate the Hipparcos catalog to stars with magnitude brighter than 6.6
# corresponds to last line of
# https://github.com/skyfielders/python-skyfield/blob/master/builders/Makefile 
URL=http://cdsarc.u-strasbg.fr/ftp/cats/I/239/hip_main.dat.gz 
curl "$URL" | zcat | awk -F\| '$6 <= 6.6 || $2 == 87937' | gzip -c -9 > hip_main.dat.gz
