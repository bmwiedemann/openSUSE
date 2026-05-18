#
# spec file for package dustrac
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


Name:           dustrac
Version:        2.2.0
Release:        0
Summary:        Tile-based 2D Racing Game
License:        GPL-3.0-only AND CC-BY-SA-3.0
Group:          Amusements/Games/Action/Race
URL:            https://juzzlin.github.io/DustRacing2D/
Source:         https://github.com/juzzlin/DustRacing2D/archive/%{version}/DustRacing2D-%{version}.tar.gz
BuildRequires:  cmake >= 3.10
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(vorbisfile)
Requires:       dejavu-fonts

%description
Dust Racing is a tile-based 2D racing game written with Qt (in C++)
and OpenGL. Dust Racing comes with a Qt-based level editor for level
creation. A separate engine, MiniCore, is used for physics modeling.

%prep
%setup -q -n DustRacing2D-%{version}

%build
%cmake \
  -DReleaseBuild=1 \
  -DSystemFonts=1 \
  -DDATA_PATH=%{_datadir}/%{name} \
  -DDOC_PATH=%{_docdir}/%{name} \
  -DBUILD_SHARED_LIBS:BOOL=OFF # build the physics engine statically
                               # (not used by any other software)
%cmake_build

%install
%cmake_install
%fdupes -s %{buildroot}%{_prefix}

%files
%{_bindir}/dustrac-game
%{_bindir}/dustrac-editor
%{_datadir}/%{name}/
%{_datadir}/applications/dustrac-game.desktop
%{_datadir}/applications/dustrac-editor.desktop
%{_datadir}/icons/hicolor/64x64/apps/dustrac-game.png
%{_datadir}/icons/hicolor/64x64/apps/dustrac-editor.png
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/dustrac.appdata.xml
%{_docdir}/%{name}

%changelog
