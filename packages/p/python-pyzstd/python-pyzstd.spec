#
# spec file for package python-pyzstd
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


%define skip_python2 1
Name:           python-pyzstd
Version:        0.15.3
Release:        0
Summary:        Python bindings to Zstandard (zstd) compression library
License:        BSD-3-Clause
URL:            https://github.com/animalize/pyzstd
Source:         https://files.pythonhosted.org/packages/source/p/pyzstd/pyzstd-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libzstd-devel >= 1.4.0
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Pyzstd module provides classes and functions for compressing and decompressing data,
using Facebook's Zstandard (or zstd as short name) algorithm.

The API is similar to Python's bz2/lzma/zlib modules.

%prep
%setup -q -n pyzstd-%{version}
# make sure we link dynamically, cannot use command line argument to pip wheel
# gh#animalize/pyzstd#18
rm -r zstd
sed -i "s/has_option('--dynamic-link-zstd')/True/" setup.py

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch discover -v tests

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pyzstd
%{python_sitearch}/pyzstd-%{version}.dist-info

%changelog
