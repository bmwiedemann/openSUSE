#
# spec file for package kcm_sddm
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


# Internal QML import
%global __requires_exclude qmlimport\\(org\\.kde\\.private\\.kcms\\.sddm

%bcond_without released
Name:           kcm_sddm
Version:        5.26.5
Release:        0
Summary:        A sddm control module for KDE
License:        GPL-2.0-only
Group:          System/GUI/KDE
URL:            https://projects.kde.org/projects/kdereview/sddm-kcm/repository
Source:         https://download.kde.org/stable/plasma/%{version}/sddm-kcm-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/sddm-kcm-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch1:         0001-Support-default.session-symlink.patch
Patch2:         0002-Read-and-write-autologin-user-to-etc-sysconfig-displ.patch
Patch3:         0003-Don-t-add-a-Wayland-suffix-to-Wayland-sessions.patch
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Widgets)
Supplements:    packageand(sddm:plasma5-workspace)
Recommends:     %{name}-lang

%description
SDDM control module for KDE. It provides a graphical frontend for the
sddm.

%lang_package

%prep
%autosetup -p1 -n sddm-kcm-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%if %{with released}
  %find_lang %{name} %{name}.lang
%endif

%if %{with released}
%files lang -f %{name}.lang
%endif

%files
%doc README.md
%license COPYING
%{_kf5_sharedir}/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy
%{_kf5_dbuspolicydir}/org.kde.kcontrol.kcmsddm.conf
%{_kf5_sharedir}/dbus-1/system-services/org.kde.kcontrol.kcmsddm.service
%{_bindir}/sddmthemeinstaller
%{_kf5_knsrcfilesdir}/sddmtheme.knsrc
%{_kf5_applicationsdir}/kcm_sddm.desktop
%dir %{_kf5_sharedir}/kpackage/
%dir %{_kf5_sharedir}/kpackage/kcms/
%{_kf5_sharedir}/kpackage/kcms/kcm_sddm/
%dir %{_kf5_plugindir}/plasma/
%dir %{_kf5_plugindir}/plasma/kcms/
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings/
%{_kf5_plugindir}/plasma/kcms/systemsettings/kcm_sddm.so
%{_libexecdir}/kauth/kcmsddm_authhelper

%changelog
