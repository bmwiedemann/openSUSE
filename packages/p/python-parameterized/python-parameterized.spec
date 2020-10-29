#
# spec file for package python-parameterized
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
Name:           python-parameterized
Version:        0.7.4
Release:        0
Summary:        Parameterized testing
License:        BSD-2-Clause
URL:            https://github.com/wolever/parameterized
Source:         https://files.pythonhosted.org/packages/source/p/parameterized/parameterized-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip_Documentation_tests.patch gh#wolever/parameterized#84 mcepl@suse.com
# Skip tests failing with Python 3.8
Patch0:         skip_Documentation_tests.patch
# PATCH-FIX-UPSTREAM remove_nose.patch mcepl@suse.com
# Remove nose dependency (patch is not very good, DO NOT SEND UPSTREAM!)
Patch1:         remove_nose.patch
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-nose2
BuildArch:      noarch
%python_subpackages

%description
Parameterized testing with any Python test framework.

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
%{python_expand nose2-%$python_version -v -B --pretty-assert}
%python_exec -m unittest parameterized.test
%pytest parameterized/test.py

%files %{python_files}
%doc CHANGELOG.txt README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
