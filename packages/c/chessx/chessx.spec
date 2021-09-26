#
# spec file for package chessx
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


Name:           chessx
Version:        1.5.6
Release:        0
Summary:        Chess database
License:        GPL-2.0-only
Group:          Amusements/Games/Board/Chess
URL:            http://chessx.sourceforge.net
# was https://sourceforge.net/projects/chessx/files/chessx/%%{version}/chessx-%%{version}.tar.gz
# using _service until https://sourceforge.net/p/chessx/bugs/287/ is fixed
Source0:        %{name}-%{version}.tar.xz
# PATCH-FEATURE-UPSTREAM chessx-install.patch aloisio@gmx.com -- make install work on linux
Patch1:         chessx-install.patch
# PATCH-FEATURE-OPENSUSE chessx-use_system_quazip.patch
Patch2:         chessx-use_system_quazip.patch
# PATCH-FIX-OPENSUSE chessx-use_system_doctest.patch aloisio@gmx.com -- use system doctest instead of embedded
Patch3:         chessx-use_system_doctest.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(doctest)
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150200
BuildRequires:  pkgconfig(quazip1-qt5)
%else
BuildRequires:  pkgconfig(quazip)
%endif
BuildRequires:  pkgconfig(zlib)

%description
ChessX is a chess database. With ChessX, you can browse, edit and
analyze a collection of chess games.

* Load and save PGN files
* Work with multiple databases simultaneously
* Browse games, including variations
* Enter moves, variations, comments
* Play games in training mode or play out games against an engine
* Setup board, copy/paste FEN, merge games
* Display opening tree for current position
* Analyze using UCI and Winboard/Xboard Chess engines
* Observe and play games on FICS

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
find %{buildroot} -size 0 -delete
%fdupes %{buildroot}

%files
%license COPYING
%doc ChangeLog README.developers TODO
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/data
%{_datadir}/pixmaps/%{name}.png

%changelog
