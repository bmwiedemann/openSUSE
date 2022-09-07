#
# spec file for package python-google-crc32c
#
# Copyright (c) 2022 SUSE LLC
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
%define modname google-crc32c
Name:           python-google-crc32c
Version:        1.5.0
Release:        0
Summary:        A python wrapper of the C library 'Google CRC32C'
License:        Apache-2.0
URL:            https://github.com/googleapis/python-crc32c
Source:         https://github.com/googleapis/python-crc32c/archive/refs/tags/v%{version}.tar.gz#/google-crc32c-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libcrc32c-devel
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A python wrapper of the C library 'Google CRC32C'.

%prep
%autosetup -p1 -n python-crc32c-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/google_crc32c*/

%changelog
