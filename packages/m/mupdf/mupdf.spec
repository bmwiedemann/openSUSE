#
# spec file for package mupdf
#
# Copyright (c) 2020 SUSE LLC
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


Name:           mupdf
Version:        1.18.0
Release:        0
Summary:        PDF and XPS Viewer and Parser and Rendering Library
License:        AGPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://mupdf.com/
Source0:        %{URL}/downloads/archive/%{name}-%{version}-source.tar.xz
Source1:        %{name}.desktop
Source2:        %{name}-gl.desktop
Patch0:         mupdf-no-strip.patch
BuildRequires:  Mesa-libGL-devel
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  jbig2dec-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  libgumbo-devel
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
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

for d in $(ls thirdparty | grep -v -e freeglut -e lcms2 -e mujs)
do
  rm -rf thirdparty/$d
done

echo > user.make "\
  USE_SYSTEM_FREETYPE := yes
  USE_SYSTEM_HARFBUZZ := yes
  USE_SYSTEM_JBIG2DEC := yes
  USE_SYSTEM_JPEGXR := yes # not used without HAVE_JPEGXR
  USE_SYSTEM_LCMS2 := no # need lcms2-art fork
  USE_SYSTEM_LIBJPEG := yes
  USE_SYSTEM_MUJS := no # build needs source anyways
  USE_SYSTEM_OPENJPEG := yes
  USE_SYSTEM_ZLIB := yes
  USE_SYSTEM_GLUT := no # need freeglut2-art frok
  USE_SYSTEM_CURL := yes
  USE_SYSTEM_GUMBO := yes
"

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
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

%suse_update_desktop_file mupdf

%if 0%{?suse_version} <= 1320
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%doc README CHANGES docs/*
%license COPYING
%{_bindir}/*
%{_datadir}/applications/mupdf*.desktop
%{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/scalable
%{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/*
%{_mandir}/man1/*.1%{?ext_man}

%files devel-static
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.a

%changelog
