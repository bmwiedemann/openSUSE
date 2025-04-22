#
# spec file for package python-azure-healthinsights-radiologyinsights
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
Name:           python-azure-healthinsights-radiologyinsights
Version:        1.0.0
Release:        0
Summary:        Microsoft Azure Health Insights Radiology Insights Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk
Source:         https://files.pythonhosted.org/packages/source/a/azure_healthinsights_radiologyinsights/azure_healthinsights_radiologyinsights-%{version}.tar.gz
BuildRequires:  %{python_module azure-core >= 1.24.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module isodate < 1.0.0}
BuildRequires:  %{python_module isodate >= 0.6.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-core >= 1.30.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       (python-isodate >= 0.6.1 with python-isodate < 1.0.0)
Requires:       python-typing_extensions >= 4.6.0
Conflicts:      python-azure-sdk <= 2.0.0
BuildArch:      noarch

%python_subpackages

%description
Health Insights is an Azure Applied AI Service built with the Azure Cognitive
Services Framework, that leverages multiple Cognitive Services, Healthcare API
services and other Azure resources.

Radiology Insights is a model that aims to provide quality checks as feedback
on errors and inconsistencies (mismatches) and ensures critical findings are
identified and communicated using the full context of the report. Follow-up
recommendations and clinical findings with measurements (sizes) documented by
the radiologist are also identified.

%prep
%setup -q -n azure_healthinsights_radiologyinsights-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%dir %{python_sitelib}/azure/healthinsights
%{python_sitelib}/azure/healthinsights/radiologyinsights
%{python_sitelib}/azure_healthinsights_radiologyinsights-*.dist-info

%changelog
