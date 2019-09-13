#
# spec file for package python-bsddb3
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-bsddb3
Version:        6.2.6
Release:        0
Summary:        Python interface for Berkeley DB
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://pypi.python.org/pypi/bsddb3
#Freecode-URL:	 https://www.jcea.es/programacion/pybsddb.htm
Source:         https://files.pythonhosted.org/packages/source/b/bsddb3/bsddb3-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  db-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-testsuite
%python_subpackages

%description
This module provides a nearly complete wrapping of the Oracle/Sleepycat C API
for the Database Environment, Database, Cursor, Log Cursor, Sequence and
Transaction objects, and each of these is exposed as a Python type in the
bsddb3.db module.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}

%description devel
This module provides a nearly complete wrapping of the Oracle/Sleepycat C API
for the Database Environment, Database, Cursor, Log Cursor, Sequence and
Transaction objects, and each of these is exposed as a Python type in the
bsddb3.db module.

This package contains the development files for %{name}

%prep
%setup -q -n bsddb3-%{version}
sed -i "1d" Lib/bsddb/dbshelve.py # Fix non-executable bits

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitearch}/bsddb3/tests

%check
%python_exec test.py

%files %{python_files}
%doc ChangeLog README.txt TODO.txt docs/*
%license licenses.txt LICENSE.txt
%{python_sitearch}/*

%files %{python_files devel}
%license licenses.txt LICENSE.txt
%{_includedir}/python%{python_version}*/bsddb3

%changelog
