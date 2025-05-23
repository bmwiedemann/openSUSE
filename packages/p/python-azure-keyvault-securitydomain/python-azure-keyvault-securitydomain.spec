#
# spec file for package python-azure-keyvault-securitydomain
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

%define realversion 1.0.0b1

%{?sle15_python_module_pythons}
Name:           python-azure-keyvault-securitydomain
Version:        1.0.0~b1
Release:        0
Summary:        Microsoft Corporation Azure Keyvault Securitydomain Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_keyvault_securitydomain/azure_keyvault_securitydomain-%{realversion}.tar.gz
BuildRequires:  %{python_module azure-keyvault-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-keyvault-nspkg >= 1.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-isodate >= 0.6.1
Requires:       (python-azure-core >= 1.31.0 with python-azure-core < 2.0.0)
Requires:       python-typing_extensions >= 4.6.0
Conflicts:      python-azure-sdk <= 2.0.0
BuildArch:      noarch

%python_subpackages

%description
Azure Key Vault helps solve the following problems:

* Managed HSM security domain management (this library) - securely
  download and restore a managed HSM's security domain
* Cryptographic key management (azure-keyvault-keys)- create, store,
  and control access to the keys used to encrypt your data
* Secrets management (azure-keyvault-secrets) - securely store and
  control access to tokens, passwords, certificates, API keys, and
  other secrets
* Certificate management (azure-keyvault-certificates) - create, manage,
  and deploy public and private SSL/TLS certificates
* Vault administration (azure-keyvault-administration) - role-based access
  control (RBAC), and vault-level backup and restore options

%prep
%setup -q -n azure_keyvault_securitydomain-%{realversion}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/keyvault/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/keyvault/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/keyvault/securitydomain
%{python_sitelib}/azure_keyvault_securitydomain-*.dist-info

%changelog
