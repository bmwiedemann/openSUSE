#
# spec file for package python-azure-security-attestation
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
Name:           python-azure-security-attestation
Version:        1.0.0
Release:        0
Summary:        Microsoft Azure Attestation Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-security-attestation/azure-security-attestation-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-security-nspkg >= 1.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-azure-security-nspkg >= 1.0.0
Requires:       python-cryptography >= 2.1.4
Requires:       python-msrest >= 0.6.21
Requires:       (python-azure-core >= 1.8.2 with python-azure-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-security-attestation <= 1.0.0
%endif
BuildArch:      noarch
%python_subpackages

%description
The Microsoft Azure Attestation (MAA) service is a unified solution for remotely verifying the
trustworthiness of a platform and integrity of the binaries running inside it. The service
supports attestation of the platforms backed by Trusted Platform Modules (TPMs) alongside the
ability to attest to the state of Trusted Execution Environments (TEEs) such as Intel(tm)
Software Guard Extensions (SGX) enclaves and Virtualization-based Security (VBS) enclaves.

Attestation is a process for demonstrating that software binaries were properly instantiated
on a trusted platform. Remote relying parties can then gain confidence that only such intended
software is running on trusted hardware. Azure Attestation is a unified customer-facing service
and framework for attestation.

Azure Attestation enables cutting-edge security paradigms such as Azure Confidential computing
and Intelligent Edge protection. Customers have been requesting the ability to independently
verify the location of a machine, the posture of a virtual machine (VM) on that machine, and
the environment within which enclaves are running on that VM. Azure Attestation will empower
these and many additional customer requests.

Azure Attestation receives evidence from compute entities, turns them into a set of claims,
validates them against configurable policies, and produces cryptographic proofs for claims-based
applications (for example, relying parties and auditing authorities).

This package has been tested with Python 2.7, 3.6 to 3.9.

%prep
%setup -q -n azure-security-attestation-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-security-attestation-%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/security/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/security/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/security/attestation
%{python_sitelib}/azure_security_attestation-*.dist-info

%changelog
