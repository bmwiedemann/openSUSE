#
# spec file for package fbi
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           fbi
Version:        2.14
Release:        0
Summary:        Image Viewer for the Linux Framebuffer Console
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://www.kraxel.org/blog/linux/fbida/
Source0:        https://www.kraxel.org/releases/fbida/fbida-%{version}.tar.gz
Source1:        https://www.kraxel.org/releases/fbida/fbida-%{version}.tar.gz.asc
Source2:        fbi.keyring
Patch0:         fbi.patch
BuildRequires:  curl-devel
BuildRequires:  freetype2-devel
BuildRequires:  giflib-devel >= 5.1.0
BuildRequires:  libjpeg-devel
BuildRequires:  libpcd-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig(cairo-gl)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(poppler-glib)
Requires:       ghostscript-library

%description
This is a image viewer for Linux framebuffer devices. It has PhotoCD,
jpeg, ppm, gif, tiff, xwd, bmp, and png support built-in.  Unknown
formats are piped through convert (ImageMagick), which hopefully can
handle it.

%package -n exiftran
Summary:        Digital Camera JPEG image transformation utility
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Other

%description -n exiftran
exiftran is a command-line utility to transform digital image JPEG
images. It can do lossless rotations like jpegtran, but unlike
jpegtran, it cares about the EXIF data.  It can rotate images
automatically by checking the EXIF orientation tag, updating the EXIF
information if needed (image dimension, orientation), and also rotating
the EXIF thumbnail. It can process multiple images at once.

%package -n fbpdf
Summary:        PDF viewer for Linux framebuffer devices
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Viewers

%description -n fbpdf
This is a PDF viewer for Linux framebuffer devices. It uses the poppler
library for rendering.

%prep
%autosetup -p1 -n fbida-%{version}

%build
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -name '*.[ch]' -print0 |\
xargs -0 sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"

export CFLAGS="%{optflags}"
make %{?_smp_mflags} prefix=%{_prefix} exiftran fbi

%install
%make_install prefix=%{_prefix}

%files
%license COPYING
%{_bindir}/fbgs
%{_bindir}/fbi
%{_mandir}/man1/fbgs.*
%{_mandir}/man1/fbi.*

%files -n exiftran
%license COPYING
%{_bindir}/exiftran
%{_mandir}/man1/exiftran.*

%files -n fbpdf
%license COPYING
%{_bindir}/fbpdf

%changelog
