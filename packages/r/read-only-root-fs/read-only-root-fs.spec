#
# spec file for package read-only-root-fs
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           read-only-root-fs
Version:        1.0+git20250422.3e17744
Release:        0
Summary:        Files and Scripts for a RO root fileystem
License:        GPL-2.0-or-later
Group:          System/Fhs
URL:            https://github.com/openSUSE/read-only-root-fs
Source:         read-only-root-fs-%{version}.tar.xz
Source1:        README.packaging.txt
BuildRequires:  dracut
BuildRequires:  update-bootloader-rpm-macros
Requires:       dracut
Requires(post): /usr/bin/mv /usr/bin/rsync /usr/bin/gawk /usr/sbin/btrfs
Requires(post): snapper
# Required if system with new /etc/fstab entries is supposed to be updated
Conflicts:      transactional-update < 5.0.0
# Support for /etc as subvolume
Conflicts:      combustion < 1.5
Conflicts:      ignition < 2.21.0
BuildArch:      noarch
%{update_bootloader_requires}

%description
Files, scripts and directories to run the system with a
read-only root filesystem with nested writable %{_sysconfdir} BTRFS subvolume.

This package should never be installed in an already running
system! It should only be selected by a system role for a
read-only root filesystem with transactional updates.
The package will create / modify entries for mounting /etc and /var.
Those entries are used by dracut to mount the overlay file systems
during the early boot phase.

%package volatile
Summary:        Dracut Module to mount a tmpfs overlay on a RO root
Group:          System/Fhs
Requires:       dracut

%description volatile
A dracut module which mounts an overlayfs each on /etc and /var, with the upper
layer in a tmpfs mount. This is the minimal setup to get a booting system, to
have a writable /root or /home, additional fstab entries can be added.

%prep
%autosetup -p1

%build

%install
cp -a etc usr %{buildroot}

%post
if [ "$1" = 1 -a "`findmnt -n -o FSTYPE -l /`" = "btrfs" ] ; then
    %{_libexecdir}/setup-etc-subvol
fi
if [ ! -e /boot/writable -a "`findmnt -n -o FSTYPE -l /`" = "btrfs" ]; then
    %{_sbindir}/mksubvolume /boot/writable
fi
%{?update_bootloader_refresh_post}

%posttrans
if [ -f %{_sysconfdir}/zypp/zypp.conf ]; then
    sed -i 's/^multiversion =.*/multiversion =/g' %{_sysconfdir}/zypp/zypp.conf
fi
# btrfsmaintainence uses as default "/", but that is read-only.
# Change that to /.snapshots/
for var in BTRFS_BALANCE_MOUNTPOINTS BTRFS_SCRUB_MOUNTPOINTS BTRFS_TRIM_MOUNTPOINTS; do
    grep -q "${var}=\"/\"" /etc/sysconfig/btrfsmaintenance && sed -i "s|${var}=.*|${var}=\"/.snapshots\"|g" /etc/sysconfig/btrfsmaintenance
done
%{?update_bootloader_posttrans}
exit 0

%files
%license COPYING
%{_libexecdir}/setup-etc-subvol
%{_prefix}/lib/dracut/dracut.conf.d/10-read-only-root-fs.conf
%dir %{_prefix}/lib/dracut/modules.d/50writable-etc
%{_prefix}/lib/dracut/modules.d/50writable-etc/*
%{_prefix}/lib/systemd/system-preset/*
%dir %{_prefix}/lib/systemd/system/systemd-udevd.service.d
%{_prefix}/lib/systemd/system/systemd-udevd.service.d/etcmount.conf
%dir %{_prefix}/lib/systemd/system/systemd-journal-flush.service.d
%{_prefix}/lib/systemd/system/systemd-journal-flush.service.d/afterlocalfs.conf
%dir %{_prefix}/lib/systemd/system/systemd-remount-fs.service.d
%{_prefix}/lib/systemd/system/systemd-remount-fs.service.d/writableagain.conf
%dir %{_sysconfdir}/grub.d
%config(noreplace) %{_sysconfdir}/grub.d/01_suse_ro_root

%files volatile
%license COPYING
%{_prefix}/lib/dracut/modules.d/99volatile-overlay/

%changelog
