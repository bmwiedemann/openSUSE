#
# spec file for package ktorrent
#
# Copyright (c) 2021 SUSE LLC
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           ktorrent
Version:        21.04.0
Release:        0
Summary:        KDE BitTorrent Client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://apps.kde.org/ktorrent
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source3:        ktorrent.1
Source4:        ktupnptest.1
# PATCH-FIX-OPENSUSE initial-preference.diff cmorve69@yahoo.es -- InitialPreference to set it as the default torrent downloader
Patch0:         initial-preference.diff
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kross)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Plotting)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5Syndication)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Torrent)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core) >= 5.14
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(taglib)
Recommends:     %{name}-lang = %{version}
%ifarch %{ix86} x86_64 %{arm} aarch64 mips mips64
BuildRequires:  cmake(Qt5WebEngineWidgets)
%endif

%description
KTorrent is a BitTorrent application by KDE which allows you to download files
using the BitTorrent protocol. It enables you to run multiple torrents at the
same time and comes with extended features to make it a full-featured client
for BitTorrent.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

# Add man pages from help2man edited.
mkdir -p %{buildroot}%{_mandir}/man1
cp -a %{SOURCE3} %{buildroot}%{_mandir}/man1
cp -a %{SOURCE4} %{buildroot}%{_mandir}/man1

# Fix any .py files with shebangs and wrong permissions.
find %{buildroot} -name "*.py" -perm 0644 -exec grep -l '#!' {} + | \
	xargs -rd'\n' chmod -f a+x

# E: env-script-interpreter
find %{buildroot}%{_kf5_sharedir}/ktorrent/scripts -name "*.py" -exec sed -i 's#env kf5kross#kf5kross#' {} \;

%suse_update_desktop_file -r org.kde.ktorrent Qt KDE Network P2P

%fdupes -s %{buildroot}

%if %{with lang}
%find_lang %{name}
%{kf5_find_htmldocs}
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog RoadMap
%{_kf5_applicationsdir}/org.kde.ktorrent.desktop
%{_kf5_appstreamdir}/org.kde.ktorrent.appdata.xml
%{_kf5_bindir}/ktmagnetdownloader
%{_kf5_bindir}/ktorrent
%{_kf5_bindir}/ktupnptest
%{_kf5_htmldir}/en/ktorrent/
%{_kf5_iconsdir}/hicolor/*/*/*.png
%{_kf5_iconsdir}/hicolor/*/*/*.svgz
%{_kf5_kxmlguidir}/ktorrent/
%{_kf5_libdir}/libktcore.so.*
%{_kf5_mandir}/man1/ktorrent.1%{?ext_man}
%{_kf5_mandir}/man1/ktupnptest.1%{?ext_man}
%{_kf5_notifydir}/ktorrent.notifyrc
%{_kf5_plugindir}/ktorrent/
%{_kf5_sharedir}/ktorrent/

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
