#
# spec file for package brux-gdk
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025, Martin Hauke <mardnh@gmx.de>
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


Name:           brux-gdk
Version:        0.2.11+git20250218
Release:        0
Summary:        A runtime and development kit using SDL and Squirrel
License:        AGPL-3.0-only
Group:          Development/Languages/Other
URL:            https://github.com/KelvinShadewing/brux-gdk
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  squirrel-devel
BuildRequires:  pkgconfig(SDL2_gfx)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(sdl2)

%description
Brux (formerly XYG) is a cross-platform, runtime-based game
development kit using the Squirrel language. It allows for games to
be written by hand in a text editor or made in an IDE similar to Game
Maker, and allows games to be ported with little to no modification
to the code, offering a "build once, run everywhere" development
process.

%prep
%autosetup

%build
cd rte
%cmake \
  -DBUILD_STATIC_LIBS=OFF \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
install -Dpm 0755 rte/build/brux %{buildroot}%{_bindir}/brux

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/brux

%changelog
