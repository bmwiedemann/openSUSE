#
# spec file for package opentoonz
#
# Copyright (c) 2025 SUSE LLC
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


Name:           opentoonz
Version:        1.7.1
Release:        0
Summary:        2D animation software
License:        BSD-2-Clause
Group:          Productivity/Graphics/Other
URL:            https://opentoonz.github.io/e/
Source0:        %{name}-%{version}.tar.xz
Source99:       %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-linker-errors-on-Linux.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Fix-build-with-Werror-return-type.patch
# Use system libraries when possible
Patch2:         0001-Use-system-stdfx.patch
# PATCH-FIX-OPENSUSE
Patch3:         opentoonz-glew_config_compat.patch
# PATCH-FIX-UPSTREAM -- Use system TIFF
Patch4:         0001-Use-system-TIFF.patch
# PATCH-FIX-UPSTREAM
Patch6:         opentoonz-cmake4.patch
BuildRequires:  boost-devel >= 1.55
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  openblas-devel
BuildRequires:  pkgconfig
# needed to setup startup script paths
BuildRequires:  sed
BuildRequires:  superlu-devel
BuildRequires:  cmake(OpenCV)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5SerialPort)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(kissfft)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmypaint)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(mypaint-brushes-1.0) >= 1.3
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
Requires:       mypaint-brushes1
# build fails on ARM (conflicting declaration between glew and gles)
ExclusiveArch:  %{ix86} x86_64 ppc64 ppc64le %{riscv}

%description
2D animation software previously known as Toonz.

%prep
%autosetup -p1

%build
# NOTE: Most third party dependencies are dropped from the tarball. Only tinyexr
# and lzodriver are kept

cd toonz
%define __sourcedir sources

# FIXME: -DCMAKE_POLICY_VERSION_MINIMUM=3.5 is temporarily needed until dependencies build with cmake 4 (e.g. kissfft)
%cmake \
  -DCMAKE_SKIP_RPATH:BOOL=ON \
  -DWITH_SYSTEM_LZO:BOOL=ON \
  -DWITH_SYSTEM_SUPERLU:BOOL=ON \
  -DWITH_TRANSLATION:BOOL=OFF \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%cmake_build

%install
cd toonz
%cmake_install

# fix library dir
%if "%{_lib}" != "lib"
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_prefix}/lib/%{name}/* %{buildroot}%{_libdir}/%{name}
rm -r %{buildroot}%{_prefix}/lib/%{name}

# fix launch script that hardcodes 'lib'
sed -i 's|/lib/|/%{_lib}/|' %{buildroot}%{_bindir}/%{name}
%endif

%files
%license LICENSE.txt
%dir %{_datadir}/metainfo
%{_bindir}/lzocompress
%{_bindir}/lzodecompress
%{_bindir}/OpenToonz
%{_bindir}/opentoonz
%{_bindir}/tcleanup
%{_bindir}/tcomposer
%{_bindir}/tconverter
%{_bindir}/tfarmcontroller
%{_bindir}/tfarmserver
%{_datadir}/applications/io.github.OpenToonz.desktop
%{_datadir}/icons/hicolor/256x256/apps/io.github.OpenToonz.png
%{_datadir}/metainfo/io.github.OpenToonz.appdata.xml
%{_datadir}/opentoonz/
%{_libdir}/opentoonz/

%changelog
