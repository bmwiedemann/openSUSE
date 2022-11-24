#
# spec file for package llmnrd
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017-2020, Martin Hauke <mardnh@gmx.de>
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
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           llmnrd
Version:        0.7
Release:        0
Summary:        Link-Local Multicast Resolution (LLMNR) Daemon
License:        GPL-2.0-only
Group:          System/Daemons
URL:            https://github.com/tklauser/llmnrd
Source:         https://github.com/tklauser/llmnrd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        llmnrd.service
Source2:        llmnrd.sysconfig
Source3:        usr.sbin.llmnrd
Patch0:	harden_llmnrd.service.patch
BuildRequires:  apparmor-profiles
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make

%description
llmnrd is a daemon implementing the Link-Local Multicast Name Resolution (LLMNR)
protocol according to RFC 4795. It uses the Netlink kernel interface.

llmnrd will respond to name resolution queries sent by Windows clients in
networks where no DNS server is available. It supports both IPv4 and IPv6.

%prep
%setup -q
%patch0 -p1

%build
export GIT_VERSION=""
export Q=""
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
make prefix=%{_prefix} DESTDIR=%{buildroot} install
install -dm0755 %{buildroot}%{_fillupdir}
install -Dpm0644 %{SOURCE1} "%{buildroot}%{_unitdir}/llmnrd.service"
install -Dpm0644 %{SOURCE2} "%{buildroot}%{_fillupdir}/sysconfig.llmnrd"
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcllmnrd
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.llmnrd

%pre
%service_add_pre llmnrd.service

%post
%service_add_post llmnrd.service
%fillup_only

%preun
%service_del_preun llmnrd.service

%postun
%service_del_postun llmnrd.service

%files
%license COPYING
%doc README.md
%{_bindir}/llmnr-query
%{_sbindir}/llmnrd
%{_sbindir}/rcllmnrd
%{_unitdir}/llmnrd.service
%{_fillupdir}/sysconfig.llmnrd
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.sbin.llmnrd
%{_mandir}/man1/llmnr-query.1%{?ext_man}
%{_mandir}/man8/llmnrd.8%{?ext_man}

%changelog
