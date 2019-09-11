#
# spec file for package ndppd
#
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           ndppd
Version:        0.2.5.43
Release:        0
Summary:        Neighbor Discovery Protocol Proxy Daemon
License:        GPL-3.0-or-later
Group:          Productivity/Networking/System
URL:            https://github.com/DanielAdolfsson/ndppd
#Git-Clone:     https://github.com/DanielAdolfsson/ndppd.git
#Source:         https://github.com/DanielAdolfsson/%%{name}/archive/%%{version}.tar.gz#/%%{name}-%%{version}.tar.gz
Source:         %{name}-%{version}.tar.xz
Source1:        ndppd-tmpfiles.conf
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libnl-3.0)
%{?systemd_requires}

%description
ndppd is a daemon that proxies certain IPv6 NDP messages between two or more
interfaces. It currently supports proxying Neighbor Solicitation Messages
and Neighbor Advertisement messages in order to allow IPv6 routing without
relying on Linux "proxy_ndp".

The daemon is partially compliant with (experimental) RFC4389. 

%prep
%setup -q

%build
export CXXFLAGS='%{optflags}'
make %{?_smp_mflags}

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}
install -D -m0644 %{SOURCE1} %{buildroot}/%{_tmpfilesdir}/%{name}.conf
install -D -m0644 ndppd.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m0644 ndppd.conf-dist %{buildroot}%{_sysconfdir}/ndppd.conf
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcndppd

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc ChangeLog README
%config %{_sysconfdir}/ndppd.conf
%{_sbindir}/ndppd
%{_sbindir}/rcndppd
%{_mandir}/man1/ndppd.1%{?ext_man}
%{_mandir}/man5/ndppd.conf.5%{?ext_man}
%{_tmpfilesdir}/%{name}.conf
%dir %attr(-,root,root) %ghost %{_rundir}/%{name}
%{_unitdir}/%{name}.service

%changelog
