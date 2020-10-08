#
# spec file for package python-azure-datalake-store
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
Name:           python-azure-datalake-store
Version:        0.0.50
Release:        0
Summary:        Microsoft Azure Data Lake Store Client Library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-datalake-store/azure-datalake-store-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-adal >= 0.4.2
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-cffi
%ifpython2
Requires:       python-futures
%endif
Requires:       python-requests >= 2.20.0
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Data Lake Store Client Library.

Azure Data Lake Store Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.3, 3.4 and 3.5.

%prep
%setup -q -n azure-datalake-store-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-datalake-store-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/samples/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/samples/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc HISTORY.rst README.rst
%license LICENSE.txt
%{python_sitelib}/azure/datalake/
%{python_sitelib}/samples/
%{python_sitelib}/azure_datalake_store-*.egg-info

%changelog
