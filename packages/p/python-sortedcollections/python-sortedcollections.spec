#
# spec file for package python-sortedcollections
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
Name:           python-sortedcollections
Version:        1.1.2
Release:        0
Summary:        Python Sorted Collections
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/grantjenks/sortedcollections
#Source:         https://files.pythonhosted.org/packages/source/s/sortedcollections/sortedcollections-%%{version}.tar.gz
Source:         https://github.com/grantjenks/python-sortedcollections/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sortedcontainers >= 2}
# /SECTION
Requires:       python-sortedcontainers >= 2
BuildArch:      noarch

%python_subpackages

%description
SortedCollections is an Python sorted collections library.

Features
--------

- ValueSortedDict - Dictionary with (key, value) item pairs sorted by value.
- ItemSortedDict - Dictionary with key-function support for item pairs.
- OrderedDict - Ordered dictionary with numeric indexing support.
- OrderedSet - Ordered set with numeric indexing support.
- IndexableDict - Dictionary with numeric indexing support.
- IndexableSet - Set with numeric indexing support.
- SegmentList - List with fast random access insertion and deletion.

%prep
%setup -q -n python-sortedcollections-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
