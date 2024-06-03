#
# spec file for package python-PyKCS11
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


%{?sle15_python_module_pythons}
Name:           python-PyKCS11
Version:        1.5.16
Release:        0
Summary:        A Full PKCS#11 wrapper for Python
License:        GPL-2.0-or-later
URL:            https://github.com/LudovicRousseau/PyKCS11
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module asn1crypto}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  softhsm-devel
BuildRequires:  swig
%python_subpackages

%description
A Full PKCS#11 wrapper for Python

%prep
%autosetup -n PyKCS11-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export $(python3 get_PYKCS11LIB.py)
# Unfortunately the test suite is irrecovabily broken
# gh#LudovicRousseau/PyKCS11#115
# %%pyunittest_arch discover -v test

%files %{python_files}
%doc Changes.txt README.md
%license COPYING
%{python_sitearch}/PyKCS11
%{python_sitearch}/PyKCS11-%{version}*-info

%changelog
