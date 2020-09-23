#
# spec file for package mpd
#
# Copyright (c) 2020 SUSE LLC
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


%define mver    0.21
%bcond_with    faad
%bcond_without mpd_iso9660
Name:           mpd
Version:        0.21.26
Release:        0
Summary:        Music Player Daemon
License:        GPL-2.0-or-later
URL:            https://www.musicpd.org
Source0:        https://www.musicpd.org/download/mpd/%{mver}/mpd-%{version}.tar.xz
Source1:        README.%{name}
Source2:        mpd-user.conf
# PATCH-FEATURE-OPENSUSE mpd-mpdconf_suse.patch --
Patch0:         %{name}-mpdconf_suse.patch
# PATCH-FEATURE-OPENSUSE mpd-docs.patch
Patch1:         mpd-docs.patch
# PATCH-FIX-OPENSUSE mpd-sndfile.patch
Patch2:         mpd-sndfile.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  group(audio)
#
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_headers-devel
BuildRequires:  libcue-devel
# MPD_ENABLE_AUTO_LIB
BuildRequires:  libgcrypt-devel
BuildRequires:  libmikmod-devel
BuildRequires:  libmp3lame-devel
BuildRequires:  meson >= 0.47.2
BuildRequires:  pkgconfig
# MPD_ENABLE_AUTO_PKG
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(audiofile)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcdio) >= 2.0.0
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libmms)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libnfs)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(shine)
BuildRequires:  pkgconfig(shout)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(yajl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zziplib)
Requires(pre):  %fillup_prereq
Requires(pre):  group(audio)
Requires(pre):  shadow
%{?systemd_requires}
%if %{with faad}
BuildRequires:  faad2-devel
%endif
%if %{with mpd_iso9660}
BuildRequires:  pkgconfig(libiso9660)
%endif

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
install -m 0644 %{SOURCE1} README.mpd
cp -a "%{SOURCE2}" "%{buildroot}%{_docdir}/%{name}/"
ln -s service %{buildroot}%{_sbindir}/rcmpd
rm %{buildroot}%{_userunitdir}/mpd.socket
ln -s ../system/mpd.socket %{buildroot}%{_userunitdir}/mpd.socket

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
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/%{name}.conf.5%{?ext_man}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_unitdir}/mpd.service
%{_unitdir}/mpd.socket
%{_userunitdir}/mpd.socket
%{_userunitdir}/mpd.service

%changelog
