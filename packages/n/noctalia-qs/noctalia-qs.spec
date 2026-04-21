#
# spec file for package noctalia-qs
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
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define         __builder ninja
Name:           noctalia-qs
Version:        0.0.12
Release:        0
Summary:        Flexible Qt/QML toolkit for Wayland shells
License:        LGPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/noctalia-dev/noctalia-qs
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  cli11-devel
BuildRequires:  cmake >= 3.22
BuildRequires:  cpptrace-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  jemalloc-devel
BuildRequires:  libgbm-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  qt6-base-private-devel
BuildRequires:  qt6-declarative-private-devel
BuildRequires:  qt6-wayland-private-devel
BuildRequires:  spirv-tools-devel
BuildRequires:  vulkan-headers
BuildRequires:  zstd
BuildRequires:  cmake(Qt6Core) >= 6.6
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xcb)
Requires:       jemalloc
Requires:       qt6-wayland
Recommends:     libqt6svg6
Recommends:     noctalia-shell
Conflicts:      quickshell
Provides:       quickshell = %{version}

%description
noctalia-qs is a fork of Quickshell, a flexible toolkit for building
desktop shells, status bars, widgets, lock screens and other desktop
components using Qt/QtQuick and QML, on Wayland and X11.

This fork is maintained by the Noctalia project and adds shell-specific
protocols (notably ext-background-effect-v1) and defaults. The binary
is named "qs" and is a drop-in replacement for the upstream quickshell
binary.

%prep
%autosetup -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DDISTRIBUTOR="openSUSE" \
    -DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES \
    -DCRASH_HANDLER=ON \
    -DCMAKE_SKIP_RPATH=ON \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=OFF
%cmake_build

%install
%cmake_install

%fdupes %{buildroot}%{_libdir}/qt6/qml
%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE LICENSE-GPL
%doc README.md
%{_bindir}/qs
%{_bindir}/quickshell
%{_datadir}/applications/dev.noctalia.noctalia-qs.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/dev.noctalia.noctalia-qs.svg

%changelog
