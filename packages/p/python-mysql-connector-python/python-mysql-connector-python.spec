#
# spec file for package python-mysql-connector-python
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-mysql-connector-python
Version:        9.6.0
Release:        0
Summary:        MySQL driver written in Python
License:        SUSE-GPL-2.0-with-FLOSS-exception
Group:          Development/Languages/Python
URL:            http://dev.mysql.com/doc/connector-python/en/index.html
# GitHub: https://github.com/mysql/mysql-connector-python
Source:         https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-%{version}-src.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module protobuf}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  mariadb
BuildRequires:  python-rpm-macros
Requires:       python-dnspython
Requires:       python-protobuf
%python_subpackages

%description
MySQL driver written in Python which does not depend on MySQL C client libraries and implements the DB API v2.0 specification (PEP-249).

%prep
%autosetup -p1 -n mysql-connector-python-%{version}-src

%build
pushd mysql-connector-python
%python_build
popd
pushd mysqlx-connector-python
%python_build
popd

%install
pushd mysql-connector-python
%python_install
popd
pushd mysqlx-connector-python
%python_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitearch}

#FIXME(toabctl): Reenable testuite
# probably won't work against mariadb 10
# the test script is using rather deep details
# of `mysql` table structure
# --matejcik
#check
#python unittests.py --with-mysql=/usr

%files %{python_files}
%license LICENSE.txt
%doc README.txt CHANGES.txt
%{python_sitearch}/mysql
%{python_sitearch}/mysql*.egg-info
%{python_sitearch}/mysqlx

%changelog
