#
# spec file for package python-azure-storage-file-share
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
Name:           python-azure-storage-file-share
Version:        12.21.0
Release:        0
Summary:        Azure Storage File Share client library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_storage_file_share/azure_storage_file_share-%{version}.tar.gz
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-storage-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-azure-storage-nspkg >= 3.0.0
Requires:       python-cryptography >= 2.1.4
Requires:       python-isodate >= 0.6.1
Requires:       python-typing_extensions >= 4.6.0
Requires:       (python-azure-core >= 1.30.0 with python-azure-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-storage-file-share < 12.15.0
%endif
BuildArch:      noarch
%python_subpackages

%description
Azure File Share storage offers fully managed file shares in the cloud that are accessible via
the industry standard [Server Message Block (SMB) protocol](https://docs.microsoft.com/windows/
desktop/FileIO/microsoft-smb-protocol-and-cifs-protocol-overview). Azure file shares can be mounted
concurrently by cloud or on-premises deployments of Windows, Linux, and macOS. Additionally,
Azure file shares can be cached on Windows Servers with Azure File Sync for fast access near
where the data is being used.

Azure file shares can be used to:

 * Replace or supplement on-premises file servers
 * "Lift and shift" applications
 * Simplify cloud development with shared application settings,
   diagnostic share, and Dev/Test/Debug tools

%prep
%setup -q -n azure_storage_file_share-%{version}

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
%{python_sitelib}/azure/storage/fileshare
%{python_sitelib}/azure_storage_file_share-*.dist-info

%changelog
