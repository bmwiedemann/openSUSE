#
# spec file for package kdenlive
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


%define mlt_version 7.0.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kdenlive
Version:        22.12.1
Release:        0
Summary:        Non-linear video editor
License:        GPL-3.0-or-later
URL:            https://www.kdenlive.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  rttr-devel
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Plotting)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5NetworkAuth)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(mlt++-7) >= %{mlt_version}
BuildRequires:  pkgconfig(mlt-framework-7) >= %{mlt_version}
BuildRequires:  pkgconfig(x11)
Requires:       melt >= 7
# It doesn't start without it (boo#994649)
Requires:       libqt5-qtquickcontrols
# needed for the new timeline
Requires:       libqt5-qtquickcontrols2
Recommends:     %{_bindir}/dvdauthor
Recommends:     %{_bindir}/dvgrab
Recommends:     %{_bindir}/ffmpeg
Recommends:     %{_bindir}/ffplay
Recommends:     %{_bindir}/genisoimage
Recommends:     %{_bindir}/mediainfo
Recommends:     frei0r-plugins
Recommends:     libv4l
Obsoletes:      kdenlive5 < %{version}
Provides:       kdenlive5 = %{version}

%description
Kdenlive is a non-linear video editor for GNU/Linux and FreeBSD, which supports
DV, AVCHD (experimental support) and HDV editing. Kdenlive relies on several
other open source projects, such as FFmpeg and the MLT video framework. It was
designed to answer all needs, from basic video editing to semi-professional
work.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%fdupes -s %{buildroot}
rm -r %{buildroot}%{_datadir}/doc/Kdenlive

%files
%defattr(0644,root,root,0755)
%attr(0755,-,-) %{_bindir}/%{name}
%attr(0755,-,-) %{_bindir}/%{name}_render
%license LICENSES/*
%doc AUTHORS README.md
%{_kf5_knsrcfilesdir}/*.knsrc
%doc %lang(en) %{_kf5_htmldir}/en/kdenlive/
%{_kf5_applicationsdir}/org.kde.kdenlive.desktop
%{_kf5_appstreamdir}/org.kde.kdenlive.appdata.xml
%{_kf5_configkcfgdir}/kdenlivesettings.kcfg
%{_kf5_debugdir}/kdenlive.categories
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/kdenlive/
%{_kf5_mandir}/man1/kdenlive*
%{_kf5_plugindir}/mltpreview.so
%{_kf5_servicesdir}/mltpreview.desktop
%{_kf5_sharedir}/kdenlive/
%{_kf5_sharedir}/knotifications5/kdenlive.notifyrc
%{_kf5_sharedir}/mime/packages/org.kde.kdenlive.xml
%{_kf5_sharedir}/mime/packages/westley.xml

%files lang -f %{name}.lang

%changelog
