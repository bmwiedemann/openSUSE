#
# spec file for package pdns-recursor
#
# Copyright (c) 2021 SUSE LLC
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


%if 0%{?suse_version} > 1230
%bcond_without systemd
%else
%bcond_with    systemd
%endif

%if 0%{?fedora_version} >= 24 || 0%{?fc24}%{?fc25}
%bcond_with    systemd_separetedlibs
%else
%bcond_without systemd_separetedlibs
%endif

%if 0%{?suse_version} > 1315 || 0%{?is_opensuse}
%bcond_without pdns_protobuf
%else
%bcond_with    pdns_protobuf
%endif

Name:           pdns-recursor
Version:        4.4.3
Release:        0
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%if 0%{?suse_version} > 1325
%ifnarch s390x
BuildRequires:  libboost_context-devel
%endif
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%endif
%if 0%{?suse_version} == 1315 && 0%{?is_opensuse}
BuildRequires:  boost_1_58_0-devel
%endif
%if ( 0%{?suse_version} <= 1315 && ! 0%{?is_opensuse} ) || 0%{?suse_version} == 1320
BuildRequires:  boost-devel
%endif

BuildRequires:  gcc-c++
BuildRequires:  libsodium-devel
BuildRequires:  lua-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
%if %{without systemd}
PreReq:         %insserv_prereq
%endif
PreReq:         %fillup_prereq
PreReq:         shadow
%else
PreReq:         shadow-utils
%endif
%if %{with pdns_protobuf}
BuildRequires:  protobuf-devel
%endif
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%if %{with systemd_separetedlibs}
BuildRequires:  pkgconfig(libsystemd)
%endif
%{?systemd_requires}
%endif
PreReq:         pdns-common
#
URL:            https://www.powerdns.com/
Source:         https://downloads.powerdns.com/releases/%{name}-%{version}.tar.bz2
Source10:       https://downloads.powerdns.com/releases/%{name}-%{version}.tar.bz2.sig
Source11:       https://powerdns.com/powerdns-keyblock.asc#/pdns-recursor.keyring
Source1:        pdns-recursor.init
Source2:        recursor.conf
#
Summary:        Modern, advanced and high performance recursing/non authoritative nameserver
License:        GPL-2.0-or-later
Group:          Productivity/Networking/DNS/Servers

%description
PowerDNS Recursor is a non authoritative/recursing DNS server. Use this
package if you need a dns cache for your network.


Authors:
--------
    http://www.powerdns.com

%prep
%autosetup -n %{name}-%{version}

%build
autoreconf -fi
ln effective_tld_names.dat effective_tld_list.dat
%configure                           \
  --enable-reproducible              \
  --disable-silent-rules             \
  --bindir=%{_sbindir}               \
  --sysconfdir=%{_sysconfdir}/pdns/  \
%if %{with dnsdist_protobuf}
  --with-protobuf \
%endif
  --with-lua                         \
  --with-socketdir=%{_rundir}        \
  --with-service-user=pdns           \
  --with-service-group=pdns
make %{?_smp_mflags}

%install
make %{?_smp_mflags} install DESTDIR="%{buildroot}"
# config
%{__install} -D -m 0644 %{S:2} %{buildroot}%{_sysconfdir}/pdns/recursor.conf
# init systems
%if %{with systemd}
%{__ln_s} -f %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
# installed by make install
rm -rvf %{buildroot}%{_sysconfdir}/init.d/%{name}
%else
%{__install} -D  -m 0755 %{S:1} %{buildroot}%{_sysconfdir}/init.d/%{name}
%{__ln_s} -f %{_sysconfdir}/init.d/%{name} %{buildroot}%{_sbindir}/rc%{name}
%endif

%clean
%{__rm} -rf %{buildroot}

%pre
%if 0%{?suse_version} && %{with systemd}
%service_add_pre %{name}.service
%endif

%if 0%{?suse_version} && %{with systemd}
%post
%service_add_post %{name}.service
%endif

%if 0%{?suse_version}
%preun
%if %{with systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif
%endif

%if 0%{?suse_version}
%postun
%if %{with systemd}
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%insserv_cleanup
%endif
%endif

%files
%defattr (-,root,root,-)
%config(noreplace)  %attr(640,root,pdns) %{_sysconfdir}/pdns/*.conf
%{_sysconfdir}/pdns/recursor.conf-dist
%if %{with systemd}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%else
%config(noreplace) %{_sysconfdir}/init.d/%{name}
%endif
%{_sbindir}/rcpdns-recursor
%{_sbindir}/pdns_recursor
%{_sbindir}/rec_control
%{_mandir}/man1/pdns_recursor.1*
%{_mandir}/man1/rec_control.1*
%doc README
%license COPYING

%changelog
