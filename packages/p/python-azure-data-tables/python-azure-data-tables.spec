#
# spec file for package python-azure-data-tables
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
Name:           python-azure-data-tables
Version:        12.6.0
Release:        0
Summary:        Microsoft Azure Azure Data Tables Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/table/azure-table
Source:         https://files.pythonhosted.org/packages/source/a/azure_data_tables/azure_data_tables-%{version}.tar.gz
BuildRequires:  %{python_module azure-data-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-data-nspkg >= 1.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       (python-azure-core >= 1.29.4 with python-azure-core < 2.0.0)
Requires:       (python-isodate >= 0.6.1 with python-isodate < 1.0.0)
Requires:       (python-typing_extensions >= 4.3.0 if python-base < 3.8)
Requires:       (python-yarl >= 1.0 with python-yarl < 2.0)
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-data-tables < 12.5.0
%endif
BuildArch:      noarch
%python_subpackages

%description
Azure Data Tables is a NoSQL data storage service that can be accessed from anywhere in the
world via authenticated calls using HTTP or HTTPS. Tables scales as needed to support the
amount of data inserted, and allow for the storing of data with non-complex accessing.
The Azure Data Tables client can be used to access Azure Storage or Cosmos accounts.

%prep
%setup -q -n azure_data_tables-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/data/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/data/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/data/tables
%{python_sitelib}/azure_data_tables-*.dist-info

%changelog
