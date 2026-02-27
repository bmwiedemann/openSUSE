#
# spec file for package plasma6-vault
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.18.0
%define qt6_version 6.9.0

%define rname plasma-vault

%bcond_without released
%bcond_without encfs
%bcond_without cryfs
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Name:           plasma6-vault
Version:        6.6.1
Release:        0
Summary:        Plasma applet and services for creating encrypted vaults
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KSysGuard) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       plasma6-vault-backend
Requires:       (/usr/bin/fusermount3 or /usr/bin/fusermount)
# encfs is EOL, creating new EncFS vaults will no longer be supported
# See https://github.com/KDE/plasma-vault/commit/ef0762f188ce6568b8fa7babbce852010366c935
Recommends:     plasma6-vault-backend-gocryptfs
Provides:       plasma-vault = %{version}
Obsoletes:      plasma-vault < %{version}
Obsoletes:      plasma-vault-lang < %{version}

%description
Plasma Vault is a plasmoid for creating and managing encrypted vaults

%if %{with encfs}
%package backend-encfs
Summary:        Necessary packages for plasma6-vault to support encfs vaults
Requires:       encfs >= 1.9.1
Requires:       plasma6-vault = %{version}
Provides:       plasma6-vault-backend = %{version}
Obsoletes:      plasma-vault-backend-encfs < %{version}
BuildArch:      noarch

%description backend-encfs
This package pulls in dependencies for the plasma6-vault encfs backend.
%endif

%if %{with cryfs}
%package backend-cryfs
Summary:        Necessary packages for plasma6-vault to support cryfs vaults
Requires:       plasma6-vault = %{version}
# Previous versions could not update properly
Requires:       cryfs >= 0.9.9
Provides:       plasma6-vault-backend = %{version}
Obsoletes:      plasma-vault-backend-cryfs < %{version}
BuildArch:      noarch

%description backend-cryfs
This package pulls in dependencies for the plasma6-vault cryfs backend.
%endif

%package backend-gocryptfs
Summary:        Necessary packages for plasma6-vault to support gocryptfs vaults
Requires:       gocryptfs >= 1.8
Requires:       plasma6-vault = %{version}
Provides:       plasma6-vault-backend = %{version}
Obsoletes:      plasma-vault-backend-gocryptfs < %{version}
BuildArch:      noarch

%description backend-gocryptfs
This package pulls in dependencies for the plasma6-vault gocryptfs backend.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --all-name

%files
%license LICENSES/*
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.vault/
%{_kf6_plugindir}/kf6/kded/plasmavault.so
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/plasmavaultfileitemaction.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.vault.so

%files lang -f %{name}.lang
%license LICENSES/*

%if %{with encfs}
%files backend-encfs
%license LICENSES/*
%endif

%if %{with cryfs}
%files backend-cryfs
%license LICENSES/*
%endif

%files backend-gocryptfs
%license LICENSES/*

%changelog
