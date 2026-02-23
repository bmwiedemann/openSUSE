#
# spec file for package librepods
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define         appid me.kavishdevar.librepods
Name:           librepods
Version:        0.1.0
Release:        0
Summary:        AirPods liberated from Apple's ecosystem
License:        AGPL-3.0-only
# Legal-Review-Notice: according to the flatpak metainfo, the project is AGPL-3.0-only
# you can find that file in linux-rust/flatpak
URL:            https://github.com/kavishdevar/librepods
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libpulse)
ExcludeArch:    %{arm32} %{ix86}

%description
LibrePods unlocks Apple's exclusive AirPods features on non-Apple devices. Get
access to noise control modes, adaptive transparency, ear detection, hearing
aid, customized transparency mode, battery status, and more - all the premium
features you paid for but Apple locked to their ecosystem.

%prep
%autosetup -a1 -n %{name}-%{version}/linux-rust

%build
%{cargo_build}

%install
install -t %{buildroot}%{_bindir} -Dpm0755 target/release/%{name}
install -Dpm0644 assets/icon.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{appid}.png
install -Dpm0644 assets/%{appid}.desktop %{buildroot}%{_datadir}/applications/%{appid}.desktop
install -Dpm0644 flatpak/%{appid}.metainfo.xml %{buildroot}%{_datadir}/metainfo/%{appid}.metainfo.xml

%files
%license ../LICENSE
%doc ../CHANGELOG.md ../FUNDING.yml ../README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{appid}.png
%{_datadir}/metainfo/%{appid}.metainfo.xml

%changelog
