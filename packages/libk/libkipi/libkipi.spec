#
# spec file for package libkipi
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _so 32_0_0
%define libname libKF5Kipi
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           libkipi
Version:        19.08.1
Release:        0
Summary:        KDE Image Plugin Interface
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
#PATCH-FIX-OPENSUSE dont-install-pics.diff - Don't install icons since those are included in libkipi11 in SLE12
Patch0:         dont-install-pics.diff
BuildRequires:  extra-cmake-modules >= 1.1.0
BuildRequires:  kconfig-devel >= 5.1.0
BuildRequires:  ki18n-devel >= 5.1.0
BuildRequires:  kservice-devel >= 5.1.0
BuildRequires:  kxmlgui-devel >= 5.1.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
Requires:       %{libname}%{_so} = %{version}

%description
This package provides a generic KDE Image Plug-in Interface used by
some KDE image applications. Plug-ins for this interface are in the
kipi-plugins package.

%package -n %{libname}%{_so}
Summary:        KDE Image Plug-In Interface
Group:          System/Libraries
Requires:       libkipi-data >= %{version}
%if !0%{?is_opensuse} && 0%{?sle_version} < 150000
#kipi icons are provided by libkipi11
Requires:       libkipi11
%endif

%description -n %{libname}%{_so}
This package provides a generic KDE image plug-in interface used by
some KDE image applications. Plug-ins for this interface are in the
kipi-plugins package.

%package data
Summary:        KDE Image Plug-In Interface - data files
Group:          System/Libraries
Conflicts:      %{libname}30_0_0

%description data
This package contains data files needed by the KDE image plug-in library.

%package devel
Summary:        KDE Image Plugin Interface
Group:          Development/Libraries/KDE
Requires:       %{libname}%{_so} = %{version}
Requires:       kconfig-devel >= 5.1.0
Requires:       ki18n-devel >= 5.1.0
Requires:       kservice-devel >= 5.1.0
Requires:       kxmlgui-devel >= 5.1.0
Requires:       pkgconfig(Qt5Core) >= 5.2.0
Requires:       pkgconfig(Qt5Gui) >= 5.2.0
Requires:       pkgconfig(Qt5Widgets) >= 5.2.0
Obsoletes:      libkipi-kf5-devel < %{version}
Provides:       libkipi-kf5-devel = %{version}

%description devel
This package provides a generic KDE Image Plug-in Interface used by
some KDE image applications. Plug-ins for this interface are in the
kipi-plugins package.

%prep
%setup -q
%if !0%{?is_opensuse} && 0%{?sle_version} < 150000
%patch0 -p1
%endif

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build

%post -n %{libname}%{_so} -p /sbin/ldconfig
%postun -n %{libname}%{_so} -p /sbin/ldconfig

%files -n %{libname}%{_so}
%{_kf5_libdir}/%{libname}.so.*

%files data
%if 0%{?is_opensuse} || !0%{?sle_version} < 150000
%{_kf5_iconsdir}/hicolor/*/apps/kipi.png
%endif
%{_kf5_servicetypesdir}/kipiplugin.desktop

%files devel
%license COPYING
%doc README
%{_kf5_cmakedir}/KF5Kipi/
%{_kf5_includedir}/KIPI/
%{_kf5_includedir}/libkipi_version.h
%{_kf5_libdir}/%{libname}.so

%changelog
