#
# spec file for package azure-cli
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        2.0.75
Release:        0
Summary:        Microsoft Azure CLI 2.0
License:        MIT
Group:          System/Management
Url:            https://github.com/Azure/azure-cli
Source:         https://files.pythonhosted.org/packages/source/a/azure-cli/azure-cli-%{version}.tar.gz
Source1:        LICENSE.txt
Patch1:         ac_use-python3-by-default.patch
%if 0%{?_test}
BuildRequires:  %{short_name} = %{version}
%else
BuildRequires:  fdupes
BuildRequires:  python3-azure-nspkg >= 3.0.0
BuildRequires:  python3-setuptools
Requires:       azure-cli-acr >= 2.2.9
Requires:       azure-cli-acs >= 2.4.4
Requires:       azure-cli-advisor >= 2.0.1
Requires:       azure-cli-ams >= 0.4.7
Requires:       azure-cli-appservice >= 0.2.21
Requires:       azure-cli-backup >= 1.2.5
Requires:       azure-cli-batch >= 4.0.3
Requires:       azure-cli-batchai >= 0.4.10
Requires:       azure-cli-billing >= 0.2.2
Requires:       azure-cli-botservice >= 0.2.2
Requires:       azure-cli-cdn >= 0.2.4
Requires:       azure-cli-cloud >= 2.1.1
Requires:       azure-cli-cognitiveservices >= 0.2.6
Requires:       azure-cli-command-modules-nspkg >= 2.0.3
Requires:       azure-cli-component >= 2.0.8
Requires:       azure-cli-configure >= 2.0.24
Requires:       azure-cli-consumption >= 0.4.4
Requires:       azure-cli-container >= 0.3.18
Requires:       azure-cli-core >= 2.0.75
Requires:       azure-cli-cosmosdb >= 0.2.11
Requires:       azure-cli-deploymentmanager >= 0.1.1
Requires:       azure-cli-dla >= 0.2.6
Requires:       azure-cli-dls >= 0.1.10
Requires:       azure-cli-dms >= 0.1.4
Requires:       azure-cli-eventgrid >= 0.2.4
Requires:       azure-cli-eventhubs >= 0.3.7
Requires:       azure-cli-extension >= 0.2.5
Requires:       azure-cli-feedback >= 2.2.1
Requires:       azure-cli-find >= 0.3.4
Requires:       azure-cli-hdinsight >= 0.3.5
Requires:       azure-cli-interactive >= 0.4.5
Requires:       azure-cli-iot >= 0.3.11
Requires:       azure-cli-iotcentral >= 0.1.7
Requires:       azure-cli-keyvault >= 2.2.16
Requires:       azure-cli-kusto >= 0.2.3
Requires:       azure-cli-lab >= 0.1.8
Requires:       azure-cli-maps >= 0.3.5
Requires:       azure-cli-monitor >= 0.2.15
Requires:       azure-cli-natgateway >= 0.1.1
Requires:       azure-cli-network >= 2.5.2
Requires:       azure-cli-nspkg >= 3.0.4
Requires:       azure-cli-policyinsights >= 0.1.4
Requires:       azure-cli-privatedns >= 1.0.2
Requires:       azure-cli-profile >= 2.1.5
Requires:       azure-cli-rdbms >= 0.3.12
Requires:       azure-cli-redis >= 0.4.4
Requires:       azure-cli-relay >= 0.1.5
Requires:       azure-cli-reservations >= 0.4.3
Requires:       azure-cli-resource >= 2.1.16
Requires:       azure-cli-role >= 2.6.4
Requires:       azure-cli-search >= 0.1.2
Requires:       azure-cli-security >= 0.1.2
Requires:       azure-cli-servicebus >= 0.3.6
Requires:       azure-cli-servicefabric >= 0.1.20
Requires:       azure-cli-signalr >= 1.0.1
Requires:       azure-cli-sql >= 2.2.5
Requires:       azure-cli-sqlvm >= 0.2.0
Requires:       azure-cli-storage >= 2.4.3
Requires:       azure-cli-telemetry >= 1.0.4
Requires:       azure-cli-vm >= 2.2.23
Requires:       python3-azure-nspkg >= 3.0.0
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
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/command_modules
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
