#
# spec file for package discover6
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0
%define rname discover
%bcond_without released
# Version in Leap 15 < 15.6 is too old
%global have_fwupd (0%{?suse_version} > 1500 || 0%{?sle_version} >= 150600)

Name:           discover6
Version:        6.1.0
Release:        0
Summary:        Software store for the KDE Plasma desktop
License:        GPL-2.0-only AND GPL-3.0-only AND GPL-3.0-or-later
URL:            https://apps.kde.org/discover/
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         0001-Warning-for-FlatHub.patch
BuildRequires:  flatpak-devel >= 0.11.8
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(AppStreamQt) >= 1.0.0
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Attica) >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
# Only available on archs providing QtWebEngine
%ifarch x86_64 aarch64 riscv64
BuildRequires:  cmake(Qt6WebView) >= %{qt6_version}
%endif
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  cmake(packagekitqt6) >= 1.0.1
%if %{have_fwupd}
BuildRequires:  pkgconfig(fwupd) >= 1.9.4
%endif
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libmarkdown) >= 3.0
%endif
Requires:       kf6-kdeclarative-imports >= %{kf6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-kuserfeedback-imports >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       qt6-declarative-imports >= %{qt6_version}
Recommends:     discover-backend-flatpak
Recommends:     discover6-backend-fwupd
Recommends:     discover6-backend-packagekit
Recommends:     discover6-notifier
Provides:       discover = %{version}
Obsoletes:      discover < %{version}
Obsoletes:      discover-lang < %{version}

%description
Discover is a graphical software manager for the KDE Plasma desktop. It helps users to find software they might want easily and quickly.

By allowing to navigate a software library by search, categories, top lists along with detailed application information including screenshots and reviews, users can more quickly find applications that suit their needs.

%package backend-packagekit
Summary:        PackageKit Backend for Discover
Requires:       PackageKit
Requires:       appstream-provider
Requires:       discover6 = %{version}
# Technically libdiscover and not the backend implements AppStream support, but
# it's useless without system package management
%requires_eq    AppStream
Provides:       discover-backend-packagekit = %{version}
Obsoletes:      discover-backend-packagekit < %{version}

%description backend-packagekit
A plugin for Discover to support management of system packages and repositories
using PackageKit.

%package backend-flatpak
Summary:        Flatpak Backend for Discover
Requires:       discover6 = %{version}
Requires:       flatpak
Provides:       discover-backend-flatpak = %{version}
Obsoletes:      discover-backend-flatpak < %{version}

%description backend-flatpak
A plugin for Discover to support installation and management of Flatpak
applications and repositories.

%if %{have_fwupd}
%package backend-fwupd
Summary:        fwupd Backend for Discover
Requires:       discover6 = %{version}
Provides:       discover-backend-fwupd = %{version}
Obsoletes:      discover-backend-fwupd < %{version}

%description backend-fwupd
A plugin for Discover to support updates of system firmware using fwupd.
%endif

%package notifier
Summary:        Update notifier for KDE Software Manager
Requires:       discover6 = %{version}
Obsoletes:      discover-plasmoid < %{version}
Obsoletes:      plasma5-pk-updates < 0.3.3
Obsoletes:      plasma5-pk-updates-lang < 0.3.3
Provides:       discover-notifier = %{version}
Obsoletes:      discover-notifier < %{version}

%description notifier
This is a notifier for Discover to inform the user that updates are available and allows the
user to install them using Discover.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%suse_update_desktop_file -r org.kde.discover Qt KDE System PackageManager

# Even without the snap backend, this is installed...
rm %{buildroot}%{_kf6_applicationsdir}/org.kde.discover.snap.desktop

%find_lang libdiscover %{name}.lang
%find_lang plasma-discover %{name}.lang

%find_lang plasma-discover-notifier notifier.lang
%find_lang kcm_updates notifier.lang

%files
%license LICENSES/*
%dir %{_kf6_plugindir}/discover/
%{_kf6_applicationsdir}/org.kde.discover.desktop
%{_kf6_applicationsdir}/org.kde.discover.urlhandler.desktop
%{_kf6_appstreamdir}/org.kde.discover.appdata.xml
%{_kf6_bindir}/plasma-discover
%{_kf6_bindir}/plasma-discover-update
%{_kf6_debugdir}/discover.categories
%{_kf6_iconsdir}/hicolor/*/apps/plasmadiscover.*
%{_kf6_kxmlguidir}/plasmadiscover/
%{_kf6_libdir}/plasma-discover/
%{_kf6_notificationsdir}/discoverabstractnotifier.notifyrc
%{_kf6_plugindir}/discover/kns-backend.so
%dir %{_kf6_sharedir}/libdiscover
%dir %{_kf6_sharedir}/libdiscover/categories

%files lang -f %{name}.lang

%files backend-packagekit
%license LICENSES/*
%{_kf6_plugindir}/discover/packagekit-backend.so
%{_kf6_sharedir}/libdiscover/categories/packagekit-backend-categories.xml
%{_kf6_appstreamdir}/org.kde.discover.packagekit.appdata.xml

%files backend-flatpak
%license LICENSES/*
%{_kf6_plugindir}/discover/flatpak-backend.so
%{_kf6_sharedir}/libdiscover/categories/flatpak-backend-categories.xml
%{_kf6_appstreamdir}/org.kde.discover.flatpak.appdata.xml
%{_kf6_applicationsdir}/org.kde.discover-flatpak.desktop
%{_kf6_iconsdir}/hicolor/scalable/apps/flatpak-discover.svg

%if %{have_fwupd}
%files backend-fwupd
%license LICENSES/*
%{_kf6_plugindir}/discover/fwupd-backend.so
%endif

%files notifier -f notifier.lang
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_updates.desktop
%dir %{_kf6_plugindir}/discover-notifier
%{_kf6_plugindir}/discover-notifier/DiscoverPackageKitNotifier.so
%{_kf6_plugindir}/discover-notifier/FlatpakNotifier.so
%{_kf6_configdir}/autostart/org.kde.discover.notifier.desktop
%{_kf6_applicationsdir}/org.kde.discover.notifier.desktop
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_updates.so
%{_libexecdir}/DiscoverNotifier

%changelog
