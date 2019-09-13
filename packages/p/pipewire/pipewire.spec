#
# spec file for package pipewire
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Luciano Santos, luc14n0@linuxmail.org.
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


%define libpipewire libpipewire-0_2-1
%define apiver 0.2
%define spa_ver 0.1

Name:           pipewire
Version:        0.2.6
Release:        0
Summary:        A Multimedia Framework designed to be an audio and video server and more
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://pipewire.org/
Source0:        https://github.com/PipeWire/pipewire/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-allocators-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(jack) >= 1.9.10
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(sbc)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)
Requires:       %{libpipewire} = %{version}
Requires:       %{name}-modules = %{version}
Requires:       %{name}-spa-tools = %{version}
Requires:       %{name}-tools = %{version}
Recommends:     %{name}-spa-plugins = %{version}

%description
PipeWire is a server and user space API to deal with multimedia pipelines.

Some of its features include:

 * Capture and playback of audio and video with minimal latency;
 * Real-time Multimedia processing on audio and video;
 * Multiprocess architecture to let applications share multimedia content;
 * GStreamer plugins for easy use and integration in current applications;
 * Sandboxed applications support.

%package -n %{libpipewire}
Summary:        A Multimedia Framework designed to be an audio and video server and more
Group:          System/Libraries

%description -n %{libpipewire}
PipeWire is a server and user space API to deal with multimedia pipelines.

Some of its features include:

 * Capture and playback of audio and video with minimal latency;
 * Real-time Multimedia processing on audio and video;
 * Multiprocess architecture to let applications share multimedia content;
 * GStreamer plugins for easy use and integration in current applications;
 * Sandboxed applications support.

This package provides the PipeWire shared library.

%package -n gstreamer-plugin-pipewire
Summary:        Gstreamer Plugin for PipeWire
Group:          System/Libraries

%description -n gstreamer-plugin-pipewire
PipeWire is a server and user space API to deal with multimedia pipelines.

This package provides the gstreamer plugin.

%package tools
Summary:        The PipeWire Tools
Group:          Productivity/Multimedia/Other

%description tools
SPA or Simple Plugin API is a plugin API.

This package provides pipewire-cli and pipewire-monitor tools.

%package spa-tools
Summary:        The PipeWire SPA Tools
Group:          Productivity/Multimedia/Other

%description spa-tools
SPA or Simple Plugin API is a plugin API.

This package provides spa-inspect and spa-monitor tools.

%package modules
Summary:        Modules For PipeWire, A Multimedia Framework
Group:          Productivity/Multimedia/Other
Requires:       pipewire

%description modules
PipeWire is a server and user space API to deal with multimedia pipelines.

The framework is used to build a modular daemon that can be configured to:

 * Be a low-latency audio server with features like pulseaudio and/or jack;
 * A video capture server that can manage hardware video capture devices
   and provide access to them;
 * A central hub where video can be made available for other applications
   such as the gnome-shell screencast API.

%package spa-plugins
Summary:        Plugins For PipeWire SPA
Group:          Productivity/Multimedia/Other
Requires:       pipewire

%description spa-plugins
PipeWire is a server and user space API to deal with multimedia pipelines.

Some of its features include:

 * Unlimited input/output ports;
 * Per port format enumeration and negotiation;
 * Enumeration/configuration of per port parameters;
 * Application controlled buffer allocation with option to let the plugin
   Allocate memory;
 * Arbitrary buffer metadata;
 * Buffers are passed around by id which is very fast and avoids the need
   for refcounting;
 * Synchronous and asynchronous processing;
 * All api is designed to work without any allocations;
 * Arbirary input/output behaviour.

This package provides plugins for extending PipeWire SPA's functionality.

%package devel
Summary:        Development Files For PipeWire, A Multimedia Framework
Group:          Development/Libraries/C and C++
Requires:       %{libpipewire} >= %{version}

%description devel
PipeWire is a server and user space API to deal with multimedia pipelines.

This package provides all the necessary files for development with PipeWire

%prep
%autosetup -p1

%build
%meson \
	-Dgstreamer=enabled \
	-Dsystemd=true \
	%{nil}
%meson_build

%install
%meson_install

%post   -n %{libpipewire} -p /sbin/ldconfig
%postun -n %{libpipewire} -p /sbin/ldconfig

%files
%{_bindir}/pipewire
%{_userunitdir}/pipewire.service
%{_userunitdir}/pipewire.socket
%config %{_sysconfdir}/pipewire/pipewire.conf
%dir %{_sysconfdir}/pipewire

%files -n %{libpipewire}
%{_libdir}/libpipewire-%{apiver}.so.*

%files -n gstreamer-plugin-pipewire
%{_libdir}/gstreamer-1.0/libgstpipewire.so

%files tools
%{_bindir}/pipewire-cli
%{_bindir}/pipewire-monitor

%files spa-tools
%{_bindir}/spa-inspect
%{_bindir}/spa-monitor

%files modules
%dir %{_libdir}/pipewire-%{apiver}
%{_libdir}/pipewire-%{apiver}/libpipewire-module-audio-dsp.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-autolink.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-client-node.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-portal.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-link-factory.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-mixer.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-protocol-native.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-rtkit.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-suspend-on-idle.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-spa-monitor.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-spa-node-factory.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-spa-node.so

%files spa-plugins
%{_libdir}/spa/alsa/libspa-alsa.so
%{_libdir}/spa/audiomixer/libspa-audiomixer.so
%{_libdir}/spa/audiotestsrc/libspa-audiotestsrc.so
%{_libdir}/spa/bluez5/libspa-bluez5.so
%{_libdir}/spa/ffmpeg/libspa-ffmpeg.so
%{_libdir}/spa/support/libspa-dbus.so
%{_libdir}/spa/support/libspa-support.so
%{_libdir}/spa/test/libspa-test.so
%{_libdir}/spa/v4l2/libspa-v4l2.so
%{_libdir}/spa/videotestsrc/libspa-videotestsrc.so
%{_libdir}/spa/volume/libspa-volume.so
%dir %{_libdir}/spa
%dir %{_libdir}/spa/alsa
%dir %{_libdir}/spa/audiomixer
%dir %{_libdir}/spa/audiotestsrc
%dir %{_libdir}/spa/bluez5
%dir %{_libdir}/spa/ffmpeg
%dir %{_libdir}/spa/support
%dir %{_libdir}/spa/test
%dir %{_libdir}/spa/v4l2
%dir %{_libdir}/spa/videotestsrc
%dir %{_libdir}/spa/volume

%files devel
%{_libdir}/libpipewire-%{apiver}.so
%{_libdir}/pkgconfig/libpipewire-%{apiver}.pc
%{_libdir}/pkgconfig/libspa-%{spa_ver}.pc
%{_includedir}/pipewire
%{_includedir}/spa

%changelog
