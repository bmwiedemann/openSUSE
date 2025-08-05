#
# spec file for package python-azure-monitor-querymetrics
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-azure-monitor-querymetrics
Version:        1.0.0
Release:        0
Summary:        Microsoft Azure Monitor Query Metrics Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_monitor_querymetrics/azure_monitor_querymetrics-%{version}.tar.gz
BuildRequires:  %{python_module azure-monitor-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-monitor-nspkg >= 1.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-isodate >= 0.6.0
Requires:       (python-azure-core >= 1.28.0 with python-azure-core < 2.0.0)
Requires:       (python-typing_extensions >= 4.3.0 if python-base < 3.8)
Conflicts:      python-azure-sdk <= 2.0.0
BuildArch:      noarch

%python_subpackages

%description
The Azure Monitor Query Metrics client library enables you to perform read-only queries
against Azure Monitor's metrics data platform. It is designed for retrieving numerical
metrics from Azure resources, supporting scenarios such as monitoring, alerting, and
troubleshooting.

 * Metrics: Numeric data collected from resources at regular intervals, stored as time
   series. Metrics provide insights into resource health and performance, and are
   optimized for near real-time analysis.

This library interacts with the Azure Monitor Metrics Data Plane API, allowing you to query
metrics for multiple resources in a single request. For details on batch querying, see Batch
API migration guide.

%prep
%setup -q -n azure_monitor_querymetrics-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/monitor/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/monitor/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/monitor/querymetrics
%{python_sitelib}/azure_monitor_querymetrics-*.dist-info

%changelog
