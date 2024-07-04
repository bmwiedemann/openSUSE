#
# spec file for package kinfocenter6
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

%define rname kinfocenter
%bcond_without released
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Name:           kinfocenter6
Version:        6.1.2
Release:        0
Summary:        Utility that provides information about a computer system
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch100:       0002-Look-for-binaries-in-Mesa-demos-path-as-well.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
# For creating the post-install symlink
BuildRequires:  systemsettings6
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libusb-1.0)
Provides:       kinfocenter5 = %{version}
Obsoletes:      kinfocenter5 < %{version}
Obsoletes:      kinfocenter5-lang < %{version}
Requires:       kf6-kcmutils-imports >= %{kf6_version}
# needed for the fileindexermonitor
Requires:       kf6-baloo-imports >= %{kf6_version}
# The executable is now a link to systemsettings6
Requires:       systemsettings6
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
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-html

%files
%license LICENSES/*.txt
%doc %lang(en) %{_kf6_htmldir}/en/kinfocenter/
%{_kf6_applicationsdir}/kcm_about-distro.desktop
%{_kf6_applicationsdir}/kcm_energyinfo.desktop
%{_kf6_applicationsdir}/org.kde.kinfocenter.desktop
%{_kf6_appstreamdir}/org.kde.kinfocenter.appdata.xml
%{_kf6_bindir}/kinfocenter
%dir %{_kf6_configdir}/menus
%{_kf6_configdir}/menus/kinfocenter.menu
%{_kf6_libdir}/libKInfoCenterInternal.so
%{_kf6_plugindir}/plasma/kcms/kcm_about-distro.so
%{_kf6_plugindir}/plasma/kcms/kcm_energyinfo.so
%dir %{_kf6_plugindir}/plasma/kcms/kinfocenter/
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_audio_information.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_block_devices.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_cpu.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_egl.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_firmware_security.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_glx.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_interrupts.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_kwinsupportinfo.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_network.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_opencl.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_pci.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_samba.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_usb.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_vulkan.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_wayland.so
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_xserver.so
%{_kf6_qmldir}/org/kde/kinfocenter/
%{_kf6_sharedir}/dbus-1/system-services/org.kde.kinfocenter.dmidecode.service
%{_kf6_dbuspolicydir}/org.kde.kinfocenter.dmidecode.conf
%{_kf6_sharedir}/desktop-directories/
%dir %{_kf6_sharedir}/kinfocenter/
%{_kf6_sharedir}/kinfocenter/categories/
%{_kf6_sharedir}/kinfocenter/firmware_security/
%{_kf6_sharedir}/polkit-1/actions/org.kde.kinfocenter.dmidecode.policy
%{_kf6_libexecdir}/kauth/kinfocenter-dmidecode-helper

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en

%changelog
