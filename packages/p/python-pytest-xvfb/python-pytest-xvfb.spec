#
# spec file for package python-pytest-xvfb
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
Name:           python-pytest-xvfb
Version:        1.2.0
Release:        0
Summary:        Pytest plugin to run Xvfb for tests
License:        MIT
URL:            https://github.com/The-Compiler/pytest-xvfb
Source:         https://files.pythonhosted.org/packages/source/p/pytest-xvfb/pytest-xvfb-%{version}.tar.gz
BuildRequires:  %{python_module PyVirtualDisplay >= 0.2.1}
BuildRequires:  %{python_module pytest >= 2.8.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  xvfb-run
Requires:       python-PyVirtualDisplay >= 0.2.1
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
%setup -q -n pytest-xvfb-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_failing_start fails on i586
%pytest -k 'not test_failing_start'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
