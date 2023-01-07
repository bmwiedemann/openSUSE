#
# spec file for package libkdcraw
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


%define _so 5
%define lname libKF5KDcraw
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           libkdcraw
Version:        22.12.1
Release:        0
Summary:        Shared library interface around dcraw
License:        LGPL-2.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  pkgconfig(libraw) >= 0.16.0
Obsoletes:      libkdcraw-kf5 < %{version}
Provides:       libkdcraw-kf5 = %{version}

%description
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.  The library documentation is available on header
files.

This library is used by kipi-plugins, digiKam and others kipi host
programs.

%package -n %{lname}%{_so}
Summary:        Shared library interface around dcraw

%description -n %{lname}%{_so}
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.  The library documentation is available on header
files.

This library is used by kipi-plugins, digiKam and others kipi host
programs.

%package devel
Summary:        Shared library interface around dcraw
Requires:       %{lname}%{_so} = %{version}
Obsoletes:      libkdcraw-kf5-devel < %{version}
Provides:       libkdcraw-kf5-devel = %{version}

%description devel
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.  The library documentation is available on header
files.

This library is used by kipi-plugins, digiKam and others kipi host
programs.

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build -- -DENABLE_LCMS2=true -DENABLE_RAWSPEED=true
  %cmake_build

%install
  %kf5_makeinstall -C build

%post -n %{lname}%{_so} -p /sbin/ldconfig
%postun -n %{lname}%{_so} -p /sbin/ldconfig

%files -n %{lname}%{_so}
%license LICENSES/*
%{_kf5_debugdir}/libkdcraw.categories
%{_kf5_libdir}/%{lname}.so.*

%files devel
%doc README
%{_kf5_cmakedir}/KF5KDcraw/
%{_kf5_includedir}/
%{_kf5_libdir}/%{lname}.so

%changelog
