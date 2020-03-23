#
# spec file for package python-Flask-Migrate
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
%bcond_without python2
Name:           python-Flask-Migrate
Version:        2.5.3
Release:        0
Summary:        SQLAlchemy database migrations for Flask applications using Alembic
License:        MIT
URL:            https://github.com/miguelgrinberg/flask-migrate/
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Migrate/Flask-Migrate-%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 0.9}
BuildRequires:  %{python_module Flask-SQLAlchemy >= 1.0}
BuildRequires:  %{python_module Flask-Script >= 0.6}
BuildRequires:  %{python_module alembic >= 0.7}
BuildRequires:  %{python_module setuptools}
%if %{with python2}
BuildRequires:  python-pathlib
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.9
Requires:       python-Flask-SQLAlchemy >= 1.0
Requires:       python-Flask-Script >= 0.6
Requires:       python-alembic >= 0.7
BuildArch:      noarch
%python_subpackages

%description
Flask-Migrate is an extension that handles SQLAlchemy database migrations
for Flask applications using Alembic. The database operations are provided
as command line arguments for Flask-Script.

%prep
%setup -q -n Flask-Migrate-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_CTYPE=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover -v

%files %{python_files}
%doc README.md
%license LICENSE
%dir %{python_sitelib}/flask_migrate
%{python_sitelib}/flask_migrate/*
%{python_sitelib}/Flask_Migrate-%{version}-py*.egg-info

%changelog
