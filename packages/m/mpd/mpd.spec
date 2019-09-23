#
# spec file for package mpd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%bcond_with    faad
%bcond_without mpd_iso9660

%if !%{defined _userunitdir}
%define _userunitdir %{_prefix}/lib/systemd/user
%endif
%define mver    0.21
Name:           mpd
Version:        0.21.9
Release:        0
Summary:        Music Player Daemon
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
Url:            https://www.musicpd.org/
Source:         https://www.musicpd.org/download/mpd/%{mver}/mpd-%{version}.tar.xz
Source2:        README.%{name}
Source3:        mpd-user.conf
# PATCH-FEATURE-OPENSUSE mpd-mpdconf_suse.patch --
Patch0:         %{name}-mpdconf_suse.patch
# PATCH-FEATURE-OPENSUSE mpd-docs.patch
Patch3:         mpd-docs.patch
# PATCH-FIX-OPENSUSE mpd-sndfile.patch
Patch4:         mpd-sndfile.patch
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_headers-devel >= 1.58
%else
BuildRequires:  boost-devel >= 1.58
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  gcc
BuildRequires:  gcc-c++
%else
# Leap 42.3+ / SLE12SP3Backports
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%endif
#uildRequires:  cdrkit-cdrtools-compat
%if %{with faad}
BuildRequires:  faad2-devel
%endif
#
BuildRequires:  hicolor-icon-theme
BuildRequires:  libcue-devel
BuildRequires:  libmikmod-devel >= 3.2
BuildRequires:  libmp3lame-devel
BuildRequires:  meson >= 0.47.2
BuildRequires:  pkgconfig
# MPD_ENABLE_AUTO_PKG
BuildRequires:  pkgconfig(alsa) >= 0.9.0
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(audiofile) >= 0.3
BuildRequires:  pkgconfig(avahi-client)
# MPD_ENABLE_AUTO_LIB
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac) >= 1.2
BuildRequires:  pkgconfig(fluidsynth) >= 1.1
BuildRequires:  pkgconfig(icu-i18n) >= 50
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(jack) >= 0.100
BuildRequires:  pkgconfig(libavcodec) >= 56.1
BuildRequires:  pkgconfig(libavformat) >= 56.1
BuildRequires:  pkgconfig(libavutil) >= 54.3
BuildRequires:  pkgconfig(libcdio) >= 2.0.0
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libcurl) >= 7.18
BuildRequires:  pkgconfig(libgme)
%if %{with mpd_iso9660}
BuildRequires:  pkgconfig(libiso9660)
%endif
BuildRequires:  pkgconfig(libmms) >= 0.4
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libmpdclient) >= 2.9
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libnfs) >= 1.11
BuildRequires:  pkgconfig(libpulse) >= 0.9.16
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(samplerate) >= 0.1.3
BuildRequires:  pkgconfig(shine) >= 3.1
BuildRequires:  pkgconfig(shout)
BuildRequires:  pkgconfig(smbclient) >= 0.2
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(sqlite3) >= 3.7.3
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(yajl) >= 2.0
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zziplib) >= 0.13
Requires(pre):  %fillup_prereq
Requires(pre):  pwdutils
Requires(pre):  shadow
%if 0%{?suse_version} >= 1500
BuildRequires:  group(audio)
Requires(pre):  group(audio)
%endif
%{?systemd_requires}

%description
A daemon for playing music (mp3, ogg vorbis, flac, and wav).  Music is
played through the server's audio device.  The daemon stores info
about all available music, and this info can be easily searched and
retrieved.  Player control, info retrieval, and playlist management
can all be managed remotely. There a bunch of clients to control mpd:
for Gnome, KDE, console and Apache (PHP).

Please read README.mpd how to configure it.

%prep
%autosetup -p1

%build
export CC=gcc
export CXX=g++
test -x "$(type -p gcc-7)" && export CC=gcc-7
test -x "$(type -p g++-7)" && export CXX=g++-7
%meson \
    -Dsidplay=disabled \
    -Dfaad=disabled \
    -Diso9660=disabled \
    -Dsyslog=enabled \
    -Deventfd=true \
    -Dsignalfd=true \
    -Depoll=true \
    -Ddatabase=true \
    -Ddaemon=true \
    -Ddocumentation=false \
    -Ddsd=true \
    -Dfifo=true \
    -Dhttpd=true \
    -Dinotify=true \
    -Dipv6=enabled \
    -Dsoundcloud=disabled \
    -Dlibwrap=disabled \
    -Dmikmod=enabled \
    -Dopenal=enabled \
    -Doss=disabled \
    -Dpipe=true \
    -Drecorder=true \
    -Dshout=enabled \
    -Dsolaris_output=enabled \
    -Dtcp=true \
    -Dtest=false \
    -Dlocal_socket=true \
    -Dvorbis=enabled \
    -Dwave_encoder=true \
    -Dicu=enabled \
    -Diconv=enabled \
    -Dsystemd=enabled \
    -Dlibmpdclient=enabled \
    -Dexpat=enabled \
    -Did3tag=enabled \
    -Dsqlite=enabled \
    -Dlibsamplerate=enabled \
    -Dsoxr=enabled \
    -Dcurl=enabled \
    -Dsmbclient=enabled \
    -Dnfs=enabled \
    -Dcdio_paranoia=enabled \
    -Dmms=enabled \
    -Dwebdav=enabled \
    -Dcue=true \
    -Dneighbor=true \
%if %{with mpd_iso9660}
    -Diso9660=enabled \
%endif
    -Dzlib=enabled \
    -Dbzip2=enabled \
    -Dupnp=enabled \
    -Dzzip=enabled \
    -Dadplug=disabled \
    -Daudiofile=enabled \
%if %{with faad}
    -Dfaad=enabled \
%endif
    -Dffmpeg=enabled \
    -Dflac=enabled \
    -Dfluidsynth=enabled \
    -Dgme=enabled \
    -Dmad=enabled \
    -Dmpg123=enabled \
    -Dmodplug=enabled \
    -Dopus=enabled \
    -Dsndfile=enabled \
    -Dmpcdec=disabled \
    -Dwavpack=enabled \
    -Dwildmidi=disabled \
    -Dshine=enabled \
    -Dvorbisenc=enabled \
    -Dlame=enabled \
    -Dtwolame=enabled \
    -Dalsa=enabled \
    -Dsndio=disabled \
    -Djack=enabled \
    -Dao=enabled \
    -Dpulse=enabled \
    -Dtremor=disabled \
    -Dsystemd_system_unit_dir=%{_unitdir} \
    -Dsystemd_user_unit_dir=%{_userunitdir}
%meson_build

%install
%meson_install
# missing dirs
install -d \
        %{buildroot}%{_localstatedir}/lib/%{name}/playlists \
        %{buildroot}%{_sbindir}
# additional docs
install -m 0644 %{SOURCE2} README.mpd
cp -a "%{SOURCE3}" "%{buildroot}%{_docdir}/%{name}/"
ln -s service %{buildroot}%{_sbindir}/rcmpd
rm %{buildroot}%{_libexecdir}/systemd/user/mpd.socket
ln -s ../system/mpd.socket %{buildroot}%{_libexecdir}/systemd/user/mpd.socket

%pre
# add mpd user only when installing first time
getent passwd mpd >/dev/null || useradd -r -g audio -d %{_localstatedir}/lib/mpd -s /sbin/nologin -c "user for mpd" mpd
%service_add_pre mpd.service mpd.socket

%post
%service_add_post mpd.service mpd.socket

%preun
%service_del_preun mpd.service mpd.socket

%postun
%service_del_postun mpd.service mpd.socket

%files
%license COPYING
%doc README.mpd
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_sbindir}/rcmpd
%attr(0755,mpd,audio) %{_localstatedir}/lib/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man5/%{name}.conf.5%{ext_man}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_unitdir}/mpd.service
%{_unitdir}/mpd.socket
%{_libexecdir}/systemd/user/mpd.socket
%{_userunitdir}/mpd.service

%changelog
