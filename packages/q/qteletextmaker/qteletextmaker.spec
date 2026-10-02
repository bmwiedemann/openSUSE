#
# spec file for package qteletextmaker
#
# Copyright (c) 2025-2026, Martin Hauke <mardnh@gmx.de>
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


Name:           qteletextmaker
Version:        1.0
Release:        0
Summary:        A teletext page editor
License:        GPL-3.0-only
#Git-Clone:     https://github.com/gkthemac/QTeletextMaker.git
URL:            https://github.com/gkthemac/QTeletextMaker
Source:         https://github.com/gkthemac/QTeletextMaker/archive/refs/tags/%{version}.tar.gz#/QTeletextMaker-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Widgets)
Provides:       bundled(QtGifImage)

%description
QTeletextMaker is a teletext page editor with an emphasis on
Level 2.5 enhancement editing.

Features
 * Load and save pages in TTI format.
 * Rendering of pages in Levels 1, 1.5, 2.5 and 3.5 including
   Local Objects and side panels.
 * Import and export of single pages in t42, EP1 and HTT formats.
 * Export PNG and animated GIF images of pages.
 * Undo and redo of editing actions.
 * Interactive X/26 Local Enhancement Data triplet editor.
 * Editing of X/27/4 and X/27/5 compositional links to
   enhancement data pages.
 * Palette editor.
 * Configurable zoom.
 * View pages in 4:3, 16:9 pillar-box and 16:9 stretch aspect
   ratios.
 * View pages in mix and attribute-less monochrome modes.

%prep
%autosetup -p1 -n QTeletextMaker-%{version}

%build
%cmake
%make_jobs

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%exclude %{_defaultdocdir}/%{name}/LICENSE
%{_defaultdocdir}/%{name}/examples
%{_bindir}/qteletextmaker
%{_datadir}/icons/hicolor/*/apps/qteletextmaker.png
%{_datadir}/applications/qteletextmaker.desktop

%changelog
