#
# spec file for package python-PyTrie
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


Name:           python-PyTrie
Version:        0.4.0
Release:        0
Summary:        A pure Python implementation of the trie data structure
License:        BSD-3-Clause
URL:            https://github.com/gsakkis/pytrie/
Source:         https://files.pythonhosted.org/packages/source/P/PyTrie/PyTrie-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sortedcontainers}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-sortedcontainers
Provides:       python-pytrie = %{version}
Obsoletes:      python-pytrie < %{version}
BuildArch:      noarch
%python_subpackages

%description
pytrie is a pure Python 3 implementation of the trie data structure.

A trie is an ordered tree data structure that is used to store a mapping
where the keys are sequences, usually strings over an alphabet. In addition to
implementing the mapping interface, tries allow finding the items for a given
prefix, and vice versa, finding the items whose keys are prefixes of a given key.

%prep
%setup -q -n PyTrie-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pytrie.py
%{python_sitelib}/[Pp]y[Tt]rie-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/pytrie*

%changelog
