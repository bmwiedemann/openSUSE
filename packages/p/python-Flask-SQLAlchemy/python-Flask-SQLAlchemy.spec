#
# spec file for package python-Flask-SQLAlchemy
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
Name:           python-Flask-SQLAlchemy
Version:        3.1.1
Release:        0
Summary:        SQLAlchemy support for Flask
License:        BSD-3-Clause
URL:            https://github.com/mitsuhiko/flask-sqlalchemy
Source:         https://files.pythonhosted.org/packages/source/f/flask_sqlalchemy/flask_sqlalchemy-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#pallets-eco/flask-sqlalchemy#1308
Patch0:         stop-using-utcnow.patch
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
# BR krb5 - the test suite fails with krb5-mini (and users in any case will only ever get krb5, never krb5-mini)
BuildRequires:  krb5
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 2.2
Requires:       python-SQLAlchemy >= 2.0.16
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask >= 2.2}
BuildRequires:  %{python_module SQLAlchemy >= 2.0.16}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Adds SQLAlchemy support to your Flask application.

%prep
%autosetup -p1 -n flask_sqlalchemy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip tests that are broken with SQLAlchemy 2.0.36
# https://github.com/pallets-eco/flask-sqlalchemy/issues/1378
donttest=("-k" "not test_model_bind")
%pytest -W "ignore::ResourceWarning" "${donttest[@]}"

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python_sitelib}/flask_sqlalchemy
%{python_sitelib}/flask_sqlalchemy-%{version}.dist-info

%changelog
