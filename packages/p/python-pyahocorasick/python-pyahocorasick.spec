#
# spec file for package python-pyahocorasick
#
# Copyright (c) 2025 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-pyahocorasick%{?psuffix}
Version:        2.1.0
Release:        0
Summary:        Library for exact or approximate multi-pattern string search
License:        BSD-3-Clause
URL:            https://github.com/WojciechMula/pyahocorasick
Source:         https://files.pythonhosted.org/packages/source/p/pyahocorasick/pyahocorasick-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
%if %{with test}
BuildRequires:  %{python_module pyahocorasick = %{version}}
%endif
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
ExclusiveArch:  aarch64 loongarch64 ppc64 ppc64le riscv64 s390x x86_64
%python_subpackages

%description
pyahocorasick is a library for exact or approximate
multi-pattern string search, meaning that one can find
multiple key strings occurrences at once in some input text.  The
library provides an `ahocorasick` Python module that you can use as
a plain dict-like Trie or convert a Trie to an automaton for efficient
Aho-Corasick search.

It is implemented in C.

%prep
%autosetup -p1 -n pyahocorasick-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/ahocorasick*.so
%{python_sitearch}/pyahocorasick-%{version}.dist-info

%endif

%changelog
