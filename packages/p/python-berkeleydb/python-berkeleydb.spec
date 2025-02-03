#
# spec file for package python-berkeleydb
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-berkeleydb
Version:        18.1.13
Release:        0
Summary:        Python bindings for Oracle Berkeley DB
License:        BSD-3-Clause
URL:            https://www.jcea.es/programacion/pybsddb.htm
Source:         https://files.pythonhosted.org/packages/source/b/berkeleydb/berkeleydb-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 65.5.0}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module wheel}
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This module provides a nearly complete wrapping of the Oracle/Sleepycat C API
for the Database Environment, Database, Cursor, Log Cursor, Sequence and
Transaction objects, and each of these is exposed as a Python type in the
berkeleydb.db module. The database objects can use various access methods:
btree, hash, recno, queue and heap.  Complete support of Oracle Berkeley DB
distributed transactions. Complete support for Oracle Berkeley DB Replication
Manager. Complete support for Oracle Berkeley DB Base Replication.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
This module provides a nearly complete wrapping of the Oracle/Sleepycat C API
for the Database Environment, Database, Cursor, Log Cursor, Sequence and
Transaction objects, and each of these is exposed as a Python type in the
berkeleydb.db module.

This package contains the development files for %{name}

%prep
%autosetup -p1 -n berkeleydb-%{version}
sed -i '/\#\!\/usr\/bin\/env\ python/d' src/berkeleydb/dbshelve.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch} %{buildroot}%{_docdir}

%check
%python_exec test.py

%files %{python_files}
%doc ChangeLog README.txt docs/*
%license LICENSE.txt licenses.txt
%{python_sitearch}/berkeleydb
%{python_sitearch}/berkeleydb-%{version}.dist-info

%files %{python_files devel}
%license licenses.txt LICENSE.txt
%{_includedir}/python%{python_version}*/berkeleydb

%changelog
