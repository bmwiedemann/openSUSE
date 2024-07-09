#
# spec file for package azure-cli-core
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

Name:           azure-cli-core
Version:        2.62.0
Release:        0
Summary:        Microsoft Azure CLI Core Module
License:        MIT
Group:          System/Management
URL:            https://github.com/Azure/azure-cli
Source:         https://files.pythonhosted.org/packages/source/a/azure-cli-core/azure_cli_core-%{version}.tar.gz
Source1:        LICENSE.txt
Patch0:         acc_disable-update-check.patch
BuildRequires:  %{pythons}-azure-nspkg >= 3.0.0
BuildRequires:  %{pythons}-pip
BuildRequires:  %{pythons}-setuptools
BuildRequires:  %{pythons}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{pythons}-PyJWT >= 2.1.0
Requires:       %{pythons}-argcomplete < 4.0
Requires:       %{pythons}-argcomplete >= 3.3.0
Requires:       %{pythons}-azure-mgmt-core < 2.0.0
Requires:       %{pythons}-azure-mgmt-core >= 1.2.0
Requires:       %{pythons}-azure-nspkg >= 3.0.0
Requires:       %{pythons}-cryptography
Requires:       %{pythons}-humanfriendly < 11.0
Requires:       %{pythons}-humanfriendly >= 10.0
Requires:       %{pythons}-jmespath
Requires:       %{pythons}-knack < 1.0.0
Requires:       %{pythons}-knack >= 0.11.0
Requires:       %{pythons}-msal < 2.0.0
Requires:       %{pythons}-msal >= 1.28.1
Requires:       %{pythons}-msal-extensions < 2.0.0
Requires:       %{pythons}-msal-extensions >= 1.2.0~b1
Requires:       %{pythons}-msrestazure < 0.7.0
Requires:       %{pythons}-msrestazure >= 0.6.4
Requires:       %{pythons}-packaging >= 20.9
Requires:       %{pythons}-paramiko < 4.0.0
Requires:       %{pythons}-paramiko >= 2.0.8
Requires:       %{pythons}-pip
Requires:       %{pythons}-pkginfo >= 1.5.0.1
Requires:       %{pythons}-psutil < 6.0
Requires:       %{pythons}-psutil >= 5.9
Requires:       %{pythons}-pyOpenSSL >= 17.1.0
Requires:       %{pythons}-requests < 3.0.0
Requires:       %{pythons}-requests >= 2.25.1
Requires:       %{pythons}-wheel >= 0.30.0
Requires:       azure-cli-telemetry >= 1.1.0
Conflicts:      azure-cli < 2.0.0

BuildArch:      noarch

%description
Microsoft Azure CLI Core Module

%prep
%autosetup -p1 -n azure_cli_core-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-cli-core-%{version}
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{_sitelibdir}

%files
%defattr(-,root,root,-)
%doc HISTORY.rst README.rst
%license LICENSE.txt
%dir %{_sitelibdir}/azure/cli
%{_sitelibdir}/azure/cli/core
%{_sitelibdir}/azure_cli_core-*.dist-info

%changelog
