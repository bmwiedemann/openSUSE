#
# spec file for package sfml3
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define so_ver -3_1
Name:           sfml3
Version:        3.1.0
Release:        0
Summary:        SFML is a simple, fast, cross-platform and object-oriented multimedia API.
License:        Zlib
Source0:        https://github.com/SFML/SFML/archive/refs/tags/3.1.0.tar.gz
# No system package, vendored like upstream's git FetchContent (offline build):
# https://github.com/Tehreer/SheenBidi/archive/refs/tags/v3.0.0.tar.gz
Source1:        SheenBidi-3.0.0.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 9
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mbedtls)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(pthread-stubs)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)

%description
SFML is a simple, fast, cross-platform and object-oriented multimedia API.
It provides access to windowing, graphics, audio and network.
It is written in C++, and has bindings for various languages such as C, .Net, Ruby, Python.

%package -n lib%{name}%{so_ver}
Summary:        Free multimedia C++ API

%description -n lib%{name}%{so_ver}
SFML is a multimedia API that provides access to graphics, input,
audio, etc., and may be seen as an object-oriented alternative to
SDL. It can be used as a minimal windowing system to interface with
OpenGL, or as a multimedia library for building games and interactive
programs.

%package devel
Summary:        SFML development files
Requires:       lib%{name}%{so_ver} = %{version}
Requires:       pkgconfig(gl)
# Conflict with other SFML versions (same include files)
Conflicts:      sfml-devel
Conflicts:      pkgconfig(sfml-all)
Conflicts:      pkgconfig(sfml-audio)
Conflicts:      pkgconfig(sfml-graphics)
Conflicts:      pkgconfig(sfml-network)
Conflicts:      pkgconfig(sfml-system)
Conflicts:      pkgconfig(sfml-window)

%description devel
SFML is a C++ multimedia API that provides a low and high-level
access to graphics, input, audio, etc., and may be seen as an
object-oriented alternative to SDL. SFML can be used as a minimal
windowing system to interface with OpenGL, or as a multimedia library
for building games or interactive programs.

This subpackage provides the header files needed to build SFML
programs.

%prep
%setup -q -n SFML-%{version} -a 1
# Apply upstream tools/sheenbidi/PatchSheenBidi.cmake by hand, its
# FetchContent PATCH_COMMAND is skipped for a local source dir, and drop
# its install rules (everything below "Install Configuration") so the
# vendored copy installs nothing
sed -i -e 's/^add_library(SheenBidi$/add_library(SheenBidi OBJECT/' -e '/^# Install Configuration/,$d' SheenBidi-3.0.0/CMakeLists.txt

%build
%cmake -DSFML_INSTALL_PKGCONFIG_FILES=TRUE \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DFETCHCONTENT_SOURCE_DIR_SHEENBIDI:PATH=%{_builddir}/SFML-%{version}/SheenBidi-3.0.0
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n lib%{name}%{so_ver}

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
