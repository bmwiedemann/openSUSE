#
# spec file for package python-jellyfish
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-jellyfish
Version:        0.8.2
Release:        0
Summary:        A library for doing approximate and phonetic matching of strings
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://github.com/jamesturk/jellyfish
Source:         https://files.pythonhosted.org/packages/source/j/jellyfish/jellyfish-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Jellyfish is a python library for doing approximate and phonetic
matching of strings.

Includes algorithms for string comparison: Levenshtein Distance,
Damerau-Levenshtein Distance, Jaro Distance, Jaro-Winkler Distance,
Match Rating Approach Comparison and Hamming Distance.

And algorithms for phonetic encoding: American Soundex, Metaphone,
NYSIIS (New York State Identification and Intelligence System) and
Match Rating Codex.

%prep
%setup -q -n jellyfish-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYTHONDONTWRITEBYTECODE=1
%pytest %{buildroot}%{$python_sitearch}/jellyfish/test.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
