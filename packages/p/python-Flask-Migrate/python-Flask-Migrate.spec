#
# spec file for package python-Flask-Migrate
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
Name:           python-Flask-Migrate
Version:        4.0.5
Release:        0
Summary:        SQLAlchemy database migrations for Flask applications using Alembic
License:        MIT
URL:            https://github.com/miguelgrinberg/flask-migrate/
Source:         https://github.com/miguelgrinberg/flask-migrate/archive/refs/tags/v%{version}.tar.gz#/Flask-Migrate-%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 0.9}
BuildRequires:  %{python_module Flask-SQLAlchemy >= 1.0}
BuildRequires:  %{python_module alembic >= 1.9.0}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.9
Requires:       python-Flask-SQLAlchemy >= 1.0
Requires:       python-alembic >= 1.9.0
BuildArch:      noarch
%python_subpackages

%description
Flask-Migrate is an extension that handles SQLAlchemy database migrations
for Flask applications using Alembic. The database operations are provided
as command line arguments for Flask-Script.

%prep
%autosetup -p1 -n Flask-Migrate-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/flask_migrate
%{python_sitelib}/Flask_Migrate-%{version}.dist-info

%changelog
