#
# spec file for package chessx
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.5.0
Release:        0
Summary:        Chess database
License:        GPL-2.0-only
Group:          Amusements/Games/Board/Chess
URL:            http://chessx.sourceforge.net
Source0:        https://sourceforge.net/projects/chessx/files/chessx/%{version}/chessx-%{version}.tgz
BuildRequires:  fdupes
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(zlib)
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
%setup -q

%build
lrelease-qt5 i18n/*
qmake-qt5 QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/pixmaps
mkdir -p %{buildroot}/%{_datadir}/applications
install -m 0755 release/%{name} -t %{buildroot}/%{_bindir}
install -m 0644 unix/%{name}.desktop -t %{buildroot}/%{_datadir}/applications
install -m 0644 data/images/%{name}.png -t %{buildroot}/%{_datadir}/pixmaps
chmod -x data/images/circle_*.svg
cp -r data -t %{buildroot}/%{_datadir}/%{name}
cp i18n/*.qm -t %{buildroot}/%{_datadir}/%{name}/data/lang
find %{buildroot} -size 0 -delete
%fdupes -s %{buildroot}

%files
%license COPYING
%doc ChangeLog README.developers TODO
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/data
%{_datadir}/pixmaps/%{name}.png

%changelog
