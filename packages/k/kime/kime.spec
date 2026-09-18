#
# spec file for package kime
#
# Copyright (c) 2026 SUSE LLC
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

Name:           kime
Version:        3.2.0
Release:        0
Summary:        Korean IME
License:        GPL-3.0-or-later
Group:          System/I18n/Korean
URL:            https://github.com/Riey/kime
Source:         https://github.com/Riey/kime/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Patch0:         0001-meson-cargo-frozen.patch

BuildRequires:  cargo
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  llvm-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-base-private-devel
BuildRequires:  update-desktop-files

%description
Kime is a fast Korean Input Method Engine for Linux.
Supports GTK3/4, Qt5/6, XIM and Wayland.

%package devel
Summary:        Development files for kime
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development files (headers and library) for kime Korean Input Method Engine.

%package gtk3
Summary:        GTK3 input module for kime
Group:          System/I18n/Korean
Requires:       %{name} = %{version}
Supplements:    (%{name} and libgtk-3-0)

%description gtk3
GTK3 input module for kime Korean Input Method Engine.

%package gtk4
Summary:        GTK4 input module for kime
Group:          System/I18n/Korean
Requires:       %{name} = %{version}
Supplements:    (%{name} and libgtk-4-1)

%description gtk4
GTK4 input module for kime Korean Input Method Engine.

%package qt5
Summary:        Qt5 input module for kime
Group:          System/I18n/Korean
Requires:       %{name} = %{version}
Supplements:    (%{name} and libQt5Gui5)

%description qt5
Qt5 input module for kime Korean Input Method Engine.

%package qt6
Summary:        Qt6 input module for kime
Group:          System/I18n/Korean
Requires:       %{name} = %{version}
Supplements:    (%{name} and libQt6Gui6)

%description qt6
Qt6 input module for kime Korean Input Method Engine.

%prep
%autosetup -p1 -a1

# Fix vendor checksum for config.guess/config.sub (non-x86_64 builds)
# Define function once, call multiple times
fix_vendor_checksums() {
    for checksum_file in $(find vendor -name ".cargo-checksum.json" 2>/dev/null); do
        pkg_dir=$(dirname "$checksum_file")
        for config_file in $(find "$pkg_dir" -name "config.guess" -o -name "config.sub" 2>/dev/null); do
            rel_path="${config_file#$pkg_dir/}"
            actual_checksum=$(sha256sum "$config_file" | cut -d' ' -f1)
            escaped_path=$(echo "$rel_path" | sed 's/\//\\\//g')
            sed -i "s/\"$escaped_path\":\"[^\"]*\"/\"$escaped_path\":\"$actual_checksum\"/g" "$checksum_file"
        done
    done
}
fix_vendor_checksums

sed -i 's|#!/usr/bin/env sh|#!/bin/sh|g' res/kime-xdg-autostart

%build
export LIBCLANG_PATH=$(llvm-config --libdir)

# Re-define function (RPM sections run in separate shells)
fix_vendor_checksums() {
    for checksum_file in $(find vendor -name ".cargo-checksum.json" 2>/dev/null); do
        pkg_dir=$(dirname "$checksum_file")
        for config_file in $(find "$pkg_dir" -name "config.guess" -o -name "config.sub" 2>/dev/null); do
            rel_path="${config_file#$pkg_dir/}"
            actual_checksum=$(sha256sum "$config_file" | cut -d' ' -f1)
            escaped_path=$(echo "$rel_path" | sed 's/\//\\\//g')
            sed -i "s/\"$escaped_path\":\"[^\"]*\"/\"$escaped_path\":\"$actual_checksum\"/g" "$checksum_file"
        done
    done
}

fix_vendor_checksums

%meson \
    -Dgtk3=enabled \
    -Dgtk4=enabled \
    -Dqt5=enabled \
    -Dqt6=enabled \
    -Dcheck=enabled \
    -Dindicator=enabled \
    -Dcandidate_window=enabled \
    -Dxim=enabled \
    -Dwayland=enabled \
    -Dsystem_engine=false \
    -Dcargo_profile=release \
    -Dinstall_headers=true \
    -Dinstall_docs=false \
    -Dqt5_plugindir=%{_libdir}/qt5/plugins \
    -Dqt6_plugindir=%{_libdir}/qt6/plugins
%meson_build

%install
%meson_install
mv %{buildroot}%{_libdir}/gtk-3.0/3.0.0/immodules/libim-kime.so \
   %{buildroot}%{_libdir}/gtk-3.0/3.0.0/immodules/im-kime.so
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/kime.desktop

%check
cargo test --frozen -p kime-engine-core

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md README.ko.md NOTICE.md docs/CHANGELOG.md docs/CONFIGURATION.md docs/CONFIGURATION.ko.md res/default_config.yaml
%{_bindir}/kime*
%{_libdir}/libkime_engine.so
%{_datadir}/applications/kime.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/kime.desktop
%{_datadir}/icons/hicolor/64x64/apps/kime-*.png

%files devel
%{_includedir}/kime_engine.h
%{_includedir}/kime_engine.hpp

%files gtk3
%dir %{_libdir}/gtk-3.0
%dir %{_libdir}/gtk-3.0/3.0.0
%dir %{_libdir}/gtk-3.0/3.0.0/immodules
%{_libdir}/gtk-3.0/3.0.0/immodules/im-kime.so

%files gtk4
%dir %{_libdir}/gtk-4.0
%dir %{_libdir}/gtk-4.0/4.0.0
%dir %{_libdir}/gtk-4.0/4.0.0/immodules
%{_libdir}/gtk-4.0/4.0.0/immodules/libkime-gtk4.so

%files qt5
%dir %{_libdir}/qt5
%dir %{_libdir}/qt5/plugins
%dir %{_libdir}/qt5/plugins/platforminputcontexts
%{_libdir}/qt5/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

%files qt6
%dir %{_libdir}/qt6
%dir %{_libdir}/qt6/plugins
%dir %{_libdir}/qt6/plugins/platforminputcontexts
%{_libdir}/qt6/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

%changelog
