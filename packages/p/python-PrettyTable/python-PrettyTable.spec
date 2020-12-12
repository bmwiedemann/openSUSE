#
# spec file for package python-PrettyTable
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2011 Christian Berendt.
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
%define oldpython python
Name:           python-PrettyTable
Version:        0.7.2
Release:        0
Summary:        Library for displaying tabular data in formatted fashion
License:        BSD-2-Clause
URL:            https://github.com/jazzband/prettytable
Source0:        https://files.pythonhosted.org/packages/source/p/prettytable/prettytable-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-prettytable = 0.7.2
Obsoletes:      %{oldpython}-prettytable < 0.7.2
%endif
%python_subpackages

%description
PrettyTable is a Python library for representing tabular data in
ASCII tables, inspired by the tables emitted by the PostgreSQL shell,
psql. PrettyTable allows for selection of which columns are to be
printed, independent alignment of columns (left or right justified or
centred) and printing of "sub-tables" by specifying a row range.

%prep
%setup -q -n prettytable-%{version}
sed -i '1s/^#!.*//' prettytable.py

%build
%python_build

%install
%python_install

%check
export LANG=en_US.UTF-8
%python_exec setup.py test

%files %{python_files}
%license COPYING
%doc CHANGELOG README
%{python_sitelib}/*

%changelog
