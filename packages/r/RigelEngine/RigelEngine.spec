#
# spec file for package RigelEngine
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019-2022, Martin Hauke <mardnh@gmx.de>
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


Name:           RigelEngine
Version:        0.9.1
Release:        0
Summary:        A modern reimplementation of the game Duke Nukem II
License:        GPL-2.0-only
Group:          Amusements/Games/Action/Arcade
URL:            https://github.com/lethal-guitar/RigelEngine
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.12
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(sdl2)
%if 0%{?sle_version} >= 150100 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc9
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif

%description
A modern reimplementation of the game Duke Nukem II, originally released in
1993 for MS-DOS by Apogee Software.

You need the original game's data files in order to play, e.g. the freely
available shareware version.

%prep
%setup -q

%build
%if 0%{?sle_version} >= 150100 && 0%{?is_opensuse}
export CC="gcc-9"
export CXX="g++-9"
%endif
%cmake -DBUILD_TESTS=ON \
 -DBUILD_MODDING_TOOLS=ON \
%ifarch %arm aarch64
 -DUSE_GL_ES=1 \
%endif

%make_jobs

%install
install -D -m0755 build/src/RigelEngine %{buildroot}%{_bindir}/RigelEngine

%check
%ctest

%files
%license LICENSE.md
%license AUTHORS.md README.md
%{_bindir}/RigelEngine

%changelog
