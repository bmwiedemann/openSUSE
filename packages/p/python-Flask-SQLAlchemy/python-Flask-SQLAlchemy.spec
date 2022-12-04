#
# spec file for package python-Flask-SQLAlchemy
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-Flask-SQLAlchemy
Version:        3.0.2
Release:        0
Summary:        SQLAlchemy support for Flask
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mitsuhiko/flask-sqlalchemy
Source:         https://files.pythonhosted.org/packages/source/F/Flask-SQLAlchemy/Flask-SQLAlchemy-%{version}.tar.gz
# BR krb5 - the test suite fails with krb5-mini (and users in any case will only ever get krb5, never krb5-mini)
BuildRequires:  krb5
BuildRequires:  %{python_module pdm-pep517}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 2.2
Requires:       python-SQLAlchemy >= 1.4.18
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask >= 2.2}
BuildRequires:  %{python_module SQLAlchemy >= 1.4.18}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Adds SQLAlchemy support to your Flask application.

%prep
%setup -q -n Flask-SQLAlchemy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python_sitelib}/flask_sqlalchemy/
%{python_sitelib}/Flask[-_]SQLAlchemy-%{version}.dist-info/

%changelog
