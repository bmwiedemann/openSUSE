#
# spec file for package python-rapidfuzz
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rapidfuzz
Version:        2.13.6
Release:        0
Summary:        Rapid fuzzy string matching
License:        MIT
URL:            https://github.com/maxbachmann/RapidFuzz
Source:         https://files.pythonhosted.org/packages/source/r/rapidfuzz/rapidfuzz-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module PyInstaller}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-build}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
Suggests:       python-numpy
%python_subpackages

%description
RapidFuzz is a fast string matching library for Python and C++, which is using the string similarity calculations from FuzzyWuzzy.

%prep
%setup -q -n rapidfuzz-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
# remove devel file
%python_expand find %{buildroot} -type f -name "rapidfuzz.h" -delete -print

%check
# tests are a bit unstable
%ifarch x86_64
export skip_tests="not (hypothesis and test_cdist)"
%else
%ifarch %ix86
export skip_tests="not (hypothesis and test_jaro_winkler_word)"
%else
export skip_tests=""
%endif
%endif
%pytest_arch -k "$skip_tests"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/rapidfuzz
%{python_sitearch}/rapidfuzz-*.dist-info

%changelog
