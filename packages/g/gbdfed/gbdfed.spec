#
# spec file for package gbdfed
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           gbdfed
Version:        1.6
Release:        1
License:        BSD-3-Clause
Summary:        A Gtk-based BDF Font Editor, Descendant of XmBDFed
Url:            http://www.math.nmsu.edu/~mleisher/Software/gbdfed/
Group:          Productivity/Graphics/Bitmap Editors
Source:         %{name}-%{version}.tar.bz2
Source1:        gbdfed.desktop
Source2:        COPYING
Source3:        gbdfed16x16.png
Source4:        gbdfed32x32.png
Source5:        gbdfed48x48.png
Patch0:         %{name}-%{version}_array-index.patch
Patch1:         %{name}-%{version}_64bit.patch
Patch2:         %{name}-%{version}-new-gtk.patch
BuildRequires:  freetype2-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A Gtk-based bitmap font (BDF) editor, descendant of XmBDFed. It can
import PK/GF fonts, HBF fonts (Han Bitmap Font),Linux console fonts
(PSF, CP, FNT), Sun console fonts (vfont), Windows FON/FNT fonts,
TrueType fonts and collections, and X server fonts. It exports PSF and
HEX fonts and allows you to edit two- and four-bits-per-pixel grayscale
fonts.

%prep
%setup -q
install -m 644 %{SOURCE2} .
%patch0
%patch1
%patch2 -p1

%build
%configure
make %{?smp_mflags}

%install
%make_install
# desktop menu
%suse_update_desktop_file -i %{name} Graphics RasterGraphics
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48}/apps
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/gbdfed.png
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/gbdfed.png
install -m 644 %{SOURCE5} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gbdfed.png
mkdir -p %{buildroot}%{_datadir}/pixmaps
ln -sf ../icons/hicolor/48x48/apps/gbdfed.png %{buildroot}%{_datadir}/pixmaps/gbdfed.png

%files
%defattr(-,root,root)
%{_datadir}/applications/gbdfed.desktop
%{_bindir}/*
%{_datadir}/icons/*
%{_datadir}/pixmaps/gbdfed.png
%doc NEWS README COPYING
%doc %{_mandir}/man1/*

%changelog
