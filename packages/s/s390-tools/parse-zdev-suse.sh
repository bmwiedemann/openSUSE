#!/bin/bash

for zdev in $(getargs rd.zdev -d 'rd_ZDEV='); do
    IFS=, read -r z_drv z_chan znet_opts <<< "$zdev"
    if [ -n "$z_drv" ] && [ "$z_drv" = "no-auto" ] ; then
        : # ignore, as it's handled by 95zdev
    elif [ -z "$z_drv" ] || [ -z "$z_chan" ]; then
        warn "Invalid arguments for rd.zdev="
    else
	info "+ chzdev --persistent --enable [...] $z_drv $z_chan $z_opts"
	chzdev --persistent --enable --force --yes --no-root-update --no-settle $z_drv $z_chan $z_opts
    fi
done

# REMOVE everything below for FCS!
# support initial implementation only for already deployed `parmfile`s
for znet in $(getargs rd.znet -d 'rd_ZNET='); do
    IFS=, read -r znet_drv znet_sc0 znet_sc1 znet_sc2 znet_options <<< "$znet"
    if [ -z "$znet_drv" ] || [ -z "$znet_sc0" ] || [ -z "$znet_sc1" ] || [ -z "$znet_sc2" ] ; then
        warn "Invalid arguments for rd.znet="
    else
	info "+ chzdev --persistent --enable $znet_drv $znet_sc0:$znet_sc1:$znet_sc2 $znet_options"
	chzdev --persistent --enable --force --yes --no-root-update --no-settle $znet_drv $znet_sc0:$znet_sc1:$znet_sc2 $znet_options
    fi
done

for dasd in $(getargs rd.dasd -d 'rd_DASD='); do
    dasd_drv=dasd
    IFS=, read -r dasd_sc0 dasd_options <<< "$dasd"
    if [ -z "$dasd_sc0" ]; then
        warn "Invalid arguments for rd.dasd="
    else
	info "+ chzdev --persistent --enable $dasd_drv $dasd_sc0 $dasd_options"
	chzdev --persistent --enable --force --yes --no-root-update --no-settle $dasd_drv $dasd_sc0 $dasd_options
    fi
done

