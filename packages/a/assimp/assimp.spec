#
# spec file for package assimp
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


%define sover 3
Name:           assimp
Version:        3.3.1
Release:        0
Summary:        Library to load and process 3D scenes from various data formats
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://assimp.org/
#Source:         https://github.com/assimp/assimp/archive/v%{version}/%{name}-%{version}.tar.gz
Source:         %{name}-%{version}-suse.tar.gz
Source9:        sanitize_source.sh
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Assimp is a library to load and process geometric scenes from various data formats. It is tailored at typical game scenarios by supporting a node hierarchy, static or skinned meshes, materials, bone animations and potential texture data. The library is not designed for speed, it is primarily useful for importing assets from various sources once and storing it in a engine-specific format for easy and fast every-day-loading.

%package -n lib%{name}%{sover}
Summary:        Headers, docs and command-line utility for %{name}
Group:          System/Libraries

%description -n lib%{name}%{sover}
Assimp is a library to load and process geometric scenes from various data formats. It is tailored at typical game scenarios by supporting a node hierarchy, static or skinned meshes, materials, bone animations and potential texture data. The library is not designed for speed, it is primarily useful for importing assets from various sources once and storing it in a engine-specific format for easy and fast every-day-loading.

%package devel
Summary:        Headers, docs and command-line utility for %{name}
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       lib%{name}%{sover} = %{version}
Requires:       libstdc++-devel

%description devel
Assimp is a library to load and process geometric scenes from various data formats. It is tailored at typical game scenarios by supporting a node hierarchy, static or skinned meshes, materials, bone animations and potential texture data. The library is not designed for speed, it is primarily useful for importing assets from various sources once and storing it in a engine-specific format for easy and fast every-day-loading.

%prep
%setup -q

dos2unix LICENSE CREDITS CHANGES README
find . -type f -name "*.lib" -delete

%build
%cmake \
      -DCMAKE_BUILD_TYPE="Release" \
      -DASSIMP_LIB_INSTALL_DIR="%{_libdir}"
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
rm -rf examples/.deps
%cmake_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n lib%{name}%{sover}  -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%defattr(-,root,root)
%if 0%{?suse_version} > 1320
%license CREDITS LICENSE
%else
%doc CREDITS LICENSE
%endif
%{_libdir}/libassimp.so.3*

%files devel
%defattr(-,root,root)
%doc README CHANGES
%{_includedir}/assimp/
%{_bindir}/assimp
%{_libdir}/libassimp.so
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/assimp.pc

%changelog
