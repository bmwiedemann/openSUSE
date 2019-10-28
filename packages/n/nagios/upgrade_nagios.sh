#!/bin/bash
#
# Copyright (C) 2013, SUSE Linux Products GmbH
# Author: Lars Vogdt
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the Novell nor the names of its contributors may be
#   used to endorse or promote products derived from this software without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
#set -x
VERSION=1
NAGIOS_CFG='/etc/nagios/nagios.cfg'
LOCK_FILE='/var/run/nagios/nagios.pid'
DATE=$(date "+%Y-%m-%d-%H:%M")
TMPFILE=$(mktemp /tmp/$(basename $0)-XXXXXX)
LOGFILE='/var/log/nagios/nagios_upgrade.log'
VERBOSE='no'
DO_ECHO=''

ALL_OBSOLETE_VARS="
aggregate_status_updates 
check_result_reaper_frequency 
command_check_interval
comment_file 
downtime_file 
enable_embedded_perl 
external_command_buffer_slots 
max_check_result_reaper_time 
p1_file
service_reaper_frequency 
sleep_time
use_embedded_perl_implicitly 
"

REMOVED_VARS="
aggregate_status_updates 
check_result_reaper_frequency 
command_check_interval
enable_embedded_perl 
external_command_buffer_slots 
max_check_result_reaper_time 
p1_file
service_reaper_frequency 
sleep_time
use_embedded_perl_implicitly 
"

CP=$(which cp)
CAT=$(which cat)
SED=$(which sed)
ECHO=$(which echo)
LOGGER=$(which logger)
GREP=$(which grep)

cleanup_and_exit(){
	local EXITCODE="$1"
	test -f "$TMPFILE" && rm "$TMPFILE"
	exit $EXITCODE
}

usage(){
	echo "Usage: $(basename $0) [OPTIONS] [path_to_nagios.cfg]"
	echo 
	echo "       -h : show this help text"
	echo "       -d : just print out the commands"
	echo "       -l : full path to log file (default: $LOGFILE)"
	echo "       -p : full path to Nagios lock file (default: $LOCK_FILE)"
	echo "       -V : print version (current: $VERSION)"
	echo
}

check_and_disable_option(){
	local OPTION="$1"
	if $GREP -q ^$OPTION "$NAGIOS_CFG" ; then
		$ECHO "- $OPTION option has been uncommented in $NAGIOS_CFG" >> "$TMPFILE"
		$DO_ECHO $SED -i "s@^$OPTION@# $OPTION@" "$NAGIOS_CFG"
	fi
}

#######################################################################
###                             MAIN                                ###
#######################################################################
trap 'echo' SIGHUP SIGINT SIGQUIT
trap 'cleanup_and_exit 1' SIGTRAP SIGBUS SIGKILL SIGPIPE SIGTERM
trap 'cleanup_and_exit 0' EXIT

if [ ! $1 ]; then
    usage
    cleanup_and_exit '1'
fi

while getopts 'hda:vl:V'  OPTION ; do
    case $OPTION in
        h) 	usage
			cleanup_and_exit '0'
        ;;
		d) DO_ECHO="$ECHO"
		;;
		p) LOCK_FILE="$OPTARG"
		;;
		v) VERBOSE='yes'
		;;
		l) LOGFILE="$OPTARG"
		;;
		V) 	echo "$(basename $0) version $VERSION"
			cleanup_and_exit '0'
		;;
	esac
done
shift $(( OPTIND - 1 ))
NAGIOS_CFG="$1"

VAR_EXISTS='no'
for option in $ALL_OBSOLETE_VARS ; do
	grep -q ^$option "$NAGIOS_CFG" && { 
		VAR_EXISTS='yes';
		if [ "$VERBOSE" == "yes" ]; then
			$ECHO "Found obsolete configuration variable $option";
		fi; }
done

if [ "$VAR_EXISTS" == "no" ]; then
    if [ "$VERBOSE" == "yes" ]; then
        $ECHO "No enabled obsolete configuration variables found in $NAGIOS_CFG"
    fi
    cleanup_and_exit '0'
fi

$DO_ECHO echo -n "$(basename $0) called at: " >> "$LOGFILE"
$DO_ECHO date >> "$LOGFILE"

if [ ! -w "$NAGIOS_CFG" ]; then
	$ECHO "Could not open/write $NAGIOS_CFG - aborting" >&2
	$ECHO "Could not open/write $NAGIOS_CFG - aborting" >> "$LOGFILE"
	usage
	cleanup_and_exit '1'
fi

$DO_ECHO $CP -f "$NAGIOS_CFG" "${NAGIOS_CFG}_${DATE}" || {
	$ECHO "Could not create backup file ${NAGIOS_CFG}_${DATE} - aborting" >&2 ; 
	$ECHO "Could not create backup file ${NAGIOS_CFG}_${DATE} - aborting" >> "$LOGFILE" ;
	cleanup_and_exit '1';
}

if ! $GREP -q ^lock_file=$LOCK_FILE "$NAGIOS_CFG" ; then
	$ECHO "- updating pid lock_file= to $LOCK_FILE in $NAGIOS_CFG" >> $TMPFILE
	$DO_ECHO $SED -i "s@^lock_file=.*@lock_file=$LOCK_FILE @" "$NAGIOS_CFG"
fi
if grep -q ^downtime_file "$NAGIOS_CFG" ; then
	set -- $($GREP ^downtime_file "$NAGIOS_CFG" | $SED 's@=@ @')
	shift
	file=$($ECHO $*)
	if [ -n "$file" ]; then
		if [ -f "$file" ]; then
			set -- $($GREP ^state_retention_file "$NAGIOS_CFG" | $SED 's@=@ @')
			shift
			state_retention_file=$($ECHO $*)
			$ECHO "- adding the content of of $file to $state_retention_file" >> $TMPFILE
			$DO_ECHO $CAT "$file" >> "$state_retention_file"
		fi
	fi
	$ECHO "- removing downtime_file variable (no longer supported) in $NAGIOS_CFG" >> $TMPFILE
	$DO_ECHO $SED -i "s@^downtime_file@# downtime_file@" "$NAGIOS_CFG"
fi
if $GREP -q ^comment_file "$NAGIOS_CFG" ; then
	set -- $($GREP ^comment_file "$NAGIOS_CFG" | $SED 's@=@ @')
	shift
	file=$($ECHO $*)
	if [ -n "$file" ]; then
		if [ -f "$file" ]; then
			$ECHO "- adding the content of $file to $state_retention_file" >> $TMPFILE
			$DO_ECHO $CAT "$file" >> "$state_retention_file"
		fi
	fi
	$ECHO "- removing comment_file variable (no longer supported) in $NAGIOS_CFG" >> $TMPFILE
	$DO_ECHO $SED -i "s@^comment_file@# comment_file@" "$NAGIOS_CFG"
fi
for option_var in $REMOVED_VARS ; do
	check_and_disable_option "$option_var"
done
if [ -s "$TMPFILE" ]; then
	if [ "$VERBOSE" == "yes" ]; then
		$CAT "$TMPFILE"
	fi
	$DO_ECHO $CAT "$TMPFILE" >> "$LOGFILE"
	$DO_ECHO $LOGGER -t nagios/rpm -f "$TMPFILE"
else
	$DO_ECHO $ECHO "nothing to do" >> "$LOGFILE"
fi
cleanup_and_exit '0'
