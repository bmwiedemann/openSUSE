#
# spec file for package sshguard
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
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if 0%{?suse_version} > 1140
%define has_systemd 1
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%else
Requires(pre):  %fillup_prereq
%endif
Name:           sshguard
Version:        2.4.0
Release:        0
Summary:        SSH brute force attack protector
License:        ISC
Group:          Productivity/Networking/Security
URL:            http://www.sshguard.net
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        sshguard.conf
Source2:        sshguard.service
Source3:        sshguard.init
Source4:        sshguard.whitelist
# PATCH-FIX-UPSTREAM sshguard-gcc5.patch
Patch0:         sshguard-gcc5.patch
Requires:       openssh
Requires(pre):  %fillup_prereq

%description
Sshguard protects networked hosts from brute force attacks
against ssh servers. It detects such attacks and blocks the
attacker's address with a firewall rule.

%prep
%setup -q
%patch0 -p1
find . -type f -iname "*.swp" -print -exec rm {} \;

%build
%configure \
  --with-firewall=iptables \
  --with-iptables=%{_sbindir}/iptables
make %{?_smp_mflags}

%install
%make_install
install -D -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}.conf
%if 0%{?has_systemd}
ln -sf service %{buildroot}/%{_sbindir}/rc%{name}
install -D -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/sshguard.service
%else
install -D -m0744 %{SOURCE3} %{buildroot}%{_sysconfdir}/init.d/sshguard
ln -s ../..%{_sysconfdir}/init.d/sshguard %{buildroot}%{_sbindir}/rcsshguard
%endif
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -D -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/whitelist
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}/db
%fillup_and_insserv

%pre
%if 0%{?has_systemd}
%service_add_pre %{name}.service
%endif

%post
%if 0%{?has_systemd}
%fillup_only sshguard
%service_add_post %{name}.service
%else
%fillup_and_insserv %{name}
%endif

%preun
%if 0%{?has_systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif

%postun
%if 0%{?has_systemd}
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%insserv_cleanup
%endif

%files
%if 0%{?suse_version} < 1330
%doc CHANGELOG.rst README.rst examples/ doc/ COPYING
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
