#
# spec file for package python-sqlsoup
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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
Name:           python-sqlsoup
Version:        0.9.1
Release:        0
Summary:        A one step database access tool, built on the SQLAlchemy ORM
License:        MIT
URL:            https://bitbucket.org/zzzeek/sqlsoup
Source:         https://files.pythonhosted.org/packages/source/s/sqlsoup/sqlsoup-%{version}.tar.gz
Patch0:         sqlsoup-0.9.1-setup_test.patch
BuildRequires:  %{python_module SQLAlchemy >= 0.7.0}
BuildRequires:  %{python_module nose >= 0.11}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
SQLSoup provides a convenient way to map Python objects to relational database
tables, with no declarative code of any kind. It's built on top of the
SQLAlchemy ORM and provides a super-minimalistic interface to an existing
database.

%prep
%setup -q -n sqlsoup-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
