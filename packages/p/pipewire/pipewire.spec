#
# spec file for package pipewire
#
# Copyright (c) 2020 SUSE LLC
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


%define libpipewire libpipewire-0_3-0
%define sover 0_3_1
%define apiver 0.3
%define spa_ver 0.2
%define spa_ver_str 0_2

Name:           pipewire
Version:        0.3.1+48
Release:        0
Summary:        A Multimedia Framework designed to be an audio and video server and more
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://pipewire.org/
Source0:        %{name}-%{version}.tar.xz
Patch0:         fix-memfd_create-call.patch

BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xmltoman
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bluez)
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
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(sbc)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
Requires:       %{libpipewire} = %{version}
Requires:       %{name}-modules = %{version}
Requires:       %{name}-spa-tools = %{version}
Requires:       %{name}-tools = %{version}
Recommends:     %{name}-spa-plugins-%{spa_ver_str} = %{version}

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

%package -n libjack-pw%{sover}
Summary:        A Multimedia Framework designed to be an audio and video server and more
Group:          Development/Libraries/C and C++

%description -n libjack-pw%{sover}
PipeWire is a server and user space API to deal with multimedia pipelines.

Some of its features include:

 * Capture and playback of audio and video with minimal latency;
 * Real-time Multimedia processing on audio and video;
 * Multiprocess architecture to let applications share multimedia content;
 * GStreamer plugins for easy use and integration in current applications;
 * Sandboxed applications support.

This package provides the PipeWire shared library.


%package -n libpulse-mainloop-glib-pw%{sover}
Summary:        A Multimedia Framework designed to be an audio and video server and more
Group:          Development/Libraries/C and C++

%description -n libpulse-mainloop-glib-pw%{sover}
PipeWire is a server and user space API to deal with multimedia pipelines.

Some of its features include:

 * Capture and playback of audio and video with minimal latency;
 * Real-time Multimedia processing on audio and video;
 * Multiprocess architecture to let applications share multimedia content;
 * GStreamer plugins for easy use and integration in current applications;
 * Sandboxed applications support.

This package provides the PipeWire shared library.

%package   -n libpulse-pw%{sover}
Summary:        A Multimedia Framework designed to be an audio and video server and more
Group:          Development/Libraries/C and C++

%description -n libpulse-pw%{sover}
PipeWire is a server and user space API to deal with multimedia pipelines.

Some of its features include:

 * Capture and playback of audio and video with minimal latency;
 * Real-time Multimedia processing on audio and video;
 * Multiprocess architecture to let applications share multimedia content;
 * GStreamer plugins for easy use and integration in current applications;
 * Sandboxed applications support.

This package provides the PipeWire shared library.

%package -n libpulse-simple-pw%{sover}
Summary:        A Multimedia Framework designed to be an audio and video server and more
Group:          Development/Libraries/C and C++

%description -n libpulse-simple-pw%{sover}
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

%package spa-plugins-%{spa_ver_str}
Summary:        Plugins For PipeWire SPA
Group:          Productivity/Multimedia/Other
Requires:       pipewire

%description spa-plugins-%{spa_ver_str}
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

%package doc
Summary:        PipeWire media server documentation
Group:          Development/Libraries/C and C++

%description doc
This package contains documentation for the PipeWire media server.

%prep
%setup
%if %{pkg_vcmp glibc < 2.27}
%patch0 -p1
%endif

%build
%meson \
	-Ddocs=true \
	-Dman=true \
	-Dgstreamer=true \
	-Dffmpeg=true \
	-Dsystemd=true \
	-Dvulkan=true \
	%{nil}
%meson_build

%install
%meson_install
%fdupes -s %{buildroot}/%{_datadir}/doc/pipewire/html

%check
%meson_test

%post   -n %{libpipewire} -p /sbin/ldconfig
%postun -n %{libpipewire} -p /sbin/ldconfig

%post   -n libjack-pw%{sover} -p /sbin/ldconfig
%postun -n libjack-pw%{sover} -p /sbin/ldconfig

%post   -n libpulse-mainloop-glib-pw%{sover} -p /sbin/ldconfig
%postun -n libpulse-mainloop-glib-pw%{sover} -p /sbin/ldconfig

%post   -n libpulse-pw%{sover} -p /sbin/ldconfig
%postun -n libpulse-pw%{sover} -p /sbin/ldconfig

%post   -n libpulse-simple-pw%{sover} -p /sbin/ldconfig
%postun -n libpulse-simple-pw%{sover} -p /sbin/ldconfig

%files
%{_bindir}/pipewire
%{_bindir}/pipewire-media-session
%{_userunitdir}/pipewire.service
%{_userunitdir}/pipewire.socket
%{_mandir}/man1/pipewire.1%{ext_man}
%{_mandir}/man5/pipewire.conf.5%{ext_man}

%dir %{_sysconfdir}/pipewire
%config %{_sysconfdir}/pipewire/pipewire.conf

%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_pcm_pipewire.so

%files -n %{libpipewire}
%license LICENSE COPYING
%doc README.md
%{_libdir}/libpipewire-%{apiver}.so.*

%files -n libjack-pw%{sover}
%{_libdir}/libjack-pw.so.*

%files -n libpulse-mainloop-glib-pw%{sover}
%{_libdir}/libpulse-mainloop-glib-pw.so.*

%files -n libpulse-pw%{sover}
%{_libdir}/libpulse-pw.so.*

%files -n libpulse-simple-pw%{sover}
%{_libdir}/libpulse-simple-pw.so.*

%files -n gstreamer-plugin-pipewire
%{_libdir}/gstreamer-1.0/libgstpipewire.so

%files tools
%{_bindir}/pw-cli
%{_bindir}/pw-dot
%{_bindir}/pw-mon
%{_bindir}/pw-profiler
%{_bindir}/pw-cat
%{_bindir}/pw-play
%{_bindir}/pw-record
%{_mandir}/man1/pw-cli.1%{ext_man}
%{_mandir}/man1/pw-mon.1%{ext_man}

%files spa-tools
%{_bindir}/spa-inspect
%{_bindir}/spa-monitor

%files modules
%dir %{_libdir}/pipewire-%{apiver}
%{_libdir}/pipewire-%{apiver}/libpipewire-module-access.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-adapter.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-client-device.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-client-node.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-link-factory.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-metadata.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-profiler.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-protocol-native.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-rtkit.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-session-manager.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-spa-device-factory.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-spa-device.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-spa-node-factory.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-spa-node.so

%files spa-plugins-%{spa_ver_str}
%{_libdir}/spa-%{spa_ver}/alsa/libspa-alsa.so
%{_libdir}/spa-%{spa_ver}/audioconvert/libspa-audioconvert.so
%{_libdir}/spa-%{spa_ver}/audiomixer/libspa-audiomixer.so
%{_libdir}/spa-%{spa_ver}/bluez5/libspa-bluez5.so
%{_libdir}/spa-%{spa_ver}/control/libspa-control.so
%{_libdir}/spa-%{spa_ver}/ffmpeg/libspa-ffmpeg.so
%{_libdir}/spa-%{spa_ver}/jack/libspa-jack.so
%{_libdir}/spa-%{spa_ver}/support/libspa-dbus.so
%{_libdir}/spa-%{spa_ver}/support/libspa-support.so
%{_libdir}/spa-%{spa_ver}/v4l2/libspa-v4l2.so
%{_libdir}/spa-%{spa_ver}/videoconvert/libspa-videoconvert.so
%{_libdir}/spa-%{spa_ver}/vulkan/libspa-vulkan.so

%dir %{_libdir}/spa-%{spa_ver}
%dir %{_libdir}/spa-%{spa_ver}/alsa
%dir %{_libdir}/spa-%{spa_ver}/audioconvert
%dir %{_libdir}/spa-%{spa_ver}/audiomixer
%dir %{_libdir}/spa-%{spa_ver}/bluez5
%dir %{_libdir}/spa-%{spa_ver}/control
%dir %{_libdir}/spa-%{spa_ver}/ffmpeg
%dir %{_libdir}/spa-%{spa_ver}/jack
%dir %{_libdir}/spa-%{spa_ver}/support
%dir %{_libdir}/spa-%{spa_ver}/v4l2
%dir %{_libdir}/spa-%{spa_ver}/videoconvert
%dir %{_libdir}/spa-%{spa_ver}/vulkan

%files devel
%{_libdir}/libpipewire-%{apiver}.so
%{_libdir}/libjack-pw.so
%{_libdir}/libpulse-mainloop-glib-pw.so
%{_libdir}/libpulse-pw.so
%{_libdir}/libpulse-simple-pw.so
%{_libdir}/pkgconfig/libpipewire-%{apiver}.pc
%{_libdir}/pkgconfig/libspa-%{spa_ver}.pc
%{_includedir}/pipewire-%{apiver}/
%{_includedir}/spa-%{spa_ver}/

%files doc
%dir %{_datadir}/doc/pipewire
%{_datadir}/doc/pipewire/html

%changelog
