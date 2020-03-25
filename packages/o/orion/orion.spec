#
# spec file for package orion
#
# Copyright (c) 2020 SUSE LLC
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


Name:           orion
Version:        1.6.7+git~20200218
Release:        0
Summary:        Twitch stream client using Qt
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Video/Players
URL:            https://alamminsalo.github.io/orion/
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Add-a-local-qthelper.hpp-copy.patch
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.6
BuildRequires:  pkgconfig(Qt5DBus) >= 5.6
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.6
BuildRequires:  pkgconfig(Qt5Quick) >= 5.6
BuildRequires:  pkgconfig(Qt5QuickControls2) >= 5.6
BuildRequires:  pkgconfig(Qt5Svg) >= 5.6
BuildRequires:  pkgconfig(mpv)
#Required for working gui
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquickcontrols2
Recommends:     gstreamer-plugins-libav

%description
QML/C++-written desktop client for Twitch.tv.

%prep
%setup -q
%patch0 -p1

#enforce package versioning in GUI
sed -i 's|v$$VERSION|v%{version}-%{release}|g' orion.pro

%build
%qmake5
%make_jobs

%install
%qmake5_install

%files
%doc README.md
%license COPYING LICENSE.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/Orion.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/Orion.appdata.xml

%changelog
