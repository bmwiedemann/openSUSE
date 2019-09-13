#!/bin/sh

# run in root directory of extracted intel-media-driver sources
for i in \
  $(grep -r RegisterDevice .| \
    grep 0x | \
    cut -d "(" -f2 | \
    cut -d "," -f1 | \
    tr [:lower:] [:upper:] | \
    sort -u); do 
  echo "Supplements:    modalias(xorg-x11-server:pci:v00008086d0000${i}sv*sd*bc*sc*i*)"
done
