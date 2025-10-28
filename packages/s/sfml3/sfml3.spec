#
# spec file for package sfml3
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
%define so_ver -3_0
Name: sfml3
Version: 3.0.2
Summary: SFML is a simple, fast, cross-platform and object-oriented multimedia API.
Release: 0
Source0: https://github.com/SFML/SFML/archive/refs/tags/3.0.2.tar.gz
License: Zlib
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: fdupes
BuildRequires: gcc-c++ >= 9
BuildRequires: libXi-devel
BuildRequires: pkgconfig
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(vorbisenc)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(pthread-stubs)

%description
SFML is a simple, fast, cross-platform and object-oriented multimedia API.
It provides access to windowing, graphics, audio and network.
It is written in C++, and has bindings for various languages such as C, .Net, Ruby, Python.

%package -n lib%{name}%{so_ver}
Summary:        Free multimedia C++ API
Group:          System/Libraries

%description -n lib%{name}%{so_ver}
SFML is a multimedia API that provides access to graphics, input,
audio, etc., and may be seen as an object-oriented alternative to
SDL. It can be used as a minimal windowing system to interface with
OpenGL, or as a multimedia library for building games and interactive
programs.

%package devel
Summary:        SFML development files
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{so_ver} = %{version}
Requires:       pkgconfig(gl)
# Conflict with other SFML versions (same include files)
Conflicts: sfml-devel
Conflicts: sfml2-devel

%description devel
SFML is a C++ multimedia API that provides a low and high-level
access to graphics, input, audio, etc., and may be seen as an
object-oriented alternative to SDL. SFML can be used as a minimal
windowing system to interface with OpenGL, or as a multimedia library
for building games or interactive programs.

This subpackage provides the header files needed to build SFML
programs.

%prep
%setup -q -n SFML-%{version}

%build
%cmake -DSFML_INSTALL_PKGCONFIG_FILES=TRUE \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{so_ver} -p /sbin/ldconfig
%postun -n lib%{name}%{so_ver} -p /sbin/ldconfig

%files -n lib%{name}%{so_ver}
%license license.md
%{_libdir}/libsfml-*.so.*

%files devel
%{_includedir}/SFML
%{_libdir}/libsfml-*.so
%{_libdir}/pkgconfig/sfml-*.pc
%{_libdir}/cmake/SFML
%{_docdir}/*

%changelog
