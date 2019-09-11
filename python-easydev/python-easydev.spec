#
# spec file for package python-easydev
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-easydev
Version:        0.9.37
Release:        0
Summary:        Common utilities to ease the development of Python packages
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/cokelaer/easydev
Source:         https://files.pythonhosted.org/packages/source/e/easydev/easydev-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module colorlog}
BuildRequires:  %{python_module line_profiler}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-colorama
Requires:       python-colorlog
Requires:       python-pexpect
Recommends:     python-line_profiler
BuildArch:      noarch

%python_subpackages

%description
The easydev package  provides miscellaneous functions that are
repeatedly used during the development of Python packages. The goal
is to help developers on speeding up their own dev. It has been used
also as an incubator for other packages and is stable.

%prep
%setup -q -n easydev-%{version}
sed -i -e '/^#!\//, 1d' easydev/appdirs.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license COPYING
%python3_only %{_bindir}/browse
%python3_only %{_bindir}/easydev_buildPackage
%{python_sitelib}/*

%changelog
