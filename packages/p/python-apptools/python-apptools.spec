#
# spec file for package python-apptools
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         X_display         ":98"
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-apptools%{psuffix}
Version:        5.3.1
Release:        0
Summary:        Application tools in Python
# Source code is under BSD but images are under different licenses
# and details are inside image_LICENSE.txt
License:        BSD-3-Clause AND LGPL-2.1-only AND LGPL-3.0-only
URL:            https://github.com/enthought/apptools
Source:         https://files.pythonhosted.org/packages/source/a/apptools/apptools-%{version}.tar.gz
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module traits}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-configobj
Requires:       python-traits
Recommends:     python-pandas
Recommends:     python-tables
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module apptools = %{version}}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module traitsui}
BuildRequires:  xorg-x11-server
%endif
%python_subpackages

%description
The apptools project includes a set of packages that Enthought has found
useful in creating a number of applications.  They implement functionality
that is commonly needed by many applications.

Part of the Enthought Tool Suite (ETS).

%prep
%autosetup -p1 -n apptools-%{version}

%if !%{with test}
%build
%pyproject_wheel
# Remove duplicates now so we can let rpm install it later
%fdupes examples/

%install
%pyproject_install
%{python_expand $python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/apptools/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/apptools/
%fdupes %{buildroot}%{$python_sitelib}
}
%endif

%if %{with test}
%check
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

%pyunittest -v
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst CHANGES.txt
%doc examples/
%license LICENSE.txt image_LICENSE*.txt
%{python_sitelib}/apptools/
%{python_sitelib}/apptools-%{version}.dist-info
%endif

%changelog
