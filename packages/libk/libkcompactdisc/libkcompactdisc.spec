#
# spec file for package libkcompactdisc
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.14.0
%define qt6_version 6.8.0

%bcond_without released
Name:           libkcompactdisc
Version:        25.08.3
Release:        0
Summary:        CD drive library for KDE Platform
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}

%description
The KDE Compact Disc library provides an API for applications using
the KDE Platform to interface with the CD drives for audio CDs.

%package -n libKCompactDisc6-5
Summary:        CD drive library for KDE Platform
Recommends:     libkcompactdisc-lang = %{version}

%description -n libKCompactDisc6-5
The KDE Compact Disc library provides an API for applications using
the KDE Platform to interface with the CD drives for audio CDs.

%package -n libkcompactdisc-qt6-devel
Summary:        Development files for the KDE CD drive library
Requires:       libKCompactDisc6-5 = %{version}

%description -n libkcompactdisc-qt6-devel
This package contains the development headers for libkcompactdisc.

%package -n libkcompactdisc-lang
Summary:        Translations for package libkcompactdisc
Supplements:    libKCompactDisc6-5 = %{version}
Supplements:    libKF5CompactDisc5 = %{version}
Provides:       libkcompactdisc-lang-all = %{version}
BuildArch:      noarch

%description -n libkcompactdisc-lang
Provides translations for package libkcompactdisc.

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKCompactDisc6-5

%files -n libKCompactDisc6-5
%license COPYING*
%{_libdir}/libKCompactDisc6.so.*

%files -n libkcompactdisc-qt6-devel
%{_includedir}/KCompactDisc6/
%{_kf6_cmakedir}/KCompactDisc6/
%{_kf6_mkspecsdir}/qt_KCompactDisc.pri
%{_libdir}/libKCompactDisc6.so

%files -n libkcompactdisc-lang -f %{name}.lang

%changelog
