#
# spec file for package python-control
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


Name:           python-control
Version:        0.10.0
Release:        0
Summary:        Python control systems library
License:        BSD-3-Clause
URL:            https://python-control.org
Source:         https://files.pythonhosted.org/packages/source/c/control/control-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM control-pr994-numpy2.patch gh#python-control/python-control#994
Patch1:         control-pr994-numpy2.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-scipy >= 1.3
Recommends:     python-slycot
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib-qt}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module scipy >= 1.3}
BuildRequires:  %{python_module slycot}
# /SECTION
%python_subpackages

%description
The Python Control Systems Library is a Python module that implements basic
operations for analysis and design of feedback control systems.

%prep
%autosetup -p1 -n control-%{version}
# remove shebang from testfiles which could be theoretically run standalone, but we don't do this
sed -i '1{\@^#!/usr/bin/env@ d}' control/tests/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The default Agg backend does not define the toolbar attribute in the Figure
# Manager used by some tests, so we run the tests with the Qt5 backend
export MPLBACKEND="Qt5Agg"
# precision issues
donttest="test_lti_nlsys_response"
# flaky precision issues
donttest="$donttest or test_response_plot_kwargs"
# gh#python-control/python-control#838
[ "${RPM_ARCH}" != "x86_64" ] && donttest="$donttest or (test_optimal_doc and shooting-3-u0-None)"
# causes i586 segfaults in matplotlib after successful balanced model reduction tests
[ $(getconf LONG_BIT) -eq 32 ] && donttest="$donttest or testBalredMatchDC"
%pytest -n auto -k "not (${donttest})"

%files %{python_files}
%doc ChangeLog README.rst
%license LICENSE
%{python_sitelib}/control
%{python_sitelib}/control-%{version}.dist-info

%changelog
