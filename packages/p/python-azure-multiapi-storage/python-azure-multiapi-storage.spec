#
# spec file for package python-azure-multiapi-storage
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-multiapi-storage
Version:        1.0.0
Release:        0
Summary:        Microsoft Azure Storage Client Library for Python - with Multi API version Support
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-multiapi-storage/azure-multiapi-storage-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-common
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.10.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-cryptography >= 2.1.4
Requires:       python-msrest >= 0.6.18
Requires:       python-python-dateutil
Requires:       python-requests
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
Microsoft Azure Storage Client Library for Python - with Multi API version Support

Handles multi-API versions of Azure Storage Data Plane originally from https://github.com/Azure/azure-storage-python.

**NOTE:**

- This is not an official Azure Storage SDK.

- It is used by https://github.com/Azure/azure-cli to support multiple API versions.

- The official Azure Storage SDK is at https://github.com/Azure/azure-storage-python.

%prep
%setup -q -n azure-multiapi-storage-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-multiapi-storage-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/azure/multiapi
%{python_sitelib}/azure_multiapi_storage-*.egg-info

%changelog
