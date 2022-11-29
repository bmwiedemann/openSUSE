#
# spec file for package antimicrox
#
# Copyright (c) 2022 SUSE LLC
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


Name:           antimicrox
Version:        3.3.2
Release:        0
Summary:        Graphical program used to map keyboard keys and mouse controls to a game-pad
# antimicrox is GPL-3.0-or-later except SDL_GameControllerDB which is Zlib
License:        GPL-3.0-or-later and Zlib
Group:          Hardware/Joystick
URL:            https://github.com/AntiMicroX/antimicroX
Source0:        https://github.com/AntiMicroX/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove_datetime_aboutdialog.patch -- avoid unneccessary rebuilds
Patch0:         remove_datetime_aboutdialog.patch
# PATCH-FIX-OPENSUSE fix_xcb_linker.patch -- fix linking xcb
Patch1:         fix_xcb_linker.patch
BuildRequires:  cmake >= 3.12
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  libqt5-qttools-devel
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xtst)

%description
Antimicrox is a graphical program used to map keyboard keys and mouse
controls to a gamepad. This program is useful for playing PC games using
a gamepad that do not have any form of built-in gamepad support.
However, you can use this program to control any desktop application with
a gamepad; on Linux, this means that your system has to be running an
X environment in order to run this program.

This application is continuation of project called AntiMicro,
which was later abandoned and revived by juliagoda.

%prep
%setup -q
%autopatch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-qt

# remove redundant changelog
rm %{buildroot}%{_datadir}/%{name}/CHANGELOG.md
rm %{buildroot}%{_datadir}/doc/%{name}/CHANGELOG.md

%fdupes %{buildroot}%{_datadir}
%suse_update_desktop_file -r io.github.antimicrox.%{name} System HardwareSettings

%files
%license LICENSE
%doc CHANGELOG.md README.md ProfileTips.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/io.github.antimicrox.%{name}.desktop
%{_datadir}/metainfo/io.github.antimicrox.%{name}.appdata.xml
%{_datadir}/mime/packages/io.github.antimicrox.%{name}.xml
%{_datadir}/icons/hicolor/*/apps/*
%dir %{_datadir}/icons/breeze
%dir %{_datadir}/icons/breeze/48x48
%{_datadir}/icons/breeze/48x48/apps*
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_udevrulesdir}/60-%{name}-uinput.rules

%changelog
