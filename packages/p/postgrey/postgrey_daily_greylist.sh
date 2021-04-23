#!/bin/bash
#
# (c) Copyright Klaus Singvogel, 2008
# All rights reserved.
#
# This script searches for relevant entries in mail log, generates
# a daily report from this data, and sends them in a (human) readable
# to specified user
#
# suggested to use with cron, before the logfiles got rotated by
# logrotate mechanism (otherwise bzcat/zcat has to be used)
# reference to variable DAILY_TIME in /etc/sysconfig/cron when the
# logfiles got rotate (exceptions to this rule possible)

# variables to modify to personal settings
reciepient=postmaster
logfile=/var/log/mail

report_flags="--check_sender=mx,a"
# report_flags='--separate_by_subnet=":==================\n" --nosingle_line --check_sender=mx,a'

# better, not to modify these variables
TEMPFILE=$(mktemp "/tmp/greylist.XXXXXX") || exit 1
# for compressed logfiles...
today=`date +"%Y%m%d"`
yesterday=`date -d yesterday +"%Y%m%d"`
##
## Attention! This script has changed to work with
##            rsyslog on an openSUSE >= 12.3 called
##            MINIMAL SERVER SELECTION
##
# Set date format to search value as your need's
# RSYSLOG:
# a RFC5424 logline start with yyyy-mm-dd
# (e.g. 2015-08-15 ) comment out the next line
# searchValue=`date -d yesterday +"%F"`
# SYSLOG-NG:
# a RFC3164 logline start with locale's abbreviated month
# (e.g. Jan  1 ) comment out the next line
searchValue=`date -d yesterday +"%b %2e"`

if [ ! -r "$logfile" ]; then
	echo "no logfile $logfile" | \
		mail -s "greylist: no greylisted host" $reciepient
	rm $TEMPFILE
	exit 1
fi

if [ -z "$logfile" ]; then
	echo "empty logfile $logfile" | \
		mail -s "greylist: no greylisted host" $reciepient
	rm $TEMPFILE
	exit 1
fi

if [ -r "$logfile"-"$today".xz ]; then
	( cat "$logfile"; xzcat "$logfile"-"$today".xz; ) |\
		grep "postgrey\|[gG]reylist" | \
                grep "$searchValue" > $TEMPFILE
elif [ -r "$logfile"-"$yesterday".xz ]; then
	( cat "$logfile"; xzcat "$logfile"-"$yesterday".xz; ) |\
		grep "postgrey\|[gG]reylist" | \
                grep "$searchValue" > $TEMPFILE
else
	cat "$logfile" | \
		grep "postgrey\|[gG]reylist" | \
                grep "$searchValue" > $TEMPFILE
fi

if [ `wc -l < $TEMPFILE` -gt 1 ]; then
	/usr/sbin/postgreyreport "$report_flags" < $TEMPFILE | \
		mail -s "greylist: yesterdays greylisted host" $reciepient
else
	( echo "no entries >$date< found in logfile $logfile" ;
          date;
	  echo "";
          ls -ls $logfile;
	  echo "";
	  ls -ls $TEMPFILE;
	  echo "";
	) | \
		mail -s "greylist: no greylisted hosts" $reciepient
fi

rm $TEMPFILE
