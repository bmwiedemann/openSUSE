#
# spec file for package python-Flask-Admin
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-Flask-Admin
Version:        2.2.0
Release:        0
Summary:        Extensible admin interface framework for Flask
License:        BSD-3-Clause
URL:            https://github.com/flask-admin/flask-admin/
Source:         https://files.pythonhosted.org/packages/source/f/flask_admin/flask_admin-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
# Test requirements
BuildRequires:  %{python_module Flask >= 2.0}
BuildRequires:  %{python_module Flask-Babel >= 3.0.1}
BuildRequires:  %{python_module Flask-SQLAlchemy >= 3}
BuildRequires:  %{python_module Flask-SQLAlchemy-Lite}
BuildRequires:  %{python_module Jinja2 >= 3.0}
BuildRequires:  %{python_module MarkupSafe >= 2.0}
BuildRequires:  %{python_module Pillow >= 10}
BuildRequires:  %{python_module SQLAlchemy-Utils >= 0.38}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module WTForms >= 2.3}
BuildRequires:  %{python_module Werkzeug >= 2.0}
BuildRequires:  %{python_module arrow >= 0.14}
BuildRequires:  %{python_module azure-storage-blob >= 12}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module boto3 >= 1.33}
BuildRequires:  %{python_module colour >= 0.1.5}
BuildRequires:  %{python_module moto}
BuildRequires:  %{python_module peewee >= 3.14}
BuildRequires:  %{python_module pymongo >= 3.10}
BuildRequires:  %{python_module pytest-recording}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tablib >= 3}
BuildRequires:  %{python_module wtf-peewee >= 3.0.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 2.0
Requires:       python-Jinja2 >= 3.0
Requires:       python-MarkupSafe >= 2.0
Requires:       python-SQLAlchemy
Requires:       python-WTForms >= 2.3
Requires:       python-Werkzeug >= 2.0
Recommends:     python-Flask-SQLAlchemy >= 3
Recommends:     python-Flask-SQLAlchemy-Lite
Recommends:     python-Pillow >= 10
Recommends:     python-SQLAlchemy >= 1.4
Recommends:     python-SQLAlchemy-Utils >= 0.38
Recommends:     python-arrow >= 0.14
Recommends:     python-azure-storage-blob >= 12
Recommends:     python-boto3 >= 1.33
Recommends:     python-colour >= 0.1.5
Recommends:     python-peewee >= 3.14
Recommends:     python-pymongo >= 3.10
Recommends:     python-tablib >= 3
Recommends:     python-wtf-peewee >= 3.0.4
BuildArch:      noarch
%python_subpackages

%description
Flask-Admin is a Flask extension that lets the user add admin
interfaces to Flask applications.

It is inspired by the django-admin Python package, though the
developer has more control over the look, feel and functionality of
the resulting application.

%prep
%autosetup -p1 -n flask_admin-%{version}

# remove contrib tests that pull in too many dependencies
rm -rf flask_admin/tests/geoa
rm -rf flask_admin/tests/{mongoengine,pymongo}
rm -rf flask_admin/tests/peeweemodel
rm -f flask_admin/tests/sqla/test_postgres.py
# these tests try to write to protected dirs in the OBS
rm -f flask_admin/tests/test_form_upload.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="test_modal_edit_bs4 or test_file_admin_edit or test_file_admin"
%pytest --block-network -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/flask_admin
%{python_sitelib}/flask_admin-%{version}.dist-info

%changelog
