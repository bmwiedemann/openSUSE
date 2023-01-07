#
# spec file for package krfb
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           krfb
Version:        22.12.1
Release:        0
Summary:        Screen sharing using the VNC/RFB protocol
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/krfb
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  LibVNCServer-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  pipewire-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xcb-util-image-devel
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)

%description
VNC-compatible server to share KDE desktops.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif

%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.krfb System RemoteAccess

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/krfb/
%{_kf5_applicationsdir}/org.kde.krfb.desktop
%{_kf5_applicationsdir}/org.kde.krfb.virtualmonitor.desktop
%{_kf5_appstreamdir}/org.kde.krfb.appdata.xml
%{_kf5_bindir}/krfb
%{_kf5_bindir}/krfb-virtualmonitor
%{_kf5_debugdir}/krfb.categories
%{_kf5_iconsdir}/hicolor/*/apps/krfb.*
%{_kf5_libdir}/libkrfbprivate.so*
%{_kf5_plugindir}/krfb/
%{_kf5_sharedir}/krfb/

%files lang -f %{name}.lang

%changelog
