#
# spec file for package pipewire
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define apiver 0.3
%define apiver_str 0_3
%define spa_ver 0.2
%define spa_ver_str 0_2
%define libpipewire libpipewire-%{apiver_str}-0

%if %{pkg_vcmp pkgconfig(vulkan) >= 1.3}
%define with_vulkan 1
%else
%define with_vulkan 0
%endif

%ifnarch s390 s390x ppc64
%define with_ldacBT 1
%define with_webrtc_audio_processing 1
%define webrtc_audio_processing_major_version 1
%else
%define with_ldacBT 0
%define with_webrtc_audio_processing 0
%endif

%if 0%{?suse_version} > 1500
%bcond_without libcamera
%else
%bcond_with libcamera
%endif

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
%bcond_without aac
%else
%bcond_with aac
%endif

%if %{?pkg_vcmp:%{pkg_vcmp meson >= 0.59.0}}%{!?pkg_vcmp:0}
%bcond_without pipewire_jack_devel
%endif

%if 0%{?ffmpeg_pref:1}
%bcond_without use_ffmpeg
%else
%bcond_with use_ffmpeg
%endif

%if 0%{?without_apparmor:0}
%bcond_with apparmor
%else
%bcond_without apparmor
%endif

%bcond_with aptx

Name:           pipewire
Version:        1.4.8+git68.636cbae9b
Release:        0
Summary:        A Multimedia Framework designed to be an audio and video server and more
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://pipewire.org/
Source0:        %{name}-%{version}.tar.zst
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE reduce-meson-dependency.patch
Patch0:         reduce-meson-dependency.patch

BuildRequires:  docutils
%if 0%{suse_version} > 1500
BuildRequires:  doxygen >= 1.9.7
%else
BuildRequires:  doxygen-1_10
%endif
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%endif
BuildRequires:  graphviz
BuildRequires:  meson >= 0.59.4
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(alsa) >= 1.1.7
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(dbus-1)
%if %{with aac}
BuildRequires:  pkgconfig(fdk-aac)
%endif
BuildRequires:  pkgconfig(fftw3f)
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
%if %{with use_ffmpeg}
# Break circular dependency with ffmpeg
BuildRequires:  %{ffmpeg_pref}-mini-devel
%endif
BuildRequires:  pkgconfig(lc3)
%if %{with libcamera}
BuildRequires:  libcamera-devel >= 0.2.0
%endif
%if %{with apparmor}
BuildRequires:  pkgconfig(libapparmor)
%endif
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libffado)
%if %{with aptx}
BuildRequires:  pkgconfig(libfreeaptx)
%endif
BuildRequires:  pkgconfig(libmysofa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sbc)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vulkan)
%if %{with_webrtc_audio_processing}
BuildRequires:  pkgconfig(webrtc-audio-processing-%{webrtc_audio_processing_major_version})
%endif
BuildRequires:  pkgconfig(x11)
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
BuildRequires:  pkgconfig(xfixes)
%endif
BuildConflicts: pipewire-libjack-%{apiver_str}-devel
Requires:       %{libpipewire} = %{version}
Requires:       %{name}-modules-%{apiver_str} = %{version}
Requires:       %{name}-session-manager
Requires:       %{name}-spa-plugins-%{spa_ver_str} = %{version}
Requires:       %{name}-spa-tools = %{version}
Requires:       %{name}-tools = %{version}
Requires:       rtkit
Suggests:       wireplumber
%{?systemd_ordering}

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
Requires:       pipewire-modules-%{apiver_str} >= %{version}
Requires:       pipewire-spa-plugins-%{spa_ver_str} >= %{version}
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
Requires(postun): update-alternatives
# Since the pipewire-libjack package is sometimes completely replacing the
# original jack libraries for some users we better make sure either they
# are also installed or we completely replace them with the pipewire
# libraries
Requires:       ((libjack0 and libjacknet0 and libjackserver0) or pipewire-jack)
Suggests:       (libjack0 if wireplumbler-video-only-profile else pipewire-jack)

%description libjack-%{apiver_str}
PipeWire is a server and user space API to deal with multimedia pipelines.

Some of its features include:

 * Capture and playback of audio and video with minimal latency;
 * Real-time Multimedia processing on audio and video;
 * Multiprocess architecture to let applications share multimedia content;
 * GStreamer plugins for easy use and integration in current applications;
 * Sandboxed applications support.

This package provides the PipeWire replacement libraries for libjack.

%package libjack-%{apiver_str}-devel
Summary:        Development files for %{name}-libjack-%{apiver_str}
Group:          Development/Libraries/C and C++
Requires:       %{name}-libjack-%{apiver_str} = %{version}
Conflicts:      libjack-devel

%description libjack-%{apiver_str}-devel
PipeWire is a server and user space API to deal with multimedia pipelines.

Some of its features include:

 * Capture and playback of audio and video with minimal latency;
 * Real-time Multimedia processing on audio and video;
 * Multiprocess architecture to let applications share multimedia content;
 * GStreamer plugins for easy use and integration in current applications;
 * Sandboxed applications support.

This package provides the PipeWire replacement development files
for libjack.

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

%package modules-%{apiver_str}
Summary:        Modules For PipeWire, A Multimedia Framework
Group:          Productivity/Multimedia/Other
Provides:       %{name}-modules = %{version}
Obsoletes:      %{name}-modules < %{version}

%description modules-%{apiver_str}
PipeWire is a server and user space API to deal with multimedia pipelines.

The framework is used to build a modular daemon that can be configured to:

 * Be a low-latency audio server with features like pulseaudio and/or jack;
 * A video capture server that can manage hardware video capture devices
   and provide access to them;
 * A central hub where video can be made available for other applications
   such as the gnome-shell screencast API.

%package module-x11-%{apiver_str}
Summary:        X11 support For PipeWire, A Multimedia Framework
Group:          Productivity/Multimedia/Other
Requires:       %{libpipewire} >= %{version}-%{release}
Requires:       %{name} >= %{version}-%{release}

%description module-x11-%{apiver_str}
PipeWire is a server and user space API to deal with multimedia pipelines.

The framework is used to build a modular daemon that can be configured to:

 * Be a low-latency audio server with features like pulseaudio and/or jack;
 * A video capture server that can manage hardware video capture devices
   and provide access to them;
 * A central hub where video can be made available for other applications
   such as the gnome-shell screencast API.

This package contains X11 bell support for PipeWire.

%package spa-plugins-%{spa_ver_str}
Summary:        Plugins For PipeWire SPA
Group:          Productivity/Multimedia/Other

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

%package spa-plugins-%{spa_ver_str}-jack
Summary:        SPA Plugin to use PipeWire as jack client
Group:          Productivity/Multimedia/Other
Requires:       jack

%description spa-plugins-%{spa_ver_str}-jack
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

This package provides the SPA plugin to connect Pipewire to a JACK server

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
Requires:       %{libpipewire} >= %{version}-%{release}
Recommends:     %{name} >= %{version}-%{release}
# Both providing /etc/alsa/conf.d/99-*-default.conf can cause issues
Conflicts:      alsa-plugins-pulse
# This is needed so that pipewire-alsa is not installed with the real pulseaudio (boo#1221235)
Requires:       pipewire-pulseaudio

%description alsa
This package contains an ALSA plugin for the PipeWire media server.

%package pulseaudio
Summary:        PipeWire PulseAudio implementation
Group:          Development/Libraries/C and C++
Requires:       %{libpipewire} >= %{version}-%{release}
Requires:       %{name} >= %{version}-%{release}
Requires:       pulseaudio-utils
Recommends:     pipewire-alsa
Conflicts:      pipewire-modules < 1.0.0
Conflicts:      pulseaudio
# Virtual Provides to support swapping between PipeWire-PA and PA
Conflicts:      pulseaudio-daemon
Provides:       pulseaudio-daemon
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
Requires(post): pulseaudio-setup
%endif
#Provides:       pulseaudio-module-bluetooth

%description pulseaudio
This package provides a PulseAudio implementation based on PipeWire

%package jack
Summary:        PipeWire JACK implementation
Group:          Development/Libraries/C and C++
Requires:       %{libpipewire} >= %{version}-%{release}
Requires:       %{name} >= %{version}-%{release}
Requires:       pipewire-libjack-%{apiver_str}
Recommends:     jack-dbus
# Virtual Provides to support swapping between PipeWire-JACK and JACKd
Conflicts:      jack-daemon
Provides:       jack-daemon
#Provides:       pulseaudio-module-jack
# We want applications to link with pipewire-libjack libraries and
# not the original ones
Conflicts:      libjack0
Conflicts:      libjacknet0
Conflicts:      libjackserver0

%description jack
This package provides an ld.so.conf file that makes all JACK clients
use the JACK implementation based on PipeWire instead of the original
JACK libraries.

%lang_package

%prep
%autosetup -N
%if %{?pkg_vcmp:%{pkg_vcmp meson <= 0.61.0}}
sed -ie "s/version : '0.3.72'/version : '%{version}'/" %{P:0}
%patch -P 0 -p1
%endif
%autopatch -m 1 -p1

%build
%if 0%{?suse_version} <= 1500
export CC=gcc-11
export CXX=g++-11
%endif
%meson \
    -Ddocs=enabled \
    -Dman=enabled \
    -Dgstreamer=enabled \
%if %{with use_ffmpeg}
    -Dffmpeg=enabled \
%else
    -Dffmpeg=disabled \
%endif
    -Dsystemd=enabled \
    -Dsystemd-user-unit-dir=%{_userunitdir} \
    -Droc=disabled \
%if %{with_vulkan}
    -Dvulkan=enabled \
%else
    -Dvulkan=disabled \
%endif
    -Dtest=enabled \
    -Daudiotestsrc=enabled \
%if %{with aac}
    -Dbluez5-codec-aac=enabled \
%else
    -Dbluez5-codec-aac=disabled \
%endif
%if %{with aptx}
    -Dbluez5-codec-aptx=enabled \
%else
    -Dbluez5-codec-aptx=disabled \
%endif
%if %{with_ldacBT}
    -Dbluez5-codec-ldac=enabled \
%else
    -Dbluez5-codec-ldac=disabled \
%endif
    -Dbluez5-codec-lc3=enabled \
    -Dbluez5-codec-lc3plus=disabled \
    -Dgsettings-pulse-schema=disabled \
%if %{with libcamera}
    -Dlibcamera=enabled \
%else
    -Dlibcamera=disabled \
%endif
    -Dpipewire-jack=enabled \
    -Djack=enabled \
%if %{with pipewire_jack_devel}
    -Djack-devel=true \
%else
    -Djack-devel=false \
%endif
%if 0%{?suse_version} <= 1500
    -Dreadline=disabled \
%endif
    -Dsession-managers="[]" \
    -Dsdl2=disabled \
    -Dsnap=disabled \
%if %{with_webrtc_audio_processing}
    -Decho-cancel-webrtc=enabled \
%else
    -Decho-cancel-webrtc=disabled \
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

%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_secdistconfdir}/limits.d/
mv %{buildroot}%{_sysconfdir}/security/limits.d/*.conf %{buildroot}%{_pam_secdistconfdir}/limits.d/
%endif

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
echo %{_libdir}/pipewire-%{apiver}/jack/ > %{buildroot}%{_sysconfdir}/ld.so.conf.d/pipewire-jack-%{_arch}.conf

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
%systemd_user_pre pipewire.service pipewire.socket

%post
# Check if the systemd_user_pre macro generated the file
# for systemd_user_post to enable the user socket.
if [ -f /run/systemd/rpm/needs-user-preset/pipewire.socket ]; then
  echo "Switching Pipewire activation using systemd user socket."
  echo "Please log out from all sessions once to make it effective."
fi
%systemd_user_post pipewire.service pipewire.socket

# If the pipewire.socket user unit is not enabled and the workaround
# for boo#1186561 has never been executed, we need to execute it now
if [ ! -L %{_sysconfdir}/systemd/user/sockets.target.wants/pipewire.socket \
    -a ! -f %{_localstatedir}/lib/pipewire/pipewire_post_workaround \
    -a -x %{_bindir}/systemctl ]; then
    for service in pipewire.service pipewire.socket ; do
        %{_bindir}/systemctl --global preset "$service" || :
    done

    mkdir -p %{_localstatedir}/lib/pipewire
    cat << EOF > %{_localstatedir}/lib/pipewire/pipewire_post_workaround
# The existence of this file means that the pipewire user services were
# enabled at least once. Please don't remove this file as that would
# make the services to be enabled again in the next package update.
#
# Check the following bugs for more information:
# https://bugzilla.opensuse.org/show_bug.cgi?id=1184852
# https://bugzilla.opensuse.org/show_bug.cgi?id=1183012
# https://bugzilla.opensuse.org/show_bug.cgi?id=1186561
EOF
fi

%preun
%systemd_user_preun pipewire.service pipewire.socket

%postun
%systemd_user_postun pipewire.service pipewire.socket

%pre pulseaudio
%systemd_user_pre pipewire-pulse.service pipewire-pulse.socket

%post pulseaudio
%systemd_user_post pipewire-pulse.service pipewire-pulse.socket
# If the pipewire-pulse.socket user service is not enabled and the workaround
# for boo#1186561 has never been executed, we need to execute it now
if [ ! -L %{_sysconfdir}/systemd/user/sockets.target.wants/pipewire-pulse.socket \
    -a ! -f %{_localstatedir}/lib/pipewire/pipewire-pulseaudio_post_workaround \
    -a -x %{_bindir}/systemctl ]; then
    for service in pipewire-pulse.service pipewire-pulse.socket ; do
        %{_bindir}/systemctl --global preset "$service" || :
    done
    mkdir -p %{_localstatedir}/lib/pipewire
    cat << EOF > %{_localstatedir}/lib/pipewire/pipewire-pulseaudio_post_workaround
# The existence of this file means that the pipewire-pulseaudio user service was
# enabled at least once. Please don't remove this file as that would
# make the services to be enabled again in the next package update.
#
# Check the following bugs for more information:
# https://bugzilla.opensuse.org/show_bug.cgi?id=1184852
# https://bugzilla.opensuse.org/show_bug.cgi?id=1183012
# https://bugzilla.opensuse.org/show_bug.cgi?id=1186561
EOF
fi
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
# Update the /etc/profile.d/pulseaudio.* files
setup-pulseaudio --auto > /dev/null
%endif

%preun pulseaudio
%systemd_user_preun pipewire-pulse.service pipewire-pulse.socket

%postun pulseaudio
%systemd_user_postun pipewire-pulse.service pipewire-pulse.socket

%post jack -p /sbin/ldconfig
%postun jack -p /sbin/ldconfig

%post   -n %{libpipewire} -p /sbin/ldconfig
%postun -n %{libpipewire} -p /sbin/ldconfig

%post libjack-%{apiver_str}
%{_sbindir}/update-alternatives --install %{_bindir}/pw-jack pw-jack %{_bindir}/pw-jack-%{apiver} 20 \
    --slave %{_mandir}/man1/pw-jack.1%{ext_man} pw-jack.1%{ext_man} %{_mandir}/man1/pw-jack-%{apiver}.1%{ext_man}
/sbin/ldconfig

%postun libjack-%{apiver_str}
if [ ! -e %{_bindir}/pw-jack-%{apiver} ] ; then
  %{_sbindir}/update-alternatives --remove pw-jack %{_bindir}/pw-jack-%{apiver}
fi
/sbin/ldconfig

%files
%license LICENSE COPYING
%doc README.md
%if 0%{?suse_version} > 1500
%dir %{_pam_secdistconfdir}/limits.d
%{_pam_secdistconfdir}/limits.d/25-pw-rlimits.conf
%else
%config(noreplace) %{_sysconfdir}/security/limits.d/25-pw-rlimits.conf
%endif
%{_bindir}/pipewire
%{_bindir}/pipewire-avb
%{_bindir}/pipewire-aes67
%if %{with_vulkan}
%{_bindir}/pipewire-vulkan
%endif
%{_userunitdir}/pipewire.service
%{_userunitdir}/pipewire.socket
%{_userunitdir}/filter-chain.service
%{_mandir}/man1/pipewire.1%{?ext_man}
%{_mandir}/man1/pw-reserve.1%{?ext_man}
%{_mandir}/man1/pw-v4l2.1%{?ext_man}
%{_mandir}/man1/spa-acp-tool.1%{?ext_man}
%{_mandir}/man1/spa-inspect.1%{?ext_man}
%{_mandir}/man1/spa-json-dump.1%{?ext_man}
%{_mandir}/man1/spa-monitor.1%{?ext_man}
%{_mandir}/man1/spa-resample.1%{?ext_man}
%{_mandir}/man5/pipewire-client.conf.5%{?ext_man}
%{_mandir}/man5/pipewire-filter-chain.conf.5%{?ext_man}
%{_mandir}/man5/pipewire.conf.5%{?ext_man}
%{_mandir}/man5/pipewire-jack.conf.5%{?ext_man}
%{_mandir}/man7/pipewire-props.7%{?ext_man}

%dir %{_datadir}/pipewire/
%{_datadir}/pipewire/pipewire.conf
%{_datadir}/pipewire/pipewire.conf.avail/
%{_datadir}/pipewire/filter-chain.conf
%dir %{_datadir}/pipewire/filter-chain/
%{_datadir}/pipewire/filter-chain/*.conf
%{_datadir}/pipewire/pipewire-avb.conf
%{_datadir}/pipewire/pipewire-aes67.conf
%if %{with_vulkan}
%{_datadir}/pipewire/pipewire-vulkan.conf
%endif
%ghost %dir %{_localstatedir}/lib/pipewire/
%ghost %{_localstatedir}/lib/pipewire/pipewire_post_workaround

%files -n %{libpipewire}
%license LICENSE COPYING
%doc README.md
%{_libdir}/libpipewire-%{apiver}.so.*

%files modules-%{apiver_str}
%dir %{_libdir}/pipewire-%{apiver}
%{_libdir}/pipewire-%{apiver}/libpipewire-module-*.so
%exclude %{_libdir}/pipewire-%{apiver}/libpipewire-module-jack-tunnel.so
%exclude %{_libdir}/pipewire-%{apiver}/libpipewire-module-jackdbus-detect.so
%exclude %{_libdir}/pipewire-%{apiver}/libpipewire-module-x11-bell.so
%exclude %{_libdir}/pipewire-%{apiver}/libpipewire-module-protocol-pulse.so
%dir %{_libdir}/pipewire-%{apiver}/v4l2/
%{_libdir}/pipewire-%{apiver}/v4l2/libpw-v4l2.so
%dir %{_datadir}/alsa-card-profile/
%dir %{_datadir}/alsa-card-profile/mixer/
%{_datadir}/alsa-card-profile/mixer/*
%{_udevrulesdir}/90-pipewire-alsa.rules
%{_datadir}/pipewire/client.conf
%{_datadir}/pipewire/client.conf.avail/
%{_datadir}/pipewire/minimal.conf
%{_mandir}/man7/libpipewire-modules.7%{?ext_man}
%{_mandir}/man7/libpipewire-module-*.7%{?ext_man}
%exclude %{_mandir}/man7/libpipewire-module-x11-bell.7%{?ext_man}

%files module-x11-%{apiver_str}
%{_libdir}/pipewire-%{apiver}/libpipewire-module-x11-bell.so
%{_mandir}/man7/libpipewire-module-x11-bell.7%{?ext_man}

%files spa-plugins-%{spa_ver_str}
%dir %{_libdir}/spa-%{spa_ver}/
%{_libdir}/spa-%{spa_ver}/aec/
%{_libdir}/spa-%{spa_ver}/alsa/
%{_libdir}/spa-%{spa_ver}/audioconvert/
%{_libdir}/spa-%{spa_ver}/audiomixer/
%{_libdir}/spa-%{spa_ver}/avb/
%{_libdir}/spa-%{spa_ver}/bluez5/
%{_libdir}/spa-%{spa_ver}/control/
%if %{with use_ffmpeg}
%{_libdir}/spa-%{spa_ver}/ffmpeg/
%endif
%if %{with libcamera}
%{_libdir}/spa-%{spa_ver}/libcamera/
%endif
%{_libdir}/spa-%{spa_ver}/support/
%{_libdir}/spa-%{spa_ver}/v4l2/
%{_libdir}/spa-%{spa_ver}/videoconvert/
%if %{with_vulkan}
%{_libdir}/spa-%{spa_ver}/vulkan/
%endif
%{_libdir}/spa-%{spa_ver}/audiotestsrc/
%{_libdir}/spa-%{spa_ver}/videotestsrc/
%{_libdir}/spa-%{spa_ver}/test/
%dir %{_libdir}/spa-%{spa_ver}/filter-graph
%{_libdir}/spa-%{spa_ver}/filter-graph/libspa-filter-graph-plugin-builtin.so
%{_libdir}/spa-%{spa_ver}/filter-graph/libspa-filter-graph-plugin-ebur128.so
%{_libdir}/spa-%{spa_ver}/filter-graph/libspa-filter-graph-plugin-ladspa.so
%{_libdir}/spa-%{spa_ver}/filter-graph/libspa-filter-graph-plugin-lv2.so
%{_libdir}/spa-%{spa_ver}/filter-graph/libspa-filter-graph-plugin-sofa.so
%{_libdir}/spa-%{spa_ver}/filter-graph/libspa-filter-graph.so
%{_libdir}/spa-%{spa_ver}/libspa.so

%dir %{_datadir}/spa-%{spa_ver}/
%dir %{_datadir}/spa-%{spa_ver}/bluez5/
%{_datadir}/spa-%{spa_ver}/bluez5/bluez-hardware.conf

%files libjack-%{apiver_str}
%dir %{_libdir}/pipewire-%{apiver}/jack
%{_libdir}/pipewire-%{apiver}/jack/libjack.so.*
%{_libdir}/pipewire-%{apiver}/jack/libjacknet.so.*
%{_libdir}/pipewire-%{apiver}/jack/libjackserver.so.*
%ghost %{_sysconfdir}/alternatives/pw-jack
%ghost %{_sysconfdir}/alternatives/pw-jack.1%{ext_man}
%{_bindir}/pw-jack-%{apiver}
%{_bindir}/pw-jack
%{_mandir}/man1/pw-jack-%{apiver}.1%{?ext_man}
%{_mandir}/man1/pw-jack.1%{?ext_man}
%{_datadir}/pipewire/jack.conf

%files libjack-%{apiver_str}-devel
%{_libdir}/pipewire-%{apiver}/jack/libjack.so
%{_libdir}/pipewire-%{apiver}/jack/libjacknet.so
%{_libdir}/pipewire-%{apiver}/jack/libjackserver.so
%if %{with pipewire_jack_devel}
%{_includedir}/jack/
%{_libdir}/pkgconfig/jack.pc
%{_libdir}/pkgconfig/jackserver.pc
%endif

%files -n gstreamer-plugin-pipewire
%{_libdir}/gstreamer-1.0/libgstpipewire.so

%files tools
%{_bindir}/pw-cat
%{_bindir}/pw-cli
%{_bindir}/pw-config
%{_bindir}/pw-container
%{_bindir}/pw-dot
%{_bindir}/pw-dsdplay
%{_bindir}/pw-dump
%{_bindir}/pw-encplay
%{_bindir}/pw-loopback
%{_bindir}/pw-link
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
%{_bindir}/pw-v4l2
%{_mandir}/man1/pw-cat.1%{?ext_man}
%{_mandir}/man1/pw-cli.1%{?ext_man}
%{_mandir}/man1/pw-config.1%{?ext_man}
%{_mandir}/man1/pw-container.1%{?ext_man}
%{_mandir}/man1/pw-dot.1%{?ext_man}
%{_mandir}/man1/pw-dump.1%{?ext_man}
%{_mandir}/man1/pw-link.1%{?ext_man}
%{_mandir}/man1/pw-loopback.1%{?ext_man}
%{_mandir}/man1/pw-metadata.1%{?ext_man}
%{_mandir}/man1/pw-mididump.1%{?ext_man}
%{_mandir}/man1/pw-mon.1%{?ext_man}
%{_mandir}/man1/pw-profiler.1%{?ext_man}
%{_mandir}/man1/pw-top.1%{?ext_man}

%files spa-tools
%{_bindir}/spa-inspect
%{_bindir}/spa-monitor
%{_bindir}/spa-acp-tool
%{_bindir}/spa-resample
%{_bindir}/spa-json-dump

%files devel
%{_libdir}/libpipewire-%{apiver}.so
%{_libdir}/pkgconfig/libpipewire-%{apiver}.pc
%{_libdir}/pkgconfig/libspa-%{spa_ver}.pc
%{_includedir}/pipewire-%{apiver}/
%{_includedir}/spa-%{spa_ver}/

%files doc
%dir %{_datadir}/doc/pipewire/
%{_datadir}/doc/pipewire/html/

%files pulseaudio
%{_bindir}/pipewire-pulse
%{_libdir}/pipewire-%{apiver}/libpipewire-module-protocol-pulse.so
%{_mandir}/man1/pipewire-pulse.1%{?ext_man}
%{_mandir}/man5/pipewire-pulse.conf.5%{?ext_man}
%{_mandir}/man7/pipewire-pulse-module-*.7%{?ext_man}
%{_mandir}/man7/pipewire-pulse-modules.7%{?ext_man}
%{_userunitdir}/pipewire-pulse.*
%{_datadir}/pipewire/pipewire-pulse.conf
%{_datadir}/pipewire/pipewire-pulse.conf.avail/
%ghost %{_localstatedir}/lib/pipewire/pipewire-pulseaudio_post_workaround

%files alsa
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_pcm_pipewire.so
%{_libdir}/alsa-lib/libasound_module_ctl_pipewire.so
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/50-pipewire.conf
%{_datadir}/alsa/alsa.conf.d/99-pipewire-default.conf
%dir %{_sysconfdir}/alsa/
%dir %{_sysconfdir}/alsa/conf.d/
%config(noreplace) %{_sysconfdir}/alsa/conf.d/50-pipewire.conf
%config(noreplace) %{_sysconfdir}/alsa/conf.d/99-pipewire-default.conf

%files jack
%config %{_sysconfdir}/ld.so.conf.d/pipewire-jack-%{_arch}.conf

%files spa-plugins-%{spa_ver_str}-jack
%{_libdir}/pipewire-%{apiver}/libpipewire-module-jack-tunnel.so
%{_libdir}/pipewire-%{apiver}/libpipewire-module-jackdbus-detect.so
%{_libdir}/spa-%{spa_ver}/jack/

%files lang -f %{name}.lang

%changelog
