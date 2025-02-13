#
# spec file for package python-azure-communication-phonenumbers
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
Name:           python-azure-communication-phonenumbers
Version:        1.2.0
Release:        0
Summary:        Microsoft Azure Communication Phone Numbers Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_communication_phonenumbers/azure_communication_phonenumbers-%{version}.tar.gz
BuildRequires:  %{python_module azure-communication-nspkg >= 0.0.0b1}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-communication-nspkg >= 0.0.0b1
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-msrest >= 0.7.1
Requires:       (python-azure-core >= 1.28.0 with python-azure-core < 2.0.0)
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-communication-phonenumbers < 1.1.0
%endif
BuildArch:      noarch
%python_subpackages

%description
Azure Communication Phone Numbers Package client library for Python

Azure Communication Phone Numbers client package is used to administer Phone Numbers.

%prep
%setup -q -n azure_communication_phonenumbers-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/communication/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/communication/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/communication/phonenumbers
%{python_sitelib}/azure_communication_phonenumbers-*.dist-info

%changelog
