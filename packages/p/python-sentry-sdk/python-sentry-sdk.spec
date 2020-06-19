#
# spec file for package python-sentry-sdk
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
# nothing provides python2-venusian >= 1.0 needed by python2-pyramid
%define skip_python2 1
Name:           python-sentry-sdk
Version:        0.14.4
Release:        0
Summary:        Python SDK for Sentry.io
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/getsentry/sentry-python
Source0:        https://github.com/getsentry/sentry-python/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 0.8}
BuildRequires:  %{python_module blinker >= 1.1}
BuildRequires:  %{python_module bottle >= 0.12.13}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module falcon >= 1.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urllib3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.8
Requires:       python-blinker >= 1.1
Requires:       python-bottle >= 0.12.13
Requires:       python-certifi
Requires:       python-falcon >= 1.4
Requires:       python-urllib3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pyramid}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rq}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module tox}
# /SECTION
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
# test_transport_works / test_transport_infinite_loop / test_simple_rate_limits/ test_data_category_limits / test_complex_limits_without_data_category stucks

# test_auto_enabling_integrations_catches_import_error asert False where False = ..., not sure
%pytest -k 'not (test_transport_works or test_auto_enabling_integrations_catches_import_error or test_filename or test_transport_infinite_loop or test_simple_rate_limits or test_data_category_limits or test_complex_limits_without_data_category)'

%files %{python_files}
%doc README.md CHANGES.md
%license LICENSE
%{python_sitelib}/*

%changelog
