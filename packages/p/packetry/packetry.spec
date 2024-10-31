#
# spec file for package packetry
#
# Copyright (c) 2022-2024, Martin Hauke <mardnh@gmx.de>
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


Name:           packetry
Version:        0.4.0
Release:        0
Summary:        USB protocol analysis application
License:        BSD-3-Clause
Group:          Hardware/Modem
#Git-Clone:     https://github.com/greatscottgadgets/packetry.git
URL:            https://github.com/greatscottgadgets/packetry
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
Patch0:         packetry-fix-desktop-file.patch
BuildRequires:  ImageMagick
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.36.8
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4) >= 4.0.0
BuildRequires:  pkgconfig(pango) >= 1.46

%description
A fast, intuitive USB 2.0 protocol analysis application for use
with Cynthion.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
%{cargo_install}

install -Dm 0644 appimage/dist/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
for size in 256 128 96 64 48 32 16; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$size"x$size/apps"
    magick convert -strip appimage/dist/icon.png -resize "$size"x"$size" %{buildroot}%{_datadir}/icons/hicolor/$size"x$size/apps/%{name}.png"
done
install -Dm 0644 appimage/dist/packetry.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/packetry
%{_bindir}/packetry-cli
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
