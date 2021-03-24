#
# spec file for package python-wrapt
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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
Name:           python-wrapt
Version:        1.12.1
Release:        0
Summary:        A Python module for decorators, wrappers and monkey patching
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/GrahamDumpleton/wrapt
Source:         https://github.com/GrahamDumpleton/wrapt/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#GrahamDumpleton/wrapt#168 -- fix pytest 6 dummy collection
Patch0:         https://github.com/GrahamDumpleton/wrapt/pull/168.patch#/fix-dummy-collector-pytest6.patch
# PATCH-FIX-UPSTREAM gh#GrahamDumpleton/wrapt#161 -- fix test for Python 3.9
Patch1:         https://github.com/GrahamDumpleton/wrapt/pull/161.patch#/wrapt-pr161-py39tests.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
The aim of the **wrapt** module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

The **wrapt** module focuses very much on correctness. It therefore goes
way beyond existing mechanisms such as ``functools.wraps()`` to ensure that
decorators preserve introspectability, signatures, type checking abilities
etc. The decorators that can be constructed using this module will work in
far more scenarios than typical decorators and provide more predictable and
consistent behaviour.

To ensure that the overhead is as minimal as possible, a C extension module
is used for performance critical components. An automatic fallback to a
pure Python implementation is also provided where a target system does not
have a compiler to allow the C extension to be compiled.

Documentation
-------------

For further information on the **wrapt** module see:

* http://wrapt.readthedocs.org/

%prep
%autosetup -p1 -n wrapt-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.rst docs/changes.rst
%{python_sitearch}/wrapt
%{python_sitearch}/wrapt-%{version}*-info

%changelog
