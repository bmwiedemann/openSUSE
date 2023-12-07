 
# spec file for package sca-patterns-alp1
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%define sca_common sca
%define patdirbase /usr/lib/%{sca_common}
%define patdir %{patdirbase}/patterns
%define patuser root
%define patgrp root
%define patmode 755
%define category ALP

Name:         sca-patterns-alp1
Version:      2.0.0
Release:      0
Summary:      Supportconfig Analysis Patterns for ALP1
License:      GPL-2.0
URL:          https://github.com/g23guy/sca-patterns-alp1
Group:        System/Monitoring
Source:       %{name}-%{version}.tar.gz
Requires:     sca-patterns-template-gen2
Buildarch:    noarch
BuildRequires: fdupes

%description
Supportconfig Analysis (SCA) appliance patterns to identify known
issues relating to all versions of SUSE Adaptable Linux Platform (ALP) 1.

See %{_docdir}/sca-patterns-base/COPYING.GPLv2

%prep
%setup -q

%build

%install
pwd;ls -la
install -d %{buildroot}/%{patdir}/%{category}
install -d %{buildroot}/%{patdir}/%{category}/alp1all
install -d %{buildroot}/%{patdir}/%{category}/alp1sp0
install -m %{patmode} patterns/%{category}/alp1all/* %{buildroot}/%{patdir}/%{category}/alp1all
install -m %{patmode} patterns/%{category}/alp1sp0/* %{buildroot}/%{patdir}/%{category}/alp1sp0
%fdupes %{buildroot}

%files
%defattr(-,%{patuser},%{patgrp})
%dir %{patdirbase}
%dir %{patdir}
%dir %{patdir}/%{category}
%dir %{patdir}/%{category}/alp1all
%dir %{patdir}/%{category}/alp1sp0
%attr(%{patmode},%{patuser},%{patgrp}) %{patdir}/%{category}/alp1all/*
%attr(%{patmode},%{patuser},%{patgrp}) %{patdir}/%{category}/alp1sp0/*

%changelog

