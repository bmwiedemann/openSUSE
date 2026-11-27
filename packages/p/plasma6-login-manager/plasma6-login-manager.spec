#
# spec file for package plasma6-login-manager
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2026 Shawn W Dunn <sfalken@opensuse.org>
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


%global kf6_version 6.30.0
%global qt6_version 6.11

%global rname plasma-login-manager
# Full Plasma6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.80.0 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

%bcond_without released
%bcond_without x11
Name:           plasma6-login-manager
Version:        6.8.3
Release:        0
Summary:        QML based login manager for the Plasma Desktop
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://invent.kde.org/plasma/plasma-login-manager
Source0:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-UPSTREAM / PATCH-FIX-OPENSUSE -- boo#1260402
Patch0:         disable-switch-to-greeter.patch
BuildRequires:  cmake >= 3.22
BuildRequires:  desktop-file-utils
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  shadow
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Screen) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickTest) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)
Requires:       (plasma6-login-manager-kcm if systemsettings6)
%systemd_requires
%sysusers_requires
Requires:       kf6-kauth
Requires:       kf6-kimageformats
Requires:       kwin6
%if %{with x11}
Requires:       xdm
%endif

%description
Plasma Login provides a display manager for KDE Plasma and with a new frontend
providing a greeter, wallpaper plugin integration and a System Settings
configuration module (KCM).

%package kcm
Summary:        KDE KCM for plasma6-login-manager
Requires:       plasma6-login-manager = %{version}-%{release}

%description kcm
Configuration module for plasma6-login-manager.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
LOGIN_DEFS_PATH="%{_sysconfdir}/login.defs"
[ -e "$LOGIN_DEFS_PATH" ] || LOGIN_DEFS_PATH="%{_distconfdir}/login.defs"

%cmake_kf6 \
  -DPAM_OS_CONFIGURATION:STRING="suse" \
  -DLOGIN_DEFS_PATH:PATH="${LOGIN_DEFS_PATH}" \
  -DSESSION_COMMAND:PATH="%{?_distconfdir}%{!?_distconfdir:%{_sysconfdir}}/X11/xdm/Xsession"

%kf6_build

%install
%kf6_install
%sysusers_generate_pre %{buildroot}%{_sysusersdir}/plasmalogin.conf plasmalogin plasmalogin.conf

%find_lang plasma_login
%find_lang kcm_plasmalogin

# De-conflict the dbus file
mv %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager{,-plasmalogin}.conf

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_plasmalogin.desktop

%pre -f plasmalogin.pre
%systemd_pre plasmalogin.service

%post
%systemd_post plasmalogin.service
%systemd_user_post plasma-login.service plasma-login-kwin_wayland.service plasma-login-wayland.target plasma-wallpaper.service
%tmpfiles_create %{_tmpfilesdir}/plasmalogin.conf

%preun
%service_del_preun plasmalogin.service
%systemd_user_preun plasma-login.service plasma-login-kwin_wayland.service plasma-login-wayland.target plasma-wallpaper.service

%postun
%service_del_postun_without_restart plasmalogin.service
%systemd_user_postun plasma-login.service plasma-login-kwin_wayland.service plasma-login-wayland.target plasma-wallpaper.service

%files -f plasma_login.lang
%license LICENSES/*
%doc README.md
%ghost %attr(711,root,root) %dir %{_rundir}/plasmalogin
%ghost %attr(750,plasmalogin,plasmalogin) %dir %{_localstatedir}/lib/plasmalogin
%{_kf6_bindir}/plasma-login-wallpaper
%{_kf6_bindir}/plasmalogin
%{_kf6_bindir}/startplasma-login-wayland
%{_kf6_dbuspolicydir}/org.freedesktop.DisplayManager-plasmalogin.conf
%dir %{_kf6_sharedir}/plasmalogin
%{_kf6_sharedir}/plasmalogin/scripts/
%{_libexecdir}/plasma-login-greeter
%{_libexecdir}/plasmalogin-helper
%{_libexecdir}/plasmalogin-helper-start-x11user
%{_pam_vendordir}/plasmalogin*
%{_sysusersdir}/plasmalogin.conf
%{_tmpfilesdir}/plasmalogin.conf
%{_unitdir}/plasmalogin.service
%{_userunitdir}/plasma-login-kwin_wayland.service
%{_userunitdir}/plasma-login-wayland.target
%{_userunitdir}/plasma-login.service
%{_userunitdir}/plasma-wallpaper.service

%files kcm -f kcm_plasmalogin.lang
%{_kf6_applicationsdir}/kcm_plasmalogin.desktop
%{_kf6_dbuspolicydir}/org.kde.kcontrol.kcmplasmalogin.conf
%{_kf6_libexecdir}/kauth/kcmplasmalogin_authhelper
%{_kf6_pluginsdir}/plasma/kcms/systemsettings/kcm_plasmalogin.so
%{_kf6_sharedir}/dbus-1/system-services/org.kde.kcontrol.kcmplasmalogin.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmplasmalogin.policy

%changelog
