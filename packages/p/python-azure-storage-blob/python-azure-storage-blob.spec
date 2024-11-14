#
# spec file for package python-azure-storage-blob
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
Name:           python-azure-storage-blob
Version:        12.24.0
Release:        0
Summary:        Microsoft Azure Storage Blob Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_storage_blob/azure_storage_blob-%{version}.tar.gz
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-storage-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-common >= 1.1.5
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-azure-storage-nspkg >= 3.0.0
Requires:       python-cryptography >= 2.1.4
Requires:       python-isodate >= 0.6.1
Requires:       (python-azure-core >= 1.30.0 with python-azure-core < 2.0.0)
Requires:       (python-azure-storage-common >= 2.1.0 with python-azure-storage-common < 3.0.0)
Requires:       (python-typing_extensions >= 4.6.0)
%if "%{python_flavor}" == "python2"
Requires:       python-futures
%endif
Conflicts:      python-azure-sdk <= 2.0.0
Conflicts:      python-azure-storage <= 0.36.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-storage-blob < 12.19.0
%endif
BuildArch:      noarch

%python_subpackages

%description
Azure Blob storage is Microsoft's object storage solution for the cloud. Blob storage is optimized
for storing massive amounts of unstructured data, such as text or binary data.

Blob storage is ideal for:

* Serving images or documents directly to a browser
* Storing files for distributed access
* Streaming video and audio
* Storing data for backup and restore, disaster recovery, and archiving
* Storing data for analysis by an on-premises or Azure-hosted service

%prep
%setup -q -n azure_storage_blob-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/storage/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/storage/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/storage/blob
%{python_sitelib}/azure_storage_blob-*.dist-info

%changelog
