#
# spec file for package python-flask-restplus
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without test
Name:           python-flask-restplus
Version:        0.13.0
Release:        0
Summary:        Rest API development with Flask
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/noirbizarre/flask-restplus
Source:         https://github.com/noirbizarre/flask-restplus/archive/%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 0.8}
BuildRequires:  %{python_module aniso8601 >= 0.82}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-enum34
BuildRequires:  python2-ipaddress
Requires:       python-Flask >= 0.8
Requires:       python-aniso8601 >= 0.82
Requires:       python-jsonschema
Requires:       python-pytz
Requires:       python-six >= 1.3.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Faker >= 0.7.3}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module mock >= 2.0.0}
BuildRequires:  %{python_module pytest < 4.0}
BuildRequires:  %{python_module pytest-benchmark >= 3.1.1}
BuildRequires:  %{python_module pytest-flask >= 0.10.0}
BuildRequires:  %{python_module pytest-mock >= 1.6.3}
BuildRequires:  %{python_module tzlocal}
%endif
%ifpython2
Requires:       python2-enum34
Requires:       python2-ipaddress
%endif
%python_subpackages

%description
Flask-RESTPlus is an extension for Flask that adds support for
building REST APIs. It provides a collection of decorators and tools
to describe APIs and to expose their documentation using Swagger.

%prep
%setup -q -n flask-restplus-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/flask_restplus

%check
%if %{with test}
# Skip tests that require networking
%pytest -k 'not URLTest and not EmailTest'
%endif

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/*

%changelog
