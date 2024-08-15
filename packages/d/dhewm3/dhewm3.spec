#
# spec file for package dhewm3
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1.5.4
Release:        0
Summary:        DOOM 3 source port
License:        GPL-3.0-only
URL:            https://dhewm3.org/
Source0:        https://github.com/dhewm/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(sdl2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openal)
Provides:       bundled(miniz)

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
%cmake -DREPRODUCIBLE_BUILD=ON ..
%make_jobs

%install
cd neo
%cmake_install

cd ..
install -Dpm 644 dist/linux/share/metainfo/org.dhewm3.Dhewm3.metainfo.xml %{buildroot}/%{_datadir}/metainfo/org.dhewm3.Dhewm3.metainfo.xml
install -Dpm 644 dist/linux/share/icons/hicolor/128x128/apps/org.dhewm3.Dhewm3.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/org.dhewm3.Dhewm3.png
install -Dpm 644 dist/linux/share/icons/hicolor/256x256/apps/org.dhewm3.Dhewm3.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/org.dhewm3.Dhewm3.png
install -Dpm 644 dist/linux/share/icons/hicolor/scalable/apps/org.dhewm3.Dhewm3.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/org.dhewm3.Dhewm3.svg
install -Dpm 644 dist/linux/share/applications/org.dhewm3.Dhewm3.desktop %{buildroot}%{_datadir}/applications/org.dhewm3.Dhewm3.desktop
install -Dpm 644 dist/linux/share/applications/org.dhewm3.Dhewm3.d3xp.desktop %{buildroot}%{_datadir}/applications/org.dhewm3.Dhewm3.d3xp.desktop

%check

%files
%doc README.md Changelog.md Configuration.md
%license COPYING.txt
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/org.dhewm3.Dhewm3.desktop
%{_datadir}/applications/org.dhewm3.Dhewm3.d3xp.desktop
%{_datadir}/icons/hicolor/*/apps/org.dhewm3.Dhewm3.*
%{_datadir}/metainfo/org.dhewm3.Dhewm3.metainfo.xml

%changelog
