#
# spec file for package libGLC
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


Name:           libGLC
Version:        0.7.2
Release:        0
Summary:        Free OpenGL Character Renderer
License:        LGPL-2.1-or-later
URL:            http://quesoglc.sf.net/
Source:         http://sourceforge.net/projects/quesoglc/files/%{version}/quesoglc-%{version}.tar.bz2
Patch1:         quesoglc-typepun.diff
BuildRequires:  Mesa-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(ice)

%description
QuesoGLC is a free (as in free speech) implementation of the OpenGL
Character Renderer (GLC). QuesoGLC is based on the FreeType library,
provides Unicode support and is designed to be easily ported to any
platform that supports both FreeType and the OpenGL API.

%package -n libGLC0
Summary:        Free OpenGL Character Renderer

%description -n libGLC0
QuesoGLC is a free (as in free speech) implementation of the OpenGL
Character Renderer (GLC). QuesoGLC is based on the FreeType library,
provides Unicode support and is designed to be easily ported to any
platform that supports both FreeType and the OpenGL API.

%package devel
Summary:        QuesoGLC Development Files
Requires:       Mesa-devel
Requires:       libGLC0 = %{version}
Requires:       pkgconfig(expat)
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(zlib)

%description devel
This package contains all necessary include files and libraries needed
to develop applications using QuesoGLC.

%prep
%autosetup -n quesoglc-%{version} -p1

%build
export CFLAGS="%{optflags} -Wno-incompatible-pointer-types"
%configure \
  --disable-static
%make_build

%ldconfig_scriptlets -n libGLC0

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%files -n libGLC0
%license COPYING
%doc AUTHORS ChangeLog README THANKS
%{_libdir}/libGLC.so.*

%files devel
%{_includedir}/*
%{_libdir}/libGLC.so
%{_libdir}/pkgconfig/quesoglc.pc

%changelog
