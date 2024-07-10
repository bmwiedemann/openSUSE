#
# spec file for package python-azure-identity-broker
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
Name:           python-azure-identity-broker
Version:        1.1.0
Release:        0
Summary:        Microsoft Azure Identity Broker plugin for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-identity-broker/azure-identity-broker-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-identity < 2.0.0}
BuildRequires:  %{python_module azure-identity >= 1.14.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-nspkg >= 3.0.0
Requires:       (python-azure-identity >= 1.15.0 with python-azure-identity < 2.0.0)
Requires:       (python-msal >= 1.25.0 with python-msal < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-identity-broker < 1.0.0
%endif
BuildArch:      noarch
%python_subpackages

%description
This package extends the Azure Identity library by providing supplemental
credentials for authenticating via an authentication broker.

An authentication broker is an application that runs on a user’s machine that
manages the authentication handshakes and token maintenance for connected
accounts. Currently, only the Windows authentication broker, Web Account
Manager (WAM), is supported.

%prep
%setup -q -n azure-identity-broker-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-identity-broker-%{version}
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
%{python_sitelib}/azure/identity/broker
%{python_sitelib}/azure_identity_broker-*.dist-info

%changelog
