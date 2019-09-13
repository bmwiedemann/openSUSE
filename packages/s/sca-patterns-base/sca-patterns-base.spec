# 
# spec file for package sca-patterns-base
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
%define patdirbase %{_prefix}/lib/%{sca_common}
%define patdir %{patdirbase}/patterns
%define prodgrp sdp
%define patuser root
%define patgrp root

Name:         sca-patterns-base
Version:      1.3
Release:      0
Summary:      Supportconfig Analysis Pattern Base Libraries
License:      GPL-2.0
URL:          https://github.com/g23guy/sca-patterns-base
Group:        System/Monitoring
Source:       %{name}-%{version}.tar.gz
Requires:     python
Requires:     bash
Requires:     perl
BuildArch:    noarch

%description
Supportconfig Analysis (SCA) appliance pattern base libraries used 
by all patterns

%prep
%setup -q

%build

%install
pwd;ls -la
install -d %{buildroot}/%{patdirbase}/patterns/local
install -d %{buildroot}/%{patdirbase}/bash
install -d %{buildroot}/%{patdirbase}/python
install -d %{buildroot}/%{patdirbase}/perl/SDP
install -d %{buildroot}%{_docdir}/%{name}
install -m 444 libraries/COPYING.GPLv2 %{buildroot}%{_docdir}/%{name}
install -m 644 libraries/bash/* %{buildroot}/%{patdirbase}/bash
install -m 644 libraries/python/* %{buildroot}/%{patdirbase}/python
install -m 644 libraries/perl/SDP/* %{buildroot}/%{patdirbase}/perl/SDP

%files
%defattr(-,%{patuser},%{patgrp})
%dir %{patdirbase}
%dir %{patdir}
%dir %{patdir}/local
%dir %{patdirbase}/bash
%dir %{patdirbase}/python
%dir %{patdirbase}/perl
%dir %{patdirbase}/perl/SDP
%dir %attr(-,root,root) %{_docdir}/%{name}
%attr(-,%{patuser},%{patgrp}) %{patdirbase}/bash/*
%attr(-,%{patuser},%{patgrp}) %{patdirbase}/python/*
%attr(-,%{patuser},%{patgrp}) %{patdirbase}/perl/SDP/*
%doc %attr(-,root,root) %{_docdir}/%{name}/*

%changelog

