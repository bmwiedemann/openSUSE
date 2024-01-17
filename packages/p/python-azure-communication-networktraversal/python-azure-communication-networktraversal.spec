#
# spec file for package python-azure-communication-networktraversal
#
# Copyright (c) 2023 SUSE LLC
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


%define realversion 1.1.0b1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-communication-networktraversal
Version:        1.1.0~b1
Release:        0
Summary:        MS Azure Communication Network Traversal Service Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-communication-networktraversal/azure-communication-networktraversal-%{realversion}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-communication-nspkg >= 0.0.0b1}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-communication-nspkg >= 0.0.0b1
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.19.1
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-msrest >= 0.6.21
BuildArch:      noarch
%python_subpackages

%description
Azure Communication Network Traversal is managing TURN credentials for Azure Communication Services.

It will provide TURN credentials to a user.

%prep
%setup -q -n azure-communication-networktraversal-%{realversion}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-communication-networktraversal-%{realversion}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/communication/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/communication/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/communication/networktraversal
%{python_sitelib}/azure_communication_networktraversal-*.egg-info

%changelog
