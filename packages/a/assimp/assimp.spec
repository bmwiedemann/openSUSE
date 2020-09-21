#
# spec file for package assimp
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


%define sover 5
Name:           assimp
Version:        5.0.1
Release:        0
Summary:        Library to load and process 3D scenes from various data formats
License:        BSD-3-Clause AND MIT
Group:          Development/Libraries/C and C++
URL:            https://assimp.org/
Source0:        %{name}-%{version}.tar.xz
Patch0:         do-not-install-irrXML.patch
# PATCH-FIX-UPSTREAM -- Don't hardcode the library and binary location
Patch1:         0001-use-GNUInstallDirs-where-possible.patch
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  irrlicht-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(zlib)

%description
Assimp is a library to load and process geometric scenes from various data formats.
It is tailored at typical game scenarios by supporting a node hierarchy, static or skinned meshes,
materials, bone animations and potential texture data. The library is not designed for speed,
it is primarily useful for importing assets from various sources once and storing it in a
engine-specific format for easy and fast every-day-loading.

%package -n lib%{name}%{sover}
Summary:        Library to load and process 3D scenes from various data formats
Group:          System/Libraries

%description -n lib%{name}%{sover}
Assimp is a library to load and process geometric scenes from various data formats.
It is tailored at typical game scenarios by supporting a node hierarchy, static or skinned meshes,
materials, bone animations and potential texture data. The library is not designed for speed,
it is primarily useful for importing assets from various sources once and storing it in a
engine-specific format for easy and fast every-day-loading.

%package devel
Summary:        Headers, docs and command-line utility for %{name}
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       lib%{name}%{sover} = %{version}
Requires:       libstdc++-devel

%description devel
Assimp is a library to load and process geometric scenes from various data formats.
It is tailored at typical game scenarios by supporting a node hierarchy, static or skinned meshes,
materials, bone animations and potential texture data. The library is not designed for speed,
it is primarily useful for importing assets from various sources once and storing it in a
engine-specific format for easy and fast every-day-loading.

%prep
%autosetup -p1

%build
%cmake

%cmake_build

%install
%cmake_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
pushd build/test
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ctest --output-on-failure --force-new-ctest-process
popd

%post -n lib%{name}%{sover}  -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license LICENSE
%{_libdir}/libassimp.so.%{sover}*

%files devel
%doc README CHANGES CREDITS
%{_includedir}/assimp/
%{_bindir}/assimp
%{_libdir}/libassimp.so
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/assimp.pc

%changelog
