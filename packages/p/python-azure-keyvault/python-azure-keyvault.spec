#
# spec file for package python-azure-keyvault
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
Name:           python-azure-keyvault
Version:        4.1.0
Release:        0
Summary:        Microsoft Azure Key Vault Client Library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-keyvault/azure-keyvault-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-keyvault-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-keyvault-certificates >= 4.1
Requires:       python-azure-keyvault-keys >= 4.1
Requires:       python-azure-keyvault-nspkg >= 1.0.0
Requires:       python-azure-keyvault-secrets >= 4.1
Requires:       python-azure-nspkg >= 3.0.0
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Key Vault libraries bundle.

This package does not contain any code in itself. It installs a set
of packages that provide APIs for Key Vault operations:

- azure-keyvault-keys
- azure-keyvault-secrets
- azure-keyvault-certificates

%prep
%setup -q -n azure-keyvault-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-keyvault-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/keyvault/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/keyvault/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{python_sitelib}/azure_keyvault-*.egg-info

%changelog
