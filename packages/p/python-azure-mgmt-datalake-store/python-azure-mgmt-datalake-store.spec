#
# spec file for package python-azure-mgmt-datalake-store
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


%define realversion 1.1.0b1

%{?sle15_python_module_pythons}
Name:           python-azure-mgmt-datalake-store
Version:        1.1.0~b1
Release:        0
Summary:        Microsoft Azure Data Lake Store Management Client Library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-mgmt-datalake-store/azure-mgmt-datalake-store-%{realversion}.zip
BuildRequires:  %{python_module azure-mgmt-datalake-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-mgmt-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-mgmt-datalake-nspkg >= 3.0.0
Requires:       python-azure-mgmt-nspkg >= 3.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-msrest >= 0.7.1
Requires:       (python-azure-common >= 1.1 with python-azure-common < 2.0.0)
Requires:       (python-azure-mgmt-core >= 1.3.2 with python-azure-mgmt-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-mgmt-datalake-store <= 1.0.0
%endif
BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Data Lake Store Management Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.4, 3.5 and 3.6.

%prep
%setup -q -n azure-mgmt-datalake-store-%{realversion}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/mgmt/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/mgmt/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/mgmt/datalake/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/mgmt/datalake/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/mgmt/datalake/store
%{python_sitelib}/azure_mgmt_datalake_store-*.dist-info

%changelog
