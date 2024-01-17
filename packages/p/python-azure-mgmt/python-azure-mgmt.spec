#
# spec file for package python-azure-mgmt
#
# Copyright (c) 2022 SUSE LLC
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
Requires:       python-azure-mgmt-advisor
Requires:       python-azure-mgmt-agfood
Requires:       python-azure-mgmt-agrifood
Requires:       python-azure-mgmt-alertsmanagement
Requires:       python-azure-mgmt-apimanagement
Requires:       python-azure-mgmt-app
Requires:       python-azure-mgmt-appconfiguration
Requires:       python-azure-mgmt-applicationinsights
Requires:       python-azure-mgmt-appplatform
Requires:       python-azure-mgmt-attestation
Requires:       python-azure-mgmt-authorization
Requires:       python-azure-mgmt-automanage
Requires:       python-azure-mgmt-automation
Requires:       python-azure-mgmt-avs
Requires:       python-azure-mgmt-azureadb2c
Requires:       python-azure-mgmt-azurestack
Requires:       python-azure-mgmt-azurestackhci
Requires:       python-azure-mgmt-baremetalinfrastructure
Requires:       python-azure-mgmt-batch
Requires:       python-azure-mgmt-batchai
Requires:       python-azure-mgmt-billing
Requires:       python-azure-mgmt-botservice
Requires:       python-azure-mgmt-cdn
Requires:       python-azure-mgmt-chaos
Requires:       python-azure-mgmt-cognitiveservices
Requires:       python-azure-mgmt-commerce
Requires:       python-azure-mgmt-communication
Requires:       python-azure-mgmt-compute
Requires:       python-azure-mgmt-confluent
Requires:       python-azure-mgmt-connectedvmware
Requires:       python-azure-mgmt-consumption
Requires:       python-azure-mgmt-containerinstance
Requires:       python-azure-mgmt-containerregistry
Requires:       python-azure-mgmt-containerservice
Requires:       python-azure-mgmt-core
Requires:       python-azure-mgmt-cosmosdb
Requires:       python-azure-mgmt-costmanagement
Requires:       python-azure-mgmt-customproviders
Requires:       python-azure-mgmt-dashboard
Requires:       python-azure-mgmt-databox
Requires:       python-azure-mgmt-databoxedge
Requires:       python-azure-mgmt-databricks
Requires:       python-azure-mgmt-datadog
Requires:       python-azure-mgmt-datafactory
Requires:       python-azure-mgmt-datalake-analytics
Requires:       python-azure-mgmt-datalake-nspkg
Requires:       python-azure-mgmt-datalake-store
Requires:       python-azure-mgmt-datamigration
Requires:       python-azure-mgmt-dataprotection
Requires:       python-azure-mgmt-datashare
Requires:       python-azure-mgmt-deploymentmanager
Requires:       python-azure-mgmt-deviceupdate
Requires:       python-azure-mgmt-devspaces
Requires:       python-azure-mgmt-devtestlabs
Requires:       python-azure-mgmt-digitaltwins
Requires:       python-azure-mgmt-dns
Requires:       python-azure-mgmt-documentdb
Requires:       python-azure-mgmt-edgegateway
Requires:       python-azure-mgmt-edgeorder
Requires:       python-azure-mgmt-elastic
Requires:       python-azure-mgmt-eventgrid
Requires:       python-azure-mgmt-eventhub
Requires:       python-azure-mgmt-extendedlocation
Requires:       python-azure-mgmt-fluidrelay
Requires:       python-azure-mgmt-frontdoor
Requires:       python-azure-mgmt-guestconfig
Requires:       python-azure-mgmt-hanaonazure
Requires:       python-azure-mgmt-hdinsight
Requires:       python-azure-mgmt-healthcareapis
Requires:       python-azure-mgmt-hybridcompute
Requires:       python-azure-mgmt-hybridkubernetes
Requires:       python-azure-mgmt-hybridnetwork
Requires:       python-azure-mgmt-imagebuilder
Requires:       python-azure-mgmt-iotcentral
Requires:       python-azure-mgmt-iothub
Requires:       python-azure-mgmt-iothubprovisioningservices
Requires:       python-azure-mgmt-keyvault
Requires:       python-azure-mgmt-kubernetesconfiguration
Requires:       python-azure-mgmt-kusto
Requires:       python-azure-mgmt-labservices
Requires:       python-azure-mgmt-loadtestservice
Requires:       python-azure-mgmt-loganalytics
Requires:       python-azure-mgmt-logic
Requires:       python-azure-mgmt-logz
Requires:       python-azure-mgmt-machinelearningcompute
Requires:       python-azure-mgmt-machinelearningservices
Requires:       python-azure-mgmt-maintenance
Requires:       python-azure-mgmt-managedservices
Requires:       python-azure-mgmt-managementgroups
Requires:       python-azure-mgmt-managementpartner
Requires:       python-azure-mgmt-maps
Requires:       python-azure-mgmt-marketplaceordering
Requires:       python-azure-mgmt-media
Requires:       python-azure-mgmt-mixedreality
Requires:       python-azure-mgmt-mobilenetwork
Requires:       python-azure-mgmt-monitor
Requires:       python-azure-mgmt-msi
Requires:       python-azure-mgmt-netapp
Requires:       python-azure-mgmt-network
Requires:       python-azure-mgmt-notificationhubs
Requires:       python-azure-mgmt-nspkg
Requires:       python-azure-mgmt-oep
Requires:       python-azure-mgmt-orbital
Requires:       python-azure-mgmt-peering
Requires:       python-azure-mgmt-policyinsights
Requires:       python-azure-mgmt-portal
Requires:       python-azure-mgmt-powerbidedicated
Requires:       python-azure-mgmt-powerbiembedded
Requires:       python-azure-mgmt-privatedns
Requires:       python-azure-mgmt-purview
Requires:       python-azure-mgmt-quantum
Requires:       python-azure-mgmt-quota
Requires:       python-azure-mgmt-rdbms
Requires:       python-azure-mgmt-recoveryservices
Requires:       python-azure-mgmt-recoveryservicesbackup
Requires:       python-azure-mgmt-recoveryservicessiterecovery
Requires:       python-azure-mgmt-redhatopenshift
Requires:       python-azure-mgmt-redis
Requires:       python-azure-mgmt-redisenterprise
Requires:       python-azure-mgmt-regionmove
Requires:       python-azure-mgmt-relay
Requires:       python-azure-mgmt-reservations
Requires:       python-azure-mgmt-resource
Requires:       python-azure-mgmt-resourceconnector
Requires:       python-azure-mgmt-resourcegraph
Requires:       python-azure-mgmt-resourcehealth
Requires:       python-azure-mgmt-resourcemover
Requires:       python-azure-mgmt-scheduler
Requires:       python-azure-mgmt-search
Requires:       python-azure-mgmt-security
Requires:       python-azure-mgmt-securityinsight
Requires:       python-azure-mgmt-serialconsole
Requires:       python-azure-mgmt-servermanager
Requires:       python-azure-mgmt-servicebus
Requires:       python-azure-mgmt-servicefabric
Requires:       python-azure-mgmt-servicefabricmanagedclusters
Requires:       python-azure-mgmt-servicelinker
Requires:       python-azure-mgmt-signalr
Requires:       python-azure-mgmt-sql
Requires:       python-azure-mgmt-sqlvirtualmachine
Requires:       python-azure-mgmt-storage
Requires:       python-azure-mgmt-storagecache
Requires:       python-azure-mgmt-storageimportexport
Requires:       python-azure-mgmt-storagepool
Requires:       python-azure-mgmt-storagesync
Requires:       python-azure-mgmt-streamanalytics
Requires:       python-azure-mgmt-subscription
Requires:       python-azure-mgmt-support
Requires:       python-azure-mgmt-synapse
Requires:       python-azure-mgmt-testbase
Requires:       python-azure-mgmt-timeseriesinsights
Requires:       python-azure-mgmt-trafficmanager
Requires:       python-azure-mgmt-videoanalyzer
Requires:       python-azure-mgmt-vmwarecloudsimple
Requires:       python-azure-mgmt-web
Requires:       python-azure-mgmt-webpubsub
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
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/azure_mgmt-*.egg-info

%changelog
