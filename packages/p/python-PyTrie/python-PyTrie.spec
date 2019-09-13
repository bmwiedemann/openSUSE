#
# spec file for package python-PyTrie
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
Name:           python-PyTrie
Version:        0.3.1
Release:        0
Summary:        A pure Python implementation of the trie data structure
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/gsakkis/pytrie/
Source:         https://files.pythonhosted.org/packages/source/P/PyTrie/PyTrie-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/gsakkis/pytrie/master/LICENSE
Patch0:         fix-sorting-py2.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sortedcontainers}
BuildRequires:  fdupes
# needs tests, on py2 they are in devel
BuildRequires:  python-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-testsuite
Requires:       python-sortedcontainers
Provides:       python-pytrie
Obsoletes:      python-pytrie
BuildArch:      noarch
%python_subpackages

%description
pytrie is a pure Python (2 and 3) implementation of the trie data structure.

A trie is an ordered tree data structure that is used to store a mapping
where the keys are sequences, usually strings over an alphabet. In addition to
implementing the mapping interface, tries allow finding the items for a given
prefix, and vice versa, finding the items whose keys are prefixes of a given key.

%prep
%setup -q -n PyTrie-%{version}
cp %{SOURCE1} .
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
