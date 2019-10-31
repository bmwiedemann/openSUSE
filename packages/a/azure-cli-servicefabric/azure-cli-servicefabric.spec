#
# spec file for package azure-cli-servicefabric
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


Name:           azure-cli-servicefabric
Version:        0.1.20
Release:        0
Summary:        Microsoft Azure CLI Service Fabric Module
License:        MIT
Group:          System/Management
Url:            https://github.com/Azure/azure-cli
Source:         https://files.pythonhosted.org/packages/source/a/azure-cli-servicefabric/azure-cli-servicefabric-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  azure-cli-command-modules-nspkg
BuildRequires:  azure-cli-nspkg
BuildRequires:  fdupes
BuildRequires:  python3-azure-nspkg >= 3.0.0
BuildRequires:  python3-setuptools
Requires:       azure-cli-command-modules-nspkg
Requires:       azure-cli-core
Requires:       azure-cli-nspkg
Requires:       python3-azure-graphrbac >= 0.60.0
Requires:       python3-azure-keyvault >= 1.1.0
Requires:       python3-azure-mgmt-compute >= 5.0.0
Requires:       python3-azure-mgmt-keyvault >= 1.1.0
Requires:       python3-azure-mgmt-network >= 3.0.0
Requires:       python3-azure-mgmt-servicefabric >= 0.2.0
Requires:       python3-azure-mgmt-storage >= 3.3.0
Requires:       python3-azure-nspkg >= 3.0.0
Requires:       python3-pyOpenSSL
Conflicts:      azure-cli < 2.0.0

BuildArch:      noarch

%description
Microsoft Azure CLI Service Fabric Module

This package is for the `sf` module.
i.e. 'azure sf'

It contains commands that can be used to
manage Service Fabric clusters.

%prep
%setup -q -n azure-cli-servicefabric-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-cli-servicefabric-%{version}
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix} --install-lib=%{python3_sitelib}
%fdupes %{buildroot}%{python3_sitelib}
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/command_modules/__init__.*
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/command_modules/__pycache__
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/__init__.*
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/__pycache__
rm -rf %{buildroot}%{python3_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{python3_sitelib}/azure/__pycache__

%files
%defattr(-,root,root,-)
%doc HISTORY.rst README.rst
%license LICENSE.txt
%{python3_sitelib}/azure/cli/command_modules/servicefabric
%{python3_sitelib}/azure_cli_servicefabric-*.egg-info

%changelog
