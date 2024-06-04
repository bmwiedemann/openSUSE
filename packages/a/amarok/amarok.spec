#
# spec file for package amarok
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


%define kf5_version 5.78.0
%define qt5_version 5.15.0
%bcond_without released
Name:           amarok
Version:        3.0.1
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
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  liblastfm-qt5-devel
BuildRequires:  libmariadbd-devel
BuildRequires:  mariadb
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  cmake(KF5Archive) >= %{kf5_version}
BuildRequires:  cmake(KF5Attica) >= %{kf5_version}
BuildRequires:  cmake(KF5Codecs) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5DNSSD) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{kf5_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5NewStuff) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Package) >= %{kf5_version}
BuildRequires:  cmake(KF5Solid) >= %{kf5_version}
BuildRequires:  cmake(KF5TextEditor) >= %{kf5_version}
BuildRequires:  cmake(KF5ThreadWeaver) >= %{kf5_version}
BuildRequires:  cmake(KF5Wallet) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(Mygpo-qt5) >= 1.1.0
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5Qml) >= %{qt5_version}
BuildRequires:  cmake(Qt5QuickWidgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5Sql) >= %{qt5_version}
BuildRequires:  cmake(Qt5Svg) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5UiTools) >= %{qt5_version}
%ifarch %{ix86} x86_64 %{x86_64} %{arm} aarch64
BuildRequires:  cmake(Qt5WebEngine) >= %{qt5_version}
%endif
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5Xml) >= %{qt5_version}
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(glib-2.0)
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
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
# phonon4qt5-backend-vlc is the backend name in Leap
Requires:       (phonon-vlc-qt5 or phonon4qt5-backend-vlc)
# needed by the context view
Requires:       kirigami2 >= %{kf5_version}
Requires:       libqt5-qtquickcontrols2 >= %{qt5_version}
Recommends:     (gstreamer-plugins-ugly if phonon4qt5-backend-gstreamer)
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

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name --with-html --with-qt

%fdupes %{buildroot}

# E: devel-file-in-non-devel-package
rm %{buildroot}%{_kf5_libdir}/libamarok{core,lib,shared,-sqlcollection,-transcoding}.so

%ldconfig_scriptlets

%files
%license COPYING*
%doc README
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
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_knsrcfilesdir}/amarok.knsrc
%{_kf5_libdir}/libamarok-sqlcollection.so.*
%{_kf5_libdir}/libamarok-transcoding.so.*
%{_kf5_libdir}/libamarok_service_lastfm_config.so
%{_kf5_libdir}/libamarokcore.so.*
%{_kf5_libdir}/libamaroklib.so.*
%{_kf5_libdir}/libamarokpud.so
%{_kf5_libdir}/libamarokshared.so.*
%{_kf5_libdir}/libampache_account_login.so
%{_kf5_libdir}/libgpodder_service_config.so
%{_kf5_notifydir}/amarok.notifyrc
%{_kf5_plugindir}/amarok_*.so
%{_kf5_plugindir}/kcm_amarok_service_*.so
%{_kf5_qmldir}/org/kde/amarok/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/amarok*.desktop
%{_kf5_sharedir}/amarok/
%{_kf5_sharedir}/dbus-1/services/org.kde.amarok.service
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kpackage/
%{_kf5_sharedir}/solid/

%files lang -f %{name}.lang
%exclude %{_kf5_htmldir}/*/amarok/

%files doc
%{_kf5_htmldir}/*/amarok/

%changelog
