#
# spec file for package libretro-play
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


Name:           libretro-play
Version:        0~git20200610
Release:        0
Summary:        Play! libretro core for PlayStation 2 emulation
License:        MIT
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  Mesa-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glu-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libbz2-devel
BuildRequires:  libicu-devel
BuildRequires:  libopenssl-devel
BuildRequires:  nlohmann_json-devel
BuildRequires:  sqlite3-devel
BuildRequires:  zlib-devel

%description
Play! is an attempt to create a PlayStation 2 emulator.

This package is for RetroArch/libretro front-end.

%prep
%setup -q

%build
mkdir build
cd build
cmake .. -DBUILD_LIBRETRO_CORE=yes -DBUILD_PLAY=off -DBUILD_TESTS=no -DENABLE_AMAZON_S3=no -DCMAKE_BUILD_TYPE="Release"
%make_jobs

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp build/Source/ui_libretro/play_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/play_libretro.so

%changelog
