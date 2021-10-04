#
# spec file for package dosbox
#
# Copyright (c) 2021 SUSE LLC
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
Version:        0.77.1
Release:        0
Summary:        A modernized DOSBox to run old DOS games
License:        GPL-2.0-or-later
URL:            https://%{name}-staging.github.io
Source0:        https://github.com/%{name}-staging/%{name}-staging/archive/v%{version}.tar.gz#/%{name}-staging-%{version}.tar.gz
Patch0:         %{name}-staging-0.77.1-config.patch
Patch1:         %{name}-staging-0.77.1-name.patch
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.54.2
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-translations = %{version}
Recommends:     fluid-soundfont-gm
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
BuildRequires:  pkgconfig(fluidsynth) >= 2.0
BuildRequires:  pkgconfig(mt32emu)
%endif

%description
%{name}-staging is DOS/x86 emulator focusing on ease of use.
Based on DOSBox, it is a fork which use modern library (e.g.: sdl2) and
practice in an attempt to revitalize the development process.
DOSBox Staging is an attempt to revitalize DOSBox's development process.
It's not a rewrite, but a continuation and improvement on the existing
DOSBox codebase while leveraging modern development tools and practices.
Added support: Opus, FLAC, MT32, GM, GUS, Raw mouse input and more.
https://github.com/dosbox-staging/dosbox-staging#readme

%package translations
Summary:        Translations for %{name}-staging
Requires:       %{name} = %{version}
BuildArch:      noarch

%description translations
This package contains translations for %{name}-staging.

%prep
%autosetup -p1 -n %{name}-staging-%{version}
%if "%{?_lib}" == "lib" || (0%{?suse_version} < 1550 && 0%{?sle_version} < 150400)
sed -i 's/.*soft_limit.*//' tests/meson.build
%endif

%build
%meson \
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150400
-Duse_fluidsynth=false -Duse_mt32emu=false
%endif
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/%{name}/translations
install -pm0644 contrib/translations/??/*.lng %{buildroot}%{_datadir}/%{name}/translations

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

%files translations
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/*.lng

%changelog
