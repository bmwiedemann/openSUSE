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

%{?sle15_python_module_pythons}
Name:           python-parameterized
Version:        0.9.0
Release:        0
Summary:        Parameterized testing
License:        BSD-2-Clause
URL:            https://github.com/wolever/parameterized
Source:         https://files.pythonhosted.org/packages/source/p/parameterized/parameterized-%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove_nose.patch mcepl@suse.com
# Remove nose dependency (patch is not very good, DO NOT SEND UPSTREAM!)
Patch1:         remove_nose.patch
# PATCH-FIX-UPSTREAM skip_failing_teardown.patch gh#wolever/parameterized#167 mcepl@suse.com
# skip failing assert in tearDownModule [sic]
Patch2:         skip_failing_teardown.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
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
%autosetup -p1 -n parameterized-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/wolever/parameterized/issues/122
sed -i 's:import mock:from unittest import mock:' parameterized/test.py
export LANG=en_US.UTF8
%if %{with nose2}
%{python_expand nose2-%$python_version -v -B --pretty-assert}
%endif
%python_exec -m unittest parameterized.test
# gh#wolever/parameterized#122
skip_tests="test_with_docstring_1_v_l_ or test_with_docstring_0_value1"
%pytest parameterized/test.py -k "not ($skip_tests)"

%files %{python_files}
%doc README.rst
# gh#wolever/parameterized#168
# %%doc CHANGELOG.txt
%license LICENSE.txt
%{python_sitelib}/parameterized
%{python_sitelib}/parameterized-%{version}*-info

%changelog
