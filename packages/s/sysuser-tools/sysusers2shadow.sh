#!/bin/sh
set -eu

# Print the command and run it
run() {
	echo "$@"
	"$@"
}

# Absolute path to busybox, if found
busybox=
for i in /bin/busybox /usr/bin/busybox; do [ -x "$i" ] && busybox=$i; done

while read LINE
do
	# "eval set" to do proper splitting while respecting quotes
	eval set -- $LINE
	case "${1-}" in
	\#*|"")
		;;
	g)
		shift
		ARGUMENTS="$1"
		if [ -n "${2-}" ] && [ "$2" != "-" ]; then
			ARGUMENTS="-g $2 $ARGUMENTS"
		fi

		if ! /usr/bin/getent group "$1" >> /dev/null; then
			if [ -x "/usr/sbin/groupadd" ]; then
				run /usr/sbin/groupadd -r $ARGUMENTS
			elif [ -x "$busybox" ]; then
				run $busybox addgroup -S $ARGUMENTS
			else
				echo "ERROR: neither groupadd nor busybox found!"
				exit 1
			fi
		fi
		;;
	u)
		shift
		ARGUMENTS="$1"
		if [ -n "${2-}" ] && [ "$2" != "-" ]; then
			ARGUMENTS="-u $2 $ARGUMENTS"
		fi
		homedir="/" # If null, empty or '-'
		if [ "${4:--}" != "-" ]; then
			homedir="$4"
		fi

		if [ -x /usr/sbin/useradd ]; then
			if ! /usr/bin/getent passwd "$1" >> /dev/null; then
				# this is useradd/shadow specific
				if /usr/bin/getent group "$1" >> /dev/null; then
					ARGUMENTS="-g $1 $ARGUMENTS"
				else
					ARGUMENTS="-U $ARGUMENTS"
				fi
			
				run /usr/sbin/useradd -r -s /sbin/nologin -c "$3" -d "${homedir}" $ARGUMENTS
			fi
		elif [ -x "$busybox" ]; then
			/usr/bin/getent group "$1" >> /dev/null || $busybox addgroup -S "$1"

			if ! /usr/bin/getent passwd "$1" >> /dev/null; then
				run $busybox adduser -S -H -s /sbin/nologin -g "$3" -G "$1" -h "${homedir}" $ARGUMENTS
			fi
		else
			echo "ERROR: neither useradd nor busybox found!"
			exit 1
		fi
	    ;;
	m)
		shift
		if [ -x /usr/sbin/usermod ] ; then
				run /usr/sbin/usermod -a -G $2 $1
		elif [ -x "$busybox" ]; then
				run $busybox addgroup $1 $2
		else
				echo "ERROR: neither usermod nor busybox found!"
				exit 1
		fi
	    ;;
	r)
		echo "range option ignored: \"$LINE\""
		;;
	*)
	    echo "Syntax Error: \"$LINE\""
	    exit 1
	    ;;
	esac
done
