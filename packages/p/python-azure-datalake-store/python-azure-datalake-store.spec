#
# spec file for package python-azure-datalake-store
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
Name:           python-azure-datalake-store
Version:        1.0.1
Release:        0
Summary:        Microsoft Azure Data Lake Store Client Library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_datalake_store/azure_datalake_store-%{version}.tar.gz
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-cffi
Requires:       python-requests >= 2.20.0
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-datalake-store < 0.0.53
%endif
BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Data Lake Store Client Library.

Azure Data Lake Store Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.3, 3.4 and 3.5.

%prep
%setup -q -n azure_datalake_store-%{version}
rm -rf samples

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/samples/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/samples/__pycache__
}

%files %{python_files}
%doc HISTORY.rst README.rst
%license License.txt
%{python_sitelib}/azure/datalake/
%{python_sitelib}/azure_datalake_store-*.dist-info

%changelog
