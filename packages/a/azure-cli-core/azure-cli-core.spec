#
# spec file for package azure-cli-core
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


Name:           azure-cli-core
Version:        2.43.0
Release:        0
Summary:        Microsoft Azure CLI Core Module
License:        MIT
Group:          System/Management
URL:            https://github.com/Azure/azure-cli
Source:         https://files.pythonhosted.org/packages/source/a/azure-cli-core/azure-cli-core-%{version}.tar.gz
Source1:        LICENSE.txt
Patch0:         acc_disable-update-check.patch
Patch1:         acc_update-argcomplete.patch
BuildRequires:  azure-cli-nspkg
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-azure-nspkg >= 3.0.0
BuildRequires:  python3-setuptools
Requires:       azure-cli-nspkg
Requires:       azure-cli-telemetry >= 1.0.8
Requires:       python3-PyJWT >= 2.1.0
Requires:       python3-argcomplete < 3.0
Requires:       python3-argcomplete >= 2.0
Requires:       python3-azure-mgmt-core < 2.0.0
Requires:       python3-azure-mgmt-core >= 1.2.0
Requires:       python3-azure-nspkg >= 3.0.0
Requires:       python3-cryptography
Requires:       python3-humanfriendly < 11.0
Requires:       python3-humanfriendly >= 10.0
Requires:       python3-jmespath
Requires:       python3-knack < 1.0.0
Requires:       python3-knack >= 0.10.0
Requires:       python3-msal < 2.0.0
Requires:       python3-msal >= 1.20.0
Requires:       python3-msal-extensions < 2.0.0
Requires:       python3-msal-extensions >= 1.0.0
Requires:       python3-msrestazure < 0.7.0
Requires:       python3-msrestazure >= 0.6.4
Requires:       python3-packaging < 22.0
Requires:       python3-packaging >= 20.9
Requires:       python3-paramiko < 3.0.0
Requires:       python3-paramiko >= 2.0.8
Requires:       python3-pip
Requires:       python3-pkginfo >= 1.5.0.1
Requires:       python3-psutil < 6.0
Requires:       python3-psutil >= 5.9
Requires:       python3-pyOpenSSL >= 17.1.0
Requires:       python3-requests < 3.0.0
Requires:       python3-requests >= 2.25.1
Requires:       python3-wheel >= 0.30.0
%if %{python3_version_nodots} < 34
Requires:       python-enum34 >= 1.0.4
%endif
Conflicts:      azure-cli < 2.0.0

BuildArch:      noarch

%description
Microsoft Azure CLI Core Module

%prep
%setup -q -n azure-cli-core-%{version}
%patch0 -p1
%patch1 -p1

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-cli-core-%{version}
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
%{python3_sitelib}/azure/cli/core
%{python3_sitelib}/azure_cli_core-*.egg-info

%changelog
