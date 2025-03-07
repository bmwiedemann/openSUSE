#
# spec file for package python-pyreadstat
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-pyreadstat
Version:        1.2.7
Release:        0
Summary:        Package to read and write statistical data files into pandas
License:        Apache-2.0
URL:            https://github.com/Roche/pyreadstat
Source:         https://github.com/Roche/pyreadstat/archive/v%{version}.tar.gz#/pyreadstat-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#Roche/pyreadstat#266
Patch0:         support-numpy-2.patch
BuildRequires:  %{python_module Cython >= 3}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pandas >= 0.24.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  glibc-devel
BuildRequires:  python-rpm-macros
BuildRequires:  zlib-devel
Requires:       python-numpy
Requires:       python-pandas >= 0.24.0
%python_subpackages

%description
Reads and Writes SAS, SPSS and Stata files into pandas data frames.

%prep
%autosetup -p1 -n pyreadstat-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv pyreadstat pyreadstat_temp
rm -rf build _build.*
export PYTHONDONTWRITEBYTECODE=1
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
rm -rf build _build.*
$python -B tests/test_basic.py
}
mv pyreadstat_temp pyreadstat

%files %{python_files}
%doc README.md change_log.md
%license LICENSE
%{python_sitearch}/pyreadstat
%{python_sitearch}/pyreadstat-%{version}.dist-info

%changelog
