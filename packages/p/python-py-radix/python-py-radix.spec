#
# spec file for package python-py-radix
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
Name:           python-py-radix
Version:        0.10.0
Release:        0
Summary:        Radix tree implementation
License:        BSD-4-Clause AND ISC
Group:          Development/Languages/Python
URL:            https://github.com/mjschultz/py-radix
Source:         https://files.pythonhosted.org/packages/source/p/py-radix/py-radix-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - Change incompatible pointer type from RadixNodeObject to PyObject
Patch:          https://github.com/mjschultz/py-radix/pull/58.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Implements the radix tree data structure for the storage and
retrieval of IPv4 and IPv6 network prefixes.

The radix tree is commonly used for routing table lookups. It efficiently
stores network prefixes of varying lengths and allows fast lookups of
containing networks.

This package includes the C-extension.

%prep
%setup -q -n py-radix-%{version}
%patch -P0 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
