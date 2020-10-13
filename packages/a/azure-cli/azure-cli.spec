#
# spec file for package azure-cli
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


# Define just "test" as a package in _multibuild file to distinguish test
# instructions here
%if "@BUILD_FLAVOR@" == ""
%define _test 0
%define name_ext %nil
%else
%define _test 1
%define name_ext -test
%endif

%if !%{?_test}
Name:           azure-cli
%else
Name:           azure-cli%{?name_ext}
%endif
%define         short_name azure-cli
Version:        2.13.0
Release:        0
Summary:        Microsoft Azure CLI 2.0
License:        MIT
Group:          System/Management
URL:            https://github.com/Azure/azure-cli
Source:         https://files.pythonhosted.org/packages/source/a/azure-cli/azure-cli-%{version}.tar.gz
Source1:        LICENSE.txt
Patch1:         ac_use-python3-by-default.patch
%if 0%{?_test}
BuildRequires:  %{short_name} = %{version}
%else
BuildRequires:  azure-cli-command-modules-nspkg >= 2.0
BuildRequires:  azure-cli-core = %{version}
BuildRequires:  azure-cli-nspkg >= 3.0.3
BuildRequires:  fdupes
BuildRequires:  python3-Fabric >= 2.4
BuildRequires:  python3-PyYAML >= 5.1
BuildRequires:  python3-azure-appconfiguration >= 1.1.1
BuildRequires:  python3-azure-batch < 10.0
BuildRequires:  python3-azure-batch >= 9.0
BuildRequires:  python3-azure-cosmos >= 3.0.2
BuildRequires:  python3-azure-datalake-store >= 0.0.49
BuildRequires:  python3-azure-functions-devops-build >= 0.0.22
BuildRequires:  python3-azure-graphrbac >= 0.60.0
BuildRequires:  python3-azure-keyvault >= 1.1.0
BuildRequires:  python3-azure-keyvault-administration >= 4.0.0b1
BuildRequires:  python3-azure-loganalytics >= 0.1.0
BuildRequires:  python3-azure-mgmt-advisor >= 2.0.1
BuildRequires:  python3-azure-mgmt-apimanagement >= 0.2.0
BuildRequires:  python3-azure-mgmt-appconfiguration >= 0.6.0
BuildRequires:  python3-azure-mgmt-applicationinsights >= 0.1.1
BuildRequires:  python3-azure-mgmt-authorization >= 0.61.0
BuildRequires:  python3-azure-mgmt-batch >= 9.0.0
BuildRequires:  python3-azure-mgmt-batchai >= 2.0
BuildRequires:  python3-azure-mgmt-billing >= 0.2
BuildRequires:  python3-azure-mgmt-botservice >= 0.2.0
BuildRequires:  python3-azure-mgmt-cdn >= 5.0.0
BuildRequires:  python3-azure-mgmt-cognitiveservices >= 6.2.0
BuildRequires:  python3-azure-mgmt-compute >= 13.0
BuildRequires:  python3-azure-mgmt-consumption >= 2.0
BuildRequires:  python3-azure-mgmt-containerinstance >= 1.4
BuildRequires:  python3-azure-mgmt-containerregistry >= 3.0.0rc15
BuildRequires:  python3-azure-mgmt-containerservice >= 9.4.0
BuildRequires:  python3-azure-mgmt-cosmosdb >= 1.0.0
BuildRequires:  python3-azure-mgmt-datalake-analytics >= 0.2.1
BuildRequires:  python3-azure-mgmt-datalake-store >= 0.5.0
BuildRequires:  python3-azure-mgmt-datamigration >= 0.1.0
BuildRequires:  python3-azure-mgmt-deploymentmanager >= 0.2.0
BuildRequires:  python3-azure-mgmt-devtestlabs >= 4.0
BuildRequires:  python3-azure-mgmt-dns >= 2.1
BuildRequires:  python3-azure-mgmt-eventgrid >= 3.0.0rc7
BuildRequires:  python3-azure-mgmt-eventhub >= 4.1.0
BuildRequires:  python3-azure-mgmt-hdinsight >= 1.7.0
BuildRequires:  python3-azure-mgmt-imagebuilder >= 0.4.0
BuildRequires:  python3-azure-mgmt-iotcentral >= 3.0.0
BuildRequires:  python3-azure-mgmt-iothub >= 0.12.0
BuildRequires:  python3-azure-mgmt-iothubprovisioningservices >= 0.2.0
BuildRequires:  python3-azure-mgmt-keyvault >= 7.0.0b3
BuildRequires:  python3-azure-mgmt-kusto >= 0.3.0
BuildRequires:  python3-azure-mgmt-loganalytics >= 0.7.0
BuildRequires:  python3-azure-mgmt-managedservices >= 1.0
BuildRequires:  python3-azure-mgmt-managementgroups >= 0.1
BuildRequires:  python3-azure-mgmt-maps >= 0.1.0
BuildRequires:  python3-azure-mgmt-marketplaceordering >= 0.1
BuildRequires:  python3-azure-mgmt-media >= 2.1.0
BuildRequires:  python3-azure-mgmt-monitor >= 0.11.0
BuildRequires:  python3-azure-mgmt-msi >= 0.2
BuildRequires:  python3-azure-mgmt-netapp >= 0.12.0
BuildRequires:  python3-azure-mgmt-network >= 12.0.0
BuildRequires:  python3-azure-mgmt-policyinsights >= 0.5.0
BuildRequires:  python3-azure-mgmt-privatedns >= 0.1.0
BuildRequires:  python3-azure-mgmt-rdbms >= 3.0.0rc1
BuildRequires:  python3-azure-mgmt-recoveryservices >= 0.4.0
BuildRequires:  python3-azure-mgmt-recoveryservicesbackup >= 0.6.0
BuildRequires:  python3-azure-mgmt-redis >= 7.0.0rc1
BuildRequires:  python3-azure-mgmt-relay >= 0.1.0
BuildRequires:  python3-azure-mgmt-reservations >= 0.6.0
BuildRequires:  python3-azure-mgmt-search >= 2.0
BuildRequires:  python3-azure-mgmt-security >= 0.4.1
BuildRequires:  python3-azure-mgmt-servicebus >= 0.6.0
BuildRequires:  python3-azure-mgmt-servicefabric >= 0.5.0
BuildRequires:  python3-azure-mgmt-signalr >= 0.4.0
BuildRequires:  python3-azure-mgmt-sql >= 0.21.0
BuildRequires:  python3-azure-mgmt-sqlvirtualmachine >= 0.5.0
BuildRequires:  python3-azure-mgmt-storage >= 11.2.0
BuildRequires:  python3-azure-mgmt-synapse >= 0.3.0
BuildRequires:  python3-azure-mgmt-trafficmanager >= 0.51.0
BuildRequires:  python3-azure-mgmt-web >= 0.47.0
BuildRequires:  python3-azure-multiapi-storage >= 0.4.1
BuildRequires:  python3-azure-nspkg >= 3.0.0
BuildRequires:  python3-azure-storage-common >= 1.4
BuildRequires:  python3-azure-synapse-accesscontrol >= 0.2.0
BuildRequires:  python3-azure-synapse-spark >= 0.2.0
BuildRequires:  python3-cryptography >= 2.3.1
BuildRequires:  python3-devel
BuildRequires:  python3-javaproperties >= 0.5.1
BuildRequires:  python3-jsmin >= 2.2.2
BuildRequires:  python3-jsondiff >= 1.2.0
BuildRequires:  python3-mock >= 4.0
BuildRequires:  python3-pydocumentdb >= 2.0.1
BuildRequires:  python3-pygments >= 2.4
BuildRequires:  python3-pytz >= 2019.1
BuildRequires:  python3-scp >= 0.13.2
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools
BuildRequires:  python3-sshtunnel >= 0.1.4
BuildRequires:  python3-urllib3 >= 1.18
BuildRequires:  python3-vsts-cd-manager >= 1.0.0
BuildRequires:  python3-websocket-client >= 0.56.0
BuildRequires:  python3-xmltodict >= 0.12
Requires:       azure-cli-command-modules-nspkg >= 2.0
Requires:       azure-cli-core = %{version}
Requires:       azure-cli-nspkg >= 3.0.3
Requires:       python3-Fabric >= 2.4
Requires:       python3-PyYAML >= 5.1
Requires:       python3-antlr4-python3-runtime < 5.0.0
Requires:       python3-antlr4-python3-runtime >= 4.7.2
Requires:       python3-azure-appconfiguration >= 1.1.1
Requires:       python3-azure-batch < 10.0
Requires:       python3-azure-batch >= 9.0
Requires:       python3-azure-cosmos >= 3.0.2
Requires:       python3-azure-datalake-store >= 0.0.49
Requires:       python3-azure-functions-devops-build >= 0.0.22
Requires:       python3-azure-graphrbac >= 0.60.0
Requires:       python3-azure-keyvault >= 1.1.0
Requires:       python3-azure-keyvault-administration >= 4.0.0b1
Requires:       python3-azure-loganalytics >= 0.1.0
Requires:       python3-azure-loganalytics >= 0.1.0
Requires:       python3-azure-mgmt-advisor >= 2.0.1
Requires:       python3-azure-mgmt-apimanagement >= 0.2.0
Requires:       python3-azure-mgmt-appconfiguration >= 0.6.0
Requires:       python3-azure-mgmt-applicationinsights >= 0.1.1
Requires:       python3-azure-mgmt-authorization >= 0.61.0
Requires:       python3-azure-mgmt-batch >= 9.0.0
Requires:       python3-azure-mgmt-batchai >= 2.0
Requires:       python3-azure-mgmt-billing >= 0.2
Requires:       python3-azure-mgmt-botservice >= 0.2.0
Requires:       python3-azure-mgmt-cdn >= 5.0.0
Requires:       python3-azure-mgmt-cognitiveservices >= 6.2.0
Requires:       python3-azure-mgmt-compute >= 13.0
Requires:       python3-azure-mgmt-consumption >= 2.0
Requires:       python3-azure-mgmt-containerinstance >= 1.4
Requires:       python3-azure-mgmt-containerregistry >= 3.0.0rc15
Requires:       python3-azure-mgmt-containerservice >= 9.4.0
Requires:       python3-azure-mgmt-cosmosdb >= 1.0.0
Requires:       python3-azure-mgmt-datalake-analytics >= 0.2.1
Requires:       python3-azure-mgmt-datalake-store >= 0.5.0
Requires:       python3-azure-mgmt-datamigration >= 0.1.0
Requires:       python3-azure-mgmt-deploymentmanager >= 0.2.0
Requires:       python3-azure-mgmt-devtestlabs >= 2.2
Requires:       python3-azure-mgmt-dns >= 2.1
Requires:       python3-azure-mgmt-eventgrid >= 3.0.0rc7
Requires:       python3-azure-mgmt-eventhub >= 4.1.0
Requires:       python3-azure-mgmt-hdinsight >= 1.7.0
Requires:       python3-azure-mgmt-imagebuilder >= 0.4.0
Requires:       python3-azure-mgmt-iotcentral >= 3.0.0
Requires:       python3-azure-mgmt-iothub >= 0.12.0
Requires:       python3-azure-mgmt-iothubprovisioningservices >= 0.2.0
Requires:       python3-azure-mgmt-keyvault >= 7.0.0b3
Requires:       python3-azure-mgmt-kusto >= 0.3.0
Requires:       python3-azure-mgmt-loganalytics >= 0.7.0
Requires:       python3-azure-mgmt-managedservices >= 1.0
Requires:       python3-azure-mgmt-managementgroups >= 0.1
Requires:       python3-azure-mgmt-maps >= 0.1.0
Requires:       python3-azure-mgmt-marketplaceordering >= 0.1
Requires:       python3-azure-mgmt-media >= 2.1.0
Requires:       python3-azure-mgmt-monitor >= 0.11.0
Requires:       python3-azure-mgmt-msi >= 0.2
Requires:       python3-azure-mgmt-netapp >= 0.12.0
Requires:       python3-azure-mgmt-network >= 12.0.0
Requires:       python3-azure-mgmt-policyinsights >= 0.5.0
Requires:       python3-azure-mgmt-privatedns >= 0.1.0
Requires:       python3-azure-mgmt-rdbms >= 3.0.0rc1
Requires:       python3-azure-mgmt-recoveryservices >= 0.4.0
Requires:       python3-azure-mgmt-recoveryservicesbackup >= 0.6.0
Requires:       python3-azure-mgmt-redis >= 7.0.0rc1
Requires:       python3-azure-mgmt-relay >= 0.1.0
Requires:       python3-azure-mgmt-reservations >= 0.6.0
Requires:       python3-azure-mgmt-search >= 2.0
Requires:       python3-azure-mgmt-security >= 0.4.1
Requires:       python3-azure-mgmt-servicebus >= 0.6.0
Requires:       python3-azure-mgmt-servicefabric >= 0.5.0
Requires:       python3-azure-mgmt-signalr >= 0.4.0
Requires:       python3-azure-mgmt-sql >= 0.21.0
Requires:       python3-azure-mgmt-sqlvirtualmachine >= 0.5.0
Requires:       python3-azure-mgmt-storage >= 11.2.0
Requires:       python3-azure-mgmt-synapse >= 0.3.0
Requires:       python3-azure-mgmt-trafficmanager >= 0.51.0
Requires:       python3-azure-mgmt-web >= 0.47.0
Requires:       python3-azure-multiapi-storage >= 0.4.1
Requires:       python3-azure-storage-common >= 1.4
Requires:       python3-azure-synapse-accesscontrol >= 0.2.0
Requires:       python3-azure-synapse-spark >= 0.2.0
Requires:       python3-cryptography >= 2.3.1
Requires:       python3-javaproperties >= 0.5.1
Requires:       python3-jsmin >= 2.2.2
Requires:       python3-jsondiff >= 1.2.0
Requires:       python3-mock >= 4.0
Requires:       python3-pydocumentdb >= 2.0.1
Requires:       python3-pygments >= 2.4
Requires:       python3-pytz >= 2019.1
Requires:       python3-scp >= 0.13.2
Requires:       python3-sshtunnel >= 0.1.4
Requires:       python3-urllib3 >= 1.18
Requires:       python3-vsts-cd-manager >= 1.0.2
Requires:       python3-websocket-client >= 0.56.0
Requires:       python3-xmltodict >= 0.12
Provides:       azure-cli-acr = 2.2.9
Obsoletes:      azure-cli-acr < 2.2.9
Provides:       azure-cli-acs = 2.4.4
Obsoletes:      azure-cli-acs < 2.4.4
Provides:       azure-cli-advisor = 2.0.1
Obsoletes:      azure-cli-advisor < 2.0.1
Provides:       azure-cli-ams = 0.4.7
Obsoletes:      azure-cli-ams < 0.4.7
Provides:       azure-cli-appservice = 0.2.21
Obsoletes:      azure-cli-appservice < 0.2.21
Provides:       azure-cli-backup = 1.2.5
Obsoletes:      azure-cli-backup < 1.2.5
Provides:       azure-cli-batch = 4.0.3
Obsoletes:      azure-cli-batch < 4.0.3
Provides:       azure-cli-batchai = 0.4.10
Obsoletes:      azure-cli-batchai < 0.4.10
Provides:       azure-cli-billing = 0.2.2
Obsoletes:      azure-cli-billing < 0.2.2
Provides:       azure-cli-botservice = 0.2.2
Obsoletes:      azure-cli-botservice < 0.2.2
Provides:       azure-cli-cdn = 0.2.4
Obsoletes:      azure-cli-cdn < 0.2.4
Provides:       azure-cli-cloud = 2.1.1
Obsoletes:      azure-cli-cloud < 2.1.1
Provides:       azure-cli-cognitiveservices = 0.2.6
Obsoletes:      azure-cli-cognitiveservices < 0.2.6
Provides:       azure-cli-component = 2.0.8
Obsoletes:      azure-cli-component < 2.0.8
Provides:       azure-cli-configure = 2.0.24
Obsoletes:      azure-cli-configure < 2.0.24
Provides:       azure-cli-consumption = 0.4.4
Obsoletes:      azure-cli-consumption < 0.4.4
Provides:       azure-cli-container = 0.3.18
Obsoletes:      azure-cli-container < 0.3.18
Provides:       azure-cli-cosmosdb = 0.2.11
Obsoletes:      azure-cli-cosmosdb < 0.2.11
Provides:       azure-cli-deploymentmanager = 0.1.1
Obsoletes:      azure-cli-deploymentmanager < 0.1.1
Provides:       azure-cli-dla = 0.2.6
Obsoletes:      azure-cli-dla < 0.2.6
Provides:       azure-cli-dls = 0.1.10
Obsoletes:      azure-cli-dls < 0.1.10
Provides:       azure-cli-dms = 0.1.4
Obsoletes:      azure-cli-dms < 0.1.4
Provides:       azure-cli-eventgrid = 0.2.4
Obsoletes:      azure-cli-eventgrid < 0.2.4
Provides:       azure-cli-eventhubs = 0.3.7
Obsoletes:      azure-cli-eventhubs < 0.3.7
Provides:       azure-cli-extension = 0.2.5
Obsoletes:      azure-cli-extension < 0.2.5
Provides:       azure-cli-feedback = 2.2.1
Obsoletes:      azure-cli-feedback < 2.2.1
Provides:       azure-cli-find = 0.3.4
Obsoletes:      azure-cli-find < 0.3.4
Provides:       azure-cli-hdinsight = 0.3.5
Obsoletes:      azure-cli-hdinsight < 0.3.5
Provides:       azure-cli-interactive = 0.4.5
Obsoletes:      azure-cli-interactive < 0.4.5
Provides:       azure-cli-iot = 0.3.11
Obsoletes:      azure-cli-iot < 0.3.11
Provides:       azure-cli-iotcentral = 0.1.7
Obsoletes:      azure-cli-iotcentral < 0.1.7
Provides:       azure-cli-keyvault = 2.2.16
Obsoletes:      azure-cli-keyvault < 2.2.16
Provides:       azure-cli-kusto = 0.2.3
Obsoletes:      azure-cli-kusto < 0.2.3
Provides:       azure-cli-lab = 0.1.8
Obsoletes:      azure-cli-lab < 0.1.8
Provides:       azure-cli-maps = 0.3.5
Obsoletes:      azure-cli-maps < 0.3.5
Provides:       azure-cli-monitor = 0.2.15
Obsoletes:      azure-cli-monitor < 0.2.15
Provides:       azure-cli-natgateway = 0.1.1
Obsoletes:      azure-cli-natgateway < 0.1.1
Provides:       azure-cli-network = 2.5.2
Obsoletes:      azure-cli-network < 2.5.2
Provides:       azure-cli-policyinsights = 0.1.4
Obsoletes:      azure-cli-policyinsights < 0.1.4
Provides:       azure-cli-privatedns = 1.0.2
Obsoletes:      azure-cli-privatedns < 1.0.2
Provides:       azure-cli-profile = 2.1.5
Obsoletes:      azure-cli-profile < 2.1.5
Provides:       azure-cli-rdbms = 0.3.12
Obsoletes:      azure-cli-rdbms < 0.3.12
Provides:       azure-cli-redis = 0.4.4
Obsoletes:      azure-cli-redis < 0.4.4
Provides:       azure-cli-relay = 0.1.5
Obsoletes:      azure-cli-relay < 0.1.5
Provides:       azure-cli-reservations = 0.4.3
Obsoletes:      azure-cli-reservations < 0.4.3
Provides:       azure-cli-resource = 2.1.16
Obsoletes:      azure-cli-resource < 2.1.16
Provides:       azure-cli-role = 2.6.4
Obsoletes:      azure-cli-role < 2.6.4
Provides:       azure-cli-search = 0.1.2
Obsoletes:      azure-cli-search < 0.1.2
Provides:       azure-cli-security = 0.1.2
Obsoletes:      azure-cli-security < 0.1.2
Provides:       azure-cli-servicebus = 0.3.6
Obsoletes:      azure-cli-servicebus < 0.3.6
Provides:       azure-cli-servicefabric = 0.1.20
Obsoletes:      azure-cli-servicefabric < 0.1.20
Provides:       azure-cli-signalr = 1.0.1
Obsoletes:      azure-cli-signalr < 1.0.1
Provides:       azure-cli-sql = 2.2.5
Obsoletes:      azure-cli-sql < 2.2.5
Provides:       azure-cli-sqlvm = 0.2.0
Obsoletes:      azure-cli-sqlvm < 0.2.0
Provides:       azure-cli-storage = 2.4.3
Obsoletes:      azure-cli-storage < 2.4.3
Provides:       azure-cli-vm = 2.2.23
Obsoletes:      azure-cli-vm < 2.2.23
Conflicts:      azure-cli < 2.0.0

BuildArch:      noarch
%endif

%description
Microsoft Azure CLI 2.0 Command Line Utilities

%prep
%if 0%{?_test}
# workaround to prevent post/install failing assuming this file for whatever
# reason
touch %{_sourcedir}/%{short_name}
%else
%setup -q -n azure-cli-%{version}
%patch1 -p1
%endif

%build
%if 0%{?_test}
az --help
%else
install -m 644 %{SOURCE1} %{_builddir}/azure-cli-%{version}
python3 setup.py build
%endif

%install
%if 0%{?_test}
# disable debug packages in package test to prevent error about missing files
%define debug_package %{nil}
%else
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix} --install-lib=%{python3_sitelib}
install -DTm644 %{buildroot}%{_bindir}/az.completion.sh %{buildroot}%{_datadir}/bash-completion/completions/az.completion.sh
%fdupes %{buildroot}%{python3_sitelib}
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/command_modules/__init__.*
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/command_modules/__pycache__
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/__init__.*
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/__pycache__
rm -rf %{buildroot}%{python3_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{python3_sitelib}/azure/__pycache__
%endif

%files
%if !%{?_test}
%defattr(-,root,root,-)
%doc HISTORY.rst README.rst
%license LICENSE.txt
%{_bindir}/az
%{_datadir}/bash-completion/completions/az.completion.sh
%exclude /usr/bin/az.bat
%exclude /usr/bin/az.completion.sh
%{python3_sitelib}/azure/cli
%{python3_sitelib}/azure_cli-*.egg-info
%endif

%changelog
