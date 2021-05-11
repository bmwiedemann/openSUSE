#
# spec file for package qtfm
#
# Copyright (c) 2021 SUSE LLC
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


Name:           qtfm
Version:        6.2.0
Release:        0
Summary:        Qt File Manager
License:        GPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/File utilities
URL:            https://qtfm.eu
Source0:        https://github.com/rodlie/qtfm/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- https://github.com/rodlie/qtfm/pull/174
Patch0:         0001-iconview-Fix-QPainterPath-path-has-incomplete-type.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
Recommends:     adwaita-icon-theme
Recommends:     udisks2

%description
Lightweight file manager using Qt.

Features:
 * Desktop (theme/applications/mime) integration
 * Customizable interface
 * Powerful custom command system
 * Customizable key bindings
 * Drag & drop functionality
 * Tabs
 * Udisks support
 * System tray daemon

%prep
%autosetup -p1

%build
%qmake5 PREFIX=%{_prefix} CONFIG+=with_magick CONFIG+=magick7 CONFIG+=with_ffmpeg
%make_build

%install
%qmake5_install
%fdupes %{buildroot}/%{_datadir}
rm -rv %{buildroot}%{_datadir}/doc

%files
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{_bindir}/qtfm
%{_bindir}/qtfm-tray
%{_datadir}/applications/qtfm.desktop
%dir %{_datadir}/icons/hicolor/{20x20,160x160}/{,apps}
%{_datadir}/icons/hicolor/*/apps/qtfm.??g
%{_sysconfdir}/xdg/autostart/qtfm-tray.desktop
%{_mandir}/man?/qtfm-tray.?%{?ext_man}
%{_mandir}/man?/qtfm.?%{?ext_man}

%changelog
