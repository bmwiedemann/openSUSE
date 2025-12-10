#
# spec file for package python-pytest-xvfb
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


%{?sle15_python_module_pythons}
Name:           python-pytest-xvfb
Version:        3.1.1
Release:        0
Summary:        Pytest plugin to run Xvfb for tests
License:        MIT
URL:            https://github.com/The-Compiler/pytest-xvfb
Source:         https://files.pythonhosted.org/packages/source/p/pytest-xvfb/pytest_xvfb-%{version}.tar.gz
BuildRequires:  %{python_module PyVirtualDisplay >= 1.3}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 2.8.1}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  xvfb-run
Requires:       python-PyVirtualDisplay >= 1.3
Requires:       python-pytest >= 2.8.1
Requires:       xdpyinfo
Recommends:     xorg-x11-server
BuildArch:      noarch
%python_subpackages

%description
A pytest plugin to run Xvfb for tests.

With Xvfb and the plugin installed, your testsuite automatically runs
with Xvfb. This allows tests to be run without windows popping up
during GUI tests or on systems without a display (like a CI).

If Xvfb is not installed, the plugin does not run and your tests will
still work as normal. However, a warning message will print to standard
output letting you know that Xvfb is not installed.

If you're currently using xvfb-run in something like .travis.yml,
simply remove it and install this plugin instead - then you'll also have the
benefits of Xvfb locally.

%prep
%setup -q -n pytest_xvfb-%{version}
rm tests/test_xvfb_windows.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# can't test this on obs
donttest="test_empty_display or test_no_xvfb_marker or test_xvfb_with_xauth"
%pytest -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_xvfb.py
%pycache_only %{python_sitelib}/__pycache__/pytest_xvfb*.pyc
%{python_sitelib}/pytest_xvfb-%{version}.dist-info

%changelog
