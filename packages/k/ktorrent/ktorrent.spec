#
# spec file for package ktorrent
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           ktorrent
Version:        24.05.2
Release:        0
Summary:        KDE BitTorrent Client
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ktorrent
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source3:        ktorrent.1
Source4:        ktupnptest.1
# PATCH-FIX-OPENSUSE initial-preference.diff cmorve69@yahoo.es -- InitialPreference to set it as the default torrent downloader
Patch0:         initial-preference.diff
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DNSSD) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Plotting) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6Syndication) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KTorrent6)
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(libmaxminddb)
%ifarch aarch64 x86_64 %{x86_64} riscv64
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif

%description
KTorrent is a BitTorrent application by KDE which allows you to download files
using the BitTorrent protocol. It enables you to run multiple torrents at the
same time and comes with extended features to make it a full-featured client
for BitTorrent.

%lang_package

%prep
%autosetup -p1

# The boost minimum version change is only cosmetic. Leap 15.2 provides 1.66
sed -i 's#1.71.0#1.66.0#' CMakeLists.txt

%build
%cmake_kf6
%kf6_build

%install
%kf6_install

# Add man pages from help2man edited.
mkdir -p %{buildroot}%{_mandir}/man1
cp -a %{SOURCE3} %{buildroot}%{_mandir}/man1
cp -a %{SOURCE4} %{buildroot}%{_mandir}/man1

# Fix any .py files with shebangs and wrong permissions.
find %{buildroot} -name "*.py" -perm 0644 -exec grep -l '#!' {} + | \
  xargs -rd'\n' chmod -f a+x

%fdupes %{buildroot}

%find_lang %{name} --with-html

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc ChangeLog RoadMap
%doc %lang(en) %{_kf6_htmldir}/en/ktorrent/
%{_kf6_applicationsdir}/org.kde.ktorrent.desktop
%{_kf6_appstreamdir}/org.kde.ktorrent.appdata.xml
%{_kf6_bindir}/ktmagnetdownloader
%{_kf6_bindir}/ktorrent
%{_kf6_bindir}/ktupnptest
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_kxmlguidir}/ktorrent/
%{_kf6_libdir}/libktcore.so.*
%{_kf6_mandir}/man1/ktorrent.1%{?ext_man}
%{_kf6_mandir}/man1/ktupnptest.1%{?ext_man}
%{_kf6_notificationsdir}/ktorrent.notifyrc
%dir %{_kf6_plugindir}/ktorrent_plugins/
%{_kf6_plugindir}/ktorrent_plugins/BandwidthSchedulerPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/DownloadOrderPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/IPFilterPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/InfoWidgetPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/LogViewerPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/MagnetGeneratorPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/MediaPlayerPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/ScanFolderPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/ScanForLostFilesPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/ShutdownPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/StatsPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/UPnPPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/ZeroconfPlugin.so
%ifarch aarch64 x86_64 %{x86_64} riscv64
%{_kf6_plugindir}/ktorrent_plugins/SearchPlugin.so
%{_kf6_plugindir}/ktorrent_plugins/SyndicationPlugin.so
%endif

%ifarch aarch64 x86_64 %{x86_64} riscv64
%{_kf6_sharedir}/ktorrent/
%endif

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/ktorrent/

%changelog
