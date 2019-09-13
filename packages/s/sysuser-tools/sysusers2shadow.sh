#!/bin/bash

while read LINE
do
    case "$LINE" in
	\#*|"")
	    ;;
	g*)
            eval arr=( $LINE )
            ARGUMENTS="${arr[1]}"
            if [ ! -z "${arr[2]}" -a "${arr[2]}" != "-" ]; then
                ARGUMENTS="-g ${arr[2]} $ARGUMENTS"
	    fi
	    if [ -x /usr/sbin/groupadd ]; then
		echo "groupadd -r $ARGUMENTS"
		/usr/bin/getent group "${arr[1]}" >> /dev/null || /usr/sbin/groupadd -r $ARGUMENTS || exit $?
	    elif [ -x /usr/bin/busybox ]; then
		echo "addgroup -S $ARGUMENTS"
		/usr/bin/getent group "${arr[1]}" >> /dev/null || /usr/bin/busybox addgroup -S $ARGUMENTS || exit $?
	    else
		echo "ERROR: neither groupadd nor busybox found!"
		exit 1
	    fi
	    ;;
	u*)
            eval arr=( $LINE )
	    ARGUMENTS="${arr[1]}"
	    if [ ! -z "${arr[2]}" -a "${arr[2]}" != "-" ]; then
		ARGUMENTS="-u ${arr[2]} $ARGUMENTS"
	    fi
	    if [ ! -z "${arr[4]}" -a "${arr[4]}" != "-" ]; then
		ARGUMENTS="-d ${arr[4]} $ARGUMENTS"
	    else
		ARGUMENTS="-d / $ARGUMENTS"
	    fi
	    /usr/bin/getent group ${arr[1]} >> /dev/null
            if [ $? -eq 0 ]; then
              	ARGUMENTS="-g ${arr[1]} $ARGUMENTS"
	    else
		ARGUMENTS="-U $ARGUMENTS"
	    fi
	    if [ -x /usr/sbin/useradd ]; then
		echo "useradd -r -s /sbin/nologin -c \"${arr[3]}\" $ARGUMENTS"
		/usr/bin/getent passwd ${arr[1]} >> /dev/null || /usr/sbin/useradd -r -s /sbin/nologin -c "${arr[3]}" $ARGUMENTS || exit $?
	    elif [ -x /usr/bin/busybox ]; then
		ARGUMENTS=`echo $ARGUMENTS | sed -e 's|-d|-h|g' -e 's|-g|-G|g'`
		echo "adduser -S -s /sbin/nologin -g \"${arr[3]}\" $ARGUMENTS"
		/usr/bin/getent passwd ${arr[1]} >> /dev/null || /usr/bin/busybox adduser -S -s /sbin/nologin -g "${arr[3]}" $ARGUMENTS || exit $?
	    else
		echo "ERROR: neither useradd nor busybox found!"
		exit 1
	    fi
	    ;;
	m*)
            eval arr=( $LINE )
	    if [ -x /usr/sbin/usermod ] ; then
		echo "usermod -a -G ${arr[2]} ${arr[1]}"
		/usr/sbin/usermod -a -G ${arr[2]} ${arr[1]} || exit $?
	    elif [ -x /usr/bin/busybox ]; then
		echo "addgroup ${arr[1]} ${arr[2]}"
		/usr/bin/busybox addgroup ${arr[1]} ${arr[2]} || exit $?
	    else
		echo "ERROR: neither usermod nor busybox found!"
		exit 1
	    fi
	    ;;
	r*)
	    echo "range option ignored: \"$LINE\""
	    ;;
	*)
	    echo "Syntax Error: \"$LINE\""
	    exit 1
	    ;;
    esac
done
