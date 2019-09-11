#
# spec file for package libktorrent
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define ktor_ver 5.1

Name:           libktorrent
Version:        2.1
Release:        0
%define sonum   6
Summary:        Torrent Downloading Library
License:        GPL-2.0+
Group:          Productivity/Networking/File-Sharing
Url:            http://ktorrent.org/
Source0:        http://download.kde.org/stable/ktorrent/%{ktor_ver}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE require-lower-LibGMP.patch
Patch0:         require-lower-LibGMP.patch
# PATCH-FIX-UPSTREAM fix-build-with-qt5.6.patch
Patch1:         fix-build-with-qt5.6.patch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  doxygen
BuildRequires:  extra-cmake-modules
BuildRequires:  gmp-devel >= 5.1.3
BuildRequires:  karchive-devel
BuildRequires:  kcrash-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libqca-qt5-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  solid-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libktorrent is a torrent downloading library.

%package devel
Summary:        Development files for libktorrent
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} > 1325
Requires:       libboost_headers-devel
%else
Requires:       boost-devel
%endif
Requires:       gmp-devel
Requires:       libKF5Torrent%{sonum} = %{version}
Requires:       libqca-qt5-devel

%description devel
This package includes the necessary files for development using libktorrent.

%package -n libKF5Torrent%{sonum}
Summary:        Torrent Downloading Library
Group:          System/Libraries
Recommends:     %{name}-lang = %{version}
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libKF5Torrent%{sonum}
libktorrent is a torrent downloading library.

%lang_package
%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%find_lang libktorrent5 %{name}.lang

%post -n libKF5Torrent%{sonum} -p /sbin/ldconfig

%postun -n libKF5Torrent%{sonum} -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/libktorrent/
%{_kf5_libdir}/libKF5Torrent.so
%{_kf5_cmakedir}/KF5Torrent/

%files -n libKF5Torrent%{sonum}
%defattr(-,root,root,-)
%doc COPYING ChangeLog RoadMap
%{_kf5_libdir}/libKF5Torrent.so.%{sonum}*

%files lang -f %{name}.lang
%defattr(-,root,root,-)

%changelog
