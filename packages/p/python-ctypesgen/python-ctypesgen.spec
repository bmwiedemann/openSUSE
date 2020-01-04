#
# spec file for package python-ctypesgen
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/
%define modname ctypesgen
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{modname}
Version:        1.0.2
Release:        0
Summary:        Pure Python Wrapper Generator for ctypes
License:        BSD-3-Clause
URL:            https://github.com/davidjamesca/ctypesgen
Source:         https://github.com/davidjamesca/ctypesgen/archive/ctypesgen-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
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
%python_expand rm -r %{buildroot}%{$python_sitelib}/ctypesgen/test
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%pytest ctypesgen/test/testsuite.py

%files %{python_files}
%license LICENSE
%doc README.md todo.txt demo/*.{c,h,py}
%python3_only %{_bindir}/%{modname}
%{python_sitelib}/ctypesgen*

%changelog
