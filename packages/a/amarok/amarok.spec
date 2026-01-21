#
# spec file for package amarok
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.12.0
%define qt6_version 6.7.0

%bcond_without released
Name:           amarok
Version:        3.3.2
Release:        0
Summary:        Media Player
License:        GPL-2.0-or-later
URL:            https://amarok.kde.org/
Source0:        https://download.kde.org/stable/amarok/%{version}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/amarok/%{version}/%{name}-%{version}.tar.xz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/blob/master/keys/nurmi@key1.asc?ref_type=heads
Source2:        amarok.keyring
%endif
# PATCH-FIX-OPENSUSE flac_mimetype_bnc671581.diff bnc#671581 ctrippe@gmx.net -- Support for the changed mimetype for flac files
Patch0:         flac_mimetype_bnc671581.diff
# PATCH-FIX-OPENSUSE
Patch1:         disable-web-plugins-by-default.patch
# PATCH-FIX-OPENSUSE
Patch2:         0001-Work-around-QTBUG-75797-for-openQA.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  libmariadbd-devel
BuildRequires:  mariadb
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DNSSD) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6ThreadWeaver) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(lastfm6)
BuildRequires:  cmake(Mygpo-qt6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
%ifarch x86_64 %{x86_64} aarch64 riscv64
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(libmtp) >= 1.0.0
BuildRequires:  pkgconfig(libofa)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(loudmouth-1.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(taglib) >= 1.12
BuildRequires:  pkgconfig(zlib)
Requires:       gstreamer-plugins-base
Recommends:     gstreamer-plugins-good
# needed by the context view
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       qt6-declarative-imports >= %{qt6_version}
Recommends:     moodbar

%description
Amarok is a media player for all kinds of media. This includes MP3, Ogg
Vorbis, audio CDs, podcasts and streams. Play lists can be stored in
.m3u or .pls files.

%package doc
Summary:        Documentation for Amarok
# The english doc was split from the main package
Conflicts:      amarok < %{version}

%description doc
This package provides documentation for the Amarok media player.

%lang_package

%prep
%autosetup -p1

# Reduce size of the context widget
sed -i 's#1.7#1.12#' src/MainWindow.cpp

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-html --with-qt

%fdupes %{buildroot}

# E: devel-file-in-non-devel-package
rm %{buildroot}%{_kf6_libdir}/libamarok{core,lib,shared,-sqlcollection,-transcoding}.so

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README
%{_kf6_applicationsdir}/org.kde.amarok.desktop
%{_kf6_applicationsdir}/org.kde.amarok_containers.desktop
%{_kf6_appstreamdir}/org.kde.amarok.*
%{_kf6_bindir}/amarok
%{_kf6_bindir}/amarok_afttagger
%{_kf6_bindir}/amarokcollectionscanner
%{_kf6_configdir}/amarok_homerc
%{_kf6_configkcfgdir}/amarokconfig.kcfg
%{_kf6_dbusinterfacesdir}/org.kde.amarok.*
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_libdir}/libamarok_service_lastfm_config.so
%{_kf6_libdir}/libamarok-sqlcollection.so.*
%{_kf6_libdir}/libamarok-transcoding.so.*
%{_kf6_libdir}/libamarokcore.so.*
%{_kf6_libdir}/libamaroklib.so.*
%{_kf6_libdir}/libamarokpud.so
%{_kf6_libdir}/libamarokshared.so.*
%{_kf6_libdir}/libampache_account_login.so
%{_kf6_libdir}/libgpodder_service_config.so
%{_kf6_notificationsdir}/amarok.notifyrc
%{_kf6_plugindir}/amarok_*.so
%{_kf6_plugindir}/kcm_amarok_service_*.so
%{_kf6_qmldir}/org/kde/amarok/
%{_kf6_sharedir}/amarok/
%{_kf6_sharedir}/dbus-1/services/org.kde.amarok.service
%dir %{_kf6_sharedir}/kio
%dir %{_kf6_sharedir}/kio/servicemenus
%{_kf6_sharedir}/kio/servicemenus/amarok_append.desktop
%{_kf6_sharedir}/kpackage/
%{_kf6_sharedir}/solid/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/*/amarok/

%files doc
%{_kf6_htmldir}/*/amarok/

%changelog
