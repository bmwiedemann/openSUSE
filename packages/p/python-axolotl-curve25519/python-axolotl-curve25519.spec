#
# spec file for package python-axolotl-curve25519
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
%define _version 0.4.1.post2
Name:           python-axolotl-curve25519
Version:        0.4.1.2
Release:        0
Summary:        A curve25519 Python wrapper with Ed25519 signatures
License:        BSD-3-Clause AND GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/tgalal/python-axolotl-curve25519
Source:         https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{_version}.tar.gz
Source1:        https://raw.githubusercontent.com/tgalal/python-axolotl-curve25519/master/LICENSE
# PATCH-FIX-UPSTREAM - Correct types in PyModuleDef / fix compilation with clang
Patch:          https://github.com/tgalal/python-axolotl-curve25519/pull/26.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This is a Python wrapper for the curve25519 library with Ed25519
signatures.

%prep
%setup -q -n %{name}-%{_version}
%patch -P0 -p1
cp -a %{SOURCE1} .

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%{python_sitearch}/*

%changelog
