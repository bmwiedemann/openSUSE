#
# spec file for package forked-daapd
#
# Copyright (c) 2018 Scott Shambarger
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


%global username daapd
%global groupname daapd

%bcond_without alsa
%bcond_without pulseaudio
%bcond_with spotify
%bcond_without lastfm
%bcond_without chromecast

Summary:        DAAP server for iTunes and Chromecast with MPD and RSP support
License:        GPL-2.0-or-later
Name:           forked-daapd
Version:        27.1
Release:        0
URL:            https://github.com/ejurgensen/forked-daapd
Source0:        https://github.com/ejurgensen/forked-daapd/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        forked-daapd_logrotate

BuildRequires:  ffmpeg-4-libavfilter-devel
BuildRequires:  gperf
BuildRequires:  libgpg-error-devel >= 1.6
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig(avahi-client) >= 0.6.24
BuildRequires:  pkgconfig(json-c), antlr3-tool, antlr3c-devel, libgcrypt-devel >= 1.2.0
BuildRequires:  pkgconfig(libavfilter), pkgconfig(libcurl)
BuildRequires:  pkgconfig(libavformat), pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libsodium), pkgconfig(libplist) >= 0.16
BuildRequires:  pkgconfig(libswscale), pkgconfig(libavutil)
BuildRequires:  pkgconfig(openssl), pkgconfig(libwebsockets) > 2.0.2
BuildRequires:  pkgconfig(sqlite3) >= 3.5.0, pkgconfig(libevent) >= 2.0.0
BuildRequires:  pkgconfig(zlib), pkgconfig(libconfuse), pkgconfig(mxml)

Requires:       logrotate
Requires(pre):  pwdutils

%if %{with alsa}
BuildRequires:  pkgconfig(alsa)
%endif
%if %{with pulseaudio}
BuildRequires:  pkgconfig(libpulse)
%endif
%if %{with spotify}
BuildRequires:  libspotify-devel
%endif
%if %{with chromecast}
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libprotobuf-c)
%endif

%global homedir %{_localstatedir}/lib/%{name}
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
forked-daapd is a DAAP/DACP (iTunes), MPD (Music Player Daemon)
and RSP (Roku) media server.

It has support for AirPlay devices/speakers, Apple Remote (and compatibles),
MPD clients, Chromecast, network streaming, internet radio, Spotify and LastFM.

It does not support streaming video by AirPlay nor Chromecast.

DAAP stands for Digital Audio Access Protocol, and is the protocol used
by iTunes and friends to share/stream media libraries over the network.

forked-daapd is a complete rewrite of mt-daapd (Firefly Media Server).

%prep
%setup -q

%build
%configure \
  --with%{!?with_alsa:out}-alsa --with%{!?with_pulseaudio:out}-pulseaudio \
  --with-libcurl --with-libwebsockets --with-libsodium --with-libplist \
  --with-avahi %{?with_spotify:--enable-spotify} \
  %{?with_lastfm:--enable-lastfm} %{?with_chromecast:--enable-chromecast} \
  --with-daapd-user=%{username} --with-daapd-group=%{groupname}
%make_build

%install
make install DESTDIR=%{buildroot} docdir=%{_pkgdocdir}
rm -f %{buildroot}%{_pkgdocdir}/INSTALL
mkdir -p %{buildroot}%{homedir}
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/%{name}.log
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 forked-daapd.service %{buildroot}%{_unitdir}/%{name}.service
rm -f %{buildroot}%{_libdir}/%{name}/*.la

# rc symlink
install -d %{buildroot}%{_sbindir}
ln -s /sbin/service %{buildroot}%{_sbindir}/rc%{name}

# install logrotate file
install -D -m0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

%pre
getent group %{groupname} >/dev/null || groupadd -r %{groupname}
getent passwd %{username} >/dev/null || \
    useradd -r -g %{groupname} -d %{homedir} -s /sbin/nologin \
    -c '%{name} User' %{username}
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_pkgdocdir}
%config(noreplace) %{_sysconfdir}/forked-daapd.conf
%{_sbindir}/forked-daapd
%{_sbindir}/rcforked-daapd
%{_libdir}/%{name}/
%{_datarootdir}/%{name}/
%{_unitdir}/%{name}.service
%attr(0750,%{username},%{groupname}) %{_localstatedir}/cache/%{name}
%attr(0750,%{username},%{groupname}) %{homedir}
%ghost %{_localstatedir}/log/%{name}.log
%{_mandir}/man?/*
%{_sysconfdir}/logrotate.d/%{name}

%changelog
