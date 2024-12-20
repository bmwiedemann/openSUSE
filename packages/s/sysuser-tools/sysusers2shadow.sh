#!/bin/sh
set -e

# Print the command and run it
run() {
	echo "$@"
	"$@"
}

if [ -x /usr/bin/systemd-sysusers ] && [ -e /proc/version ]; then

	if [ -n "$1" ] && [ "$1" != "%3" ]; then
		REPLACE_ARG="--replace=/usr/lib/sysusers.d/$1"
	fi
	# Use systemd-sysusers and let it read the input directly from stdin
	if ! run /usr/bin/systemd-sysusers $REPLACE_ARG - ; then
		run /usr/bin/systemd-sysusers -
	fi
else
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

			if /usr/bin/getent passwd "$1" >> /dev/null; then
			    continue
			fi

			# Split user and Group id. Must work with busybox sh.
			case $2 in
				(*:*) USER_ID=${2%:*} GROUP_ID=${2##*:};;
				(*)   USER_ID=$2      GROUP_ID="";;
			esac

			if [ -n "$USER_ID" ] && [ "$USER_ID" != "-" ]; then
				ARGUMENTS="-u $USER_ID $ARGUMENTS"
			fi

			homedir="/" # If null, empty or '-'
			if [ "${4:--}" != "-" ]; then
				homedir="$4"
			fi

			# Set shell only if not null, empty nor '-'
			if [ "${5:--}" != "-" ]; then
				ARGUMENTS="$ARGUMENTS -s $5"
			else
				ARGUMENTS="$ARGUMENTS -s /usr/sbin/nologin"
			fi

			if [ -x /usr/sbin/useradd ]; then
			    if [ -n "$GROUP_ID" ] && [ "$GROUP_ID" != "-" ]; then
				ARGUMENTS="-g $GROUP_ID $ARGUMENTS"
			    else
				# this is useradd/shadow specific
				if /usr/bin/getent group "$1" >> /dev/null; then
				    ARGUMENTS="-g $1 $ARGUMENTS"
				else
				    ARGUMENTS="-U $ARGUMENTS"
				fi
			    fi

			    run /usr/sbin/useradd -r -c "$3" -d "${homedir}" $ARGUMENTS
			elif [ -x "$busybox" ]; then
			    if [ -n "$GROUP_ID" ] && [ "$GROUP_ID" != "-" ]; then
				run $busybox adduser -S -H -g "$3" -G "GROUP_ID" -h "${homedir}" $ARGUMENTS
			    else
				/usr/bin/getent group "$1" >> /dev/null || $busybox addgroup -S "$1"

				run $busybox adduser -S -H -g "$3" -G "$1" -h "${homedir}" $ARGUMENTS
			    fi
			else
				echo "ERROR: neither useradd nor busybox found!"
				exit 1
			fi
		;;
		m)
			shift
			if [ -x /usr/sbin/usermod ] ; then
				run /usr/sbin/usermod -a -G "$2" "$1"
			elif [ -x "$busybox" ]; then
				run $busybox addgroup "$1" "$2"
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
fi
