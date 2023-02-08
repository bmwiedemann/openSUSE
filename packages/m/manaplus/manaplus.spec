#
# spec file for package manaplus
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


Name:           manaplus
Version:        2.1.3.17
Release:        0
Summary:        A client for Evol Online and The Mana World: 2D MMORPG
License:        GPL-2.0-or-later
Group:          Amusements/Games/RPG
URL:            https://manaplus.org/
Source:         https://download.tuxfamily.org/manaplus/download/%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM fix-include-time_h.patch -- Fix missing include for time.h when not using clang
Patch0:         fix-include-time_h.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  fontpackages-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  liberation-fonts
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL_gfx)
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_net)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(sdl)
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  pkgconfig(sdl2)
%endif
Requires:       dejavu-fonts
Requires:       liberation-fonts
Recommends:     %{name}-lang
Provides:       evolonline-client = %{version}
Provides:       manaworld-client = %{version}
%lang_package

%description
ManaPlus is extended client for Evol Online, The Mana World and
similar servers based on the eAthena fork. As a 2D style game, Evol
Online creates a fantasy environment. The Mana World (TMW) is an
effort to create an MMORPG. TMW uses 2D graphics and creates a large
and diverse interactive world.

%prep
%autosetup -p1

%build
%configure --enable-unittests
make %{?_smp_mflags}

%install
%make_install
chmod -x %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%if 0%{?suse_version} <= 1500
%fdupes -s %{buildroot}%{_datadir}
%endif
%find_lang %{name}

rm -f %{buildroot}%{_datadir}/%{name}/data/fonts/dejavu*.ttf
ln -s %{_ttfontsdir}/DejaVuSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/dejavusans-bold.ttf
ln -s %{_ttfontsdir}/DejaVuSansMono-Bold.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/dejavusansmono-bold.ttf
ln -s %{_ttfontsdir}/DejaVuSansMono.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/dejavusansmono.ttf
ln -s %{_ttfontsdir}/DejaVuSerifCondensed-Bold.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/dejavuserifcondensed-bold.ttf
ln -s %{_ttfontsdir}/DejaVuSerifCondensed.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/dejavuserifcondensed.ttf
ln -s %{_ttfontsdir}/DejaVuSans.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/dejavusans.ttf

rm -f %{buildroot}%{_datadir}/%{name}/data/fonts/liberation*.ttf
ln -s %{_ttfontsdir}/LiberationMono-Bold.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/liberationsansmono-bold.ttf
ln -s %{_ttfontsdir}/LiberationMono-Regular.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/liberationsansmono.ttf
ln -s %{_ttfontsdir}/LiberationSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/liberationsans-bold.ttf
ln -s %{_ttfontsdir}/LiberationSans-Regular.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/liberationsans.ttf

%if 0%{?suse_version} <= 1500
%check
make %{?_smp_mflags} check || ( cat "src/test-suite.log" && false )
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog docs/*.txt README
%{_bindir}/manaplus
%{_bindir}/dyecmd
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/manaplustest.desktop
%{_mandir}/man6/%{name}*
%{_datadir}/metainfo/%{name}.metainfo.xml

%files lang -f %{name}.lang

%changelog
