#
# spec file for package dmraid
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?suse_version} >= 1550
%define sbindir %_sbindir
%else
%define sbindir /sbin
%endif

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           dmraid
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  device-mapper-devel
BuildRequires:  libselinux-devel
BuildRequires:  suse-module-tools
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel

Requires:       aaa_base
Requires:       kpartx
Requires(post): coreutils
Requires(postun):coreutils
URL:            http://people.redhat.com/~heinzm/sw/dmraid/src/
Summary:        A Device-Mapper Software RAID Support Tool
License:        GPL-2.0-only
Version:        1.0.0.rc16.3
%define src_version 1.0.0.rc16-3
Release:        0
Source:         https://people.redhat.com/~heinzm/sw/dmraid/src/dmraid-%{src_version}.tar.bz2
Source1:        sysconfig.dmraid
Source3:        README.SUSE
Source6:        dmraid-activation.service
Patch0:         dmraid-1.0.0.rc13-geometry.patch
Patch1:         rebuild.fix
Patch2:         ddf-erase
Patch3:         dmraid-move-var-lock-to-run-lock.patch
Patch4:         fix-undefined-symbol.patch
Patch5:         0001-remove-partitions-with-O_RDONLY.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         %fillup_prereq
%{systemd_requires}

%description
This software discovers, activates, deactivates, and displays
properties of software RAID sets, such as ATARAID, and contained DOS
partitions.

dmraid uses libdevmapper and the device-mapper kernel runtime to create
devices with respective mappings for the ATARAID sets discovered.

The following ATARAID types are supported:

- Highpoint HPT37X

- Highpoint HPT45X

- Intel Software RAID

- Promise FastTrak

- Silicon Image Medley

%package devel
Summary:        Development files for dmraid
Requires:       %{name} = %{version}

%description devel
This software discovers, activates, deactivates, and displays
properties of software RAID sets, such as ATARAID, and contained DOS
partitions.

dmraid uses libdevmapper and the device-mapper kernel runtime to create
devices with respective mappings for the ATARAID sets discovered.

%prep
%setup -n dmraid/%{src_version}/dmraid
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2

cp %{SOURCE3} .

%build
#rm -f aclocal.m4
autoreconf -fi
rm -r autom4te.cache
%configure \
  --with-usrlibdir=%{_libdir} \
%if 0%{?suse_version} < 1550
  --sbindir=%{sbindir} \
%endif
  --with-user=`id -nu` --with-group=`id -ng` \
  --enable-libselinux --enable-libsepol
make

%install
%make_install
rm -f %{buildroot}%{_libdir}/libdmraid.a
mkdir -p %{buildroot}%{_fillupdir}
install -m644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.dmraid
install -D -m 0644 %{S:6} %{buildroot}%{_unitdir}/dmraid-activation.service
install -d %{buildroot}%{_tmpfilesdir}
echo 'd /run/lock/dmraid 0700 root root -' > %{buildroot}%{_tmpfilesdir}/dmraid.conf
# E: spurious-executable-perm (Badness: 50) /usr/include/dmraid/locking.h
chmod -x %{buildroot}%{_prefix}/include/dmraid/*h

%pre
%service_add_pre dmraid-activation.service

%preun
%service_del_preun dmraid-activation.service

%post
/sbin/ldconfig
%service_add_post dmraid-activation.service
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%{fillup_only}

%postun
/sbin/ldconfig
%service_del_postun dmraid-activation.service
%{?regenerate_initrd_post}

%files
%defattr(-, root, root)
%{sbindir}/dmraid
%{sbindir}/dmevent_tool
%{_mandir}/man8/*
%doc LICENSE LICENSE_GPL LICENSE_LGPL README README.SUSE TODO doc/*
%{_fillupdir}/sysconfig.dmraid
%{_libdir}/libdmraid.so.*
%{_libdir}/libdmraid-events-isw.so
%dir %{_libdir}/device-mapper
%{_libdir}/device-mapper/libdmraid-events-isw.so
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/dmraid.conf
%{_unitdir}/dmraid-activation.service

%files devel
%defattr(-, root, root)
%{_prefix}/include/dmraid
%{_libdir}/libdmraid.so

%changelog
