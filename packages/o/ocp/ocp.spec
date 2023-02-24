#
# spec file for package ocp
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

Name:           ocp
Version:        0.2.103
Release:        0
Summary:        Open Cubic Player for MOD/S3M/XM/IT/MIDI music files
# Code is GPL-2.0-or-later, Graphics and animations are CC-BY-3.0
License:        GPL-2.0-or-later AND CC-BY-3.0
Group:          Productivity/Multimedia/Sound/Players
URL:            https://stian.cubic.org/coding-ocp.php
Source0:        https://stian.cubic.org/ocp/%{name}-%{version}.tar.bz2
Source1:        ftp://ftp.cubic.org/pub/player/gfx/opencp25image1.zip
Source2:        ftp://ftp.cubic.org/pub/player/gfx/opencp25ani1.zip
Patch1:         ocp-ini-set-audio-output.patch
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gnu-unifont-otf-fonts
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  xa
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libancient)
BuildRequires:  pkgconfig(libcjson)
BuildRequires:  pkgconfig(libdiscid)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
Requires:       gnu-unifont-otf-fonts
Provides:       opencubicplayer
### Bundled libs
#./playtimidity/timidity-git
Provides:       bundled(timidity++)
#./playsid/libsidplayfp-git
Provides:       bundled(libsidplayfp)
#./playopl/adplug-git
Provides:       bundled(adplug)
#./playopl/adplugdb-git
Provides:       bundled(adplugdb)
#./playopl/libbinio-git
Provides:       bundled(libbinio)

%description
Open Cubic Player is a music file player ported from DOS that supports
Amiga MOD module formats and many variants, such as MTM, STM, 669,
S3M, XM, and IT.  It is also able to render MIDI files using sound
patches and play SID, OGG Vorbis, FLAC, and WAV files.  OCP provides a
nice text-based interface with several text-based and graphical
visualizations.

%prep
%setup -q
%patch1 -p1
unzip %{SOURCE1}
mv license.txt license-images.txt
unzip %{SOURCE2}
mv license.txt license-videos.txt

%build
%configure \
  --with-x11 \
  --with-alsa \
  --without-coreaudio \
  --without-oss \
  --with-lzw \
  --with-lzh \
  --with-flac \
  --without-sdl \
  --with-sdl2 \
  --with-mad \
  --with-unifont-otf=%{_datadir}/fonts/truetype/Unifont.otf \
  --with-unifont-csur-otf=%{_datadir}/fonts/truetype/Unifont_CSUR.otf \
  --with-unifont-upper-otf=%{_datadir}/fonts/truetype/Unifont_Upper.otf \
  --without-update-desktop-database \
  --without-update-mime-database
%make_build

%install
%make_install
# we package the docs ourselves
rm -Rv %{buildroot}%{_datadir}/doc/ocp/
# install images and animations
cp -pv CPPIC*.TGA CPANI*.DAT %{buildroot}%{_datadir}/%{name}/data

%files
%license COPYING license-images.txt license-videos.txt
%doc AUTHORS BUGS CREDITS KEYBOARD_REMAPS SUID
%{_bindir}/ocp
%{_bindir}/ocp-curses
%{_bindir}/ocp-sdl2
%{_bindir}/ocp-vcsa
%{_bindir}/ocp-x11
%{_libdir}/ocp/
%{_datadir}/applications/cubic.org-opencubicplayer.desktop
%{_datadir}/icons/hicolor/*/apps/opencubicplayer.png
%{_datadir}/icons/hicolor/scalable/apps/opencubicplayer.svg
%{_datadir}/mime/packages/opencubicplayer.xml
%{_datadir}/ocp/
%{_mandir}/man1/ocp.1%{?ext_man}

%changelog
