#
# spec file for package python-ntplib
#
# Copyright (c) 2025 SUSE LLC
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


%define upstream_name ntplib
Name:           python-%{upstream_name}
Version:        0.4.0
Release:        0
Summary:        Python NTP library
License:        MIT
Group:          Development/Libraries/Python
URL:            https://pypi.python.org/pypi/ntplib
Source0:        ntplib-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module offers a simple interface to query NTP servers from Python.
It also provides utility functions to translate NTP fields values to text
(mode, leap indicator...). Since it's pure Python, and only depends on core
modules, it should work on any platform with a decent Python implementation.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%doc CHANGELOG
%{python_sitelib}/ntplib.py
%{python_sitelib}/ntplib-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/ntplib*

%changelog
