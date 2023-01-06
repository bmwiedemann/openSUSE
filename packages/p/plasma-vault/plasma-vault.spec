#
# spec file for package plasma-vault
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


%define kf5_version 5.98.0
%bcond_without released
Name:           plasma-vault
Version:        5.26.5
Release:        0
Summary:        Plasma applet and services for creating encrypted vaults
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-vault-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-vault-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  cmake(KF5Activities) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5NetworkManagerQt) >= %{kf5_version}
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version}
BuildRequires:  cmake(KF5SysGuard)
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
Requires:       plasma-vault-backend
Recommends:     %{name}-lang
# We recommend encfs for now as cryfs has certain issues
Recommends:     plasma-vault-backend-encfs

%description
Plasma Vault is a plasmoid for creating and managing encrypted vaults

%package backend-encfs
Summary:        Necessary packages for plasma-vault to support encfs vaults
Group:          Productivity/Security
Requires:       %{name} = %{version}
Requires:       encfs
Provides:       plasma-vault-backend

%description backend-encfs
This package pulls in dependencies for the plasma-vault encfs backend.

%package backend-cryfs
Summary:        Necessary packages for plasma-vault to support cryfs vaults
Group:          Productivity/Security
Requires:       %{name} = %{version}
# Previous versions could not update properly
Requires:       cryfs >= 0.9.9
Provides:       plasma-vault-backend

%description backend-cryfs
This package pulls in dependencies for the plasma-vault cryfs backend.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%make_install -C build
%if %{with released}
  %find_lang %{name} --with-man --all-name
%endif

%files
%license LICENSES/*
%{_kf5_plugindir}/kf5/kded/
%dir %{_kf5_plugindir}/plasma/applets
%{_kf5_plugindir}/plasma/applets/plasma_applet_vault.so
%dir %{_kf5_plasmadir}/plasmoids
%{_kf5_plasmadir}/plasmoids/org.kde.plasma.vault
%dir %{_kf5_plugindir}/kf5/kfileitemaction
%{_kf5_plugindir}/kf5/kfileitemaction/plasmavaultfileitemaction.so
%{_kf5_appstreamdir}/
%{_kf5_servicesdir}/plasma-applet-org.kde.plasma.vault.desktop

%if %{with released}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%files backend-encfs
%license LICENSES/*

%files backend-cryfs
%license LICENSES/*

%changelog
