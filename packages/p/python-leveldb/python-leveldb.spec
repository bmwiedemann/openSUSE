#
# spec file for package python-leveldb
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
Name:           python-leveldb
Version:        0.201
Release:        0
Summary:        Python bindings for leveldb database library
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://code.google.com/p/py-leveldb/
Source:         https://files.pythonhosted.org/packages/source/l/leveldb/leveldb-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python bindings for leveldb database library.

%prep
%setup -q -n leveldb-%{version}
chmod -x README

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest_arch test/test.py

%files %{python_files}
%doc README
%{python_sitearch}/*

%changelog
