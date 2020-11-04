#
# spec file for package python-HeapDict
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
Name:           python-HeapDict
Version:        1.0.1
Release:        0
Summary:        A heap with decrease-key and increase-key operations
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://stutzbachenterprises.com/
Source:         https://files.pythonhosted.org/packages/source/H/HeapDict/HeapDict-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# These packages contain module test from stdlib,
# it has nothing to do with this package being noarch
BuildRequires:  python2-devel
BuildRequires:  python3-testsuite
BuildArch:      noarch
%python_subpackages

%description
HeapDict implements the MutableMapping ABC, meaning it works pretty
much like a regular Python dict.  It's designed to be used as a
priority queue.

Unlike the Python standard library's heapq module, the HeapDict
supports efficiently changing the priority of an existing object
(often called "decrease-key" in textbooks).  Altering the priority is
important for many algorithms such as Dijkstra's Algorithm and A*.

%prep
%setup -q -n HeapDict-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test_heap.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
