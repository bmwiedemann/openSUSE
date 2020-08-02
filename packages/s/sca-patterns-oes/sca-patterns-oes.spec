# 
# spec file for package sca-patterns-oes
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define mode 544
%define category OES

Name:         sca-patterns-oes
Version:      1.3
Release:      0
Summary:      Supportconfig Analysis Patterns for OES
License:      GPL-2.0
URL:          https://github.com/g23guy/sca-patterns-oes
Group:        System/Monitoring
Source:       %{name}-%{version}.tar.gz
BuildRequires: fdupes
Requires:     sca-patterns-base
Buildarch:    noarch

%description
Supportconfig Analysis (SCA) appliance patterns to identify known
issues relating to all versions of Open Enterprise Server (OES)

See %{_docdir}/sca-patterns-base/COPYING.GPLv2

%prep
%setup -q

%build

%install
pwd;ls -la
install -d %{buildroot}/%{patdir}/%{category}
install -d %{buildroot}/%{patdir}/%{category}/oes11all
install -d %{buildroot}/%{patdir}/%{category}/oes11sp1
install -d %{buildroot}/%{patdir}/%{category}/oes11sp2
install -d %{buildroot}/%{patdir}/%{category}/oes1all
install -d %{buildroot}/%{patdir}/%{category}/oes2all
install -d %{buildroot}/%{patdir}/%{category}/oes2sp3
install -m %{mode} patterns/%{category}/oes11all/* %{buildroot}/%{patdir}/%{category}/oes11all
install -m %{mode} patterns/%{category}/oes11sp1/* %{buildroot}/%{patdir}/%{category}/oes11sp1
install -m %{mode} patterns/%{category}/oes11sp2/* %{buildroot}/%{patdir}/%{category}/oes11sp2
install -m %{mode} patterns/%{category}/oes1all/* %{buildroot}/%{patdir}/%{category}/oes1all
install -m %{mode} patterns/%{category}/oes2all/* %{buildroot}/%{patdir}/%{category}/oes2all
install -m %{mode} patterns/%{category}/oes2sp3/* %{buildroot}/%{patdir}/%{category}/oes2sp3
%fdupes %{buildroot}

%files
%defattr(-,%{patuser},%{patgrp})
%dir %{patdirbase}
%dir %{patdir}
%dir %{patdir}/%{category}
%dir %{patdir}/%{category}/oes11all
%dir %{patdir}/%{category}/oes11sp1
%dir %{patdir}/%{category}/oes11sp2
%dir %{patdir}/%{category}/oes1all
%dir %{patdir}/%{category}/oes2all
%dir %{patdir}/%{category}/oes2sp3
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/oes11all/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/oes11sp1/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/oes11sp2/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/oes1all/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/oes2all/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/oes2sp3/*

%changelog

