#
# spec file for package pdfquirk
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2007-2011 Klaas Freitag <freitag@kde.org>
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


Name:           pdfquirk
Version:        0.95
Release:        0
Summary:        App to create PDFs from images or scans
License:        GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://dragotin.github.io/quirksite
Source0:        https://github.com/dragotin/pdfquirk/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        pdfquirk_es.ts

BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core) >= 5.5.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Widgets)
Requires:       ImageMagick
Recommends:     deskew
Recommends:     sane-backends

%description
PDF Quirk helps to generate PDF files from images from storage
or directly from the scanner.

%prep
%autosetup -p1
# Update the spanish translation that came in after release
cp %{SOURCE1} resources/

%build

%cmake
%cmake_build

%install
%cmake_install

%suse_update_desktop_file -r de.volle-kraft-voraus.pdfquirk Graphics Scanning

%files
%{_bindir}/pdfquirk
%{_datadir}/applications/de.volle-kraft-voraus.pdfquirk.desktop
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/metainfo/de.volle-kraft-voraus.pdfquirk.appdata.xml

%doc AUTHORS README.md
%license LICENSE

%changelog
