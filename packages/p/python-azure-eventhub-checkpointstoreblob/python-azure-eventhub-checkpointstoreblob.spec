#
# spec file for package python-azure-eventhub-checkpointstoreblob
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
Name:           python-azure-eventhub-checkpointstoreblob
Version:        1.1.1
Release:        0
Summary:        Azure EventHubs Checkpoint Store client library for Python using Storage Blobs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-eventhub-checkpointstoreblob/azure-eventhub-checkpointstoreblob-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-core >= 1.2.2}
BuildRequires:  %{python_module azure-eventhub < 6.0.0}
BuildRequires:  %{python_module azure-eventhub >= 5.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module cryptography >= 2.1.4}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module msrest >= 0.6.10}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.2.2
Requires:       python-azure-eventhub < 6.0.0
Requires:       python-azure-eventhub >= 5.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-cryptography >= 2.1.4
Requires:       python-msrest >= 0.6.10

Conflicts:      python-azure-sdk <= 2.0.0
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
%setup -q -n azure-eventhub-checkpointstoreblob-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-eventhub-checkpointstoreblob-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/eventhub/extensions/checkpointstoreblob
%{python_sitelib}/azure_eventhub_checkpointstoreblob-*.egg-info

%changelog
