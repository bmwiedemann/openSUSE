#
# spec file for package python-pytest-timeout
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%bcond_with ringdisabled
%{?sle15_python_module_pythons}
Name:           python-pytest-timeout
Version:        2.1.0
Release:        0
Summary:        Pytest plugin to abort hanging tests
License:        MIT
URL:            https://github.com/pytest-dev/pytest-timeout/
Source:         https://files.pythonhosted.org/packages/source/p/pytest-timeout/pytest-timeout-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 5.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 5.0.0
# SECTION test
%if !%{with ringdisabled}
BuildRequires:  %{python_module pytest-cov}
%endif
BuildRequires:  %{python_module pexpect}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
This is a plugin which will terminate tests after a certain timeout.
When doing so it will show a stack dump of all threads running at the
time.  This is useful when running tests under a continuous
integration server or simply if you don't know why the test suite
hangs.

Note that while by default on POSIX systems pytest will continue to
execute the tests after a test has timed, out this is not always
possible.  Often the only sure way to interrupt a hanging test is by
terminating the entire process.  As this is a hard termination
(``os._exit()``) it will result in no teardown, JUnit XML output etc.
But the plugin will ensure you will have the debugging output on
stderr nevertheless, which is the most important part at this stage.

%prep
%setup -q -n pytest-timeout-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if %{with ringdisabled}
donttest="or test_cov"
%endif
%pytest -k "not (donttestprefix $donttest)"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_timeout-%{version}*-info
%{python_sitelib}/pytest_timeout.py*
%pycache_only %{python_sitelib}/__pycache__/pytest_timeout*.pyc

%changelog
