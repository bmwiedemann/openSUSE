#
# spec file for package heimer
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021 Fabio Pesari
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


Name:           heimer
Version:        3.6.3
Release:        0
Summary:        Mind map, diagram, and note-taking tool
License:        CC-BY-SA-3.0 AND GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://github.com/juzzlin/Heimer
Source0:        https://github.com/juzzlin/Heimer/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Xml)

%description
Heimer is a desktop application for creating mind maps and other
suitable diagrams. Features:
* Adjustable grid
* Automatic layout optimization
* Autosave
* Easy-to-use UI
* Export to PNG or SVG
* Forever 100% free
* Full undo/redo
* Nice animations
* Quickly add node text and edge labels
* Save/load in XML-based .ALZ-files
* Translations in English (default), Chinese, Dutch, Finnish, French, Italian, Spanish
* Very fast
* Zoom in/out/fit
* Zoom with mouse wheel

%prep
%setup -q -n Heimer-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
%fdupes -s %{buildroot}%{_datadir}

%files
%doc README.md
%license COPYING
%{_bindir}/heimer
%{_datadir}/applications/heimer.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/256x256/apps/heimer.png
%{_datadir}/metainfo/heimer.appdata.xml
%{_datadir}/pixmaps/heimer.png

%changelog
