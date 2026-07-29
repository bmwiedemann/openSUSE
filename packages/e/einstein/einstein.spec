#
# spec file for package einstein
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


Name:           einstein
Version:        2.0
Release:        0
Summary:        Einstein's Puzzle
License:        GPL-2.0-or-later
URL:            https://web.archive.org/web/20121029043853/http://games.flowix.com/en/index.html
Source0:        https://github.com/13ilya/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(zlib)

%description
Einstein's Puzzle is a logic game based on Einstein's famous riddle.
The game goal is to open all cards in square of 6x6 cards.
For this, a number of hints describing relations between card positions are given.

%prep
%autosetup -p1

%build
pushd mkres
%make_build OPTIMIZE="%{optflags} -O3"
popd
pushd res
./build.sh
popd
%make_build OPTIMIZE="%{optflags} -O3"

%install
%make_install

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.res
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop

%changelog
