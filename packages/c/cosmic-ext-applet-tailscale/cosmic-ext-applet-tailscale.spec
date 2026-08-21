#
# spec file for package cosmic-ext-applet-tailscale
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


%define         appid com.bhh32.gui-scale-applet
Name:           cosmic-ext-applet-tailscale
Version:        3.10.2
Release:        0
Summary:        Tailscale applet for the COSMIC Desktop
License:        BSD-3-Clause
URL:            https://github.com/cosmic-utils/gui-scale-applet
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.96
BuildRequires:  pkgconfig(xkbcommon)

%description
This is a COSMIC applet for Tailscale. It has SSH and Allow Routes
enable/disable and Tail Drop functionality.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
install -Dpm0755 ./target/release/gui-scale-applet -t %{buildroot}%{_bindir}
install -Dpm0644 data/%{appid}.metainfo.xml -t %{buildroot}%{_datadir}/metainfo
install -Dpm0644 data/%{appid}.desktop -t %{buildroot}%{_datadir}/applications
install -Dpm0644 data/icons/scalable/apps/%{appid}.png -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

%files
%license LICENSE
%doc README.md
%{_bindir}/gui-scale-applet
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.png
%{_datadir}/metainfo/%{appid}.metainfo.xml

%changelog
