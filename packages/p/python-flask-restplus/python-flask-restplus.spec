#
# spec file for package python-flask-restplus
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
%bcond_without python2
Name:           python-flask-restplus
Version:        0.13.0
Release:        0
Summary:        Rest API development with Flask
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/noirbizarre/flask-restplus
Source:         https://github.com/noirbizarre/flask-restplus/archive/%{version}.tar.gz
Patch0:         pytest4.patch
Patch1:         001-Fix-content-type-assertion-for-werkzeug-1.0.patch
Patch2:         002-Update-cached_property-import-for-werkzeug-1.0.patch
# PATCH-FIX-UPSTREAM 003-Import-from-flask-scaffold.patch _endpoint_from_view_func moved to flask.scaffold after flask 2.0.0 https://github.com/pallets/flask/commit/9f7c602a84faa8371be4ece23e4405282d1283d2
Patch3:         003-Import-from-flask-scaffold.patch
# PATCH-FIX-UPSTREAM 004-Import-from-collections-abc.patch collections: remove deprecated aliases to ABC classes bpo#37324
Patch4:         004-Import-from-collections-abc.patch
BuildRequires:  %{python_module Flask >= 0.8}
BuildRequires:  %{python_module aniso8601 >= 0.82}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python2-enum34
BuildRequires:  python2-ipaddress
%endif
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
BuildRequires:  %{python_module pytest-benchmark >= 3.1.1}
BuildRequires:  %{python_module pytest-flask >= 0.10.0}
BuildRequires:  %{python_module pytest-mock >= 1.6.3}
BuildRequires:  %{python_module pytest}
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
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

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
