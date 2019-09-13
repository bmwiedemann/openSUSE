#
# spec file for package trackballs
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           trackballs
Version:        1.3.1
Release:        0
Summary:        A Marble Madness-like Game
License:        GPL-2.0-only
Group:          Amusements/Games/3D/Other
URL:            https://trackballs.github.io/
Source0:        https://github.com/trackballs/trackballs/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  guile-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
Obsoletes:      %{name}-music
Obsoletes:      %{name}-music-extra

%description
Trackballs is a game similar to the classic "Marble Madness" game
on the Amiga from the 80s. The player collects points by steering a
marble ball through a labyrinth filled with vicious hammers, pools of
acid, and other obstacles.

%prep
%setup -q

%build
%cmake \
    -DTRACKBALLS_DOC_DIR=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%{_docdir}/%{name}
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/trackballs.*

%changelog
