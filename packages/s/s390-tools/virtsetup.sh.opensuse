#!/bin/sh
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# Perform setup tasks based on what hypervisor is in charge.
#

# Source the sysconfig file
if [ -r /etc/sysconfig/virtsetup ]; then
  . /etc/sysconfig/virtsetup
else echo "No /etc/sysconfig/virtsetup file was found."
     exit 1
fi

#
# Get our hostname
#
my_hostname="$(hostname)"

#
# Find out the hypervisor we're running on/under.
#
hypervisor="$(/usr/bin/systemd-detect-virt)"

case "${hypervisor}" in
	zvm)
		if [ ! -c /dev/vmcp ]; then
		  modprobe vmcp
		  sleep 1
		  if [ ! -c /dev/vmcp ]; then
		    echo "Unable to load the vmcp kernel module."
		    exit 1
		  fi
		fi
		echo "The vmcp device driver is ready."
		if [ "${ZVM_DETACH_DISKS}" == "yes" ]; then
		  echo "Detaching devices to prepare for Live Guest Relocation."
		  /usr/lib/systemd/scripts/detach_disks.sh
		fi
		if [ "${ZVM_WARN_ABOUT_POSSIBLE_LGR_PROBLEMS}" == yes ]; then
		  /usr/sbin/lgr_check
		fi
	;;
	none)
		hypervisor="lpar"
		if [ "${LPAR_SCLP_HOSTNAME}" == "yes" ]; then
		  # If the sclp_cpi module is already loaded, we have to unload it
		  # so we can be sure it has the correct system name specified
		  # when we reload it again.
		  if grep -qw sclp_cpi /proc/modules 2>/dev/null; then
			rmmod sclp_cpi
			sleep 1
		  fi
		  if grep -qw sclp_cpi /proc/modules 2>/dev/null; then
			echo "Unable to unload the sclp_cpi kernel module."
			exit 1
		  fi
		  echo "Setting the LPAR name via the sclp_cpi module."
		  modprobe sclp_cpi system_name="$my_hostname"
		  if ! grep -qw sclp_cpi /proc/modules 2>/dev/null; then
		   echo "We were unable to load the sclp_cpi module to set the LPAR name."
		   exit 2
		  fi 
		fi
	;;
	kvm)
	;;
	*)
		echo "An unknown hypervisor, \"${hypervisor}\" was detected."
		echo "Please report this to your support provider."
		exit 3
	;;
esac

#
# Now let's check for any scripts that other packages may have provided
# to do specific things they need. The scripts must be marked executable
# and have a suffix indicating which hypervisor for which they are to be run.
# Currently that is one of: kvm, lpar, or zvm.
# E.g., 01-test.script.zvm would only be run if the system is a z/VM guest.
#

for script in $(ls /lib/s390-tools/virtsetup/*.${hypervisor} 2>/dev/null)
  do if [ -x "${script}" ]; then
	echo "Executing ${script}..."
	"${script}"
	echo "Done."
	echo
     fi
  done

exit 0
