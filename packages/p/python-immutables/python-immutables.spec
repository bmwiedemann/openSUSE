#
# spec file for package python-immutables
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
%define skip_python2 1
Name:           python-immutables
Version:        0.14
Release:        0
Summary:        Immutable collections for Python
License:        Apache-2.0
URL:            https://github.com/MagicStack/immutables
Source:         https://files.pythonhosted.org/packages/source/i/immutables/immutables-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip_32bit_tests.patch gh#MagicStack/immutables#53 mcepl@suse.com
# skip failing tests on 32bit architectures
Patch0:         skip_32bit_tests.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Immutable collections for Python.

%prep
%autosetup -p1 -n immutables-%{version}

sed -i 's/\.system//' setup.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%{python_expand rm %{buildroot}%{$python_sitearch}/immutables/*.[ch]
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
