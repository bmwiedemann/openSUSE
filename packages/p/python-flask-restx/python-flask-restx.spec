#
# spec file for package python-flask-restx
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
Name:           python-flask-restx
Version:        0.2.0
Release:        0
Summary:        Framework for fast, easy and documented API development with Flask
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-restx/flask-restx
Source:         https://github.com/python-restx/flask-restx/archive/%{version}.tar.gz
BuildRequires:  %{python_module Faker}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module aniso8601}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-flask}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest < 6}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tzlocal}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
Requires:       python-aniso8601
Requires:       python-jsonschema
Requires:       python-pytz
BuildArch:      noarch
%python_subpackages

%description
Flask-RESTX is a community driven fork of Flask-RESTPlus. It is an extension for Flask
that adds support for quickly building REST APIs. It encourages best practices with
minimal setup. If you are familiar with Flask, Flask-RESTX should be easy to pick up.
It provides a coherent collection of decorators and tools to describe your API and expose
its documentation properly using Swagger.

%prep
%setup -q -n flask-restx-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not URLTest and not EmailTest'

%files %{python_files}
%doc README.rst CONTRIBUTING.rst
%license LICENSE
%{python_sitelib}/*

%changelog
