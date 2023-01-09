#
# spec file for package baresip
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


Name:           baresip
Version:        2.10.0
Release:        0
Summary:        Modular SIP useragent
License:        BSD-3-Clause
Group:          Productivity/Telephony/SIP/Clients
URL:            https://github.com/baresip/baresip
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ilbc-devel
BuildRequires:  jack-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  sndio-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(codec2)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-net-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libmosquitto)
BuildRequires:  pkgconfig(libmp3lame)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libre) >= 2.10.0
BuildRequires:  pkgconfig(librem) >= 2.10.0
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(spandsp)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(webrtc-audio-processing)
Recommends:     baresip-devel
Recommends:     baresip-video

%description
A modular SIP user-agent
with support for audio and video, and many IETF standards
such as SIP, SDP, RTP/RTCP, STUN, TURN, and ICE.

Supports both IPv4 and IPv6, and the following features.
 * Audio codecs: AMR, G.711, G.722, G.726, GSM, L16, MPA, OPUS.
 * Video codecs: H.263, H.264, H.265, MPEG4, VP8, VP9.
 * Audio drivers: Alsa, JACK, OSS, Portaudio, sndio.
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
 * Audio drivers: Alsa, JACK, OSS, Portaudio, sndio.
 * Video sources: FFmpeg avformat, Video4Linux2, X11 Grabber.
 * Video output: SDL2, X11, DirectFB.
 * NAT Traversal: STUN, TURN, ICE, NATBD, NAT-PMP, PCP.
 * Media encryption: SRTP, DTLS-SRTP.
 * DNS Service Discovery: Avahi.
 * Telemetry messaging: MQTT.
 * Control interfaces: JSON-over-TCP.

This subpackage provides the modules that are needed for video
support.

%package devel
Summary:        Development files for the baresip library
Requires:       libbaresip2 = %{version}-%{release}
Requires:       pkgconfig

%description devel
The baresip-devel package includes header files and libraries necessary
for developing programs which use the baresip C library.

%package -n libbaresip2
Summary:        Standard library for baresip
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description -n libbaresip2
This package contains the shared library needed to run programs compiled with
baresip

%prep
%setup -q
mv modules/mqtt/README.md README.mqtt
sed 's|/usr/local/lib|%{_libdir}/|g' -i src/config.c
sed 's|/usr/local/lib|%{_libdir}/|g' -i docs/examples/config
sed 's|/usr/local/share|%{_datadir}/|g' -i docs/examples/config

%build
%cmake \
	-DCMAKE_SKIP_BUILD_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install

%post   -n libbaresip2 -p /sbin/ldconfig
%postun -n libbaresip2 -p /sbin/ldconfig

%files
%license LICENSE
%doc CHANGELOG.md README.md README.mqtt
%doc docs/examples
%{_bindir}/baresip
%{_datadir}/baresip
%dir %{_libdir}/baresip
%dir %{_libdir}/baresip/modules
%{_libdir}/baresip/modules/aac.so
%{_libdir}/baresip/modules/account.so
%{_libdir}/baresip/modules/alsa.so
%{_libdir}/baresip/modules/aubridge.so
%{_libdir}/baresip/modules/auconv.so
%{_libdir}/baresip/modules/aufile.so
%{_libdir}/baresip/modules/auresamp.so
%{_libdir}/baresip/modules/ausine.so
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
%{_libdir}/baresip/modules/gtk.so
%{_libdir}/baresip/modules/httpd.so
%{_libdir}/baresip/modules/httpreq.so
%{_libdir}/baresip/modules/ice.so
%{_libdir}/baresip/modules/jack.so
%{_libdir}/baresip/modules/l16.so
%{_libdir}/baresip/modules/menu.so
%{_libdir}/baresip/modules/mixausrc.so
%{_libdir}/baresip/modules/mixminus.so
%{_libdir}/baresip/modules/mpa.so
%{_libdir}/baresip/modules/mqtt.so
%{_libdir}/baresip/modules/multicast.so
%{_libdir}/baresip/modules/mwi.so
%{_libdir}/baresip/modules/natpmp.so
%{_libdir}/baresip/modules/netroam.so
%{_libdir}/baresip/modules/opus.so
%{_libdir}/baresip/modules/opus_multistream.so
%{_libdir}/baresip/modules/pcp.so
%{_libdir}/baresip/modules/plc.so
%{_libdir}/baresip/modules/presence.so
%{_libdir}/baresip/modules/portaudio.so
%{_libdir}/baresip/modules/pulse.so
%{_libdir}/baresip/modules/pulse_async.so
%{_libdir}/baresip/modules/rtcpsummary.so
%{_libdir}/baresip/modules/serreg.so
%{_libdir}/baresip/modules/snapshot.so
%{_libdir}/baresip/modules/sndfile.so
%{_libdir}/baresip/modules/srtp.so
%{_libdir}/baresip/modules/stdio.so
%{_libdir}/baresip/modules/stun.so
%{_libdir}/baresip/modules/syslog.so
%{_libdir}/baresip/modules/turn.so
%{_libdir}/baresip/modules/uuid.so
%{_libdir}/baresip/modules/vumeter.so
%{_libdir}/baresip/modules/webrtc_aec.so

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/lib%{name}.pc

%files -n libbaresip2
%{_libdir}/lib%{name}.so.2*

%files video
%{_libdir}/baresip/modules/av1.so
%{_libdir}/baresip/modules/avfilter.so
%{_libdir}/baresip/modules/avcodec.so
%{_libdir}/baresip/modules/avformat.so
%{_libdir}/baresip/modules/fakevideo.so
%{_libdir}/baresip/modules/gst.so
%{_libdir}/baresip/modules/sdl.so
%{_libdir}/baresip/modules/selfview.so
%{_libdir}/baresip/modules/swscale.so
%{_libdir}/baresip/modules/vidbridge.so
%{_libdir}/baresip/modules/vidinfo.so
%{_libdir}/baresip/modules/vp8.so
%{_libdir}/baresip/modules/vp9.so
%{_libdir}/baresip/modules/x11.so

%changelog
