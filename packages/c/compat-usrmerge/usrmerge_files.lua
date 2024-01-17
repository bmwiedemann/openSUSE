usrmerge_files = {
-- aaa_base
["/sbin/refresh_initrd"] = 1,
["/sbin/service"] = 1,
["/sbin/smart_agetty"] = 1,
-- apparmor-parser
["/sbin/apparmor_parser"] = 1,
["/sbin/rcapparmor"] = 1,
-- audit
["/sbin/audispd"] = 1,
["/sbin/auditctl"] = 1,
["/sbin/auditd"] = 1,
["/sbin/augenrules"] = 1,
["/sbin/aureport"] = 1,
["/sbin/ausearch"] = 1,
["/sbin/autrace"] = 1,
-- aws-efs-utils
["/sbin/mount.efs"] = 1,
-- bash
["/bin/bash"] = 1,
["/bin/sh"] = 1,
-- biosdevname
["/sbin/biosdevname"] = 1,
-- blktrace
["/bin/blkparse"] = 1,
["/bin/blktrace"] = 1,
["/bin/btrace"] = 1,
-- blog
["/sbin/blogctl"] = 1,
["/sbin/blogd"] = 1,
["/sbin/blogger"] = 1,
["/sbin/isserial"] = 1,
["/sbin/setconsole"] = 1,
["/sbin/showconsole"] = 1,
-- btrfsprogs
["/sbin/btrfs"] = 1,
["/sbin/btrfs-convert"] = 1,
["/sbin/btrfs-image"] = 1,
["/sbin/btrfsck"] = 1,
["/sbin/btrfstune"] = 1,
["/sbin/fsck.btrfs"] = 1,
["/sbin/mkfs.btrfs"] = 1,
-- ceph-common
["/sbin/mount.ceph"] = 1,
-- cifs-utils
["/sbin/mount.cifs"] = 1,
["/sbin/mount.smb3"] = 1,
-- coreutils coreutils-single
["/bin/arch"] = 1,
["/bin/basename"] = 1,
["/bin/cat"] = 1,
["/bin/chgrp"] = 1,
["/bin/chmod"] = 1,
["/bin/chown"] = 1,
["/bin/cp"] = 1,
["/bin/date"] = 1,
["/bin/dd"] = 1,
["/bin/df"] = 1,
["/bin/echo"] = 1,
["/bin/false"] = 1,
["/bin/ln"] = 1,
["/bin/ls"] = 1,
["/bin/md5sum"] = 1,
["/bin/mkdir"] = 1,
["/bin/mknod"] = 1,
["/bin/mktemp"] = 1,
["/bin/mv"] = 1,
["/bin/pwd"] = 1,
["/bin/readlink"] = 1,
["/bin/rm"] = 1,
["/bin/rmdir"] = 1,
["/bin/sleep"] = 1,
["/bin/sort"] = 1,
["/bin/stat"] = 1,
["/bin/stty"] = 1,
["/bin/sync"] = 1,
["/bin/touch"] = 1,
["/bin/true"] = 1,
["/bin/uname"] = 1,
-- cpio
["/bin/cpio"] = 1,
-- crda
["/sbin/crda"] = 1,
["/sbin/regdbdump"] = 1,
-- cryptsetup
["/sbin/cryptsetup"] = 1,
-- dash
["/bin/dash"] = 1,
-- davfs2
["/sbin/mount.davfs"] = 1,
["/sbin/umount.davfs"] = 1,
-- dbus-1
["/bin/dbus-cleanup-sockets"] = 1,
["/bin/dbus-daemon"] = 1,
["/bin/dbus-monitor"] = 1,
["/bin/dbus-send"] = 1,
["/bin/dbus-test-tool"] = 1,
["/bin/dbus-update-activation-environment"] = 1,
["/bin/dbus-uuidgen"] = 1,
-- dd_rescue
["/bin/dd_rescue"] = 1,
-- dd_rhelp
["/bin/dd_rhelp"] = 1,
-- device-mapper
["/sbin/dmsetup"] = 1,
-- dhcp-client
["/sbin/dhclient"] = 1,
["/sbin/dhclient-script"] = 1,
["/sbin/dhclient6"] = 1,
-- diod
["/sbin/mount.diod"] = 1,
-- dmraid
["/sbin/dmevent_tool"] = 1,
["/sbin/dmraid"] = 1,
-- dosfstools
["/sbin/dosfsck"] = 1,
["/sbin/dosfslabel"] = 1,
["/sbin/fsck.fat"] = 1,
["/sbin/fsck.msdos"] = 1,
["/sbin/fsck.vfat"] = 1,
["/sbin/mkdosfs"] = 1,
["/sbin/mkfs.fat"] = 1,
["/sbin/mkfs.msdos"] = 1,
["/sbin/mkfs.vfat"] = 1,
-- dracut
["/sbin/installkernel"] = 1,
["/sbin/mkinitrd"] = 1,
-- drbd-utils
["/sbin/drbdadm"] = 1,
["/sbin/drbdmeta"] = 1,
["/sbin/drbdmon"] = 1,
["/sbin/drbdsetup"] = 1,
-- e2fsprogs
["/sbin/badblocks"] = 1,
["/sbin/debugfs"] = 1,
["/sbin/dumpe2fs"] = 1,
["/sbin/e2fsck"] = 1,
["/sbin/e2image"] = 1,
["/sbin/e2label"] = 1,
["/sbin/e2mmpstatus"] = 1,
["/sbin/e2undo"] = 1,
["/sbin/fsck.ext2"] = 1,
["/sbin/fsck.ext3"] = 1,
["/sbin/fsck.ext4"] = 1,
["/sbin/logsave"] = 1,
["/sbin/mke2fs"] = 1,
["/sbin/mkfs.ext2"] = 1,
["/sbin/mkfs.ext3"] = 1,
["/sbin/mkfs.ext4"] = 1,
["/sbin/resize2fs"] = 1,
["/sbin/tune2fs"] = 1,
-- ecryptfs-utils
["/sbin/mount.ecryptfs"] = 1,
["/sbin/mount.ecryptfs_private"] = 1,
["/sbin/umount.ecryptfs"] = 1,
["/sbin/umount.ecryptfs_private"] = 1,
-- ed
["/bin/ed"] = 1,
-- elilo
["/sbin/elilo"] = 1,
["/sbin/eliloalt"] = 1,
-- exfat-utils
["/sbin/dumpexfat"] = 1,
["/sbin/exfatfsck"] = 1,
["/sbin/exfatlabel"] = 1,
["/sbin/fsck.exfat"] = 1,
["/sbin/mkexfatfs"] = 1,
["/sbin/mkfs.exfat"] = 1,
-- f2fs-tools-compat
["/sbin/defrag.f2fs"] = 1,
["/sbin/dump.f2fs"] = 1,
["/sbin/f2fstat"] = 1,
["/sbin/fibmap.f2fs"] = 1,
["/sbin/fsck.f2fs"] = 1,
["/sbin/mkfs.f2fs"] = 1,
["/sbin/parse.f2fs"] = 1,
["/sbin/resize.f2fs"] = 1,
["/sbin/sload.f2fs"] = 1,
-- fedfs-utils-client
["/sbin/mount.fedfs"] = 1,
-- fillup
["/bin/fillup"] = 1,
-- findutils
["/bin/find"] = 1,
-- fuse
["/sbin/mount.fuse"] = 1,
-- fuse-exfat
["/sbin/mount.exfat"] = 1,
["/sbin/mount.exfat-fuse"] = 1,
-- fxload
["/sbin/fxload"] = 1,
-- gawk
["/bin/gawk"] = 1,
-- gawk mawk
["/bin/awk"] = 1,
-- glibc
["/sbin/ldconfig"] = 1,
-- glusterfs
["/sbin/mount.glusterfs"] = 1,
-- grep
["/bin/egrep"] = 1,
["/bin/fgrep"] = 1,
["/bin/grep"] = 1,
-- grubby
["/sbin/grubby"] = 1,
["/sbin/new-kernel-pkg"] = 1,
-- gzip
["/bin/gunzip"] = 1,
["/bin/gzip"] = 1,
["/bin/zcat"] = 1,
-- hdparm
["/sbin/hdparm"] = 1,
["/sbin/wiper.sh"] = 1,
-- hostname
["/bin/dnsdomainname"] = 1,
["/bin/domainname"] = 1,
["/bin/hostname"] = 1,
["/bin/nisdomainname"] = 1,
["/bin/ypdomainname"] = 1,
-- info
["/sbin/install-info"] = 1,
-- info4
["/sbin/install-info4"] = 1,
-- initviocons
["/bin/initviocons"] = 1,
-- insserv-compat
["/sbin/chkconfig"] = 1,
["/sbin/insserv"] = 1,
-- iproute2
["/bin/ip"] = 1,
["/sbin/ip"] = 1,
-- iputils
["/bin/arping"] = 1,
["/bin/clockdiff"] = 1,
["/bin/ping"] = 1,
["/bin/ping6"] = 1,
["/bin/tracepath"] = 1,
["/bin/tracepath6"] = 1,
["/sbin/rdisc"] = 1,
-- ipvsadm
["/sbin/ipvsadm"] = 1,
["/sbin/ipvsadm-restore"] = 1,
["/sbin/ipvsadm-save"] = 1,
-- iscsiuio
["/sbin/brcm_iscsiuio"] = 1,
["/sbin/iscsiuio"] = 1,
-- jfsutils
["/sbin/fsck.jfs"] = 1,
["/sbin/jfs_debugfs"] = 1,
["/sbin/jfs_fsck"] = 1,
["/sbin/jfs_fscklog"] = 1,
["/sbin/jfs_logdump"] = 1,
["/sbin/jfs_mkfs"] = 1,
["/sbin/jfs_tune"] = 1,
["/sbin/mkfs.jfs"] = 1,
-- kbd
["/bin/chvt"] = 1,
["/bin/clrunimap"] = 1,
["/bin/deallocvt"] = 1,
["/bin/dumpkeys"] = 1,
["/bin/fgconsole"] = 1,
["/bin/getkeycodes"] = 1,
["/bin/getunimap"] = 1,
["/bin/kbd_mode"] = 1,
["/bin/kbdinfo"] = 1,
["/bin/kbdrate"] = 1,
["/bin/loadkeys"] = 1,
["/bin/loadunimap"] = 1,
["/bin/mapscrn"] = 1,
["/bin/openvt"] = 1,
["/bin/outpsfheader"] = 1,
["/bin/psfaddtable"] = 1,
["/bin/psfgettable"] = 1,
["/bin/psfstriptable"] = 1,
["/bin/psfxtable"] = 1,
["/bin/resizecons"] = 1,
["/bin/screendump"] = 1,
["/bin/setfont"] = 1,
["/bin/setkeycodes"] = 1,
["/bin/setleds"] = 1,
["/bin/setlogcons"] = 1,
["/bin/setmetamode"] = 1,
["/bin/setpalette"] = 1,
["/bin/setvesablank"] = 1,
["/bin/setvtrgb"] = 1,
["/bin/showconsolefont"] = 1,
["/bin/showkey"] = 1,
["/bin/spawn_console"] = 1,
["/bin/spawn_login"] = 1,
["/bin/unicode_start"] = 1,
["/bin/unicode_stop"] = 1,
["/sbin/fbtest"] = 1,
-- kexec-tools
["/sbin/kexec"] = 1,
-- keyutils
["/bin/keyctl"] = 1,
["/sbin/key.dns_resolver"] = 1,
["/sbin/request-key"] = 1,
-- klogd
["/sbin/klogd"] = 1,
-- kmod
["/bin/lsmod"] = 1,
["/sbin/depmod"] = 1,
["/sbin/insmod"] = 1,
["/sbin/lsmod"] = 1,
["/sbin/modinfo"] = 1,
["/sbin/modprobe"] = 1,
["/sbin/rmmod"] = 1,
-- kpartx
["/sbin/kpartx"] = 1,
-- ksh
["/bin/ksh93"] = 1,
-- ksh mksh
["/bin/ksh"] = 1,
-- libewf-tools
["/sbin/mount.ewf"] = 1,
["/sbin/umount.ewf"] = 1,
-- live-net-installer
["/bin/extend"] = 1,
-- lvm2
["/sbin/lvchange"] = 1,
["/sbin/lvconvert"] = 1,
["/sbin/lvcreate"] = 1,
["/sbin/lvdisplay"] = 1,
["/sbin/lvextend"] = 1,
["/sbin/lvm"] = 1,
["/sbin/lvmconfig"] = 1,
["/sbin/lvmdiskscan"] = 1,
["/sbin/lvmdump"] = 1,
["/sbin/lvmpolld"] = 1,
["/sbin/lvmsadc"] = 1,
["/sbin/lvmsar"] = 1,
["/sbin/lvreduce"] = 1,
["/sbin/lvremove"] = 1,
["/sbin/lvrename"] = 1,
["/sbin/lvresize"] = 1,
["/sbin/lvs"] = 1,
["/sbin/lvscan"] = 1,
["/sbin/pvchange"] = 1,
["/sbin/pvck"] = 1,
["/sbin/pvcreate"] = 1,
["/sbin/pvdisplay"] = 1,
["/sbin/pvmove"] = 1,
["/sbin/pvremove"] = 1,
["/sbin/pvresize"] = 1,
["/sbin/pvs"] = 1,
["/sbin/pvscan"] = 1,
["/sbin/vgcfgbackup"] = 1,
["/sbin/vgcfgrestore"] = 1,
["/sbin/vgchange"] = 1,
["/sbin/vgck"] = 1,
["/sbin/vgconvert"] = 1,
["/sbin/vgcreate"] = 1,
["/sbin/vgdisplay"] = 1,
["/sbin/vgexport"] = 1,
["/sbin/vgextend"] = 1,
["/sbin/vgimport"] = 1,
["/sbin/vgimportclone"] = 1,
["/sbin/vgmerge"] = 1,
["/sbin/vgmknodes"] = 1,
["/sbin/vgreduce"] = 1,
["/sbin/vgremove"] = 1,
["/sbin/vgrename"] = 1,
["/sbin/vgs"] = 1,
["/sbin/vgscan"] = 1,
["/sbin/vgsplit"] = 1,
-- mailutils mailx
["/bin/mail"] = 1,
-- makedev
["/sbin/MAKEDEV"] = 1,
-- mawk
["/bin/mawk"] = 1,
-- mcstrans
["/sbin/mcstransd"] = 1,
-- mdadm
["/sbin/mdadm"] = 1,
["/sbin/mdmon"] = 1,
-- mingetty
["/sbin/mingetty"] = 1,
-- mksh
["/bin/lksh"] = 1,
["/bin/mksh"] = 1,
["/bin/pdksh"] = 1,
-- multipath-tools
["/sbin/mpathpersist"] = 1,
["/sbin/multipath"] = 1,
["/sbin/multipathd"] = 1,
-- munin
["/sbin/rcmunin-cgi-graph"] = 1,
["/sbin/rcmunin-cgi-html"] = 1,
-- munin-node
["/sbin/rcmunin-node"] = 1,
-- net-tools
["/sbin/ether-wake"] = 1,
["/sbin/nameif"] = 1,
["/sbin/plipconfig"] = 1,
["/sbin/slattach"] = 1,
-- net-tools-deprecated
["/bin/ifconfig"] = 1,
["/bin/netstat"] = 1,
["/bin/route"] = 1,
["/sbin/arp"] = 1,
["/sbin/ipmaddr"] = 1,
["/sbin/iptunnel"] = 1,
-- netconsole-tools
["/sbin/netconsole-server"] = 1,
-- nfs-client
["/sbin/mount.nfs"] = 1,
["/sbin/mount.nfs4"] = 1,
["/sbin/umount.nfs"] = 1,
["/sbin/umount.nfs4"] = 1,
-- nfs-kernel-server
["/sbin/nfsdcltrack"] = 1,
-- nilfs-utils
["/sbin/mkfs.nilfs2"] = 1,
["/sbin/mount.nilfs2"] = 1,
["/sbin/nilfs_cleanerd"] = 1,
["/sbin/umount.nilfs2"] = 1,
-- ntfs-3g
["/sbin/mount.lowntfs-3g"] = 1,
["/sbin/mount.ntfs"] = 1,
["/sbin/mount.ntfs-3g"] = 1,
-- ntfsprogs
["/sbin/mkfs.ntfs"] = 1,
-- ocfs2-tools
["/sbin/fsck.ocfs2"] = 1,
["/sbin/mkfs.ocfs2"] = 1,
["/sbin/mount.ocfs2"] = 1,
["/sbin/mounted.ocfs2"] = 1,
["/sbin/o2cluster"] = 1,
["/sbin/ocfs2_hb_ctl"] = 1,
["/sbin/tunefs.ocfs2"] = 1,
-- ocfs2-tools-o2cb
["/sbin/o2cb"] = 1,
["/sbin/o2cb.init"] = 1,
["/sbin/o2cb_ctl"] = 1,
["/sbin/ocfs2.init"] = 1,
-- ooRexx
["/sbin/rcooRexx"] = 1,
-- open-iscsi
["/sbin/iscsi-gen-initiatorname"] = 1,
["/sbin/iscsi-iname"] = 1,
["/sbin/iscsi_discovery"] = 1,
["/sbin/iscsi_fw_login"] = 1,
["/sbin/iscsi_offload"] = 1,
["/sbin/iscsiadm"] = 1,
["/sbin/iscsid"] = 1,
["/sbin/iscsistart"] = 1,
-- open-vm-tools
["/sbin/mount.vmhgfs"] = 1,
-- pam
["/sbin/faillock"] = 1,
["/sbin/mkhomedir_helper"] = 1,
["/sbin/pam_namespace_helper"] = 1,
["/sbin/pam_timestamp_check"] = 1,
["/sbin/pwhistory_helper"] = 1,
["/sbin/unix2_chkpwd"] = 1,
["/sbin/unix_chkpwd"] = 1,
["/sbin/unix_update"] = 1,
-- pam-deprecated
["/sbin/pam_tally2"] = 1,
-- pam_mount
["/sbin/mount.crypt"] = 1,
["/sbin/mount.crypt_LUKS"] = 1,
["/sbin/umount.crypt"] = 1,
["/sbin/umount.crypt_LUKS"] = 1,
-- pciutils
["/sbin/lspci"] = 1,
["/sbin/setpci"] = 1,
-- pcmciautils
["/sbin/lspcmcia"] = 1,
["/sbin/pccardctl"] = 1,
-- perl-Bootloader
["/sbin/pbl"] = 1,
["/sbin/update-bootloader"] = 1,
-- plymouth
["/bin/plymouth"] = 1,
-- policycoreutils
["/sbin/restorecon"] = 1,
["/sbin/restorecon_xattr"] = 1,
["/sbin/setfiles"] = 1,
-- polkit-default-privs
["/sbin/chkstat-polkit"] = 1,
["/sbin/set_polkit_default_privs"] = 1,
-- powerd
["/sbin/detectups"] = 1,
["/sbin/powerd"] = 1,
-- procps
["/bin/pgrep"] = 1,
["/bin/pkill"] = 1,
["/bin/ps"] = 1,
["/sbin/sysctl"] = 1,
-- psmisc
["/bin/fuser"] = 1,
-- rarpd
["/sbin/rarpd"] = 1,
-- rash
["/bin/rash"] = 1,
-- reiserfs
["/sbin/debugfs.reiserfs"] = 1,
["/sbin/debugreiserfs"] = 1,
["/sbin/fsck.reiserfs"] = 1,
["/sbin/mkfs.reiserfs"] = 1,
["/sbin/mkreiserfs"] = 1,
["/sbin/reiserfsck"] = 1,
["/sbin/reiserfstune"] = 1,
["/sbin/resize_reiserfs"] = 1,
["/sbin/tunefs.reiserfs"] = 1,
-- rpcbind
["/bin/rpcinfo"] = 1,
["/sbin/pmap_set2"] = 1,
["/sbin/rpcbind"] = 1,
["/sbin/rpcinfo"] = 1,
-- rpm
["/bin/rpm"] = 1,
-- rsyslog
["/sbin/rsyslogd"] = 1,
-- rungetty
["/sbin/rungetty"] = 1,
-- scsh
["/bin/scsh"] = 1,
-- scsirastools
["/sbin/getmd"] = 1,
["/sbin/mdevt"] = 1,
["/sbin/sgdefects"] = 1,
["/sbin/sgdiag"] = 1,
["/sbin/sgdiskmon"] = 1,
["/sbin/sgdskfl"] = 1,
["/sbin/sgevt"] = 1,
["/sbin/sgmode"] = 1,
["/sbin/sgraidmon"] = 1,
["/sbin/sgsafte"] = 1,
-- sdparm
["/sbin/sas_disk_blink"] = 1,
["/sbin/scsi_ch_swp"] = 1,
["/sbin/sdparm"] = 1,
-- sed
["/bin/sed"] = 1,
-- supportutils
["/sbin/analyzevmcore"] = 1,
["/sbin/chkbin"] = 1,
["/sbin/getappcore"] = 1,
["/sbin/supportconfig"] = 1,
-- sysconfig
["/sbin/ifuser"] = 1,
["/sbin/rcnetwork"] = 1,
-- sysconfig-netconfig
["/sbin/netconfig"] = 1,
-- syslog-ng
["/sbin/syslog-ng"] = 1,
-- syslogd
["/sbin/syslogd"] = 1,
-- systemd-sysvinit
["/sbin/halt"] = 1,
["/sbin/init"] = 1,
["/sbin/poweroff"] = 1,
["/sbin/reboot"] = 1,
["/sbin/runlevel"] = 1,
["/sbin/shutdown"] = 1,
["/sbin/telinit"] = 1,
-- sysvinit-tools
["/bin/fsync"] = 1,
["/bin/usleep"] = 1,
["/sbin/checkproc"] = 1,
["/sbin/fstab-decode"] = 1,
["/sbin/killall5"] = 1,
["/sbin/killproc"] = 1,
["/sbin/mkill"] = 1,
["/sbin/pidofproc"] = 1,
["/sbin/rvmtab"] = 1,
["/sbin/start_daemon"] = 1,
["/sbin/startproc"] = 1,
["/sbin/vhangup"] = 1,
-- tar
["/bin/tar"] = 1,
-- tcsh
["/bin/csh"] = 1,
["/bin/tcsh"] = 1,
-- tomoyo-tools
["/sbin/tomoyo-init"] = 1,
-- tunctl
["/sbin/tunctl"] = 1,
-- udhcp
["/sbin/udhcpc"] = 1,
-- util-linux
["/bin/dmesg"] = 1,
["/bin/kill"] = 1,
["/bin/login"] = 1,
["/bin/more"] = 1,
["/bin/mount"] = 1,
["/bin/su"] = 1,
["/bin/umount"] = 1,
["/sbin/agetty"] = 1,
["/sbin/blkid"] = 1,
["/sbin/blockdev"] = 1,
["/sbin/cfdisk"] = 1,
["/sbin/chcpu"] = 1,
["/sbin/ctrlaltdel"] = 1,
["/sbin/fdisk"] = 1,
["/sbin/findfs"] = 1,
["/sbin/fsck"] = 1,
["/sbin/fsck.cramfs"] = 1,
["/sbin/fsck.minix"] = 1,
["/sbin/fsfreeze"] = 1,
["/sbin/fstrim"] = 1,
["/sbin/hwclock"] = 1,
["/sbin/losetup"] = 1,
["/sbin/mkfs"] = 1,
["/sbin/mkfs.bfs"] = 1,
["/sbin/mkfs.cramfs"] = 1,
["/sbin/mkfs.minix"] = 1,
["/sbin/mkswap"] = 1,
["/sbin/nologin"] = 1,
["/sbin/pivot_root"] = 1,
["/sbin/raw"] = 1,
["/sbin/sfdisk"] = 1,
["/sbin/swaplabel"] = 1,
["/sbin/swapoff"] = 1,
["/sbin/swapon"] = 1,
["/sbin/switch_root"] = 1,
["/sbin/wipefs"] = 1,
-- util-linux-systemd
["/bin/findmnt"] = 1,
["/bin/logger"] = 1,
["/bin/lsblk"] = 1,
-- vim
["/bin/ex"] = 1,
["/bin/vi"] = 1,
["/bin/vim"] = 1,
-- virtualbox
["/sbin/vboxconfig"] = 1,
-- virtualbox-guest-tools
["/sbin/mount.vboxsf"] = 1,
-- virtualbox-qt
["/sbin/vbox-fix-usb-rules.sh"] = 1,
-- vlan
["/sbin/vconfig"] = 1,
-- wicked-service
["/sbin/ifdown"] = 1,
["/sbin/ifprobe"] = 1,
["/sbin/ifstatus"] = 1,
["/sbin/ifup"] = 1,
-- xfsdump
["/sbin/xfsdump"] = 1,
["/sbin/xfsrestore"] = 1,
-- xfsprogs
["/sbin/fsck.xfs"] = 1,
["/sbin/mkfs.xfs"] = 1,
["/sbin/xfs_repair"] = 1,
-- yast2
["/sbin/yast"] = 1,
["/sbin/yast2"] = 1,
-- zsh
["/bin/zsh"] = 1,
}
