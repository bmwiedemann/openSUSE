#
# spec file for package python-SQLAlchemy
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-SQLAlchemy
Version:        2.0.31
Release:        0
Summary:        Database Abstraction Library
License:        MIT
URL:            https://www.sqlalchemy.org
Source:         https://files.pythonhosted.org/packages/source/S/SQLAlchemy/SQLAlchemy-%{version}.tar.gz
Source1:        SQLAlchemy.keyring
# devel is needed for optional C extensions cprocessors.so, cresultproxy.so and cutils.so
BuildRequires:  %{python_module Cython >= 3}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Requires:       python-greenlet > 0.4.17
Requires:       python-typing_extensions >= 4.2.0
Provides:       python-sqlalchemy = %{version}
Obsoletes:      python-sqlalchemy < %{version}
Conflicts:      python-SQLAlchemy1
%if %{python_version_nodots} < 38
Requires:       python-importlib-metadata
%endif
# SECTION test requirements
BuildRequires:  %{python_module greenlet > 0.4.17}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pytest >= 4.4.0}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module typing_extensions >= 4.2.0}
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
%autosetup -p1 -n SQLAlchemy-%{version}

rm -rf doc/build # Remove unnecessary scripts for building documentation
sed -i 's/\r$//' examples/dynamic_dict/dynamic_dict.py

find . -type f -name ".gitignore" -exec rm {} \;

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch -n2 -q --nomemory --notimingintensive --nomypy -k 'not (test_parseconnect and CreateEngineTest and test_bad_args)'

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst README.dialects.rst README.unittests.rst
%{python_sitearch}/sqlalchemy/
%{python_sitearch}/SQLAlchemy-%{version}.dist-info

%if 0%{?suse_version} > 1500
%files -n %{name}-doc
%endif
%doc doc/
%doc examples/

%changelog
