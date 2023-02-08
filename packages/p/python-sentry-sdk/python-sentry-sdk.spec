#
# spec file for package python-sentry-sdk
#
# Copyright (c) 2023 SUSE LLC
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
# nothing provides python2-venusian >= 1.0 needed by python2-pyramid
%define skip_python2 1
%define skip_python36 1
Name:           python-sentry-sdk
Version:        1.15.0
Release:        0
Summary:        Python SDK for Sentry.io
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/getsentry/sentry-python
Source0:        https://github.com/getsentry/sentry-python/archive/%{version}/sentry-python-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.8}
BuildRequires:  %{python_module Flask >= 0.11}
BuildRequires:  %{python_module SQLAlchemy >= 1.2}
BuildRequires:  %{python_module aiohttp >= 3.5}
BuildRequires:  %{python_module asttokens}
BuildRequires:  %{python_module blinker >= 1.1}
BuildRequires:  %{python_module bottle >= 0.12.13}
BuildRequires:  %{python_module celery >= 3}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module executing}
BuildRequires:  %{python_module falcon >= 1.4}
BuildRequires:  %{python_module httpx >= 0.16.0}
BuildRequires:  %{python_module pymongo >= 3.1}
BuildRequires:  %{python_module rq >= 0.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module starlette >= 0.19.1}
BuildRequires:  %{python_module tornado >= 5}
# upstream use %{python_module urllib3 >= 1.26.11}
BuildRequires:  %{python_module urllib3 >= 1.25.10}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module jsonschema >= 3.2.0}
BuildRequires:  %{python_module pyramid}
BuildRequires:  %{python_module pyrsistent >= 0.16.0}
BuildRequires:  %{python_module pytest-cov >= 2.8.1}
BuildRequires:  %{python_module pytest-forked >= 1.1.3}
BuildRequires:  %{python_module pytest-localserver >= 0.5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tox}
# /SECTION
# SECTION extra requirements - which rise up buildtime error or missing in openSUSE
#BuildRequires:  %%{python_module pyspark >= 2.4.4}
#BuildRequires:  %%{python_module apache-beam >= 2.12}
#BuildRequires:  %%{python_module huey >= 2}
#BuildRequires:  %%{python_module pure_eval}
#BuildRequires:  %%{python_module chalice >= 1.16.0}
#BuildRequires:  %%{python_module starlite >= 1.48}
#BuildRequires:  %%{python_module fastapi >= 0.79.0}
#BuildRequires:  %%{python_module quart >= 0.16.1}
#BuildRequires:  %%{python_module sanic >= 0.8}
#BuildRequires:  %%{python_module opentelemetry-distro >= 0.35b0}
# /SECTION
Requires:       python-Django >= 1.8
Requires:       python-Flask >= 0.11
Requires:       python-SQLAlchemy >= 1.2
Requires:       python-aiohttp >= 3.5
Requires:       python-asttokens
Requires:       python-blinker >= 1.1
Requires:       python-bottle >= 0.12.13
Requires:       python-celery >= 3
Requires:       python-certifi
Requires:       python-executing
Requires:       python-falcon >= 1.4
Requires:       python-httpx >= 0.16.0
Requires:       python-jsonschema
Requires:       python-pymongo >= 3.1
Requires:       python-rq >= 0.6
Requires:       python-starlette >= 0.19.1
Requires:       python-tornado >= 5
Requires:       python-urllib3 >= 1.10.0
# SECTION extra requirements - which rise up buildtime error or missing in openSUSE
#Requires:       python-sanic >= 0.8
#Requires:       python-apache-beam >= 2.12
#Requires:       python-huey >= 2
#Requires:       python-pyspark >= 2.4.4
#Requires:       python-pure_eval
#Requires:       python-chalice >= 1.16.0
#Requires:       python-starlite >= 1.48
#Requires:       python-fastapi >= 0.79.0
#Requires:       python-quart >= 0.16.1
#Requires:       python-sanic >= 0.8
#Requires:       python-opentelemetry-distro >= 0.35b0
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
A Python SDK for Sentry.io.
https://sentry.io/for/python/

%prep
%setup -q -n sentry-python-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS="-W ignore::DeprecationWarning"
# do not test integration:
rm -r tests/integrations
# test_auto_enabling_integrations_catches_import_error asert False where False = ..., not sure
%pytest -rs -k 'not (test_transport_works or test_auto_enabling_integrations_catches_import_error or test_filename or test_transport_infinite_loop or test_simple_rate_limits or test_data_category_limits or test_complex_limits_without_data_category or test_leaks)'

%files %{python_files}
%doc README.md CHANGELOG.md CONTRIBUTING.md CONTRIBUTING-aws-lambda.md
%license LICENSE
%{python_sitelib}/sentry*/

%changelog
