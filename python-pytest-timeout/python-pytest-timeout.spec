#
# spec file for package python-pytest-timeout
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
Name:           python-pytest-timeout
Version:        1.3.3
Release:        0
Summary:        Pytest plugin to abort hanging tests
License:        MIT
Group:          Development/Languages/Python
URL:            http://bitbucket.org/pytest-dev/pytest-timeout/
Source:         https://files.pythonhosted.org/packages/source/p/pytest-timeout/pytest-timeout-%{version}.tar.gz
Patch0:         pytest4.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pytest >= 3.6.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pexpect
Requires:       python-pytest >= 3.6.0
BuildArch:      noarch
%python_subpackages

%description
This is a plugin which will terminate tests after a certain timeout.
When doing so it will show a stack dump of all threads running at the
time.  This is useful when running tests under a continuous
integration server or simply if you don't know why the test suite
hangs.

Note that while by default on POSIX systems py.test will continue to
execute the tests after a test has timed, out this is not always
possible.  Often the only sure way to interrupt a hanging test is by
terminating the entire process.  As this is a hard termination
(``os._exit()``) it will result in no teardown, JUnit XML output etc.
But the plugin will ensure you will have the debugging output on
stderr nevertheless, which is the most important part at this stage.
See below for detailed information on the timeout methods and their
side-effects.

%prep
%setup -q -n pytest-timeout-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m pytest test_pytest_timeout.py

%files %{python_files}
%license LICENSE
%doc README
%{python_sitelib}/pytest_timeout-%{version}-py*.egg-info
%{python_sitelib}/pytest_timeout.py*
%pycache_only %{python_sitelib}/__pycache__/pytest_timeout*.py*

%changelog
