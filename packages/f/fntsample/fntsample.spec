#
# spec file for package fntsample
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


Name:           fntsample
Version:        5.4
Release:        0
Summary:        Program for producing font samples
License:        CC-PDDC AND GPL-3.0-or-later
URL:            https://github.com/eugmes/fntsample
Source:         https://github.com/eugmes/fntsample/archive/refs/tags/release/%{version}.tar.gz#/fntsample-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  unicode-blocks
BuildRequires:  pkgconfig(cairo) >= 1.15.4
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo) >= 1.37.0
BuildRequires:  pkgconfig(pangoft2) >= 1.37.0
Requires:       unicode-blocks
%lang_package

%description
fntsample is a program for making font samples that show Unicode coverage of
the font. The samples are similar in appearance to Unicode charts.

Features:
* Support for various font formats using FreeType library, including TrueType,
  OpenType, and Type1.
* Creation of samples in PDF and PostScript format.
* Addition of outlines with Unicode block names for PDF samples.
* Selection of code ranges to show in charts.
* Comparisons of two font files with highlighting of added glyphs.

%prep
%autosetup -n %{name}-release-%{version}

%build
%cmake \
  -DUNICODE_BLOCKS=%{_datadir}/unicode/Blocks.txt
%cmake_build

%install
%cmake_install
# do no use env in shebang
sed -i 's/\/usr\/bin\/env perl/\/usr\/bin\/perl/' %{buildroot}%{_bindir}/*

%find_lang %{name}

%files
%license COPYING
%doc ChangeLog
%{_bindir}/fntsample
%{_bindir}/pdf-extract-outline
%{_bindir}/pdfoutline
%{_mandir}/man1/fntsample.1%{?ext_man}
%{_mandir}/man1/pdf-extract-outline.1%{?ext_man}
%{_mandir}/man1/pdfoutline.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
