#
# spec file for package alure
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2012 openSUSE_user1
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


Name:           alure
Version:        1.2
Release:        0
Summary:        Audio Library Tools REloaded
# ALURE code is LGPL-2.0+; note -devel subpackage has its own license tag
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/kcat/alure
Source0:        %{name}-%{version}.tar.bz2
# PATCh-FIX-UPSTREAM alure-gcc47.patch -- patch for build with gcc47
Patch0:         alure-gcc47.patch
# PATCH-FIX-UPSTREAM alure-lib-suffix.patch -- Enable installation in suffixed directory
Patch1:         alure-lib-suffix.patch
BuildRequires:  cmake
BuildRequires:  flac-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc-c++
BuildRequires:  libmodplug-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRequires:  pkgconfig

%description
ALURE is a utility library to help manage common tasks with OpenAL
applications. This includes device enumeration and initialization,
file loading, and streaming.

%package        devel
Summary:        Development files for %{name}
# Devel doc includes some files under GPLv2+ from NaturalDocs
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n libalure1
Summary:        Utility library around OpenAL
License:        LGPL-2.0-or-later
Group:          System/Libraries

%description -n libalure1
ALURE is a utility library to help manage common tasks with OpenAL
applications.

%prep
%autosetup -p0

%build
%cmake \
  -DBUILD_STATIC=OFF \
  -DMPG123=OFF \
  -DMODPLUG=ON
%cmake_build

%install
%cmake_install

find %{buildroot} -type f -name "*.la" -delete -print

# remove installed html doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}/html
# fix encoding
sed -i 's/\r$//' docs/html/javascript/main.js docs/html/styles/1.css

%post   -n libalure1 -p /sbin/ldconfig
%postun -n libalure1 -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/alure*

%files -n libalure1
%{_libdir}/libalure.so.*

%files devel
%doc docs/html examples
%{_includedir}/AL/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
