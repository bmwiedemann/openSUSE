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


%define _use_internal_dependency_generator 0

%global provfind sh -c "grep -v -e 'libpulse.*\\.so' -e 'libjack.*\\.so' | %__find_provides"
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

Name:           pipewire
Version:        0.3.13
Release:        0
Summary:        A Multimedia Framework designed to be an audio and video server and more
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://pipewire.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Patch0:         fix-memfd_create-call.patch
Patch1:         do-not-use-snd_pcm_ioplug_hw_avail.patch
Patch2:         do-not-install-alsa-config-files.patch

BuildRequires:  doxygen
BuildRequires:  fdupes
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc9
%endif
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
License:        MIT
Group:          System/Libraries
Recommends:     pipewire

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
License:        MIT
Group:          Development/Libraries/C and C++
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description libjack-%{apiver_str}
PipeWire is a server and user space API to deal with multimedia pipelines.

Some of its features include:

 * Capture and playback of audio and video with minimal latency;
 * Real-time Multimedia processing on audio and video;
 * Multiprocess architecture to let applications share multimedia content;
 * GStreamer plugins for easy use and integration in current applications;
 * Sandboxed applications support.

This package provides the PipeWire replacement libraries for libjack.


%package libpulse-%{apiver_str}
Summary:        A Multimedia Framework designed to be an audio and video server and more
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description libpulse-%{apiver_str}
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
License:        MIT
Group:          System/Libraries

%description -n gstreamer-plugin-pipewire
PipeWire is a server and user space API to deal with multimedia pipelines.

This package provides the gstreamer plugin.

%package tools
Summary:        The PipeWire Tools
License:        MIT
Group:          Productivity/Multimedia/Other

%description tools
SPA or Simple Plugin API is a plugin API.

This package provides pipewire-cli and pipewire-monitor tools.

%package spa-tools
Summary:        The PipeWire SPA Tools
License:        MIT
Group:          Productivity/Multimedia/Other

%description spa-tools
SPA or Simple Plugin API is a plugin API.

This package provides spa-inspect and spa-monitor tools.

%package modules
Summary:        Modules For PipeWire, A Multimedia Framework
License:        MIT
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
License:        MIT
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
License:        MIT
Group:          Development/Libraries/C and C++
Requires:       %{libpipewire} >= %{version}

%description devel
PipeWire is a server and user space API to deal with multimedia pipelines.

This package provides all the necessary files for development with PipeWire

%package doc
Summary:        PipeWire media server documentation
License:        MIT
Group:          Development/Libraries/C and C++

%description doc
This package contains documentation for the PipeWire media server.

%prep
%setup
%if %{pkg_vcmp glibc < 2.27}
%patch0 -p1
%endif

%if %{pkg_vcmp alsa-devel < 1.1.7}
%patch1 -p1
sed -i -e "s/dependency('alsa', version : '>=1.1.7')/dependency('alsa', version : '>=1.1.5')/" meson.build
%endif
sed -i -e "s/meson_version : '>= 0.49.0',/meson_version : '>= 0.46.0',/" meson.build
%patch2 -p1

%autopatch -m 100 -p1

%build
%if %{pkg_vcmp gcc < 8}
export CC=gcc-9
%endif
%meson \
	-Ddocs=true \
	-Dman=true \
	-Dgstreamer=true \
	-Dffmpeg=true \
	-Dsystemd=true \
%if %{with_vulkan}
	-Dvulkan=true \
%else
	-Dvulkan=false \
%endif
	-Dtest=true \
	-Daudiotestsrc=true \
	%{nil}
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_sysconfdir}/alsa/conf.d/
for filename in 50-pipewire.conf \
                99-pipewire-default.conf ; do
    cp -a pipewire-alsa/conf/"$filename" %{buildroot}%{_sysconfdir}/alsa/conf.d/
done

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for wrapper in pw-pulse pw-jack ; do
    mv  %{buildroot}%{_bindir}/$wrapper   %{buildroot}%{_bindir}/$wrapper-%{apiver}
    ln -s -f %{_sysconfdir}/alternatives/$wrapper %{buildroot}%{_bindir}/$wrapper
done

for manpage in pw-jack pw-pulse ; do
    mv  %{buildroot}%{_mandir}/man1/$manpage.1 %{buildroot}%{_mandir}/man1/$manpage-%{apiver}.1
    ln -s -f %{_sysconfdir}/alternatives/$manpage.1%{ext_man} %{buildroot}%{_mandir}/man1/$manpage.1%{ext_man}
done

%fdupes -s %{buildroot}/%{_datadir}/doc/pipewire/html

%check
%meson_test

%post
if [ ! -f /etc/systemd/user/sockets.target.wants/%{name}.socket ]; then
  echo "Switching Pipewire activation using systemd user socket."
  echo "Please log out from all sessions once to make it effective."
fi
%systemd_user_post pipewire.socket
# FIXME: workaround to make sure the user socket symlink creation (related to bsc#1083473)
if [ ! -f /etc/systemd/user/sockets.target.wants/%{name}.socket ]; then
  # below should work once when preset is defined properly:
  #  /usr/bin/systemctl --no-reload --global preset pipewire.socket
  mkdir -p /etc/systemd/user/sockets.target.wants
  ln -s %{_userunitdir}/%{name}.socket /etc/systemd/user/sockets.target.wants/%{name}.socket
fi

%preun
%systemd_user_preun pipewire.socket

%postun
%systemd_user_postun pipewire.socket

%post   -n %{libpipewire} -p /sbin/ldconfig
%postun -n %{libpipewire} -p /sbin/ldconfig

%post libpulse-%{apiver_str}
%{_sbindir}/update-alternatives --install %{_bindir}/pw-pulse pw-pulse %{_bindir}/pw-pulse-%{apiver} 20 \
    --slave %{_mandir}/man1/pw-pulse.1%{ext_man} pw-pulse.1%{ext_man} %{_mandir}/man1/pw-pulse-%{apiver}.1%{ext_man}

%postun libpulse-%{apiver_str}
if [ ! -e %{_bindir}/pw-pulse-%{apiver} ] ; then
  %{_sbindir}/update-alternatives --remove pw-pulse %{_bindir}/pw-pulse-%{apiver}
fi

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
%{_mandir}/man1/pipewire.1%{ext_man}
%{_mandir}/man5/pipewire.conf.5%{ext_man}

%dir %{_sysconfdir}/pipewire
%config %{_sysconfdir}/pipewire/pipewire.conf

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

%files libpulse-%{apiver_str}
%license pipewire-pulseaudio/LICENSE
%dir %{_libdir}/pipewire-%{apiver}/pulse
%{_libdir}/pipewire-%{apiver}/pulse/libpulse.so*
%{_libdir}/pipewire-%{apiver}/pulse/libpulse-simple.so*
%{_libdir}/pipewire-%{apiver}/pulse/libpulse-mainloop-glib.so*
%ghost %{_sysconfdir}/alternatives/pw-pulse
%ghost %{_sysconfdir}/alternatives/pw-pulse.1%{ext_man}
%{_bindir}/pw-pulse-%{apiver}
%{_bindir}/pw-pulse
%{_mandir}/man1/pw-pulse-%{apiver}.1%{ext_man}
%{_mandir}/man1/pw-pulse.1%{ext_man}

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
%{_bindir}/pw-metadata
%{_bindir}/pw-mididump
%{_bindir}/pw-midiplay
%{_bindir}/pw-midirecord
%{_bindir}/pw-reserve
%{_mandir}/man1/pw-cli.1%{ext_man}
%{_mandir}/man1/pw-mon.1%{ext_man}
%{_mandir}/man1/pw-cat.1%{ext_man}
%{_mandir}/man1/pw-dot.1%{ext_man}
%{_mandir}/man1/pw-metadata.1%{ext_man}
%{_mandir}/man1/pw-mididump.1%{ext_man}
%{_mandir}/man1/pw-profiler.1%{ext_man}

%files spa-tools
%{_bindir}/spa-inspect
%{_bindir}/spa-monitor
%{_bindir}/spa-acp-tool
%{_bindir}/spa-resample

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
%if %{with_vulkan}
%{_libdir}/spa-%{spa_ver}/vulkan/libspa-vulkan.so
%endif
%{_libdir}/spa-%{spa_ver}/audiotestsrc/libspa-audiotestsrc.so
%{_libdir}/spa-%{spa_ver}/test/libspa-test.so

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
%if %{with_vulkan}
%dir %{_libdir}/spa-%{spa_ver}/vulkan
%endif
%dir %{_libdir}/spa-%{spa_ver}/audiotestsrc
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

%changelog
