#
# spec file for package kaffeine
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


Name:           kaffeine
Version:        2.0.18git.20230531T022124~afc6c12
Release:        0
Summary:        VLC-based Multimedia Player
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kaffeine/
Source0:        %{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE kaffeine-fixsplitter.patch -- GUI improvement (allow more flexibly set splitters)
Patch0:         kaffeine-fixsplitter.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(libdvbv5)
BuildRequires:  pkgconfig(libvlc) >= 3.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xscrnsaver)
Requires:       libQt5Sql5-sqlite
Requires:       vlc-noX
Recommends:     vlc-codecs

%description
Kaffeine is a media player.
What makes it different from the others is its excellent support of digital TV (DVB).
Kaffeine has a user-friendly interface so that even first-time users can start immediately
playing their movies: from DVD (including DVD menus, titles, chapters, etc.), VCD, or a file.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name}

%{kf5_find_htmldocs}

%files
%license COPYING
%doc README.md
%doc %lang(en) %{_kf5_htmldir}/en/kaffeine/
%{_kf5_applicationsdir}/org.kde.kaffeine.desktop
%{_kf5_appstreamdir}/org.kde.kaffeine.appdata.xml
%{_kf5_bindir}/kaffeine
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_mandir}/man1/kaffeine.1%{?ext_man}
%{_kf5_sharedir}/kaffeine/
%{_kf5_sharedir}/solid/actions/

%files lang -f %{name}.lang
%{_kf5_mandir}/*/man1/kaffeine.1%{?ext_man}
%{_kf5_htmldir}/*/kaffeine/
%exclude %{_kf5_htmldir}/en/

%changelog
