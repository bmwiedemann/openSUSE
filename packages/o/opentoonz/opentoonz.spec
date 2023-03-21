#
# spec file for package opentoonz
#
# Copyright (c) 2022 SUSE LLC
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
Version:        1.6.0
Release:        0
Summary:        2D animation software
License:        BSD-2-Clause
Group:          Productivity/Graphics/Other
URL:            https://opentoonz.github.io/e/
Source0:        %{name}-%{version}.tar.xz
Source99:       %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-linker-errors-on-Linux.patch
# PATCH-FIX-OPENSUSE -- Use the system mypaint brushes
Patch1:         0001-Use-the-system-mypaint-brushes.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Clarify-size_t-origin-for-tgc-hash-BucketNode.patch
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
BuildRequires:  update-desktop-files
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
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
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
# NOTE: Third party dependencies are dropped from the tarball thanks to the
# _service file. Only kissfft130, lzo/driver and tiff-4.0.3 shall be kept.

# TODO upstream planning to replace custom thirdparty libs with system versions
cd thirdparty/tiff-*
export CFLAGS="%{optflags} -fPIC"
%configure --disable-jbig
%make_build
cd -

cd toonz
%define __sourcedir sources
%cmake \
  -DCMAKE_SKIP_RPATH=TRUE \
  -DWITH_SYSTEM_LZO=TRUE \
  -DWITH_SYSTEM_SUPERLU=TRUE

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

%suse_update_desktop_file io.github.OpenToonz 2DGraphics

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
