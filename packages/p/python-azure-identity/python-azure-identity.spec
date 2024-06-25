#
# spec file for package python-azure-identity
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
Name:           python-azure-identity
Version:        1.17.1
Release:        0
Summary:        Azure Identity client library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-identity/azure-identity-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-cryptography >= 2.5
Requires:       python-typing_extensions >= 4.0.0
Requires:       (python-azure-core >= 1.23.0 with python-azure-core < 2.0.0)
Requires:       (python-msal >= 1.24.0 with python-msal < 2.0.0)
Requires:       (python-msal-extensions >= 0.3.0 with python-msal-extensions < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-identity < 1.15.0
%endif
BuildArch:      noarch
%python_subpackages

%description
Azure Identity authenticating with Azure Active Directory for Azure SDK
libraries. It provides credentials Azure SDK clients can use to authenticate
their requests.

%prep
%setup -q -n azure-identity-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-identity-%{version}
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
%{python_sitelib}/azure/identity
%{python_sitelib}/azure_identity-*.dist-info

%changelog
