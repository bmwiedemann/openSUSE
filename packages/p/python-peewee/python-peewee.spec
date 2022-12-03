#
# spec file for package python-peewee
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-peewee
Version:        3.15.4
Release:        0
Summary:        An expressive ORM that supports multiple SQL backends
License:        BSD-3-Clause
URL:            https://github.com/coleifer/peewee
Source:         https://github.com/coleifer/peewee/archive/refs/tags/%{version}.tar.gz#/peewee-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module PyMySQL}
BuildRequires:  %{python_module apsw}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  pkgconfig(sqlite3)
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
An expressive ORM that supports PostgreSQL, MySQL and SQLite.

%prep
%setup -q -n peewee-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pwiz.py
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch tests

%post
%python_install_alternative pwiz.py

%postun
%python_uninstall_alternative pwiz.py

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.rst TODO.rst
%{_bindir}/pwiz.py-%{python_bin_suffix}
%python_alternative %{_bindir}/pwiz.py
%{python_sitearch}/*

%changelog
