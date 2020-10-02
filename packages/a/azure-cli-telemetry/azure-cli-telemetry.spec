#
# spec file for package azure-cli-telemetry
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


Name:           azure-cli-telemetry
Version:        1.0.6
Release:        0
Summary:        Microsoft Azure CLI Telemetry Package
License:        MIT
Group:          System/Management
URL:            https://github.com/Azure/azure-cli
Source:         https://files.pythonhosted.org/packages/source/a/azure-cli-telemetry/azure-cli-telemetry-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  azure-cli-nspkg
BuildRequires:  fdupes
BuildRequires:  python3-azure-nspkg >= 3.0.0
BuildRequires:  python3-setuptools
Requires:       azure-cli-nspkg
Requires:       python3-applicationinsights < 0.12
Requires:       python3-applicationinsights >= 0.11.1
Requires:       python3-azure-nspkg >= 3.0.0
Requires:       python3-portalocker < 2.0
Requires:       python3-portalocker >= 1.2
Conflicts:      azure-cli < 2.0.0

BuildArch:      noarch

%description
Microsoft Azure CLI Telemetry Package

This is the Microsoft Azure CLI Telemetry package. It is not intended to be installed directly by the end user.

This package includes:
1. Support API for Azure CLI to gather telemetry.
2. Telemetry upload process.

%prep
%setup -q -n azure-cli-telemetry-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-cli-telemetry-%{version}
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix} --install-lib=%{python3_sitelib}
%fdupes %{buildroot}%{python3_sitelib}
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/__init__.*
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/__pycache__
rm -rf %{buildroot}%{python3_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{python3_sitelib}/azure/__pycache__

%files
%defattr(-,root,root,-)
%doc HISTORY.rst README.rst
%license LICENSE.txt
%{python3_sitelib}/azure/cli/telemetry
%{python3_sitelib}/azure_cli_telemetry-*.egg-info

%changelog
