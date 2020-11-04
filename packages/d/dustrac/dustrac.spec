#
# spec file for package dustrac
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


Name:           dustrac
Version:        2.0.5
Release:        0
Summary:        Tile-based 2D Racing Game
License:        GPL-3.0-only AND CC-BY-SA-3.0
Group:          Amusements/Games/Action/Race
URL:            https://juzzlin.github.io/DustRacing2D/
Source:         https://github.com/juzzlin/DustRacing2D/archive/%{version}/dustrac-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Include-stdexcept-for-std-runtime_error.patch
BuildRequires:  cmake >= 2.8.12
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  gcc >= 4.6
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Xml)
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
%patch0 -p1

%build
%cmake \
  -DReleaseBuild=1 \
  -DDATA_PATH=%{_datadir}/%{name} \
  -DDOC_PATH=%{_docdir}/%{name} \
  -DBUILD_SHARED_LIBS:BOOL=OFF # build the physics engine statically
                               # (not used by any other software)
make %{?_smp_mflags}

%install
%cmake_install
%fdupes -s %{buildroot}%{_prefix}

# Use system fonts
rm %{buildroot}%{_datadir}/%{name}/fonts/DejaVuSans-Bold.ttf
ln -s %{_datadir}/fonts/truetype/DejaVuSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/fonts/DejaVuSans-Bold.ttf

%files
%{_bindir}/dustrac-game
%{_bindir}/dustrac-editor
%{_datadir}/%{name}/
%{_datadir}/applications/dustrac-game.desktop
%{_datadir}/applications/dustrac-editor.desktop
%{_datadir}/pixmaps/dustrac-game.png
%{_datadir}/pixmaps/dustrac-editor.png
%{_datadir}/icons/hicolor/64x64/apps/dustrac-game.png
%{_datadir}/icons/hicolor/64x64/apps/dustrac-editor.png
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/dustrac.appdata.xml
%{_docdir}/%{name}

%changelog
