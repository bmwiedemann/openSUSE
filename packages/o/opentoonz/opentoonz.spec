#
# spec file for package opentoonz
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global __requires_exclude ^(libcolorfx|libimage|libsound|libtif).*
%global __provides_exclude ^(libcolorfx|libimage|libsound|libtif).*
Name:           opentoonz
Version:        1.3.0
Release:        0
Summary:        2D animation software
# need to review license as site indicates: "modified BSD license"
License:        BSD-2-Clause
Group:          Productivity/Graphics/Other
URL:            https://opentoonz.github.io/e/
Source0:        %{name}-v%{version}.tar.xz
Source3:        %{name}-rpmlintrc
Patch1:         p_handle-no-return-in-nonvoid-function.patch
Patch2:         p_add-zlo-to-cmake-include-path-suffixes.patch
Patch3:         Fix-build-with-Qt-5_13.patch
BuildRequires:  boost-devel >= 1.55
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libusb-devel
BuildRequires:  openblas-devel
BuildRequires:  pkgconfig
# needed to setup startup script paths
BuildRequires:  sed
BuildRequires:  superlu-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(freeglut)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libmypaint)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  i586 x86_64

%description
2D animation software previously known as Toonz.

%prep
%autosetup -p1 -n %{name}-v%{version}

# Remove all thirdparty except tiff which is patched.
find thirdparty/* -maxdepth 0 ! -name "tiff-*" ! -name "lzo" ! -name "kiss_fft*" -type d -exec rm -r "{}" \;
# Keep thirdparty/lzo/driver, but remove library.
rm -r thirdparty/lzo/2.*

%build
# TODO upstream planning to replace custom thirdparty libs with system versions
cd thirdparty/tiff-*
export CFLAGS="%{optflags} -fPIC"
%configure
%make_build
cd -

cd toonz
%define __sourcedir sources
%cmake \
  -DCMAKE_EXE_LINKER_FLAGS="-Wl,--no-as-needed" \
  -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--no-as-needed" \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--no-as-needed"

%make_jobs

%install
cd toonz
%cmake_install

# fix lib dir since install puts 64bit libs in /usr/lib/
%ifarch x86_64
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_prefix}/lib/%{name}/* %{buildroot}%{_libdir}/%{name}
rm -r %{buildroot}%{_prefix}/lib/%{name}

# fix launch script that references lib/ instead of lib64/.
sed -i 's|/lib/|/lib64/|' %{buildroot}%{_bindir}/%{name}
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
