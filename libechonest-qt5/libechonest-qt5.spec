#
# spec file for package libechonest-qt5
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _major_version 2
%define _minor_version 3
%define _patch_version 0
%define soname %{_major_version}_%{_minor_version}
Name:           libechonest-qt5
Version:        %{_major_version}.%{_minor_version}.%{_patch_version}+20150206
Release:        0
# main package
Summary:        Qt library for communicating with The Echo Nest
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            https://projects.kde.org/libechonest
Source:         libechonest-%{version}.tar.bz2
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM -- 0001-Fix-build-with-Qt-5.11.patch
Patch0:         0001-Fix-build-with-Qt-5.11.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Xml)

%description
It currently supports almost all of the features of the Echo Nest API, including all the API functions.

# bin package
%package -n libechonest5-%{soname}
Summary:        Qt library for communicating with The Echo Nest
Group:          System/Libraries

%description  -n libechonest5-%{soname}
It currently supports almost all of the features of the Echo Nest API, including all the API functions.

# devel package
%package devel
Summary:        Qt library for communicating with The Echo Nest
Group:          Development/Libraries/C and C++
Requires:       libechonest5-%{soname} = %{version}

%description devel
It currently supports almost all of the features of the Echo Nest API, including all the API functions.

%prep
%autosetup -p1 -n libechonest-%{version}

%build
%cmake -DBUILD_WITH_QT4=OFF \
       -DECHONEST_BUILD_TESTS=OFF

%make_jobs

%install
%cmake_install

%post -n libechonest5-%{soname} -p /sbin/ldconfig
%postun -n libechonest5-%{soname} -p /sbin/ldconfig

%files -n libechonest5-%{soname}
%license COPYING*
%{_libdir}/libechonest*.so.*

%files devel
%license COPYING*
%{_libdir}/libechonest*.so
%{_includedir}/echonest5/
%{_libdir}/pkgconfig/libechonest5.pc

%changelog
