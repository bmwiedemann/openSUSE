#
# spec file for package SDL3_ttf
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


Name:           SDL3_ttf
%define lname	libSDL3_ttf0
Version:        3.1.2
Release:        0
Summary:        Simple DirectMedia Layer Truetype library
License:        Zlib
Group:          Development/Libraries/X11
URL:            https://github.com/libsdl-org/SDL_ttf
Source:         https://github.com/libsdl-org/SDL_ttf/releases/download/prerelease-%version/SDL3_ttf-%version.tar.gz
Source2:        https://github.com/libsdl-org/SDL_ttf/releases/download/prerelease-%version/SDL3_ttf-%version.tar.gz.sig
Source9:        %name.keyring
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sdl3)

%description
This is a library that allows using TrueType fonts in SDL applications.

%package -n %lname
Summary:        Simple DirectMedia Layer Truetype library
Group:          System/Libraries

%description -n %lname
This is a library that allows using TrueType fonts in SDL applications.

%package devel
Summary:        Header files for the Simple DirectMedia Layer Truetype library
Group:          Development/Libraries/X11
Requires:       %lname = %version

%description devel
This is a library that allows using TrueType fonts in SDL applications.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
rm -Rf "%buildroot/%_datadir/licenses"

%ldconfig_scriptlets -n %lname

%files -n %lname
%license LICENSE.txt
%_libdir/libSDL3_ttf.so.*

%files devel
%_includedir/SDL*
%_libdir/cmake/
%_libdir/pkgconfig/*.pc
%_libdir/libSDL3_ttf.so

%changelog
