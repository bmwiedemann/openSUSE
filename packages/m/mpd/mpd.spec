#
# spec file for package mpd
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


%define mver    0.23
%bcond_with    faad
%bcond_without mpd_iso9660
Name:           mpd
Version:        0.23.11
Release:        0
Summary:        Music Player Daemon
License:        GPL-2.0-or-later
URL:            https://musicpd.org
Source0:        https://musicpd.org/download/%{name}/%{mver}/%{name}-%{version}.tar.xz
Source1:        https://musicpd.org/download/%{name}/%{mver}/%{name}-%{version}.tar.xz.sig
Source2:        README.%{name}
Source3:        %{name}-user.conf
Source4:        %{name}.firewalld
Source5:        %{name}.tmpfiles.d
Source9:        %{name}.keyring
Patch0:         %{name}-conf.patch
Patch1:         %{name}-sndfile.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_headers-devel
BuildRequires:  libcue-devel
BuildRequires:  group(audio)
# MPD_ENABLE_AUTO_LIB
BuildRequires:  libgcrypt-devel
BuildRequires:  libmikmod-devel
BuildRequires:  libmp3lame-devel
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
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
BuildRequires:  pkgconfig(fmt)
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
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(liburing)
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

%package doc
Summary:        Additional Package Documentation
BuildArch:      noarch

%description doc
This package contains optional documentation provided in addition to this package's base documentation.

%prep
%autosetup -p1

%build
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
    -Ddocumentation=enabled \
    -Dmanpages=true \
    -Ddsd=true \
    -Dfifo=true \
    -Dhttpd=true \
    -Dinotify=true \
    -Dipv6=enabled \
    -Dsoundcloud=disabled \
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
    -Dupnp=pupnp \
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
    -Dpcre=enabled \
    -Dsystemd_system_unit_dir=%{_unitdir} \
    -Dsystemd_user_unit_dir=%{_userunitdir}
%meson_build

%install
%meson_install
mv %{buildroot}%{_datadir}/doc/%{name}/html .
rm -r %{buildroot}%{_datadir}/doc/%{name}
install -pm0644 %{SOURCE2} %{SOURCE3} .
install -Dpm0644 %{SOURCE4} %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml
install -Dpm0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dpm0644 doc/mpdconf.example %{buildroot}%{_sysconfdir}/%{name}.conf
# Remove duplicate for mpd.socket and replace it with a symlink.
rm %{buildroot}%{_userunitdir}/%{name}.socket
ln -s ../system/%{name}.socket %{buildroot}%{_userunitdir}/%{name}.socket
mkdir %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rc%{name}
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/playlists

%pre
getent passwd %{name} >/dev/null || useradd -rc 'Music Player Daemon' -s /bin/false -d %{_localstatedir}/lib/%{name} -g audio %{name}
%service_add_pre %{name}.service %{name}.socket

%post
%service_add_post %{name}.service %{name}.socket
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun
%service_del_preun %{name}.service %{name}.socket

%postun
%service_del_postun %{name}.service %{name}.socket

%files
%license COPYING
%doc AUTHORS NEWS README.md README.%{name} %{name}-user.conf doc/mpdconf.example
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_sbindir}/rc%{name}
%attr(0755,mpd,audio) %{_localstatedir}/lib/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/%{name}.conf.5%{?ext_man}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_userunitdir}/%{name}.socket
%{_userunitdir}/%{name}.service
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/%{name}.xml
%{_tmpfilesdir}/%{name}.conf
%ghost %dir /run/%{name}

%files doc
%doc html/*.{html,js} html/_static

%changelog
