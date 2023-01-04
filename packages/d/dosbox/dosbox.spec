#
# spec file for package dosbox
#
# Copyright (c) 2023 SUSE LLC
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


Name:           dosbox
Version:        0.80.0
Release:        0
Summary:        DOS/x86 emulator to run old DOS games
License:        GPL-2.0-or-later
URL:            https://%{name}-staging.github.io
Source0:        https://github.com/%{name}-staging/%{name}-staging/archive/v%{version}.tar.gz#/%{name}-staging-%{version}.tar.gz
Patch0:         %{name}-staging-0.80.0-config.patch
Patch1:         %{name}-staging-0.80.0-name.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fluidsynth) >= 2.3.0
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(iir)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(mt32emu)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(slirp) >= 4.7.0
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(zlib)
Recommends:     fluid-soundfont-gm
Provides:       %{name}-translations = %{version}
Obsoletes:      %{name}-translations < %{version}

%description
%{name}-staging is DOS/x86 emulator focusing on ease of use.
Based on DOSBox, it is a fork which use modern library (e.g.: sdl2) and
practice in an attempt to revitalize the development process.
DOSBox Staging is an attempt to revitalize DOSBox's development process.
It's not a rewrite, but a continuation and improvement on the existing
DOSBox codebase while leveraging modern development tools and practices.
Added support: Opus, FLAC, MT32, GM, GUS, Raw mouse input and more.
https://github.com/dosbox-staging/dosbox-staging#readme

%prep
%autosetup -p1 -n %{name}-staging-%{version}

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}

%check
%meson_test

%files
%license COPYING
%doc AUTHORS README README.md docs/README.video THANKS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.{png,svg}
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/%{name}

%changelog
