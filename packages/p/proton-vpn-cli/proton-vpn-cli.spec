#
# spec file for package proton-vpn-cli
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         pythons python3
%define         _name proton_vpn_cli
Name:           proton-vpn-cli
Version:        0.1.7
Release:        0
Summary:        Official Proton VPN CLI
License:        GPL-3.0-or-later
URL:            https://github.com/ProtonVPN/proton-vpn-cli
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module dbus_fast}
BuildRequires:  %{python_module installer}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module proton-core}
BuildRequires:  %{python_module proton-keyring-linux}
BuildRequires:  %{python_module proton-vpn-api-core}
BuildRequires:  %{python_module proton-vpn-daemon}
BuildRequires:  %{python_module proton-vpn-local-agent}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tabulate}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{pythons}-click
Requires:       %{pythons}-dbus_fast
Requires:       %{pythons}-packaging
Requires:       %{pythons}-proton-core
Requires:       %{pythons}-proton-keyring-linux
Requires:       %{pythons}-proton-vpn-api-core
Requires:       %{pythons}-proton-vpn-daemon
Requires:       %{pythons}-proton-vpn-local-agent
Requires:       %{pythons}-tabulate
BuildArch:      noarch

%description
The Proton VPN CLI is intended for every Proton VPN service user.

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{$python_sitelib}

%files
%doc README.md
%license LICENSE COPYING.md
%{_bindir}/protonvpn
%{python_sitelib}/proton
%{python_sitelib}/%{_name}-%{version}.dist-info

%changelog
