#
# spec file for package ServiceReport
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define libversion %(echo %{version} | sed -e 's/\+git.*$//')

# By default python 3 is used to build the package.
%define python python3
Name:           ServiceReport
Version:        2.2.4+git4.cdcbdfa
Release:        0
Summary:        A tool to validate and repair First Failure Data Capture (FFDC) configuration
License:        GPL-2.0-only
Group:          System/Management
URL:            https://github.com/linux-ras/ServiceReport
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM fix_setup.patch gh#linux-ras/ServiceReport!32 mcepl@suse.com
# Don't install data files and modernize Python package setup
Patch0:         fix_setup.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  systemd-rpm-macros
BuildArch:      noarch
%systemd_requires

%description
ServiceReport is a python based tool that investigates the incorrect
First Failure Data Capture (FFDC) configuration and optionally repairs
the incorrect configuration

%define debug_package %{nil}

%prep
%autosetup -p1

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
install -D -m 644 man/servicereport.8 \
    %{buildroot}%{_mandir}/man8/servicereport.8
install -D -m 644 service/servicereport.service \
    %{buildroot}%{_unitdir}/servicereport.service
%fdupes %{buildroot}%{python3_sitelib}

%pre
%service_add_pre servicereport.service

%post
%service_add_post servicereport.service

%preun
%service_del_preun servicereport.service

%postun
%service_del_postun servicereport.service

%files
%license COPYING
%doc README.md
%{_mandir}/man8/*
%{_bindir}/servicereport
%{_unitdir}/servicereport.service
%{python3_sitelib}/servicereportpkg
%{python3_sitelib}/[Ss]ervice[Rr]eport-%{libversion}*-info

%changelog
