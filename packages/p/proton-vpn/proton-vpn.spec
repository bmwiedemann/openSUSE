#
# spec file for package proton-vpn
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
%global pythons python3
%else
%global pythons python311
%endif
Name:           proton-vpn
Version:        4.2.0
Release:        0
Summary:        Official Proton VPN client
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://github.com/ProtonVPN/proton-vpn-gtk-app
Source:         https://github.com/ProtonVPN/proton-vpn-gtk-app/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  gtk3-devel
BuildRequires:  python-rpm-macros
BuildRequires:  %{pythons}-dbus-python
BuildRequires:  %{pythons}-gobject
BuildRequires:  %{pythons}-packaging
BuildRequires:  %{pythons}-proton-vpn-api-core >= 0.21.0
BuildRequires:  %{pythons}-proton-vpn-connection >= 0.14.2
BuildRequires:  %{pythons}-proton-vpn-killswitch-network-manager
BuildRequires:  %{pythons}-proton-vpn-logger
BuildRequires:  %{pythons}-proton-vpn-network-manager-openvpn
BuildRequires:  %{pythons}-pycairo
BuildRequires:  %{pythons}-pytest
BuildRequires:  %{pythons}-pytest-cov
BuildRequires:  %{pythons}-setuptools
BuildRequires:  update-desktop-files
Requires:       gtk3
Requires:       %{pythons}-dbus-python
Requires:       %{pythons}-gobject
Requires:       %{pythons}-packaging
Requires:       %{pythons}-proton-vpn-api-core
Requires:       %{pythons}-proton-vpn-connection >= 0.14.2
Requires:       %{pythons}-proton-vpn-killswitch-network-manager
Requires:       %{pythons}-proton-vpn-logger
Requires:       %{pythons}-proton-vpn-network-manager-openvpn
Requires:       %{pythons}-pycairo
Conflicts:      protonvpn-gui
Provides:       protonvpn-app = %{version}
BuildArch:      noarch

%description
The Proton VPN client is easy to use and packed with advanced features
carefully designed to improve your online security.

%prep
%setup -q -n proton-vpn-gtk-app-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}/

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
mkdir -p %{buildroot}/%{_datadir}/applications
cp rpmbuild/SOURCES/proton-vpn-logo.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/proton-vpn.svg

%suse_update_desktop_file -c proton-vpn "Proton VPN" "Proton VPN Client" protonvpn-app proton-vpn "GTK;Network;Utility"

%check
# ignore UI tests as they segfault with no desktop env
%pytest tests/unit --ignore=tests/unit/widgets/

%files
%doc README.md
%license LICENSE COPYING.md
%{_datadir}/applications/proton-vpn.desktop
%{_datadir}/icons/hicolor/*/apps/proton-vpn.*
%{python3_sitelib}/proton/
%{python3_sitelib}/proton_vpn_gtk_app-%{version}*.egg-info
%{_bindir}/protonvpn-app

%changelog
