#
# spec file for package lumine-capture
#
# Copyright (c) 2026 Netflate <netflate@gmail.com>
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


Name:           lumine-capture
Version:        0.3.0
Release:        0
Summary:        Screenshot and annotation tool for Wayland with built-in OCR
License:        (Apache-2.0 OR MIT) AND OFL-1.1
URL:            https://github.com/Netflate/LumineCapture
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  onnxruntime-devel
BuildRequires:  rust >= 1.88
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xkbcommon)
ExclusiveArch:  x86_64 aarch64

%description
LumineCapture is a fast, lightweight screenshot tool for Wayland.
It starts quickly without a background daemon and opens captures in
a GUI editor.

It captures the whole workspace, a monitor, a region or a window
(KDE Plasma only for now). The editor has basic annotations, blur,
pixelation and a color picker; screenshots can be copied, saved or
pinned on screen.

Built-in offline OCR (PaddleOCR) lets you select and copy text
straight from a screenshot. Models are downloaded from the GUI.

Works on most Wayland compositors, including KDE Plasma, COSMIC,
niri and Hyprland. GNOME is not supported yet.

%prep
%autosetup -a1 -n LumineCapture-%{version}

%build
# link the system ONNX Runtime instead of downloading one
export ORT_LIB_LOCATION=%{_libdir}
export ORT_PREFER_DYNAMIC_LINK=1
%{cargo_build}

%install
install -D -p -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
# KWin grants screenshot access by the Exec= path of this file, so it has to be /usr/bin/lumine-capture
install -D -p -m 0644 assets/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
for icon in assets/hicolor/*/apps/*; do
    install -D -p -m 0644 "$icon" "%{buildroot}%{_datadir}/icons/${icon#assets/}"
done

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
export ORT_LIB_LOCATION=%{_libdir}
export ORT_PREFER_DYNAMIC_LINK=1
%{cargo_test} --release

%files
%license LICENSE-MIT LICENSE-APACHE assets/fonts/LICENSE-OFL.txt
%doc README.md docs/lumine-capture-shortcuts-kde.kksrc
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/lumine-capture.*
%{_datadir}/icons/hicolor/*/apps/lumine-pin.*

%changelog
