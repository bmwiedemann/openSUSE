#
# spec file for package fontforge
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           fontforge
Version:        20251009
Release:        0
Summary:        A Font Editor
License:        GPL-3.0-or-later
URL:            https://fontforge.org/
Source0:        https://github.com/fontforge/fontforge/releases/download/%{version}/fontforge-%{version}.tar.xz
# PATCH-FIX-OPENSUSE fontforge-version.patch pgajdos@suse.com -- fontforge --version now returns fontforge release version.
Patch0:         fontforge-version.patch
# PATCH-FIX-OPENSUSE add-bitmap-transform-support.patch boo#1169444 alarrosa@suse.com -- support transforming bitmap glyphs from python with one of the predefined transformations.
Patch1:         add-bitmap-transform-support.patch
# PATCH-FIX-UPSTREAM fontforge-fix-crash-issue-in-allmarkglyphs.patch qzhao@suse.com -- Fix crash issue in allmarkglyphs (#5668).
Patch2:         fontforge-fix-crash-issue-in-allmarkglyphs.patch
# PATCH-FIX-UPSTREAM fontforge-fix-UFO-crash-for-empty-contours.patch qzhao@suse.com -- Fix UFO crash for empty contours (#5645).
Patch3:         fontforge-fix-UFO-crash-for-empty-contours.patch
# PATCH-FIX-UPSTREAM fontforge-fix-crash-in-Metrics-View.patch qzhao@suse.com -- Fix crash in Metrics View (#5647).
Patch4:         fontforge-fix-crash-in-Metrics-View.patch
# PATCH-FIX-UPSTREAM fontforge-fix-crash-on-UpDown-keypress-in-the-feature-list.patch qzhao@suse.com -- Metrics view: Fix crash on Up/Down keypress while in the feature list (#5683).
Patch5:         fontforge-fix-crash-on-UpDown-keypress-in-the-feature-list.patch
# PATCH-FIX-UPSTREAM fontforge-CVE-2025-15279-part01_7d67700c.patch CVE-2025-15279 ZDI-CAN-27517 bsc#1256013 qzhao@suse.com -- Fix CVE-2025-15279: Heap buffer overflow in BMP RLE decompression (#5720)
Patch6:         fontforge-CVE-2025-15279-part01_7d67700c.patch
# PATCH-FIX-UPSTREAM fontforge-CVE-2025-15275.patch CVE-2025-15275 ZDI-25-1189 ZDI-CAN-28543 bsc#1256025 qzhao@suse.com -- Fix CVE-2025-15275: Heap buffer overflow in SFD image parsing (#5721).
Patch7:         fontforge-CVE-2025-15275.patch
# PATCH-FIX-UPSTREAM fontforge-CVE-2025-15269.patch CVE-2025-15269 ZDI-25-1195 ZDI-CAN-28564 bsc#1256032 qzhao@suse.com -- Fix CVE-2025-15269: Use-after-free in SFD ligature parsing (#5722).
Patch8:         fontforge-CVE-2025-15269.patch
# PATCH-FIX-UPSTREAM fontforge-CVE-2025-15279-part02_720ea950.patch CVE-2025-15279 ZDI-CAN-27517 bsc#1256013 qzhao@suse.com -- Fix CVE-2025-15279: Move bounds check inside cnt >= 3 block (#5723).
Patch9:         fontforge-CVE-2025-15279-part02_720ea950.patch
# PATCH-FIX-UPSTREAM fontforge-fix-crash-for-content-over-32767-characters-in-GDraw.patch qzhao@suse.com -- Fix crash for content over 32767 characters in GDraw multiline text field (#5728).
Patch10:        fontforge-fix-crash-for-content-over-32767-characters-in-GDraw.patch
# PATCH-FIX-UPSTREAM fontforge-fix-multiple-crashes-in-Multiple-Masters.patch qzhao@suse.com -- Fix multiple crashes in Multiple Masters (#5733).
Patch11:        fontforge-fix-multiple-crashes-in-Multiple-Masters.patch
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  giflib-devel
BuildRequires:  git
BuildRequires:  gtk3-devel
BuildRequires:  gtkmm3-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libspiro-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel >= 3.8
BuildRequires:  readline-devel
BuildRequires:  woff2-devel
BuildRequires:  xz
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)

%description
FontForge allows editing of outline and bitmap fonts.  With it, you can
create new fonts or modify old ones.  It also converts font formats and
can convert among PostScript (ASCII & binary Type 1, some Type 3s, and
some Type 0s), TrueType, OpenType (Type2), and CID-keyed fonts.

%package doc
Summary:        Documentation for FontForge
BuildArch:      noarch

%description doc
FontForge allows editing of outline and bitmap fonts. With it, you can
create new fonts or modify old ones. It also converts font formats and
can convert among PostScript, TrueType, OpenType, and CID-keyed fonts.

This subpackage contains the documentation to FontForge.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Requires:       %{name} = %{version}
Requires:       freetype2-devel

%description devel
FontForge allows editing of outline and bitmap fonts. With it, you can
create new fonts or modify old ones. It also converts font formats and
can convert among PostScript, TrueType, OpenType, and CID-keyed fonts.

This subpackage contains all necessary include files and libraries needed
to develop applications that use FontForge libraries.

%prep
%autosetup -p1

%build
%cmake \
    -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}/html

%install
%cmake_install
%find_lang FontForge
find %{buildroot} -type f -name "*.la" -delete -print
rm %{buildroot}%{_docdir}/%{name}/html/.buildinfo
rm %{buildroot}%{_docdir}/%{name}/html/.nojekyll
%fdupes -s %{buildroot}%{_datadir}/%{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f FontForge.lang
%license LICENSE COPYING.gplv3
%exclude %{_docdir}/%{name}/html
%{_mandir}/man1/*.1%{?ext_man}
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_datadir}/fontforge/
%{python3_sitearch}/*
%{_datadir}/applications/org.fontforge.FontForge.desktop
%{_datadir}/icons/hicolor/*/apps/org.fontforge.FontForge.png
%{_datadir}/icons/hicolor/scalable/apps/org.fontforge.FontForge.svg
%{_datadir}/metainfo/org.fontforge.FontForge.*.xml
%{_datadir}/mime/packages/%{name}.xml
%dir %{_docdir}/fontforge

%files doc
%license LICENSE
%doc AUTHORS README.md
%doc %{_docdir}/%{name}/html

%files devel
%doc CONTRIBUTING.md
%{_libdir}/lib*.so

%changelog
