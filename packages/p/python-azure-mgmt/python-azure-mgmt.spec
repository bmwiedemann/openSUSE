#
# spec file for package python-azure-mgmt
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-azure-mgmt
Version:        4.0.0
Release:        0
Summary:        Microsoft Azure Resource Management bundle
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-mgmt/azure-mgmt-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-mgmt-advisor
Requires:       python-azure-mgmt-agfood
Requires:       python-azure-mgmt-agrifood
Requires:       python-azure-mgmt-alertsmanagement
Requires:       python-azure-mgmt-apicenter
Requires:       python-azure-mgmt-apimanagement
Requires:       python-azure-mgmt-app
Requires:       python-azure-mgmt-appcomplianceautomation
Requires:       python-azure-mgmt-appconfiguration
Requires:       python-azure-mgmt-appcontainers
Requires:       python-azure-mgmt-applicationinsights
Requires:       python-azure-mgmt-appplatform
Requires:       python-azure-mgmt-arizeaiobservabilityeval
Requires:       python-azure-mgmt-astro
Requires:       python-azure-mgmt-attestation
Requires:       python-azure-mgmt-authorization
Requires:       python-azure-mgmt-automanage
Requires:       python-azure-mgmt-automation
Requires:       python-azure-mgmt-avs
Requires:       python-azure-mgmt-azureadb2c
Requires:       python-azure-mgmt-azurearcdata
Requires:       python-azure-mgmt-azurestack
Requires:       python-azure-mgmt-azurestackhci
Requires:       python-azure-mgmt-azurestackhcivm
Requires:       python-azure-mgmt-baremetalinfrastructure
Requires:       python-azure-mgmt-batch
Requires:       python-azure-mgmt-batchai
Requires:       python-azure-mgmt-billing
Requires:       python-azure-mgmt-billingbenefits
Requires:       python-azure-mgmt-botservice
Requires:       python-azure-mgmt-carbonoptimization
Requires:       python-azure-mgmt-cdn
Requires:       python-azure-mgmt-chaos
Requires:       python-azure-mgmt-cloudhealth
Requires:       python-azure-mgmt-cognitiveservices
Requires:       python-azure-mgmt-commerce
Requires:       python-azure-mgmt-communication
Requires:       python-azure-mgmt-compute
Requires:       python-azure-mgmt-computefleet
Requires:       python-azure-mgmt-computerecommender
Requires:       python-azure-mgmt-computeschedule
Requires:       python-azure-mgmt-confidentialledger
Requires:       python-azure-mgmt-confluent
Requires:       python-azure-mgmt-connectedcache
Requires:       python-azure-mgmt-connectedvmware
Requires:       python-azure-mgmt-consumption
Requires:       python-azure-mgmt-containerinstance
Requires:       python-azure-mgmt-containerorchestratorruntime
Requires:       python-azure-mgmt-containerregistry
Requires:       python-azure-mgmt-containerservice
Requires:       python-azure-mgmt-containerservicefleet
Requires:       python-azure-mgmt-containerservicesafeguards
Requires:       python-azure-mgmt-core
Requires:       python-azure-mgmt-cosmosdb
Requires:       python-azure-mgmt-cosmosdbforpostgresql
Requires:       python-azure-mgmt-costmanagement
Requires:       python-azure-mgmt-customproviders
Requires:       python-azure-mgmt-dashboard
Requires:       python-azure-mgmt-databasewatcher
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
Requires:       python-azure-mgmt-defendereasm
Requires:       python-azure-mgmt-dependencymap
Requires:       python-azure-mgmt-deploymentmanager
Requires:       python-azure-mgmt-desktopvirtualization
Requires:       python-azure-mgmt-devcenter
Requires:       python-azure-mgmt-devhub
Requires:       python-azure-mgmt-deviceregistry
Requires:       python-azure-mgmt-deviceupdate
Requires:       python-azure-mgmt-devopsinfrastructure
Requires:       python-azure-mgmt-devspaces
Requires:       python-azure-mgmt-devtestlabs
Requires:       python-azure-mgmt-digitaltwins
Requires:       python-azure-mgmt-dns
Requires:       python-azure-mgmt-dnsresolver
Requires:       python-azure-mgmt-durabletask
Requires:       python-azure-mgmt-dynatrace
Requires:       python-azure-mgmt-edgegateway
Requires:       python-azure-mgmt-edgeorder
Requires:       python-azure-mgmt-edgezones
Requires:       python-azure-mgmt-education
Requires:       python-azure-mgmt-elastic
Requires:       python-azure-mgmt-elasticsan
Requires:       python-azure-mgmt-eventgrid
Requires:       python-azure-mgmt-eventhub
Requires:       python-azure-mgmt-extendedlocation
Requires:       python-azure-mgmt-fabric
Requires:       python-azure-mgmt-fluidrelay
Requires:       python-azure-mgmt-frontdoor
Requires:       python-azure-mgmt-graphservices
Requires:       python-azure-mgmt-guestconfig
Requires:       python-azure-mgmt-hanaonazure
Requires:       python-azure-mgmt-hardwaresecuritymodules
Requires:       python-azure-mgmt-hdinsight
Requires:       python-azure-mgmt-hdinsightcontainers
Requires:       python-azure-mgmt-healthcareapis
Requires:       python-azure-mgmt-healthdataaiservices
Requires:       python-azure-mgmt-hybridcompute
Requires:       python-azure-mgmt-hybridconnectivity
Requires:       python-azure-mgmt-hybridcontainerservice
Requires:       python-azure-mgmt-hybridkubernetes
Requires:       python-azure-mgmt-hybridnetwork
Requires:       python-azure-mgmt-imagebuilder
Requires:       python-azure-mgmt-impactreporting
Requires:       python-azure-mgmt-informaticadatamanagement
Requires:       python-azure-mgmt-iotcentral
Requires:       python-azure-mgmt-iotfirmwaredefense
Requires:       python-azure-mgmt-iothub
Requires:       python-azure-mgmt-iothubprovisioningservices
Requires:       python-azure-mgmt-iotoperations
Requires:       python-azure-mgmt-keyvault
Requires:       python-azure-mgmt-kubernetesconfiguration
Requires:       python-azure-mgmt-kubernetesconfiguration-extensions
Requires:       python-azure-mgmt-kubernetesconfiguration-extensiontypes
Requires:       python-azure-mgmt-kubernetesconfiguration-fluxconfigurations
Requires:       python-azure-mgmt-kusto
Requires:       python-azure-mgmt-labservices
Requires:       python-azure-mgmt-lambdatesthyperexecute
Requires:       python-azure-mgmt-largeinstance
Requires:       python-azure-mgmt-loadtesting
Requires:       python-azure-mgmt-loadtestservice
Requires:       python-azure-mgmt-loganalytics
Requires:       python-azure-mgmt-logic
Requires:       python-azure-mgmt-logz
Requires:       python-azure-mgmt-machinelearningcompute
Requires:       python-azure-mgmt-machinelearningservices
Requires:       python-azure-mgmt-maintenance
Requires:       python-azure-mgmt-managedapplications
Requires:       python-azure-mgmt-managednetworkfabric
Requires:       python-azure-mgmt-managedservices
Requires:       python-azure-mgmt-managementgroups
Requires:       python-azure-mgmt-managementpartner
Requires:       python-azure-mgmt-maps
Requires:       python-azure-mgmt-marketplaceordering
Requires:       python-azure-mgmt-media
Requires:       python-azure-mgmt-migrationassessment
Requires:       python-azure-mgmt-migrationdiscoverysap
Requires:       python-azure-mgmt-mixedreality
Requires:       python-azure-mgmt-mobilenetwork
Requires:       python-azure-mgmt-mongodbatlas
Requires:       python-azure-mgmt-monitor
Requires:       python-azure-mgmt-msi
Requires:       python-azure-mgmt-mysqlflexibleservers
Requires:       python-azure-mgmt-neonpostgres
Requires:       python-azure-mgmt-netapp
Requires:       python-azure-mgmt-network
Requires:       python-azure-mgmt-networkanalytics
Requires:       python-azure-mgmt-networkcloud
Requires:       python-azure-mgmt-networkfunction
Requires:       python-azure-mgmt-newrelicobservability
Requires:       python-azure-mgmt-nginx
Requires:       python-azure-mgmt-notificationhubs
Requires:       python-azure-mgmt-nspkg
Requires:       python-azure-mgmt-oep
Requires:       python-azure-mgmt-onlineexperimentation
Requires:       python-azure-mgmt-oracledatabase
Requires:       python-azure-mgmt-orbital
Requires:       python-azure-mgmt-paloaltonetworksngfw
Requires:       python-azure-mgmt-peering
Requires:       python-azure-mgmt-pineconevectordb
Requires:       python-azure-mgmt-planetarycomputer
Requires:       python-azure-mgmt-playwright
Requires:       python-azure-mgmt-playwrighttesting
Requires:       python-azure-mgmt-policyinsights
Requires:       python-azure-mgmt-portal
Requires:       python-azure-mgmt-portalservicescopilot
Requires:       python-azure-mgmt-postgresqlflexibleservers
Requires:       python-azure-mgmt-powerbidedicated
Requires:       python-azure-mgmt-powerbiembedded
Requires:       python-azure-mgmt-privatedns
Requires:       python-azure-mgmt-purestorageblock
Requires:       python-azure-mgmt-purview
Requires:       python-azure-mgmt-quantum
Requires:       python-azure-mgmt-qumulo
Requires:       python-azure-mgmt-quota
Requires:       python-azure-mgmt-rdbms
Requires:       python-azure-mgmt-recoveryservices
Requires:       python-azure-mgmt-recoveryservicesbackup
Requires:       python-azure-mgmt-recoveryservicesdatareplication
Requires:       python-azure-mgmt-recoveryservicessiterecovery
Requires:       python-azure-mgmt-redhatopenshift
Requires:       python-azure-mgmt-redis
Requires:       python-azure-mgmt-redisenterprise
Requires:       python-azure-mgmt-regionmove
Requires:       python-azure-mgmt-relay
Requires:       python-azure-mgmt-reservations
Requires:       python-azure-mgmt-resource
Requires:       python-azure-mgmt-resource-bicep
Requires:       python-azure-mgmt-resourceconnector
Requires:       python-azure-mgmt-resourcegraph
Requires:       python-azure-mgmt-resourcehealth
Requires:       python-azure-mgmt-resourcemover
Requires:       python-azure-mgmt-scheduler
Requires:       python-azure-mgmt-scvmm
Requires:       python-azure-mgmt-search
Requires:       python-azure-mgmt-security
Requires:       python-azure-mgmt-securitydevops
Requires:       python-azure-mgmt-securityinsight
Requires:       python-azure-mgmt-selfhelp
Requires:       python-azure-mgmt-serialconsole
Requires:       python-azure-mgmt-servermanager
Requires:       python-azure-mgmt-servicebus
Requires:       python-azure-mgmt-servicefabric
Requires:       python-azure-mgmt-servicefabricmanagedclusters
Requires:       python-azure-mgmt-servicelinker
Requires:       python-azure-mgmt-servicenetworking
Requires:       python-azure-mgmt-signalr
Requires:       python-azure-mgmt-sitemanager
Requires:       python-azure-mgmt-sphere
Requires:       python-azure-mgmt-springappdiscovery
Requires:       python-azure-mgmt-sql
Requires:       python-azure-mgmt-sqlvirtualmachine
Requires:       python-azure-mgmt-standbypool
Requires:       python-azure-mgmt-storage
Requires:       python-azure-mgmt-storageactions
Requires:       python-azure-mgmt-storagecache
Requires:       python-azure-mgmt-storagediscovery
Requires:       python-azure-mgmt-storageimportexport
Requires:       python-azure-mgmt-storagemover
Requires:       python-azure-mgmt-storagepool
Requires:       python-azure-mgmt-storagesync
Requires:       python-azure-mgmt-streamanalytics
Requires:       python-azure-mgmt-subscription
Requires:       python-azure-mgmt-support
Requires:       python-azure-mgmt-synapse
Requires:       python-azure-mgmt-terraform
Requires:       python-azure-mgmt-testbase
Requires:       python-azure-mgmt-timeseriesinsights
Requires:       python-azure-mgmt-trafficmanager
Requires:       python-azure-mgmt-trustedsigning
Requires:       python-azure-mgmt-videoanalyzer
Requires:       python-azure-mgmt-vmwarecloudsimple
Requires:       python-azure-mgmt-voiceservices
Requires:       python-azure-mgmt-web
Requires:       python-azure-mgmt-webpubsub
Requires:       python-azure-mgmt-weightsandbiases
Requires:       python-azure-mgmt-workloadmonitor
Requires:       python-azure-mgmt-workloadorchestration
Requires:       python-azure-mgmt-workloads
Requires:       python-azure-mgmt-workloadssapvirtualinstance
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-mgmt <= 4.0.0
%endif
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/azure_mgmt-*.dist-info

%changelog
