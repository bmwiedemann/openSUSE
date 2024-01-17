

# Look for the NPIV vport with the WWPN
#  $1 contains the WWPN  (assumes it does not contain a leading "0x")
find_vhost()
{
  unset vhost

  # look in upstream locations
  for fchost in /sys/class/fc_vports/* ; do
    if test -e $fchost/port_name ; then
      wwpn=`cat $fchost/port_name | sed -e s/^0x//`
      if test $wwpn = $1 ; then 
        # Note: makes the assumption the vport will always have an scsi_host child
        vhost=`ls -d $fchost/device/host*`
        vhost=`basename $vhost`
        return
      fi
    fi
  done

  # look in vendor-specific locations

  # Emulex - just looks like another scsi_host - so look at fc_hosts...
  for fchost in /sys/class/fc_host/* ; do
    if test -e $fchost/port_name ; then
      wwpn=`cat $fchost/port_name | sed -e s/^0x//`
      if test $wwpn = $1 ; then 
        # Note: makes the assumption the vport will always have an scsi_host child
        vhost=`basename $fchost`
        return
      fi
    fi
  done
}


# Create a NPIV vport with WWPN
#  $1 contains the VPORT WWPN
#  $2 may contain the VPORT WWNN
# (assumes no name contains a leading "0x")
create_vport()
{
  wwpn=$1
  wwnn=$2
  if [ -z "$wwnn" ]; then
    # auto generate wwnn, follow FluidLabUpdateForEmulex.pdf
    # Novell specific identifier
    # byte 6 = 0 indicates WWNN, = 1 indicates WWPN
    wwnn=${wwpn:0:6}"0"${wwpn:7}
  fi
  # find a base adapter with npiv support that is on the right fabric

  # Look via upstream interfaces
  for fchost in /sys/class/fc_host/* ; do
    if test -e $fchost/vport_create ; then
      # is the link up, w/ NPIV support ?
      pstate=`cat $fchost/port_state`
      ptype=`cat $fchost/port_type | cut -c 1-5`
      if [ $pstate = "Online" -a $ptype = "NPort" ] ; then
        vmax=`cat $fchost/max_npiv_vports`
        vinuse=`cat $fchost/npiv_vports_inuse`
        avail=`expr $vmax - $vinuse`
        if [ $avail -gt 0 ] ; then
          # create the vport
          echo $wwpn":"$wwnn > $fchost/vport_create
          if [ $? -eq 0 ] ; then
            return 0
          fi
          # failed - so we'll just look for the next adapter
        fi
      fi
    fi
  done

  # Look in vendor-specific locations

  # Emulex: interfaces mirror upstream, but are under adapter scsi_host
  for shost in /sys/class/scsi_host/* ; do
    if [ -e $shost/vport_create ] ; then
      fchost=`ls -d $shost/device/fc_host*`
      # is the link up, w/ NPIV support ?
      if [ -e $fchost/port_state ] ; then
        pstate=`cat $fchost/port_state`
        ptype=`cat $fchost/port_type | cut -c 1-5`
        if [ $pstate = "Online" -a $ptype = "NPort" ] ; then
          vmax=`cat $shost/max_npiv_vports`
          vinuse=`cat $shost/npiv_vports_inuse`
          avail=`expr $vmax - $vinuse`
          if [ $avail -gt 0 ] ; then
            # create the vport
            echo $wwpn":"$wwnn > $shost/vport_create
            if [ $? -eq 0 ] ; then
              return 0
            fi
            # failed - so we'll just look for the next adapter
          fi
        fi
      fi
    fi
  done

  # BFA are under adapter scsi_host
  for shost in /sys/class/scsi_host/* ; do
    if [ -e $shost/vport_create ] ; then
      fchost=`ls -d $shost/device/fc_host/*`
      # is the link up, w/ NPIV support ?
      if [ -e $fchost/port_state ] ; then
        pstate=`cat $fchost/port_state`
        ptype=`cat $fchost/port_type | cut -c 1-5`
        if [ $pstate = "Online" -a $ptype = "NPort" ] ; then
          # create the vport
          echo $wwpn":"$wwnn > $shost/vport_create
          if [ $? -eq 0 ] ; then
            return 0
          fi
          # failed - so we'll just look for the next adapter
        fi
      fi
    fi
  done

  return 1
}


# Look for the LUN on the indicated scsi_host (which is an NPIV vport)
#  $1 is the scsi_host name (normalized to simply the hostX name)
#  $2 is the WWPN of the tgt port the lun is on
#       Note: this implies we don't support a multipath'd lun, or we
#         are explicitly identifying a "path"
#  $3 is the LUN number of the scsi device
find_sdev()
{
  unset dev
  hostno=${1/*host/}
  for sdev in /sys/class/scsi_device/${hostno}:*:$3 ; do
    if test -e $sdev/device/../fc_trans*/target${hostno}*/port_name ; then
      tgtwwpn=`cat $sdev/device/../fc_trans*/target${hostno}*/port_name | sed -e s/^0x//`
      if test $tgtwwpn = $2 ; then
        if test -e $sdev/device/block* ; then
          dev=`ls $sdev/device/block*`
          dev=${dev##*/}
          return
        fi
      fi
    fi
  done
}


# Look for the NPIV vhost based on a scsi "sdX" name
#   $1 is the "sdX" name
find_vhost_from_dev()
{
   unset vhost
   hostno=`readlink /sys/block/$1/device`
   hostno=${hostno##*/}
   hostno=${hostno%%:*}
   if test -z "$hostno" ; then return; fi
   vhost="host"$hostno
}


# We're about to terminate a vhost based on a scsi device
# Flush all nodes on that vhost as they are about to go away
#  $1 is the vhost
flush_nodes_on_vhost()
{ 
  if test ! -x /sbin/blockdev ; then  return;  fi
  hostno=${1/*host/}
  for sdev in /sys/class/scsi_device/${hostno}:* ; do
    if test -e $sdev/device/block* ; then
      dev=`ls $sdev/device/block*`
      dev="/dev/"$dev
      if test -n "$dev"; then
        blockdev --flushbufs $dev
      fi
    fi
  done
}


# Terminate a NPIV vhost
#   $1 is vhost
delete_vhost()
{
  # use upstream interface
  for vport in /sys/class/fc_vports/* ; do
    if test -e $vport/device/$1 ; then
      if test -e $vport/vport_delete ; then
        echo "1" > $vport/vport_delete
        if test $? -ne 0 ; then exit 6; fi
        sleep 4
        return
      fi
    fi
  done

  # use vendor specific interface

  # Emulex
  if test -e /sys/class/fc_host/$1/device/../scsi_host*/lpfc_drvr_version ; then
    shost=`ls -1d /sys/class/fc_host/$1/device/../scsi_host* | sed s/.*scsi_host://`
    vportwwpn=`cat /sys/class/fc_host/$1/port_name | sed s/^0x//`
    vportwwnn=`cat /sys/class/fc_host/$1/node_name | sed s/^0x//`
    echo "$vportwwpn:$vportwwnn" > /sys/class/scsi_host/$shost/vport_delete
    if test $? -ne 0 ; then exit 6; fi
    sleep 4
    return
  fi

  # Qlogic
  if test -e /sys/class/fc_host/$1/device/../scsi_host*/driver_version ; then
    shost=`ls -1d /sys/class/fc_host/$1/device/../scsi_host* | sed s/.*scsi_host://`
    vportwwpn=`cat /sys/class/fc_host/$1/port_name | sed s/^0x//`
    vportwwnn=`cat /sys/class/fc_host/$1/node_name | sed s/^0x//`
    echo "$vportwwpn:$vportwwnn" > /sys/class/scsi_host/$shost/vport_delete
    if test $? -ne 0 ; then exit 6; fi
    sleep 4
    return
  fi

  # BFA
  if test -e /sys/class/fc_host/$1/device/../scsi_host/*/driver_name ; then
    shost=`ls -1d /sys/class/fc_host/$1/device/../scsi_host/* | sed s#.*scsi_host/##`
    vportwwpn=`cat /sys/class/fc_host/$1/port_name | sed s/^0x//`
    vportwwnn=`cat /sys/class/fc_host/$1/node_name | sed s/^0x//`
    echo "$vportwwpn:$vportwwnn" > /sys/class/scsi_host/$shost/vport_delete
    if test $? -ne 0 ; then exit 6; fi
    sleep 4
    return
  fi


  exit 6
}


vport_status()
{
  # Look via upstream interfaces
  for fchost in /sys/class/fc_host/* ; do
    if test -e $fchost/vport_create ; then
      vport_status_display $fchost $fchost
    fi
  done

  # Look in vendor-specific locations

  # Emulex: interfaces mirror upstream, but are under adapter scsi_host
  for shost in /sys/class/scsi_host/* ; do
    if [ -e $shost/vport_create ] ; then
      fchost=`ls -d $shost/device/fc_host*`
      vport_status_display $fchost $shost
    fi
  done

  return 0
}


vport_status_display()
{
  echo
  echo "fc_host:            " $2
  echo "port_state:         " `cat $1/port_state`
  echo "port_type:          " `cat $1/port_type`
  echo "fabric_name:        " `cat $1/fabric_name`
  echo "max_npiv_vports:    " `cat $2/max_npiv_vports`
  echo "npiv_vports_inuse:  " `cat $2/npiv_vports_inuse`
  echo "modeldesc:          " `cat $2/modeldesc`
  echo "speed:              " `cat $1/speed`

  return 0
}

