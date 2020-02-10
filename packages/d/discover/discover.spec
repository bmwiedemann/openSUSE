#
# spec file for package discover
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_without lang
Name:           discover
Version:        5.18.0
Release:        0
Summary:        Software store for the KDE Plasma desktop
License:        GPL-2.0-only AND GPL-3.0-only AND GPL-3.0-or-later
Group:          System/GUI/KDE
Url:            https://quickgit.kde.org/?p=discover.git
Source:         discover-%{version}.tar.xz
%if %{with lang}
Source1:        discover-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch1:         0001-Warning-for-FlatHub.patch
BuildRequires:  cmake >= 2.8.12
BuildRequires:  extra-cmake-modules
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
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(packagekitqt5) >= 1.0.1
BuildRequires:  pkgconfig(fwupd) >= 1.0.6
Requires:       kirigami2
Requires:       libqt5-qtquickcontrols2
Recommends:     %{name}-lang
Recommends:     %{name}-backend-packagekit
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
  rm %{buildroot}%{_kf5_applicationsdir}/org.kde.discover.snap.urlhandler.desktop

%if %{with lang}
  %find_lang libdiscover %{name}.lang
  %find_lang plasma-discover %{name}.lang

  %find_lang plasma-discover-notifier notifier.lang
%else
  touch notifier.lang
%endif

%files
%license COPYING*
%{_kf5_bindir}/plasma-discover
%{_kf5_libdir}/plasma-discover/
%dir %{_kf5_plugindir}/discover/
%{_kf5_plugindir}/discover/kns-backend.so
%{_kf5_applicationsdir}/org.kde.discover.desktop
%{_kf5_applicationsdir}/org.kde.discover.urlhandler.desktop
%{_kf5_iconsdir}/hicolor/*/apps/plasmadiscover.*
%{_kf5_notifydir}/discoverabstractnotifier.notifyrc
%{_kf5_kxmlguidir}/plasmadiscover/
%dir %{_kf5_sharedir}/libdiscover/
%dir %{_kf5_sharedir}/libdiscover/categories/
%{_kf5_appstreamdir}/org.kde.discover.appdata.xml
%{_kf5_sharedir}/discover/
%{_libdir}/libexec/kf5/discover/
%{_kf5_knsrcfilesdir}/discover_ktexteditor_codesnippets_core.knsrc
%{_kf5_debugdir}/discover.categories

%if %{with lang}
%files lang -f %{name}.lang
%endif

%files backend-packagekit
%license COPYING*
%{_kf5_plugindir}/discover/packagekit-backend.so
%{_kf5_sharedir}/libdiscover/categories/packagekit-backend-categories.xml
%{_kf5_appstreamdir}/org.kde.discover.packagekit.appdata.xml

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150100
%files backend-flatpak
%license COPYING*
%{_kf5_plugindir}/discover/flatpak-backend.so
%{_kf5_sharedir}/libdiscover/categories/flatpak-backend-categories.xml
%{_kf5_appstreamdir}/org.kde.discover.flatpak.appdata.xml
%{_kf5_applicationsdir}/org.kde.discover-flatpak.desktop
%{_kf5_iconsdir}/hicolor/*/apps/flatpak-discover.svg
%endif

%files backend-fwupd
%license COPYING*
%{_kf5_plugindir}/discover/fwupd-backend.so

%files notifier -f notifier.lang
%license COPYING*
%dir %{_kf5_plugindir}/discover-notifier
%{_kf5_configdir}/autostart/org.kde.discover.notifier.desktop
%{_libdir}/libexec/DiscoverNotifier
%{_kf5_plugindir}/discover-notifier/DiscoverPackageKitNotifier.so
%{_kf5_plugindir}/discover-notifier/FlatpakNotifier.so
%{_kf5_applicationsdir}/org.kde.discover.notifier.desktop

%changelog
