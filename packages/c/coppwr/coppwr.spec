#
# spec file for package coppwr
#
# Copyright (c) 2025 mantarimay
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


%define appid   io.github.dimtpap.coppwr
Name:           coppwr
Version:        1.7.1
Release:        0
Summary:        Low level PipeWire control GUI
License:        GPL-3.0-or-later
URL:            https://github.com/dimtpap/coppwr
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  pipewire-devel
BuildRequires:  rust >= 1.70
ExclusiveArch:  x86_64 aarch64

%description
coppwr is a tool that provides low level control over the PipeWire
multimedia server.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
install -Dm755 "target/release/%{name}" "%{buildroot}%{_bindir}/%{name}"
install -Dm644 "assets/%{appid}.desktop" "%{buildroot}%{_datadir}/applications/%{appid}.desktop"
install -Dm644 "assets/%{appid}.metainfo.xml" "%{buildroot}%{_datadir}/metainfo/%{appid}.metainfo.xml"
install -Dm644 "assets/icon/scalable.svg" "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg"
install -Dm644 "assets/icon/512.png" "%{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{appid}.png"
install -Dm644 "assets/icon/256.png" "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{appid}.png"
install -Dm644 "assets/icon/128.png" "%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{appid}.png"
install -Dm644 "assets/icon/64.png" "%{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{appid}.png"
install -Dm644 "assets/icon/48.png" "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{appid}.png"
install -Dm644 "assets/icon/32.png" "%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{appid}.png"

%files
%license LICENSE*
%doc README*
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/icons/hicolor

%changelog
