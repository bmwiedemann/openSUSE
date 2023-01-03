#
# spec file for package python-bitarray
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-bitarray
Version:        2.6.2
Release:        0
Summary:        Efficient Arrays of Booleans
License:        Python-2.0
URL:            https://github.com/ilanschnell/bitarray
Source:         https://github.com/ilanschnell/bitarray/archive/%{version}.tar.gz#/bitarray-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This module provides an object type which efficiently represents an
array of booleans.  Bitarrays are sequence types and behave very
much like usual lists. Eight bits are represented by one byte in a
contiguous block of memory. The user can select between two
representations; little-endian and big-endian.
All of the functionality is implemented in C. Methods for accessing
the machine representation are provided.  This can be useful when
bit level access to binary files is required, such as portable
bitmap image files (.pbm).
Also, when dealing with compressed data which uses variable bit
length encoding, you may find this module useful.

%prep
%setup -q -n bitarray-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
rm examples/growth/.gitignore

%check
# tests don't run from within the source directory
%python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}; cd /tmp/; $python -c 'import bitarray; bitarray.test()'

%files %{python_files}
%license LICENSE
%doc examples CHANGE_LOG README.rst
%{python_sitearch}/bitarray*

%changelog
