#
# spec file for package python-Flask-Admin
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
Name:           python-Flask-Admin
Version:        1.6.1
Release:        0
Summary:        Extensible admin interface framework for Flask
License:        BSD-3-Clause
URL:            https://github.com/flask-admin/flask-admin/
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Admin/Flask-Admin-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Flask-BabelEx has been firmly deprecated, switch to Babel
# directly.
Patch0:         switch-to-babel.patch
# cherry-picks from https://github.com/flask-admin/flask-admin/pull/2328 Support latest flask, sqlalchemy, flask-sqlalchemy and wtforms
Patch1:         model-from-model.patch
Patch2:         reverse-relation-for-model.patch
Patch3:         bytes-not-str.patch
BuildRequires:  %{python_module Flask >= 0.7}
BuildRequires:  %{python_module Flask-Babel}
BuildRequires:  %{python_module Flask-SQLAlchemy}
BuildRequires:  %{python_module Pillow >= 3.3.2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module SQLAlchemy-Utils}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module WTForms}
BuildRequires:  %{python_module arrow}
BuildRequires:  %{python_module colour}
BuildRequires:  %{python_module peewee}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requre}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.7
Requires:       python-SQLAlchemy
Requires:       python-WTForms
BuildArch:      noarch
%python_subpackages

%description
Flask-Admin is a Flask extension that lets the user add admin
interfaces to Flask applications.

It is inspired by the django-admin Python package, though the
developer has more control over the look, feel and functionality of
the resulting application.

%prep
%autosetup -p1 -n Flask-Admin-%{version}

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
%pytest -k 'not test_model and not test_inline_form_base_class and not test_safe_redirect'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/flask_admin
%{python_sitelib}/Flask_Admin-%{version}.dist-info

%changelog
