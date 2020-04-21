#
# spec file for package python-prometheus_client
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
%bcond_without python2
Name:           python-prometheus_client
Version:        0.7.1
Release:        0
Summary:        Python client for the Prometheus monitoring system
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/prometheus/client_python
Source:         https://github.com/prometheus/client_python/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-Twisted
Provides:       python-prometheus-client = %{version}-%{release}
Obsoletes:      python-prometheus-client < %{version}-%{release}
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-futures
%endif
%python_subpackages

%description
The official Python 2 and 3 client for Prometheus.

%prep
%setup -q -n client_python-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# some tests are currently broken in ppc64le
# see https://bugzilla.suse.com/show_bug.cgi?id=1164604
%pytest -k "not TestProcessCollector"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
