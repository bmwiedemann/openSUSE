#!/bin/bash

# check_cups - nagios plugin
#
# Copyright (C) 2008-2010, Novell, Inc.
# Copyright (C) 2011-2013, SUSE Linux Products GmbH
# Author: Martin Caj <mcaj@suse.cz>
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
#
# Autor notes:    
#        I`d like to thank to John E. Vincent (nagios-plugs@lusis.org)
#        I learn a lof from his check CUPS print queue plugin.
#        Then I`d like to thank to Mark Shirley for his check_cups_printer.sh
#        script, which was also inspiration for me.
#        Both of them you can find on http://exchange.nagios.org/ web site.
#        Martin Caj 31/01/2013 <mcaj@suse.cz>
#
#        version 0.3 has no awk any more, cut can do it as well.
#        the appamor profile was fixed as well.
#         Martin Caj 01/11/2013 
#
# check_cups - nagios plugin for checking cups service
# Description:
#
# This plugin will check the status of a remote CUPS
# print service for the printer status, then if status is ok 
# it will check the queue. It can check all avaible printes
# on the cups, or just one of them.
# Then the plugin will check the queue:
# it will provide the size of the queue
# and optionally the age of the queue
#
# Version : 0.3

#searchning the lpstat:
LPSTAT="$(which lpstat)"
DEBUG='no'

# debug the script:
#set -x

# Nagios return codes
STATE_OK=0
STATE_WARNING=1
STATE_CRITICAL=2
STATE_UNKNOWN=3
STATE_DEPENDENT=4


# check it lpstat is missing.
if [ ! -x "$LPSTAT" ]
then
    echo "UNKNOWN: "$LPSTAT" not found or is not executable by the nagios user"
    exitstatus="$STATE_UNKNOWN"
    exit "$exitstatus"
fi

PROGNAME=$(basename $0)


print_usage() {
# Name: print_usage
# Desc: It just prints the usage. 

    echo "Usage: $PROGNAME -H <hostname> -w <size warning level> -c <size critical level> [-P] [-p<The CUPS printer name>] [-Q <s|b>] [-a <max age>] [-d]"
    echo 
    echo "Notes:"
    echo "-H <hostname>    : Hostname - Can be a hostname or IP address."
    echo "-P               : Check only the printers status."
    echo "-p <printername> : will check only the specified printer."
    echo "-Q <s|b>         : Type of check - Can be queue size (s) or both queue size and queue age (b)."
    echo "-w <int>         : WARNING level for queue size."
    echo "-c <int>         : CRITICAL level for queue size."
    echo "-a <int>         : Max age of queue. Returns CRITICAL if jobs exists longer than <max age> days."
	echo "-d               : enable debug output"
    echo 
}

print_help() {
# Name: print_help
# Desc: Print the usage and help.

    print_usage
    echo 
    echo "This plugin will check the CUPS print service for the printer status."
    echo "It can check the queue on a remote (or local with -H localhost) CUPS server."
    echo "It can check both: the size of the queue and the age of the oldest print job in the queue."
    echo "-w and -c are for warning and critical levels of the queue size."
    echo "-a is optional for specifying the max age of a job in the print queue. Anything older than <max age>"
    echo "will return a CRITICAL"
    echo "For more details have look into the README file. "
    echo 
    exit 0
}


check_queue_size() {
# Name: check_queue_size
# Desc: It check the status of the CUPS queue size.
# $exitstatus= might be ok|warn"crittical deppends on -w and -c 
                        
if [ "$JOBCOUNT" -ge "$critlevel" ]
then
    MESSAGE="CRITICAL: CUPS queue size - "$JOBCOUNT"| "$PERFDATA""
        exitstatus="$STATE_CRITICAL"
elif [ "$JOBCOUNT" -ge "$warnlevel" ]
then
    MESSAGE="WARNING: CUPS queue size - "$JOBCOUNT"| "$PERFDATA""
        exitstatus="$STATE_WARNING"
else
    MESSAGE="OK: CUPS queue size - "$JOBCOUNT"| "$PERFDATA""
        exitstatus="$STATE_OK"
fi 

}

check_printer_status() {
# Name:check_printer_status
# Desc: It check status of all printers or one specific printer 
# output is store in $OUTPUT and $exitstatus

if [ -z "$printername" ]
    then
    if [ "$DEBUG" == 'yes' ]; then
        echo "Checking all printers..."
    fi
    RESULT=$("$LPSTAT" -h "$hostname" -p )
    if [ $? != 0 ]
        then
            echo "ERROR:  Probably wrong host name: "$hostname", or CUPS is not running." 
            exit "$STATE_UNKNOWN"
        fi
else
    if [ "$DEBUG" == 'yes' ]; then
        echo "Checking only printer: $printername"
    fi
    RESULT=$("$LPSTAT" -h "$hostname" -p "$printername")
    if [ $? != 0 ] 
    then
        echo "ERROR: the printer $printername doesn't exist on CUPS server $hostname." 
        echo "please check command: '$LPSTAT -h $hostname -p' without printer name."
        exit "$STATE_UNKNOWN"
    fi
fi

case "$RESULT" in
    *Rejecting*)
        messages=$(echo "$RESULT"|grep -i rejecting )
        OUTPUT="CRITICAL - CUPS printer is rejecting jobs for: $messages."
        exitstatus="$STATE_CRITICAL"
    ;;
    *Unable*)
        messages=$(echo "$RESULT"|grep -i unable )
        OUTPUT="CRITICAL - CUPS Unable to connect: $messages."
        exitstatus="$STATE_CRITICAL"
    ;;
    *disabled*)
        messages=$(echo "$RESULT"|grep -i disabled)
        OUTPUT="CRITICAL - CUPS printer: $messages."
        exitstatus="$STATE_CRITICAL"
    ;;
    *Paused*)
        messages=$(echo "$RESULT"|grep -i paused)
        OUTPUT="WARNING: - CUPS printer is: $messages."
        exitstatus="$STATE_WARNING"
    ;;
    *printing*)
        OUTPUT="OK - CUPS printer is printing now."
        exitstatus="$STATE_OK"
    ;;
    *idle*)
        OUTPUT="OK - CUPS printer $printername is idle."
        exitstatus="$STATE_OK"
    ;;
    *)
        OUTPUT="CRITICAL - Unknown error occured while checking: $RESULT."
        exitstatus="$STATE_CRITICAL"
    ;;
esac

}

# Test how many variable we got on command line
# The minimum for test printers is 3

if [ $# -lt 3 ]; then
    print_usage
    exit "$STATE_UNKNOWN"
fi

# this set default exit status to:
exitstatus="$STATE_UNKNOWN"

# by default is test pritner disabled, you must allow it with -p $printer or -P all printers
testprinter="0"

# testing arguments:
while test -n "$1"; do
    case "$1" in
        --help)
            print_help
            exit "$STATE_OK"
            ;;
        -h)
            print_help
            exit "$STATE_OK"
            ;;
        -P)
            testprinter="1"
            ;;
        -p)
            testprinter="2"
            printername="$2"
            shift
            ;;
        -H)
            hostname="$2"
            shift
            ;;
        -Q)
            testtype="$2"
            shift
            ;;
        -w)
            warnlevel="$2"
            shift
            ;;
        -c)    
            critlevel="$2"
            shift
            ;;
        -a)    
            maxage="$2"
            shift
            ;;
        -d)
            DEBUG='yes'
            ;;
    esac
    shift
done

# Check arguments for validity:
if [ -z "$hostname" ]
then
    echo "You must specify a hostname (or localhost to test the local system)" >&2
    print_usage
    exitstatus="$STATE_UNKNOWN"
    exit "$exitstatus"
fi

# testing printer(s) 
if [ "$testprinter" -eq "2" ] # Check specific printer and continue with the script
then
    check_printer_status "$printername" 
    
    if [ -z "$testtype" ] # exit if there is no -Q checks
    then
        echo "$OUTPUT"
        exit "$exitstatus"
    fi
elif [ "$testprinter" -eq "1" ]; then # check all printers 
    check_printer_status
    if [ -z "$testtype" ]; then # exit if there is no -Q checks
        echo "$OUTPUT"
        exit "$exitstatus"
    fi
else # no cuos check is need
    if [ "$DEBUG" == 'yes' ]; then	
        echo "No printer check required. Checking the queue ..."
    fi
fi

# testing arguments for the queue checks:
if [[ -z "$critlevel" || -z "$warnlevel" ]] # Did we get warn and crit values?
then    
    echo "You must specify a warning and critical level"
    print_usage
    exitstatus="$STATE_UNKNOWN"
    exit "$exitstatus" 
elif [ $critlevel -lt $warnlevel ] # Do the warn/crit values make sense?
then
    echo "CRITICAL value of $critlevel is less than WARNING level of $warnlevel"
    print_usage
    exitstatus="$STATE_UNKNOWN"
    exit "$exitstatus"
fi

# what kind of queue test will be run:
if [ -z "$testtype" ]
then
    echo "You must specify a test type"
    print_usage
    exitstatus="$STATE_UNKNOWN"
    exit "$exitstatus"
# this is a very nice elif, it match if -a X is missing
elif [[ "$testtype" = [b]* && -z "$maxage" ]] 
then
    echo "You must specify <max age> when using a test type of 'b'"
    print_usage
    exitstatus="$STATE_UNKNOWN"
    exit "$exitstatus"
else
    if [ "$DEBUG" == 'yes' ]; then
        echo "Testing queue on $hostname ..."
    fi
    JOBTMP=$(mktemp -t lpstat.XXXXXX) # Create a tmpfile to store the lpstat results
    STALEJOBCOUNT=0 # default number of old jobs
    CURDATETS=$(date +%s) # Get the current date as unixtime
    "$LPSTAT" -h "$hostname" -o > "$JOBTMP" # run the lpstat command against the host.

    if [ $? -ne 0 ]
    then
        rm -rf "$JOBTMP"
        echo "UNKNOWN: lpstat command returned an error. Please test this script manually."
        exitstatus="$STATE_UNKNOWN"
        exit "$exitstatus"
    fi
    JOBCOUNT=$(wc -l < $JOBTMP) # populate the jobcount
    PERFDATA="print_jobs=${JOBCOUNT};${warnlevel};${critlevel};0"
    if [[ "$JOBCOUNT" -gt 0 && "$maxage" ]]
    then
        MAXAGETS=$(echo "86400 * $maxage" | bc) # 86400 seconds in a day * maxage
        exec<"$JOBTMP" # read the file to determine job age
        while read PRINTJOB
        do
            # Grab the job date from the job listing
            JOBDATE=$(echo "$PRINTJOB" | cut -c50-73) 
            # Convert the job date to unixtime
            JOBDATETS=$(date --date="$JOBDATE" +%s) 
            DATEDIFF=$(echo "($CURDATETS - $JOBDATETS)" | bc)
            if [ $DATEDIFF -gt $MAXAGETS ]
            then
                MESSAGE="CRITICAL: Some CUPS jobs are older than $maxage days| $PERFDATA"
                exitstatus="$STATE_CRITICAL"
            else
                check_queue_size
            fi
        done
    else
        check_queue_size
    fi
    rm -rf "$JOBTMP"
fi

# end: print the results and end with exit code for Nagios
echo "$OUTPUT"
echo "$MESSAGE"
exit "$exitstatus"
