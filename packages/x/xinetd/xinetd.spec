#
# spec file for package xinetd
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif
Name:           xinetd
Version:        2.3.15.4
Release:        0
Summary:        An 'inetd' with Expanded Functionality
License:        xinetd
Group:          Productivity/Networking/System
URL:            https://github.com/openSUSE/xinetd/
Source0:        https://github.com/openSUSE/xinetd/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        README.SUSE
Source2:        logrotate
Source3:        sysconfig.xinetd
# PATCH-FIX-SUSE: use sysconfig service to generate the content
Patch0:         xinetd-service-sysconfig.patch
BuildRequires:  pkgconfig
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libtirpc)
Requires(post): %fillup_prereq
Provides:       inet-daemon
%{?systemd_requires}

%description
xinetd takes the abilities of inetd and appends additional
functionality:
- Access Control
- Prevention of 'denial of access' attacks
- Extensive logging abilities
- Clear configuration file

%prep
%setup -q
%patch0 -p1

# README.SUSE and logrotate
cp %{SOURCE1} %{SOURCE2} .

%build
%configure \
    --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install

#xinetd.service
install -D -m 0644 contrib/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
ln -sf service %{buildroot}%{_sbindir}/rc%{name}

# sysconfig
install -d -m 755 %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE3} %{buildroot}%{_fillupdir}

%pre
%service_add_pre %{name}.service

%post
%{fillup_only -n xinetd}
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md CHANGELOG COPYRIGHT README.SUSE logrotate
%{_mandir}/man5/*
%{_mandir}/man8/*
%dir %{_sysconfdir}/xinetd.d
%config(noreplace) %{_sysconfdir}/xinetd.d/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sbindir}/xinetd
%{_sbindir}/rcxinetd
%{_bindir}/*
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.xinetd

%changelog
