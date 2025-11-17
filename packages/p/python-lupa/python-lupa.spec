#
# spec file for package python-lupa
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
Name:           python-lupa
Version:        2.6
Release:        0
Summary:        Python wrapper around Lua and LuaJIT
License:        MIT
URL:            https://github.com/scoder/lupa
Source:         https://files.pythonhosted.org/packages/source/l/lupa/lupa-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(lua)
Suggests:       lua
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
Recommends:     luajit
# Synchronized with archs where luajit is build
%ifnarch ppc64 ppc64le s390x
BuildRequires:  pkgconfig(luajit)
%endif
# /suse_version
%endif
%python_subpackages

%description
Python wrapper around Lua and LuaJIT.

%prep
%autosetup -p1 -n lupa-%{version}

rm -rf third-party/

%build
export CFLAGS="-fno-strict-aliasing %{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv lupa/tests .
mv lupa lupa.hide
sed -i 's/lupa.tests/tests/g' tests/test.py
%pyunittest_arch discover -v

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitearch}/lupa
%{python_sitearch}/lupa-%{version}*-info

%changelog
