#
# spec file for package python-azure-storage-blob-changefeed
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

%define realversion 12.0.0b5

%{?sle15_python_module_pythons}
Name:           python-azure-storage-blob-changefeed
Version:        12.0.0~b5
Release:        0
Summary:        Microsoft Azure Storage Blob ChangeFeed Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-storage-blob-changefeed/azure-storage-blob-changefeed-%{realversion}.tar.gz
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-storage-blob >= 12.19.1}
BuildRequires:  %{python_module azure-storage-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-azure-storage-nspkg >= 3.0.0
Requires:       (python-azure-storage-blob >= 12.19.1 with python-azure-storage-blob < 13.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-storage-blob-changefeed < 12.14.0
%endif
BuildArch:      noarch
%python_subpackages

%description
This preview package for Python enables users to get blob change feed events.
These events can be lazily generated, iterated by page, retrieved for a specific
time interval, or iterated from a specific continuation token.

%prep
%setup -q -n azure-storage-blob-changefeed-%{realversion}

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
%{python_sitelib}/azure/storage/blob/changefeed
%{python_sitelib}/azure_storage_blob_changefeed-*.dist-info

%changelog
