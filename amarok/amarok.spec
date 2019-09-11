#
# spec file for package amarok
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# Make sure to require at least the version used for linking to avoid undefined symbols at runtime
%define required_libtag  %(rpm -qf `ldd $(type -P tagreader) | awk '/libtag.so.[0-9]/{ print $3 }'`)
Name:           amarok
Version:        2.9.0
Release:        0
Summary:        Media Player for KDE
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Players
Url:            http://amarok.kde.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
# for reproducible builds
Source99:       %{name}.changes
# PATCH-FIX-OPENSUSE initial-preference.diff bnc#605522 llunak@novell.com -- Increase initial preference to be used for audio files instead of Kaffeine
Patch1:         initial-preference.diff
# PATCH-FIX-OPENSUSE flac_mimetype_bnc671581.diff bnc#671581 ctrippe@gmx.net -- Support for the changed mimetype for flac files
Patch2:         flac_mimetype_bnc671581.diff
# PATCH-FIX-OPENSUSE
Patch3:         disable-web-plugins-by-default.patch
# PATCH-FIX-UPSTREAM
Patch4:         Fix-build-with-gcc6.patch
# Required for the fdupes macro
BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpod-devel >= 0.7.0
BuildRequires:  libkde4-devel >= 4.6.0
BuildRequires:  liblastfm-devel
BuildRequires:  libmtp-devel
BuildRequires:  libmygpo-qt-devel >= 1.0.5
BuildRequires:  libmysqlclient-devel
BuildRequires:  libmysqld-devel
BuildRequires:  libofa-devel
BuildRequires:  openssl-devel
BuildRequires:  libqca2-devel
BuildRequires:  libqjson-devel
BuildRequires:  libqt4-devel >= 4.8.2
BuildRequires:  libxml2-devel
BuildRequires:  loudmouth-devel
%if 0%{?is_opensuse}
BuildRequires:  breeze5-icons
%else
BuildRequires:  oxygen-icon-theme
%endif
BuildRequires:  qt4-qtscript
BuildRequires:  taglib
BuildRequires:  taglib-devel >= 1.7
BuildRequires:  taglib-extras-devel >= 1.0
BuildRequires:  tcpd-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
Requires:       libtag-extras1 >= 1.0
Requires:       phonon-backend
Requires:       taglib >= 1.7
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Recommends:     %{name}-lang = %{version}
Recommends:     clamz
Recommends:     qt4-qtscript
Recommends:     kio_audiocd4
Recommends:     gstreamer-plugins-ugly
Provides:       kde4-amarok = 2.0.90
Obsoletes:      kde4-amarok <= 2.0.89
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%requires_ge  %{required_libtag}
%kde4_runtime_requires

%description
Amarok is a media player for all kinds of media. This includes MP3, Ogg
Vorbis, audio CDs, podcasts and streams. Play lists can be stored in
.m3u or .pls files.

%lang_package

%prep
: required_libtag '%{required_libtag}'
%setup -q
%patch1
%patch2
%patch3 -p1
%patch4 -p1

# Remove build time references so build-compare can do its work
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{SOURCE99} '+%%b %%e %%Y')
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" src/main.cpp

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
# force not to use MYSQLCONFIG as mariadb_config provided by mariadb-connector-c doesn't support "--libmysqld-libs" option anymore
%if 0%{?suse_version} >= 1500
%cmake_kde4 -d build -- -DMYSQLCONFIG_EXECUTABLE:BOOL=OFF -DWITH_QTWEBKIT=OFF
%else
%cmake_kde4 -d build -- -DMYSQLCONFIG_EXECUTABLE:BOOL=OFF
%endif
%make_jobs

%install
%kde4_makeinstall -C build

# Remove *.so files (not needed), fix "devel-file-in-non-devel-package" rpmlint warning
# "libampache_account_login.so" should not be removed
rm -f %{buildroot}%{_kde4_libdir}/libamarok{core,lib,ocsclient,pud,shared,-sqlcollection,-transcoding}.so

#bnc722284 amarok is not really a good player for audio-cds, remove the action for solid
rm -f %{buildroot}%{_kde4_appsdir}/solid/actions/amarok-play-audiocd.desktop

# Disable all scripts by default (boo#1070899)
sed -i"" "s/X-KDE-PluginInfo-EnabledByDefault=true/X-KDE-PluginInfo-EnabledByDefault=false/g" %{buildroot}%{_kde4_appsdir}/amarok/scripts/*/script.spec

%if 0%{?is_opensuse}
# Copy the icon for amzdownloader over from breeze
for i in 16 22 24
do
   mkdir -p %{buildroot}%{_kde4_iconsdir}/hicolor/${i}x${i}/actions
   cp %{_kde4_iconsdir}/breeze/actions/${i}/download.svg %{buildroot}%{_kde4_iconsdir}/hicolor/${i}x${i}/actions/
done
%else
# Copy the icon for amzdownloader over from oxygen
for i in 16 22 32 48
do
   mkdir -p %{buildroot}%{_kde4_iconsdir}/hicolor/${i}x${i}/actions
   cp %{_kde4_iconsdir}/oxygen/${i}x${i}/actions/download.png %{buildroot}%{_kde4_iconsdir}/hicolor/${i}x${i}/actions/
done
%endif

# Symlink service menu to the KF5 location
mkdir -p %{buildroot}%{_kf5_servicesdir}/ServiceMenus
ln -s %{_kde4_servicesdir}/ServiceMenus/amarok_append.desktop %{buildroot}/%{_kf5_servicesdir}/ServiceMenus/

%suse_update_desktop_file org.kde.amarok Qt KDE AudioVideo Audio Player
%suse_update_desktop_file -r amzdownloader Qt KDE AudioVideo Audio Player

%fdupes -s %{buildroot}

%find_lang amarok
%find_lang amarokcollectionscanner_qt amarok.lang
%find_lang amarokpkg amarok.lang

%kde_post_install

%post
/sbin/ldconfig
%mime_database_post

%postun
/sbin/ldconfig
%mime_database_postun

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING* ChangeLog README TODO
%{_kde4_bindir}/amarok
%{_kde4_bindir}/amarok_afttagger
%{_kde4_bindir}/amarokcollectionscanner
%{_kde4_bindir}/amarokmp3tunesharmonydaemon
%{_kde4_bindir}/amarokpkg
%{_kde4_bindir}/amzdownloader
%{_kde4_modulesdir}/amarok_*
%{_kde4_modulesdir}/kcm_amarok_service_*
%{_kde4_libdir}/libamarok-sqlcollection.so.*
%{_kde4_libdir}/libamarok-transcoding.so.*
%{_kde4_libdir}/libamarokcore.so.*
%{_kde4_libdir}/libamaroklib.so.*
%{_kde4_libdir}/libamarokocsclient.so.*
%{_kde4_libdir}/libamarokpud.so.*
%{_kde4_libdir}/libamarokshared.so.*
%{_kde4_libdir}/libampache_account_login.so
%{_kde4_libdir}/libamarok_service_lastfm_shared.so
%{_kde4_applicationsdir}/org.kde.amarok.desktop
%{_kde4_applicationsdir}/org.kde.amarok_containers.desktop
%{_kde4_applicationsdir}/amzdownloader.desktop
%{_datadir}/dbus-1/interfaces/org.freedesktop.MediaPlayer.player.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.MediaPlayer.root.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.MediaPlayer.tracklist.xml
%{_datadir}/dbus-1/interfaces/org.kde.amarok.App.xml
%{_datadir}/dbus-1/interfaces/org.kde.amarok.Collection.xml
%{_datadir}/dbus-1/interfaces/org.kde.amarok.Mpris1Extensions.Player.xml
%{_datadir}/dbus-1/interfaces/org.kde.amarok.Mpris2Extensions.Player.xml
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.kde.amarok.appdata.xml
%{_datadir}/mime/packages/amzdownloader.xml
%{_kde4_iconsdir}/hicolor/*/apps/amarok.*
%{_kde4_iconsdir}/hicolor/*/actions/download.*
%{_kde4_appsdir}/amarok/
%dir %{_kde4_appsdir}/desktoptheme
%dir %{_kde4_appsdir}/desktoptheme/default
%dir %{_kde4_appsdir}/desktoptheme/default/widgets
%{_kde4_appsdir}/desktoptheme/default/widgets/amarok-*
%{_kde4_appsdir}/kconf_update/amarok-2.4.1-tokens_syntax_update.pl
%{_kde4_appsdir}/kconf_update/amarok.upd
%{_kde4_sharedir}/config.kcfg/amarokconfig.kcfg
%{_kde4_configdir}/amarok*
%{_kde4_servicesdir}/ServiceMenus/amarok_append.desktop
%{_kde4_servicesdir}/amarok-*
%{_kde4_servicesdir}/amarok_*
%{_kde4_servicesdir}/amarok.protocol
%{_kde4_servicesdir}/amarok*.protocol
%{_kde4_servicetypesdir}/amarok_*
%dir %{_kf5_servicesdir}/ServiceMenus/
%{_kf5_servicesdir}/ServiceMenus/amarok_append.desktop

%files lang -f amarok.lang
%defattr(-,root,root,-)

%changelog
