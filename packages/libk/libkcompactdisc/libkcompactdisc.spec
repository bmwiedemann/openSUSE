#
# spec file for package libkcompactdisc
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
Name:           libkcompactdisc
Version:        22.12.0
Release:        0
Summary:        CD drive library for KDE Platform
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  alsa-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  xz
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)

%description
The KDE Compact Disc library provides an API for applications using
the KDE Platform to interface with the CD drives for audio CDs.

%package -n libKF5CompactDisc5
Summary:        CD drive library for KDE Platform
Provides:       %{name} = %{version}
Recommends:     %{name}-lang

%description -n libKF5CompactDisc5
The KDE Compact Disc library provides an API for applications using
the KDE Platform to interface with the CD drives for audio CDs.

%package devel
Summary:        Development files for the KDE CD drive library
Requires:       libKF5CompactDisc5 = %{version}

%description devel
This package contains the development headers for libkcompactdisc.

%lang_package

%prep
%autosetup -p1
FAKE_BUILDDATE=$(LC_ALL=C date -r %{_sourcedir}/%{name}.changes '+%{b} %{e} %{Y}')
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" src/wmlib/wm_helpers.c

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post  -n libKF5CompactDisc5 -p /sbin/ldconfig
%postun -n libKF5CompactDisc5 -p /sbin/ldconfig

%files -n libKF5CompactDisc5
%license COPYING*
%{_kf5_libdir}/libKF5CompactDisc.so.*

%files devel
%{_kf5_cmakedir}/KF5CompactDisc/
%{_kf5_includedir}/KCompactDisc/
%{_kf5_includedir}/kcompactdisc_version.h
%{_kf5_libdir}/libKF5CompactDisc.so

%files lang -f %{name}.lang

%changelog
