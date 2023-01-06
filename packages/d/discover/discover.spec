#
# spec file for package discover
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without released
# Version in Leap 15.2 is too old
%global have_fwupd (0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300)

Name:           discover
Version:        5.26.5
Release:        0
Summary:        Software store for the KDE Plasma desktop
License:        GPL-2.0-only AND GPL-3.0-only AND GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://quickgit.kde.org/?p=discover.git
Source:         https://download.kde.org/stable/plasma/%{version}/discover-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/discover-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch1:         0001-Warning-for-FlatHub.patch
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  flatpak-devel
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(AppStreamQt) >= 0.11.1
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Attica)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WindowSystem)
# Disabled until upstream complies with the KDE policies
#BuildRequires:  cmake(KUserFeedback)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Concurrent) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
%ifarch %{ix86} x86_64 %{arm} aarch64 mips mips64
BuildRequires:  cmake(Qt5WebView)
%endif
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(packagekitqt5) >= 1.0.1
%if %{have_fwupd}
BuildRequires:  pkgconfig(fwupd) >= 1.0.6
%endif
Requires:       kdeclarative-components
Requires:       kirigami2
Requires:       kuserfeedback-imports
Requires:       libqt5-qtquickcontrols2
Recommends:     %{name}-backend-packagekit
Recommends:     %{name}-lang
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150100
Recommends:     %{name}-backend-flatpak
%endif
# Conflicts with plasma5-pk-updates
# Recommends:     %%{name}-notifier
Recommends:     %{name}-backend-fwupd

%description
Discover is a graphical software manager for the KDE Plasma desktop. It helps users to find software they might want easily and quickly.

By allowing to navigate a software library by search, categories, top lists along with detailed application information including screenshots and reviews, users can more quickly find applications that suit their needs.

%package backend-packagekit
Summary:        PackageKit Backend for Discover
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
# Technically libdiscover and not the backend implements AppStream support, but
# it's useless without system package management
Requires:       AppStream
Requires:       PackageKit
Requires:       appstream-provider

%description backend-packagekit
A plugin for Discover to support management of system packages and repositories
using PackageKit.

%package backend-flatpak
Summary:        Flatpak Backend for Discover
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       flatpak

%description backend-flatpak
A plugin for Discover to support installation and management of Flatpak
applications and repositories.

%package backend-fwupd
Summary:        fwupd Backend for Discover
Group:          System/GUI/KDE
Requires:       %{name} = %{version}

%description backend-fwupd
A plugin for Discover to support updates of system firmware using fwupd.

%package notifier
Summary:        Update notifier for KDE Software Manager
Group:          System/GUI/KDE
Conflicts:      plasma5-pk-updates
Obsoletes:      %{name}-plasmoid < %{version}
Requires:       %{name} = %{version}

%description notifier
This is a notifier for Discover to inform the user that updates are available and allows the
user to install them using Discover.

%lang_package

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %suse_update_desktop_file -r org.kde.discover Qt KDE System PackageManager

  # Even without the snap backend, this is installed...
  rm %{buildroot}%{_kf5_applicationsdir}/org.kde.discover.snap.desktop

%if %{with released}
  %find_lang libdiscover %{name}.lang
  %find_lang plasma-discover %{name}.lang

  %find_lang plasma-discover-notifier notifier.lang
  %find_lang kcm_updates notifier.lang
%else
  touch notifier.lang
%endif

%files
%license LICENSES/*
%dir %{_kf5_plugindir}/discover/
%{_kf5_applicationsdir}/org.kde.discover.desktop
%{_kf5_applicationsdir}/org.kde.discover.urlhandler.desktop
%{_kf5_appstreamdir}/org.kde.discover.appdata.xml
%{_kf5_bindir}/plasma-discover
%{_kf5_bindir}/plasma-discover-update
%{_kf5_debugdir}/discover.categories
%{_kf5_iconsdir}/hicolor/*/apps/plasmadiscover.*
%{_kf5_kxmlguidir}/plasmadiscover/
%{_kf5_libdir}/plasma-discover/
%{_kf5_notifydir}/discoverabstractnotifier.notifyrc
%{_kf5_plugindir}/discover/kns-backend.so
%dir %{_kf5_sharedir}/libdiscover
%dir %{_kf5_sharedir}/libdiscover/categories
%dir %{_kf5_libexecdir}/discover
%{_kf5_libexecdir}/discover/runservice

%if %{with released}
%files lang -f %{name}.lang
%endif

%files backend-packagekit
%license LICENSES/*
%{_kf5_plugindir}/discover/packagekit-backend.so
%{_kf5_sharedir}/libdiscover/categories/packagekit-backend-categories.xml
%{_kf5_appstreamdir}/org.kde.discover.packagekit.appdata.xml

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150100
%files backend-flatpak
%license LICENSES/*
%{_kf5_plugindir}/discover/flatpak-backend.so
%{_kf5_sharedir}/libdiscover/categories/flatpak-backend-categories.xml
%{_kf5_appstreamdir}/org.kde.discover.flatpak.appdata.xml
%{_kf5_applicationsdir}/org.kde.discover-flatpak.desktop
%{_kf5_iconsdir}/hicolor/*/apps/flatpak-discover.svg
%endif

%if %{have_fwupd}
%files backend-fwupd
%license LICENSES/*
%{_kf5_plugindir}/discover/fwupd-backend.so
%endif

%files notifier -f notifier.lang
%license LICENSES/*
%{_kf5_applicationsdir}/kcm_updates.desktop
%dir %{_kf5_plugindir}/discover-notifier
%{_kf5_plugindir}/discover-notifier/DiscoverPackageKitNotifier.so
%{_kf5_plugindir}/discover-notifier/FlatpakNotifier.so
%{_kf5_configdir}/autostart/org.kde.discover.notifier.desktop
%{_kf5_applicationsdir}/org.kde.discover.notifier.desktop
%dir %{_kf5_plugindir}/plasma/
%dir %{_kf5_plugindir}/plasma/kcms/
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings/
%{_kf5_plugindir}/plasma/kcms/systemsettings/kcm_updates.so
%dir %{_kf5_sharedir}/kpackage/
%dir %{_kf5_sharedir}/kpackage/kcms/
%{_kf5_sharedir}/kpackage/kcms/kcm_updates/
%{_libexecdir}/DiscoverNotifier

%changelog
