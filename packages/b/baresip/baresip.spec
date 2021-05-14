#
# spec file for package baresip
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           baresip
Version:        1.1.0
Release:        0
Summary:        Modular SIP useragent
License:        BSD-3-Clause
Group:          Productivity/Telephony/SIP/Clients
URL:            https://github.com/baresip/baresip
Source:         %{URL}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ilbc-devel
BuildRequires:  jack-devel
BuildRequires:  libgsm-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(codec2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-net-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libre) >= 2.0
BuildRequires:  pkgconfig(librem) >= 1.0
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(spandsp)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(vpx)
Recommends:     baresip-video

%description
A modular SIP user-agent
with support for audio and video, and many IETF standards
such as SIP, SDP, RTP/RTCP, STUN, TURN, and ICE.

Supports both IPv4 and IPv6, and the following features.
 * Audio codecs: AMR, G.711, G.722, G.726, GSM, L16, MPA, OPUS.
 * Video codecs: H.263, H.264, H.265, MPEG4, VP8, VP9.
 * Audio drivers: Alsa, GStreamer, JACK, OSS, Portaudio, sndio.
 * Video sources: FFmpeg avformat, Video4Linux2, X11 Grabber.
 * Video output: SDL2, X11, DirectFB.
 * NAT Traversal: STUN, TURN, ICE, NATBD, NAT-PMP, PCP.
 * Media encryption: SRTP, DTLS-SRTP.
 * DNS Service Discovery: Avahi.
 * Telemetry messaging: MQTT.
 * Control interfaces: JSON-over-TCP.

%package        video
Summary:        Video support for the Baresip useragent
Group:          Productivity/Telephony/SIP/Clients
Requires:       %{name} = %{version}

%description   video
A modular SIP user-agent
with support for audio and video, and many IETF standards
such as SIP, SDP, RTP/RTCP, STUN, TURN, and ICE.

Supports both IPv4 and IPv6, and the following features.
 * Audio codecs: AMR, G.711, G.722, G.726, GSM, L16, MPA, OPUS.
 * Video codecs: H.263, H.264, H.265, MPEG4, VP8, VP9.
 * Audio drivers: Alsa, GStreamer, JACK, OSS, Portaudio, sndio.
 * Video sources: FFmpeg avformat, Video4Linux2, X11 Grabber.
 * Video output: SDL2, X11, DirectFB.
 * NAT Traversal: STUN, TURN, ICE, NATBD, NAT-PMP, PCP.
 * Media encryption: SRTP, DTLS-SRTP.
 * DNS Service Discovery: Avahi.
 * Telemetry messaging: MQTT.
 * Control interfaces: JSON-over-TCP.

This subpackage provides the modules that are needed for video
support.

%prep
%setup -q
mv modules/mqtt/README.md README.mqtt
sed 's|/usr/local/lib|%{_libdir}/|g' -i src/config.c
sed 's|/usr/local/lib|%{_libdir}/|g' -i docs/examples/config
sed 's|/usr/local/share|%{_datadir}/|g' -i docs/examples/config

%build
export CFLAGS="%{optflags} -fpie -I/usr/include/ffmpeg"
export LFLAGS="%{optflags} -pie"
%make_build \
    V=1 \
    RELEASE=1 \
    USE_TLS=1 \
    PREFIX=%{_prefix}/ \
    MOD_PATH="%{_libdir}/baresip/modules" \
    EXTRA_MODULES="avcodec avformat swscale" \

%install
%make_install LIBDIR=%{_libdir} EXTRA_MODULES="avcodec avformat swscale"

%files
%license docs/COPYING
%doc README.md README.mqtt docs/ChangeLog
%doc docs/examples
%{_bindir}/baresip
%{_datadir}/baresip
%dir %{_libdir}/baresip
%dir %{_libdir}/baresip/modules
%{_libdir}/baresip/modules/account.so
%{_libdir}/baresip/modules/alsa.so
%{_libdir}/baresip/modules/aubridge.so
%{_libdir}/baresip/modules/aufile.so
%{_libdir}/baresip/modules/ausine.so
%{_libdir}/baresip/modules/auloop.so
%{_libdir}/baresip/modules/b2bua.so
%{_libdir}/baresip/modules/codec2.so
%{_libdir}/baresip/modules/cons.so
%{_libdir}/baresip/modules/contact.so
%{_libdir}/baresip/modules/ctrl_dbus.so
%{_libdir}/baresip/modules/ctrl_tcp.so
%{_libdir}/baresip/modules/debug_cmd.so
%{_libdir}/baresip/modules/dtls_srtp.so
%{_libdir}/baresip/modules/ebuacip.so
%{_libdir}/baresip/modules/echo.so
%{_libdir}/baresip/modules/evdev.so
%{_libdir}/baresip/modules/g711.so
%{_libdir}/baresip/modules/g722.so
%{_libdir}/baresip/modules/g726.so
%{_libdir}/baresip/modules/gsm.so
%{_libdir}/baresip/modules/gtk.so
%{_libdir}/baresip/modules/httpd.so
%{_libdir}/baresip/modules/httpreq.so
%{_libdir}/baresip/modules/ice.so
%{_libdir}/baresip/modules/jack.so
%{_libdir}/baresip/modules/l16.so
%{_libdir}/baresip/modules/menu.so
%{_libdir}/baresip/modules/mixausrc.so
%{_libdir}/baresip/modules/multicast.so
%{_libdir}/baresip/modules/mwi.so
%{_libdir}/baresip/modules/natpmp.so
%{_libdir}/baresip/modules/opus.so
%{_libdir}/baresip/modules/opus_multistream.so
%{_libdir}/baresip/modules/oss.so
%{_libdir}/baresip/modules/plc.so
%{_libdir}/baresip/modules/presence.so
%{_libdir}/baresip/modules/pulse.so
%{_libdir}/baresip/modules/rtcpsummary.so
%{_libdir}/baresip/modules/serreg.so
%{_libdir}/baresip/modules/snapshot.so
%{_libdir}/baresip/modules/sndfile.so
%{_libdir}/baresip/modules/speex_pp.so
%{_libdir}/baresip/modules/srtp.so
%{_libdir}/baresip/modules/stdio.so
%{_libdir}/baresip/modules/stun.so
%{_libdir}/baresip/modules/syslog.so
%{_libdir}/baresip/modules/turn.so
%{_libdir}/baresip/modules/uuid.so
%{_libdir}/baresip/modules/vumeter.so

%files video
%{_libdir}/baresip/modules/avcodec.so
%{_libdir}/baresip/modules/avformat.so
%{_libdir}/baresip/modules/cairo.so
%{_libdir}/baresip/modules/fakevideo.so
%{_libdir}/baresip/modules/gst*
%{_libdir}/baresip/modules/sdl*
%{_libdir}/baresip/modules/selfview.so
%{_libdir}/baresip/modules/swscale.so
%{_libdir}/baresip/modules/v4l2.so
%{_libdir}/baresip/modules/v4l2_codec.so
%{_libdir}/baresip/modules/vidbridge.so
%{_libdir}/baresip/modules/vidinfo.so
%{_libdir}/baresip/modules/vidloop.so
%{_libdir}/baresip/modules/vp8.so
%{_libdir}/baresip/modules/vp9.so
%{_libdir}/baresip/modules/x11.so
%{_libdir}/baresip/modules/x11grab.so

%changelog
