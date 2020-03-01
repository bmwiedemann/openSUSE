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
Name:           python-mysqlclient
Version:        1.4.6
Release:        0
Summary:        Python interface to MySQL
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/PyMySQL/mysqlclient-python
Source:         https://files.pythonhosted.org/packages/source/m/mysqlclient/mysqlclient-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libmysqlclient-devel
BuildRequires:  mariadb-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-attrs
BuildRequires:  unzip
Recommends:     mariadb
Provides:       python-mysql = %{version}
Obsoletes:      python-mysql < %{version}
Provides:       python-MySQL-python = %{version}
Obsoletes:      python-MySQL-python < %{version}
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
%python_build

python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo

%check
exit_code=0
cconf=abuild-myclient.cnf
#
# start the mariadb server
#
%mysql_testserver_start -u auth_db_user -p auth_db_pass
#
# creating client mysql config
#
%mysql_testserver_cconf -n $cconf
#
# running the test
#
rm -r MySQLdb
export TESTDB="$PWD/$cconf"
%pytest_arch -k "not (test_LONG or test_TEXT)"
#
# stopping mariadb
#
%mysql_testserver_stop
exit $exit_code

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%doc HISTORY.rst MANIFEST.in README.md build/sphinx/html
%{python_sitearch}/*

%changelog
