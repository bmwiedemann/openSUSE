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

%global kf5_version 5.58.0

%bcond_without lang
Name:           kinfocenter5
Version:        5.23.5
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
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/kinfocenter-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 1.2.0
BuildRequires:  kf5-filesystem
BuildRequires:  libraw1394-devel
BuildRequires:  pciutils-devel
BuildRequires:  systemsettings5
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Completion) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KDELibs4Support) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Package) >= %{kf5_version}
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KF5Solid) >= %{kf5_version}
BuildRequires:  cmake(KF5Solid) >= %{kf5_version}
BuildRequires:  cmake(KF5Wayland) >= %{_plasma5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libusb-1.0)
%ifarch %arm aarch64
BuildRequires:  pkgconfig(glesv2)
%else
BuildRequires:  pkgconfig(gl)
%endif
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
Conflicts:      kdebase4-workspace < 5.3.0
Recommends:     %{name}-lang
# needed for the fileindexermonitor
Requires:       baloo5-imports
# The executable is now a link to systemsettings5
Requires:       systemsettings5

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
%if %{with lang}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif

%files
%license LICENSES/*.txt
%{_kf5_bindir}/kinfocenter
%dir %{_kf5_plugindir}/
%{_kf5_plugindir}/kcm_devinfo.so
%{_kf5_plugindir}/kcm_info.so
%{_kf5_plugindir}/kcm_memory.so
%{_kf5_plugindir}/kcm_opengl.so
%{_kf5_plugindir}/kcm_pci.so
%{_kf5_plugindir}/kcm_usb.so
%{_kf5_plugindir}/kcm_view1394.so
%dir %{_kf5_plugindir}/kcms/
%{_kf5_plugindir}/kcms/kcm_about-distro.so
%{_kf5_plugindir}/kcms/kcm_energyinfo.so
%{_kf5_plugindir}/kcms/kcm_nic.so
%{_kf5_plugindir}/kcms/kcm_samba.so
%{_kf5_plugindir}/kcms/kcm_vulkan.so
%{_kf5_plugindir}/kcms/kcm_cpu.so
%{_kf5_plugindir}/kcms/kcm_interrupts.so
%{_kf5_plugindir}/kcms/kcm_wayland.so
%{_kf5_applicationsdir}/org.kde.kinfocenter.desktop
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en/
%doc %{_kf5_htmldir}/en/kinfocenter/
%{_kf5_sharedir}/kpackage/
%dir %{_kf5_sharedir}/kinfocenter/
%{_kf5_sharedir}/kinfocenter/categories/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_configdir}/menus/kinfocenter.menu
%{_kf5_sharedir}/desktop-directories/
%{_kf5_appstreamdir}/org.kde.kinfocenter.appdata.xml
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/kinfocenter/

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
