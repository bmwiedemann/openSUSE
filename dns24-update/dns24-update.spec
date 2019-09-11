#
# spec file for package dns24-update
#
# Copyright (c) specCURRENT_YEAR SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dns24-update
Version:        1.0
Release:        0
Summary:        Simple update client for the dns24.ch DynDNS service
License:        GPL-3.0-or-later
Group:          Productivity/Networking/DNS/Utilities
Url:            https://www.dns24.ch/
Source0:        dns24@.service
Source1:        dns24@.timer
Source20:       README.md
Source10:       template.curl
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A simple utility for regularly updating one or more dynamic DNS records on the
dns24.ch service.

%prep

%build
cp %{SOURCE20} .

%install
mkdir -p %{buildroot}%{_unitdir}
cp %{SOURCE0} %{SOURCE1} %{buildroot}%{_unitdir}

mkdir -p %{buildroot}/etc/dns24/
cp %{SOURCE10} %{buildroot}/etc/dns24/

%pre
%service_add_pre dns24@.service

%post
%service_add_post dns24@.service

%preun
%service_del_preun dns24@.service

%postun
%service_del_postun dns24@.service

%files
%defattr(-,root,root)
%{_unitdir}/dns24@.*
%dir %attr(0750,-,-) /etc/dns24
%config(noreplace) /etc/dns24/template.curl
%doc README.md

%changelog
