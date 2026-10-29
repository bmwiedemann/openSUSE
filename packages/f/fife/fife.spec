#
# spec file for package fife
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2011 Nelson Marques <nmarques@opensuse.org>
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


%define sover 0_4_2
%define oname fifengine
Name:           fife
Version:        0.4.3
Release:        0
Summary:        The Flexible Isometric Free Engine, a 2D game engine
License:        LGPL-2.1-or-later
URL:            https://www.fifengine.de
Source:         https://github.com/fifengine/fifengine/archive/%{version}/%{oname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fife-boost_1_85.patch -- https://github.com/fifengine/fifengine/issues/1085
Patch0:         fife-boost_1_85.patch
# PATCH-FIX-OPENSUSE fife-cmake-cmp0078.patch -- keep legacy
# swig_add_library target names (_fife, _fifechan): CMP0078 NEW (default
# since this release raised cmake_minimum_required to 3.15) names the
# module target <name>, which collides with the core add_library(fife)
# and breaks install(TARGETS _fife)
Patch1:         fife-cmake-cmp0078.patch
BuildRequires:  cmake
BuildRequires:  fifechan-devel
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  swig
BuildRequires:  tinyxml-devel
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1330
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_regex-devel
%if 0%{?suse_version} < 1600
BuildRequires:  libboost_system-devel
%endif
%else
BuildRequires:  boost-devel
%endif

%description
FIFE stands for Flexible Isometric Free Engine and is a cross platform
game creation framework. It provides the ability to create a
game using Python interfaces.

%package -n libfife%{sover}
Summary:        The Flexible Isometric Free Engine, a 2D game engine

%description -n libfife%{sover}
FIFE stands for Flexible Isometric Free Engine and is a cross platform
game creation framework. It provides the ability to create a
game using Python interfaces.

%package -n python3-%{name}
Summary:        Python 3 extensions for the FIFE engine
Requires:       python3

%description -n python3-%{name}
FIFE stands for Flexible Isometric Free Engine and is a cross platform
game creation framework. It provides the ability to create a
game using Python interfaces.

%package devel
Summary:        Development files for the FIFE 2D game engine
Requires:       libfife%{sover} = %{version}
Requires:       python3-fife = %{version}

%description devel
FIFE stands for Flexible Isometric Free Engine and is a cross platform
game creation framework. It provides the ability to create a
game using Python interfaces.

%prep
%setup -q -n %{oname}-%{version}
%patch -P 0 -p1
%patch -P 1 -p1

%build
%define __builddir py3
# renderbackendopengl.cpp uses legacy fixed-function entry points
# (glColorPointer/glTexCoordPointer), only in libGL, not libOpenGL
%cmake \
    -DOpenGL_GL_PREFERENCE=LEGACY \
    -Dbuild-library=ON \
    -Drend-camzone=ON \
    -Drend-grid=ON \
    -Dlibrocket=ON \
    -Dbuild-python=ON \
    -DPYTHON_SITE_PACKAGES=%{python3_sitearch} \
    -DCMAKE_CXX_FLAGS='-DUSE_BOOST_FILESYSTEM_V3'
%make_build
cd ..

%install
%define __builddir py3
%cmake_install

# Blocked by https://github.com/fifengine/fifengine/issues/879
# %%check
# export PYTHONPATH="%%{buildroot}%%{python3_sitearch}"
# python3 ./run_tests.py -a

%post -n libfife%{sover} -p /sbin/ldconfig
%postun -n libfife%{sover} -p /sbin/ldconfig

%files -n libfife%{sover}
%if ( 0%{?suse_version} == 1315 && 0%{?sle_version} == 120100 ) || ! 0%{?is_opensuse}
# Leap 42.1 or SLE
%license LICENSE.md
%doc AUTHORS
%else
%license LICENSE.md AUTHORS
%endif
%{_libdir}/*.so.*

%files -n python3-%{name}
# Only the fife dir is installed (no egg-info/dist-info); an extra
# files glob matching nothing would fail the build
%{python3_sitearch}/fife

%files devel
%doc CHANGELOG.md README.md
%{_includedir}/fife/
%{_libdir}/*.so

%changelog
