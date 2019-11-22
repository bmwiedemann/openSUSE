#
# spec file for package python-PyHamcrest
#
# Copyright (c) 2019 SUSE LLC
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
Name:           python-PyHamcrest
Version:        1.9.0
Release:        0
Summary:        Hamcrest framework for matcher objects
License:        BSD-3-Clause
URL:            https://github.com/hamcrest/PyHamcrest
# PyPi is missing tests
#Source:         https://files.pythonhosted.org/packages/source/P/PyHamcrest/PyHamcrest-%%{version}.tar.gz
Source:         https://github.com/hamcrest/PyHamcrest/archive/V%{version}.tar.gz
Patch0:         0001-Add-boolean-matchers.patch
# # PATCH-FIX-UPSTREAM pytest4.patch gh#hamcrest/PyHamcrest#123 mcepl@suse.com
# # eliminate non-compatible test case
# Patch1:         pytest4.patch
# PATCH-FIX-UPSTREAM pytest4-02.patch gh#hamcrest/PyHamcrest#123 mcepl@suse.com
# compatibility with pytest4+ (from gh#hamcrest/PyHamcrest#124)
Patch1:         pytest4-02.patch
BuildRequires:  %{python_module hypothesis >= 1.11}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.4
Provides:       python-hamcrest = %{version}
Obsoletes:      python-hamcrest < %{version}
BuildArch:      noarch
%python_subpackages

%description
Hamcrest framework for matcher objects.
PyHamcrest is a framework for writing matcher objects,
allowing you to declaratively define “match” rules.

%prep
%setup -q -n PyHamcrest-%{version}
%autopatch -p1

rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/hamcrest

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/hamcrest
%{python_sitelib}/PyHamcrest-%{version}-py*.egg-info/

%changelog
