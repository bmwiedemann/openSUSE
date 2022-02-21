#
# spec file for package python-flask-jwt-extended
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


%define skip_python2 1
Name:           python-flask-jwt-extended
Version:        4.3.1
Release:        0
Summary:        A Flask extension that provides JWT support
License:        MIT
URL:            https://github.com/vimalloc/flask-jwt-extended
Source:         https://files.pythonhosted.org/packages/source/F/Flask-JWT-Extended/Flask-JWT-Extended-%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 1.0}
BuildRequires:  %{python_module PyJWT >= 2.0}
BuildRequires:  %{python_module Werkzeug >= 0.14}
BuildRequires:  %{python_module cryptography >= 3.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 1.0
Requires:       python-PyJWT >= 2.0
Requires:       python-Werkzeug >= 0.14
Suggests:       python-cryptography >= 3.0
BuildArch:      noarch
%python_subpackages

%description
Flask-JWT-Extended not only adds support for using JSON Web Tokens
(JWT) to Flask for protecting views, but also many
(optional) features built in to make working with JSON
Web Tokens easier. These include:

- Support for adding custom claims to JSON Web Tokens
- Custom claims validation on received tokens
- Creating tokens from complex objects or complex object from received tokens
- Refresh tokens
- Token freshness and separate view decorators to only allow fresh tokens
- Token revoking/blacklisting
- Storing tokens in cookies and CSRF protection

%prep
%setup -q -n Flask-JWT-Extended-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/flask_jwt_extended

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%dir %{python_sitelib}/flask_jwt_extended
%{python_sitelib}/flask_jwt_extended/*
%{python_sitelib}/Flask_JWT_Extended-%{version}-py*.egg-info

%changelog
