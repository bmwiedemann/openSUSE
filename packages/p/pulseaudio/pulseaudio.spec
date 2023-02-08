#
# spec file for package pulseaudio
#
# Copyright (c) 2022 SUSE LLC
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

%ifarch armv7 armv7hl
%define _lto_cflags %{nil}
%endif

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define drvver  16.1
%define soname  0
%define _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d
%define _bashcompletionsdir %{_datadir}/bash-completion/completions
Name:           pulseaudio
Version:        16.1
Release:        0
Summary:        A Networked Sound Server
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Sound Daemons
Url:            https://www.freedesktop.org/wiki/Software/PulseAudio/
Source:         https://www.freedesktop.org/software/pulseaudio/releases/%{name}-%{version}.tar.xz
Source1:        default.pa-for-gdm
Source2:        setup-pulseaudio
Source3:        sysconfig.sound-pulseaudio
Source5:        pulseaudio.service
Source6:        disable_flat_volumes.conf
Source7:        pulseaudio.tmpfiles
Source8:        pulseaudio-gdm-hooks.tmpfiles
Source9:        client-system.conf
Source10:       system-user-pulse.conf
Source98:       pulseaudio-rpmlintrc
Source99:       baselibs.conf
Patch0:         disabled-start.diff
Patch1:         suppress-socket-error-msg.diff
# PATCH-FIX-OPENSUSE qpaeq-shebang.patch Avoid rpmlint error due to using env python shebang
Patch5:         qpaeq-shebang.patch
# PATCH-FIX-OPENSUSE Workaround for old systemd on Leap 15.x
Patch6:         pulseaudio-old-systemd-workaround.patch
# PATCH-FIX-OPENSUSE Workaround for suse-module-tools directory
Patch7:         pulseaudio-dump-module-Ignore-invalid-module-init-tools.patch
BuildRequires:  alsa-devel >= 1.0.19
BuildRequires:  bluez-devel >= 5
BuildRequires:  fdupes
BuildRequires:  fftw3-devel >= 3.0
BuildRequires:  gcc-c++
BuildRequires:  jack-devel
BuildRequires:  meson
BuildRequires:  libatomic_ops-devel >= 1.2
BuildRequires:  libavahi-devel
BuildRequires:  libcap-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libsndfile-devel >= 1.0.18
BuildRequires:  libtool
BuildRequires:  pkgconfig(libudev) >= 143
BuildRequires:  libwebrtc_audio_processing-devel >= 0.3
BuildRequires:  orc >= 0.4.9
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  speexdsp-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(dbus-1) >= 1.4.12
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-rtp-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(lirc)
BuildRequires:  pkgconfig(sbc) >= 1.0
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tdb)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xtst)

Requires:       rtkit
Requires:       udev >= 146
#!BuildIgnore:  user(pulse)
Requires(pre):  user(pulse)
## needs the same liborc version which was used to build against
%requires_eq    liborc-0_4-0
Requires(post): pulseaudio-setup
Recommends:     alsa-plugins-pulse
Suggests:       libsoxr0 >= 0.1.1
Conflicts:      kernel < 2.6.31
Obsoletes:      libpulsecore9 < 0.9.15
Provides:       libpulsecore9 = 0.9.15
Obsoletes:      libpulsecore7 < 0.9.13
Provides:       libpulsecore7 = 0.9.13

Provides:       pulseaudio-daemon
Conflicts:      pulseaudio-daemon

%description
pulseaudio is a networked sound server for Linux, other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

%package setup
Summary:        Set-up script for PulseAudio
Group:          System/Sound Daemons
Requires(post): %fillup_prereq

%description setup
This package contains a setup script for making PulseAudio working with
various applications.

%package module-lirc
Summary:        LIRC module for PulseAudio
Group:          System/Sound Daemons
Requires:       %{name} = %{version}
Supplements:	(pulseaudio and lirc-core)

%description module-lirc
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package provides support for IR and RF remotes.

%package module-x11
Summary:        X11 module for PulseAudio
Group:          System/Sound Daemons
Requires:       %{name} = %{version}
Requires:       %{name}-utils = %{version}

%description module-x11
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package provides the components needed to automatically start
the PulseAudio sound server on X11 startup.

%package module-zeroconf
Summary:        Zeroconf module for PulseAudio
Group:          System/Sound Daemons
Requires:       %{name} = %{version}
Supplements:	(pulseaudio and avahi)

%description module-zeroconf
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package provides zeroconf network support for the PulseAudio sound server

%package system-wide
Summary:        Support for running PulseAudio daemon system wide
Group:          System/Sound Daemons
Requires:       %{name}
%systemd_requires

%description system-wide
PulseAudio daemon can be run as a system-wide instance which than can be shared
by multiple local users. We recommend running the PulseAudio daemon per-user,
just like the traditional ESD sound daemon. In some situations however, such as
embedded systems where no real notion of a user exists, it makes sense to use
the system-wide mode.

Before you now go ahead and use it please read about what is wrong with system
mode:

http://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/WhatIsWrongWithSystemWide

%package module-jack
Summary:        JACK support for the PulseAudio sound server
Group:          System/Sound Daemons
Requires:       %{name} = %{version}

%description module-jack
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package includes support for Jack-based applications.

%package module-bluetooth
Summary:        Bluetooth support for the PulseAudio sound server
Group:          System/Sound Daemons
Requires:       %{name} = %{version}
Requires:       bluez >= 5
Supplements:	(pulseaudio and bluez)

%description module-bluetooth
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

Contains Bluetooth audio (A2DP/HSP/HFP) support for the PulseAudio sound server.

%package module-gsettings
Summary:        GSettings module for PulseAudio
Group:          System/Sound Daemons
Requires:       %{name} = %{version}
Conflicts:      %{name}-module-gconf

%description module-gsettings
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package provides GSettings storage of PulseAudio sound server settings.

%package -n libpulse%{soname}
Summary:        Client interface to PulseAudio
Group:          System/Libraries
Provides:       pulseaudio-libs = %{version}
Obsoletes:      pulseaudio-libs < %{version}

%description -n libpulse%{soname}
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package contains the system libraries for clients of pulseaudio
sound server.

%package -n libpulse-mainloop-glib%{soname}
Summary:        GLIB 2.0 Main Loop wrapper for PulseAudio
Group:          System/Sound Daemons
Provides:       pulseaudio-libs-glib2 = %{version}
Obsoletes:      pulseaudio-libs-glib2 < %{version}

%description -n libpulse-mainloop-glib%{soname}
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package contains the GLIB Main Loop bindings for the PulseAudio
sound server.

%package -n libpulse-devel
Summary:        Development package for the pulseaudio library
Group:          Development/Libraries/C and C++
Requires:       libpulse%{soname} = %{version}
Requires:       libpulse-mainloop-glib%{soname} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(glib-2.0)
Provides:       pulseaudio-devel = %{version}
Obsoletes:      pulseaudio-devel < %{version}

%description -n libpulse-devel
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package contains the files needed to compile programs that use the
pulseaudio library.

%package utils
Summary:        PulseAudio utilities
Group:          System/Sound Daemons
Requires:       pulseaudio-daemon
Requires:       libpulse%{soname} = %{version}
Requires:       libpulse-mainloop-glib%{soname} = %{version}

%description utils
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package provides utilies for making use of the PulseAudio sound
server.

%package gdm-hooks
Summary:        PulseAudio GDM integration
Group:          Productivity/Multimedia/Other
#avoid cycle
#!BuildIgnore:  gdm
Requires:       %{name} = %{version}
Requires:       gdm >= 2.22
Supplements:    (pulseaudio and gdm)
#for the gdm user
Requires(pre):  gdm

%description gdm-hooks
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package contains GDM integration hooks for the PulseAudio sound server.

%package bash-completion
Summary:        PulseAudio Bash completion
Group:          System/Shells
Requires:       %{name}-utils = %{version}
Requires:       bash-completion
Supplements:    (pulseaudio and bash-completion)

%description bash-completion
Optional dependency offering bash completion for various PulseAudio utilities

%package zsh-completion
Summary:        PulseAudio zsh completion
Group:          System/Shells
Requires:       %{name}-utils = %{version}
Requires:       zsh
Supplements:    (pulseaudio and zsh)

%description zsh-completion
Optional dependency offering zsh completion for various PulseAudio utilities

%package -n system-user-pulse
Summary:        System user for PulseAudio
Group:          System/Base
Requires(pre):  group(audio)
BuildArch:      noarch
%sysusers_requires

%description -n system-user-pulse
System user for PulseAudio

%lang_package

%prep
%setup -q -T -b0
%patch0 -p1
%patch1 -p1
%patch5 -p1
# workaround for Leap 15.x
%if 0%{?suse_version} < 1550
%patch6 -p1
%endif
%patch7 -p1

%build
%meson \
      --auto-features=auto \
      -Dhal-compat=false   \
      -Dgsettings=enabled  \
      -Dgstreamer=enabled  \
      -Ddoxygen=false      \
      -Dsystem_user=pulse  \
      -Dsystem_group=pulse \
      -Daccess_group=pulse-access     \
      -Drunning-from-build-tree=false \
      -Dpulsedsp-location='%{_prefix}/\$LIB/pulseaudio' \
      -Dudevrulesdir="%{_udevrulesdir}"      \
      -Dsystemduserunitdir="%{_userunitdir}" \
      -Db_pie=true \
      %{nil}

%meson_build
%sysusers_generate_pre %{SOURCE10} pulseaudio system-user-pulse.conf

%install
%meson_install
rm -rf \
	"%{buildroot}%{_libdir}"/*.la \
	"%{buildroot}%{_libdir}/pulseaudio/modules"/*.la \
	"%{buildroot}%{_libdir}/pulseaudio"/*.la

# configure --disable-static had no effect; delete manually.
rm -rf "%{buildroot}%{_libdir}"/*.a

# system-wide service (optional)
install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# some HW may get undetected without this (check pulseaudio 6.0RC1 announce)
ln -s default.conf %{buildroot}%{_datadir}/pulseaudio/alsa-mixer/profile-sets/extra-hdmi.conf

# remove xwayland.sessions.d files. Do we have such directory?
rm %{buildroot}%{_sysconfdir}/xdg/Xwayland-session.d/00-pulseaudio-x11

install %{SOURCE2} %{buildroot}%{_bindir}
chmod 755 %{buildroot}%{_bindir}/setup-pulseaudio
install -d %{buildroot}%{_fillupdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
touch %{buildroot}%{_sysconfdir}/profile.d/pulseaudio.sh
touch %{buildroot}%{_sysconfdir}/profile.d/pulseaudio.csh
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 644 %{SOURCE7} %{buildroot}%{_prefix}/lib/tmpfiles.d/pulseaudio.conf
install -m 644 %{SOURCE8} %{buildroot}%{_prefix}/lib/tmpfiles.d/pulseaudio-gdm-hooks.conf
mkdir -p %{buildroot}%{_prefix}/share/factory/var/lib/gdm/.pulse
install -m 644 %{SOURCE1} %{buildroot}%{_prefix}/share/factory/var/lib/gdm/.pulse/default.pa
# create .d conf dirs (since 8.0)
mkdir -p %{buildroot}%{_sysconfdir}/pulse/client.conf.d
install -m 0644 %{SOURCE9} %{buildroot}%{_sysconfdir}/pulse/client.conf.d/50-system.conf
mkdir -p %{buildroot}%{_sysconfdir}/pulse/daemon.conf.d
# create .d startup dirs (since 15.0)
mkdir -p %{buildroot}%{_sysconfdir}/pulse/default.pa.d
mkdir -p %{buildroot}%{_sysconfdir}/pulse/system.pa.d

# Install disable_flat_volumes.conf
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/pulse/daemon.conf.d/60-disable_flat_volumes.conf
# user
install -Dm0644 %{SOURCE10} %{buildroot}%{_sysusersdir}/system-user-pulse.conf
# move dbus-1 system.d file to /usr
install -Dm0644 %{buildroot}%{_sysconfdir}/dbus-1/system.d/pulseaudio-system.conf %{buildroot}%{_datadir}/dbus-1/system.d/pulseaudio-system.conf
rm -rf %{buildroot}%{_sysconfdir}/dbus-1


%find_lang %{name}

%pre -n system-user-pulse -f pulseaudio.pre

%post
/sbin/ldconfig
%tmpfiles_create pulseaudio.conf
if [ ! -f /etc/systemd/user/sockets.target.wants/%{name}.socket ]; then
  echo "Switching PulseAudio activation using systemd user socket."
  echo "Please log out from all sessions once to make it effective."
fi
%systemd_user_post pulseaudio.socket
# FIXME: workaround to make sure the user socket symlink creation (bsc#1083473)
if [ ! -f /etc/systemd/user/sockets.target.wants/%{name}.socket ]; then
  # below should work once when preset is defined properly:
  #  /usr/bin/systemctl --no-reload --global preset pulseaudio.socket
  mkdir -p /etc/systemd/user/sockets.target.wants
  ln -s %{_userunitdir}/%{name}.socket /etc/systemd/user/sockets.target.wants/%{name}.socket
fi
# Update the /etc/profile.d/pulseaudio.* files
setup-pulseaudio --auto > /dev/null

%preun
%systemd_user_preun pulseaudio.socket

%postun
/sbin/ldconfig
%systemd_user_postun pulseaudio.socket

%post   -n libpulse%{soname} -p /sbin/ldconfig
%postun -n libpulse%{soname} -p /sbin/ldconfig
%post   -n libpulse-mainloop-glib%{soname} -p /sbin/ldconfig
%postun -n libpulse-mainloop-glib%{soname} -p /sbin/ldconfig

%pre system-wide
%service_add_pre pulseaudio.service
exit 0

%post system-wide
%service_add_post pulseaudio.service
exit 0

%preun system-wide
%service_del_preun pulseaudio.service
exit 0

%postun system-wide
%service_del_postun pulseaudio.service
exit 0

%post setup
%{fillup_only -an sound}

%post gdm-hooks
%tmpfiles_create pulseaudio-gdm-hooks.conf

%files
%doc README
%license LICENSE GPL LGPL
%{_bindir}/pulseaudio
%{_bindir}/qpaeq
%dir %{_datadir}/pulseaudio
%{_datadir}/pulseaudio/alsa-mixer
%dir %{_libdir}/pulseaudio
%{_libdir}/pulseaudio/libpulsecore-%{drvver}.so
%dir %{_libdir}/pulseaudio/
%dir %{_libdir}/pulseaudio/modules/
%{_libdir}/pulseaudio/modules/libalsa-util.so
%{_libdir}/pulseaudio/modules/libcli.so
%{_libdir}/pulseaudio/modules/liboss-util.so
%{_libdir}/pulseaudio/modules/libprotocol-cli.so
%{_libdir}/pulseaudio/modules/libprotocol-http.so
%{_libdir}/pulseaudio/modules/libprotocol-native.so
%{_libdir}/pulseaudio/modules/libprotocol-simple.so
%{_libdir}/pulseaudio/modules/librtp.so
%{_libdir}/pulseaudio/modules/libwebrtc-util.so
%{_libdir}/pulseaudio/modules/module-alsa-card.so
%{_libdir}/pulseaudio/modules/module-alsa-sink.so
%{_libdir}/pulseaudio/modules/module-alsa-source.so
%{_libdir}/pulseaudio/modules/module-always-sink.so
%{_libdir}/pulseaudio/modules/module-always-source.so
%{_libdir}/pulseaudio/modules/module-allow-passthrough.so
%{_libdir}/pulseaudio/modules/module-augment-properties.so
%{_libdir}/pulseaudio/modules/module-card-restore.so
%{_libdir}/pulseaudio/modules/module-cli.so
%{_libdir}/pulseaudio/modules/module-cli-protocol-tcp.so
%{_libdir}/pulseaudio/modules/module-cli-protocol-unix.so
%{_libdir}/pulseaudio/modules/module-combine.so
%{_libdir}/pulseaudio/modules/module-combine-sink.so
%{_libdir}/pulseaudio/modules/module-console-kit.so
%{_libdir}/pulseaudio/modules/module-dbus-protocol.so
%{_libdir}/pulseaudio/modules/module-default-device-restore.so
%{_libdir}/pulseaudio/modules/module-detect.so
%{_libdir}/pulseaudio/modules/module-device-manager.so
%{_libdir}/pulseaudio/modules/module-device-restore.so
%{_libdir}/pulseaudio/modules/module-echo-cancel.so
%{_libdir}/pulseaudio/modules/module-equalizer-sink.so
%{_libdir}/pulseaudio/modules/module-filter-apply.so
%{_libdir}/pulseaudio/modules/module-filter-heuristics.so
%{_libdir}/pulseaudio/modules/module-http-protocol-tcp.so
%{_libdir}/pulseaudio/modules/module-http-protocol-unix.so
%{_libdir}/pulseaudio/modules/module-intended-roles.so
%{_libdir}/pulseaudio/modules/module-ladspa-sink.so
%{_libdir}/pulseaudio/modules/module-loopback.so
%{_libdir}/pulseaudio/modules/module-match.so
%{_libdir}/pulseaudio/modules/module-mmkbd-evdev.so
%{_libdir}/pulseaudio/modules/module-native-protocol-fd.so
%{_libdir}/pulseaudio/modules/module-native-protocol-tcp.so
%{_libdir}/pulseaudio/modules/module-native-protocol-unix.so
%{_libdir}/pulseaudio/modules/module-null-sink.so
%{_libdir}/pulseaudio/modules/module-null-source.so
%{_libdir}/pulseaudio/modules/module-oss.so
%{_libdir}/pulseaudio/modules/module-pipe-sink.so
%{_libdir}/pulseaudio/modules/module-pipe-source.so
%{_libdir}/pulseaudio/modules/module-position-event-sounds.so
%{_libdir}/pulseaudio/modules/module-remap-sink.so
%{_libdir}/pulseaudio/modules/module-rescue-streams.so
%{_libdir}/pulseaudio/modules/module-role-cork.so
%{_libdir}/pulseaudio/modules/module-rtp-recv.so
%{_libdir}/pulseaudio/modules/module-rtp-send.so
%{_libdir}/pulseaudio/modules/module-rygel-media-server.so
%{_libdir}/pulseaudio/modules/module-simple-protocol-tcp.so
%{_libdir}/pulseaudio/modules/module-simple-protocol-unix.so
%{_libdir}/pulseaudio/modules/module-sine.so
%{_libdir}/pulseaudio/modules/module-sine-source.so
%{_libdir}/pulseaudio/modules/module-stream-restore.so
%{_libdir}/pulseaudio/modules/module-suspend-on-idle.so
%{_libdir}/pulseaudio/modules/module-switch-on-connect.so
%{_libdir}/pulseaudio/modules/module-switch-on-port-available.so
%{_libdir}/pulseaudio/modules/module-systemd-login.so
%{_libdir}/pulseaudio/modules/module-tunnel-sink.so
%{_libdir}/pulseaudio/modules/module-tunnel-sink-new.so
%{_libdir}/pulseaudio/modules/module-tunnel-source.so
%{_libdir}/pulseaudio/modules/module-tunnel-source-new.so
%{_libdir}/pulseaudio/modules/module-udev-detect.so
%{_libdir}/pulseaudio/modules/module-virtual-sink.so
%{_libdir}/pulseaudio/modules/module-virtual-source.so
%{_libdir}/pulseaudio/modules/module-virtual-surround-sink.so
%{_libdir}/pulseaudio/modules/module-volume-restore.so
%{_libdir}/pulseaudio/modules/module-remap-source.so
%{_libdir}/pulseaudio/modules/module-role-ducking.so
%{_udevrulesdir}/90-pulseaudio.rules
%{_mandir}/man1/pulseaudio.1*
%{_mandir}/man5/default.pa.5*
%{_mandir}/man5/pulse-client.conf.5*
%{_mandir}/man5/pulse-daemon.conf.5*
%{_mandir}/man5/pulse-cli-syntax.5*
%dir %{_sysconfdir}/pulse/
%dir %{_sysconfdir}/pulse/daemon.conf.d
%dir %{_sysconfdir}/pulse/default.pa.d
%dir %{_sysconfdir}/pulse/system.pa.d
%config %{_sysconfdir}/pulse/client.conf.d/50-system.conf
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf.d/60-disable_flat_volumes.conf
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf
%config(noreplace) %{_sysconfdir}/pulse/default.pa
%config(noreplace) %{_sysconfdir}/pulse/system.pa
%{_datadir}/dbus-1/system.d/pulseaudio-system.conf
# init
%dir %{_userunitdir}
%{_userunitdir}/%{name}.service
%{_userunitdir}/%{name}.socket
%{_prefix}/lib/tmpfiles.d/pulseaudio.conf
%ghost %dir %{_localstatedir}/lib/pulseaudio

# xwayland integration
%{_userunitdir}/pulseaudio-x11.service

%files setup
%{_bindir}/setup-pulseaudio
%{_fillupdir}/sysconfig.sound-pulseaudio
# created by setup-pulseaudio script
%ghost %{_sysconfdir}/profile.d/pulseaudio.sh
%ghost %{_sysconfdir}/profile.d/pulseaudio.csh

%files gdm-hooks
%attr(0750, gdm, gdm) %ghost %dir %{_localstatedir}/lib/gdm
%attr(0700, gdm, gdm) %ghost %dir %{_localstatedir}/lib/gdm/.pulse
%attr(0600, gdm, gdm) %ghost %{_localstatedir}/lib/gdm/.pulse/default.pa
%dir %{_prefix}/share/factory/var
%dir %{_prefix}/share/factory/var/lib
%dir %{_prefix}/share/factory/var/lib/gdm
%dir %{_prefix}/share/factory/var/lib/gdm/.pulse
%{_prefix}/share/factory/var/lib/gdm/.pulse/default.pa
%{_prefix}/lib/tmpfiles.d/pulseaudio-gdm-hooks.conf

%files -n libpulse%{soname}
%license LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%dir %{_sysconfdir}/pulse/client.conf.d
%config(noreplace) %{_sysconfdir}/pulse/client.conf
%{_libdir}/libpulse.so.%{soname}
%{_libdir}/libpulse.so.%{soname}.*
%{_libdir}/libpulse-simple.so.*
%dir %{_libdir}/pulseaudio
%{_libdir}/pulseaudio/libpulsecommon-%{drvver}.so

%files -n libpulse-devel
%{_includedir}/pulse/
%{_libdir}/libpulse.so
%{_libdir}/libpulse-mainloop-glib.so
%{_libdir}/libpulse-simple.so
%{_libdir}/pkgconfig/libpulse*.pc
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/PulseAudio
%{_libdir}/cmake/PulseAudio/PulseAudio*.cmake
%{_datadir}/vala

%files -n libpulse-mainloop-glib%{soname}
%{_libdir}/libpulse-mainloop-glib.so.%{soname}
%{_libdir}/libpulse-mainloop-glib.so.%{soname}.*
%{_datadir}/glib-2.0/schemas/org.freedesktop.pulseaudio.gschema.xml

%files module-bluetooth
%dir %{_libdir}/pulseaudio
%dir %{_libdir}/pulseaudio/modules
%{_libdir}/pulseaudio/modules/module-bluetooth-policy.so
%{_libdir}/pulseaudio/modules/module-bluetooth-discover.so
%{_libdir}/pulseaudio/modules/libbluez5-util.so
%{_libdir}/pulseaudio/modules/module-bluez5-device.so
%{_libdir}/pulseaudio/modules/module-bluez5-discover.so

%files module-gsettings
%dir %{_libexecdir}/pulse
%dir %{_libdir}/pulseaudio
%dir %{_libdir}/pulseaudio/modules
%{_libdir}/pulseaudio/modules/module-gsettings.so
%{_libexecdir}/pulse/gsettings-helper
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/pulseaudio.convert

%files module-lirc
%dir %{_libdir}/pulseaudio
%dir %{_libdir}/pulseaudio/modules
%{_libdir}/pulseaudio/modules/module-lirc.so

%files module-jack
%dir %{_libdir}/pulseaudio
%dir %{_libdir}/pulseaudio/modules
%{_libdir}/pulseaudio/modules/module-jack-sink.so
%{_libdir}/pulseaudio/modules/module-jack-source.so
%{_libdir}/pulseaudio/modules/module-jackdbus-detect.so

%files module-x11
%dir %{_libdir}/pulseaudio
%dir %{_libdir}/pulseaudio/modules
%{_sysconfdir}/xdg/autostart/pulseaudio.desktop
%{_bindir}/start-pulseaudio-x11
%{_libdir}/pulseaudio/modules/module-x11-bell.so
%{_libdir}/pulseaudio/modules/module-x11-cork-request.so
%{_libdir}/pulseaudio/modules/module-x11-publish.so
%{_libdir}/pulseaudio/modules/module-x11-xsmp.so
%{_mandir}/man1/start-pulseaudio-x11.1*

%files module-zeroconf
%dir %{_libdir}/pulseaudio
%dir %{_libdir}/pulseaudio/modules
%{_libdir}/pulseaudio/modules/libavahi-wrap.so
%{_libdir}/pulseaudio/modules/libraop.so
%{_libdir}/pulseaudio/modules/module-raop-discover.so
%{_libdir}/pulseaudio/modules/module-raop-sink.so
%{_libdir}/pulseaudio/modules/module-zeroconf-discover.so
%{_libdir}/pulseaudio/modules/module-zeroconf-publish.so

%files utils
%{_bindir}/pa-info
%{_bindir}/pacat
%{_bindir}/pacmd
%{_bindir}/pactl
%{_bindir}/paplay
%{_bindir}/parec
%{_bindir}/pamon
%{_bindir}/parecord
%{_bindir}/pax11publish
%{_bindir}/padsp
%{_bindir}/pasuspender
%dir %{_libdir}/pulseaudio
%{_libdir}/pulseaudio/libpulsedsp.so
%{_mandir}/man1/pacat.1*
%{_mandir}/man1/pacmd.1*
%{_mandir}/man1/pactl.1*
%{_mandir}/man1/paplay.1*
%{_mandir}/man1/pasuspender.1*
%{_mandir}/man1/padsp.1*
%{_mandir}/man1/pax11publish.1*
%{_mandir}/man1/pamon.1%{ext_man}
%{_mandir}/man1/parec.1%{ext_man}
%{_mandir}/man1/parecord.1%{ext_man}

%files lang -f %{name}.lang

%files system-wide
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_bashcompletionsdir}/pulseaudio
%{_bashcompletionsdir}/pacat
%{_bashcompletionsdir}/pacmd
%{_bashcompletionsdir}/pactl
%{_bashcompletionsdir}/padsp
%{_bashcompletionsdir}/paplay
%{_bashcompletionsdir}/parec
%{_bashcompletionsdir}/parecord
%{_bashcompletionsdir}/pasuspender

%files zsh-completion
%dir %{_datarootdir}/zsh
%dir %{_datarootdir}/zsh/site-functions/
%{_datarootdir}/zsh/site-functions/_pulseaudio

%files -n system-user-pulse
%{_sysusersdir}/system-user-pulse.conf

%changelog
