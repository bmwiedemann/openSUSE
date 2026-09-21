#
# spec file for package 86Box
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


Name:           86Box
Version:        6.0
Release:        1
Summary:        Emulator of x86-based machines based on PCem
License:        GPL-2.0-or-later
URL:            https://86box.net/
Source0:        https://github.com/86Box/86Box/archive/refs/tags/v%{version}.tar.gz#/86Box-%{version}.tar.gz
BuildRequires:  cmake >= 3.21
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(rtmidi)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(slirp)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(zlib)
Recommends:     fluid-soundfont-gm
Recommends:     fluidsynth
Recommends:     ghostscript
Recommends:     libgamemode0
ExclusiveArch:  x86_64

%description
86Box is a low level x86 emulator that runs older operating systems
and software designed for IBM PC systems and compatibles from 1981
through fairly recent system designs based on the PCI bus.

%prep
%autosetup -p1

%build
%cmake_qt6 \
	-DRELEASE=on \
	-DUSE_QT6=on \
	-DDISCORD=off
%{qt6_build}

%install
%{qt6_install}

# Icons
for i in 48 64 72 128 256; do
    install -Dpm 0644 src/unix/assets/${i}x${i}/net.86box.86Box.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done
# Desktop file
mkdir -p %{buildroot}%{_datadir}/applications
install -Dpm 0644 src/unix/assets/net.86box.86Box.desktop %{buildroot}%{_datadir}/applications/net.86box.86Box.desktop
%suse_update_desktop_file -r net.86box.86Box Emulator

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/net.86box.86Box.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
