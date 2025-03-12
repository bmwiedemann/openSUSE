#
# spec file for package sshguard
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%define has_systemd 1
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
Name:           sshguard
Version:        2.4.3
Release:        0
Summary:        SSH brute force attack protector
License:        ISC
Group:          Productivity/Networking/Security
URL:            https://www.sshguard.net/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        sshguard.conf
Source2:        sshguard.service
Source3:        sshguard.init
Source4:        sshguard.whitelist
# PATCH-FIX-UPSTREAM sshguard-gcc5.patch
Patch0:         sshguard-gcc5.patch
Patch1:         harden_sshguard.service.patch
# build with gcc15 (https://bitbucket.org/sshguard/sshguard/issues/189/fail-with-gcc15)
Patch2:         sshguard-gcc15.patch
Requires:       openssh
BuildRequires:  bison
Requires(pre):  %fillup_prereq

%description
Sshguard protects networked hosts from brute force attacks
against ssh servers. It detects such attacks and blocks the
attacker's address with a firewall rule.

%prep
%autosetup -p1

%build
%configure \
  --with-firewall=iptables \
  --with-iptables=%{_sbindir}/iptables
%make_build

%install
%make_install
install -D -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}.conf
sed -i "s|BACKEND=.*$|BACKEND=\"%{_libexecdir}/sshg-fw-firewalld\"|g" %{buildroot}%{_sysconfdir}/%{name}.conf
ln -sf service %{buildroot}/%{_sbindir}/rc%{name}
install -D -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/sshguard.service
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -D -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/whitelist
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}/db
%fillup_and_insserv

%pre
%service_add_pre %{name}.service

%post
%fillup_only sshguard
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%if 0%{?suse_version} < 1330
%license COPYING
%doc CHANGELOG.rst README.rst examples/ doc/
%else
%doc CHANGELOG.rst README.rst examples/ doc/
%license COPYING
%endif
%{_sbindir}/*
%{_mandir}/man8/%{name}*
%{_mandir}/man7/%{name}-setup*
%if 0%{?has_systemd}
%{_unitdir}/sshguard.service
%else
%config %{_sysconfdir}/init.d/sshguard
%endif
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/whitelist
%dir %{_localstatedir}/lib/%{name}
%attr(755,root,root) %{_localstatedir}/lib/%{name}/db
%{_libexecdir}/sshg-*

%changelog
