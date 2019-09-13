#
# spec file for package orion
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.6.6+git~20190714
Release:        0
Summary:        Twitch stream client using Qt
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Video/Players
Url:            http://alamminsalo.github.io/orion/
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc

BuildRequires:  pkgconfig(Qt5Core)          	>=  5.6
BuildRequires:  pkgconfig(Qt5DBus)          	>=  5.6
BuildRequires:  pkgconfig(Qt5OpenGL)        	>=  5.6
BuildRequires:  pkgconfig(Qt5Quick)         	>=  5.6
BuildRequires:  pkgconfig(Qt5QuickControls2)	>=  5.6
BuildRequires:  pkgconfig(Qt5Svg)           	>=  5.6

BuildRequires:  pkgconfig(mpv)

#Required for working gui
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquickcontrols2

Requires(post):     hicolor-icon-theme
Requires(postun):   hicolor-icon-theme
Requires(post):     update-desktop-files
Requires(postun):   update-desktop-files

Recommends:     gstreamer-plugins-libav

%description
QML/C++-written desktop client for Twitch.tv.

%prep
%setup -q

#enforce package versioning in GUI
sed -i 's|v$$VERSION|v%{version}-%{release}|g' orion.pro
#fix paths
sed -i 's|path = /usr/local/share/|path = /usr/share/|g' orion.pro
#fix categories in .desktop file
sed -i 's|Categories=Game|Categories=Network;FileTransfer;|g' distfiles/Orion.desktop

%build
qmake-qt5 QMAKE_CFLAGS+="%optflags" QMAKE_CXXFLAGS+="%optflags" QMAKE_STRIP="/bin/true"
make %{?_smp_mflags}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%install
make install INSTALL_ROOT="%buildroot"

%files
%defattr(-,root,root)
%doc README.md
%license COPYING LICENSE.txt

%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/Orion.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/Orion.appdata.xml

%changelog
