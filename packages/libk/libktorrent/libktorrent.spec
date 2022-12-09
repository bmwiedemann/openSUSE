#
# spec file for package libktorrent
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


%define sonum   6
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           libktorrent
Version:        22.12.0
Release:        0
Summary:        Torrent Downloading Library
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ktorrent
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  extra-cmake-modules
BuildRequires:  gmp-devel >= 6.0.0
BuildRequires:  libboost_headers-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Core) >= 5.14.0
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Xml)

%description
libktorrent is a torrent downloading library.

%package devel
Summary:        Development files for libktorrent
Requires:       gmp-devel
Requires:       libKF5Torrent%{sonum} = %{version}
Requires:       libboost_headers-devel
Requires:       libgcrypt-devel
Requires:       cmake(KF5Archive)
Requires:       cmake(KF5Config)
Requires:       cmake(KF5KIO)
Requires:       cmake(Qca-qt5)
Requires:       cmake(Qt5Core)
Requires:       cmake(Qt5Network)

%description devel
This package includes the necessary files for development using libktorrent.

%package -n libKF5Torrent%{sonum}
Summary:        Torrent Downloading Library
Recommends:     %{name}-lang = %{version}
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libKF5Torrent%{sonum}
libktorrent is a torrent downloading library.

%lang_package

%prep
%autosetup -p1

# The boost minimum version change is only cosmetic. Leap 15.2 provides 1.66
sed -i 's#1.71.0#1.66.0#' CMakeLists.txt

%build
%ifarch ppc64
%define _lto_cflags %{nil}
%endif

%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang libktorrent5 %{name}.lang

%post -n libKF5Torrent%{sonum} -p /sbin/ldconfig
%postun -n libKF5Torrent%{sonum} -p /sbin/ldconfig

%files devel
%{_kf5_cmakedir}/KF5Torrent/
%{_kf5_includedir}/libktorrent/
%{_kf5_libdir}/libKF5Torrent.so

%files -n libKF5Torrent%{sonum}
%license LICENSES/*
%doc ChangeLog RoadMap
%{_kf5_libdir}/libKF5Torrent.so.*

%files lang -f %{name}.lang

%changelog
