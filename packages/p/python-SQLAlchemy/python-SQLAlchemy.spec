#
# spec file for package python-SQLAlchemy
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-SQLAlchemy
Version:        1.3.23
Release:        0
Summary:        Database Abstraction Library
License:        MIT
URL:            https://www.sqlalchemy.org
Source:         https://files.pythonhosted.org/packages/source/S/SQLAlchemy/SQLAlchemy-%{version}.tar.gz
Source1:        SQLAlchemy.keyring
# PATCH-FIX-UPSTREAM tests_overcome_bpo42967.patch gh#sqlalchemy/sqlalchemy#5969 mcepl@suse.com
# over effects of bpo#42967, which forbade mixing amps and
# semicolons in query strings as separators.
Patch0:         tests_overcome_bpo42967.patch
# devel is needed for optional C extensions cprocessors.so, cresultproxy.so and cutils.so
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Provides:       python-sqlalchemy = %{version}
Obsoletes:      python-sqlalchemy < %{version}
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest >= 4.4.0}
BuildRequires:  %{python_module pytest-xdist}
# /SECTION
%ifpython2
Obsoletes:      %{oldpython}-sqlalchemy < %{version}
Provides:       %{oldpython}-sqlalchemy = %{version}
%endif
%python_subpackages

%description
SQLAlchemy is an Object Relational Mappper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually
as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

%package -n %{name}-doc
Summary:        Documentation for python-SQLAlchemy
Provides:       %{python_module SQLAlchemy-doc = %{version}}
BuildArch:      noarch

%description -n %{name}-doc
This package contains HTML documentation, including tutorials and API
reference for python-SQLAlchemy.

%prep
%autosetup -p1 -n SQLAlchemy-%{version}

rm -rf doc/build # Remove unnecessary scripts for building documentation
sed -i 's/\r$//' examples/dynamic_dict/dynamic_dict.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# One test fails on Python 3.6
# packaging.version.InvalidVersion: Invalid version: 'SQLAlchemy'
%pytest_arch -n auto -k 'not (test_parseconnect and CreateEngineTest and test_bad_args)'

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst README.dialects.rst README.unittests.rst
%{python_sitearch}/sqlalchemy/
%{python_sitearch}/SQLAlchemy-%{version}-py*.egg-info

%files -n %{name}-doc
%doc doc/
%doc examples/

%changelog
