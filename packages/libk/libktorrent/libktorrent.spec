#
# spec file for package libktorrent
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           libktorrent
Version:        24.05.1
Release:        0
Summary:        Torrent Downloading Library
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ktorrent
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  gmp-devel >= 6.0.0
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(libgcrypt) >= 1.4.5

%description
libktorrent is a torrent downloading library.

%package -n libKTorrent6
Summary:        Torrent Downloading Library
Provides:       libktorrent = %{version}
Obsoletes:      libktorrent < %{version}
Provides:       libktorrent-lang = %{version}
Obsoletes:      libktorrent-lang < %{version}

%description -n libKTorrent6
libktorrent is a torrent downloading library.

%package devel
Summary:        Development files for libktorrent
Requires:       libKTorrent6 = %{version}
Requires:       libboost_headers-devel >= 1.66.0
Requires:       cmake(KF6Archive) >= %{kf6_version}
Requires:       cmake(KF6Config) >= %{kf6_version}
Requires:       cmake(KF6KIO) >= %{kf6_version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Core5Compat) >= %{qt6_version}
Requires:       cmake(Qt6Network) >= %{qt6_version}
Requires:       gmp-devel >= 6.0.0
Requires:       pkgconfig(libgcrypt) >= 1.4.5

%description devel
This package includes the necessary files for development using libktorrent.

%lang_package -n libKTorrent6

%prep
%autosetup -p1

# The boost minimum version change is only cosmetic. Leap 15 only provides 1.66...
sed -i 's#1.71.0#1.66.0#' CMakeLists.txt

%build
%ifarch ppc64
%define _lto_cflags %{nil}
%endif

%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKTorrent6

%files -n libKTorrent6
%license LICENSES/*
%{_kf6_libdir}/libKTorrent6.so.*

%files devel
%{_kf6_cmakedir}/KTorrent6/
%{_kf6_includedir}/libktorrent/
%{_kf6_libdir}/libKTorrent6.so

%files -n libKTorrent6-lang -f %{name}.lang

%changelog
