#
# spec file for package python-easydev
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
Name:           python-easydev
Version:        0.9.38
Release:        0
Summary:        Common utilities to ease the development of Python packages
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/cokelaer/easydev
Source:         https://files.pythonhosted.org/packages/source/e/easydev/easydev-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-colorama
Requires:       python-colorlog
Requires:       python-pexpect
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-line_profiler
BuildArch:      noarch
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
%python_subpackages

%description
The easydev package  provides miscellaneous functions that are
repeatedly used during the development of Python packages. The goal
is to help developers on speeding up their own dev. It has been used
also as an incubator for other packages and is stable.

%prep
%setup -q -n easydev-%{version}
sed -i -e '/^#!\//, 1d' easydev/appdirs.py
rm -r easydev/share/__pycache__

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/easydev_buildPackage
%python_clone -a %{buildroot}%{_bindir}/browse
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative easydev_buildPackage
%python_install_alternative browse

%postun
%python_uninstall_alternative easydev_buildPackage
%python_uninstall_alternative browse

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/browse
%python_alternative %{_bindir}/easydev_buildPackage
%{python_sitelib}/*

%changelog
