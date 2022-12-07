#
# spec file for package azure-cli
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
Version:        2.43.0
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
BuildRequires:  python-rpm-macros
Requires:       azure-cli-command-modules-nspkg >= 2.0
Requires:       azure-cli-core = %{version}
Requires:       azure-cli-nspkg >= 3.0.3
Requires:       python3-Fabric >= 2.4
Requires:       python3-PyGithub >= 1.38
Requires:       python3-PyMySQL >= 1.0.2
Requires:       python3-PyNaCl >= 1.5.0
Requires:       python3-PyYAML >= 5.1
Requires:       python3-antlr4-python3-runtime >= 4.9.3
Requires:       python3-azure-appconfiguration >= 1.1.1
Requires:       python3-azure-batch >= 12.0
Requires:       python3-azure-cosmos >= 3.0.2
Requires:       python3-azure-data-tables >= 12.4.0
Requires:       python3-azure-datalake-store >= 0.0.49
Requires:       python3-azure-graphrbac >= 0.60.0
Requires:       python3-azure-keyvault >= 1.1.0
Requires:       python3-azure-keyvault-administration >= 4.0.0b3
Requires:       python3-azure-keyvault-keys >= 4.5.1
Requires:       python3-azure-loganalytics >= 0.1.0
Requires:       python3-azure-mgmt-advisor >= 9.0.0
Requires:       python3-azure-mgmt-apimanagement >= 3.0.0
Requires:       python3-azure-mgmt-appconfiguration >= 2.2.0
Requires:       python3-azure-mgmt-applicationinsights >= 1.0.0
Requires:       python3-azure-mgmt-authorization >= 0.61.0
Requires:       python3-azure-mgmt-batch >= 16.2.0
Requires:       python3-azure-mgmt-batchai >= 7.0.0b1
Requires:       python3-azure-mgmt-billing >= 6.0.0
Requires:       python3-azure-mgmt-botservice >= 2.0.0b3
Requires:       python3-azure-mgmt-cdn >= 12.0.0
Requires:       python3-azure-mgmt-cognitiveservices >= 13.3.0
Requires:       python3-azure-mgmt-compute >= 29.0.0
Requires:       python3-azure-mgmt-consumption >= 2.0
Requires:       python3-azure-mgmt-containerinstance >= 9.1.0
Requires:       python3-azure-mgmt-containerregistry >= 10.0.0
Requires:       python3-azure-mgmt-containerservice >= 20.6.0
Requires:       python3-azure-mgmt-cosmosdb >= 8.0.0
Requires:       python3-azure-mgmt-databoxedge >= 1.0.0
Requires:       python3-azure-mgmt-datalake-analytics >= 0.2.1
Requires:       python3-azure-mgmt-datalake-store >= 0.5.0
Requires:       python3-azure-mgmt-datamigration >= 10.0.0
Requires:       python3-azure-mgmt-deploymentmanager >= 0.2.0
Requires:       python3-azure-mgmt-devtestlabs >= 2.2
Requires:       python3-azure-mgmt-dns >= 8.0.0
Requires:       python3-azure-mgmt-eventgrid >= 10.2.0
Requires:       python3-azure-mgmt-eventhub >= 10.1.0
Requires:       python3-azure-mgmt-extendedlocation >= 1.0.0b2
Requires:       python3-azure-mgmt-hdinsight >= 9.0.0
Requires:       python3-azure-mgmt-imagebuilder >= 1.1.0
Requires:       python3-azure-mgmt-iotcentral >= 10.0.0b1
Requires:       python3-azure-mgmt-iothub >= 2.3.0
Requires:       python3-azure-mgmt-iothubprovisioningservices >= 1.1.0
Requires:       python3-azure-mgmt-keyvault >= 10.1.0
Requires:       python3-azure-mgmt-kusto >= 0.3.0
Requires:       python3-azure-mgmt-loganalytics >= 13.0.0
Requires:       python3-azure-mgmt-managedservices >= 1.0
Requires:       python3-azure-mgmt-managementgroups >= 1.0.0
Requires:       python3-azure-mgmt-maps >= 2.0.0
Requires:       python3-azure-mgmt-marketplaceordering >= 1.1.0
Requires:       python3-azure-mgmt-media >= 9.0
Requires:       python3-azure-mgmt-monitor >= 5.0.0
Requires:       python3-azure-mgmt-msi >= 6.1.0
Requires:       python3-azure-mgmt-netapp >= 9.0.1
Requires:       python3-azure-mgmt-network >= 21.0.1
Requires:       python3-azure-mgmt-policyinsights >= 1.1.0b2
Requires:       python3-azure-mgmt-privatedns >= 1.0.0
Requires:       python3-azure-mgmt-rdbms >= 10.2.0b5
Requires:       python3-azure-mgmt-recoveryservices >= 2.1.0
Requires:       python3-azure-mgmt-recoveryservicesbackup >= 5.1.0b1
Requires:       python3-azure-mgmt-redhatopenshift >= 1.1.0
Requires:       python3-azure-mgmt-redis >= 13.1.0
Requires:       python3-azure-mgmt-relay >= 0.1.0
Requires:       python3-azure-mgmt-reservations >= 2.0.0
Requires:       python3-azure-mgmt-resource >= 21.1.0
Requires:       python3-azure-mgmt-search >= 8.0
Requires:       python3-azure-mgmt-security >= 2.0.0b1
Requires:       python3-azure-mgmt-servicebus >= 8.1.0
Requires:       python3-azure-mgmt-servicefabric >= 1.0.0
Requires:       python3-azure-mgmt-servicefabricmanagedclusters >= 1.0.0
Requires:       python3-azure-mgmt-servicelinker >= 1.0.0
Requires:       python3-azure-mgmt-signalr >= 1.1.0
Requires:       python3-azure-mgmt-sql >= 4.0.0b5
Requires:       python3-azure-mgmt-sqlvirtualmachine >= 1.0.0b4
Requires:       python3-azure-mgmt-storage >= 21.0.0
Requires:       python3-azure-mgmt-synapse >= 2.1.0b5
Requires:       python3-azure-mgmt-trafficmanager >= 1.0.0
Requires:       python3-azure-mgmt-web >= 7.0.0
Requires:       python3-azure-multiapi-storage >= 0.10.0
Requires:       python3-azure-storage-common >= 1.4
Requires:       python3-azure-synapse-accesscontrol >= 0.5.0
Requires:       python3-azure-synapse-artifacts >= 0.14.0
Requires:       python3-azure-synapse-managedprivateendpoints >= 0.3.0
Requires:       python3-azure-synapse-spark >= 0.2.0
Requires:       python3-chardet >= 3.0.4
Requires:       python3-colorama >= 0.4.4
Requires:       python3-distro
Requires:       python3-javaproperties >= 0.5.1
Requires:       python3-jsondiff >= 2.0.0
Requires:       python3-packaging >= 20.9
Requires:       python3-pydocumentdb >= 2.0.1
Requires:       python3-pygments >= 2.4
Requires:       python3-scp >= 0.13.2
Requires:       python3-semver >= 2.13.0
Requires:       python3-six >= 1.10.0
Requires:       python3-sshtunnel >= 0.1.4
Requires:       python3-urllib3
Requires:       python3-websocket-client >= 1.3.1
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
set +x
for i in $(az | sed -n 's/\s*\([a-z,-]*\)\s\+\:.*/\1/p') ; do
    echo -n "Testing $i command .. "
    if az $i --help > /dev/null 2>&1 ; then
	echo "OK"
    else
	echo "FAIL"
    fi
done
set -x
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
install -DTm644 %{buildroot}%{_bindir}/az.completion.sh %{buildroot}%{_datadir}/bash-completion/completions/az
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
%{_datadir}/bash-completion/completions/az
%exclude /usr/bin/az.bat
%exclude /usr/bin/az.completion.sh
%exclude /usr/bin/azps.ps1
%{python3_sitelib}/azure/cli
%{python3_sitelib}/azure_cli-*.egg-info
%endif

%changelog
