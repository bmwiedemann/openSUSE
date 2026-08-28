#
# spec file for package cosmic-settings
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


%define         appid com.system76.CosmicSettings
Name:           cosmic-settings
Version:        1.7.0
Release:        0
Summary:        COSMIC Settings
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-settings
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  llvm-devel
BuildRequires:  mold
BuildRequires:  pkgconfig
BuildRequires:  polkit
BuildRequires:  rust >= 1.90
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       NetworkManager-connection-editor
Requires:       NetworkManager-openvpn
Requires:       accountsservice
Requires:       cosmic-randr
Requires:       cosmic-settings-daemon
Requires:       iso-codes

%description
The settings application for the COSMIC desktop environment. Developed with
libcosmic, using the iced GUI library.

%prep
%autosetup -a1

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
%fdupes %{buildroot}

%check
%{cargo_test}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/applications/%{appid}.{About,Accessibility,Appearance,Applications,Bluetooth,DateTime,DefaultApps,Desktop,Displays,Dock,Firmware,Input,LegacyApplications,Power,Keyboard,Mouse,Network,Notifications,Panel,RegionLanguage,Sound,StartupApps,System,Time,Touchpad,Users,Vpn,Wallpaper,WindowManagement,Wired,Wireless,Workspaces}.desktop
%{_datadir}/cosmic
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/icons/hicolor/scalable/status/*.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/polkit-1/actions/%{appid}.Users.policy
%{_datadir}/polkit-1/rules.d/%{name}.rules

%changelog
