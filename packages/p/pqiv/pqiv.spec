#
# spec file for package pqiv
#
# Copyright (c) 2022 SUSE LLC
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


Name:           pqiv
Version:        2.12
Release:        0
Summary:        Minimalist image viewer
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/phillipberndt/pqiv
Source:         https://github.com/phillipberndt/pqiv/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ImageMagick)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(poppler-glib)

%description
pqiv is a powerful GTK 3 based command-line image viewer with a minimal UI. It
is highly customizable, can be fully controlled from scripts, and has support
for various file formats including PDF, Postscript, video files and archives.
It is optimized to be quick and responsive.
It comes with support for animations, slideshows, transparency, VIM-like key
bindings, automated loading of new images as they appear, external image
filters, image preloading, and much more.
pqiv started as a Python rewrite of qiv avoiding imlib, but evolved into a much
more powerful tool. Today, pqiv stands for powerful quick image viewer.
Features:
 * Command line image viewer
 * Directory traversing to view whole directories
 * Watch files and directories for changes
 * Natural order sorting of the images
 * A status bar showing information on the current image
 * Transparency and animation support
 * Moving, zooming, rotation, flipping
 * Slideshows
 * Highly customizable and scriptable
 * Supports external image filters (e.g. `convert`)
 * Preloads the next image in the background
 * Fade between images
 * Optional PDF/eps/ps support (useful e.g. for scientific plots)
 * Optional video format support (e.g. for webm animations)

%package ffmpeg
Summary:        Backend ffmpeg/libav for %{name}
Group:          Productivity/Graphics/Viewers
Requires:       %{name} = %{version}

%description ffmpeg
Backend ffmpeg/libav for %{name}

%package gdkpixbuf
Summary:        Backend gdkpixbuf for %{name}
Group:          Productivity/Graphics/Viewers
Requires:       %{name} = %{version}

%description gdkpixbuf
Backend gdkpixbuf for %{name}

%package libarchive
Summary:        Backend libarchive for %{name}
Group:          Productivity/Graphics/Viewers
Requires:       %{name} = %{version}

%description libarchive
Backend libarchive/libarchive_cbx for %{name}

%package poppler
Summary:        Backend poppler for %{name}
Group:          Productivity/Graphics/Viewers
Requires:       %{name} = %{version}

%description poppler
Backend poppler for %{name}

%package spectre
Summary:        Backend spectre for %{name}
Group:          Productivity/Graphics/Viewers
Requires:       %{name} = %{version}

%description spectre
Backend spectre for %{name}

%package wand
Summary:        Backend wand for %{name}
Group:          Productivity/Graphics/Viewers
Requires:       %{name} = %{version}

%description wand
Backend wand for %{name}

%package webp
Summary:        Backend webp for %{name}
Group:          Productivity/Graphics/Viewers
Requires:       %{name} = %{version}

%description webp
Backend webp for %{name}

%prep
%setup -q

%build
./configure \
  --libdir=%{_libdir} \
  --backends-build=shared \
  --backends=archive_cbx,gdkpixbuf,libav,poppler,spectre,wand,webp

%make_build

%install
%make_install

%files
%{_mandir}/man1/%{name}.1%{?ext_man}
%dir %{_libdir}/%{name}
%doc README.markdown
%license LICENSE
%{_datadir}/applications/pqiv.desktop
%{_bindir}/%{name}

%files ffmpeg
%{_libdir}/%{name}/%{name}-backend-libav.so

%files gdkpixbuf
%{_libdir}/%{name}/%{name}-backend-gdkpixbuf.so

%files libarchive
%{_libdir}/%{name}/%{name}-backend-archive.so
%{_libdir}/%{name}/%{name}-backend-archive_cbx.so

%files poppler
%{_libdir}/%{name}/%{name}-backend-poppler.so

%files spectre
%{_libdir}/%{name}/%{name}-backend-spectre.so

%files wand
%{_libdir}/%{name}/%{name}-backend-wand.so

%files webp
%{_libdir}/%{name}/%{name}-backend-webp.so

%changelog
