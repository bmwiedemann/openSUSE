#
# spec file for package mtpaint
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2013 B1 Systems GmbH, Vohburg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mtpaint
Version:        3.50
Release:        0
Summary:        Painting program for creating icons and pixel-based artwork
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
URL:            http://mtpaint.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://downloads.sourceforge.net/%{name}/%{name}_handbook-%{version}.zip
# PATCH-FIX-OPENSUSE mtpaint-3.50-xdg-open.patch -- fix hardcoded apps, options and handbook location
Patch0:         mtpaint-3.50-xdg-open.patch
# PATCH-FIX-OPENSUSE mtpaint-3.50-strip.patch rh#787462 -- don't strip binary
Patch1:         mtpaint-3.50-strip.patch
# PATCH-FIX-UPSTREAM https://github.com/wjaguar/mtPaint/issues/60 -- fix gcc version parsing
Patch2:         mtpaint-3.50-fix-gcc-version-parsing.patch
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  unzip
Requires:       ImageMagick
Recommends:     %{name}-lang
Recommends:     exif
%lang_package

%description
mtPaint is a painting program designed for creating icons and
pixel-based artwork. It can edit indexed palette or 24 bit RGB images
and offers basic painting and palette manipulation tools. Its main
file format is PNG, although it can also handle JPEG, GIF, TIFF, BMP,
XPM, and XBM files.

%package handbook
Summary:        Handbook for the mtpaint painting application
License:        GFDL-1.2-only
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description handbook
Documentation for the painting application mtpaint.

%prep
%autosetup -p1 -a1

%build
# fix warnings for gcc >= 4.4, use -fno-strict-aliasing
export CFLAGS="%{optflags} -fno-strict-aliasing"
# This is not an autoconf-generated configure
./configure \
    --prefix=%{_prefix} \
    --docdir=%{_defaultdocdir}/%{name} \
    asneeded \
    cflags \
    GIF \
    gtk3 \
    gtkfilesel \
    imagick \
    intl \
    jpeg \
    jp2v2 \
    lcms2 \
    man \
    tiff \
    thread \
    webp
%make_build

%install
%make_install \
    MT_PREFIX=%{_prefix} \
    BIN_INSTALL=%{_bindir} \
    MT_DATAROOT=%{_datadir} \
    MT_LANG_DEST=%{_datadir}/locale \
    MT_MAN_DEST=%{_mandir}

%find_lang %{name}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}*

%files handbook
%license %{name}_handbook-%{version}/COPYING
%doc %{name}_handbook-%{version}/docs/*

%files lang -f %{name}.lang

%changelog
