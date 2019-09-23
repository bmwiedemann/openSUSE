#
# spec file for package ipxrip
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           ipxrip
License:        GPL-2.0+
Group:          Productivity/Networking/Routing
Provides:       ipxripd 
Version:        0.7
Release:        0
Summary:        IPX Routing Daemon
Source:         ipxripd-%{version}.tar.bz2
Source1:        ipxd.service
Patch:          ipxripd-%{version}.dif
Patch1:         ipxripd-%{version}-axp.dif
Patch2:         ipxripd-%{version}-secfix.dif
Patch3:         ipxripd-%{version}-2.6kernel-fix.diff
%{?systemd_requires}
BuildRequires:  systemd-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is an RIP/SAP daemon for Linux. With this daemon, you can turn
your Linux machine into an IPX router.

%prep
%setup -n ipxripd
%patch
%patch1
%patch2
%patch3

%build
make

%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}/%{_unitdir}
install -m 744 %{S:1} %{buildroot}/%{_unitdir}/ipxrip.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}
install -d %{buildroot}%{_sysconfdir}
install -m 644 ipx_ticks %{buildroot}/%{_sysconfdir}

%pre 
%service_add_pre ipxrip.service

%post
%service_add_post ipxrip.service

%preun
%service_del_preun ipxrip.service

%postun
%service_del_postun ipxrip.service

%files
%defattr(-,root,root)
%doc README COPYING
%doc %{_mandir}/man?/*
%{_sbindir}/*
%{_unitdir}/ipxrip.service
%config(noreplace) %{_sysconfdir}/ipx_ticks

%changelog

