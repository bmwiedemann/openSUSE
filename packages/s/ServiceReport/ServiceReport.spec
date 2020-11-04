#
# spec file for package ServiceReport
#
# Copyright (c) 2020 SUSE LLC
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


# By default python 3 is used to build the package.
%define python python3
Name:           ServiceReport
Version:        2.2.2
Release:        0
Summary:        A tool to validate and repair First Failure Data Capture (FFDC) configuration
License:        GPL-2.0-only
Group:          System/Management
URL:            https://github.com/linux-ras/ServiceReport
Source0:        https://github.com/linux-ras/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch1:         0001-Add-active-dump-check-in-kdump-and-FADump-plugin.patch
Patch2:         0002-Introduce-a-new-option-to-mark-plugins-optional.patch
Patch3:         0003-HTX-Mark-HTX-plugin-as-optional.patch
Patch4:         0004-Add-new-option-to-run-all-applicable-plugins.patch
Patch5:         0005-Allow-distro-classes-to-redefine-the-capture-kernel-.patch
Patch6:         0006-utils-remove-the-invalid-function-call-to-walk_packa.patch
Patch7:         0007-Update-data-files-of-the-project.patch
Patch8:         0008-Run-servicereport-using-python3-binary.patch
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
%{python3_sitelib}/%{name}-%{version}*.egg-info
%else
%{python_sitelib}/servicereportpkg
%{python_sitelib}/%{name}-%{version}*.egg-info
%endif

%changelog
