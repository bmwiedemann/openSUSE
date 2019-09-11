#
# spec file for package python-ctypesgen
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/
%define modname ctypesgen
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{modname}
Version:        0.1.1
Release:        0
Summary:        Pure Python Wrapper Generator for ctypes
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/olsonse/ctypesgen
Source:         https://github.com/olsonse/ctypesgen/archive/ctypesgen-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%ifpython2
Obsoletes:      %{modname} < %{version}
Provides:       %{modname} = %{version}
%endif
%python_subpackages

%description
This project automatically generates ctypes wrappers for header files written in C.

%prep
%autosetup -n %{modname}-%{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd test
export PYTHONDONTWRITEBYTECODE=1
%python_exec testsuite.py
popd

%files %{python_files}
%license LICENSE
%doc README todo.txt demo/*.{c,h,py}
%python3_only %{_bindir}/%{modname}
%{python_sitelib}/ctypesgen*

%changelog
