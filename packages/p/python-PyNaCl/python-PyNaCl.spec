#
# spec file for package python-PyNaCl
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
Name:           python-PyNaCl
Version:        1.3.0
Release:        0
Summary:        Python binding to the Networking and Cryptography (NaCl) library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pyca/pynacl/
Source:         https://pypi.org/packages/source/P/PyNaCl/PyNaCl-%{version}.tar.gz
# https://github.com/pyca/pynacl/commit/a8c08b18f3a2e8f2140c531afaf42715fcab68e7
Patch0:         python-PyNaCl-hypothesis-remove-average_size.patch
Patch1:         fix_tests.patch
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pycparser}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libsodium)
Requires:       python-cffi
Requires:       python-six
# SECTION test requirements
BuildRequires:  %{python_module hypothesis >= 3.27.0}
BuildRequires:  %{python_module pytest >= 3.2.1}
# /SECTION
%python_subpackages

%description
PyNaCl is a Python binding to the `Networking and Cryptography library`_,
a crypto library with the stated goal of improving usability, security and
speed.

%prep
%setup -q -n PyNaCl-%{version}
%autopatch -p1
rm -Rf src/libsodium

%build
export SODIUM_INSTALL="system"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}/%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
