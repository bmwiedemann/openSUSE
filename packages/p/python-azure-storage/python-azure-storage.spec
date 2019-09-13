#
# spec file for package python-azure-storage
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-azure-storage
Version:        0.36.0
Release:        0
Summary:        Microsoft Azure Storage Client Library
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-storage/azure-storage-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Provides:       python-azure-sdk-storage = %version
Obsoletes:      python-azure-sdk-storage < %version
BuildRequires:  %{python_module azure-nspkg}
Requires:       python-azure-common < 2.0.0
Requires:       python-azure-common >= 1.1.5
Requires:       python-azure-nspkg
Requires:       python-cryptography
Requires:       python-python-dateutil
Requires:       python-requests
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Storage Client Library.
 
Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.3, 3.4, 3.5 and 3.6.

%prep
%setup -q -n azure-storage-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-storage-%{version}
%python_build

%install
%python_install
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/tests/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/tests/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/azure/storage
%{python_sitelib}/azure_storage-*.egg-info

%changelog
