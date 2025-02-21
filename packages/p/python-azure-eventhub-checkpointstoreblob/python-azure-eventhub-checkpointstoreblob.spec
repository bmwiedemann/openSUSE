#
# spec file for package python-azure-eventhub-checkpointstoreblob
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
Name:           python-azure-eventhub-checkpointstoreblob
Version:        1.2.0
Release:        0
Summary:        Azure EventHubs Checkpoint Store client library for Python using Storage Blobs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_eventhub_checkpointstoreblob/azure_eventhub_checkpointstoreblob-%{version}.tar.gz
BuildRequires:  %{python_module azure-eventhub < 6.0.0}
BuildRequires:  %{python_module azure-eventhub >= 5.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-nspkg >= 3.0.0
Requires:       (python-azure-eventhub >= 5.0.0 with python-azure-eventhub < 6.0.0)
Requires:       (python-azure-storage-blob >= 12.0.0 with python-azure-storage-blob < 13.0.0)

Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-eventhub-checkpointstoreblob <= 1.1.4
%endif
BuildArch:      noarch
%python_subpackages

%description
Azure EventHubs Checkpoint Store is used for storing checkpoints while processing events
from Azure Event Hubs. This Checkpoint Store package works as a plug-in package to
EventHubConsumerClient. It uses Azure Storage Blob as the persistent store for maintaining
checkpoints and partition ownership information.

Please note that this is a sync library, for async version of the Azure EventHubs Checkpoint
Store client library, please refer to the package azure-eventhub-checkpointstoreblob-aio.

%prep
%setup -q -n azure_eventhub_checkpointstoreblob-%{version}
# Remove vendoring of python-azure-storage-blob
sed -i 's/._vendor/azure/g' azure/eventhub/extensions/checkpointstoreblob/_blobstoragecs.py
rm -rf azure/eventhub/extensions/checkpointstoreblob/_vendor

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/eventhub/extensions/checkpointstoreblob
%{python_sitelib}/azure_eventhub_checkpointstoreblob-*.dist-info

%changelog
