#
# spec file for package python-parameterized
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
Name:           python-parameterized
Version:        0.7.1
Release:        0
Summary:        Parameterized testing
License:        BSD-2-Clause
URL:            https://github.com/wolever/parameterized
Source:         https://files.pythonhosted.org/packages/source/p/parameterized/parameterized-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip_Documentation_tests.patch gh#wolever/parameterized#84 mcepl@suse.com
# Skip tests failing with Python 3.8
Patch0:         skip_Documentation_tests.patch
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose2}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module unittest2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-nose
Suggests:       python-nose2
Suggests:       python-unittest2
BuildArch:      noarch
%python_subpackages

%description
Parameterized testing with any Python test framework.

Not working with supportest "pytest" versions

%prep
%setup -q -n parameterized-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
# gh#wolever/parameterized#84
%{python_expand nosetests-%$python_version}
%{python_expand nose2-%$python_version}
%{python_expand unit2-%$python_version}
%python_exec -m unittest parameterized.test

%files %{python_files}
%doc CHANGELOG.txt README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
