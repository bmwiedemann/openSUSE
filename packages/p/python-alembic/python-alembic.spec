#
# spec file for package python-alembic
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-alembic
Version:        1.15.2
Release:        0
Summary:        A database migration tool for SQLAlchemy
License:        MIT
URL:            https://github.com/sqlalchemy/alembic
Source0:        https://files.pythonhosted.org/packages/source/a/alembic/alembic-%{version}.tar.gz
BuildRequires:  %{python_module Mako}
BuildRequires:  %{python_module SQLAlchemy >= 2.0.0}
BuildRequires:  %{python_module backports.zoneinfo if %python-base < 3.9}
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.9}
BuildRequires:  %{python_module importlib-resources if %python-base < 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytzdata}
BuildRequires:  %{python_module typing-extensions >= 4}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-Mako
Requires:       python-SQLAlchemy >= 2.0.0
Requires:       python-typing-extensions >= 4
BuildArch:      noarch
%if 0%{?python_version_nodots} < 39
Requires:       python-importlib-metadata
Requires:       python-importlib-resources
%endif
%python_subpackages

%description
Alembic is a new database migrations tool, written by the author
of SQLAlchemy <http://www.sqlalchemy.org>.  A migrations tool
offers the following functionality:

* Can emit ALTER statements to a database in order to change
  the structure of tables and other constructs
* Provides a system whereby "migration scripts" may be constructed;
  each script indicates a particular series of steps that can "upgrade" a
  target database to a new version, and optionally a series of steps that can
  "downgrade" similarly, doing the same steps in reverse.
* Allows the scripts to execute in some sequential manner.

%prep
%setup -q -n alembic-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/alembic

%check
%pytest -n auto

%pre
%python_libalternatives_reset_alternative alembic

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%python_alternative %{_bindir}/alembic
%{python_sitelib}/alembic
%{python_sitelib}/alembic-%{version}*-info

%changelog
