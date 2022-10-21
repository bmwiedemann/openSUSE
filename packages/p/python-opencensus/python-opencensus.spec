#
# spec file
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_without python2
Name:           python-opencensus%{psuffix}
Version:        0.11.0
Release:        0
Summary:        A stats collection and distributed tracing framework
License:        Apache-2.0
URL:            https://github.com/census-instrumentation/opencensus-python
Source:         https://github.com/census-instrumentation/opencensus-python/archive/v%{version}.tar.gz#/opencensus-python-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM opencensus-pr1002-remove-mock.patch -- gh#census-instrumentation/opencensus-python#1002
Patch0:         opencensus-pr1002-remove-mock.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-core < 3.0.0
Requires:       python-google-api-core >= 1.0.0
Requires:       python-opencensus-context >= 0.1.3
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module google-api-core >= 1.0.0}
BuildRequires:  %{python_module opencensus >= %{version}}
BuildRequires:  %{python_module opencensus-context >= 0.1.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module retrying}
%if %{with python2}
BuildRequires:  python-mock
BuildRequires:  python-unittest2
%endif
%endif
%python_subpackages

%description
OpenCensus - A stats collection and distributed tracing framework

OpenCensus provides a framework to measure a server's resource usage
and collect performance stats. This repository contains Python related
utilities and supporting software needed by OpenCensus.

%prep
%autosetup -p1 -n opencensus-python-%{version}
# do not hardcode versions
sed -i -e 's:==:>=:g' setup.py

%build
%python_build

%install
%if !%{with test}
%python_install
# add ext infrastructure
%python_expand mkdir %{buildroot}%{$python_sitelib}/opencensus/ext/
%python_expand cp %{buildroot}%{$python_sitelib}/opencensus/__init__* %{buildroot}%{$python_sitelib}/opencensus/ext
%python_expand [ -e %{buildroot}%{$python_sitelib}/opencensus/__pycache* ] && cp -r %{buildroot}%{$python_sitelib}/opencensus/__pycache* %{buildroot}%{$python_sitelib}/opencensus/ext

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# recursion error in mock != 3; gh#census-instrumentation/opencensus-python#868
donttest="TestGetExporterThreadPeriodic and (test_multiple_producers or test_threaded_export)"
%pytest tests/unit -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/opencensus
%{python_sitelib}/opencensus-%{version}*-info
%endif

%changelog
