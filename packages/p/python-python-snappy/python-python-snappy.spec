#
# spec file for package python-python-snappy
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
Name:           python-python-snappy
Version:        0.5.4
Release:        0
Summary:        Python library for the snappy compression library
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/andrix/python-snappy
Source:         https://files.pythonhosted.org/packages/source/p/python-snappy/python-snappy-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  snappy-devel
%python_subpackages

%description
Python library for the snappy compression library from Google.

%prep
%setup -q -n python-snappy-%{version}
sed -i -e '/^#!\//, 1d' snappy/snappy.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mkdir tester
cp test_*.py tester/
pushd tester
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -B test_snappy.py
$python -B test_formats.py
$python -B test_hadoop_snappy.py
}
popd

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
