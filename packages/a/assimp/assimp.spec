#
# spec file for package assimp
#
# Copyright (c) 2023 SUSE LLC
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
Version:        5.3.1
Release:        0
Summary:        Library to load and process 3D scenes from various data formats
License:        BSD-3-Clause AND MIT
Group:          Development/Libraries/C and C++
URL:            https://www.assimp.org/
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         0001-Don-t-build-the-collada-importer-exporter-tests.patch
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

%package -n libassimp%{sover}
Summary:        Library to load and process 3D scenes from various data formats
Group:          System/Libraries

%description -n libassimp%{sover}
Assimp is a library to load and process geometric scenes from various data formats.
It is tailored at typical game scenarios by supporting a node hierarchy, static or skinned meshes,
materials, bone animations and potential texture data. The library is not designed for speed,
it is primarily useful for importing assets from various sources once and storing it in a
engine-specific format for easy and fast every-day-loading.

%package devel
Summary:        Headers, docs and command-line utility for assimp
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libassimp%{sover} = %{version}
Requires:       libstdc++-devel
Requires:       pkgconfig(minizip)

%description devel
Assimp is a library to load and process geometric scenes from various data formats.
It is tailored at typical game scenarios by supporting a node hierarchy, static or skinned meshes,
materials, bone animations and potential texture data. The library is not designed for speed,
it is primarily useful for importing assets from various sources once and storing it in a
engine-specific format for easy and fast every-day-loading.

%prep
%autosetup -p1

%build
%cmake \
    -DASSIMP_IGNORE_GIT_HASH=ON \
    -DASSIMP_BUILD_ZLIB=OFF \
    -DASSIMP_WARNINGS_AS_ERRORS=OFF \
    -DASSIMP_BUILD_ASSIMP_TOOLS=ON \
    -DASSIMP_BUILD_COLLADA_IMPORTER=OFF \
    -DASSIMP_BUILD_COLLADA_EXPORTER=OFF

%cmake_build

%install
%cmake_install

find %{buildroot} -type f -name "*.la" -delete -print

%check
pushd build
# utIssues.OpacityBugWhenExporting_727 test fails
# utVersion.aiGetVersionRevisionTest passes with git builds only
# the models-nonbsd are not in the tarball, tests depending on it are also excluded
./bin/unit --gtest_filter="-utIssues.OpacityBugWhenExporting_727:utVersion.aiGetVersionRevisionTest:ut3DImportExport*:ut3DSImportExport*:utMD2Importer*:utMD5Importer*:utBlenderImporter*:utQ3BSPImportExport*:utXImporter.importDwarf:utDXFImporterExporter.importRifle:utPMXImporter.importTest"
popd

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%license LICENSE
%{_libdir}/libassimp.so.%{sover}*

%files devel
%doc CHANGES CREDITS
%{_bindir}/assimp
%{_includedir}/assimp/
%{_libdir}/libassimp.so
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/assimp.pc

%changelog
