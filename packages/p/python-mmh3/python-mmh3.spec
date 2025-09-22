#
# spec file for package python-mmh3
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-mmh3
Version:        5.2.0
Release:        0
Summary:        Python extension for MurmurHash (MurmurHash3)
License:        MIT
URL:            https://github.com/hajimes/mmh3
Source:         https://github.com/hajimes/mmh3/archive/refs/tags/v%{version}.tar.gz#/mmh3-%{version}.tar.gz
Group:          Development/Languages/Python
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module mypy >= 1.0}
BuildRequires:  %{python_module pytest >= 7.0.0}
BuildRequires:  gcc-c++
# /SECTION
BuildRequires:  fdupes

%python_subpackages

%description
Python extension for MurmurHash (MurmurHash3), a set of fast and robust hash functions.

%prep
%autosetup -p1 -n mmh3-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm -f %{buildroot}%{$python_sitearch}/mmh3-4.1.0.dist-info/REQUESTED
%python_expand rm -f %{buildroot}%{$python_sitearch}/mmh3/{murmurhash3.h,murmurhash3.c,mmh3module.c,hashlib.h,py.typed}

%check
%python_expand export PYTHONPATH=$PYTHONPATH:%{buildroot}%{$python_sitearch}
%pytest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/mmh3.cpython*
%{python_sitearch}/mmh3
%{python_sitearch}/mmh3-%{version}.dist-info

%changelog
