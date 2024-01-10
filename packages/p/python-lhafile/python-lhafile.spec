#
# spec file for package python-lhafile
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-lhafile
Version:        0.3.0
Release:        0
Summary:        LHA archive support for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/FrodeSolheim/python-lhafile/
Source:         https://files.pythonhosted.org/packages/source/l/lhafile/lhafile-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Lhafile is a python C extension to extract lha files (.lzh).
The interface is similar to the zipfile module in the regular
Python distribution.

%prep
%setup -q -n lhafile-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license COPYING.txt
%doc README.md
%{python_sitearch}/lhafile
%{python_sitearch}/lzhlib.*
%{python_sitearch}/lhafile-%{version}.dist-info

%changelog
