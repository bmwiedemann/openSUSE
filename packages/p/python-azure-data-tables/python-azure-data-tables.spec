#
# spec file for package python-azure-data-tables
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
Name:           python-azure-data-tables
Version:        12.0.0b2
Release:        0
Summary:        Microsoft Azure Azure Data Tables Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/table/azure-table
Source:         https://files.pythonhosted.org/packages/source/a/azure-data-tables/azure-data-tables-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-data-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-core >= 1.2.2
Requires:       python-azure-data-nspkg >= 1.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-msrest >= 0.6.10
%ifpython2
Requires:       python-enum34 >= 1.0.4
Requires:       python-futures
Requires:       python-typing
%endif
BuildArch:      noarch
%python_subpackages

%description
Azure Data Tables is a NoSQL data storage service that can be accessed from anywhere in the
world via authenticated calls using HTTP or HTTPS. Tables scales as needed to support the
amount of data inserted, and allow for the storing of data with non-complex accessing.
The Azure Data Tables client can be used to access Azure Storage or Cosmos accounts.

%prep
%setup -q -n azure-data-tables-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-data-tables-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/data/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/data/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/data/tables
%{python_sitelib}/azure_data_tables-*.egg-info

%changelog
