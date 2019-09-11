#!/bin/bash
#
# Copyright (C) 2014 Robert Milasan <rmilasan@suse.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This script run manually by user, will generate a persistent rule for
# a given network interface to rename it to new interface name.
#

_prj="$(basename $0 2>/dev/null)"
prj="${_prj%.*}"
ver="0.2"

log_info()
{
  local msg="$1"
  echo "$prj: $msg"
}

log_error()
{
 local msg="$1"
 echo "$prj: $msg" >&2
}

usage()
{
  cat << EOF
$prj: udev persistent rule generator script

Usage: $prj [OPTION] ...

       -h              Show this help
       -l              List available interfaces
       -m              Generate the persistent rule based on interface MAC address
                       default option, if nothing is specified
       -p              Generate the persistent rule based on interface PCI slot
       -v              Be more verbose
       -V              Output the version number
       -c [INTERFACE]  Current interface name (ex: ip link)
                       only needed for retrieving information
       -n [INTERFACE]  New interface name (ex: net0)
       -o [FILE]       Where to write the new generate rule (default: /dev/stdout)
                       prefered location is /etc/udev/rules.d/70-persistent-net.rules

Example:
       $prj -v -c enp0s4 -n lan0
    or
       $prj -m -c enp0s4 -n net0 -o /etc/udev/rules.d/70-persistent-net.rules
    or
       $prj -p -c wlp3s0 -n wlan0 -o /etc/udev/rules.d/50-mynet.rules

EOF
}

display_note()
{
  cat << EOF

NOTE: Using the generate persistent rule might mean you will need to do extra work to ensure
that it will work accordingly. This mean, regenerating the initramfs/initrd image and/or using 
'net.ifnames=0' option at boot time.
In openSUSE/SUSE, the user will need to regenerate the initramfs/initrd image, but usually there
is no need for 'net.ifnames=0' option if the persistent rule is available in initramfs/initrd image.
EOF
}

get_pci()
{
  local path="$1"
  local pci=""

  if [ -L "$path/device" ]; then
     local pci_link="$(readlink -f $path/device 2>/dev/null)"
     pci="$(basename $pci_link 2>/dev/null)"
  fi
  echo $pci
}

get_pci_id()
{
  local path="$1"
  local pci_id=""

  if [ -r "$path/device/uevent" ]; then
     local _pci_id="$(cat $path/device/uevent|grep ^PCI_ID 2>/dev/null)"
     pci_id="${_pci_id#*=}"
  fi
  echo $pci_id
}

get_macaddr()
{
  local path="$1"
  local macaddr=""

  if [ -r "$path/address" ]; then
     macaddr="$(cat $path/address 2>/dev/null)"
  fi
  echo $macaddr
}

get_type()
{
  local path="$1"
  local dev_type=""
  
  if [ -r "$path/type" ]; then
     dev_type="$(cat $path/type 2>/dev/null)"
  fi
  echo $dev_type
}

get_dev_id()
{
  local path="$1"
  local dev_id=""

  if [ -r "$path/dev_id" ]; then
     dev_id="$(cat $path/dev_id 2>/dev/null)"
  fi
  echo $dev_id
}

get_devtype()
{
  local path="$1"
  local devtype=""
  if [ -r "$path/uevent" ]; then
     local _devtype="$(cat $path/uevent|grep ^DEVTYPE 2>/dev/null)"
     devtype="${_devtype#*=}"
  fi
  echo $devtype
}

get_subsystem()
{
  local path="$1"
  local subsystem=""

  if [ -L "$path/subsystem" ]; then
     local subsystem_link="$(readlink -f $path/subsystem 2>/dev/null)"
     subsystem="$(basename $subsystem_link 2>/dev/null)"
  fi
  echo $subsystem
}

get_parent_subsystem()
{
  local path="$1"
  local subsystem=""

  if [ -L "$path/device/subsystem" ]; then
     local subsystem_link="$(readlink -f $path/device/subsystem 2>/dev/null)"
     subsystem="$(basename $subsystem_link 2>/dev/null)"
  fi
  echo $subsystem
}

get_driver()
{
  local path="$1"
  local driver=""

  if [ -L "$path/device/driver" ]; then
     local driver_link="$(readlink -f $path/device/driver 2>/dev/null)"
     driver="$(basename $driver_link 2>/dev/null)"
  fi
  echo $driver
}

valid_mac()
{
  local macaddr="$1"
  local valid_macaddr=""

  if [ -n "$macaddr" ]; then
     valid_macaddr="$(echo $macaddr | sed -n '/^\([0-9a-z][0-9a-z]:\)\{5\}[0-9a-z][0-9a-z]$/p')"
  fi
  echo $valid_macaddr
}

valid_dev_type()
{
  local dev_type="$1"
  
  case "$dev_type" in
         [0-32])
         echo "$dev_type" ;;
         *)
         echo "invalid" ;;
  esac
}

generate_comment()
{
  local pci_id="$1"
  local driver="$2"
  local output="$3"
  local device_type="$4"
  local _type=""
  
  if [ -z "$pci_id" ]; then
     log_error "\$pci_id empty."
     exit 1
  elif [ -z "$driver" ]; then
     log_error "\$driver empty."
     exit 1
  elif [ -z "$output" ]; then
     log_error "\$output empty."
     exit 1
  else
     if [ "$device_type" == "pci" ]; then
        _type="PCI"
     elif [ "$device_type" == "usb" ]; then
        _type="USB"
     else
        _type="Unknown"
     fi
     echo "# $_type device $pci_id ($driver)" >> $output
  fi
}

generate_rule()
{
  local _subsystem="$1"
  local _mac="$2"
  local _pci="$3"
  local _dev_id="$4"
  local _dev_type="$5"
  local _kernel="$6"
  local _interface="$7"
  local output="$8"

  if [ -z "$_subsystem" ]; then
     log_error "\$_subsystem empty."
     exit 1
  elif [ -z "$_dev_id" ]; then
     log_error "\$_dev_id empty."
     exit 1
  elif [ -z "$_dev_type" ]; then
     log_error "\$_dev_type empty."
     exit 1
  elif [ -z "$_kernel" ]; then
     log_error "\$_kernel empty."
     exit 1
  elif [ -z "$_interface" ]; then
     log_error "\$_interface empty."
     exit 1
  elif [ -z "$output" ]; then
     output="/dev/stdout"
  fi

  if [ "$_mac" != "none" ]; then
     echo "SUBSYSTEM==\"$_subsystem\", ACTION==\"add\", DRIVERS==\"?*\", ATTR{address}==\"$_mac\", \
ATTR{dev_id}==\"$_dev_id\", ATTR{type}==\"$_dev_type\", KERNEL==\"$_kernel\", NAME=\"$_interface\"" >> ${output}
  elif [ "$_pci" != "none" ]; then
     echo "SUBSYSTEM==\"$_subsystem\", ACTION==\"add\", DRIVERS==\"?*\", KERNELS==\"$_pci\", \
ATTR{dev_id}==\"$_dev_id\", ATTR{type}==\"$_dev_type\", KERNEL==\"$_kernel\", NAME=\"$_interface\"" >> ${output}
  else
     log_error "MAC address or PCI slot information missing."
     exit 1
  fi
}

list_adapters()
{
  declare -a netdev
  local count=0
  local _netdev=""
  local _dev=""

  for _dev in $SYSPATH/*; do
      if [ -L "$_dev/device" ]; then
         local _dev_type="$(cat $_dev/type 2>/dev/null)"
         if [ "$(valid_dev_type $_dev_type)" == "invalid" ]; then
            continue;
         fi
         _dev="$(basename $_dev 2>/dev/null)"
         netdev[$count]="$_dev"
         count=$((count + 1))
      fi
  done

  echo "Found $count network interfaces:"
  for _netdev in "${netdev[@]}"; do
     _macaddr="$(get_macaddr $SYSPATH/$_netdev)"
     _pcislot="$(get_pci $SYSPATH/$_netdev)"
     echo "I: INTERFACE: $_netdev"
     echo "I: MACADDR: $_macaddr"
     echo "I: PCI: $_pcislot"
  done
}

if [ $# -eq 0 ]; then
   usage
   log_error "missing option(s)."
   exit 1
fi

SYSPATH="/sys/class/net"

use_mac=0
use_pci=0
use_verbose=0

while getopts "hlmpvVc:n:o:" opt; do
  case "$opt" in
     h)
       usage; exit 0;;
     l)
       list_adapters; exit 0;;
     m)
       use_mac=1 ;;
     p)
       use_pci=1 ;;
     v)
       use_verbose=1 ;;
     V)
       echo "$prj $ver"; exit 0;;
     c)
       ifcur="$OPTARG" ;;
     n)
       ifnew="$OPTARG" ;;
     o)
       output="$OPTARG" ;;
     \?)
       exit 1 ;;
  esac
done

if [[ "$use_mac" -eq 0 ]] && [[ "$use_pci" -eq 0 ]]; then
   use_mac=1
fi

if [[ "$use_mac" -eq 1 ]] && [[ "$use_pci" -eq 1 ]]; then
   log_error "generating a persistent rule can be done only using one of the option, -m or -p, not both."
   exit 1
fi

outfile="$output"
if [ -z "$output" ]; then
   outfile="/dev/stdout"
else
   dir="$(dirname $outfile 2>/dev/null)"
   tmpfile="$dir/.tmp_file"
   if [ -d "$dir" ]; then
      touch "$tmpfile" >/dev/null 2>&1
      if [ $? -ne 0 ]; then
         log_error "no write access for $outfile. make sure you have write permissions to $dir."
         exit 1
      fi
      rm -f "$tmpfile" >/dev/null 2>&1
   else
      log_error "$dir not a directory."
      exit 1
  fi
fi

interface="$ifcur"
if [ -z "$interface" ]; then
   log_error "current interface must be specified."
   exit 1
elif [ "$interface" == "lo" ]; then
   log_error "loopback interface is not a valid interface."
   exit 1
fi
[ "$use_verbose" -eq 1 ] && echo "I: INTERFACE=$interface"

new_interface="$ifnew"
if [ -z "$new_interface" ]; then
   log_error "new interface must be specified."
   exit 1
elif [ "$new_interface" == "lo" ]; then
   log_error "new interface cant be named loopback interface."
   exit 
fi
[ "$use_verbose" -eq 1 ] && echo "I: INTERFACE_NEW=$new_interface"

path="$SYSPATH/$interface"
if [ ! -d "$path" ]; then
   log_error "devpath $path not a directory."
   exit 1
fi
[ "$use_verbose" -eq 1 ] && echo "I: DEVPATH=$path"

devtype="$(get_devtype $path)"
if [ -n "$devtype" ]; then
   [ "$use_verbose" -eq 1 ] && echo "I: DEVTYPE=$devtype"
fi

parent_subsystem="$(get_parent_subsystem $path)"
if [ -z "$parent_subsystem" ]; then
   log_error "unable to retrieve parent subsystem for interface $interface."
   exit 1
fi
[ "$use_verbose" -eq 1 ] && echo "I: PARENT_SUBSYSTEM=$parent_subsystem"

subsystem="$(get_subsystem $path)"
if [ -z "$subsystem" ]; then
   log_error "unable to retrieve subsystem for interface $interface."
   exit 1
fi
[ "$use_verbose" -eq 1 ] && echo "I: SUBSYSTEM=$subsystem"

pci_id="$(get_pci_id $path)"
if [ -z "$pci_id" ]; then
   pci_id="0x:0x"
fi
[ "$use_verbose" -eq 1 ] && echo "I: PCI_ID=$pci_id"

driver="$(get_driver $path)"
if [ -z "$driver" ]; then
   log_error "unable to retrieve driver for interface $interface."
   exit 1
fi
[ "$use_verbose" -eq 1 ] && echo "I: DRIVER=$driver"

if [ "$use_mac" -eq 1 ]; then
   macaddr="$(get_macaddr $path)"
   if [ -z "$macaddr" ]; then
      log_error "unable to retrieve MAC address for interface $interface."
      exit 1
   fi
   if [ "$(valid_mac $macaddr)" != "$macaddr" ]; then
      log_error "$macaddr invalid MAC address."
      exit 1
  fi
  [ "$use_verbose" -eq 1 ] && echo "I: MACADDR=$macaddr"
fi

if [ "$use_pci" -eq 1 ]; then
   pci="$(get_pci $path)"
   if [ -z "$pci" ]; then
      log_error "unable to retrieve PCI slot for interface $interface."
      exit 1
   fi
   [ "$use_verbose" -eq 1 ] && echo "I: KERNELS=$pci"
fi

dev_id="$(get_dev_id $path)"
if [ -z "$dev_id" ]; then
   log_error "unable to retrieve dev_id for interface $interface."
   exit 1
fi
[ "$use_verbose" -eq 1 ] && echo "I: DEV_ID=$dev_id"

dev_type="$(get_type $path)"
if [ -z "$dev_type" ]; then
   log_error "unable to retrieve dev_type for interface $interface."
   exit 1
elif [ "$(valid_dev_type $dev_type)" == "invalid" ]; then
   log_info "$interface not a supported device."
   exit 1
fi
[ "$use_verbose" -eq 1 ] && echo "I: TYPE=$dev_type"

kernel="eth*"
if [ -n "$devtype" ]; then
   if [ "$devtype" == "wlan" ]; then
      kernel="wlan*"
   fi
fi

if [ -n "$output" ]; then
   echo "Persistent rule written to "$outfile""
   generate_comment "$pci_id" "$driver" "$outfile" "$parent_subsystem"
fi

if [ "$use_mac" -eq 1 ]; then
   generate_rule "$subsystem" "$macaddr" "none" "$dev_id" "$dev_type" "$kernel" "$new_interface"
   if [ -n "$output" ]; then
      generate_rule "$subsystem" "$macaddr" "none" "$dev_id" "$dev_type" "$kernel" "$new_interface" "$outfile"
   fi
elif [ "$use_pci" -eq 1 ]; then
   generate_rule "$subsystem" "none" "$pci" "$dev_id" "$dev_type" "$kernel" "$new_interface"
   if [ -n "$output" ]; then
      generate_rule "$subsystem" "none" "$pci" "$dev_id" "$dev_type" "$kernel" "$new_interface" "$outfile"
   fi
fi

if [ -n "$output" ]; then
   display_note
fi

exit 0
