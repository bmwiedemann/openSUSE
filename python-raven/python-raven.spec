#
# spec file for package python-raven
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
Name:           python-raven
Version:        6.10.0
Release:        0
Summary:        A client for Sentry
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/getsentry/raven-python
Source:         https://files.pythonhosted.org/packages/source/r/raven/raven-%{version}.tar.gz
# https://github.com/getsentry/raven-python/issues/1284
Patch0:         remove-unittest2.patch
BuildRequires:  %{python_module Flask >= 0.8}
BuildRequires:  %{python_module Flask-Login >= 0.2.0}
BuildRequires:  %{python_module Logbook}
BuildRequires:  %{python_module Paste}
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module ZConfig}
BuildRequires:  %{python_module anyjson}
BuildRequires:  %{python_module blinker >= 1.1}
BuildRequires:  %{python_module bottle}
BuildRequires:  %{python_module celery >= 2.5}
BuildRequires:  %{python_module exam >= 0.5.2}
BuildRequires:  %{python_module flake8 >= 2.6}
BuildRequires:  %{python_module kombu}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pytest >= 3.0.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-flake8}
BuildRequires:  %{python_module pytest-pythonpath}
BuildRequires:  %{python_module pytest-timeout >= 0.4}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado >= 4.1}
BuildConflicts: %{python_module tornado >= 5}
BuildRequires:  %{python_module vine}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python-web.py
Recommends:     python-Flask >= 0.8
Recommends:     python-blinker >= 1.1
BuildArch:      noarch
%python_subpackages

%description
Raven is a Python client for Sentry. It supports many frameworks,
including Django, Flask, and Pylons. Raven also includes drop-in
support for any WSGI-compatible web application.

%prep
%setup -q -n raven-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -rf %{buildroot}/%{$python_sitelib}/raven/data/cacert.pem

# Tests are completely broken https://github.com/getsentry/raven-python/issues/1283
# %%check
# %%{python_expand export PYTHONPATH=%{buildroot}%%{$python_sitelib}
# py.test-%%{$python_bin_suffix} -k 'not (TornadoAsyncClientTestCase or TornadoTransportTests)'
# }

%files %{python_files}
%license LICENSE
%doc README.rst
%python3_only %{_bindir}/raven
%{python_sitelib}/*

%changelog
