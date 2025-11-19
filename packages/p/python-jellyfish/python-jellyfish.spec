#
# spec file for package python-jellyfish
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-jellyfish
Version:        1.2.1
Release:        0
Summary:        A library for doing approximate and phonetic matching of strings
License:        BSD-2-Clause
URL:            http://github.com/jamesturk/jellyfish
Source0:        https://files.pythonhosted.org/packages/source/j/jellyfish/jellyfish-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  cargo-packaging
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
%autosetup -p1 -n jellyfish-%{version} -a1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.md docs/*
%{python_sitearch}/jellyfish
%{python_sitearch}/jellyfish-%{version}.dist-info

%changelog
