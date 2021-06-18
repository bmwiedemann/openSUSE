#
# spec file for package pdfmixtool
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


Name:           pdfmixtool
Version:        1.0.1
Release:        0
Summary:        Split, Merge, Rotate and Mix PDF Files
License:        GPL-3.0-only
Group:          Productivity/Publishing/PDF
URL:            https://gitlab.com/scarpetta/pdfmixtool/
Source0:        https://gitlab.com/scarpetta/pdfmixtool/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
# PATCH-FIX-UPSTREAM qpdf9.patch asterios.dramis@gmail.com -- Fix compilation with qpdf-9 in Leap <= 15.2
Patch0:         qpdf9.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(libqpdf)

%description
An application to split, merge, rotate, mix and create multipage PDF files.

%prep
%setup -q -n %{name}-v%{version}
%if 0%{?sle_version} <= 150200 && 0%{?is_opensuse}
%patch0 -p1
%endif

%build
%cmake
%cmake_build

%install
%cmake_install
%suse_update_desktop_file -r -G "PDF Mix Tool" eu.scarpetta.PDFMixTool Qt Office Publishing Graphics Viewer
# Fix rpmlint warning "files-duplicate"
install -dpm 0755 %{buildroot}%{_defaultdocdir}/%{name}
install -pm 0644 AUTHORS.md CHANGELOG.md TRANSLATORS.md %{buildroot}%{_defaultdocdir}/%{name}/
%fdupes -s %{buildroot}

%files
%license LICENSE
%doc AUTHORS.md CHANGELOG.md README.md TRANSLATORS.md
%{_bindir}/pdfmixtool
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/*.xml
%{_datadir}/pdfmixtool/

%changelog
