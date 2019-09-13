#
# spec file for package python-binaryornot
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
# Tests run too slowly on some architectures
%ifarch %{ix86} x86_64  ppc64 ppc64le
%bcond_without  test
%else
%bcond_with     test
%endif
Name:           python-binaryornot
Version:        0.4.4
Release:        0
Summary:        Python package to check if a file is binary or text
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/audreyr/binaryornot
Source:         https://files.pythonhosted.org/packages/source/b/binaryornot/binaryornot-%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove_hypothesis_tests.patch -- remove hypothesis-based tests
Patch0:         remove_hypothesis_tests.patch
BuildRequires:  %{python_module chardet >= 3.0.2}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-chardet >= 3.0.2
BuildArch:      noarch
%python_subpackages

%description
Pure Python package to guess whether a file is binary or text,
using a heuristic similar to Perl's pp_fttext and its analysis
by eliben.

%prep
%setup -q -n binaryornot-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python tests/test_check.py
}
%endif

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst HISTORY.rst README.rst
%{python_sitelib}/*

%changelog
