#
# spec file for package Coin
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


%define soname 80
%bcond_with docs

Name:           Coin4
Version:        4.0.3
Release:        0
Summary:        Scene-graph based retain-mode 3D graphics library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/coin3d/coin/wiki
Source0:        https://github.com/coin3d/coin/releases/download/v%{version}/coin-%{version}-src.tar.gz
# PATCH-FIX-OPENSUSE -- direct GLX usage causes problems on Wayland (taken from Fedora)
Patch2:         coin-no_glx.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  openal-soft-devel
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)

%description
Coin is a scene-graph based, retain-mode, rendering and model
manipulation C++ class library that uses OpenGL for its 3D graphics.
Coin is compatible to Open Inventor 2.1 and also has support for 3D
sound, GLSL shaders, and additional file formats like VRML97.

%package devel
Summary:        Development files for Coin, a 3D graphics library
Group:          Development/Libraries/C and C++
Requires:       fontconfig-devel
Requires:       freetype2-devel
Requires:       libCoin%{soname} = %{version}
Requires:       openal-soft-devel
Requires:       zlib-devel
Requires:       pkgconfig(bzip2)
Requires:       pkgconfig(dri)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Conflicts:      Coin-devel < 4.0.0

%description devel
Coin is a scene-graph based, retain-mode, rendering and model
manipulation C++ class library that uses OpenGL for its 3D graphics.
Coin is compatible to Open Inventor 2.1 and also has support for 3D
sound, GLSL shaders, and additional file formats like VRML97.

This subpackage contains libraries and header files for developing
applications that want to make use of Coin.

%package devel-doc
Summary:        Development documentation for Coin
Group:          Documentation/HTML

%description devel-doc
Coin is a scene-graph based, retain-mode, rendering and model
manipulation C++ class library.

This package contains the API and other development documentation.

%package -n libCoin%{soname}
Summary:        Scene-graph based retain-mode 3D graphics library
Group:          System/Libraries

%description -n libCoin%{soname}
Coin is a scene-graph based, retain-mode, rendering and model
manipulation C++ class library that uses OpenGL for its 3D graphics.
Coin is compatible to Open Inventor 2.1 and also has support for 3D
sound, GLSL shaders, and additional file formats like VRML97.

%prep
%setup -q -n coin
%autopatch -p1
sed -i '/^#include <Inventor\/C\/basic.h>$/i #include <Inventor/C/errors/debugerror.h>' include/Inventor/SbBasic.h

%build
# DATADIR must be relative to _prefix, and the "4" is added automatically
# default __builddir clashes with existing "build" dir
%global __builddir my_build
%cmake \
    -DCMAKE_INSTALL_DOCDIR=%{_docdir}/Coin \
    -DCMAKE_INSTALL_DATADIR=share/Coin \
    -DHAVE_MULTIPLE_VERSION:BOOL=ON \
    -DCOIN_BUILD_SHARED_LIBS:BOOL=ON \
    -DCOIN_BUILD_TESTS:BOOL=ON \
    %{?with_docs:-DCOIN_BUILD_DOCUMENTATION:BOOL=ON} \
    %{!?with_docs:-DCOIN_BUILD_DOCUMENTATION:BOOL=OFF} \
    -DCOIN_THREADSAFE:BOOL=ON \
    -DUSE_EXTERNAL_EXPAT:BOOL=ON \
    -DFONTCONFIG_RUNTIME_LINKING:BOOL=OFF \
    -DFREETYPE_RUNTIME_LINKING:BOOL=OFF \
    -DLIBBZIP2_RUNTIME_LINKING:BOOL=OFF \
    -DOPENAL_RUNTIME_LINKING:BOOL=OFF \
    -DSIMAGE_RUNTIME_LINKING:BOOL=OFF \
    -DZLIB_RUNTIME_LINKING:BOOL=OFF \
    -DGLU_RUNTIME_LINKING:BOOL=OFF \
    %{nil}
%cmake_build

%install
%cmake_install

# Remove disfunct coin-config (missing *.cfg file)
rm %{buildroot}%{_bindir}/coin-config

# Remove build configuration
rm -Rf %{buildroot}%{_datadir}/Coin/conf

%fdupes %{buildroot}/%{_prefix}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%post -n libCoin%{soname} -p /sbin/ldconfig
%postun -n libCoin%{soname} -p /sbin/ldconfig

%files -n libCoin%{soname}
%license COPYING
%{_datadir}/%{name}
%{_libdir}/libCoin.so.%{soname}*

%files devel
%doc AUTHORS ChangeLog FAQ NEWS README.md RELNOTES THANKS
%license COPYING FAQ.legal
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/Inventor/
%{_includedir}/%{name}/SoDebug.h
%{_includedir}/%{name}/SoWinEnterScope.h
%{_includedir}/%{name}/SoWinLeaveScope.h
%{_libdir}/pkgconfig/Coin.pc
%{_libdir}/cmake/Coin*
%{_libdir}/libCoin.so

%if %{with docs}
%files devel-doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html
%endif

%changelog
