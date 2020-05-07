#
# spec file for package libksysguard5
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_without lang
Name:           libksysguard5
Version:        5.18.5
Release:        0
Summary:        Task management and system monitoring library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/libksysguard-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/libksysguard-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        baselibs.conf
BuildRequires:  extra-cmake-modules >= 1.2.0
BuildRequires:  kf5-filesystem
BuildRequires:  xz
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Network) >= 5.4.0
%ifnarch ppc ppc64 ppc64le s390 s390x riscv64
BuildRequires:  cmake(Qt5WebChannel) >= 5.4.0
BuildRequires:  cmake(Qt5WebEngineWidgets) >= 5.4.0
%endif
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.4.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} < 1330
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
BuildRequires:  gcc7-c++
%endif
Recommends:     %{name}-lang

%description
Task management and system monitoring library.

%package devel
Summary:        Task management and system monitoring library -- devel files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       cmake(KF5Config)
Requires:       cmake(KF5I18n)
Requires:       cmake(KF5IconThemes)
Requires:       cmake(Qt5Core) >= 5.4.0
Requires:       cmake(Qt5Network) >= 5.4.0
Requires:       cmake(Qt5Widgets) >= 5.4.0
Conflicts:      kdebase4-workspace-devel

%description devel
Task management and system monitoring library. This package contains development
files.

%package helper
Summary:        Task management and system monitoring library -- helper files
Group:          Development/Libraries/C and C++
Conflicts:      kdebase4-workspace < 5.3.0

%description helper
Task management and system monitoring library. This package contains helper files
for actions that require elevated privileges.

%lang_package

%prep
%autosetup -p1 -n libksysguard-%{version}

%build
  %if 0%{?suse_version} < 1330
  # It does not build with the default compiler (GCC 4.8) on Leap 42.x
    export CC=gcc-7
    export CXX=g++-7
  %endif
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
%endif

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_libdir}/libksgrd.so.*
%{_kf5_libdir}/liblsofui.so.*
%{_kf5_libdir}/libksignalplotter.so.*
%{_kf5_libdir}/libprocesscore.so.*
%{_kf5_libdir}/libprocessui.so.*
%{_kf5_sharedir}/ksysguard/
%{_kf5_debugdir}/*.categories

%files helper
%license COPYING*
%{_kf5_libdir}/libexec/
%{_kf5_dbuspolicydir}/org.kde.ksysguard.processlisthelper.conf
%{_kf5_sharedir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_kf5_sharedir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy

%files devel
%license COPYING*
%{_includedir}/ksysguard/
%{_kf5_libdir}/cmake/KF5SysGuard/
%{_kf5_libdir}/libksgrd.so
%{_kf5_libdir}/liblsofui.so
%{_kf5_libdir}/libksignalplotter.so
%{_kf5_libdir}/libprocesscore.so
%{_kf5_libdir}/libprocessui.so

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
