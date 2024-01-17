#!/bin/sh
# Get truncated Hipparcos catalog for testing
# Truncate the Hipparcos catalog to stars with magnitude brighter than 6.6
# corresponds to last line of
# https://github.com/skyfielders/python-skyfield/blob/master/builders/Makefile 
# but with an SSL secured URL for the source (boo#1182424)
URL="https://cdsarc.cds.unistra.fr/ftp/I/239/hip_main.dat"
curl "$URL" | awk -F\| '$6 <= 6.6 || $2 == 87937' | gzip -c -9 > hip_main.dat.gz
