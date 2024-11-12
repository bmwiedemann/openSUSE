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
Version:        4.7.4
Release:        0
Summary:        Official Proton VPN client
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://github.com/ProtonVPN/proton-vpn-gtk-app
Source:         https://github.com/ProtonVPN/proton-vpn-gtk-app/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module proton-core}
BuildRequires:  %{python_module proton-vpn-api-core >= 0.25.0}
BuildRequires:  %{python_module proton-vpn-network-manager}
BuildRequires:  %{python_module pycairo}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  gtk3-devel
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
Requires:       %{pythons}-dbus-python
Requires:       %{pythons}-distro
Requires:       %{pythons}-gobject
Requires:       %{pythons}-packaging
Requires:       %{pythons}-proton-core
Requires:       %{pythons}-proton-vpn-api-core >= 0.35.2
Requires:       %{pythons}-proton-vpn-network-manager >= 0.9.1
Requires:       %{pythons}-pycairo
Requires:       %{pythons}-requests
Requires:       gtk3
Conflicts:      protonvpn-gui
Provides:       protonvpn-app = %{version}
BuildArch:      noarch

%description
The Proton VPN client is easy to use and packed with advanced features
carefully designed to improve your online security.

%prep
%setup -q -n proton-vpn-gtk-app-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%fdupes %{buildroot}%{python_sitelib}/

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
%{python_sitelib}/proton/
%{python_sitelib}/proton_vpn_gtk_app-%{version}*.egg-info
%{_bindir}/protonvpn-app

%changelog
