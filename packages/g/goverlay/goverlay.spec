#
# spec file for package goverlay
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


Name:           goverlay
Version:        1.8.10
Release:        0
Summary:        Graphical UI to help manage overlays
License:        GPL-3.0-or-later
URL:            https://github.com/benjamimgois/goverlay
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE goverlay-build-flags.patch - Adjust build flags for RPM packaging (debuginfo and PIE)
Patch0:         goverlay-build-flags.patch
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  lazarus
BuildRequires:  libQt6Pas-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(sdl2)
ExclusiveArch:  x86_64 aarch64
Requires:       7zip
Requires:       mangohud
# Nerd symbols is necessary to show icons in goverlay interface
Requires:       symbols-only-nerd-fonts
Requires:       wget
Recommends:     Mesa-demo
Recommends:     vkSumi
Recommends:     vkbasalt
Recommends:     vulkan-tools
%if 0%{?suse_version} > 1500
BuildRequires:  lazarus-lcl-qt6
%endif
Provides:       pascube = %{version}
Obsoletes:      pascube <= 1.7.0

%description
GOverlay is a graphical UI to manage Vulkan/OpenGL overlays.

%prep
%autosetup -p1
chmod -x LICENSE README.md
sed -i '1s|^#!/usr/bin/env python3|#!/usr/bin/python3|' assets/goverlay-steam-shortcut.py

%build
%{set_build_flags}
%make_build

%install
%make_install prefix=%{_prefix} libexecdir=/%{_lib}
install -d %{buildroot}%{_libexecdir}/goverlay
sed -i \
    -e 's/^StartupWMClass=.*/StartupWMClass=goverlay/' \
    %{buildroot}%{_datadir}/applications/io.github.benjamimgois.goverlay.desktop
strip -s %{buildroot}%{_bindir}/goverlay 2>/dev/null || strip -s %{buildroot}%{_libdir}/goverlay 2>/dev/null || true
strip -s %{buildroot}%{_libdir}/bgmod/bgmod 2>/dev/null || true
strip -s %{buildroot}%{_libdir}/bgmod/bgmod-uninstaller 2>/dev/null || true
strip -s %{buildroot}%{_libdir}/pascube 2>/dev/null || true
rm -rf %{buildroot}%{_datadir}/goverlay/data/icons/{128x128,256x256,512x512}
ln -sf %{_datadir}/icons/hicolor/128x128/apps/io.github.benjamimgois.goverlay.png \
       %{buildroot}%{_datadir}/goverlay/assets/icons/goverlay.png
%fdupes %{buildroot}%{_datadir}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_libdir}/bgmod
%{_libdir}/bgmod-uninstaller
%{_libdir}/pascube
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*%{name}.png
%{_datadir}/metainfo/io.github.benjamimgois.%{name}.metainfo.xml

%changelog
