#
# spec file for package python-control
#
# Copyright (c) 2021 SUSE LLC
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


%define skip_python2 1
%define skip_python36 1
Name:           python-control
Version:        0.9.1
Release:        0
Summary:        Python control systems library
License:        BSD-3-Clause
URL:            http://python-control.org
Source:         https://files.pythonhosted.org/packages/source/c/control/control-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-scipy
Recommends:     python-slycot
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib-qt5}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module slycot}
BuildRequires:  libjemalloc2
# /SECTION
%python_subpackages

%description
The Python Control Systems Library is a Python module that implements basic
operations for analysis and design of feedback control systems.

%prep
%autosetup -p1 -n control-%{version}
#remove shebang
sed -i '1{\@^#!/usr/bin/env@ d}' control/tests/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The default Agg backend does not define the toolbar attribute in the Figure
# Manager used by some tests, so we run the tests with the Qt5 backend
export MPLBACKEND="Qt5Agg"
# preload malloc library to avoid free() error on i586 architecture
if [[ $(getconf LONG_BIT) == 32 ]]; then
export LD_PRELOAD="%{_libdir}/libjemalloc.so.2"
fi
%pytest

%files %{python_files}
%doc ChangeLog README.rst
%license LICENSE
%{python_sitelib}/control
%{python_sitelib}/control-%{version}-py*.egg-info

%changelog
