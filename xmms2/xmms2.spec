#
# spec file for package xmms2
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define codename DrO_o
%{!?python_sitelib:  %global python_sitelib  %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
# these macros are not defined under < 11.4, which ruby is 1.8-
%{!?rb_sitelibdir: %global rb_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}
%{!?rb_sitearchdir: %global rb_sitearchdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')}
%if 0%{?packman_bs}
%bcond_without restricted
%bcond_with cunit
%else
%bcond_with restricted
%if 0%{?suse_version} >= 1320
%bcond_without cunit
%else
%bcond_with cunit
%endif
%endif
%if 0%{?suse_version} >= 1120
%bcond_without gme
%bcond_with libsidplay
%else
%bcond_with gme
%bcond_without libsidplay
%endif
Name:           xmms2
Version:        0.8
Release:        0
Summary:        A modular audio framework and plugin architecture
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Players
URL:            http://xmms2.org
# TODO: Make sure to update the verison number in xmms2-pkgconfig.patch.
Source0:        http://prdownloads.sourceforge.net/xmms2/xmms2-%{version}%{codename}.tar.bz2
Source1:        xmms2-client-launcher.sh
Source2:        README.SUSE
Source3:        %{name}-ripper.1
# Don't add extra CFLAGS, we're smart enough, thanks.
Patch0:         %{name}-0.8-no-O0.patch
# Remove rpath in sid plugin
Patch4:         %{name}-0.8-rpath.patch
Patch6:         %{name}-0.8-spelling-error.patch
# Add -as-needed flag
Patch9:         %{name}-0.8-linker-flags.patch
Patch10:        %{name}-0.8-fix-cast-error.patch
# PATCH-FIX-UPSTREAM xmms2-pkgconfig.patch dimstar@opensuse.org -- pkg-config Version field contains illegal characters.
Patch13:        xmms2-pkgconfig.patch
Patch14:        %{name}-0.8-fixwarnings.patch
Patch17:        xmms-airplay-openssl11.patch
BuildRequires:  SDL-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  avahi-compat-mDNSResponder-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  flac-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libao-devel
BuildRequires:  libavahi-glib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdiscid-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libofa-devel
BuildRequires:  libogg-devel
BuildRequires:  libpulse-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libshout-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvisual-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  pyrex
BuildRequires:  python-devel
BuildRequires:  python-xml
BuildRequires:  readline-devel
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  speex-devel
BuildRequires:  sqlite-devel
BuildRequires:  wavpack-devel
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
Requires:       %{name}-plugin-base
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if 0%{?suse_version} > 1140
# Add vorbis and ogg to build env
Patch15:        %{name}-0.8-add-lib-vorbis-and-ogg.patch
%endif
%if 0%{?suse_version} >= 1310
# PATCH-PACKMAN-FIX adjust samba-4.0 include path for libsmbclient.h
Patch16:        %{name}-samba4-include-path.patch
%endif
%if 0%{?suse_version} > 1140
# for libcdio_cdda1
BuildRequires:  libcdio-paranoia-devel
%endif
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le %{arm} aarch64
BuildRequires:  valgrind-devel
%endif
%if %{with libsidplay}
%if 0%{?suse_version} >= 1120
BuildRequires:  sidplay-libs-devel >= 2.0
%else
BuildRequires:  libsidplay-devel >= 2.0
%endif
%endif
%if %{with cunit}
BuildRequires:  cunit-devel
%endif
%if 0%{?suse_version} >= 1120 && %{with gme}
BuildRequires:  libgme-devel
%endif
%if %{with restricted}
BuildRequires:  libfaad-devel
BuildRequires:  libmms-devel
BuildRequires:  libmpg123-devel
%endif

%description
XMMS2 is an audio framework, but it is not a general multimedia player - it
will not play videos. It has a modular framework and plugin architecture for
audio processing, visualisation and output, but this framework has not been
designed to support video. Also the client-server design of XMMS2 (and the
daemon being independent of any graphics output) practically prevents direct
video output being implemented. It has support for a wide range of audio
formats, which is expandable via plugins. It includes a basic CLI interface
to the XMMS2 framework, but most users will want to install a graphical XMMS2
client (such as gxmms2 or esperanza).

%package -n libxmmsclient++-glib1
Summary:        Glib C++ client library for %{name}
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Players

%description -n libxmmsclient++-glib1
A simple glib c++ client library for XMMS2.

%package -n libxmmsclient++4
Summary:        C++ client library for %{name}
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Players

%description -n libxmmsclient++4
A simple C++ client library for XMMS2.

%package -n libxmmsclient-glib1
Summary:        Glib Client library for %{name}
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Players

%description -n libxmmsclient-glib1
A simple Glib client library for XMMS2.

%package -n libxmmsclient6
Summary:        Client library for %{name}
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Players

%description -n libxmmsclient6
A simple client library for XMMS2.

%package devel
Summary:        Development libraries and headers for XMMS2
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libxmmsclient++-glib1
Requires:       libxmmsclient++4
Requires:       libxmmsclient-glib1
Requires:       libxmmsclient6
Requires:       pkgconfig
Requires:       pkgconfig(glib-2.0)
%if 0%{?suse_version} > 1325
Requires:       libboost_headers-devel
%else
Requires:       boost-devel
%endif

%description devel
Development libraries and headers for XMMS2. You probably need this to develop
or build new plugins for XMMS2.

%package docs
Summary:        Development documentation for XMMS2
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description docs
API documentation for the XMMS2 modular audio framework architecture.

%package -n python-xmms2
Summary:        Python support for XMMS2
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python

%description -n python-xmms2
Python bindings for XMMS2.

%package perl
Summary:        Perl support for XMMS2
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Languages/Perl
Requires:       %{name} = %{version}
Requires:       perl-base

%description perl
Perl bindings for XMMS2.

%package ruby
Summary:        Ruby support for XMMS2
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}
Requires:       ruby >= 1.8

%description ruby
Ruby bindings for XMMS2.

%package plugin-base
Summary:        Base plugins for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-base
Contains the basic plugins for XMMS2, such as:
* Playlist support: PLS, RSS, XSPF
* Sound output: ALSA, WAV disk writer, OSS
* Sound effects: Equalizer, Replay Gain

%package plugin-airplay
Summary:        Airplay support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-airplay
The Airport Express output plugin for XMMS2.

%package plugin-ao
Summary:        libao support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-ao
This plugin lets XMMS2 output via libao, a cross-platform
audio output library.

%package plugin-apefile
Summary:        Apefile support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-apefile
An XMMS2 demuxer plugin to parse Monkey Audio streams (.ape files).

%package plugin-asf
Summary:        ASF support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-asf
An XMMS2 demuxer plugin to parse the Advanced Systems Format (.asf files).

%package plugin-asx
Summary:        ASX support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-asx
An XMMS2 playlist plugin to read Advanced Stream Redirector (.asx) files.

%if 0%{?suse_version} > 1140
%package plugin-cdda
Summary:        CD-DA support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-cdda
An XMMS2 transport plugin to read Red Book standard audio discs.
%endif

%package plugin-cue
Summary:        CUE support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-cue
An XMMS2 playlist plugin to parse CUE sheets (.cue files).

%package plugin-curl
Summary:        Curl support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-curl
An XMMS2 transport plugin adding support for opening HTTP and FTP URLs.

%package plugin-daap
Summary:        DAAP support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-daap
An XMMS2 plugin to access iTunes (DAAP) music shares.

%package plugin-flac
Summary:        FLAC support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-flac
An XMMS2 input plugin to read ".flac" (Free Lossless Audio Codec) files.

%package plugin-flv
Summary:        FLV support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-flv
An XMMS2 input plugin to parse FLV containers for audio streams.

%package plugin-gvfs
Summary:        Gnome VFS support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-gvfs
An XMMS2 transport plugin to access files through the Gnome VFS API.

%if 0%{?suse_version} >= 1120
%if %{with gme}
%package plugin-gme
Summary:        GME support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-gme
An XMMS2 input plugin to read certain game music files
(.ay, .gbs, .gym, .nsf, .nsfe, .sap, .spc, .vgm).
%endif
%endif

%package plugin-html
Summary:        HTML support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-html
An XMMS2 playlist plugin to parse HTML playlists.

%package plugin-ices
Summary:        Icecast support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-ices
An XMMS2 output plugin to stream to an Icecast server.

%package plugin-icymetaint
Summary:        ICY stream support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-icymetaint
An XMMS2 transformation plugin to parse ICY/Shoutcast metadata from
audio streams.

%package plugin-id3v2
Summary:        ID3v2 support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-id3v2
An XMMS2 transformation plugin to parse ID3v2 metadata from MPEG
audio files.

%package plugin-jack
Summary:        Jack support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-jack
An XMMS2 output plugin for the Jack audio server.

%package plugin-karaoke
Summary:        Karaoke support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-karaoke
Voice removal effect plugin for XMMS2.

%package plugin-m3u
Summary:        M3U support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-m3u
An XMMS2 playlist plugin to parse .m3u playlists.

%package plugin-modplug
Summary:        Modplug support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-modplug
An XMMS2 input plugin to read and decode module files
(.it, .s3m, .xm, etc.)

%package plugin-mp4
Summary:        MPEG-4 container support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-mp4
An XMMS2 demuxer plugin to read .mp4 containers (MPEG-4 Part 14).

%package plugin-musepack
Summary:        Musepack support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-musepack
XMMS2 input plugin to decode Musepack.

%package plugin-normalize
Summary:        Volume normalization plugin for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-normalize
An XMMS2 transformation plugin that normalizes volume.

%package plugin-ofa
Summary:        Open Fingerprint support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-ofa
An XMMS2 plugin to support the Open Fingerprint Architecture.

%package plugin-pulse
Summary:        PulseAudio support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-pulse
An XMMS2 output plugin for PulseAudio.

%package plugin-samba
Summary:        SMB/CIFS support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-samba
An XMMS2 transport plugin adding support for accessing SMB/CIFS file shares.

%package plugin-sndfile
Summary:        libsndfile integration for %{name}
License:        GPL-2.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-sndfile
An XMMS2 input plugin to decode audio through libsndfile.

%package plugin-speex
Summary:        Speex support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-speex
An XMMS2 input plugin to read Speex-encoded files.

%package plugin-tta
Summary:        True Audio Codec support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-tta
An XMMS2 plugin to parse the True Audio Codec TTA file format.

%package plugin-vocoder
Summary:        Vocoder support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-vocoder
The XMMS2 Vocoder effect plugin.

%package plugin-wave
Summary:        RIFF support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-wave
An XMMS2 input plugin to parse RIFF containers with either
MP3 or WAVE data.

%package plugin-wavpack
Summary:        Wavpack support for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-wavpack
An XMMS2 decoder plugin for the Wavpack format.

%if %{with restricted}
%package plugin-restricted
Summary:        Restricted plugins for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugin-restricted
A set of XMMS2 decoder plugins for AAC (through libfaad), MMS and
MPEG-1 Layer 3 (through libmpg123).
%endif

%prep
%setup -q -n %{name}-%{version}%{codename}
%patch0 -p1
%patch4 -p1
%patch6 -p1
%patch9 -p1
%patch10 -p1
%patch13 -p1
%patch14 -p1
%if 0%{?suse_version} > 1140
%patch15 -p1
%endif
%if 0%{?suse_version} >= 1310
%patch16 -p1
%endif
%patch17 -p1
# unpack waf first to patch for ruby 2.2
./waf --help &> /dev/null
mv .waf-*/waflib .
# remove bytecompiled
find waflib -name "*.pyc" -delete
rm -rf .waf-*
# remove bz from waf executable
sed -i '/^#==>$/,$d' waf
# patch for ruby 2.2
%if 0%{?suse_version} > 1320
sed -i "s/Config::CONFIG/RbConfig::CONFIG/" waflib/Tools/ruby.py
%endif

# This header doesn't need to be executable
chmod -x src/include/xmmsclient/xmmsclient++/dict.h

%build
cp %{SOURCE2} .
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--with-perl-archdir=%{perl_archlib} \
	--with-ruby-archdir=%{rb_sitearchdir} \
	--with-ruby-libdir=%{rb_sitelibdir} \
	--with-pkgconfigdir=%{_libdir}/pkgconfig
./waf build -v %{?_smp_mflags}
# make the docs
doxygen

%install
./waf install \
	--destdir=%{buildroot} \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--with-ruby-archdir=%{rb_sitearchdir} \
	--with-ruby-libdir=%{rb_sitelibdir} \
	--with-perl-archdir=%{perl_archlib} \
	--with-pkgconfigdir=%{_libdir}/pkgconfig
# Convert to utf-8
for i in %{buildroot}%{_mandir}/man1/*.gz; do
	gunzip $i;
done
for i in %{buildroot}%{_mandir}/man1/*.1; do
	iconv -o $i.iso88591 -f iso88591 -t utf8 $i
	mv $i.iso88591 $i
done
install -m0755 %{SOURCE1} %{buildroot}%{_bindir}

#the libraries are built as 64bit, they are just installed in the wrong dir
%if "%{_lib}" == "lib64"
mv %{buildroot}%{_libexecdir}/* %{buildroot}/%{_libdir}/
mv %{buildroot}/%{_libdir}/perl* %{buildroot}%{_libexecdir}/
%endif

cp %{SOURCE3} %{buildroot}/%{_mandir}/man1/
%fdupes %{buildroot}

%post -n libxmmsclient++-glib1 -p /sbin/ldconfig
%postun -n libxmmsclient++-glib1 -p /sbin/ldconfig
%post -n libxmmsclient++4 -p /sbin/ldconfig
%postun -n libxmmsclient++4 -p /sbin/ldconfig
%post -n libxmmsclient-glib1 -p /sbin/ldconfig
%postun -n libxmmsclient-glib1 -p /sbin/ldconfig
%post -n libxmmsclient6 -p /sbin/ldconfig
%postun -n libxmmsclient6 -p /sbin/ldconfig

%files
%license COPYING COPYING.GPL COPYING.LGPL
%doc AUTHORS README TODO README.SUSE
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_mandir}/man1/*.gz
%{_datadir}/pixmaps/*
%{_datadir}/%{name}

%files -n libxmmsclient++-glib1
%{_libdir}/libxmmsclient++-glib.so.1
%{_libdir}/libxmmsclient++-glib.so.1.0.0

%files -n libxmmsclient++4
%{_libdir}/libxmmsclient++.so.4
%{_libdir}/libxmmsclient++.so.4.0.0

%files -n libxmmsclient-glib1
%{_libdir}/libxmmsclient-glib.so.1
%{_libdir}/libxmmsclient-glib.so.1.0.0

%files -n libxmmsclient6
%{_libdir}/libxmmsclient.so.6
%{_libdir}/libxmmsclient.so.6.0.0

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/libxmmsclient*.so
%{_libdir}/pkgconfig/%{name}-*.pc

%files docs
%doc doc/xmms2/html

%files perl
%{perl_archlib}/Audio/
%{perl_archlib}/auto/Audio/

%files -n python-xmms2
%dir %{python_sitearch}/xmmsclient/
%{python_sitearch}/xmmsclient/*

%files ruby
%{rb_sitearchdir}/*.so
%{rb_sitelibdir}/xmmsclient
%{rb_sitelibdir}/xmmsclient.rb

%files plugin-base
%{_libdir}/xmms2/libxmms_alsa.so
%{_libdir}/xmms2/libxmms_diskwrite.so
%{_libdir}/xmms2/libxmms_equalizer.so
%{_libdir}/xmms2/libxmms_file.so
%{_libdir}/xmms2/libxmms_xml.so
%{_libdir}/xmms2/libxmms_vorbis.so
%{_libdir}/xmms2/libxmms_null.so
%{_libdir}/xmms2/libxmms_nulstripper.so
%{_libdir}/xmms2/libxmms_oss.so
%{_libdir}/xmms2/libxmms_pls.so
%{_libdir}/xmms2/libxmms_replaygain.so
%{_libdir}/xmms2/libxmms_rss.so
%{_libdir}/xmms2/libxmms_xspf.so
%if 0%{?suse_version} >= 1330
%{_libdir}/xmms2/libxmms_mpg123.so
%endif

%files plugin-airplay
%{_libdir}/xmms2/libxmms_airplay.so

%files plugin-ao
%{_libdir}/xmms2/libxmms_ao.so

%files plugin-apefile
%{_libdir}/xmms2/libxmms_apefile.so

%files plugin-asf
%{_libdir}/xmms2/libxmms_asf.so

%files plugin-asx
%{_libdir}/xmms2/libxmms_asx.so

%if 0%{?suse_version} > 1140
%files plugin-cdda
%{_libdir}/xmms2/libxmms_cdda.so
%endif

%files plugin-cue
%{_libdir}/xmms2/libxmms_cue.so

%files plugin-curl
%{_libdir}/xmms2/libxmms_curl.so

%files plugin-daap
%{_libdir}/xmms2/libxmms_daap.so

%files plugin-flac
%{_libdir}/xmms2/libxmms_flac.so

%files plugin-flv
%{_libdir}/xmms2/libxmms_flv.so

%files plugin-gvfs
%{_libdir}/xmms2/libxmms_gvfs.so

%if 0%{?suse_version} >= 1120
%if %{with gme}
%files plugin-gme
%{_libdir}/xmms2/libxmms_gme.so
%endif
%endif

%files plugin-html
%{_libdir}/xmms2/libxmms_html.so

%files plugin-ices
%{_libdir}/xmms2/libxmms_ices.so

%files plugin-icymetaint
%{_libdir}/xmms2/libxmms_icymetaint.so

%files plugin-id3v2
%{_libdir}/xmms2/libxmms_id3v2.so

%files plugin-jack
%{_libdir}/xmms2/libxmms_jack.so

%files plugin-karaoke
%{_libdir}/xmms2/libxmms_karaoke.so

%files plugin-m3u
%{_libdir}/xmms2/libxmms_m3u.so

%files plugin-modplug
%{_libdir}/xmms2/libxmms_modplug.so

%files plugin-mp4
%{_libdir}/xmms2/libxmms_mp4.so

%files plugin-musepack
%{_libdir}/xmms2/libxmms_musepack.so

%files plugin-normalize
%{_libdir}/xmms2/libxmms_normalize.so

%files plugin-ofa
%{_libdir}/xmms2/libxmms_ofa.so

%files plugin-pulse
%{_libdir}/xmms2/libxmms_pulse.so

%files plugin-samba
%{_libdir}/xmms2/libxmms_samba.so

%files plugin-sndfile
%{_libdir}/xmms2/libxmms_sndfile.so

%files plugin-speex
%{_libdir}/xmms2/libxmms_speex.so

%files plugin-tta
%{_libdir}/xmms2/libxmms_tta.so

%files plugin-vocoder
%{_libdir}/xmms2/libxmms_vocoder.so

%files plugin-wave
%{_libdir}/xmms2/libxmms_wave.so

%files plugin-wavpack
%{_libdir}/xmms2/libxmms_wavpack.so

%if %{with restricted}
%files plugin-restricted
%{_libdir}/xmms2/libxmms_faad.so
%{_libdir}/xmms2/libxmms_mms.so
%if 0%{?suse_version} < 1330
%{_libdir}/xmms2/libxmms_mpg123.so
%endif
%endif

%changelog
