#
# spec file for package python-mysqlclient
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
%define oldpython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-mysqlclient%{psuffix}
Version:        1.4.6
Release:        0
Summary:        Python interface to MySQL
License:        GPL-2.0-or-later
URL:            https://github.com/PyMySQL/mysqlclient-python
Source:         https://files.pythonhosted.org/packages/source/m/mysqlclient/mysqlclient-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libmysqlclient-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-attrs
BuildRequires:  unzip
Recommends:     mariadb
Provides:       python-mysql = %{version}
Obsoletes:      python-mysql < %{version}
Provides:       python-MySQL-python = %{version}
Obsoletes:      python-MySQL-python < %{version}
%if %{with test}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module mysqlclient >= %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  mariadb-rpm-macros
%endif
%ifpython2
Provides:       %{oldpython}-mysql = %{version}
Obsoletes:      %{oldpython}-mysql < %{version}
Provides:       %{oldpython}-MySQL-python = %{version}
Obsoletes:      %{oldpython}-MySQL-python < %{version}
%endif
%python_subpackages

%description
MySQLdb is an interface to the popular MySQL database server for Python.

This package adds Python 3 support and bug fixes to MySQLdb1.

%prep
%setup -q -n mysqlclient-%{version}

%build
%if !%{with test}
%python_build

python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo
%endif

%check
%if %{with test}
exit_code=0
cconf=abuild-myclient.cnf
#
# start the mariadb server
#
%mysql_testserver_start -u auth_db_user -p auth_db_pass -d test_database
#
# creating client mysql config
#
%mysql_testserver_cconf -n $cconf -d test_database
#
# running the test
#
rm -r MySQLdb
export TESTDB="$PWD/$cconf"
%pytest_arch -k "not (test_LONG or test_TEXT)" || exit_code=1
#
# stopping mariadb
#
%mysql_testserver_stop
exit $exit_code
%endif

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc HISTORY.rst MANIFEST.in README.md build/sphinx/html
%{python_sitearch}/*
%endif

%changelog
