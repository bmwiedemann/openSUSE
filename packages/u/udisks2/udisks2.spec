#
# spec file for package udisks2
#
# Copyright (c) 2022 SUSE LLC
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


%define somajor 0
%define libudisks lib%{name}-%{somajor}
%define libblockdev_version 2.19
# valid options are 'luks1' or 'luks2' - Note, remove this and the sed call, as upstream moves to luks2 as default
%define default_luks_encryption luks2

Name:           udisks2
Version:        2.9.4
Release:        0
Summary:        Disk Manager
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          System/Daemons
URL:            https://github.com/storaged-project/udisks
Source0:        %{url}/releases/download/udisks-%{version}/udisks-%{version}.tar.bz2
Patch0:         harden_udisks2-zram-setup@.service.patch
Patch1:         harden_udisks2.service.patch
Patch2:         0001-udiskslinuxmountoptions-Do-not-free-static-daemon-re.patch
BuildRequires:  chrpath
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gobject-introspection-devel >= 0.6.2
BuildRequires:  libacl-devel
BuildRequires:  libblockdev-btrfs-devel >= %{libblockdev_version}
BuildRequires:  libblockdev-crypto-devel >= %{libblockdev_version}
BuildRequires:  libblockdev-fs-devel >= %{libblockdev_version}
BuildRequires:  libblockdev-kbd-devel >= %{libblockdev_version}
BuildRequires:  libblockdev-loop-devel >= %{libblockdev_version}
BuildRequires:  libblockdev-lvm-dbus-devel >= %{libblockdev_version}
BuildRequires:  libblockdev-lvm-devel >= %{libblockdev_version}
BuildRequires:  libblockdev-mdraid-devel >= %{libblockdev_version}
BuildRequires:  libblockdev-part-devel >= %{libblockdev_version}
BuildRequires:  libblockdev-swap-devel >= %{libblockdev_version}
BuildRequires:  lvm2-devel
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(blkid) >= 2.17.0
BuildRequires:  pkgconfig(blockdev) >= 2.19
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gudev-1.0) >= 165
BuildRequires:  pkgconfig(libatasmart) >= 0.17
BuildRequires:  pkgconfig(libconfig) >= 1.3.2
BuildRequires:  pkgconfig(libstoragemgmt) >= 1.3.0
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(mount) >= 2.30
BuildRequires:  pkgconfig(polkit-agent-1) >= 0.102
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.102
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(uuid)
Requires:       %{libudisks} = %{version}
# For LUKS devices
Requires:       cryptsetup
# Needed to pull in the system bus daemon
Requires:       dbus-1 >= 1.4.0
# For mkfs.vfat
Requires:       dosfstools
# For mkfs.ext3, mkfs.ext3, e2label
Requires:       e2fsprogs
# For ejecting removable disks
Requires:       eject
# sgdisk is called by udisksd to modify the partition tables... thus a needed tool.
Requires:       gptfdisk
# We need at least this version for bugfixes/features etc.
Requires:       libatasmart-utils >= 0.17
Requires:       libblockdev >= %{libblockdev_version}
Requires:       libblockdev-crypto >= %{libblockdev_version}
Requires:       libblockdev-fs >= %{libblockdev_version}
Requires:       libblockdev-loop >= %{libblockdev_version}
Requires:       libblockdev-mdraid >= %{libblockdev_version}
Requires:       libblockdev-part >= %{libblockdev_version}
Requires:       libblockdev-swap >= %{libblockdev_version}
# Needed to pull in the udev daemon
Requires:       udev >= 208
# For mount, umount, mkswap
Requires:       util-linux
# For mkfs.xfs, xfs_admin
Requires:       xfsprogs
Recommends:     %{libudisks}_btrfs
# Add Obsoletes to ease removal of deprecated standalone vdo module
Obsoletes:      libudisks2-0_vdo <= 2.9.4
%{?systemd_requires}
# Upstream First - Policy:
# Never add any patches to this package without the upstream commit id
# in the patch. Any patches added here without a very good reason to make
# an exception will be silently removed with the next version update.

%description
The Udisks project provides a daemon, tools and libraries to access and
manipulate disks, storage devices and technologies.

%package -n %{libudisks}
Summary:        Dynamic library to access the UDisksd daemon
License:        LGPL-2.0-or-later
Group:          System/Libraries

%description -n %{libudisks}
This package contains the dynamic library, which provides
access to the UDisksd daemon.

%package -n typelib-1_0-UDisks-2_0
Summary:        Introspection bindings for the UDisks Client Library version 2
License:        LGPL-2.0-or-later
Group:          System/Libraries

%description -n typelib-1_0-UDisks-2_0
UDisks provides a daemon, D-Bus API and command line tools
for managing disks and storage devices.

This package provides the GObject Introspection bindings for
the UDisks client library.

%package -n %{libudisks}-devel
Summary:        Development files for UDisks
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{libudisks} >= %{version}

%description -n %{libudisks}-devel
This package contains the development files for the library libUDisks2, a
dynamic library, which provides access to the UDisksd daemon.

%package docs
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description docs
This package contains developer documentation for %{name}.

%package -n %{libudisks}_bcache
Summary:        UDisks module for Bcache
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       %{libudisks} >= %{version}
Requires:       libblockdev-kbd >= %{libblockdev_version}

%description -n %{libudisks}_bcache
This package contains the UDisks module for bcache support.

%package -n %{libudisks}_btrfs
Summary:        UDisks module for btrfs
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       %{libudisks} >= %{version}
Requires:       libblockdev-btrfs >= %{libblockdev_version}

%description -n %{libudisks}_btrfs
This package contains the UDisks module for btrfs support.

%package -n %{libudisks}_lsm
Summary:        UDisks module for LSM
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       %{libudisks} >= %{version}
Requires:       libstoragemgmt >= 1.3.0

%description -n %{libudisks}_lsm
This package contains the UDisks module for LSM support.

%package -n %{libudisks}_lvm2
Summary:        UDisks module for LVM2
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       %{libudisks} >= %{version}
Requires:       libblockdev-lvm >= %{libblockdev_version}
Requires:       lvm2

%description -n %{libudisks}_lvm2
This package contains the UDisks module for LVM2 support.

%package -n %{libudisks}_zram
Summary:        UDisks module for Zram
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       %{libudisks} = %{version}
Requires:       libblockdev-kbd >= %{libblockdev_version}
Requires:       libblockdev-swap >= %{libblockdev_version}

%description -n %{libudisks}_zram
This package contains the UDisks module for zram support.

%lang_package

%prep
%autosetup -p1 -n udisks-%{version}
# Move to luks2 as default
sed -i udisks/udisks2.conf.in -e "s/encryption=luks1/encryption=%{default_luks_encryption}/"

%build
%configure \
	--disable-static \
	--disable-gtk-doc \
	--docdir=%{_docdir}/%{name} \
	--enable-bcache \
	--enable-btrfs \
	--enable-lsm \
	--enable-lvm2 \
	--enable-lvmcache \
	--enable-zram \
	--disable-vdo \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -print -type f -delete
chrpath --delete %{buildroot}/%{_sbindir}/umount.udisks2
chrpath --delete %{buildroot}/%{_bindir}/udisksctl
chrpath --delete %{buildroot}/%{_libexecdir}/udisks2/udisksd
%find_lang udisks2

# Create udisks2 rclink
mkdir -p %{buildroot}/%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}

# Move example config file to docs
mkdir -p %{buildroot}%{_docdir}/%{name}
mv -v %{buildroot}%{_sysconfdir}/udisks2/mount_options.conf.example %{buildroot}%{_docdir}/%{name}/mount_options.conf.example

%post -n %{libudisks} -p /sbin/ldconfig
%postun -n %{libudisks} -p /sbin/ldconfig

%pre -n %{name}
%service_add_pre udisks2.service

%post -n %{name}
%{?udev_rules_update:%udev_rules_update}
%service_add_post udisks2.service
%tmpfiles_create %{_tmpfilesdir}/udisks2.conf

%preun -n %{name}
%service_del_preun udisks2.service

%postun -n %{name}
%service_del_postun udisks2.service

%pre -n %{libudisks}_zram
%service_add_pre udisks2-zram-setup@.service

%post -n %{libudisks}_zram
%service_add_post udisks2-zram-setup@.service

%preun -n %{libudisks}_zram
%service_del_preun udisks2-zram-setup@.service

%postun -n %{libudisks}_zram
%service_del_postun udisks2-zram-setup@.service

%files
%doc AUTHORS NEWS
%{_bindir}/udisksctl
%{_datadir}/dbus-1/system.d/org.freedesktop.UDisks2.conf
%dir %{_sysconfdir}/udisks2
%dir %{_sysconfdir}/udisks2/modules.conf.d
%config %{_sysconfdir}/udisks2/udisks2.conf
%doc %{_docdir}/%{name}/mount_options.conf.example
%{_tmpfilesdir}/udisks2.conf
%ghost %{_rundir}/media
%{_datadir}/bash-completion/completions/udisksctl
%{_unitdir}/udisks2.service
%dir %{_udevrulesdir}
%{_udevrulesdir}/80-udisks2.rules
%{_udevrulesdir}/90-udisks2-zram.rules
%{_sbindir}/rc%{name}
%{_sbindir}/umount.udisks2
%dir %{_libexecdir}/udisks2
%{_libexecdir}/udisks2/udisksd
%{_mandir}/man1/udisksctl.1%{?ext_man}
%{_mandir}/man5/udisks2.conf.5%{?ext_man}
%{_mandir}/man8/udisksd.8%{?ext_man}
%{_mandir}/man8/udisks.8%{?ext_man}
%{_mandir}/man8/umount.udisks2.8%{?ext_man}
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.UDisks2.service
# Permissions for local state data are 0700 to avoid leaking information
# about e.g. mounts to unprivileged users
%attr(0700,root,root) %dir %{_localstatedir}/lib/udisks2

%files -n %{libudisks}
%license COPYING
%{_libdir}/libudisks2.so.*

%files -n typelib-1_0-UDisks-2_0
%{_libdir}/girepository-1.0/UDisks-2.0.typelib

%files -n %{libudisks}-devel
%doc HACKING README.md
%{_libdir}/libudisks2.so
%dir %{_includedir}/udisks2
%dir %{_includedir}/udisks2/udisks
%{_includedir}/udisks2/udisks/*.h
%{_libdir}/pkgconfig/udisks2.pc
%{_libdir}/pkgconfig/udisks2-bcache.pc
%{_libdir}/pkgconfig/udisks2-btrfs.pc
%{_libdir}/pkgconfig/udisks2-lsm.pc
%{_libdir}/pkgconfig/udisks2-lvm2.pc
%{_libdir}/pkgconfig/udisks2-zram.pc
%{_datadir}/gir-1.0/UDisks-2.0.gir

%files docs
%doc %{_datadir}/gtk-doc/html/udisks2/

%files -n %{libudisks}_bcache
%dir %{_libdir}/udisks2
%dir %{_libdir}/udisks2/modules
%{_libdir}/udisks2/modules/libudisks2_bcache.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.bcache.policy

%files -n %{libudisks}_btrfs
%dir %{_libdir}/udisks2
%dir %{_libdir}/udisks2/modules
%{_libdir}/udisks2/modules/libudisks2_btrfs.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.btrfs.policy

%files -n %{libudisks}_lsm
%dir %{_sysconfdir}/udisks2/modules.conf.d
%attr(0600,root,root) %config %{_sysconfdir}/udisks2/modules.conf.d/udisks2_lsm.conf
%dir %{_libdir}/udisks2
%dir %{_libdir}/udisks2/modules
%{_libdir}/udisks2/modules/libudisks2_lsm.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.lsm.policy
%{_mandir}/man5/udisks2_lsm.conf.5%{?ext_man}

%files -n %{libudisks}_lvm2
%dir %{_libdir}/udisks2
%dir %{_libdir}/udisks2/modules
%{_libdir}/udisks2/modules/libudisks2_lvm2.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.lvm2.policy

%files -n %{libudisks}_zram
%dir %{_libdir}/udisks2
%dir %{_libdir}/udisks2/modules
%{_libdir}/udisks2/modules/libudisks2_zram.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.zram.policy
%{_unitdir}/udisks2-zram-setup@.service

%files lang -f udisks2.lang

%changelog
