#
# spec file for package sca-patterns-sle15
#
# Copyright (c) 2021 SUSE LLC
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


%define sca_common sca
%define patdirbase /usr/lib/%{sca_common}
%define patdir %{patdirbase}/patterns
%define patuser root
%define patgrp root
%define mode 544
%define category SLE

Name:           sca-patterns-sle15
Version:        1.0.3
Release:        0
Summary:        Supportconfig Analysis Patterns for SLE15
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://github.com/g23guy/sca-patterns-sle15
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fdupes
Requires:       sca-patterns-base
BuildArch:      noarch

%description
Supportconfig Analysis (SCA) appliance patterns to identify known
issues relating to all versions of SLE15. 

See %{_docdir}/sca-patterns-base/COPYING.GPLv2

%prep
%setup -q

%build

%install
pwd;ls -la
install -d %{buildroot}/%{patdir}/%{category}
install -d %{buildroot}/%{patdir}/%{category}/sle15all
install -d %{buildroot}/%{patdir}/%{category}/sle15sp0
install -d %{buildroot}/%{patdir}/%{category}/sle15sp1
install -d %{buildroot}/%{patdir}/%{category}/sle15sp2
install -d %{buildroot}/%{patdir}/%{category}/sle15sp3
install -d %{buildroot}/%{patdir}/%{category}/sle15sp4
install -m %{mode} patterns/%{category}/sle15all/* %{buildroot}/%{patdir}/%{category}/sle15all
install -m %{mode} patterns/%{category}/sle15sp0/* %{buildroot}/%{patdir}/%{category}/sle15sp0
install -m %{mode} patterns/%{category}/sle15sp1/* %{buildroot}/%{patdir}/%{category}/sle15sp1
install -m %{mode} patterns/%{category}/sle15sp2/* %{buildroot}/%{patdir}/%{category}/sle15sp2
install -m %{mode} patterns/%{category}/sle15sp3/* %{buildroot}/%{patdir}/%{category}/sle15sp3
install -m %{mode} patterns/%{category}/sle15sp4/* %{buildroot}/%{patdir}/%{category}/sle15sp4
%fdupes %{buildroot}

%files
%defattr(-,%{patuser},%{patgrp})
%dir %{patdirbase}
%dir %{patdir}
%dir %{patdir}/%{category}
%dir %{patdir}/%{category}/sle15all
%dir %{patdir}/%{category}/sle15sp0
%dir %{patdir}/%{category}/sle15sp1
%dir %{patdir}/%{category}/sle15sp2
%dir %{patdir}/%{category}/sle15sp3
%dir %{patdir}/%{category}/sle15sp4
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle15all/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle15sp0/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle15sp1/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle15sp2/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle15sp3/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle15sp4/*
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/sle15sp4/README

%changelog
