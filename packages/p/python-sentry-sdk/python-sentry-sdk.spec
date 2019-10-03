#
# spec file for package python-sentry-sdk
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
Name:           python-sentry-sdk
Version:        0.12.3
Release:        0
Summary:        Python SDK for Sentry.io
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/getsentry/sentry-python
Source0:        https://github.com/getsentry/sentry-python/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        pytest.ini
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
# BuildRequires:  %{python_module Werkzeug}
# BuildRequires:  %{python_module eventlet}
# BuildRequires:  %{python_module gevent}
# BuildRequires:  %{python_module hypothesis}
# BuildRequires:  %{python_module pyramid}
# BuildRequires:  %{python_module pytest-localserver}
# BuildRequires:  %{python_module pytest}
# BuildRequires:  %{python_module rq}
# BuildRequires:  %{python_module tornado}
# BuildRequires:  %{python_module tox}
# /SECTION
%python_subpackages

%description
A Python SDK for Sentry.io.
https://sentry.io/for/python/

%prep
%setup -q -n sentry-python-%{version}
# do not test integration:
rm -r tests/integrations
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS="-W ignore::DeprecationWarning"

cp %{SOURCE1} .

# a subset of tests fail on OBS
# - test_transport_works eventlet parameterized tests fail
# TODO disable since pytest does not respect filters
# %%pytest -k 'not (test_scope_initialized_before_client or test_configure_scope_unavailable or test_thread_local_is_patched or test_leaks or test_transport_works or test_iter_stacktraces)'

%files %{python_files}
%doc README.md CHANGES.md
%license LICENSE
%{python_sitelib}/*

%changelog
