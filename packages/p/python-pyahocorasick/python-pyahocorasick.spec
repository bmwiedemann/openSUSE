#
# spec file for package python-pyahocorasick
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyahocorasick
Version:        1.4.4
Release:        0
Summary:        Library for exact or approximate multi-pattern string search
License:        BSD-3-Clause
URL:            https://github.com/WojciechMula/pyahocorasick
Source:         https://files.pythonhosted.org/packages/source/p/pyahocorasick/pyahocorasick-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
skip_tests=""
# gh#WojciechMula/pyahocorasick#142
%ifarch ppc64 s390x armv7l
skip_tests+="not (test_iter2 or test_iter3)"
%endif
%pytest_arch -k "${skip_tests}" unittests.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
