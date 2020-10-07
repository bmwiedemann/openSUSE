#
# spec file for package Play
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


Name:           Play
Version:        0~git20201003
Release:        0
Summary:        Play! - PlayStation 2 Emulator
License:        MIT
Group:          System/Emulators/Other
URL:            http://purei.org
Source:         %{name}-%{version}.tar.xz
Patch0:         fix-aarch64.patch
BuildRequires:  Mesa-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glu-devel
BuildRequires:  libbz2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libevdev-devel
BuildRequires:  libicu-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  nlohmann_json-devel
BuildRequires:  openal-soft-devel
BuildRequires:  sqlite3-devel
BuildRequires:  zlib-devel

%description
Play! is a PlayStation 2 emulator for Windows, macOS, UNIX, Android & iOS platforms.

This package is for RetroArch/libretro front-end.

%prep
%setup -q
%patch0 -p0

%build
mkdir build
cd build
cmake .. \
        -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
        -DCMAKE_INSTALL_LIBEXEC="%{_libexecdir}" \
        -DCMAKE_BUILD_TYPE="Release" \
        -DCMAKE_SKIP_RPATH="YES"

%cmake_build

%install
%cmake_install

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/1024x1024
%dir %{_datadir}/icons/hicolor/1024x1024/apps
%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
