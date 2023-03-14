#
# spec file for package hotspot
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


Name:           hotspot
Version:        1.4.1
Release:        0
Summary:        Perf GUI for performance analysis
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            https://github.com/KDAB/hotspot
Source:         https://github.com/KDAB/hotspot/releases/download/v%{version}/hotspot-v%{version}.tar.gz
# PATCH-FIX-UPSTREAM Make privilege escalation optional (CVE-2023-28144)
Patch0:         0001-Opt-in-via-CMake-to-allow-privilege-escalation.patch
BuildRequires:  glibc-devel-static
BuildRequires:  kddockwidgets-devel
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  libzstd-devel
BuildRequires:  qcustomplot-devel
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
# qcustomplot-devel in Leap 15 needs this dependency. Keep it there for the moment
%if 0%{?suse_version} == 1500
BuildRequires:  cmake(Qt5PrintSupport)
%endif
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(libdebuginfod)
Requires:       perf

%description
Hotspot is a standalone GUI for performance data with an UI like KCachegrind
around Linux perf.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake_kf5 -d build -- -DALLOW_PRIVILEGE_ESCALATION:BOOL=OFF

%install
%kf5_makeinstall -C build

# Unneeded
rm %{buildroot}%{_datadir}/dbus-1/{system-services/com.kdab.hotspot.perf.service,system.d/com.kdab.hotspot.perf.conf}
rm %{buildroot}%{_datadir}/polkit-1/actions/com.kdab.hotspot.perf.policy
%if %{pkg_vcmp kf5-filesystem >= 20220307}
  rm %{buildroot}%{_libexecdir}/{elevate_perf_privileges.sh,kauth/hotspot-auth-helper}
%else
  rm %{buildroot}%{_kf5_libdir}/libexec/{elevate_perf_privileges.sh,kauth/hotspot-auth-helper}
%endif

%files
%license LICENSE.GPL.txt
%doc README.md
%{_kf5_applicationsdir}/com.kdab.hotspot.desktop
%{_kf5_appstreamdir}/com.kdab.Hotspot.appdata.xml
%{_kf5_bindir}/hotspot
%if %{pkg_vcmp kf5-filesystem >= 20220307}
%{_libexecdir}/hotspot-perfparser
%else
%{_kf5_libdir}/libexec/hotspot-perfparser
%endif
%{_kf5_iconsdir}/hicolor/*/*/hotspot.png
%{_kf5_notifydir}/hotspot.notifyrc

%changelog
