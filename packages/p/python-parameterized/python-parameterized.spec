#
# spec file for package python-parameterized
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_with ringdisabled
%if %{with ringdisabled}
# nose2 is actively maintained, but not used much in the distribution. No need to test it in ring1
%bcond_with nose2
%else
%bcond_without nose2
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{?sle15_python_module_pythons}
Name:           python-parameterized
Version:        0.8.1
Release:        0
Summary:        Parameterized testing
License:        BSD-2-Clause
URL:            https://github.com/wolever/parameterized
Source:         https://files.pythonhosted.org/packages/source/p/parameterized/parameterized-%{version}.tar.gz
# PATCH-FIX-UPSTREAM parameterized-pr116-pytest4.patch -- gh#wolever/parameterized#116, fix pytest >= 4 execution
Patch0:         parameterized-pr116-pytest4.patch
# PATCH-FIX-OPENSUSE remove_nose.patch mcepl@suse.com
# Remove nose dependency (patch is not very good, DO NOT SEND UPSTREAM!)
Patch1:         remove_nose.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
%if %{with nose2}
BuildRequires:  %{python_module nose2}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
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
# https://github.com/wolever/parameterized/issues/122
sed -i 's:import mock:from unittest import mock:' parameterized/test.py
export LANG=en_US.UTF8
%if %{with nose2}
%{python_expand nose2-%$python_version -v -B --pretty-assert}
%endif
%python_exec -m unittest parameterized.test
# https://github.com/wolever/parameterized/issues/122
%pytest parameterized/test.py -k 'not (test_with_docstring_1_v_l_ or test_with_docstring_0_value1)'

%files %{python_files}
%doc CHANGELOG.txt README.rst
%license LICENSE.txt
%{python_sitelib}/parameterized
%{python_sitelib}/parameterized-%{version}*-info

%changelog
