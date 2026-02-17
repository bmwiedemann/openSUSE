#
# spec file for package mupdf
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2011 Guido Berhoerster.
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


%if 0%{suse_version} < 1600
%define gcc_ver 11
%endif
Name:           mupdf
Version:        1.27.1
Release:        0
Summary:        PDF and XPS Viewer and Parser and Rendering Library
License:        AGPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://mupdf.com/
Source0:        https://mupdf.com/downloads/archive/%{name}-%{version}-source.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}-gl.desktop
Patch0:         mupdf-no-strip.patch
# PATCH-FIX-UPSTREAM cve-2026-25556.patch -- based on commit d4743b6092d513321c23c6f7fe5cff87cde043c1
Patch1:         cve-2026-25556.patch
BuildRequires:  Mesa-libGL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  jbig2dec-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  zstd
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
Provides:       bundled(freeglut) = 3.0.0
Provides:       bundled(freeglut-art) = 3.0.0
Provides:       bundled(gumbo-parser) = 0.10.1
Provides:       bundled(lcms2) = 2.14
Provides:       bundled(lcms2-art) = 2.14
Provides:       bundled(mujs) = 1.3.2
Requires:       xdg-utils

%description
MuPDF is a PDF and XPS viewer and parser/rendering library.

The renderer in MuPDF is tailored for anti-aliased graphics. It
renders text with metrics and spacing accurate to within fractions of
a pixel for reproducing the look of a printed page on screen.

MuPDF supports PDF 1.7 with transparency, encryption, hyperlinks,
annotations and search. MuPDF can also read XPS documents
(OpenXPS/ECMA-388).

%package devel-static
Summary:        Development Files for mupdf
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel-static
This package contains development files needed for developing applications
based on mupdf.

%prep
%autosetup -p1 -n %{name}-%{version}-source

for d in $(ls thirdparty | grep -v -e freeglut -e lcms2 -e mujs -e extract -e gumbo-parser)
do
  rm -rf thirdparty/$d
done

echo > user.make "\
  USE_SYSTEM_BROTLI := yes
  USE_SYSTEM_FREETYPE := yes
  USE_SYSTEM_HARFBUZZ := yes
  USE_SYSTEM_JBIG2DEC := yes
  USE_SYSTEM_JPEGXR := yes # not used without HAVE_JPEGXR
  USE_SYSTEM_LCMS2 := no # need lcms2-art fork
  USE_SYSTEM_LIBJPEG := yes
  USE_SYSTEM_MUJS := no # build needs source anyways
  USE_SYSTEM_OPENJPEG := yes
  USE_SYSTEM_TESSERACT := yes
  USE_SYSTEM_ZLIB := yes
  USE_SYSTEM_GLUT := no # need freeglut2-art frok
  USE_SYSTEM_CURL := yes
"

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CC=gcc%{?gcc_ver:-%{gcc_ver}}
export CXX=g++%{?gcc_ver:-%{gcc_ver}}
export XCFLAGS="%{optflags} -fcommon -fPIC -DJBIG_NO_MEMENTO -DTOFU -DTOFU_CJK"
%make_build build=release verbose=yes

%install
%make_install build=release prefix=%{_prefix} libdir=%{_libdir}
rm -rf %{buildroot}%{_datadir}/doc/%{name}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m644 docs/logo/mupdf-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mupdf.svg
install -p -m644 docs/logo/mupdf-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mupdf-gl.svg
## fix strange permissons
chmod 0644 %{buildroot}%{_libdir}/*.a
find %{buildroot}/%{_mandir} -type f -exec chmod 0644 {} \;
find %{buildroot}/%{_includedir} -type f -exec chmod 0644 {} \;
cd %{buildroot}/%{_bindir} && ln -s %{name}-x11 %{name}
%fdupes %{buildroot}%{_datadir}

%files
%doc README CHANGES docs/*
%license COPYING
%{_bindir}/mupdf*
%{_bindir}/mutool
%{_datadir}/applications/mupdf*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*
%{_mandir}/man1/*.1%{?ext_man}

%files devel-static
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.a

%changelog
