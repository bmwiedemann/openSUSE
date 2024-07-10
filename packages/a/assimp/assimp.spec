#
# spec file for package assimp
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


%define sover 5
Name:           assimp
Version:        5.4.2
Release:        0
Summary:        Library to load and process 3D scenes from various data formats
License:        BSD-3-Clause AND MIT
Group:          Development/Libraries/C and C++
URL:            https://www.assimp.org/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.22
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
  -DASSIMP_WARNINGS_AS_ERRORS=OFF \
  -DASSIMP_BUILD_ASSIMP_TOOLS=ON

%cmake_build

%install
%cmake_install

find %{buildroot} -type f -name "*.la" -delete -print

%check
# More tests fail on s390x with version 5.4.1, skip %%check
%ifnarch s390x
pushd build
gtest_filter="-"

# utVersion.aiGetVersionRevisionTest passes with git builds only
gtest_filter="${gtest_filter}:utVersion.aiGetVersionRevisionTest"

# the models-nonbsd are not in the tarball, tests depending on it are also excluded
gtest_filter="${gtest_filter}:ut3DImportExport.importMarRifle"
gtest_filter="${gtest_filter}:ut3DImportExport.importMarRifleA"
gtest_filter="${gtest_filter}:ut3DImportExport.importMarRifleD"
gtest_filter="${gtest_filter}:ut3DSImportExport.importCartWheel"
gtest_filter="${gtest_filter}:ut3DSImportExport.importGranate"
gtest_filter="${gtest_filter}:ut3DSImportExport.importJeep1"
gtest_filter="${gtest_filter}:ut3DSImportExport.importMarRifle"
gtest_filter="${gtest_filter}:ut3DSImportExport.importMp5Sil"
gtest_filter="${gtest_filter}:ut3DSImportExport.importPyramob"
gtest_filter="${gtest_filter}:utBlenderImporter.importBob"
gtest_filter="${gtest_filter}:utBlenderImporter.importFleurOptonl"
gtest_filter="${gtest_filter}:utDXFImporterExporter.importRifle"
gtest_filter="${gtest_filter}:utMD2Importer.importDolphin"
gtest_filter="${gtest_filter}:utMD2Importer.importFlag"
gtest_filter="${gtest_filter}:utMD2Importer.importHorse"
gtest_filter="${gtest_filter}:utMD5Importer.importBoarMan"
gtest_filter="${gtest_filter}:utMD5Importer.importBob"
gtest_filter="${gtest_filter}:utPMXImporter.importTest"
gtest_filter="${gtest_filter}:utQ3BSPImportExport.importerTest"
gtest_filter="${gtest_filter}:utXImporter.importDwarf"

%ifnarch x86_64
# tests fail, because they assume you can compare floats
# See https://github.com/assimp/assimp/issues/4438
gtest_filter="${gtest_filter}:AssimpAPITest_aiMatrix3x3.*"
gtest_filter="${gtest_filter}:AssimpAPITest_aiMatrix4x4.*"
gtest_filter="${gtest_filter}:AssimpAPITest_aiQuaternion.*"
gtest_filter="${gtest_filter}:AssimpAPITest_aiVector2D.*"
gtest_filter="${gtest_filter}:AssimpAPITest_aiVector3D.*"
%endif
%endif

./bin/unit --gtest_filter="${gtest_filter}"
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
