#
# spec file for package python-azure-healthinsights-cancerprofiling
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

%define realversion 1.0.0b1.post1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-azure-healthinsights-cancerprofiling
Version:        1.0.0~b1.post1
Release:        0
Summary:        Microsoft Azure Health Insights Cancer Profiling Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk
Source:         https://files.pythonhosted.org/packages/source/a/azure-healthinsights-cancerprofiling/azure-healthinsights-cancerprofiling-%{realversion}.zip
BuildRequires:  %{python_module azure-core >= 1.24.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module isodate >= 0.6.1}
BuildRequires:  %{python_module isodate < 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-core >= 1.24.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-isodate >= 0.6.1
Requires:       python-isodate < 1.0.0
Requires:       (python-typing_extensions >= 4.3.0 if python-base < 3.8)
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
Health Insights is an Azure Applied AI Service built with the Azure Cognitive
Services Framework, that leverages multiple Cognitive Services, Healthcare API
services and other Azure resources.

The Cancer Profiling model receives clinical records of oncology patients and
outputs cancer staging, such as clinical stage TNM categories and pathologic
stage TNM categories as well as tumor site, histology.

%prep
%setup -q -n azure-healthinsights-cancerprofiling-%{realversion}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%dir %{python_sitelib}/azure/healthinsights
%{python_sitelib}/azure/healthinsights/cancerprofiling
%{python_sitelib}/azure_healthinsights_cancerprofiling-*.egg-info

%changelog
