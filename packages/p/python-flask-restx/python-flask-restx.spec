#
# spec file for package python-flask-restx
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
%bcond_without python2
Name:           python-flask-restx
Version:        0.5.1
Release:        0
Summary:        Framework for fast, easy and documented API development with Flask
License:        BSD-3-Clause
Group:          Development/Languages/Python
#PATCH-FIX-UPSTREAM https://github.com/python-restx/flask-restx/pull/423 Handle change to Werkzeug 2.1.0 change to Request.get_json().
Patch0:         werkzeug.patch
#PATCH-FIX-UPSTREAM https://github.com/python-restx/flask-restx/pull/427 Handle Werkzeug 2.1.0 change to Response.autocorrect_location_header.
Patch1:         redirect.patch
#PATCH-FIX-UPSTREAM https://github.com/python-restx/flask-restx/pull/463 Fix missing parse_rule method
Patch2:         merged_pr_463.patch
URL:            https://github.com/python-restx/flask-restx
Source:         https://github.com/python-restx/flask-restx/archive/%{version}.tar.gz
BuildRequires:  %{python_module Faker}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module aniso8601}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-flask}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tzlocal}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python2-enum34
%endif
Requires:       python-Flask
Requires:       python-aniso8601
Requires:       python-jsonschema
Requires:       python-pytz
%ifpython2
Requires:       python2-enum34
%endif
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
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#python-restx/flask-restx#411 for LoggingTest.test_override_app_level
%pytest -k 'not (URLTest or EmailTest or test_handle_non_api_error or test_override_app_level)'

%files %{python_files}
%doc README.rst CONTRIBUTING.rst
%license LICENSE
%{python_sitelib}/*

%changelog
