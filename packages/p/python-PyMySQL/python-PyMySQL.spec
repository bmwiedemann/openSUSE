#
# spec file for package python-PyMySQL
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-PyMySQL
Version:        0.9.3
Release:        0
Summary:        Pure Python MySQL Driver
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/PyMySQL/PyMySQL/
Source:         https://files.pythonhosted.org/packages/source/P/PyMySQL/PyMySQL-%{version}.tar.gz
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
# will be removed with next release
BuildRequires:  %{python_module unittest2}
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
%setup -q -n PyMySQL-%{version}
# remove unwanted shebang
sed -i '1 { /^#!/ d }' pymysql/tests/thirdparty/test_MySQLdb/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Needs mysql server
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE
%doc CHANGELOG README.rst
%{python_sitelib}/*

%changelog
