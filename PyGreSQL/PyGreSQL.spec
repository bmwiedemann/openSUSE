#
# spec file for package PyGreSQL
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           PyGreSQL
Url:            http://www.pygresql.org
Summary:        Python Client Library for PostgreSQL
Version:        4.1.1
Release:        1
License:        BSD-3-Clause
Group:          Productivity/Databases/Clients
Source0:        https://pypi.python.org/packages/source/P/PyGreSQL/%{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  openssl-devel
BuildRequires:  postgresql-devel
BuildRequires:  python-devel
Provides:       postgresql-python pg_pyth = %{version}
Obsoletes:      postgresql-python pg_pyth < %{version}

%description
PyGreSQL is a Python module that interfaces to a PostgreSQL database.
It embeds the PostgreSQL query library to allow easy use of PostgreSQL
features from a Python script.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install  --prefix=%{_prefix} --root=%buildroot

%files
%defattr(-,root,root,-)
%doc docs/* tutorial
%{python_sitearch}

%changelog
