#
# spec file for package kdenlive
#
# Copyright (c) 2024 SUSE LLC
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


%define mlt_version 7.14.0
%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kdenlive
Version:        24.05.2
Release:        0
Summary:        Non-linear video editor
License:        GPL-3.0-or-later
URL:            https://www.kdenlive.org/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  rttr-devel
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6NetworkAuth) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(mlt++-7) >= %{mlt_version}
BuildRequires:  pkgconfig(mlt-framework-7) >= %{mlt_version}
BuildRequires:  pkgconfig(x11)
Requires:       libmlt7-module-qt6
Requires:       melt >= 7
# Required at runtime
Requires:       qt6-declarative-imports >= %{qt6_version}
# Required by the composition and effects panel
Requires:       kf6-knewstuff-imports >= %{kf6_version}
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
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --with-man --all-name

%fdupes -s %{buildroot}

# Already packaged with %%doc
rm -r %{buildroot}%{_datadir}/doc/Kdenlive

%files
%license LICENSES/*
%doc AUTHORS README.md
%doc %lang(en) %{_kf6_htmldir}/en/kdenlive/
%dir %{_kf6_plugindir}/kf6/thumbcreator
%{_kf6_applicationsdir}/org.kde.kdenlive.desktop
%{_kf6_appstreamdir}/org.kde.kdenlive.appdata.xml
%{_kf6_bindir}/kdenlive
%{_kf6_bindir}/kdenlive_render
%{_kf6_configkcfgdir}/kdenlivesettings.kcfg
%{_kf6_debugdir}/kdenlive.categories
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_knsrcfilesdir}/kdenlive_effects.knsrc
%{_kf6_knsrcfilesdir}/kdenlive_keyboardschemes.knsrc
%{_kf6_knsrcfilesdir}/kdenlive_luts.knsrc
%{_kf6_knsrcfilesdir}/kdenlive_renderprofiles.knsrc
%{_kf6_knsrcfilesdir}/kdenlive_titles.knsrc
%{_kf6_knsrcfilesdir}/kdenlive_wipes.knsrc
%{_kf6_mandir}/man1/kdenlive.1%{ext_man}
%{_kf6_mandir}/man1/kdenlive_render.1%{ext_man}
%{_kf6_notificationsdir}/kdenlive.notifyrc
%{_kf6_plugindir}/kf6/thumbcreator/mltpreview.so
%{_kf6_sharedir}/kdenlive/
%{_kf6_sharedir}/mime/packages/org.kde.kdenlive.xml
%{_kf6_sharedir}/mime/packages/westley.xml

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kdenlive/

%changelog
