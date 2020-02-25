#!/bin/bash
#
# Generates xendomains unit
#

read_conf_from_file() {
	${sbindir}/xl create --quiet --dryrun --defconfig "$1"
}

big2littleendian_32bit(){
	echo ${1:6:2}${1:4:2}${1:2:2}${1:0:2}
}

read_hex() {
	local out_var=$1; shift
	local input=$1; shift
	local pos_var=$1; shift
	local length=$1; shift
	local hex=$(dd bs=1 skip=${!pos_var} count=$length status=none <$input | xxd -p -c$length -l$length)
	read -r $pos_var <<<"$((${!pos_var} + $length))"
	read -r $out_var <<<"$hex"
}

hex2dec() {
	local hex=$1; shift
	local little_endian=$1; shift
	if $little_endian; then
		hex=$(big2littleendian_32bit $hex)
	fi
	echo $((0x$hex))
}

read_conf_from_image(){
	local pos=0 length=0
	
	local magic_header byte_order mandatory_flags optional_flags optional_data_len config_len config_json

	read_hex magic_header $1 pos 32
	# "Xen saved domain, xl format\n \0 \r"
	if [ "$magic_header" != "58656e20736176656420646f6d61696e2c20786c20666f726d61740a2000200d" ]; then
		log $err "Unknown file format in $1. Wrong magic header: '0x$magic_header'"
		return 1
	fi

	read_hex byte_order $1 pos 4
	case "$byte_order" in
	04030201) little_endian=true;;
	01020304) little_endian=false;;
 	*) log $err "Unknown byte order 0x$byte_order in $1"; return 1;;
	esac

	#define XL_MANDATORY_FLAG_JSON (1U << 0) /* config data is in JSON format */
	#define XL_MANDATORY_FLAG_STREAMv2 (1U << 1) /* stream is v2 */
	read_hex mandatory_flags $1 pos 4
	if [ "$(($(hex2dec $mandatory_flags $little_endian) & 0x3))" -ne 3 ]; then
		log $err "Unknown config format or stream version. Mandatory flags are 0x$mandatory_flag"
		return 1
	fi

	read_hex optional_flags $1 pos 4
	read_hex optional_data_len $1 pos 4
	optional_data_len=$(hex2dec $optional_data_len $little_endian)

	# I'll not use but saved memory dump will begin at $((pos+optional_data_len))
	read_hex config_len $1 pos 4
	config_len=$(hex2dec $config_len $little_endian)

	# null terminated string
	read_hex config_json $1 pos $config_len
	xxd -p -r <<<"$config_json"
}

log() {
	local msg_loglevel=$1; shift
	if [ "$msg_loglevel" -gt "$LOGLEVEL" ]; then
		return 0
	fi
	echo "$@" >&2
}


emerg=0; alert=1; crit=2; err=3
warning=4; notice=5; info=6; debug=7
LOGLEVEL=${LOGLEVEL:-4}
if [ "$SYSTEMD_LOG_LEVEL" ]; then
	LOGLEVEL=${!SYSTEMD_LOG_LEVEL}
fi
log $debug "Using loglevel $LOGLEVEL"
trap "log $err Error on \$LINENO: \$(caller)" ERR

log $debug "loading /etc/xen/scripts/hotplugpath.sh..."
. /etc/xen/scripts/hotplugpath.sh

#log $debug "testing for ${sbindir}/xl..."
#CMD=${sbindir}/xl
#if ! $CMD list &> /dev/null; then
#	log $err "${sbindir}/xl list failed!"
#	log $err "$($CMD list &>&1)"
#	exit $?
#fi
#log $debug "${sbindir}/xl list OK!"

log $debug "loading /etc/sysconfig/xendomains..."
XENDOM_CONFIG=/etc/sysconfig/xendomains
if ! test -r $XENDOM_CONFIG; then
	echo "$XENDOM_CONFIG not existing" >&2;
        exit 6
fi

. $XENDOM_CONFIG

doms_conf=()
doms_restore=()
doms_source=()

log $debug "Reading saved domains..."
if [ "$XENDOMAINS_RESTORE" = "true" ] && [ -d "$XENDOMAINS_SAVE" ]; then
        for dom in $XENDOMAINS_SAVE/*; do
		log $debug "Trying $dom..."
        	if ! [ -r $dom ] ; then
			log $debug "Not readable $dom..."
			continue
		fi
	
		log $debug "Reading conf from $dom..."
		if ! dom_conf=$(read_conf_from_image $dom); then
			log $error "Cannot read conf from $dom"
			continue
		fi

		log $debug "Adding $dom to the list"
		doms_conf+=("$dom_conf")
		doms_restore+=(true)
		doms_source+=("$dom")
	done
fi

log $debug "Reading auto domains..."
if [ -d "$XENDOMAINS_AUTO" ]; then
	for dom in $XENDOMAINS_AUTO/*; do
		log $debug "Trying $dom..."
	 	if ! [ -r $dom ] ; then
			log $debug "Not readable $dom..."
			continue
		fi

		log $debug "Reading conf from $dom..."
		if ! dom_conf=$(read_conf_from_file $dom); then
			echo 123
			log $error "Cannot read conf from $dom"
			continue
		fi

		log $debug "Adding $dom to the list"
		doms_conf+=("$dom_conf")
		doms_restore+=(false)
		doms_source+=("$dom")
	done
fi

log $debug "We have ${#doms_conf[*]} to check"
for i in ${!doms_conf[*]}; do
	log $debug "Doing dom $i..."

	dom_conf="${doms_conf[i]}"
	dom_restore="${doms_restore[i]}"
	dom_source="${doms_source[i]}"

	dom_name=$(sed -n 's/^.*(name \(.*\))$/\1/p;s/^.*"name": "\(.*\)",$/\1/p' <<<"$dom_conf")
        readarray -t required_disks <<<"$(sed -n -e '/^    "disks": \[/,/    \],/{ /"pdev_path":/ { s/.*"pdev_path": "//;s/".*//p } }' <<<"$dom_conf")"

	log $debug "dom $i is named $dom_name..."
	for disk in "${required_disks[@]}"; do
		disk_control_var=control_$(tr -d -c '[a-zA-Z0-9_]' <<<"$disk")
		if [ "${!disk_control_var:-0}" -eq 1 ]; then
			log $debug "$disk for $dom_name is already being checked"
			continue
		fi
		declare $disk_control_var=1
		log $debug "waiting for $disk for $dom_name"
		(
			j=0 found_loglevel=$debug
			while true; do
				if [ -e "$disk" ]; then
					log $found_loglevel "disk $disk found (after $j seconds)"
					exit 0
				fi
				if [ "$(( j++ % 5))" -eq 0 ]; then
					log $warning "still waiting for $disk for $dom_name..."
					found_loglevel=$warning
				fi
				sleep 1
			done
		) &
	done
done

wait
log $debug "Exiting normally"
