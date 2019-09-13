#
# spec file for package azure-cli-monitor
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


Name:           azure-cli-monitor
Version:        0.2.10
Release:        0
Summary:        Microsoft Azure CLI 'Monitor' Command Module
License:        MIT
Group:          System/Management
Url:            https://github.com/Azure/azure-cli
Source:         https://files.pythonhosted.org/packages/source/a/azure-cli-monitor/azure-cli-monitor-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  azure-cli-command-modules-nspkg
BuildRequires:  azure-cli-nspkg
BuildRequires:  fdupes
BuildRequires:  python3-azure-nspkg >= 3.0.0
BuildRequires:  python3-setuptools
Requires:       azure-cli-command-modules-nspkg
Requires:       azure-cli-core
Requires:       azure-cli-nspkg
Requires:       python3-azure-mgmt-monitor >= 0.5.2
Requires:       python3-azure-nspkg >= 3.0.0
Conflicts:      azure-cli < 2.0.0

BuildArch:      noarch

%description
Microsoft Azure CLI 'Monitor' Command Module

This package is for the 'monitor' module.
i.e. 'az monitor'

%prep
%setup -q -n azure-cli-monitor-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-cli-monitor-%{version}
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
%{python3_sitelib}/azure/cli/command_modules/monitor
%{python3_sitelib}/azure_cli_monitor-*.egg-info

%changelog
