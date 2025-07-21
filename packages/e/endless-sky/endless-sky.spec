#
# spec file for package endless-sky
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%if 0%{?sle_version} && 0%{?sle_version} < 160000
%define force_gcc_version 13
%endif
%define lname   io.github.endless_sky.endless_sky
Name:           endless-sky
Version:        0.10.14
Release:        0
Summary:        Space exploration, trading, and combat game
License:        CC-BY-3.0 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND GPL-3.0-only
Group:          Amusements/Games/Action/Arcade
URL:            https://endless-sky.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE endless-sky-fix-data-path.patch -- Fix installation path of data
Patch0:         endless-sky-fix-data-path.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
%if 0%{?suse_version} < 1600
BuildRequires:  gcc%{?force_gcc_version}
BuildRequires:  gcc%{?force_gcc_version}-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  Catch2-devel
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg8-devel
BuildRequires:  libmad-devel
BuildRequires:  libuuid-devel
BuildRequires:  minizip-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)

%description
Explore other star systems. Earn money by trading, carrying passengers,
or completing missions. Use your earnings to buy a better ship or to
upgrade the weapons and engines on your current one. Blow up pirates.
Take sides in a civil war. Or leave human space behind and hope to
find some friendly aliens whose culture is more civilized than your own...

%prep
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CXXFLAGS="%{optflags} -fvisibility=hidden -fvisibility-inlines-hidden"
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%else
export CXXFLAGS="%{optflags} -fvisibility=hidden -fvisibility-inlines-hidden -Wno-error=dangling-reference"
%endif
%autosetup -p1
cmake --preset linux

%build
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CXXFLAGS="%{optflags} -fvisibility=hidden -fvisibility-inlines-hidden"
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%else
export CXXFLAGS="%{optflags} -fvisibility=hidden -fvisibility-inlines-hidden -Wno-error=dangling-reference"
%endif
export CFLAGS="%{optflags} -fvisibility=hidden"
cmake --build --preset linux-release --target EndlessSky

%install
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CXXFLAGS="%{optflags} -fvisibility=hidden -fvisibility-inlines-hidden"
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%else
export CXXFLAGS="%{optflags} -fvisibility=hidden -fvisibility-inlines-hidden -Wno-error=dangling-reference"
%endif
export CFLAGS="%{optflags} -fvisibility=hidden"
cmake --install build/linux --prefix %{buildroot}%{_prefix} --strip

%fdupes %{buildroot}

%files
%license license.txt
%doc README.md changelog copyright
%{_bindir}/endless-sky
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{lname}.desktop
%{_mandir}/man6/*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{lname}.appdata.xml

%changelog
