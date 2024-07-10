#
# spec file for package python-HeapDict
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


Name:           python-HeapDict
Version:        1.0.1
Release:        0
Summary:        A heap with decrease-key and increase-key operations
License:        BSD-3-Clause
URL:            http://stutzbachenterprises.com/
Source:         https://files.pythonhosted.org/packages/source/H/HeapDict/HeapDict-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_main' test_heap.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/heapdict.py*
%pycache_only %{python_sitelib}/__pycache__/heapdict*
%{python_sitelib}/HeapDict-%{version}.dist-info

%changelog
