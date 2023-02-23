#
# spec file for package python-azure-storage-queue
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
Name:           python-azure-storage-queue
Version:        12.6.0
Release:        0
Summary:        Microsoft Azure Storage Queue Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-storage-queue/azure-storage-queue-%{version}.zip
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-storage-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-common >= 1.1.5
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.26.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-azure-storage-common < 3.0.0
Requires:       python-azure-storage-common >= 2.1.0
Requires:       python-azure-storage-nspkg >= 3.0.0
Requires:       python-cryptography >= 2.1.4
Requires:       python-isodate >= 0.6.1
Requires:       (python-typing_extensions >= 4.0.1 if python-base < 3.8)
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
%setup -q -n azure-storage-queue-%{version}

%build
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
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/storage/queue
%{python_sitelib}/azure_storage_queue-*.egg-info

%changelog
