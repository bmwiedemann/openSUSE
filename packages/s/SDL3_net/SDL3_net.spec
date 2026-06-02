#
# spec file for package SDL3_net
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


%define lname	libSDL3_net0
Name:           SDL3_net
Version:        3.2.0
Release:        0
Summary:        SDL3 networking library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://github.com/libsdl-org/SDL_net
Source:         https://www.libsdl.org/projects/SDL_net/release/%name-%version.tar.gz
Source2:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(sdl3)

%description
This is a networking library for use with SDL.

%package -n %lname
Summary:        Simple DirectMedia Layer 3 – Networking library
Group:          System/Libraries
Provides:       SDL3_net = %version

%description -n %lname
This is a networking library for use with SDL.

%package devel
Summary:        Development files for the SDL3 networking library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release
Obsoletes:      libSDL3_net-devel < %version-%release
Provides:       libSDL3_net-devel = %version-%release

%description devel
This is a networking library for use with SDL.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# we have a %%license file entry already
rm -Rf "%buildroot/usr/share/licenses"

%ldconfig_scriptlets -n %lname

%files -n %lname
%license LICENSE.txt
%_libdir/libSDL3_net.so.*

%files devel
%doc README.md
%_includedir/SDL3_net/
%_libdir/libSDL3_net.so
%_libdir/pkgconfig/sdl3-net.pc
%_libdir/cmake/

%changelog
