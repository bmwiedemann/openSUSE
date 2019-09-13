#
# spec file for package python-iniparse
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.4
Release:        0
Summary:        Python Module for Accessing and Modifying Configuration Data in INI files
License:        MIT
Group:          Development/Libraries/Python
Url:            http://code.google.com/p/iniparse/
Source:         http://iniparse.googlecode.com/files/iniparse-%{version}.tar.gz
# PATCH-FIX-UPSTREAM: speilicke@suse.com -- Backport of https://code.google.com/p/iniparse/issues/detail?id=31
Patch0:         iniparse-insert-after-commented-option.patch
# PATCH-FIX-UPSTREAM: timlau@fedoraproject.org -- Backport of https://code.google.com/p/iniparse/issues/detail?id=28
Patch1:         iniparse-fix-issue-28.patch
# PATCH-FIX-OPENSUSE: timlau@fedoraproject.org -- Variant of http://code.google.com/p/iniparse/issues/detail?id=22 that uses python-six to support py2+py3, from Fedora
Patch2:         python-iniparse-python3-compat.patch
# PATCH-FIX-OPENSUSE: ngompa13@gmail.com -- Fix setup.py to have correct information, from Fedora
Patch3:         python-iniparse-setup-fixes.patch

BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  python-rpm-macros
# python2-devel contains test module, even for noarch package
BuildRequires:  python2-devel
# tests require testsuite modules
BuildRequires:  python3-testsuite
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Requires:       python-six

%python_subpackages

%description
iniparse is an INI parser for Python which is API compatible with the
standard library's ConfigParser, preserves structure of INI files
(order of sections & options, indentation, comments, and blank lines
are preserved when data is updated), and is more convenient to use.

%prep
%setup -q -n iniparse-%{version}
%patch0 -p0
%patch1 -p1
%patch2 -p0
%patch3 -p0

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
%defattr(-,root,root,-)
%doc Changelog LICENSE LICENSE-PSF README html/*
%{python_sitelib}/*

%changelog
