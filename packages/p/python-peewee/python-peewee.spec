#
# spec file for package python-peewee
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
Name:           python-peewee
Version:        3.10.0
Release:        0
Summary:        An expressive ORM that supports multiple SQL backends
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/coleifer/peewee
Source:         https://files.pythonhosted.org/packages/source/p/peewee/peewee-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  pkgconfig(sqlite3)
%python_subpackages

%description
An expressive ORM that supports PostgreSQL, MySQL and SQLite.

%prep
%setup -q -n peewee-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone %{buildroot}%{_bindir}/pwiz.py
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.rst TODO.rst
%{_bindir}/pwiz.py-%{python_bin_suffix}
%python3_only %{_bindir}/pwiz.py
%{python_sitearch}/*

%changelog
