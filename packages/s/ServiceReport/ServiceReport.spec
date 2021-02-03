#
# spec file for package ServiceReport
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


%define libversion %(echo %{version} | sed -e "s/+git.*//")

# By default python 3 is used to build the package.
%define python python3
Name:           ServiceReport
Version:        2.2.2+git10.1caca0630e36
Release:        0
Summary:        A tool to validate and repair First Failure Data Capture (FFDC) configuration
License:        GPL-2.0-only
Group:          System/Management
URL:            https://github.com/linux-ras/ServiceReport
Source:         %{name}-%{version}.tar.xz
BuildRequires:  %{python}
BuildRequires:  %{python}-setuptools
BuildRequires:  systemd-rpm-macros
%systemd_requires
BuildArch:      noarch

%description
ServiceReport is a python based tool that investigates the incorrect
First Failure Data Capture (FFDC) configuration and optionally repairs
the incorrect configuration

%define debug_package %{nil}

%prep
%setup -q
%autopatch -p1

%build
%{python} setup.py build

%install
%{python} setup.py install --root=%{buildroot}

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
%{_mandir}/man8/*
%doc %{_datadir}/doc/*
%{_bindir}/servicereport
%{_unitdir}/servicereport.service

%if "%{python}" == "python3"
%{python3_sitelib}/servicereportpkg
%{python3_sitelib}/%{name}-%{libversion}*.egg-info
%else
%{python_sitelib}/servicereportpkg
%{python_sitelib}/%{name}-%{libversion}*.egg-info
%endif

%changelog
