#
# spec file for package python-prometheus-client
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


%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-prometheus-client
Version:        0.17.0
Release:        0
Summary:        Python client for the Prometheus monitoring system
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/prometheus/client_python
Source:         https://github.com/prometheus/client_python/archive/v%{version}.tar.gz
%if 0%{suse_version} >= 1550
# we disable testing the optional Twisted integration on older versions because that dependency tree is troublesome
BuildRequires:  %{python_module Twisted}
%endif
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-Twisted
Provides:       python-prometheus_client = %{version}-%{release}
Obsoletes:      python-prometheus_client < %{version}-%{release}
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-futures
%endif
%python_subpackages

%description
The official Python 2 and 3 client for Prometheus.

%prep
%autosetup -p1 -n client_python-%{version}

sed -i -e '1{/\/usr\/bin\/python/d}' \
    prometheus_client/__init__.py \
    prometheus_client/bridge/graphite.py \
    prometheus_client/openmetrics/exposition.py \
    prometheus_client/openmetrics/parser.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/prometheus_client
%{python_sitelib}/prometheus_client-%{version}*-info

%changelog
