#
# spec file for package kinfocenter5
#
# Copyright (c) 2022 SUSE LLC
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


# Internal QML imports
%global __requires_exclude qmlimport\\(org\\.kde\\.kinfocenter.*

%global kf5_version 5.98.0

%bcond_without released
Name:           kinfocenter5
Version:        5.26.4
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Utility that provides information about a computer system
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/kinfocenter-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kinfocenter-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch100:       0002-Look-for-binaries-in-Mesa-demos-path-as-well.patch
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  systemsettings5
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Package) >= %{kf5_version}
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KF5Solid) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(libusb-1.0)
Conflicts:      kdebase4-workspace < 5.3.0
Recommends:     %{name}-lang
# needed for the fileindexermonitor
Requires:       baloo5-imports
# The executable is now a link to systemsettings5
Requires:       systemsettings5
# lspci is called by the PCI KCM
Requires:       pciutils
# GLX is always present
Requires:       /usr/bin/glxinfo
# Vulkan might not be needed
Requires:       (/usr/bin/vulkaninfo if libvulkan1)
# Plasma Wayland and X11 sessions are always installed
Requires:       /usr/bin/wayland-info
Requires:       /usr/bin/xdpyinfo
# Note: Not available as /usr/bin/eglinfo yet (boo#1195695)
Recommends:     /usr/bin/eglinfo
# The "Firmware Security" page does fwupdmgr ... | aha | ...
Recommends:     (aha if fwupd)
# Mesa-demos includes it, but as a whole it's too fat,
# so don't pull it in by default.
Suggests:       Mesa-demo

%description
KDE Utility that provides information about a computer system.

%lang_package

%prep
%autosetup -p1 -n kinfocenter-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif

%files
%license LICENSES/*.txt
%{_kf5_applicationsdir}/kcm_about-distro.desktop
%{_kf5_bindir}/kinfocenter
%{_kf5_libdir}/libKInfoCenterInternal.so
%dir %{_kf5_plugindir}/
%dir %{_kf5_plugindir}/plasma/
%dir %{_kf5_plugindir}/plasma/kcms/
%{_kf5_plugindir}/plasma/kcms/kcm_about-distro.so
%{_kf5_plugindir}/plasma/kcms/kcm_energyinfo.so
%dir %{_kf5_plugindir}/plasma/kcms/kinfocenter/
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_cpu.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_devinfo.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_egl.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_firmware_security.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_glx.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_interrupts.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_nic.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_pci.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_kwinsupportinfo.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_samba.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_usb.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_vulkan.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_wayland.so
%{_kf5_plugindir}/plasma/kcms/kinfocenter/kcm_xserver.so
%{_kf5_applicationsdir}/org.kde.kinfocenter.desktop
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en/
%doc %{_kf5_htmldir}/en/kinfocenter/
%{_kf5_sharedir}/kpackage/
%dir %{_kf5_sharedir}/kinfocenter/
%{_kf5_sharedir}/kinfocenter/categories/
%{_kf5_configdir}/menus/kinfocenter.menu
%{_kf5_sharedir}/desktop-directories/
%dir %{_libexecdir}/kauth/
%{_libexecdir}/kauth/kinfocenter-dmidecode-helper
%{_kf5_sharedir}/dbus-1/system-services/org.kde.kinfocenter.dmidecode.service
%{_kf5_sharedir}/dbus-1/system.d/org.kde.kinfocenter.dmidecode.conf
%{_kf5_sharedir}/polkit-1/actions/org.kde.kinfocenter.dmidecode.policy
%{_kf5_appstreamdir}/org.kde.kinfocenter.appdata.xml
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/kinfocenter/

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
