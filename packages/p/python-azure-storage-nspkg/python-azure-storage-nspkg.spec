#
# spec file for package python-azure-storage-nspkg
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
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-storage-nspkg
Version:        3.1.0
Release:        0
Summary:        Microsoft Azure Storage namespace package
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-storage-nspkg/azure-storage-nspkg-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-nspkg >= 3.0.0
Conflicts:      python-azure-sdk <= 2.0.0
Conflicts:      python-azure-storage <= 0.36.0

BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Storage namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure.storage namespace.

%prep
%setup -q -n azure-storage-nspkg-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-storage-nspkg-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/azure/storage
%{python_sitelib}/azure_storage_nspkg-*.egg-info

%changelog
