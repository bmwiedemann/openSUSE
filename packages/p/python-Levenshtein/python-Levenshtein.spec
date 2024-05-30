#
# spec file for package python-Levenshtein
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


%{?sle15_python_module_pythons}
Name:           python-Levenshtein
Version:        0.25.1
Release:        0
Summary:        Python extension computing string distances and similarities
License:        GPL-2.0-or-later
URL:            https://github.com/rapidfuzz/Levenshtein
Source:         https://files.pythonhosted.org/packages/source/L/Levenshtein/Levenshtein-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scikit-build}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
%python_subpackages

%description
The Levenshtein Python C extension module contains functions for fast
computation of

 * Levenshtein (edit) distance, and edit operations
 * string similarity
 * approximate median strings, and generally string averaging
 * string sequence and set similarity

It supports both normal and Unicode strings.

%prep
%setup -q -n Levenshtein-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license COPYING
%doc HISTORY.md README.md
%{python_sitearch}/

%changelog
