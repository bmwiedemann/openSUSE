#!/bin/bash
set -e

DEBUG=${DEBUG:-"0"}

[ "${DEBUG}" -eq "1" ] && set -x

HOSTNAME=${HOSTNAME:-$(hostname)}
WORKGROUP=${WORKGROUP:-"WORKGROUP"}

export PATH=/usr/sbin:/sbin:${PATH}

CONFIG_FILE="/etc/samba/smb.conf"

setup_timezone() {
    if [ -n "$TZ" ]; then
	TZ_FILE="/usr/share/zoneinfo/$TZ"
	if [ -f "$TZ_FILE" ]; then
	    echo "Setting container timezone to: $TZ"
	    ln -snf "$TZ_FILE" /etc/localtime
	else
	    echo "Cannot set timezone \"$TZ\": timezone does not exist."
	fi
    fi
}

add_user() {
    IFS=: read -r name password uid group gid <<<"$1"

    echo -n "Add user $name... "
    [[ -n "$group" ]] && { grep -q "^$group:" /etc/group | groupadd ${gid:+-g $gid} "$group"; }
    grep -q "^$name:" /etc/passwd || useradd -M ${group:+-g $group} ${uid:+-u $uid} "$name"
    echo -e "$password\n$password" | smbpasswd -s -a "$name"
    echo "DONE"
}

add_share() {
    IFS=: read -r sharename sharepath browseable ro guest users admins writelist comment <<<"$1"

    echo -n "Add share '$sharename' with path '$sharepath'... "
    echo "[$sharename]" >>"$CONFIG_FILE"
    echo "  path = \"$sharepath\"" >>"$CONFIG_FILE"
    [[ -n "$browseable" ]] && echo "  browseable = $browseable" >>"$CONFIG_FILE"
    [[ -n "$ro" ]] && echo "  read only = $ro" >>"$CONFIG_FILE"
    [[ -n "$guest" ]] && echo "  guest ok = $guest" >>"$CONFIG_FILE"
    [[ -n "$users" ]] && echo "  valid users = $(tr ',' ' ' <<< "$users")" >>"$CONFIG_FILE"
    [[ -n "$admins" ]] && echo "  admin users = $(tr ',' ' ' <<< "$admins")" >>"$CONFIG_FILE"
    [[ -n "$writelist" ]] && echo "  write list = $(tr ',' ' ' <<< "$writelist")" >>"$CONFIG_FILE"
    [[ -n "$comment" ]] && echo "  comment = $(tr '_' ' ' <<< "$comment")" >>"$CONFIG_FILE"
    echo "" >>"$CONFIG_FILE"
    [[ ! -d "$sharepath" ]] && mkdir -p "$sharepath"
    echo "DONE"
}

init_smb_conf() {
    cat >"$CONFIG_FILE" <<EOT
[global]
  workgroup = $WORKGROUP
  server string = $HOSTNAME
  netbios name = $HOSTNAME
  server role = standalone server
;  hosts allow = 192.168.1. 192.168.2. 127.
  security = user
  create mask = 0664
  directory mask = 0775
  force create mode = 0664
  force directory mode = 0775
  load printers = no
  guest account = nobody
  log file = /dev/stdout
  max log size = 50
  map to guest = bad user
  socket options = TCP_NODELAY SO_RCVBUF=8192 SO_SNDBUF=8192
  local master = no
  dns proxy = no
# Security
  client ipc max protocol = SMB3
  client ipc min protocol = SMB2_10
  client max protocol = SMB3
  client min protocol = SMB2_10
  server max protocol = SMB3
  server min protocol = SMB2_10

[homes]
  comment = Home Directories
  valid users = %S, %D%w%S
  browseable = No
  read only = No
  inherit acls = Yes

EOT

}

show_help() {
            cat <<EOT
Samba server container

The container will be configured as samba sharing server and it just needs:
 * host directories to be mounted,
 * users (one or more username:password tuples) provided,
 * shares defined (name, path).

Options:
 -s <name:path>[:browse:readonly:guest:users:admins:writelist:comment]
    Configure a share.
     * name		Required, name of the share
     * path		Required, exported path of the share
     * browse		Optional, if share is seen in a net view
     * readonly		Optional, if share is read-only or read-write
     * guest		Optional
     * users		Optional, comma separated list of valid users
     * admins           Optional, comma separated list of admin users
     * writelist        Optional, comma separated list of of users with write access
     * comment		Optional, '_' will be replaced with a space
 -u <name:password>[:UID:group:GID] 
    Create user with optional UID and group. This option is not recommended
    because the password will be visible by users listing the processes.
     * name		Required, username
     * password		Required, password of user
     * UID		Optional, UID of the user
     * group		Optional, users default group
     * GID		Optional, GID of the group
 -h 
    Display help text and exit

Environment variables:
  DEBUG=[0|1]		Enable debug mode
  TZ=<timezone>		Set timezone
  WORKGROUP=<name>	Specify name of workgroup, default is 'WORKGROUP'
  USER=<name:password>[:UID:group:GID]
  SHARE=<name:path>[:browse:readonly:guest:users:admins:writelist:comment]
  USER_FILE=<filename>	Specify file containing user entries to create
  SHARE_FILE=<filename>	Specify file containing shares to export

Additional variables starting with the same name followed by a number are
supported for 'USER' and 'SHARE', e.g. SHARE, SHARE1, SHARE2, ...

USER_FILE and SHARE_FILE expect files which contain one line per entry in
the format of 'USER' and 'SHARE'.

EOT
}

#
# Main
#

setup_timezone
init_smb_conf

while getopts ":u:s:h" opt; do
    case $opt in
	h)
            show_help
            exit 0
            ;;
	u)
	    add_user "$OPTARG"
            ;;
	s)
	    add_share "$OPTARG"
            ;;
	\?)
            echo "Invalid option: -$OPTARG"
            echo
            show_help
            exit 1
            ;;
	:)
            echo "Error: option -$OPTARG requires an argument."
            echo
            show_help
            exit 1
            ;;
    esac
done

# handle environment variables
while read -r user; do
    add_user "$user"
done < <(env | awk '/^USER[0-9=_]/ {sub (/^[^=]*=/, "", $0); print}')

while read -r share; do
    add_share "$share"
done < <(env | awk '/^SHARE[0-9=_]/ {sub (/^[^=]*=/, "", $0); print}')

if [ -n "${USER_FILE}" ]; then
    while read -r line
    do
        add_user "$line"
    done <<< "$USER_FILE"
fi

if [ -n "${SHARE_FILE}" ]; then
    while read -r line
    do
        add_share "$line"
    done <<< "$SHARE_FILE"
fi

exec catatonit -- smbd -F --debug-stdout --no-process-group --configfile="$CONFIG_FILE" < /dev/null
