#
# spec file for package python-sentry-sdk
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


# nothing provides python2-venusian >= 1.0 needed by python2-pyramid
%{?sle15_python_module_pythons}
Name:           python-sentry-sdk
Version:        2.19.0
Release:        0
Summary:        Python SDK for Sentry.io
License:        BSD-2-Clause
URL:            https://github.com/getsentry/sentry-python
Source0:        https://github.com/getsentry/sentry-python/archive/%{version}/sentry-python-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.0}
BuildRequires:  %{python_module Flask >= 1.0}
BuildRequires:  %{python_module MarkupSafe}
BuildRequires:  %{python_module SQLAlchemy >= 1.2}
BuildRequires:  %{python_module aiohttp >= 3.5}
BuildRequires:  %{python_module asttokens}
BuildRequires:  %{python_module asyncpg >= 0.23}
BuildRequires:  %{python_module blinker >= 1.1}
BuildRequires:  %{python_module bottle >= 0.12.13}
BuildRequires:  %{python_module celery >= 4}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module executing}
BuildRequires:  %{python_module falcon >= 1.4}
BuildRequires:  %{python_module grpcio >= 1.39}
BuildRequires:  %{python_module httpx >= 0.16.0}
BuildRequires:  %{python_module loguru >= 0.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pymongo >= 3.1}
BuildRequires:  %{python_module rq >= 0.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module starlette >= 0.19.1}
BuildRequires:  %{python_module tornado >= 6}
BuildRequires:  %{python_module urllib3 >= 1.26.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module PySocks}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module fastapi >= 0.79.0}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module h2}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module jsonschema >= 3.2.0}
BuildRequires:  %{python_module pyramid}
BuildRequires:  %{python_module pyrsistent >= 0.16.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov >= 2.8.1}
BuildRequires:  %{python_module pytest-forked >= 1.4.0}
BuildRequires:  %{python_module pytest-localserver >= 0.5.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module responses}
# /SECTION
# SECTION test requirements - which rise up buildtime error or missing in openSUSE
#BuildRequires:  %%{python_module pytest-watch >= 4.2.0}
# /SECTION
# SECTION extra requirements - which rise up buildtime error or missing in openSUSE
#BuildRequires:  %%{python_module arq >= 0.23}
#BuildRequires:  %%{python_module pyspark >= 2.4.4}
#BuildRequires:  %%{python_module apache-beam >= 2.12}
#BuildRequires:  %%{python_module huey >= 2}
#BuildRequires:  %%{python_module pure_eval}
#BuildRequires:  %%{python_module chalice >= 1.16.0}
#BuildRequires:  %%{python_module starlite >= 1.48}
#BuildRequires:  %%{python_module quart >= 0.16.1}
#BuildRequires:  %%{python_module sanic >= 0.8}
#BuildRequires:  %%{python_module opentelemetry-distro >= 0.40b0}
#BuildRequires:  %%{python_module beam >= 2.12}
#BuildRequires:  %%{python_module chalice >= 1.16.0}
#BuildRequires:  %%{python_module clickhouse-driver >= 0.2.0}
# /SECTION
# Install requirements
Requires:       python-certifi
Requires:       python-urllib3 >= 1.26.11
# Extra requirements
Suggests:       python-Django >= 2.0
Suggests:       python-Flask >= 1.0
Suggests:       python-MarkupSafe
Suggests:       python-SQLAlchemy >= 1.2
Suggests:       python-aiohttp >= 3.5
Suggests:       python-asttokens
Suggests:       python-asyncpg >= 0.23
Suggests:       python-blinker >= 1.1
Suggests:       python-bottle >= 0.12.13
Suggests:       python-celery >= 4
Suggests:       python-executing
Suggests:       python-falcon >= 1.4
Suggests:       python-fastapi >= 0.79.0
Suggests:       python-grpcio >= 1.39
Suggests:       python-httpx >= 0.16.0
Suggests:       python-jsonschema
Suggests:       python-loguru >= 0.5
Suggests:       python-pymongo >= 3.1
Suggests:       python-rq >= 0.6
Suggests:       python-starlette >= 0.19.1
Suggests:       python-tornado >= 6
Suggests:       python-h2
# SECTION extra requirements - which rise up buildtime error or missing in openSUSE
#Requires:       python-sanic >= 0.8
#Requires:       python-apache-beam >= 2.12
#Requires:       python-huey >= 2
#Requires:       python-arq >= 0.23
#Requires:       python-pyspark >= 2.4.4
#Requires:       python-pure_eval
#Requires:       python-chalice >= 1.16.0
#Requires:       python-starlite >= 1.48
#Requires:       python-quart >= 0.16.1
#Requires:       python-sanic >= 0.8
#Requires:       python-opentelemetry-distro >= 0.40b0
#Requires:       python- beam >= 2.12}
#Requires:       python-chalice >= 1.16.0}
#Requires:       python-clickhouse-driver >= 0.2.0}
#Requires:       python-fastapi >= 0.79.0}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
A Python SDK for Sentry.io.
https://sentry.io/for/python/

%prep
%autosetup -p1 -n sentry-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# Fix python-bytecode-inconsistent-mtime
pushd %{buildroot}%{python_sitelib}
find . -name '*.pyc' -exec rm -f '{}' ';'
python%python_bin_suffix -m compileall *.py ';'
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTEST_ADDOPTS="-W ignore::DeprecationWarning"
export DJANGO_SETTINGS_MODULE=tests.conftest
# do not test integration (many package are missing at SUSE):
rm -r tests/integrations
# test_auto_enabling_integrations_catches_import_error asert False where False = ..., not sure
IGNORED_CHECKS="(test_default_release and test_utils)"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_new_scopes_compat_event"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_transport_works"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_auto_enabling_integrations_catches_import_error"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_socks_proxy or test_utils"
# https://github.com/getsentry/sentry-python/issues/3624
IGNORED_CHECKS="${IGNORED_CHECKS} or test_redis_disabled_when_not_installed"
# Related to this report gh#getsentry/sentry-python#576, looks like it
# freeze also with python 3.13
IGNORED_CHECKS="${IGNORED_CHECKS} or eventlet or greenlet"
%pytest -rs -k "not (${IGNORED_CHECKS})"

%files %{python_files}
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE
%{python_sitelib}/sentry_sdk
%{python_sitelib}/sentry_sdk-%{version}.dist-info

%changelog
