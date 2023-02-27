#
# spec file for package ultimatestunts
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


Name:           ultimatestunts
Version:        0.7.7.1
Release:        0
Summary:        A racing game in the style of "Stunts"
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Race
URL:            http://ultimatestunts.nl/
Source:         http://downloads.sf.net/ultimatestunts/ultimatestunts-srcdata-0771.tar.gz
Patch1:         01-fix-missing-includes.diff
Patch2:         02-fix-type-puns.diff
Patch3:         03-fix-format-mismatches.diff
Patch4:         04-fix-parallel-build-issue.diff
Patch5:         05-fix-destdir.diff
Patch6:         ultimatestunts-add-pthread.patch
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(freealut)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(vorbisfile)
Requires:       %name-data

%description
Ultimate Stunts is a remake of the famous DOS game "Stunts". Racing in
Ultimate Stunts involves some really spectacular stunts, like
loopings, corkscrews, bridges to jump over, etc. You can also design
your own tracks.

%package data
Summary:        Graphics, music, cars and tracks for Ultimate Stunts
Group:          Amusements/Games/3D/Race
BuildArch:      noarch

%description data
This package contains the game data for Ultimate Stunts.

Ultimate Stunts is a remake of the famous DOS game "Stunts". Racing in
Ultimate Stunts involves some really spectacular stunts, like
loopings, corkscrews, bridges to jump over, etc. You can also design
your own tracks.

%package lang
Summary:        Translations for Ultimate Stunts
Group:          Amusements/Games/3D/Race
BuildArch:      noarch

%description lang
This package contains the translations for Ultimate Stunts.

Ultimate Stunts is a remake of the famous DOS game "Stunts". Racing in
Ultimate Stunts involves some really spectacular stunts, like
loopings, corkscrews, bridges to jump over, etc. You can also design
your own tracks.

%prep
%autosetup -p1 -n %name-srcdata-0771

%build
find . -type d -name .svn -exec rm -Rf "{}" "+"
%configure
%make_build -j1

%install
%make_install usdatadir="%buildroot/%_datadir/ultimatestunts"
%fdupes %buildroot/%_prefix

%files
%config %_sysconfdir/ultimatestunts.conf
%_bindir/ustunts*
%license COPYING

%files data
%_datadir/%name
%_datadir/%name/lang

%changelog
