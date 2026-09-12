#
# spec file for package python-maxminddb
#
# Copyright (c) 2026 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-maxminddb
Version:        3.1.1
Release:        0
Summary:        Reader for the MaxMind DB format
License:        Apache-2.0
URL:            https://www.maxmind.com/
Source:         https://files.pythonhosted.org/packages/source/m/maxminddb/maxminddb-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77.0.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libmaxminddb)
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This is a Python module for reading MaxMind DB files. The module includes both
a pure Python reader and an optional C extension.

MaxMind DB is a binary file format that stores data indexed by IP address
subnets (IPv4 or IPv6).

%prep
%autosetup -n maxminddb-%{version}
# no bundled libmaxminddb, see MAXMINDDB_USE_SYSTEM_LIBMAXMINDDB below
rm -r extension/libmaxminddb

%build
export CFLAGS="%{optflags}"
export MAXMINDDB_USE_SYSTEM_LIBMAXMINDDB=1
# without this setup.py silently falls back to the pure Python reader
export MAXMINDDB_REQUIRE_EXTENSION=1
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# else the extension tests skip themselves when the .so is missing
export MM_FORCE_EXT_TESTS=1
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/maxminddb/
%{python_sitearch}/maxminddb-%{version}.dist-info

%changelog
