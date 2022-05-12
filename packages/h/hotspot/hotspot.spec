#
# spec file for package hotspot
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


Name:           hotspot
Version:        1.3.0
Release:        0
Summary:        Perf GUI for performance analysis
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            https://github.com/KDAB/hotspot
Source:         https://github.com/KDAB/hotspot/releases/download/v%{version}/hotspot-v%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-CMake-Don-t-assume-KDE_INSTALL_-variables-are-relati.patch
BuildRequires:  glibc-devel-static
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  libzstd-devel
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
Requires:       perf

%description
Hotspot is a standalone GUI for performance data with an UI like KCachegrind
around Linux perf.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake_kf5 -d build

%install
%kf5_makeinstall -C build

%files
%license LICENSE.GPL.txt
%doc README.md
%{_kf5_bindir}/hotspot
%if %{pkg_vcmp kf5-filesystem >= 20220307}
%{_libexecdir}/hotspot-perfparser
%{_libexecdir}/elevate_perf_privileges.sh
%else
%{_kf5_libdir}/libexec/hotspot-perfparser
%{_kf5_libdir}/libexec/elevate_perf_privileges.sh
%endif
%{_kf5_iconsdir}/hicolor/*/*/hotspot.png

%changelog
