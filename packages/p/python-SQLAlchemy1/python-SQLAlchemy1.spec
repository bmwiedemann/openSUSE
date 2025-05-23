#
# spec file for package python-SQLAlchemy1
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


%define skip_python2 1
%define oldpython python
%{?sle15_python_module_pythons}
Name:           python-SQLAlchemy1
Version:        1.4.54
Release:        0
Summary:        Database Abstraction Library
License:        MIT
URL:            https://www.sqlalchemy.org
Source:         https://files.pythonhosted.org/packages/source/s/sqlalchemy/sqlalchemy-%{version}.tar.gz
Source1:        SQLAlchemy.keyring
# devel is needed for optional C extensions cprocessors.so, cresultproxy.so and cutils.so
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Requires:       python-greenlet
Provides:       python-SQLAlchemy = %{version}
Provides:       python-sqlalchemy = %{version}
Conflicts:      python-SQLAlchemy
%if %{python_version_nodots} < 38
Requires:       python-importlib-metadata
%endif
# SECTION test requirements
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pytest >= 4.4.0}
# /SECTION
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
%autosetup -p1 -n sqlalchemy-%{version}

rm -rf doc/build # Remove unnecessary scripts for building documentation
sed -i 's/\r$//' examples/dynamic_dict/dynamic_dict.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# One test fails on Python 3.6
# packaging.version.InvalidVersion: Invalid version: 'SQLAlchemy'
%pytest_arch -k 'not (test_parseconnect and CreateEngineTest and test_bad_args)'

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst README.dialects.rst README.unittests.rst
%{python_sitearch}/sqlalchemy/
%if 0%{?suse_version} > 1600
%{python_sitearch}/sqlalchemy-%{version}.dist-info
%else
%{python_sitearch}/SQLAlchemy-%{version}.dist-info
%endif

%files -n %{name}-doc
%doc doc/
%doc examples/

%changelog
