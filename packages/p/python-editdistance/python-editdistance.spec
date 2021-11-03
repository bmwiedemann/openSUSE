#
# spec file for package python-editdistance
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-editdistance
Version:        0.6.0
Release:        0
Summary:        An implementation of the edit distance (Levenshtein distance)
License:        MIT
URL:            https://www.github.com/aflc/editdistance
Source:         https://files.pythonhosted.org/packages/source/e/editdistance/editdistance-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-base
%python_subpackages

%description
An implementation of the edit distance (Levenshtein distance).

This library implements Levenshtein distance with C++ and Cython.

The algorithm used in this library is proposed by Heikki Hyyrö,
"Explaining and extending the bit-parallel approximate string
matching algorithm of Myers", (2001).

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description devel
This package contains the files needed for binding the %{name} C module.

%prep
%setup -q -n editdistance-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.rst
%exclude %{python_sitearch}/editdistance/*.h
%{python_sitearch}/

%files %{python_files devel}
%{python_sitearch}/editdistance/*.h

%changelog
