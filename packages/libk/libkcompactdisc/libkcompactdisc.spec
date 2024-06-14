#
# spec file for package libkcompactdisc
#
# Copyright (c) 2024 SUSE LLC
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


%define rname  libkcompactdisc
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define library_name libKCompactDisc6
%define so_suffix -5
%else
%define qt5 1
%define kf5_version 5.92.0
%define qt5_version 5.15.2
%define library_name libKF5CompactDisc
%define so_suffix 5
%endif
%bcond_without released
Name:           libkcompactdisc%{?pkg_suffix}
Version:        24.05.1
Release:        0
Summary:        CD drive library for KDE Platform
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
%if 0%{?qt6}
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
%else
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5Solid) >= %{kf5_version}
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
%endif

%description
The KDE Compact Disc library provides an API for applications using
the KDE Platform to interface with the CD drives for audio CDs.

%package -n %{library_name}%{so_suffix}
Summary:        CD drive library for KDE Platform
Recommends:     libkcompactdisc-lang = %{version}

%description -n %{library_name}%{so_suffix}
The KDE Compact Disc library provides an API for applications using
the KDE Platform to interface with the CD drives for audio CDs.

%package devel
Summary:        Development files for the KDE CD drive library
Requires:       %{library_name}%{so_suffix} = %{version}

%description devel
This package contains the development headers for libkcompactdisc.

%if 0%{?qt6}
%package -n libkcompactdisc-lang
Summary:        Translations for package libkcompactdisc
Supplements:    libKCompactDisc6-5 = %{version}
Supplements:    libKF5CompactDisc5 = %{version}
Provides:       libkcompactdisc-lang-all = %{version}
# Briefly existed in the devel project
Obsoletes:      libKF5CompactDisc5-lang
Obsoletes:      libKCompactDisc6-5-lang
BuildArch:      noarch

%description -n libkcompactdisc-lang
Provides translations for package libkcompactdisc.
%endif

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%if 0%{?qt6}
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE
%kf6_build
%else
%cmake_kf5 -d build
%cmake_build
%endif

%install
%if 0%{?qt6}
%kf6_install

%find_lang %{name} --all-name
%else
%kf5_makeinstall -C build

# Only one translation package for both flavors
rm -r %{buildroot}%{_datadir}/locale
%endif

%ldconfig_scriptlets -n %{library_name}%{so_suffix}

%files -n %{library_name}%{so_suffix}
%license COPYING*
%{_libdir}/%{library_name}.so.*

%files devel
%if 0%{?qt6}
%{_kf6_cmakedir}/KCompactDisc6/
%{_includedir}/KCompactDisc6/
%{_kf6_mkspecsdir}/qt_KCompactDisc.pri
%else
%{_kf5_cmakedir}/KF5CompactDisc/
%{_kf5_includedir}/KCompactDisc/
%{_kf5_mkspecsdir}/qt_KCompactDisc.pri
%endif
%{_libdir}/%{library_name}.so

%if 0%{?qt6}
%files -n libkcompactdisc-lang -f %{name}.lang
%endif

%changelog
