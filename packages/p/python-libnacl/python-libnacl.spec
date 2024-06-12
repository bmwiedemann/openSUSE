#
# spec file for package python-libnacl
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
Name:           python-libnacl
Version:        2.1.0
Release:        0
Summary:        Python bindings for libsodium based on ctypes
License:        Apache-2.0
URL:            https://github.com/saltstack/libnacl
Source0:        https://github.com/saltstack/libnacl/archive/v%{version}.tar.gz#/libnacl-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libsodium)
# This will need updating and verification but smart magic is not copied by
#  singlespec macros
Requires:       libsodium26
BuildArch:      noarch
%python_subpackages

%description
This library is used to gain direct access to the functions exposed by Daniel J. Bernstein's nacl library via libsodium.
It has been constructed to maintain extensive documentation on how to use nacl as well as being completely portable. The file
in libnacl/__init__.py can be pulled out and placed directly in any project to give a single file binding to all of nacl.

%prep
%autosetup -p1 -n libnacl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
%python_expand $python tests/runtests.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/libnacl
%{python_sitelib}/libnacl-%{version}.dist-info

%changelog
