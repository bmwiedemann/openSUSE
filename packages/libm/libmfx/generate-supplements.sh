#!/bin/sh

# run in root directory of extracted MediaSDK-intel-mediasdk sources
for i in \
  $(grep ", MFX_HW" api/mfx_dispatch/linux/device_ids.h | \
    grep 0x | \
    sed 's/.*{.*0x//g' | \
    cut -d "," -f1 | \
    tr [:lower:] [:upper:] | \
    sort -u); do 
  echo "Supplements:    modalias(xorg-x11-server:pci:v00008086d0000${i}sv*sd*bc*sc*i*)"
done
