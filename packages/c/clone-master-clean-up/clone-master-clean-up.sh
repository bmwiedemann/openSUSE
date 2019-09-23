#!/bin/bash

# The script cleans up a system for cloning preparation.
# Author: Howard Guo <hguo@suse.com>

set -e
# bsc#1092378
DROP_IN_FILE=/etc/clone-master-clean-up/custom_remove
SYSCONF_FILE=/etc/sysconfig/clone-master-clean-up

err_exit() {
  echo "Sorry! An error occured on line $1, the clean up routine did not complete successfully."
  exit 1
}
trap 'err_exit $LINENO' ERR

[ "$UID" != "0" ] && echo 'Please run this program as root user.' && exit 1

echo 'The script will delete all SSH keys, log data, and more. Type YES and enter to proceed.'
read answer
[ "$answer" != "YES" ] && exit 1

# source config file
if [ -r "$SYSCONF_FILE" ]; then
    . "$SYSCONF_FILE"
else
    echo 'Failed to read /etc/sysconfig/clone-master-clean-up'
    exit 1
fi

echo 'Wiping active swap devices/files (this may take a while)'
while read swap_name discard; do
  uuid=$(env $(blkid -o export "$swap_name") printenv UUID)
  echo "Turning off swap device/file $swap_name (UUID $uuid)"
  swapoff "$swap_name"
  echo "Zero-overwriting $swap_name..."
  shred -n1 --random-source=/dev/zero "$swap_name"
  mkswap "$swap_name" -U "$uuid"
done < <(tail -n+2 /proc/swaps)

echo 'Removing system registration information and zypper repositories'
> /etc/SUSEConnect
find /etc/zypp \( -iname 'suse*' -o -iname 'scc*' \) -delete

echo "Removing zypper anonymous ID"
rm -rf /var/lib/zypp/AnonymousUniqueId

echo 'Removing SSH host keys, user SSH keys, authorized keys, and shell history'
rm -rf /etc/ssh/ssh_host*key* /root/.ssh/* /home/*/.ssh/* /home/*/.*_history &> /dev/null

echo 'Removing all mails and cron-jobs'
rm -rf /var/spool/mail/*
rm -rf /var/spool/cron/{lastrun,tabs}/*

echo "Clean up postfix"
rm -rf /var/spool/postfix/{active,corrupt,deferred,hold,maildrop,saved,bounce,defer,flush,incoming,trace}/*

echo 'Removing all temporary files'
rm -rf /tmp/* /tmp/.* /var/tmp/* /var/tmp/.* &> /dev/null || true

echo 'Clearing log files and removing log archives'
find /var/log -type f -exec truncate -s 0 {} \;
find /var/log \( -iname '*.old' -o -iname '*.xz' -o -iname '*.gz' \) -delete

echo 'Clearing HANA firewall script'
rm -rf /etc/hana-firewall.d/generated_hana_firewall_script

echo 'Removing random seeds'
for seed in /var/lib/systemd/random-seed /var/lib/misc/random-seed; do
[ -f "$seed" ] && rm -f "$seed"
done

echo 'Clearing systemd journal'
pushd /etc/systemd
cp journald.conf journald.conf.bak
echo -e '\nSystemMaxUse=1K' >> journald.conf
systemctl restart systemd-journald
mv journald.conf.bak journald.conf
popd

echo 'Clearing systemd machine ID file'
truncate -s 0 /etc/machine-id

echo 'Removing domain name and set host name from DHCP in network config'
sed -i 's/^NETCONFIG_DNS_STATIC_SEARCHLIST=.*$/NETCONFIG_DNS_STATIC_SEARCHLIST=""/g' /etc/sysconfig/network/config
sed -i 's/^DHCLIENT_SET_HOSTNAME=.*$/DHCLIENT_SET_HOSTNAME="yes"/g' /etc/sysconfig/network/dhcp

echo 'Removing persistent network interfaces'
netudev=/etc/udev/rules.d/70-persistent-net.rules
if [ -f "$netudev" ]; then
  if grep -i 'automatically generated' "$netudev" &> /dev/null; then
    rm "$netudev"
  fi
fi

echo 'Restoring initial system-wide network config'
truncate -s 0 /etc/{hostname,hosts,resolv.conf}
cat << EOF > /etc/hosts
127.0.0.1       localhost
::1             localhost ipv6-localhost ipv6-loopback
fe00::0         ipv6-localnet
ff00::0         ipv6-mcastprefix
ff02::1         ipv6-allnodes
ff02::2         ipv6-allrouters
ff02::3         ipv6-allhosts
EOF

echo 'Enabling YaST Firstboot if necessary'
[ -e /etc/YaST2/firstboot.xml ] && touch /var/lib/YaST2/reconfig_system

if [ "$CMCU_RSNAP" = "yes" ]; then
    if [ -d /.snapshots ]; then
        echo "Remove all btrfs snapshots from /.snapshot"
        for s in `snapper list | awk '/pre/||/post/{print $3}'`; do
            snapper delete $s
        done
    fi
fi
if [ "$CMCU_ZYPP_REPOS" = "yes" ]; then
    echo "Clean up all zypper repositories"
    rm -rf /etc/zypp/repos.d/*
fi
if [ "$CMCU_SUDOERS" = "yes" ]; then
    echo 'Restoring initial sudoers settings'
    cat << EOF > /etc/sudoers
Defaults always_set_home
Defaults env_reset
Defaults env_keep = "LANG LC_ADDRESS LC_CTYPE LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE LC_TIME LC_ALL LANGUAGE LINGUAS XDG_SESSION_COOKIE"
Defaults secure_path="/usr/sbin:/usr/bin:/sbin:/bin"
Defaults !insults
Defaults targetpw

ALL ALL=(ALL) ALL
root ALL=(ALL) ALL
EOF
fi

echo 'Would you like to give root user a new password? Type YES to set a new password, otherwise simply press Enter.'
read answer
[ "$answer" == "YES" ] && passwd root

if [ "$CMCU_EC2" = "yes" ]; then
    if curl --connect-timeout 3 '169.254.169.254/latest' &> /dev/null; then
       echo 'EC2 specific: allowing ec2-user to run sudo'
       echo 'ec2-user ALL=(ALL) ALL' >> /etc/sudoers
       echo 'Note to EC2 user:'
       echo 'This instance will no longer be accessible after a reboot due to removal of all authorized SSH keys.'
       echo "New SSH key will be installed automatically if you create a new instance from this instance's image."
    fi
fi

if [ "$CMCU_USERIDS" = "yes" ]; then
    echo "clean up user ids >= 1000"
    for i in `awk -F ":" '$3 >= 1000 && $1 !~ /nobody/ {print $1}' /etc/passwd`; do
        userdel -r $i
    done
fi

echo "swap the uuid strings with dev strings in /etc/fstab"
> /tmp/fstab.tmp
while read disk remain; do
    case "$disk" in
    UUID=*)
        uuid=${disk#UUID=}
        new_disk=`/usr/sbin/blkid -U $uuid`
        ;;
    LABEL=*)
        label=${disk#LABEL=}
        new_disk=`/usr/sbin/blkid -L $label`
        ;;
    *)
        new_disk="$disk"
        ;;
    esac
    echo "$new_disk $remain" >> /tmp/fstab.tmp
done < /etc/fstab
if [ -s /tmp/fstab.tmp ]; then
    cp /tmp/fstab.tmp /etc/fstab
fi
rm -rf /tmp/fstab.tmp

echo "Clean up network files (except interfaces using dhcp boot protocol)"
# additional files like bondig interfaces or vlans can be found in 
# /var/adm/clone-master-clean-up/custom_remove.template
for intf in `ls -1 /etc/sysconfig/network/ifcfg-eth*`; do
    bprot=`grep "^BOOTPROTO=" $intf | sed "s/^BOOTPROTO=//"`
    if ! [[ "$bprot" =~ dhcp ]]; then
        rm -rf $intf
    fi
done
if [ -d /var/lib/wicked ]; then
    echo "Clean up persistent network data"
    rm -rf /var/lib/wicked/*
fi

echo "Clean up collectd"
rm -rf /var/lib/collectd/WebYaST/*

echo "Clean up /root"
rm -rf /root/.viminfo /root/.bash_history /root/.Xauthority /root/.ICEauthority /root/.xsession-errors* /root/.dbus/session-bus/* /root/.config/* /root/.cache/*

echo "Clean up cache, crash and coredump"
rm -rf /var/cache/*/* /var/crash/* /var/lib/systemd/coredump/*

# checking for 'drop-in' file
if [ -r "$DROP_IN_FILE" ]; then
    echo "Remove files and directories found in the drop-in file '$DROP_IN_FILE'"
    while read line; do
        [[ "$line" =~ ^# ]] && continue
        if [ -f "$line" ]; then
            rm "$line"
        elif [ -d "$line" ]; then
            rm -rf "$line"
        else
            echo "Error: '$line' has wrong format. At the moment only files or directories are supported."
        fi
    done < $DROP_IN_FILE
fi

echo 'Finished. The system is now sparkling clean. Feel free to shut it down and image it.'

