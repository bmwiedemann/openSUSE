#
# spec file for package python-PyMySQL
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


# mariadb-rpm-macros is either not available or not sufficient for Leaps
%if 0%{?suse_version} > 1500
%bcond_without tests
%else
%bcond_with tests
%endif

%{?sle15_python_module_pythons}
Name:           python-PyMySQL
Version:        1.1.1
Release:        0
Summary:        Pure Python MySQL Driver
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/PyMySQL/PyMySQL/
Source:         https://github.com/PyMySQL/PyMySQL/archive/v%{version}.tar.gz#/PyMySQL-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
%if %{with tests}
BuildRequires:  mariadb-rpm-macros
%endif
# will be removed with next release
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
BuildArch:      noarch
%python_subpackages

%description
This package contains a pure-Python MySQL client library. Documentation on the
MySQL client/server protocol can be found here:
http://forge.mysql.com/wiki/MySQL_Internals_ClientServer_Protocol

The goal of pymysql is to be a drop-in replacement for MySQLdb and work on
CPython 2.3+, Jython, IronPython, PyPy and Python 3. We test for compatibility
by simply changing the import statements in the Django MySQL backend and running
its unit tests as well as running it against the MySQLdb and myconnpy unit tests.

%prep
%autosetup -p1 -n PyMySQL-%{version}
# remove unwanted shebang
sed -i '1 { /^#!/ d }' pymysql/tests/thirdparty/test_MySQLdb/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with tests}
%check
exit_code=0
dbuser='db_user'
dbuserpw='db_user_secret'
dbname1='test1'
dbname2='test2'
# Needs mysql server
#%%python_expand PYTHONPATH=%%{buildroot}%%{$python_sitelib} py.test-%%{$python_bin_suffix} -v
cconf=abuild-myclient.cnf
#
# start the mariadb server
#
%mysql_testserver_start -u $dbuser -p $dbuserpw -d $dbname1:$dbname2 -t 3306
#
# creating client config, see base.py
#
cat << EOF > pymysql/tests/databases.json
[{"host":"localhost","user":"$dbuser","passwd":"$dbuserpw",
   "database":"$dbname1", "use_unicode": true, "local_infile": true},
 {"host":"localhost","user":"$dbuser","passwd":"$dbuserpw","database":"$dbname2"}]
EOF
#
# running the test
#
export USER="$dbuser"
export PASSWORD="$dbuserpw"
# test_json is broken for mariadb 11.0.2
%pytest pymysql/tests  -k 'not (test_stored_procedures or test_json)' || exit_code=1
#
# stopping mariadb
#
%mysql_testserver_stop
exit $exit_code
%endif

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%{python_sitelib}/pymysql
%{python_sitelib}/[pP]y[mM]y[sS][qQ][lL]-%{version}.dist-info

%changelog
