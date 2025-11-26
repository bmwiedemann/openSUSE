#
# spec file for package pdfmixtool
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        1.2.1
Release:        0
Summary:        Split, Merge, Rotate and Mix PDF Files
License:        GPL-3.0-only
Group:          Productivity/Publishing/PDF
URL:            https://gitlab.com/scarpetta/pdfmixtool/
Source0:        https://gitlab.com/scarpetta/pdfmixtool/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(libqpdf)
BuildRequires:  pkgconfig(poppler-qt6)

%description
An application to split, merge, rotate, mix and create multipage PDF files.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc AUTHORS.md CHANGELOG.md README.md TRANSLATORS.md
%{_bindir}/pdfmixtool
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/*.xml

%changelog
