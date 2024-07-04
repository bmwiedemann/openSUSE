#
# spec file for package sddm-kcm6
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

%define rname sddm-kcm

%bcond_without released
Name:           sddm-kcm6
Version:        6.1.2
Release:        0
Summary:        A sddm control module for KDE
License:        GPL-2.0-only
URL:            https://projects.kde.org/projects/kdereview/sddm-kcm/repository
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch1:         0001-Support-default.session-symlink.patch
Patch2:         0002-Read-and-write-autologin-user-to-etc-sysconfig-displ.patch
Patch3:         0003-Don-t-add-a-Wayland-suffix-to-Wayland-sessions.patch
# PATCH-FEATURE (?)-OPENSUSE
Patch4:         0001-Remove-some-features-with-questionable-security.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Supplements:    (sddm and plasma6-workspace)
Provides:       kcm_sddm = %{version}
Obsoletes:      kcm_sddm < %{version}
Obsoletes:      kcm_sddm-lang < %{version}

%description
SDDM control module for Plasma. It provides a graphical frontend for the SDDM.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang kcm_sddm

%files
%doc README.md
%license LICENSES/*
%{_kf6_bindir}/sddmthemeinstaller
%{_kf6_applicationsdir}/kcm_sddm.desktop
%{_kf6_dbuspolicydir}/org.kde.kcontrol.kcmsddm.conf
%{_kf6_knsrcfilesdir}/sddmtheme.knsrc
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_sddm.so
%{_kf6_sharedir}/dbus-1/system-services/org.kde.kcontrol.kcmsddm.service
%{_kf6_sharedir}/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy
%{_kf6_libexecdir}/kauth/kcmsddm_authhelper

%files lang -f kcm_sddm.lang

%changelog
