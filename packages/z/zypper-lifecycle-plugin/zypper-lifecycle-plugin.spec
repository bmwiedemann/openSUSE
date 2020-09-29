#
# spec file for package zypper-lifecycle-plugin
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           zypper-lifecycle-plugin
Url:            https://github.com/SUSE/zypper-lifecycle
Version:        0.6.1601367426.843fe7a
Release:        0
Requires:       zypper >= 1.13.10
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  zypper >= 1.13.10
%if 0%{?suse_version} >= 1210
BuildRequires:  systemd-rpm-macros
%endif
%{?systemd_requires}

Source:         zypper-lifecycle-%{version}.tar.xz
Summary:        Zypper subcommand for lifecycle information
License:        GPL-2.0
Group:          System/Packages
BuildArch:      noarch
Supplements:    zypper

%description
Zypper subcommand for products and packages lifecycle information.

%prep
%setup -q -n zypper-lifecycle-%{version}

%build

%install
mkdir -p %{buildroot}/usr/lib/zypper/commands %{buildroot}/%{_mandir}/man8
install -m 755 zypper-lifecycle %{buildroot}/usr/lib/zypper/commands/
install -m 644 zypper-lifecycle.8 %{buildroot}/%{_mandir}/man8/
mkdir -p %{buildroot}/var/lib/lifecycle
mkdir -p %{buildroot}/usr/share/lifecycle
install -m 755 lifecycle-report %{buildroot}/usr/share/lifecycle/
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 644 lifecycle-report.service %{buildroot}%{_unitdir}
install -m 644 lifecycle-report.timer %{buildroot}%{_unitdir}
install -D -m 644 sysconfig.lifecycle-report %{buildroot}%{_fillupdir}/sysconfig.lifecycle-report

%pre
%service_add_pre lifecycle-report.service lifecycle-report.timer

%post
%{fillup_only -n lifecycle-report}
%service_add_post lifecycle-report.service lifecycle-report.timer

%preun
%service_del_preun lifecycle-report.service lifecycle-report.timer

%postun
%service_del_postun lifecycle-report.service lifecycle-report.timer

%files
%defattr(-,root,root,-)
/usr/lib/zypper/commands
/usr/share/lifecycle
/var/lib/lifecycle
%{_mandir}/man8/*
%{_unitdir}/*
%{_fillupdir}/*

%changelog
