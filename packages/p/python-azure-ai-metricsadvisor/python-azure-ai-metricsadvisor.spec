#
# spec file for package python-azure-ai-metricsadvisor
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
Name:           python-azure-ai-metricsadvisor
Version:        1.0.0b1
Release:        0
Summary:        Microsoft Azure Metrics Advisor Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-ai-metricsadvisor/azure-ai-metricsadvisor-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-ai-nspkg >= 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-ai-nspkg >= 1.0.0
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.6.0
Requires:       python-msrest >= 0.6.12
Requires:       python-six >= 1.6
Conflicts:      python-azure-sdk <= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
Metrics Advisor is a scalable real-time time series monitoring, alerting, and root cause analysis platform.

Use Metrics Advisor to:

 * Analyze multi-dimensional data from multiple data sources
 * Identify and correlate anomalies
 * Configure and fine-tune the anomaly detection model used on your data
 * Diagnose anomalies and help with root cause analysis

%prep
%setup -q -n azure-ai-metricsadvisor-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-ai-metricsadvisor-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/ai/metricsadvisor
%{python_sitelib}/azure_ai_metricsadvisor-*.egg-info

%changelog
