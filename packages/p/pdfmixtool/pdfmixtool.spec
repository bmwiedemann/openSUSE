#
# spec file for package pdfmixtool
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


Name:           pdfmixtool
Version:        1.1.1
Release:        0
Summary:        Split, Merge, Rotate and Mix PDF Files
License:        GPL-3.0-only
Group:          Productivity/Publishing/PDF
URL:            https://gitlab.com/scarpetta/pdfmixtool/
Source0:        https://gitlab.com/scarpetta/pdfmixtool/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Patch1:         stop_using_obsolete_standards.patch
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(libqpdf)

%description
An application to split, merge, rotate, mix and create multipage PDF files.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
%suse_update_desktop_file -r -G "PDF Tools" eu.scarpetta.PDFMixTool Qt Office Publishing Graphics Viewer

%files
%license LICENSE
%doc AUTHORS.md CHANGELOG.md README.md TRANSLATORS.md
%{_bindir}/pdfmixtool
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/*.xml

%changelog
