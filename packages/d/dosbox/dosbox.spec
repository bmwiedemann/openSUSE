#
# spec file for package dosbox
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


%define __builder ninja
Name:           dosbox
Version:        0.83.1
Release:        0
Summary:        DOS/x86 emulator to run old DOS games
License:        GPL-2.0-or-later
URL:            https://%{name}-staging.github.io
Source0:        https://github.com/%{name}-staging/%{name}-staging/archive/v%{version}.tar.gz#/%{name}-staging-%{version}.tar.gz
Patch0:         %{name}-staging-config.patch
Patch1:         %{name}-staging-name.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  cmake(FluidSynth) >= 2.6.2
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(MT32Emu)
BuildRequires:  cmake(SDL2)
BuildRequires:  cmake(iir)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(asio)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(slirp)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(zlib-ng)
Recommends:     fluid-soundfont-gm
Recommends:     libslirp0
ExclusiveArch:  x86_64 aarch64

%description
%{name}-staging is a DOS/x86 emulator focusing on ease of use.
Based on DOSBox, it is a fork which uses modern libraries (e.g.: SDL2) and
practices in an attempt to revitalize the development process.
DOSBox Staging is an attempt to revitalize DOSBox's development process.
It's not a rewrite, but a continuation and improvement on the existing
DOSBox codebase while leveraging modern development tools and practices.
Added support: Opus, FLAC, MT32, GM, GUS, Raw mouse input and more.
https://github.com/dosbox-staging/dosbox-staging#readme

%prep
%autosetup -p1 -n %{name}-staging-%{version}

%build
export CMAKE_GENERATOR="Ninja"
%cmake -LA \
      -DCMAKE_SKIP_INSTALL_RPATH=ON \
      -DUSE_SYSTEM_LIBS=ON
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.{png,svg}
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/%{name}

%changelog
