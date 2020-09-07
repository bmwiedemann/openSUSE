#
# spec file for package lldpd
#
# Copyright (c) 2020 SUSE LLC
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


%define lldpd_user lldpd
%define lldpd_group lldpd
%define lldpd_chroot %{_localstatedir}/run/lldpd
%define sover 4
%define libname liblldpctl%{sover}
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           lldpd
Version:        1.0.6
Release:        0
Summary:        Implementation of IEEE 802.1ab (LLDP)
# We have some GPL linux headers in include/linux, they are used on
# platforms where glibc headers are not recent enough
License:        ISC AND GPL-2.0-or-later
Group:          System/Daemons
URL:            http://vincentbernat.github.com/lldpd/
Source0:        http://media.luffy.cx/files/lldpd/%{name}-%{version}.tar.gz
Source1:        lldpd.sysconfig
Source2:        http://media.luffy.cx/files/lldpd/%{name}-%{version}.tar.gz.gpg#/%{name}-%{version}.tar.gz.asc
Source3:        http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0x95A42FE8353525F9#/%{name}.keyring
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libxml-2.0)
Requires(pre):  %fillup_prereq
Requires(pre):  pwdutils

%description
This implementation provides LLDP sending and reception, supports VLAN
and includes an SNMP subagent that can interface to an SNMP agent
through AgentX protocol.

LLDP is an industry standard protocol designed to supplant proprietary
Link-Layer protocols such as Extreme EDP (Extreme Discovery Protocol)
and CDP (Cisco Discovery Protocol). The goal of LLDP is to provide an
inter-vendor compatible mechanism to deliver Link-Layer notifications
to adjacent network devices.

This daemon is also able to deal with CDP, FDP, SONMP and EDP
protocol. It also handles LLDP-MED extension.

%package -n %{libname}
Summary:        Implementation of IEEE 802.1ab - Shared library
License:        MIT
Group:          System/Libraries

%description -n %{libname}
This package provides the shared library for lldpd.

LLDP is an industry standard protocol designed to supplant proprietary
Link-Layer protocols such as Extreme EDP (Extreme Discovery Protocol)
and CDP (Cisco Discovery Protocol). The goal of LLDP is to provide an
inter-vendor compatible mechanism to deliver Link-Layer notifications
to adjacent network devices.

%package devel
Summary:        Implementation of IEEE 802.1ab - Tools and header files for developers
License:        MIT
Group:          Development/Languages/C and C++
Requires:       lldpd = %{version}-%{release}

%description devel
This package is required to develop alternate clients for lldpd.

LLDP is an industry standard protocol designed to supplant proprietary
Link-Layer protocols such as Extreme EDP (Extreme Discovery Protocol)
and CDP (Cisco Discovery Protocol). The goal of LLDP is to provide an
inter-vendor compatible mechanism to deliver Link-Layer notifications
to adjacent network devices.

%prep
%setup -q

%build
%configure \
   --with-snmp \
   --with-xml \
   --with-libbsd \
   --enable-cdp \
   --enable-edp \
   --enable-sonmp \
   --enable-fdp \
   --enable-lldpmed \
   --enable-dot1 \
   --enable-dot3 \
   --enable-custom \
   --disable-oldies \
   --with-privsep-user=%{lldpd_user} \
   --with-privsep-group=%{lldpd_group} \
   --with-privsep-chroot=%{lldpd_chroot} \
   --with-systemdsystemunitdir=%{_unitdir} \
   --with-sysusersdir=no \
   --docdir=%{_docdir}/lldpd \
   --enable-pie \
   --disable-static

[ -f %{_includedir}/net-snmp/agent/struct.h ] || touch src/struct.h
make %{?_smp_mflags} V=1

%install
%make_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.lldpd
install -dm0755 %{buildroot}/%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rclldpd
rm -f %{buildroot}%{_libdir}/liblldpctl.la

%pre
# Create lldpd user/group
if getent group %{lldpd_group} >/dev/null 2>&1 ; then : ; else \
 %{_sbindir}/groupadd -r %{lldpd_group} > /dev/null 2>&1 || exit 1 ; fi
if getent passwd %{lldpd_user} >/dev/null 2>&1 ; then : ; else \
 %{_sbindir}/useradd -g %{lldpd_group} -M -r -s /sbin/nologin \
 -c "LLDP daemon" -d %{lldpd_chroot} %{lldpd_user} 2> /dev/null \
 || exit 1 ; fi

%service_add_pre lldpd.service

%post -n %{libname} -p /sbin/ldconfig
%postun  -n %{libname} -p /sbin/ldconfig
%post
%service_add_post lldpd.service
%fillup_only

%preun
%service_del_preun lldpd.service

%postun
%service_del_postun lldpd.service

%files
%dir %{_docdir}/lldpd
%doc %{_docdir}/lldpd/NEWS
%license %{_docdir}/lldpd/LICENSE
%doc %{_docdir}/lldpd/ChangeLog
%doc %{_docdir}/lldpd/README.md
%doc %{_docdir}/lldpd/CONTRIBUTE.md
%{_sbindir}/lldpd
%{_sbindir}/lldpctl
%{_sbindir}/lldpcli
%{_datadir}/zsh
%{_datadir}/bash-completion
%{_mandir}/man8/lldp*.8%{?ext_man}
%config %{_sysconfdir}/lldpd.d
%{_unitdir}/lldpd.service
%{_sbindir}/rclldpd
%{_fillupdir}/sysconfig.lldpd

%files -n %{libname}
%{_libdir}/liblldpctl.so.*

%files devel
%{_libdir}/liblldpctl.so
%{_libdir}/pkgconfig/lldpctl.pc
%{_includedir}/lldpctl.h
%{_includedir}/lldp-const.h

%changelog
