#
# spec file for package pipewire
#
# Copyright (c) 2021 SUSE LLC
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


%define _use_internal_dependency_generator 0

%global provfind sh -c "grep -v -e 'libjack.*\\.so' | %__find_provides"
%global __find_provides %provfind

%define apiver 0.3
%define apiver_str 0_3
%define spa_ver 0.2
%define spa_ver_str 0_2

%define libpipewire libpipewire-%{apiver_str}-0
%if %{pkg_vcmp pkgconfig(vulkan) >= 1.1}
%define with_vulkan 1
%else
%define with_vulkan 0
%endif

%ifnarch s390 s390x ppc64
%define with_ldacBT 1
%else
%define with_ldacBT 0
%endif

Name:           pipewire
Version:        0.3.25
Release:        0
Summary:        A Multimedia Framework designed to be an audio and video server and more
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://pipewire.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Source99:       baselibs.conf

BuildRequires:  doxygen
BuildRequires:  fdupes
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc9
%endif
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
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
%if %{with_ldacBT}
BuildRequires:  pkgconfig(ldacBT-abr)
BuildRequires:  pkgconfig(ldacBT-enc)
%endif
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(sbc)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
Requires:       %{libpipewire} = %{version}
Requires:       %{name}-modules = %{version}
Requires:       %{name}-spa-plugins-%{spa_ver_str} = %{version}
Requires:       %{name}-spa-tools = %{version}
Requires:       %{name}-tools = %{version}

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
Recommends:     pipewire >= %{version}

%description -n %{libpipewire}
PipeWire is a server and user space API to deal with multimedia pipelines.

Some of its features include:

 * Capture and playback of audio and video with minimal latency;
 * Real-time Multimedia processing on audio and video;
 * Multiprocess architecture to let applications share multimedia content;
 * GStreamer plugins for easy use and integration in current applications;
 * Sandboxed applications support.

This package provides the PipeWire shared library.

%package libjack-%{apiver_str}
Summary:        PipeWire libjack replacement libraries
Group:          Development/Libraries/C and C++
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description libjack-%{apiver_str}
PipeWire is a server and user space API to deal with multimedia pipelines.

Some of its features include:

 * Capture and playback of audio and video with minimal latency;
 * Real-time Multimedia processing on audio and video;
 * Multiprocess architecture to let applications share multimedia content;
 * GStreamer plugins for easy use and integration in current applications;
 * Sandboxed applications support.

This package provides the PipeWire replacement libraries for libjack.

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
This package contains command line utilities for the PipeWire media server.

%package spa-tools
Summary:        The PipeWire SPA Tools
Group:          Productivity/Multimedia/Other

%description spa-tools
SPA or Simple Plugin API is a plugin API.

This package provides spa-inspect and spa-monitor tools.

%package modules
Summary:        Modules For PipeWire, A Multimedia Framework
Group:          Productivity/Multimedia/Other
Requires:       pipewire = %{version}

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

%package alsa
Summary:        PipeWire media server ALSA support
Group:          Development/Libraries/C and C++
Recommends:     %{name} >= %{version}-%{release}
Requires:       %{libpipewire} >= %{version}-%{release}

%description alsa
This package contains an ALSA plugin for the PipeWire media server.

%package pulseaudio
Summary:        PipeWire PulseAudio implementation
Group:          Development/Libraries/C and C++
Recommends:     %{name} >= %{version}-%{release}
Requires:       %{libpipewire} >= %{version}-%{release}
Conflicts:      pulseaudio

# Virtual Provides to support swapping between PipeWire-PA and PA
Provides:       pulseaudio-daemon
Conflicts:      pulseaudio-daemon
#Provides:       pulseaudio-module-bluetooth
#Provides:       pulseaudio-module-jack

%description pulseaudio
This package provides a PulseAudio implementation based on PipeWire

%lang_package

%prep
%autosetup -p1

%build
%if %{pkg_vcmp gcc < 8}
export CC=gcc-9
%endif
%meson \
	-Ddocs=enabled \
	-Dman=enabled \
	-Dgstreamer=enabled \
	-Dffmpeg=enabled \
	-Dsystemd=enabled \
%if %{with_vulkan}
	-Dvulkan=enabled \
%else
	-Dvulkan=disabled \
%endif
	-Dtest=enabled \
	-Daudiotestsrc=enabled \
        -Dbluez5-codec-aac=disabled \
        -Dbluez5-codec-aptx=disabled \
        -Dlibcamera=disabled \
%if %{with_ldacBT}
        -Dbluez5-codec-ldac=enabled \
%else
        -Dbluez5-codec-ldac=disabled \
%endif
	%{nil}
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_sysconfdir}/alsa/conf.d/
cp %{buildroot}%{_datadir}/alsa/alsa.conf.d/50-pipewire.conf \
        %{buildroot}%{_sysconfdir}/alsa/conf.d/50-pipewire.conf
cp %{buildroot}%{_datadir}/alsa/alsa.conf.d/99-pipewire-default.conf \
        %{buildroot}%{_sysconfdir}/alsa/conf.d/99-pipewire-default.conf
touch %{buildroot}%{_sysconfdir}/pipewire/media-session.d/with-alsa
mkdir -p %{buildroot}%{_udevrulesdir}
mv -fv %{buildroot}/lib/udev/rules.d/90-pipewire-alsa.rules %{buildroot}%{_udevrulesdir}

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for wrapper in pw-jack ; do
    mv  %{buildroot}%{_bindir}/$wrapper   %{buildroot}%{_bindir}/$wrapper-%{apiver}
    ln -s -f %{_sysconfdir}/alternatives/$wrapper %{buildroot}%{_bindir}/$wrapper
done

for manpage in pw-jack ; do
    mv  %{buildroot}%{_mandir}/man1/$manpage.1 %{buildroot}%{_mandir}/man1/$manpage-%{apiver}.1
    ln -s -f %{_sysconfdir}/alternatives/$manpage.1%{ext_man} %{buildroot}%{_mandir}/man1/$manpage.1%{ext_man}
done

%fdupes -s %{buildroot}/%{_datadir}/doc/pipewire/html

%find_lang %{name} %{name}.lang

%check
%meson_test

%pre
%systemd_user_pre pipewire.service pipewire.socket pipewire-media-session.service

%post
# Check if the systemd_user_pre macro generated the file
# for systemd_user_post to enable the user socket.
if [ -f /run/systemd/rpm/needs-user-preset/pipewire.socket ]; then
  echo "Switching Pipewire activation using systemd user socket."
  echo "Please log out from all sessions once to make it effective."
fi
%systemd_user_post pipewire.service pipewire.socket pipewire-media-session.service

%preun
%systemd_user_preun pipewire.service pipewire.socket pipewire-media-session.service

%postun
%systemd_user_postun pipewire.service pipewire.socket pipewire-media-session.service

%pre pulseaudio
%systemd_user_pre pipewire-pulse.service pipewire-pulse.socket

%post pulseaudio
%systemd_user_post pipewire-pulse.service pipewire-pulse.socket

%preun pulseaudio
%systemd_user_preun pipewire-pulse.service pipewire-pulse.socket

%postun pulseaudio
%systemd_user_postun pipewire-pulse.service pipewire-pulse.socket

%post   -n %{libpipewire} -p /sbin/ldconfig
%postun -n %{libpipewire} -p /sbin/ldconfig

%post libjack-%{apiver_str}
%{_sbindir}/update-alternatives --install %{_bindir}/pw-jack pw-jack %{_bindir}/pw-jack-%{apiver} 20 \
    --slave %{_mandir}/man1/pw-jack.1%{ext_man} pw-jack.1%{ext_man} %{_mandir}/man1/pw-jack-%{apiver}.1%{ext_man}

%postun libjack-%{apiver_str}
if [ ! -e %{_bindir}/pw-jack-%{apiver} ] ; then
  %{_sbindir}/update-alternatives --remove pw-jack %{_bindir}/pw-jack-%{apiver}
fi

%files
%{_bindir}/pipewire
%{_bindir}/pipewire-media-session
%{_userunitdir}/pipewire.service
%{_userunitdir}/pipewire.socket
%{_userunitdir}/pipewire-media-session.service
%{_mandir}/man1/pipewire.1%{ext_man}
%{_mandir}/man5/pipewire.conf.5%{ext_man}

%dir %{_sysconfdir}/pipewire
%config(noreplace) %{_sysconfdir}/pipewire/pipewire.conf
%config(noreplace) %{_sysconfdir}/pipewire/client.conf
%config(noreplace) %{_sysconfdir}/pipewire/client-rt.conf
%config(noreplace) %{_sysconfdir}/pipewire/jack.conf
%config(noreplace) %{_sysconfdir}/pipewire/pipewire-pulse.conf
%dir %{_sysconfdir}/pipewire/media-session.d
%config(noreplace) %{_sysconfdir}/pipewire/media-session.d/media-session.conf
%config(noreplace) %{_sysconfdir}/pipewire/media-session.d/alsa-monitor.conf
%config(noreplace) %{_sysconfdir}/pipewire/media-session.d/bluez-monitor.conf
%config(noreplace) %{_sysconfdir}/pipewire/media-session.d/v4l2-monitor.conf

%files -n %{libpipewire}
%license LICENSE COPYING
%doc README.md
%{_libdir}/libpipewire-%{apiver}.so.*

%files libjack-%{apiver_str}
%dir %{_libdir}/pipewire-%{apiver}/jack
%{_libdir}/pipewire-%{apiver}/jack/libjack.so*
%{_libdir}/pipewire-%{apiver}/jack/libjacknet.so*
%{_libdir}/pipewire-%{apiver}/jack/libjackserver.so*
%ghost %{_sysconfdir}/alternatives/pw-jack
%ghost %{_sysconfdir}/alternatives/pw-jack.1%{ext_man}
%{_bindir}/pw-jack-%{apiver}
%{_bindir}/pw-jack
%{_mandir}/man1/pw-jack-%{apiver}.1%{ext_man}
%{_mandir}/man1/pw-jack.1%{ext_man}
%config(noreplace) %{_sysconfdir}/pipewire/media-session.d/with-jack

%files -n gstreamer-plugin-pipewire
%{_libdir}/gstreamer-1.0/libgstpipewire.so

%files tools
%{_bindir}/pw-cat
%{_bindir}/pw-cli
%{_bindir}/pw-dot
%{_bindir}/pw-dump
%{_bindir}/pw-loopback
%{_bindir}/pw-metadata
%{_bindir}/pw-mididump
%{_bindir}/pw-midiplay
%{_bindir}/pw-midirecord
%{_bindir}/pw-mon
%{_bindir}/pw-play
%{_bindir}/pw-profiler
%{_bindir}/pw-record
%{_bindir}/pw-reserve
%{_bindir}/pw-top
%{_mandir}/man1/pw-cat.1%{ext_man}
%{_mandir}/man1/pw-cli.1%{ext_man}
%{_mandir}/man1/pw-dot.1%{ext_man}
%{_mandir}/man1/pw-metadata.1%{ext_man}
%{_mandir}/man1/pw-mididump.1%{ext_man}
%{_mandir}/man1/pw-mon.1%{ext_man}
%{_mandir}/man1/pw-profiler.1%{ext_man}

%files spa-tools
%{_bindir}/spa-inspect
%{_bindir}/spa-monitor
%{_bindir}/spa-acp-tool
%{_bindir}/spa-resample
%{_bindir}/spa-json-dump

%files modules
%dir %{_libdir}/pipewire-%{apiver}
%{_libdir}/pipewire-%{apiver}/libpipewire-module-access.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-adapter.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-client-device.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-client-node.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-link-factory.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-metadata.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-portal.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-profiler.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-protocol-native.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-protocol-pulse.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-rtkit.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-session-manager.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-spa-device-factory.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-spa-device.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-spa-node-factory.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-spa-node.so
%dir %{_datadir}/alsa-card-profile
%dir %{_datadir}/alsa-card-profile/mixer
%{_datadir}/alsa-card-profile/mixer/*

%files spa-plugins-%{spa_ver_str}
%{_libdir}/spa-%{spa_ver}/alsa/libspa-alsa.so
%{_libdir}/spa-%{spa_ver}/audioconvert/libspa-audioconvert.so
%{_libdir}/spa-%{spa_ver}/audiomixer/libspa-audiomixer.so
%{_libdir}/spa-%{spa_ver}/bluez5/libspa-bluez5.so
%{_libdir}/spa-%{spa_ver}/control/libspa-control.so
%{_libdir}/spa-%{spa_ver}/ffmpeg/libspa-ffmpeg.so
%{_libdir}/spa-%{spa_ver}/jack/libspa-jack.so
%{_libdir}/spa-%{spa_ver}/support/libspa-dbus.so
%{_libdir}/spa-%{spa_ver}/support/libspa-journal.so
%{_libdir}/spa-%{spa_ver}/support/libspa-support.so
%{_libdir}/spa-%{spa_ver}/v4l2/libspa-v4l2.so
%{_libdir}/spa-%{spa_ver}/videoconvert/libspa-videoconvert.so
%if %{with_vulkan}
%{_libdir}/spa-%{spa_ver}/vulkan/libspa-vulkan.so
%endif
%{_libdir}/spa-%{spa_ver}/audiotestsrc/libspa-audiotestsrc.so
%{_libdir}/spa-%{spa_ver}/test/libspa-test.so
%{_libdir}/spa-%{spa_ver}/videotestsrc/libspa-videotestsrc.so
%{_libdir}/spa-%{spa_ver}/volume/libspa-volume.so

%dir %{_libdir}/spa-%{spa_ver}
%dir %{_libdir}/spa-%{spa_ver}/alsa
%dir %{_libdir}/spa-%{spa_ver}/audioconvert
%dir %{_libdir}/spa-%{spa_ver}/audiomixer
%dir %{_libdir}/spa-%{spa_ver}/bluez5
%dir %{_libdir}/spa-%{spa_ver}/control
%dir %{_libdir}/spa-%{spa_ver}/volume
%dir %{_libdir}/spa-%{spa_ver}/ffmpeg
%dir %{_libdir}/spa-%{spa_ver}/jack
%dir %{_libdir}/spa-%{spa_ver}/support
%dir %{_libdir}/spa-%{spa_ver}/v4l2
%dir %{_libdir}/spa-%{spa_ver}/videoconvert
%if %{with_vulkan}
%dir %{_libdir}/spa-%{spa_ver}/vulkan
%endif
%dir %{_libdir}/spa-%{spa_ver}/audiotestsrc
%dir %{_libdir}/spa-%{spa_ver}/videotestsrc
%dir %{_libdir}/spa-%{spa_ver}/test

%files devel
%{_libdir}/libpipewire-%{apiver}.so
%{_libdir}/pkgconfig/libpipewire-%{apiver}.pc
%{_libdir}/pkgconfig/libspa-%{spa_ver}.pc
%{_includedir}/pipewire-%{apiver}/
%{_includedir}/spa-%{spa_ver}/

%files doc
%dir %{_datadir}/doc/pipewire
%{_datadir}/doc/pipewire/html

%files pulseaudio
%{_bindir}/pipewire-pulse
%{_userunitdir}/pipewire-pulse.*
%config(noreplace) %{_sysconfdir}/pipewire/media-session.d/with-pulseaudio

%files alsa
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_pcm_pipewire.so
%{_libdir}/alsa-lib/libasound_module_ctl_pipewire.so
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/50-pipewire.conf
%{_datadir}/alsa/alsa.conf.d/99-pipewire-default.conf
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/50-pipewire.conf
%config(noreplace) %{_sysconfdir}/alsa/conf.d/99-pipewire-default.conf
%config(noreplace) %{_sysconfdir}/pipewire/media-session.d/with-alsa
%{_udevrulesdir}/90-pipewire-alsa.rules

%files lang -f %{name}.lang

%changelog
