#
# spec file for package python-azure-storage-common
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
Name:           python-azure-storage-common
Version:        2.1.0
Release:        0
Summary:        Microsoft Azure Storage Common Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-storage-common/azure-storage-common-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-storage-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-common >= 1.1.5
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-azure-storage-nspkg >= 3.0.0
Requires:       python-cryptography
Requires:       python-python-dateutil
Requires:       python-requests
Conflicts:      python-azure-sdk <= 2.0.0
Conflicts:      python-azure-storage <= 0.36.0

BuildArch:      noarch

%python_subpackages

%description
This project provides a client library in Python that makes it easy to
consume Microsoft Azure Storage services. For documentation please see
the Microsoft Azure `Python Developer Center`_ and our `API Reference`_
Page.

%prep
%setup -q -n azure-storage-common-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-storage-common-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/storage/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/storage/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/azure/storage/common
%{python_sitelib}/azure_storage_common-*.egg-info

%changelog
