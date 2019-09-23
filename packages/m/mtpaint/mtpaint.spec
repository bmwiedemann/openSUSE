#
# spec file for package mtpaint
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.40
Release:        0
Summary:        Painting program for creating icons and pixel-based artwork
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
URL:            http://mtpaint.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://downloads.sourceforge.net/%{name}/%{name}_handbook-%{version}.zip
Patch0:         mtpaint-3.40-buff.diff
# PATCH-FIX-OPENSUSE mtpaint-3.40-xdg-open.patch -- fix hardcoded apps, options and handbook location
Patch1:         mtpaint-3.40-xdg-open.patch
# PATCH-FIX-OPENSUSE mtpaint-3.40-strip.patch rh#787462 -- don't strip binary
Patch2:         mtpaint-3.40-strip.patch
# PATCH-FIX-OPENSUSE mtpaint-3.40-giflib5.diff -- fix build with giflib-5.x
Patch3:         mtpaint-3.40-giflib5.diff
BuildRequires:  desktop-file-utils
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libopenjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
Requires:       ImageMagick
Recommends:     %{name}-lang
Recommends:     exif
%lang_package

%description
mtPaint is a simple painting program designed for creating icons and
pixel-based artwork. It can edit indexed palette or 24 bit RGB images
and offers basic painting and palette manipulation tools. Its main
file format is PNG, although it can also handle JPEG, GIF, TIFF, BMP,
XPM, and XBM files.

%package handbook
Summary:        Handbook for the mtpaint painting application
License:        GFDL-1.2-only
Group:          Productivity/Graphics/Bitmap Editors
Requires:       %{name} = %{version}
BuildArch:      noarch

%description handbook
Install this package is want to read the handbook for the painting
application mtpaint.

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1
%patch2
%patch3 -p1

%build
# fix warnings for gcc >= 4.4, use -fno-strict-aliasing
export CFLAGS="%{optflags} -fno-strict-aliasing"
# This is not a "normal" configure
./configure \
    --prefix=%{_prefix} \
    --docdir=%{_defaultdocdir}/%{name} \
    asneeded \
    cflags \
    GIF \
    gtk2 \
    gtkfilesel \
    imagick \
    intl \
    jp2 \
    jpeg \
    lcms2 \
    man \
    tiff \
    thread
make %{?_smp_mflags}

%install
make install \
    MT_PREFIX=%{buildroot}%{_prefix} \
    BIN_INSTALL=%{buildroot}%{_bindir} \
    MT_DATAROOT=%{buildroot}%{_datadir} \
    MT_LANG_DEST=%{buildroot}%{_datadir}/locale \
    MT_MAN_DEST=%{buildroot}%{_mandir}

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
