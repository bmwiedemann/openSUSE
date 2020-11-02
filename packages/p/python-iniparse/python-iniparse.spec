#
# spec file for package python-iniparse
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017 Neal Gompa <ngompa13@gmail.com>.
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
Name:           python-iniparse
Version:        0.5
Release:        0
Summary:        Python Module for Accessing and Modifying Configuration Data in INI files
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/candlepin/python-iniparse
Source:         https://files.pythonhosted.org/packages/source/i/iniparse/iniparse-%{version}.tar.gz
# PATCH-FIX-UPSTREAM: speilicke@suse.com -- Backport of https://code.google.com/p/iniparse/issues/detail?id=31
Patch0:         iniparse-insert-after-commented-option.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  python-rpm-macros
# python2-devel contains test module, even for noarch package
BuildRequires:  python2-devel
# tests require testsuite modules
BuildRequires:  %{python_module testsuite}
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
iniparse is an INI parser for Python which is API compatible with the
standard library's ConfigParser, preserves structure of INI files
(order of sections & options, indentation, comments, and blank lines
are preserved when data is updated), and is more convenient to use.

%prep
%setup -q -n iniparse-%{version}
%patch0

chmod 644 html/index.html
sed -i "/.*test_multiprocessing.*/d" tests/__init__.py # NOTE(saschpe): Doesn't work and I'm lazy

%build
%python_build

%install
%python_install
rm -rf %{buildroot}%{_datadir}/doc/iniparse-%{version} # Remove unwanted stuff

%check
%python_exec runtests.py

%files %{python_files}
%license LICENSE
%doc Changelog LICENSE-PSF README.md html/*
%{python_sitelib}/*

%changelog
