#
# spec file for package amarok
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


# Leap 15.1 compatibility
%{!?_kf5_knsrcfilesdir: %global _kf5_knsrcfilesdir %{_kf5_configdir}}
Name:           amarok
Version:        2.9.70git.20200930T124856~3973278a68
Release:        0
Summary:        Media Player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://amarok.kde.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-lang.tar.xz
# PATCH-FIX-OPENSUSE flac_mimetype_bnc671581.diff bnc#671581 ctrippe@gmx.net -- Support for the changed mimetype for flac files
Patch1:         flac_mimetype_bnc671581.diff
# PATCH-FIX-OPENSUSE
Patch2:         disable-web-plugins-by-default.patch
# PATCH-FIX-OPENSUSE
Patch3:         0001-Work-around-QTBUG-75797-for-openQA.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  fftw-devel
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpod-devel >= 0.7.0
BuildRequires:  liblastfm-qt5-devel
BuildRequires:  libmtp-devel >= 1.0.0
BuildRequires:  libmygpo-qt5-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libmysqld-devel
BuildRequires:  libofa-devel
BuildRequires:  libqca-qt5-devel
BuildRequires:  libxml2-devel
BuildRequires:  loudmouth-devel
BuildRequires:  mysql
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Attica)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(taglib-extras)
BuildRequires:  pkgconfig(zlib)
# needed by the context view
Requires:       kirigami2
Requires:       libqt5-qtquickcontrols
Requires:       libtag-extras1 >= 1.0
Recommends:     %{name}-lang = %{version}
Recommends:     (gstreamer-plugins-ugly if phonon4qt5-backend-gstreamer)
Recommends:     moodbar

%description
Amarok is a media player for all kinds of media. This includes MP3, Ogg
Vorbis, audio CDs, podcasts and streams. Play lists can be stored in
.m3u or .pls files.

%lang_package

%prep
%autosetup -p1 -a1
cat >> CMakeLists.txt << EOF
ki18n_install(po)
EOF

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang amarok %{name}.lang
%find_lang amarokcollectionscanner_qt %{name}.lang
%find_lang amarokpkg %{name}.lang

%suse_update_desktop_file  org.kde.amarok
%suse_update_desktop_file  org.kde.amarok_containers

%fdupes -s %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc AUTHORS ChangeLog README TODO
%{_kf5_applicationsdir}/org.kde.amarok.desktop
%{_kf5_applicationsdir}/org.kde.amarok_containers.desktop
%{_kf5_appstreamdir}/org.kde.amarok.*
%{_kf5_bindir}/amarok
%{_kf5_bindir}/amarok_afttagger
%{_kf5_bindir}/amarokcollectionscanner
%{_kf5_bindir}/amarokpkg
%{_kf5_configdir}/*
%{_kf5_configkcfgdir}/
%{_kf5_dbusinterfacesdir}/
%{_kf5_htmldir}/en/amarok/
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_knsrcfilesdir}/amarok.knsrc
%{_kf5_libdir}/libamarok-sqlcollection.so*
%{_kf5_libdir}/libamarok-transcoding.so*
%{_kf5_libdir}/libamarok_service_lastfm_config.so
%{_kf5_libdir}/libamarokcore.so*
%{_kf5_libdir}/libamaroklib.so*
%{_kf5_libdir}/libamarokpud.so*
%{_kf5_libdir}/libamarokshared.so*
%{_kf5_libdir}/libampache_account_login.so
%{_kf5_libdir}/libgpodder_service_config.so
%{_kf5_notifydir}/amarok.notifyrc
%{_kf5_plugindir}/amarok_*.so
%{_kf5_plugindir}/kcm_amarok_service_*.so
%{_kf5_qmldir}/org/kde/amarok/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/amarok*.desktop
%{_kf5_sharedir}/amarok/
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kpackage/
%{_kf5_sharedir}/solid/

%files lang -f %{name}.lang

%changelog
