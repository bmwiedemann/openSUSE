#
# spec file for package moc
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


Name:           moc
Version:        2.6.0~svn2994
Release:        0
Summary:        Console audio player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
Url:            http://moc.daper.net/
Source0:        trunk-%{version}.tar.xz

Patch1:         moc.timestamp.patch
Patch2:         moc.TiMidity_Config.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  file-devel
BuildRequires:  libdb-4_8-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac) >= 1.1
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmodplug) >= 0.7
BuildRequires:  pkgconfig(librcc)
BuildRequires:  pkgconfig(libtimidity) >= 0.1.0
BuildRequires:  pkgconfig(ogg) >= 1.0
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile) >= 1.0.0
BuildRequires:  pkgconfig(speex) >= 1.0.0
BuildRequires:  pkgconfig(taglib_c)
BuildRequires:  pkgconfig(vorbis) >= 1.0
BuildRequires:  pkgconfig(vorbisfile) >= 1.0
BuildRequires:  pkgconfig(wavpack) >= 4.31

%description
MOC (music on console) is a console audio player for LINUX/UNIX designed to be
powerful and easy to use.
You just need to select a file from some directory using the menu similar to
Midnight Commander, and MOC will start playing all files in this directory
beginning from the chosen file. There is no need to create play lists like in
other players.
If you want to combine some files from one or few directories on one play list,
you can do this. The play list will be remembered between runs or you can save
it as an m3u file to load it whenever you want.
Need the console where MOC is running for more important things? Need to close
the X terminal emulator? You don't have to stop playing - just press q and the
interface will be detached leaving the server running. You can attach it later,
or you can attach one interface in the console, and another in the X terminal
emulator, no need to switch just to play another file.
MOC plays smoothly, regardless of system or I/O load because it uses the output
buffer in a separate thread. It doesn't cause gaps between files, because the
next file to be played is precached while playing the current file.

Internet stream (Icecast, Shoutcast) are supported.
Key mapping can be fully customized.
Supported file formats are: mp3, Ogg Vorbis, FLAC, Musepack, Speex, WAVE, AIFF,
AU (and other less popular formats supported by libsndfile. New formats support
is under development.

Other features:
  * Simple mixer.
  * Color themes.
  * Searching the menu (the play list or a directory) like M-s in Midnight Commander.
  * The way MOC creates titles from tags is configurable.
  * Optional character set conversion for file tags using iconv().
  * OSS, JACK, and ALSA output.

%prep
%autosetup -p1 -n trunk-%{version}

%build
autoreconf -fi
%configure --help
%configure \
	--with-gnu-ld \
	--without-included-ltdl \
	--without-sidplay2 \
	--without-oss \
	--without-sndio \
	--without-aac \
	\
	--without-mp3 \
	\
	--with-bdb-dir=%_prefix \
	--with-alsa \
	--with-jack \
	--with-magic \
	--with-ncurses \
	--without-ncursesw \
	--with-samplerate \
	--with-ffmpeg \
	--with-flac \
	--with-modplug \
	--with-musepack \
	--with-rcc \
	--with-sndfile \
	--with-speex\
	--with-timidity\
	--with-vorbis \
	--with-wavpack \
	--with-curl \
	--disable-static
make %{?_smp_mflags}

%install
%make_install
# Stupid libtool files
rm -rf %{buildroot}%{_libdir}/moc/decoder_plugins/*.la
# Someday people will honor docdir...
rm -rf %{buildroot}%{_datadir}/doc/moc/

%files
%defattr(0644,root,root,0755)
%license COPYING
%doc AUTHORS NEWS README TODO config.example keymap.example
%attr(0755,-,-) %{_bindir}/mocp
%{_mandir}/man1/mocp.1*
%{_libdir}/moc/
%{_datadir}/moc/

%changelog
