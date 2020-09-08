#
# spec file for package jag
#
# Copyright (c) 2020 SUSE LLC
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


Name:           jag
Version:        0.3.8
Release:        0
Summary:        Arcade and Puzzle 2D Game in which you have to break all the target pieces
# jag.xlabsoft.com is down
License:        GPL-3.0-or-later
Group:          Amusements/Games/Logic
URL:            https://gitlab.com/coringao/jag
Source0:        https://gitlab.com/coringao/jag/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source2:        %{name}.appdata.xml
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(xrandr)
Requires:       %{name}-data
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
The aim of JAG is to break all of the target pieces on each level,
and to do this before the time runs out. Keep doing this until you
have beaten the last level and won the game.

%package data
Summary:        Data files for the JAG game
Group:          Amusements/Games/Logic
Requires:       %{name}
Recommends:     %{name}-editor
BuildArch:      noarch

%description data
The aim of JAG is to break all of the target pieces on each level,
and to do this before the time runs out. Keep doing this until you
have beaten the last level and won the game.

Data files (bonus, help, lang, levels, schemes, sounds, tools) for JAG.

%package editor
Summary:        Level Editor for the JAG game
Group:          Amusements/Games/Logic
Requires:       %{name}
Provides:       jag-level-editor = %{version}
Obsoletes:      jag-level-editor < %{version}

%description editor
The aim of JAG is to break all of the target pieces on each level,
and to do this before the time runs out. Keep doing this until you
have beaten the last level and won the game.

This package contains the level editor for JAG.

%prep
%setup -q

# qmake...
sed -i 's#target.path = %{_prefix}/games/#target.path = %{_bindir}#' game.pro
sed -i 's#target.path = %{_prefix}/games/#target.path = %{_bindir}#' src/editor/jag-editor.pro

%build
%qmake5
pushd src/editor
%qmake5
popd

make %{?_smp_mflags}
pushd src/editor
make %{?_smp_mflags}
popd

%install
%qmake5_install
pushd src/editor
%qmake5_install
popd

# Install the desktop files
install -Dm 0644 src/jag.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%suse_update_desktop_file -c %{name}-editor "JAG Level Editor" JAG jag-editor jag-editor "Game;LogicGame;"

# Install icons for applications menus
install -Dm 0644 src/images/jag.png %{buildroot}%{_datadir}/pixmaps/jag.png
install -Dm 0644 src/editor/jag-editor.png %{buildroot}%{_datadir}/pixmaps/jag-editor.png

# Install software gallery metadata
install -Dm 0644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%license LICENSE
%doc CHANGELOG README.md
%dir %{_datadir}/appdata/
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/jag.png

%files data
%license LICENSE
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/data/

%files editor
%license LICENSE
%dir %{_datadir}/games/%{name}
%{_bindir}/jag-editor
%{_datadir}/applications/jag-editor.desktop
%{_datadir}/games/%{name}/editor/
%{_datadir}/pixmaps/jag-editor.png

%changelog
