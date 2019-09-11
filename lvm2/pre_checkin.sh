#!/usr/bin/env bash

master="lvm2.spec"
sections="COMMON-DEF COMMON-PATCH COMMON-PREP COMMON-CONFIG"
for slave in device-mapper.spec lvm2-clvm.spec; do
{
    prev=1
    for section in $sections; do
        begin="/$section-BEGIN/"
        end="/$section-END/"
        sed -n -e "${prev},${begin}p" $slave
        sed -n -e "${begin},${end}p" $master | head -n -1 | tail -n +2
        prev=$end
    done
    sed -n -e "${prev},\$p" $slave
} > $slave.tmp && mv $slave.tmp $slave
done

# changelogs

cp lvm2.changes lvm2-clvm.changes
cp lvm2.changes device-mapper.changes
