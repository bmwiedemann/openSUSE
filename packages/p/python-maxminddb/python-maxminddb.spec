#
# spec file for package python-maxminddb
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
Name:           python-maxminddb
Version:        2.0.3
Release:        0
Summary:        Reader for the MaxMind DB format
License:        Apache-2.0
URL:            http://www.maxmind.com/
Source:         https://files.pythonhosted.org/packages/source/m/maxminddb/maxminddb-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libmaxminddb-devel
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python-ipaddress
%endif
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This is a Python module for reading MaxMind DB files. The module includes both
a pure Python reader and an optional C extension.

MaxMind DB is a binary file format that stores data indexed by IP address
subnets (IPv4 or IPv6).

%prep
%setup -q -n maxminddb-%{version}
sed -i '/nose/d' setup.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
