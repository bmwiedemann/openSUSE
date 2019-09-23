#
# spec file for package dhewm3
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


Name:           dhewm3
Version:        1.5.0
Release:        0
Summary:        DOOM 3 source port
License:        GPL-3.0-only
Group:          Amusements/Games/3D/Shoot
Url:            https://github.com/dhewm/dhewm3
Source0:        https://github.com/dhewm/%{name}/archive/%{version}.tar.gz
# upstream bug: https://github.com/dhewm/dhewm3/issues/172
Patch0:         0001-Remove-use-of-date-time-macros.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(sdl2)
BuildRequires:  pkgconfig(libcurl)
# BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)

%description
dhewm3 is a DOOM 3 GPL source port.
Unlike the original DOOM 3, dhewm3 uses:

- SDL for low level OS support, OpenGL and input handling
- OpenAL for audio output, all OS specific audio backends are gone
- OpenAL EFX for EAX reverb effects
- Better support for widescreen (and arbitrary display resolutions)

%prep
%setup -q
%autopatch -p1

%build
cd neo
%cmake ..
%make_jobs

%install
cd neo
%cmake_install

%files
%doc README.md
%license COPYING.txt
%{_bindir}/%{name}
%{_libdir}/%{name}

%changelog
