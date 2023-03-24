#
# spec file for package xine-lib
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


Name:           xine-lib
# %%bcond_with = default off
# %%bcond_without = default on
#
# --with distributable      -> don't build libxine2-codecs
# --without distributable   -> build libxine2-codecs
#
# default for buildservice is no patented codecs
%bcond_without distributable
%bcond_with onlynondistributable
%if 0%{?suse_version} > 1320
BuildRequires:  gcc
BuildRequires:  pkgconfig(libmpeg2)
%else
BuildRequires:  gcc8
%endif
%bcond_without sdl
%bcond_without jack
#
BuildRequires:  ImageMagick-devel
BuildRequires:  alsa-devel
BuildRequires:  flac-devel
BuildRequires:  giflib-devel
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  gtk2-devel
BuildRequires:  imlib2-devel
BuildRequires:  krb5-devel
BuildRequires:  libcdio-devel
BuildRequires:  libdrm-devel
BuildRequires:  libmng-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtool
BuildRequires:  libv4l-devel >= 0.8.4
BuildRequires:  libvorbis-devel
BuildRequires:  lirc-devel
BuildRequires:  perl
BuildRequires:  readline-devel
BuildRequires:  speex-devel
BuildRequires:  update-desktop-files
BuildRequires:  vcdimager-devel
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(liba52)
#Prevent building against ffmpeg 3
BuildRequires:  pkgconfig(libavcodec) >= 58
BuildRequires:  pkgconfig(libavformat) >= 58
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xv)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xvmc)
BuildRequires:  pkgconfig(zlib)
%if %{without distributable}
BuildRequires:  libfaad-devel
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdts)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-glx)
BuildRequires:  pkgconfig(vdpau)
%endif
BuildRequires:  libpulse-devel
%if %{with sdl}
BuildRequires:  pkgconfig(sdl)
%endif
%if %{with jack}
BuildRequires:  libjack-devel
%endif
BuildRequires:  libmodplug-devel
Version:        1.2.13
Release:        0
%define abiversion 2.11
Summary:        Video Player with Plug-Ins
License:        GPL-2.0-or-later AND SUSE-Public-Domain
Group:          Productivity/Multimedia/Video/Players
URL:            https://www.xine-project.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Source:         http://sourceforge.net/projects/xine/files/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        baselibs.conf

Patch0:         xine-lib-libdvdread_udf.diff
Patch1:         xine-lib-v4l-2.6.38.patch
# Add theora FOURCC to libxine I found an avi container that xine wouldn't play.
Patch4:         xine-lib-theora.patch

%description
<p>Great video and multimediaplayer, supports DVD, MPEG, AVI, DivX, VCD, Quicktime ...</p><p>You need a frontend for xine-lib like <a href=http://packman.links2linux.de/package/xine-ui>xine-ui</a>, <a href=http://packman.links2linux.de/package/gxine>gxine</a>, <a href=http://packman.links2linux.de/package/kaffeine>kaffeine</a> or <a href=http://packman.links2linux.de/package/totem>totem</a>.</p><p>Since 1-rc6 the package number is reduced, all you may miss, is in the base package</p><p>If you want to play css encrypted Video-DVD's, you need to install <a href=http://packman.links2linux.de/package/libdvdcss2>libdvdcss</a>.</p>

%description -l de
<p>Gro&szlig;artiger Video- und Multimediaplayer mit Support f&uuml;r DVD, MPEG, AVI, DivX, VCD,Quicktime ...</p><p>Bitte beachten Sie, dass Sie neben der xine-lib auch eine Bedienoberfl&auml;che wie <a href=http://packman.links2linux.de/package/xine-ui>xine-ui</a>, <a href=http://packman.links2linux.de/package/gxine>gxine</a>, <a href=http://packman.links2linux.de/package/kaffeine>kaffeine</a> oder <a href=http://packman.links2linux.de/package/totem>totem</a> ben&ouml;tigen.</p><p>Seit 1-rc6 wurde die Zahl der Pakete reduziert, alles was sie eventuell vermissen, wurde in das Basispaket integriert.</p><p>Wenn Sie css verschl&uuml;sselte Video-DVDs abspielen wollen, m&uuml;ssen Sie zus&auml;tzlich die <a href=http://packman.links2linux.de/package/libdvdcss2>libdvdcss</a> installieren.</p>

%package -n libxine2
Summary:        Video Player with Plug-Ins
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
Provides:       libxine2-syncfb = %{version}-%{release}
Obsoletes:      libxine2-syncfb < %{version}-%{release}
Provides:       libxine2-xvmc = %{version}-%{release}
Obsoletes:      libxine2-xvmc < %{version}-%{release}
Provides:       libxine2-dvb = %{version}-%{release}
Obsoletes:      libxine2-dvb < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}
Recommends:     libxine2-codecs = %{version}
Recommends:     opensuse-codecs-installer

%description -n libxine2
xine is a video player with a graphical front-end that supports a large
number of file formats (VCD and MPEG2, for example) using plug-ins.
Several plug-ins are included. Others can be installed after xine
installation. xine supports stereo sound using OSS and AC5.1 using
Alsa.

%if %{with distributable}
This version of xine may lack certain features because of legal
requirements (potential patent violation). See also
http://en.opensuse.org/XINE#Legal_Matters
%endif

More information about xine plug-ins can be found at
http://www.xine-project.org/home

Authors:
--------
    Guenter Bartsch <guenter@sourceforge.net>

%description -n libxine2 -l de
xine ist ein Videoplayer mit grafischem  Frontend und unterstützt
eine vielzahl an Dateiformaten (z.B. VCD und MPEG2) mit hilfe von
Plugins. Einige Plugins sind enthalten, andere können nach der
Installation von xine nachinstalliert werden. xine untersützt
Stereosound via OSS und AC5.1 per Alsa.

%if %{with distributable}
Diese xine-Version lässt eventuell einige Funktione aus rechtlichen
Gründen vermissen (mögliche Patentverletzungen). Siehe dazu
http://en.opensuse.org/XINE#Legal_Matters
%endif

Weitere Informationen über xine Plugins finden Sie unter
http://www.xine-project.org/home

Autoren:
--------
    Guenter Bartsch <guenter@sourceforge.net>

%package -n libxine-devel
Summary:        Development environment for xine-based media players
License:        GPL-2.0-or-later AND SUSE-Public-Domain
Group:          Development/Libraries/C and C++
Requires:       freetype2-devel
Requires:       glibc-devel
Requires:       libv4l-devel
Requires:       libxine2 = %{version}
Requires:       zlib-devel
Obsoletes:      libxine2-devel < %{version}-%{release}
Provides:       libxine2-devel = %{version}-%{release}
Obsoletes:      xine-lib2-devel < %{version}-%{release}
Provides:       xine-lib2-devel = %{version}-%{release}
Obsoletes:      xine-devel < %{version}-%{release}
Provides:       xine-devel = %{version}-%{release}

%description -n libxine-devel
This package contains all necessary include files, libraries and
configuration files needed to compile applications that use the xine
media player.

xine is a video player which supports a large number of file formats
(i.e., VCD, MPEG2) using plug-ins. Several plug-ins are included.
Others can be post-installed. Supports stereo sound using OSS and AC5.1
using Alsa.

%if %{with distributable}
This version of xine may lack certain features because of legal
requirements (potential patent violation). See also
http://en.opensuse.org/XINE#Legal_Matters
%endif

More information about xine plug-ins can be found at
http://www.xine-project.org/home

Authors:
--------
    Guenter Bartsch <guenter@users.sourceforge.net>

%description -n libxine-devel -l de
Dieses Paket enthält alle nötigen Include Dateien, Biblioteken und
Konfigurationsdateien, die benötigt werden, um Anwendungen zu
kompilieren, die den xine Media Player verwenden.

xine ist ein Videoplayer mit grafischem  Frontend und unterstützt
eine vielzahl an Dateiformaten (z.B. VCD und MPEG2) mit hilfe von
Plugins. Einige Plugins sind enthalten, andere können nach der
Installation von xine nachinstalliert werden. xine untersützt
Stereosound via OSS und AC5.1 per Alsa.

%if %{with distributable}
Diese xine-Version lässt eventuell einige Funktione aus rechtlichen
Gründen vermissen (mögliche Patentverletzungen). Siehe dazu
http://en.opensuse.org/XINE#Legal_Matters
%endif

Weitere Informationen über xine Plugins finden Sie unter
http://www.xine-project.org/home

Autoren:
--------
    Guenter Bartsch <guenter@sourceforge.net>

%package -n libxine2-pulse
Summary:        Pulseaudio plugin for xine
License:        GPL-2.0-or-later AND SUSE-Public-Domain
Group:          Productivity/Multimedia/Video/Players
Requires:       libxine2 = %{version}
Supplements:    packageand(libpulse0:libxine2)

%description -n libxine2-pulse
libxine sound output plugin for the pulseaudio soundserver



Authors:
--------
    Guenter Bartsch <guenter@users.sourceforge.net>

%description -n libxine2-pulse -l de
libxine Soundausgabeplugin für den Pulseaudio Soundserver



Autoren:
--------
    Guenter Bartsch <guenter@sourceforge.net>

%if %{with sdl}

%package -n libxine2-sdl
Summary:        SDL plugin for xine
License:        GPL-2.0-or-later AND SUSE-Public-Domain
Group:          Productivity/Multimedia/Video/Players
Requires:       libxine2 = %{version}

%description -n libxine2-sdl
SDL xine video output plugin



Authors:
--------
    Guenter Bartsch <guenter@users.sourceforge.net>

%description -n libxine2-sdl -l de
SDL xine Video-Ausgabeplugin



Autoren:
--------
    Guenter Bartsch <guenter@sourceforge.net>
%endif

%if %{with jack}

%package -n libxine2-jack
Summary:        Jack plugin for xine
License:        GPL-2.0-or-later AND SUSE-Public-Domain
Group:          Productivity/Multimedia/Video/Players
Requires:       libxine2 = %{version}

%description -n libxine2-jack
xine sound output plugin for the jack soundserver



Authors:
--------
    Guenter Bartsch <guenter@users.sourceforge.net>

%description -n libxine2-jack -l de
xine Soundausgabeplugin für den jack Soundserver



Autoren:
--------
    Guenter Bartsch <guenter@sourceforge.net>
%endif

%if %{without distributable}

%package -n libxine2-codecs
# these libs are possibly illegal and may not work without libdvdcss anyway
Summary:        Xine plugins for watching DVDs, DivX and more
License:        GPL-2.0-or-later AND SUSE-Public-Domain
Group:          Productivity/Multimedia/Video/Players
Requires:       libxine2 = %{version}
Provides:       libxine2-dvd = %{version}-%{release}
Obsoletes:      libxine2-dvd < %{version}-%{release}
Provides:       libxine2-dxr3 = %{version}-%{release}
Obsoletes:      libxine2-dxr3 < %{version}-%{release}
%ifarch %{ix86}
Provides:       libxine2-w32dll = %{version}-%{release}
Obsoletes:      libxine2-w32dll < %{version}-%{release}
%endif
Recommends:     libdvdcss2 >= 1.2.10

%description -n libxine2-codecs
With these xine plug-ins, you can watch DVDs and all other kind of
media using xine. More information about xine plug-ins can be found at
http://www.xine-project.org/home



Authors:
--------
    Guenter Bartsch <guenter@sourceforge.net>

%description -n libxine2-codecs -l de
Mit diesem xine Plugins können Sie DVDs und alle von xine unterstützten
Medienverainten abspielen. Weitere Informationtne über xine Plugins
finden Sie unter
http://www.xine-project.org/home



Autoren:
--------
    Guenter Bartsch <guenter@sourceforge.net>
%endif

%prep
%if %{with distributable} && %{with onlynondistributable}
%error need --without distributable for --with onlynondistributable
%endif
%autosetup -p1 -n %{name}.%{version}

%build
cat <<EOF
+++ rpm build options +++'
Distributable version:	%{with distributable}
%if %{without distributable}
  Codecs package only:	%{with onlynondistributable}
%endif
External ffmpeg:	1
Pulseaudio:		%{with pulseaudio}
SDL:			%{with sdl}
aalib:			0
esd:			0
jack:			%{with jack}
gnome_vfs:		0
directfb:		0
modplug:		%{with modplug}
+++++++++++++++++++++++++'
EOF
%if %{with distributable}
# Taken from precheckin_cripple_tarball.sh
# $1: files $2: entries $3: prefix $4: postfix
# NOTE: the perl do_nukeentry has stopped working with the latest perl
# I've left it here hoping someone will fix it. Thanks
# Don't forget to remove xine-lib-nukefaadetc.patch when the perl scripts are functioning again.

do_nukeentry() {
for d in $1 ; do
  perl -i -e 'undef $/; $_=<>; for $e (qw|'"$2"'|) { s|(?<=[^-a-zA-Z0-9_./])'"$3"'$e'"$4"'(?=[^-a-zA-Z0-9_./])||g }; print' ${d}
done
}

do_nukeentrynp() {
for i in ${2};do
  cat ${1}|grep -v ${i} >${1}n;mv ${1}n ${1}
done
}

# $1: files $2: entries $3: prefix $4: postfix
do_nukeline() {
for d in $1 ; do
  perl -i -e 'undef $/; $_=<>; for $e (qw|'"$2"'|) { s|^.*(?<=[^-a-zA-Z0-9_./])'"$3"'$e'"$4"'(?=[^-a-zA-Z0-9_./]).*$||mg }; print' $d
done
}

# $1: dir $2: files/dirs
do_remove() {
pushd "$1" >/dev/null || exit 1
rm -rf $2
popd >/dev/null
}

# Cripple source
#
# combined/ffmpeg
echo 1>&2 "Crippling..."

c_subdirs="faad planar dxr3 asf dmx_video libdts libfaad libffmpeg libspucc libspudec libspudvb libw32dll"
c_demuxers="group_video.c demux_elem.c xineplug_dmx_asf.la asfheader.h asfheader.c demux_asf.c xineplug_dmx_mpeg.la demux_mpeg.c xineplug_dmx_mpeg_block.la demux_mpeg_block.c xineplug_dmx_mpeg_ts.la demux_ts.c xineplug_dmx_mpeg_elem.la demux_elem.c xineplug_dmx_mpeg_pes.la demux_mpeg_pes.c xineplug_dmx_yuv4mpeg2.la demux_yuv4mpeg2.c"
c_input="xineplug_inp_mms.la input_mms.c mms.c mmsh.c ../demuxers/asfheader.c mms.h mmsh.h"
c_libxineadec="xineplug_decode_gsm610.la xineplug_decode_nsf.la gsm610.c nsf.c  gsm610 nosefart"
c_post="planar pp_module PLANAR"

do_nukeentry src/Makefile.am             "$c_subdirs"
do_nukeentry configure.ac                "$c_subdirs" "src/" "/[a-zA-Z0-9_./]*Makefile"
do_remove    src                         "$c_subdirs"
do_nukeentry src/demuxers/Makefile.am    "$c_subdirs"
do_nukeentry contrib/Makefile.am         "$c_subdirs"
do_nukeentry src/demuxers/Makefile.am    "$c_demuxers"
do_remove    src/demuxers                "$c_demuxers"
do_nukeentry src/input/Makefile.am       "$c_input"
do_remove    src/input                   "$c_input"
#do_nukeentry src/audio_dec/Makefile.am   "$c_audiodec"
#do_remove    src/audio_dec               "$c_audiodec"
#do_nukeentry src/combined/Makefile.am    "ffmpeg"
#do_remove    src/combined                "ffmpeg"
do_nukeentrynp src/post/Makefile.am       "$c_post"
#do_nukeline  src/post/planar/planar.c    "pp_init_plugin pp_special_info"
do_remove    src/post                     "planar"
sed -i 's@libfaad@@g' contrib/Makefile.am
%endif

rm -f m4/libtool15.m4
sed -i -e 's|/tmp/vdr-xine|/var/lib/vdr-xine|g' src/vdr/input_vdr.c

export CFLAGS="%{optflags} -fno-strict-aliasing -fno-force-addr `pkg-config --cflags smbclient`"
export CCASFLAGS=-Wa,--noexecstack
test -x "$(type -p gcc-7)" && export CC="$_"
test -x "$(type -p gcc-8)" && export CC="$_"
echo 'AC_DEFUN([AC_REQUIRE_AUX_FILE])dnl' >> acinclude.m4

#rm -f configure
#if [ ! -f configure ]; then
./autogen.sh noconfig
#else
#AUTOPOINT=true autoreconf -fi
#fi

%configure \
	--disable-rpath \
	--docdir=%{_defaultdocdir}/xine \
	--enable-antialiasing \
	--with-libflac \
	--with-freetype \
	--enable-v4l \
	--enable-modplug \
%if %{without sdl}
	--without-sdl \
%endif
%if %{with distributable}
	--disable-faad \
	--disable-vdpau \
	--disable-dxr3 \
	--disable-asf \
%else
        --enable-dxr3 \
%endif
%ifarch %{ix86}
	--with-w32-path=/usr/lib/win32 \
%endif
	--with-pic \
	--with-external-dvdnav
#	--disable-libxine-builtins
#	--with-install-plugins-helper=${_prefix}/lib/opensuse-codecs-installer
echo $CFLAGS
make %{?jobs:-j%{jobs}} V=1

%install
make install DESTDIR=%{buildroot}
LIB="%{buildroot}%{_libdir}/xine/plugins/%{abiversion}"
# install documentation
#install -m 0644 %%{SOURCE1} COPYING AUTHORS %%{buildroot}%%{_defaultdocdir}/xine/
# remove usless READMEs
rm %{buildroot}%{_defaultdocdir}/xine/README.{irix,solaris,WIN32}
# remove .la files, they are evil
rm %{buildroot}%{_libdir}/*.la
rm -f files
%ifarch %{ix86}
  mkdir -p %{buildroot}/usr/lib/win32
%endif
%if %{with distributable}
rm -rf %{buildroot}%{_libdir}/xine/plugins/%{abiversion}/post
rm -f %{buildroot}%{_libdir}/xine/plugins/%{abiversion}/xineplug_dmx_video.so
%endif
#
# big plugin sorting
 #
cat > plugins << EOF
# these plugins do not have legal problems
xineplug_tls_gnutls
xineplug_ao_out_alsa
xineplug_ao_out_oss
xineplug_vo_out_fb
xineplug_vo_gl_egl_x11
xineplug_vo_gl_glx
xineplug_vo_out_opengl
xineplug_vo_out_opengl2
xineplug_vo_out_xshm
xineplug_vo_out_xv
xineplug_vo_out_xcbshm
xineplug_vo_out_xcbxv
xineplug_vo_out_raw
xineplug_decode_mad
xineplug_decode_a52
xineplug_decode_to_spdif
%if %{without distributable}
xineplug_vo_out_vdpau
xineplug_vo_gl_egl_wl
%endif
xineplug_inp_dvb
xineplug_inp_dvd
xineplug_inp_v4l
xineplug_inp_v4l2
xineplug_inp_network
xineplug_inp_cdda
xineplug_inp_smb
xineplug_inp_pvr
xineplug_inp_rtp
#New in 1.2.7
xineplug_decode_rawvideo
xineplug_decode_libpng
%if %{without distributable}
xineplug_decode_vdpau
post/xineplug_post_audio_filters
post/xineplug_post_goom
post/xineplug_post_mosaico
post/xineplug_post_switch
post/xineplug_post_tvtime
post/xineplug_post_visualizations
xineplug_dmx_video
%endif
#end new
xineplug_decode_lpcm
xineplug_decode_real
xineplug_decode_mpc
xineplug_decode_gdk_pixbuf
xineplug_decode_spucmml
xineplug_decode_spuhdmv
xineplug_decode_libjpeg
xineplug_decode_image
xineplug_decode_libvpx
xineplug_dmx_audio
xineplug_dmx_image
xineplug_dmx_fli
xineplug_dmx_nsv
xineplug_dmx_mng
xineplug_dmx_pva
xineplug_dmx_games
xineplug_dmx_slave
xineplug_dmx_modplug
xineplug_dmx_playlist
xineplug_flac
xineplug_sputext
xineplug_xiph
xineplug_vdr
xineplug_vo_out_xxmc
xineplug_vo_out_xvmc
%ifarch %{ix86}
xineplug_vo_out_vidix
vidix/cyberblade_vid
vidix/mach64_vid
vidix/mga_crtc2_vid
vidix/mga_vid
vidix/nvidia_vid
vidix/pm2_vid
vidix/pm3_vid
vidix/radeon_vid
vidix/rage128_vid
vidix/savage_vid
vidix/sis_vid
vidix/unichrome_vid
%endif
#
.pulse
xineplug_ao_out_pulseaudio
#
.jack
xineplug_ao_out_jack
#
.sdl
xineplug_vo_out_sdl
#
#
.codecs
# libmad and MPEG related plugins
xineplug_decode_spudvb
xineplug_inp_vcd
xineplug_inp_vcdo
xineplug_decode_mpeg2
# these plugins do have legal problems
xineplug_decode_dts
xineplug_decode_faad
xineplug_decode_ff
xineplug_decode_dvaudio
xineplug_dmx_asf
xineplug_inp_mms
xineplug_inp_bluray
# I am not sure about these plugins, they need to be checked
# Closed Captioning Decoder (EIA-608). Patented ???
xineplug_decode_spucc
xineplug_decode_spu
# NES Music File Format. free ??
xineplug_nsf
# Philips claimed intellectual property on GSM 06.10
xineplug_decode_gsm610
%ifarch %{ix86}
xineplug_decode_w32dll
%endif
xineplug_dxr3
xineplug_vo_out_vaapi
xineplug_hw_frame_vaapi
xineplug_va_display_drm
xineplug_va_display_glx
xineplug_va_display_wl
xineplug_va_display_x11
# unfortunately using external ffmpeg links the planar post
# processing plugin against ffmpeg libs
post/xineplug_post_planar
#
EOF
#
OUT_FILE=""
grep -v ^# plugins | while read i; do
  [ "${i:0:1}" = "." ] && OUT_FILE=${i} && continue
  echo %{_libdir}/xine/plugins/%{abiversion}/${i}.so >> files${OUT_FILE}
done
%find_lang libxine2
cat libxine2.lang >>files
%if %{with distributable}
xargs -i+ rm -f %{buildroot}/+ <files.codecs
%else
%if 0%{?__debug_package}
# strip patent encumbered plugins to prevent their source from
# ending up in the debuginfo package
xargs -i+ strip --strip-debug %{buildroot}/+ <files.codecs
%endif
%endif
%if %{with onlynondistributable}
for i in files files.*; do
  test "$i" = 'files.codecs' || xargs -i+ rm -f %{buildroot}/+ < $i
done
rm -rf %{buildroot}/usr/share %{buildroot}/usr/bin
rm -rf %{buildroot}%{_defaultdocdir}/xine %{buildroot}/usr/include
rm -rf %{buildroot}/usr/lib/win32 %{buildroot}/%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_libdir}/xine/plugins/%{abiversion}/{vidix,mime.types}
rm -f  %{buildroot}%{_libdir}/libxine*
%endif
rm -rf %{buildroot}%{_mandir}/man5

%if %{without onlynondistributable}

%post -n libxine2 -p /sbin/ldconfig

%postun -n libxine2 -p /sbin/ldconfig

%files -n libxine2 -f files
%defattr(-,root,root)
%{_bindir}/xine-list-*
%ifarch %{ix86}
%dir /usr/lib/win32
%endif
%dir /%{_libdir}/xine
%dir /%{_libdir}/xine/plugins
%dir /%{_libdir}/xine/plugins/%{abiversion}
%dir /usr/share/xine-lib
%{_libdir}/libxine.so.*
%doc %{_mandir}/man1/xine-list-*.gz
#%%doc %%{_mandir}/man5/xine.*
%{_defaultdocdir}/xine
%if %{without distributable}
%dir %{_libdir}/xine/plugins/%{abiversion}/post
%endif
%{_libdir}/xine/plugins/%{abiversion}/mime.types
#
# xine fonts
# cetus is a freeware font from http://www.fontfreak.com/authors/gregfonts.htm
#
/usr/share/xine-lib/fonts
%ifarch %{ix86}
%dir %{_libdir}/xine/plugins/%{abiversion}/vidix
%endif

%files -n libxine2-pulse -f files.pulse
%defattr(-,root,root,0755)

%if %{with sdl}

%files -n libxine2-sdl -f files.sdl
%defattr(-,root,root,0755)
%endif

%if %{with jack}

%files -n libxine2-jack -f files.jack
%defattr(-,root,root,0755)
%endif

%files -n libxine-devel
%defattr(-,root,root)
%doc %{_mandir}/man1/xine-config.1.gz
/usr/bin/xine-config
%{_libdir}/pkgconfig/libxine.pc
%{_libdir}/libxine.so
/usr/share/aclocal/xine.m4
/usr/include/xine
/usr/include/xine.h
%endif
# onlynondistributable

%if %{without distributable}

%files -n libxine2-codecs -f files.codecs
%defattr(-,root,root)
%dir %{_libdir}/xine
%dir %{_libdir}/xine/plugins
%dir %{_libdir}/xine/plugins/%{abiversion}
%dir %{_libdir}/xine/plugins/%{abiversion}/post
%endif

%changelog
