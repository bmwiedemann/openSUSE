#
# spec file
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-flaky%{?psuffix}
Version:        3.7.0
Release:        0
Summary:        Plugin for nose or py.test that automatically reruns flaky tests
License:        Apache-2.0
URL:            https://github.com/box/flaky
Source:         https://files.pythonhosted.org/packages/source/f/flaky/flaky-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM remove_nose.patch gh#box/flaky#171 mcepl@suse.com
# remove dependency on nose
Patch0:         remove_nose.patch
# PATCH-FEATURE-UPSTREAM remove_mock.patch gh#box/flaky#171 mcepl@suse.com
# this patch makes things totally awesome
Patch1:         remove_mock.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module flaky >= %{version}}
BuildRequires:  %{python_module genty}
BuildRequires:  %{python_module pytest}
%if 0%{?suse_version} <= 1500
BuildRequires:  python-mock
%endif
%endif
%python_subpackages

%description
Flaky is a plugin for py.test that automatically reruns flaky tests.

Ideally, tests reliably pass or fail, but sometimes test fixtures must rely on components that aren't 100%
reliable. With flaky, instead of removing those tests or marking them to @skip, they can be automatically
retried.

For more information about flaky, see `this presentation <http://opensource.box.com/flaky/>`_.

%prep
%autosetup -p1 -n flaky-%{version}

%if !%{with test}
%build
%python_build
%endif

%if !%{with test}
%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest -k 'example and not options' --doctest-modules test/test_pytest/
%pytest -k 'example and not options' test/test_pytest/
%pytest -p no:flaky test/test_pytest/test_flaky_pytest_plugin.py
export PYTEST_ADDOPTS="--force-flaky --max-runs 2"
%pytest test/test_pytest/test_pytest_options_example.py
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
