#
# spec file for package libkcompactdisc
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           libkcompactdisc
Version:        20.08.2
Release:        0
Summary:        CD drive library for KDE Platform
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  alsa-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  xz
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
The KDE Compact Disc library provides an API for applications using
the KDE Platform to interface with the CD drives for audio CDs.

%package -n libKF5CompactDisc5
Summary:        CD drive library for KDE Platform
Group:          System/Libraries
Provides:       %{name} = %{version}
Recommends:     %{name}-lang

%description -n libKF5CompactDisc5
The KDE Compact Disc library provides an API for applications using
the KDE Platform to interface with the CD drives for audio CDs.

%package devel
Summary:        Development files for the KDE CD drive library
Group:          Development/Libraries/C and C++
Requires:       libKF5CompactDisc5 = %{version}

%description devel
This package contains the development headers for libkcompactdisc.

%lang_package

%prep
%setup -q
FAKE_BUILDDATE=$(LC_ALL=C date -r %{_sourcedir}/%{name}.changes '+%{b} %{e} %{Y}')
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" src/wmlib/wm_helpers.c

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post  -n libKF5CompactDisc5 -p /sbin/ldconfig
%postun -n libKF5CompactDisc5 -p /sbin/ldconfig

%files -n libKF5CompactDisc5
%license COPYING*
%{_kf5_libdir}/libKF5CompactDisc.so.*

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5CompactDisc/
%{_kf5_includedir}/KCompactDisc/
%{_kf5_includedir}/kcompactdisc_version.h
%{_kf5_libdir}/libKF5CompactDisc.so
%{_kf5_mkspecsdir}/qt_KCompactDisc.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
