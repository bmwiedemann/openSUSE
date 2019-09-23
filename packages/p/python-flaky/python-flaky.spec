#
# spec file for package python-flaky
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-flaky
Version:        3.6.1
Release:        0
Summary:        Plugin for nose or py.test that automatically reruns flaky tests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/box/flaky
Source:         https://files.pythonhosted.org/packages/source/f/flaky/flaky-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module flaky >= %{version}}
BuildRequires:  %{python_module genty}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Flaky is a plugin for nose or py.test that automatically reruns flaky tests.

Ideally, tests reliably pass or fail, but sometimes test fixtures must rely on components that aren't 100%
reliable. With flaky, instead of removing those tests or marking them to @skip, they can be automatically
retried.

For more information about flaky, see `this presentation <http://opensource.box.com/flaky/>`_.

%prep
%setup -q -n flaky-%{version}

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
%{python_expand echo
    nosetests="nosetests-%{$python_bin_suffix}"
    pytest="pytest-%{$python_bin_suffix}"
    $nosetests --with-flaky --exclude="test_nose_options_example" test/test_nose/
    $pytest    -k 'example and not options' --doctest-modules test/test_pytest/
    $pytest    -k 'example and not options' test/test_pytest/
    $pytest    -p no:flaky test/test_pytest/test_flaky_pytest_plugin.py
    $nosetests --with-flaky --force-flaky --max-runs 2 test/test_nose/test_nose_options_example.py
    $pytest    --force-flaky --max-runs 2  test/test_pytest/test_pytest_options_example.py
}
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
