#
# spec file for package python-psycopg2
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
Name:           python-psycopg2
Version:        2.8.6
Release:        0
Summary:        Python-PostgreSQL Database Adapter
License:        LGPL-3.0-or-later AND (LGPL-3.0-or-later OR ZPL-2.0) AND SUSE-GPL-2.0-with-openssl-exception
URL:            http://initd.org/psycopg/
Source:         https://files.pythonhosted.org/packages/source/p/psycopg2/psycopg2-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# newer postgresql packages pg_config in -server-devel
%if 0%{?sle_version} > 150100 || 0%{?suse_version} > 1500
BuildRequires:  postgresql-server-devel >= 9.1
%else
BuildRequires:  postgresql-devel >= 9.1
%endif
%if 0%{?suse_version} || 0%{?fedora_version} >= 24
Suggests:       postgresql-server
%endif
%python_subpackages

%description
psycopg2 is a PostgreSQL database adapter for the Python programming
language.

psycopg2 is different from the other database adapter because it was
designed for heavily multi-threaded applications that create and destroy
lots of cursors and make a conspicuous number of concurrent INSERTs or
UPDATEs. psycopg2 also provide asychronous operations and support
for coroutine libraries.

%prep
%setup -q -n psycopg2-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitearch}/psycopg2/tests # Don't package testsuite
%fdupes %{buildroot}/%{_mandir}  # Create symlinks for man pages
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# tests require running PGSQL
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m unittest discover

%files %{python_files}
%license LICENSE
%doc AUTHORS NEWS README.rst
%{python_sitearch}/psycopg2/
%{python_sitearch}/psycopg2-%{version}-py%{python_version}.egg-info

%changelog
