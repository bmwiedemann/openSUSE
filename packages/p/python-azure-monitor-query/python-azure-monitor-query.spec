#
# spec file for package python-azure-monitor-query
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


%{?sle15_python_module_pythons}
Name:           python-azure-monitor-query
Version:        1.4.0
Release:        0
Summary:        Microsoft Azure Azure Monitor Query Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-monitor-query/azure-monitor-query-%{version}.tar.gz
Source1:        LICENSE.txt
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
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-monitor-query < 1.2.1
%endif
BuildArch:      noarch

%python_subpackages

%description
Azure Monitor helps you maximize the availability and performance of your applications and
services. It delivers a comprehensive solution for collecting, analyzing, and acting on
telemetry from your cloud and on-premises environments.

All data collected by Azure Monitor fits into one of two fundamental types, metrics and logs.
Metrics are numerical values that describe some aspect of a system at a particular point in
time. They are lightweight and capable of supporting near real-time scenarios. Logs contain
different kinds of data organized into records with different sets of properties for each
type. Telemetry such as events and traces are stored as logs in addition to performance data
so that it can all be combined for analysis.

%prep
%setup -q -n azure-monitor-query-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-monitor-query-%{version}
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
%license LICENSE.txt
%{python_sitelib}/azure/monitor/query
%{python_sitelib}/azure_monitor_query-*.dist-info

%changelog
