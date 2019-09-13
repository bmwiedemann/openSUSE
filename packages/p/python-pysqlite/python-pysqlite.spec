#
# spec file for package python-pysqlite
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


Name:           python-pysqlite
Version:        2.8.3
Release:        0
Summary:        DB-API 2.0 interface for SQLite 3.x
License:        Zlib
Group:          Development/Languages/Python
URL:            http://github.com/ghaering/pysqlite
Source:         https://files.pythonhosted.org/packages/source/p/pysqlite/pysqlite-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python-setuptools
BuildRequires:  sqlite3-devel
Requires:       sqlite3
Provides:       python-sqlite = %{version}
Provides:       python2-pysqlite = %{version}
Provides:       python2-sqlite = %{version}
Obsoletes:      python-sqlite < %{version}
Provides:       python-sqlite2 = %{version}
Obsoletes:      python-sqlite2 < %{version}

%description
Python interface to SQLite 3

pysqlite is an interface to the SQLite 3.x embedded relational database engine.
It is almost fully compliant with the Python database API version 2.0 also
exposes the unique features of SQLite.

%prep
%setup -q -n pysqlite-%{version}

%build
CFLAGS="%{optflags}" %python2_build

%install
%python2_install
%fdupes %{buildroot}%{python2_sitearch}
rm -rf %{buildroot}%{_prefix}/pysqlite2-doc # Remove wrongly installed junk

%files
%license LICENSE
%{python2_sitearch}/*

%changelog
