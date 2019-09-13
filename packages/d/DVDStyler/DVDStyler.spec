#
# spec file for package DVDStyler
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012-2014 Mariusz Fik <fisiu@opensuse.org>
# Copyright (c) 2011-2012 Pascal Bleser <pascal.bleser@opensuse.org>
# Copyright (c) 2007-2011 Detlef Reichelt <detlef@links2linux.de>
# Copyright (c) 2004-2005 Rainer Lay <rainer@links2linux.de>
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


%define wxsvgver %(pkg-config --modversion libwxsvg)
Name:           DVDStyler
Version:        3.0.4
Release:        0
Summary:        GUI frontend for dvdauthor and other related tools
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            https://www.dvdstyler.org
Source:         https://sourceforge.net/projects/dvdstyler/files/dvdstyler/%{version}/%{name}-%{version}.tar.bz2
Source1:        gpl-3.0.txt
# PATCH-FIX-UPSTREAM DVDStyler-fix-build-ffmpeg4.patch -- Fix build with ffmpeg v4
Patch0:         DVDStyler-fix-build-ffmpeg4.patch

BuildRequires:  bison
#!BuildIgnore: cdrkit-cdrtools-compat
BuildRequires:  dvd+rw-tools
BuildRequires:  dvdauthor
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  mkisofs >= 2.01
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-3_0-devel
BuildRequires:  xmlto
BuildRequires:  zip
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwxsvg) >= 1.5.11
BuildRequires:  pkgconfig(mjpegtools)
Requires:       dvd+rw-tools
Requires:       dvdauthor >= 0.7.1
Requires:       dvdisaster >= 0.79.5
Requires:       libwxsvg3 = %{wxsvgver}
Requires:       mjpegtools
Requires:       mkisofs
Requires:       wxsvg = %{wxsvgver}
Requires:       xine-ui >= 0.99.1

%description
DVDStyler is a DVD authoring application for the creation of DVDs. It
allows not only burning of video files on DVD that can be played on
standalone DVD players, but also creation of individually designed
DVD menus.
Features:

*creation and burning of DVD video with interactive menus
*ability to design a custom DVD menu or to select one from the
 list of ready to use menu templates
*creation of photo slideshow
*addition of multiple subtitle and audio tracks
*support for AVI, MOV, MP4, MPEG, OGG, WMV and other file formats
*support for MPEG-2, MPEG-4, DivX, Xvid, MP2, MP3, AC-3 and other
 audio and video formats
*support for multi-core processors
*use of MPEG and VOB files without reencoding, see FAQ
*placement of files with different audio/video format on one DVD
 (support for titlesets)
*support for drag & drop
*flexible menu creation on the basis of scalable vector graphic
*import of image file for background
*placement of buttons, text, images and other graphic objects anywhere on
 the menu screen
*modification of the font/color and other parameters of buttons
 and graphic objects
*scaling of any button or graphic object
*copy any menu object or whole menu
*customize navigation using DVD scripting

%lang_package

%prep
%setup -q
%patch0 -p1
# do not install docs
sed -i '/^doc_DATA/d' Makefile.in
cp -v %{SOURCE1} .

%build
export FFMPEG_PATH=%{_bindir}/ffmpeg
%configure --enable-debug
make %{?_smp_mflags}

%install
%make_install

%suse_update_desktop_file -r dvdstyler DiscBurning
%find_lang dvdstyler

%files
%doc AUTHORS ChangeLog README
%license COPYING gpl-3.0.txt
%{_bindir}/dvdstyler
%{_datadir}/applications/dvdstyler.desktop
%{_datadir}/dvdstyler
%{_datadir}/pixmaps/dvdstyler.png
%{_mandir}/man1/dvdstyler.1%{ext_man}

%files lang -f dvdstyler.lang

%changelog
