#
# spec file for package python-libnacl
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
Name:           python-libnacl
Version:        1.6.1
Release:        0
Summary:        Python bindings for libsodium based on ctypes
License:        Apache-2.0
URL:            https://github.com/saltstack/libnacl
Source0:        https://github.com/saltstack/libnacl/archive/v%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libsodium)
# This will need updating and verification but smart magic is not copied by
#  singlespec macros
Requires:       libsodium23
%python_subpackages

%description
This library is used to gain direct access to the functions exposed by Daniel J. Bernstein's nacl library via libsodium.
It has been constructed to maintain extensive documentation on how to use nacl as well as being completely portable. The file
in libnacl/__init__.py can be pulled out and placed directly in any project to give a single file binding to all of nacl.

%prep
%setup -q -n libnacl-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
%python_expand $python tests/runtests.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
