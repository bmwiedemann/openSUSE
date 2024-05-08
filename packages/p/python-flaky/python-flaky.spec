#
# spec file for package python-flaky
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%bcond_with test
%endif
Name:           python-flaky%{?psuffix}
Version:        3.8.1
Release:        0
Summary:        Plugin for nose or py.test that automatically reruns flaky tests
License:        Apache-2.0
URL:            https://github.com/box/flaky
Source:         https://files.pythonhosted.org/packages/source/f/flaky/flaky-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module flaky >= %{version}}
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
%pyproject_wheel
%endif

%if !%{with test}
%install
%pyproject_install
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
%{python_sitelib}/flaky
%{python_sitelib}/flaky-%{version}.dist-info
%endif

%changelog
