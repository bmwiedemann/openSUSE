#
# spec file for package dmraid
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Requires(postun): coreutils
Url:            http://people.redhat.com/~heinzm/sw/dmraid/src/
Summary:        A Device-Mapper Software RAID Support Tool
License:        GPL-2.0-only
Group:          System/Base
Version:        1.0.0.rc16
Release:        0
Source:         ftp://people.redhat.com/heinzm/sw/dmraid/src/dmraid-%{version}.tar.bz2
Source1:        sysconfig.dmraid
Source3:        README.SUSE
Source6:        dmraid-activation.service
Patch1:         dmraid-1.0.0.rc16-cvs-2010-02-02.patch
Patch2:         dmraid-1.0.0.rc13-geometry.patch
Patch3:         lib-install.patch
Patch4:         handle_spaces
Patch5:         remove_trylock
Patch6:         rebuild.fix
Patch7:         ddf-erase
Patch8:         dmraid-move-var-lock-to-run-lock.patch
Patch9:         dmraid-destdir.patch
Patch10:        fix-undefined-symbol.patch
Patch11:        0001-remove-partitions-with-O_RDONLY.patch
Patch12:        fix-return-function-type.patch

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
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This software discovers, activates, deactivates, and displays
properties of software RAID sets, such as ATARAID, and contained DOS
partitions.

dmraid uses libdevmapper and the device-mapper kernel runtime to create
devices with respective mappings for the ATARAID sets discovered.

%prep
%setup -n dmraid/%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p2
%patch12 -p2

cp %{SOURCE3} .

%build
#rm -f aclocal.m4
autoreconf -fi
rm -r autom4te.cache
%configure \
  --libdir=/%_lib \
  --sbindir=/sbin \
  --with-user=`id -nu` --with-group=`id -ng` \
  --enable-libselinux --enable-libsepol
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%_lib/libdmraid.a
mkdir -p $RPM_BUILD_ROOT%{_fillupdir}
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_fillupdir}/sysconfig.dmraid
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
/sbin/dmraid
/sbin/dmevent_tool
%{_mandir}/man8/*
%doc LICENSE LICENSE_GPL LICENSE_LGPL README README.SUSE TODO doc/*
%{_fillupdir}/sysconfig.dmraid
/%{_lib}/libdmraid-events-isw.so
/%{_lib}/libdmraid.so.1.0.0.rc16-3
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/dmraid.conf
%{_unitdir}/dmraid-activation.service

%files devel
%defattr(-, root, root)
%dir %{_prefix}/include/dmraid
%{_prefix}/include/dmraid
/%{_lib}/libdmraid.so

%changelog
