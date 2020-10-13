#
# spec file for package azure-cli-core
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


Name:           azure-cli-core
Version:        2.13.0
Release:        0
Summary:        Microsoft Azure CLI Core Module
License:        MIT
Group:          System/Management
URL:            https://github.com/Azure/azure-cli
Source:         https://files.pythonhosted.org/packages/source/a/azure-cli-core/azure-cli-core-%{version}.tar.gz
Source1:        LICENSE.txt
Patch0:         acc_disable-update-check.patch
BuildRequires:  azure-cli-nspkg
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-azure-nspkg >= 3.0.0
BuildRequires:  python3-mock
BuildRequires:  python3-setuptools
Requires:       azure-cli-nspkg
Requires:       azure-cli-telemetry >= 1.0.6
Requires:       python3-PyJWT
Requires:       python3-PyYAML < 6.0
Requires:       python3-PyYAML >= 5.2
Requires:       python3-adal < 2.0
Requires:       python3-adal >= 1.2.3
Requires:       python3-argcomplete < 2.0
Requires:       python3-argcomplete >= 1.8
Requires:       python3-azure-mgmt-core < 2.0.0
Requires:       python3-azure-mgmt-core >= 1.2.0
Requires:       python3-azure-mgmt-resource < 16.0.0
Requires:       python3-azure-mgmt-resource >= 15.0.0
Requires:       python3-azure-nspkg >= 3.0.0
Requires:       python3-colorama >= 0.4.1
Requires:       python3-humanfriendly < 9.0
Requires:       python3-humanfriendly >= 4.7
Requires:       python3-jmespath
Requires:       python3-knack < 1.0.0
Requires:       python3-knack >= 0.7.2
Requires:       python3-msal < 2.0.0
Requires:       python3-msal >= 1.0.0
Requires:       python3-msal-extensions < 1.0.0
Requires:       python3-msal-extensions >= 0.1.3
Requires:       python3-msrest >= 0.4.4
Requires:       python3-msrestazure >= 0.6.3
Requires:       python3-paramiko < 3.0.0
Requires:       python3-paramiko >= 2.0.8
Requires:       python3-pip
Requires:       python3-pkginfo >= 1.5.0.1
Requires:       python3-pyOpenSSL >= 17.1.0
Requires:       python3-requests < 3.0.0
Requires:       python3-requests >= 2.22
Requires:       python3-six < 2.0.0
Requires:       python3-six >= 1.12
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
