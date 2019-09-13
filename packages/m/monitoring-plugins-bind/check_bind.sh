#!/bin/sh

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

PROGNAME=`basename $0`
VERSION="Version 1.3,"
AUTHOR="2009, Mike Adolphs (http://www.matejunkie.com/)"

ST_OK=0
ST_WR=1
ST_CR=2
ST_UK=3
path_pid="/var/run/named"
name_pid="named.pid"
path_rndc="/usr/sbin"
path_stats="/var/bind"
path_tmp="/tmp"
version=9.4
pid_check=1

print_version() {
    echo "$VERSION $AUTHOR"
}

print_help() {
    print_version $PROGNAME $VERSION
    echo ""
    echo "$PROGNAME is a Nagios plugin to check the bind daemon whether it's"
    echo "running via its pid file and then gets the statistics via rndc stats."
    echo "The user that run the script needs the ability to 'sudo rndc stats'!"
    echo "The timeframe in which the rndc stats output is updated is controlled"
    echo "by the check interval. The output shows amount of requests of various"
    echo "types occured during the last check interval."
    echo "The script itself is written sh-compliant and free software under the"
    echo "terms of the GPLv2 (or later)."
    echo ""
    echo "$PROGNAME -p/--path_pid /var/run/named -n/--name_pid named.pid"
    echo "  -r/--path-rndc /usr/sbin -s/--path-stats /var/bind"
    echo "  -V/--bind-version 9.3/9.4/9.5 -N"
    echo ""
    echo "Options:"
    echo "  -p/--path-pid)"
    echo "     Path where the pid file for bind is stored. You might need to"
    echo "     alter this to your distribution's way of dealing with pid files."
    echo "     Default is: /var/run/named"
    echo "  -n/--name_pid)"
    echo "     Name of the pid file. Default is: named.pid"
    echo "  -r/--path-rndc)"
    echo "     Path where the rndc binary is located. Default is: /usr/sbin"
    echo "  -s/--path-stats)"
    echo "     Path where the named.stats file is stored. Default is:"
    echo "     /var/bind"
    echo "  -t/--path-tmp)"
    echo "     Path where the temporary named.stats excerpt is being stored."
    echo "     Default is: /tmp"
    echo "  -V/--bind-version)"
    echo "     Specifies the bind version you're running. Currently there's"
    echo "     BIND 9.3, 9.4 and 9.5 supported. Default is: 9.4"
    echo "  -N/--no-pid-check)"
    echo "     If you don't want that the script checks for the pid file,"
    echo "     use this option. Default is: off"
    echo "  -C/--chroot)"
    echo "     If you're running BIND in a chroot environment, use this"
    echo "     option to define a path to be chrooted. Please adjust also"
    echo "     your sudo configuration to enable the Nagios user to chroot!"
    echo "     Default is: /opt/chroot-bind"
    exit $ST_UK
}

while test -n "$1"; do
    case "$1" in
        -help|-h)
            print_help
            exit $ST_UK
            ;;
        --version|-v)
            print_version $PROGNAME $VERSION
            exit $ST_UK
            ;;
        --path-pid|-p)
            path_pid=$2
            shift
            ;;
	--name-pid|-n)
	    name_pid=$2
	    shift
	    ;;
	--path-rndc|-r)
	    path_rndc=$2
	    shift
	    ;;
	--path-stats|-s)
	    path_stats=$2
	    shift
	    ;;
        --path-tmp|-t)
            path_tmp=$2
            shift
            ;;
	--bind-version|-V)
	    version=$2
	    shift
	    ;;
        --no-check-pid|-N)
            pid_check=0
	    ;;
        --chroot|-C)
            path_chroot=$2
	    shift
	    ;;
        *)
            echo "Unknown argument: $1"
            print_help
            exit $ST_UK
            ;;
    esac
    shift
done

check_pid() {
    if [ -f "$path_pid/$name_pid" ]
    then
        retval=0
    else
        retval=1
    fi
}

trigger_stats() {
    if [ -n "$path_chroot" ]
    then
        sudo chroot $path_chroot $path_rndc/rndc stats
    else
    sudo $path_rndc/rndc stats
    fi
}

copy_to_tmp() {
    tac $path_stats/named.stats | awk '/--- \([0-9]*\)/{p=1} p{print} /\+\+\+ \([0-9]*\)/{p=0;if (count++==1) exit}' > $path_tmp/named.stats.tmp
}

get_vals() {
    case ${version} in
        9.3)
            succ_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^success [0-9]*' | sort -n | awk '{print $2}'` 
            succ_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^success [0-9]*' | sort -n | grep -m1 '^success [0-9]*' | awk '{print $2}'`
            ref_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^referral [0-9]*' | sort -n | awk '{print $2}'`
            ref_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^referral [0-9]*' | sort -n | grep -m1 '^referral [0-9]*' | awk '{print $2}'`
            nxrr_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^nxrrset [0-9]*' | sort -n | awk '{print $2}'`
            nxrr_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^nxrrset [0-9]*' | sort -n | grep -m1 '^nxrrset [0-9]*' | awk '{print $2}'`
            nxdom_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^nxdomain [0-9]*' | sort -n | awk '{print $2}'`
            nxdom_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^nxdomain [0-9]*' | sort -n | grep -m1 '^nxdomain [0-9]*' | awk '{print $2}'`
            rec_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^recursion [0-9]*' | sort -n | awk '{print $2}'`
            rec_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^recursion [0-9]*' | sort -n | grep -m1 '^recursion [0-9]*' | awk '{print $2}'`
            fail_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^failure [0-9]*' | sort -n | awk '{print $2}'`
            fail_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^failure [0-9]*' | sort -n | grep -m1 '^failure [0-9]*' | awk '{print $2}'`
            ;;
        9.4)
            succ_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^success [0-9]*' | sort -n | awk '{print $2}'` 
            succ_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^success [0-9]*' | sort -n | grep -m1 '^success [0-9]*' | awk '{print $2}'`
            ref_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^referral [0-9]*' | sort -n | awk '{print $2}'`
            ref_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^referral [0-9]*' | sort -n | grep -m1 '^referral [0-9]*' | awk '{print $2}'`
            nxrr_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^nxrrset [0-9]*' | sort -n | awk '{print $2}'`
            nxrr_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^nxrrset [0-9]*' | sort -n | grep -m1 '^nxrrset [0-9]*' | awk '{print $2}'`
            nxdom_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^nxdomain [0-9]*' | sort -n | awk '{print $2}'`
            nxdom_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^nxdomain [0-9]*' | sort -n | grep -m1 '^nxdomain [0-9]*' | awk '{print $2}'`
            rec_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^recursion [0-9]*' | sort -n | awk '{print $2}'`
            rec_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^recursion [0-9]*' | sort -n | grep -m1 '^recursion [0-9]*' | awk '{print $2}'`
            fail_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^failure [0-9]*' | sort -n | awk '{print $2}'`
            fail_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^failure [0-9]*' | sort -n | grep -m1 '^failure [0-9]*' | awk '{print $2}'`
            dup_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^duplicate [0-9]*' | sort -n | awk '{print $2}'`
            dup_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^duplicate [0-9]*' | sort -n | grep -m1 '^duplicate [0-9]*' | awk '{print $2}'`
            drop_1st=`cat $path_tmp/named.stats.tmp | grep -m1 '^dropped [0-9]*' | sort -n | awk '{print $2}'`
            drop_2nd=`cat $path_tmp/named.stats.tmp | grep -o '^dropped [0-9]*' | sort -n | grep -m1 '^dropped [0-9]*' | awk '{print $2}'`
            ;;
        9.5)
            succ_1st=`grep 'resulted in successful answer' $path_tmp/named.stats.tmp | awk '{ print $1 }' | grep -m1 ''`
            succ_2nd=`grep 'resulted in successful answer' $path_tmp/named.stats.tmp | awk '{ print $1 }' | sort -n | grep -m1 ''`
            ref_1st=`grep 'resulted in referral' $path_tmp/named.stats.tmp | awk '{ print $1 }' | grep -m1 ''`
            ref_2nd=`grep 'resulted in referral' $path_tmp/named.stats.tmp | awk '{ print $1 }' | sort -n | grep -m1 ''`
            nxrr_1st=`grep 'resulted in nxrrset' $path_tmp/named.stats.tmp | awk '{ print $1 }' | grep -m1 ''`
            nxrr_2nd=`grep 'resulted in nxrrset' $path_tmp/named.stats.tmp | awk '{ print $1 }' | sort -n | grep -m1 ''`
            nxdom_1st=`grep 'resulted in NXDOMAIN' $path_tmp/named.stats.tmp | awk '{ print $1 }' | grep -m1 ''`
            nxdom_2nd=`grep 'resulted in NXDOMAIN' $path_tmp/named.stats.tmp | awk '{ print $1 }' | sort -n | grep -m1 ''`
            rec_1st=`grep 'caused recursion' $path_tmp/named.stats.tmp | awk '{ print $1 }' | grep -m1 ''`
            rec_2nd=`grep 'caused recursion' $path_tmp/named.stats.tmp | awk '{ print $1 }' | sort -n | grep -m1 ''`
            fail_1st=`grep 'resulted in SERVFAIL' $path_tmp/named.stats.tmp | awk '{ print $1 }' | grep -m1 ''`
            fail_2nd=`grep 'resulted in SERVFAIL' $path_tmp/named.stats.tmp | awk '{ print $1 }' | sort -n | grep -m1 ''`
            dup_1st=`grep 'duplicate queries received' $path_tmp/named.stats.tmp | awk '{ print $1 }' | grep -m1 ''`
            dup_2nd=`grep 'duplicate queries received' $path_tmp/named.stats.tmp | awk '{ print $1 }' | sort -n | grep -m1 ''`
            ;;
    esac

    if [ "$succ_1st" == '' ]
    then
        success=0
    else
        success=`expr $succ_1st - $succ_2nd`
    fi
    if [ "$ref_1st" == '' ]
    then
        referral=0
    else
        referral=`expr $ref_1st - $ref_2nd`
    fi
    if [ "$nxrr_1st" == '' ]
    then
        nxrrset=0
    else
        nxrrset=`expr $nxrr_1st - $nxrr_2nd`
    fi
    if [ "$nxdom_1st" == '' ]
    then
        nxdomain=0
    else
        nxdomain=`expr $nxdom_1st - $nxdom_2nd`
    fi
    if [ "$rec_1st" == '' ]
    then
        recursion=0
    else
        recursion=`expr $rec_1st - $rec_2nd`
    fi
    if [ "$fail_1st" == '' ]
    then
        failure=0
    else
        failure=`expr $fail_1st - $fail_2nd`
    fi
    if [ "$dup_1st" == '' ]
    then
        duplicate=0
    else
        duplicate=`expr $dup_1st - $dup_2nd`
    fi
    if [ "$drop_1st" == '' ]
    then
        dropped=0
    else
        dropped=`expr $drop_1st - $drop_2nd`
    fi
}
	
get_perfdata() {
    case ${version} in
        9.3)
            perfdata=`echo "'success'=$success 'referral'=$referral 'nxrrset'=$nxrrset 'nxdomain'=$nxdomain 'recursion'=$recursion 'failure'=$failure"`
            ;;
	*)
            perfdata=`echo "'success'=$success 'referral'=$referral 'nxrrset'=$nxrrset 'nxdomain'=$nxdomain 'recursion'=$recursion 'failure'=$failure 'duplicate'=$duplicate 'dropped'=$dropped"`
            ;;
    esac
}

if [ ${pid_check} == 1 ]
then
    check_pid
    if [ "$retval" = 1 ]
    then
        echo "There's no pid file for bind9. Is it actually running?"
        exit $ST_CR
    fi
fi

trigger_stats
copy_to_tmp
get_vals
get_perfdata

echo "Bind9 is running. $success successfull requests, $referral referrals, $nxdomain nxdomains since last check. | $perfdata"
exit $ST_OK
