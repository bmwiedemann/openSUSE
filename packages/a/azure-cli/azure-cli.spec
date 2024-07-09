#
# spec file for package azure-cli
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


%if 0%{?suse_version} >= 1600
%define pythons %{primary_python}
%else
%define pythons python311
%endif
%global _sitelibdir %{%{pythons}_sitelib}

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
Version:        2.62.0
Release:        0
Summary:        Microsoft Azure CLI 2.0
License:        MIT
Group:          System/Management
URL:            https://github.com/Azure/azure-cli
Source:         https://files.pythonhosted.org/packages/source/a/azure-cli/azure_cli-%{version}.tar.gz
Source1:        LICENSE.txt
Patch1:         ac_use-python3-by-default.patch
%if 0%{?_test}
BuildRequires:  %{short_name} = %{version}
%else
BuildRequires:  %{pythons}-pip
BuildRequires:  %{pythons}-wheel
BuildRequires:  azure-cli-core = %{version}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{pythons}-Fabric >= 3.2.2
Requires:       %{pythons}-PyGithub >= 1.38
Requires:       %{pythons}-PyNaCl >= 1.5.0
Requires:       %{pythons}-PyYAML >= 5.1
Requires:       %{pythons}-antlr4-python3-runtime >= 4.13.1
Requires:       %{pythons}-azure-appconfiguration >= 1.1.1
Requires:       %{pythons}-azure-batch >= 14.2.0
Requires:       %{pythons}-azure-cosmos >= 3.0.2
Requires:       %{pythons}-azure-data-tables >= 12.4.0
Requires:       %{pythons}-azure-datalake-store >= 0.0.49
Requires:       %{pythons}-azure-graphrbac >= 0.60.0
Requires:       %{pythons}-azure-keyvault-administration >= 4.4.0~b2
Requires:       %{pythons}-azure-keyvault-certificates >= 4.7.0
Requires:       %{pythons}-azure-keyvault-keys >= 4.9.0~b3
Requires:       %{pythons}-azure-keyvault-secrets >= 4.7.0
Requires:       %{pythons}-azure-mgmt-advisor >= 9.0.0
Requires:       %{pythons}-azure-mgmt-apimanagement >= 4.0.0
Requires:       %{pythons}-azure-mgmt-appconfiguration >= 3.0.0
Requires:       %{pythons}-azure-mgmt-appcontainers >= 2.0.0
Requires:       %{pythons}-azure-mgmt-applicationinsights >= 1.0.0
Requires:       %{pythons}-azure-mgmt-authorization >= 4.0.0
Requires:       %{pythons}-azure-mgmt-batch >= 17.3.0
Requires:       %{pythons}-azure-mgmt-batchai >= 7.0.0b1
Requires:       %{pythons}-azure-mgmt-billing >= 6.0.0
Requires:       %{pythons}-azure-mgmt-botservice >= 2.0.0b3
Requires:       %{pythons}-azure-mgmt-cdn >= 12.0.0
Requires:       %{pythons}-azure-mgmt-cognitiveservices >= 13.5.0
Requires:       %{pythons}-azure-mgmt-compute >= 31.0.0
Requires:       %{pythons}-azure-mgmt-containerinstance >= 10.1.0
Requires:       %{pythons}-azure-mgmt-containerregistry >= 10.3.0
Requires:       %{pythons}-azure-mgmt-containerservice >= 30.0.0
Requires:       %{pythons}-azure-mgmt-cosmosdb >= 9.5.1
Requires:       %{pythons}-azure-mgmt-databoxedge >= 1.0.0
Requires:       %{pythons}-azure-mgmt-datamigration >= 10.0.0
Requires:       %{pythons}-azure-mgmt-devtestlabs >= 2.2
Requires:       %{pythons}-azure-mgmt-dns >= 8.0.0
Requires:       %{pythons}-azure-mgmt-eventgrid >= 10.2.0
Requires:       %{pythons}-azure-mgmt-eventhub >= 10.1.0
Requires:       %{pythons}-azure-mgmt-extendedlocation >= 1.0.0b2
Requires:       %{pythons}-azure-mgmt-hdinsight >= 9.0.0
Requires:       %{pythons}-azure-mgmt-imagebuilder >= 1.3.0
Requires:       %{pythons}-azure-mgmt-iotcentral >= 10.0.0b1
Requires:       %{pythons}-azure-mgmt-iothub >= 3.0.0
Requires:       %{pythons}-azure-mgmt-iothubprovisioningservices >= 1.1.0
Requires:       %{pythons}-azure-mgmt-keyvault >= 10.3.0
Requires:       %{pythons}-azure-mgmt-kusto >= 0.3.0
Requires:       %{pythons}-azure-mgmt-loganalytics >= 13.0.0
Requires:       %{pythons}-azure-mgmt-managedservices >= 1.0
Requires:       %{pythons}-azure-mgmt-managementgroups >= 1.0.0
Requires:       %{pythons}-azure-mgmt-maps >= 2.0.0
Requires:       %{pythons}-azure-mgmt-marketplaceordering >= 1.1.0
Requires:       %{pythons}-azure-mgmt-media >= 9.0
Requires:       %{pythons}-azure-mgmt-monitor >= 5.0.0
Requires:       %{pythons}-azure-mgmt-msi >= 7.0.0
Requires:       %{pythons}-azure-mgmt-netapp >= 10.1.0
Requires:       %{pythons}-azure-mgmt-policyinsights >= 1.1.0b4
Requires:       %{pythons}-azure-mgmt-privatedns >= 1.0.0
Requires:       %{pythons}-azure-mgmt-rdbms >= 10.2.0b16
Requires:       %{pythons}-azure-mgmt-recoveryservices >= 3.0.0
Requires:       %{pythons}-azure-mgmt-recoveryservicesbackup >= 9.1.0
Requires:       %{pythons}-azure-mgmt-redhatopenshift >= 1.4.0
Requires:       %{pythons}-azure-mgmt-redis >= 14.3.0
Requires:       %{pythons}-azure-mgmt-reservations >= 2.0.0
Requires:       %{pythons}-azure-mgmt-resource >= 23.1.1
Requires:       %{pythons}-azure-mgmt-search >= 9.0
Requires:       %{pythons}-azure-mgmt-security >= 6.0.0
Requires:       %{pythons}-azure-mgmt-servicebus >= 8.2.0
Requires:       %{pythons}-azure-mgmt-servicefabric >= 2.1.0
Requires:       %{pythons}-azure-mgmt-servicefabricmanagedclusters >= 2.0.0~b6
Requires:       %{pythons}-azure-mgmt-servicelinker >= 1.2.0~b2
Requires:       %{pythons}-azure-mgmt-signalr >= 2.0.0~b1
Requires:       %{pythons}-azure-mgmt-sql >= 4.0.0b17
Requires:       %{pythons}-azure-mgmt-sqlvirtualmachine >= 1.0.0b5
Requires:       %{pythons}-azure-mgmt-storage >= 21.2.0
Requires:       %{pythons}-azure-mgmt-synapse >= 2.1.0b5
Requires:       %{pythons}-azure-mgmt-trafficmanager >= 1.0.0
Requires:       %{pythons}-azure-mgmt-web >= 7.2.0
Requires:       %{pythons}-azure-monitor-query >= 1.2.0
Requires:       %{pythons}-azure-multiapi-storage >= 1.2.0
Requires:       %{pythons}-azure-storage-common >= 1.4
Requires:       %{pythons}-azure-synapse-accesscontrol >= 0.5.0
Requires:       %{pythons}-azure-synapse-artifacts >= 0.19.0
Requires:       %{pythons}-azure-synapse-managedprivateendpoints >= 0.4.0
Requires:       %{pythons}-azure-synapse-spark >= 0.2.0
Requires:       %{pythons}-chardet >= 5.2.0
Requires:       %{pythons}-colorama >= 0.4.4
Requires:       %{pythons}-distro
Requires:       %{pythons}-javaproperties >= 0.5.1
Requires:       %{pythons}-jsondiff >= 2.0.0
Requires:       %{pythons}-packaging >= 20.9
Requires:       %{pythons}-pycomposefile >= 0.0.29
Requires:       %{pythons}-pygments >= 2.4
Requires:       %{pythons}-scp >= 0.13.2
Requires:       %{pythons}-semver >= 2.13.0
Requires:       %{pythons}-six >= 1.10.0
Requires:       %{pythons}-sshtunnel >= 0.1.4
Requires:       %{pythons}-tabulate
Requires:       %{pythons}-urllib3
Requires:       %{pythons}-websocket-client >= 1.3.1
Requires:       %{pythons}-xmltodict >= 0.12
Requires:       azure-cli-core = %{version}
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
%setup -q -n azure_cli-%{version}
%patch -P 1 -p1
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
%pyproject_wheel
%endif

%install
%if 0%{?_test}
# disable debug packages in package test to prevent error about missing files
%define debug_package %{nil}
%else
%pyproject_install
install -DTm644 %{buildroot}%{_bindir}/az.completion.sh %{buildroot}%{_datadir}/bash-completion/completions/az
%fdupes %{buildroot}%{_sitelibdir}
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
%{_sitelibdir}/azure/cli
%{_sitelibdir}/azure_cli-*.dist-info
%endif

%changelog
