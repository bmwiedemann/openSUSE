#
# spec file for package python-azure-agrifood-farming
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
Name:           python-azure-agrifood-farming
Version:        1.0.0b2
Release:        0
Summary:        Microsoft Azure AgriFood Farming client library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-agrifood-farming/azure-agrifood-farming-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-agrifood-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-agrifood-nspkg >= 1.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-msrest >= 0.6.21
Requires:       python-six >= 1.11.0
Requires:       (python-azure-core >= 1.24.0 with python-azure-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-agrifood-farming < 1.0.0b2
%endif
BuildArch:      noarch

%python_subpackages

%description
FarmBeats is a B2B PaaS offering from Microsoft that makes it easy for AgriFood companies
to build intelligent digital agriculture solutions on Azure. FarmBeats allows users to
acquire, aggregate, and process agricultural data from various sources (farm equipment,
weather, satellite) without the need to invest in deep data engineering resources. Customers
can build SaaS solutions on top of FarmBeats and leverage first class support for model
building to generate insights at scale.

Use FarmBeats client library for Python to do the following.

 * Create & update farmers, farms, fields, seasonal fields and boundaries.
 * Ingest satellite and weather data for areas of interest.
 * Ingest farm operations data covering tilling, planting, harvesting
   and application of farm inputs.

%prep
%setup -q -n azure-agrifood-farming-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-agrifood-farming-%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/agrifood/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/agrifood/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/agrifood/farming
%{python_sitelib}/azure_agrifood_farming-*.dist-info

%changelog
