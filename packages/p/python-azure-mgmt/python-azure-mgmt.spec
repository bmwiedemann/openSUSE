#
# spec file for package python-azure-mgmt
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
Name:           python-azure-mgmt
Version:        4.0.0
Release:        0
Summary:        Microsoft Azure Resource Management bundle
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-mgmt/azure-mgmt-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-mgmt-advisor < 5.0.0
Requires:       python-azure-mgmt-advisor >= 4.0.0
Requires:       python-azure-mgmt-alertsmanagement < 1.0.0
Requires:       python-azure-mgmt-alertsmanagement >= 0.2.0
Requires:       python-azure-mgmt-apimanagement < 1.0.0
Requires:       python-azure-mgmt-apimanagement >= 0.2.0
Requires:       python-azure-mgmt-appconfiguration < 1.0.0
Requires:       python-azure-mgmt-appconfiguration >= 0.6.0
Requires:       python-azure-mgmt-applicationinsights < 1.0.0
Requires:       python-azure-mgmt-applicationinsights >= 0.3.0
Requires:       python-azure-mgmt-appplatform < 2.0.0
Requires:       python-azure-mgmt-appplatform >= 1.0.0
Requires:       python-azure-mgmt-attestation < 1.0.0
Requires:       python-azure-mgmt-attestation >= 0.1.0
Requires:       python-azure-mgmt-authorization < 1.0.0
Requires:       python-azure-mgmt-authorization >= 0.61.0
Requires:       python-azure-mgmt-automation < 1.0.0
Requires:       python-azure-mgmt-automation >= 0.1.1
Requires:       python-azure-mgmt-batch < 10.0.0
Requires:       python-azure-mgmt-batch >= 9.0.0
Requires:       python-azure-mgmt-batchai < 3.0.0
Requires:       python-azure-mgmt-batchai >= 2.0.0
Requires:       python-azure-mgmt-billing < 1.0.0
Requires:       python-azure-mgmt-billing >= 0.2.0
Requires:       python-azure-mgmt-botservice < 1.0.0
Requires:       python-azure-mgmt-botservice >= 0.1.0
Requires:       python-azure-mgmt-cdn < 6.0.0
Requires:       python-azure-mgmt-cdn >= 5.1.0
Requires:       python-azure-mgmt-cognitiveservices < 7.0.0
Requires:       python-azure-mgmt-cognitiveservices >= 6.2.0
Requires:       python-azure-mgmt-commerce < 2.0.0
Requires:       python-azure-mgmt-commerce >= 1.0.1
Requires:       python-azure-mgmt-compute < 14.0.0
Requires:       python-azure-mgmt-compute >= 13.0.0
Requires:       python-azure-mgmt-consumption < 4.0.0
Requires:       python-azure-mgmt-consumption >= 3.0.0
Requires:       python-azure-mgmt-containerinstance < 3.0.0
Requires:       python-azure-mgmt-containerinstance >= 2.0.0
Requires:       python-azure-mgmt-containerregistry < 4.0.0
Requires:       python-azure-mgmt-containerregistry >= 3.0.0
Requires:       python-azure-mgmt-containerservice < 10.0.0
Requires:       python-azure-mgmt-containerservice >= 9.4.0
Requires:       python-azure-mgmt-core < 2.0.0
Requires:       python-azure-mgmt-core >= 1.0.0
Requires:       python-azure-mgmt-cosmosdb < 2.0.0
Requires:       python-azure-mgmt-cosmosdb >= 1.0.0
Requires:       python-azure-mgmt-costmanagement < 1.0.0
Requires:       python-azure-mgmt-costmanagement >= 0.2.0
Requires:       python-azure-mgmt-databricks < 1.0.0
Requires:       python-azure-mgmt-databricks >= 0.1.0
Requires:       python-azure-mgmt-datafactory < 1.0.0
Requires:       python-azure-mgmt-datafactory >= 0.13.0
Requires:       python-azure-mgmt-datalake-analytics < 1.0.0
Requires:       python-azure-mgmt-datalake-analytics >= 0.6.0
Requires:       python-azure-mgmt-datalake-store < 1.0.0
Requires:       python-azure-mgmt-datalake-store >= 0.5.0
Requires:       python-azure-mgmt-datamigration < 5.0.0
Requires:       python-azure-mgmt-datamigration >= 4.0.0
Requires:       python-azure-mgmt-datashare < 1.0.0
Requires:       python-azure-mgmt-datashare >= 0.2.0
Requires:       python-azure-mgmt-deploymentmanager < 1.0.0
Requires:       python-azure-mgmt-deploymentmanager >= 0.2.0
Requires:       python-azure-mgmt-devspaces < 1.0.0
Requires:       python-azure-mgmt-devspaces >= 0.1.0
Requires:       python-azure-mgmt-devtestlabs < 5.0.0
Requires:       python-azure-mgmt-devtestlabs >= 4.0.0
Requires:       python-azure-mgmt-dns < 4.0.0
Requires:       python-azure-mgmt-dns >= 3.0.0
Requires:       python-azure-mgmt-documentdb < 1.0.0
Requires:       python-azure-mgmt-documentdb >= 0.1.3
Requires:       python-azure-mgmt-edgegateway < 1.0.0
Requires:       python-azure-mgmt-edgegateway >= 0.1.0
Requires:       python-azure-mgmt-eventgrid < 4.0.0
Requires:       python-azure-mgmt-eventgrid >= 3.0.0rc8
Requires:       python-azure-mgmt-eventhub < 9.0.0
Requires:       python-azure-mgmt-eventhub >= 8.0.0
Requires:       python-azure-mgmt-frontdoor < 1.0.0
Requires:       python-azure-mgmt-frontdoor >= 0.3.0
Requires:       python-azure-mgmt-hanaonazure < 1.0.0
Requires:       python-azure-mgmt-hanaonazure >= 0.14.0
Requires:       python-azure-mgmt-hdinsight < 2.0.0
Requires:       python-azure-mgmt-hdinsight >= 1.7.0
Requires:       python-azure-mgmt-healthcareapis < 1.0.0
Requires:       python-azure-mgmt-healthcareapis >= 0.1.0
Requires:       python-azure-mgmt-hybridcompute < 2.0.0
Requires:       python-azure-mgmt-hybridcompute >= 1.0.0
Requires:       python-azure-mgmt-imagebuilder < 1.0.0
Requires:       python-azure-mgmt-imagebuilder >= 0.4.0
Requires:       python-azure-mgmt-iotcentral < 4.0.0
Requires:       python-azure-mgmt-iotcentral >= 3.1.0
Requires:       python-azure-mgmt-iothub < 1.0.0
Requires:       python-azure-mgmt-iothub >= 0.10.0
Requires:       python-azure-mgmt-iothubprovisioningservices < 1.0.0
Requires:       python-azure-mgmt-iothubprovisioningservices >= 0.2.0
Requires:       python-azure-mgmt-keyvault < 8.0.0
Requires:       python-azure-mgmt-keyvault >= 7.0.0
Requires:       python-azure-mgmt-kubernetesconfiguration < 1.0.0
Requires:       python-azure-mgmt-kubernetesconfiguration >= 0.2.0
Requires:       python-azure-mgmt-kusto < 1.0.0
Requires:       python-azure-mgmt-kusto >= 0.9.0
Requires:       python-azure-mgmt-labservices < 1.0.0
Requires:       python-azure-mgmt-labservices >= 0.1.1
Requires:       python-azure-mgmt-loganalytics < 1.0.0
Requires:       python-azure-mgmt-loganalytics >= 0.7.0
Requires:       python-azure-mgmt-logic < 5.0.0
Requires:       python-azure-mgmt-logic >= 4.0.0
Requires:       python-azure-mgmt-machinelearningcompute < 1.0.0
Requires:       python-azure-mgmt-machinelearningcompute >= 0.4.1
Requires:       python-azure-mgmt-machinelearningservices < 1.0.0
Requires:       python-azure-mgmt-machinelearningservices >= 0.1.0
Requires:       python-azure-mgmt-managedservices < 2.0.0
Requires:       python-azure-mgmt-managedservices >= 1.0.0
Requires:       python-azure-mgmt-managementgroups < 1.0.0
Requires:       python-azure-mgmt-managementgroups >= 0.1.0
Requires:       python-azure-mgmt-managementpartner < 1.0.0
Requires:       python-azure-mgmt-managementpartner >= 0.1.0
Requires:       python-azure-mgmt-maps < 1.0.0
Requires:       python-azure-mgmt-maps >= 0.1.0
Requires:       python-azure-mgmt-marketplaceordering < 1.0.0
Requires:       python-azure-mgmt-marketplaceordering >= 0.1.0
Requires:       python-azure-mgmt-media < 3.0.0
Requires:       python-azure-mgmt-media >= 2.1.0
Requires:       python-azure-mgmt-mixedreality < 1.0.0
Requires:       python-azure-mgmt-mixedreality >= 0.2.0
Requires:       python-azure-mgmt-monitor < 1.0.0
Requires:       python-azure-mgmt-monitor >= 0.11.0
Requires:       python-azure-mgmt-msi < 2.0.0
Requires:       python-azure-mgmt-msi >= 1.0.0
Requires:       python-azure-mgmt-netapp < 1.0.0
Requires:       python-azure-mgmt-netapp >= 0.12.0
Requires:       python-azure-mgmt-network < 17.0.0
Requires:       python-azure-mgmt-network >= 16.0.0
Requires:       python-azure-mgmt-notificationhubs < 3.0.0
Requires:       python-azure-mgmt-notificationhubs >= 2.0.0
Requires:       python-azure-mgmt-peering < 1.0.0
Requires:       python-azure-mgmt-peering >= 0.2.0
Requires:       python-azure-mgmt-policyinsights < 1.0.0
Requires:       python-azure-mgmt-policyinsights >= 0.5.0
Requires:       python-azure-mgmt-powerbiembedded < 3.0.0
Requires:       python-azure-mgmt-powerbiembedded >= 2.0.0
Requires:       python-azure-mgmt-privatedns < 1.0.0
Requires:       python-azure-mgmt-privatedns >= 0.1.0
Requires:       python-azure-mgmt-rdbms < 4.0.0
Requires:       python-azure-mgmt-rdbms >= 3.0.0
Requires:       python-azure-mgmt-recoveryservices < 1.0.0
Requires:       python-azure-mgmt-recoveryservices >= 0.5.0
Requires:       python-azure-mgmt-recoveryservicesbackup < 1.0.0
Requires:       python-azure-mgmt-recoveryservicesbackup >= 0.8.0
Requires:       python-azure-mgmt-redhatopenshift < 1.0.0
Requires:       python-azure-mgmt-redhatopenshift >= 0.1.0
Requires:       python-azure-mgmt-redis < 8.0.0
Requires:       python-azure-mgmt-redis >= 7.0.0rc1
Requires:       python-azure-mgmt-relay < 1.0.0
Requires:       python-azure-mgmt-relay >= 0.1.0
Requires:       python-azure-mgmt-reservations < 1.0.0
Requires:       python-azure-mgmt-reservations >= 0.8.0
Requires:       python-azure-mgmt-resource < 11.0.0
Requires:       python-azure-mgmt-resource >= 10.2.0
Requires:       python-azure-mgmt-resourcegraph < 3.0.0
Requires:       python-azure-mgmt-resourcegraph >= 2.0.0
Requires:       python-azure-mgmt-scheduler < 3.0.0
Requires:       python-azure-mgmt-scheduler >= 2.0.0
Requires:       python-azure-mgmt-search < 3.0.0
Requires:       python-azure-mgmt-search >= 2.0.0
Requires:       python-azure-mgmt-security < 1.0.0
Requires:       python-azure-mgmt-security >= 0.4.1
Requires:       python-azure-mgmt-serialconsole < 1.0.0
Requires:       python-azure-mgmt-serialconsole >= 0.1.0
Requires:       python-azure-mgmt-servermanager < 3.0.0
Requires:       python-azure-mgmt-servermanager >= 2.0.0
Requires:       python-azure-mgmt-servicebus < 1.0.0
Requires:       python-azure-mgmt-servicebus >= 0.5.3
Requires:       python-azure-mgmt-servicefabric < 1.0.0
Requires:       python-azure-mgmt-servicefabric >= 0.5.0
Requires:       python-azure-mgmt-signalr < 1.0.0
Requires:       python-azure-mgmt-signalr >= 0.4.0
Requires:       python-azure-mgmt-sql < 1.0.0
Requires:       python-azure-mgmt-sql >= 0.21.0
Requires:       python-azure-mgmt-sqlvirtualmachine < 1.0.0
Requires:       python-azure-mgmt-sqlvirtualmachine >= 0.5.0
Requires:       python-azure-mgmt-storage < 12.0.0
Requires:       python-azure-mgmt-storage >= 11.2.0
Requires:       python-azure-mgmt-storagecache < 1.0.0
Requires:       python-azure-mgmt-storagecache >= 0.3.0
Requires:       python-azure-mgmt-storageimportexport < 1.0.0
Requires:       python-azure-mgmt-storageimportexport >= 0.1.0
Requires:       python-azure-mgmt-storagesync < 1.0.0
Requires:       python-azure-mgmt-storagesync >= 0.2.0
Requires:       python-azure-mgmt-subscription < 1.0.0
Requires:       python-azure-mgmt-subscription >= 0.6.0
Requires:       python-azure-mgmt-synapse < 1.0.0
Requires:       python-azure-mgmt-synapse >= 0.3.0
Requires:       python-azure-mgmt-trafficmanager < 1.0.0
Requires:       python-azure-mgmt-trafficmanager >= 0.51.0
Requires:       python-azure-mgmt-web < 1.0.0
Requires:       python-azure-mgmt-web >= 0.47.0
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Resource Management bundle.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package does not contain any code in itself. It installs a set
of packages that provide management APIs for the various Azure services.

All packages in this bundle have been tested with Python 2.7, 3.4, 3.5, 3.6 and 3.7.

%prep
%setup -q -n azure-mgmt-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-mgmt-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/azure_mgmt-*.egg-info

%changelog
