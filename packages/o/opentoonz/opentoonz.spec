#
# spec file for package opentoonz
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


Name:           opentoonz
Version:        1.4.0
Release:        0
Summary:        2D animation software
# need to review license as site indicates: "modified BSD license"
License:        BSD-2-Clause
Group:          Productivity/Graphics/Other
URL:            https://opentoonz.github.io/e/
Source0:        %{name}-%{version}.tar.xz
Source3:        %{name}-rpmlintrc
Patch0:         p_handle-no-return-in-nonvoid-function.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Fix-linker-errors-on-Linux.patch
# PATCH-FIX-OPENSUSE -- Use the system mypaint brushes
Patch2:         0001-Use-the-system-mypaint-brushes.patch
# PATCH-FIX-UPSTREAM
Patch3:         0001-Fix-build-with-GCC-10.patch
# PATCH-FIX-UPSTREAM
Patch4:         0001-Fix-build-with-Qt-5.15.patch
# PATCH-FIX-UPSTREAM
Patch5:         0001-System-depend-code-deduplication.patch
BuildRequires:  boost-devel >= 1.55
BuildRequires:  cmake
BuildRequires:  freeglut-devel
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
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libmypaint)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  i586 x86_64
# the package is called mypaint-brushes1 in the devel project,
# but mypaint-brushes in the Leap:15.2 repo.
%if 0%{?sle_version} == 150200
Requires:       mypaint-brushes < 2.0
%else
Requires:       mypaint-brushes1
%endif

%description
2D animation software previously known as Toonz.

%prep
%autosetup -p1

# Remove all thirdparty except tiff which is patched.
find thirdparty/* -maxdepth 0 ! -name "tiff-*" ! -name "lzo" ! -name "kiss_fft*" -type d -exec rm -r "{}" \;
# Keep thirdparty/lzo/driver, but remove library.
rm -r thirdparty/lzo/2.*

# Use the mypaint brushes instead of the local copy
rm -fr stuff/library/mypaint\ brushes

%build

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
