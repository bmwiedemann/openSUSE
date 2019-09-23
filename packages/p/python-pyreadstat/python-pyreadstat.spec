#
# spec file for package python-pyreadstat
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pyreadstat
Version:        0.2.9
Release:        0
Summary:        Package to read and write statistical data files into pandas
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Roche/pyreadstat
Source:         https://codeload.github.com/Roche/pyreadstat/tar.gz/v%{version}#/pyreadstat-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  glibc-devel
BuildRequires:  python-rpm-macros
BuildRequires:  zlib-devel
Requires:       python-numpy
Requires:       python-pandas
# SECTION test requirements
BuildRequires:  %{python_module pandas}
# /SECTION
%python_subpackages

%description
Reads and Writes SAS, SPSS and Stata files into pandas data frames.

%prep
%setup -q -n pyreadstat-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
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
%{python_sitearch}/*

%changelog
