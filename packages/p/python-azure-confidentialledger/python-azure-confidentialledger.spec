#
# spec file for package python-azure-confidentialledger
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
Name:           python-azure-confidentialledger
Version:        1.1.1
Release:        0
Summary:        Microsoft Azure Confidential Ledger client library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-confidentialledger/azure-confidentialledger-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-cryptography >= 2.1.4
Requires:       (python-azure-core >= 1.24.0 with python-azure-core < 2.0.0)
Requires:       (python-isodate >= 0.6.1 with python-isodate < 1.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-confidentialledger < 1.1.1
%endif
BuildArch:      noarch

%python_subpackages

%description
Azure Confidential Ledger provides a service for logging to an immutable, tamper-proof
ledger. As part of the Azure Confidential Computing portfolio, Azure Confidential Ledger
runs in secure, hardware-based trusted execution environments, also known as enclaves.
It is built on Microsoft Research's Confidential Consortium Framework.

%prep
%setup -q -n azure-confidentialledger-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-confidentialledger-%{version}
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
%license LICENSE.txt
%{python_sitelib}/azure/confidentialledger
%{python_sitelib}/azure_confidentialledger-*.dist-info

%changelog
