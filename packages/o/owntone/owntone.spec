#
# spec file for package owntone
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2018 Scott Shambarger
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


%global username owntone
%global groupname owntone

%bcond_without alsa
%bcond_without pulseaudio
%bcond_with spotify
%bcond_without lastfm
%bcond_without chromecast

Summary:        DAAP server for iTunes and Chromecast with MPD and RSP support
License:        GPL-2.0-or-later
Name:           owntone
Version:        28.5
Release:        0
URL:            https://github.com/owntone/owntone-server
Source0:        %url/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        owntone_logrotate
Patch0:         harden_owntone.service.patch

Provides:       forked-daapd = %version
Obsoletes:      forked-daapd < 28

BuildRequires:  antlr3-tool
BuildRequires:  antlr3c-devel
BuildRequires:  gperf
BuildRequires:  libgcrypt-devel >= 1.2.0
BuildRequires:  libgpg-error-devel >= 1.6
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig(avahi-client) >= 0.6.24
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libconfuse) >= 3.0
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent) >= 2.0.0
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libwebsockets) > 2.0.2
BuildRequires:  pkgconfig(mxml)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3) >= 3.5.0
BuildRequires:  pkgconfig(zlib)

Requires:       logrotate
Requires(pre):  pwdutils

%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libplist-2.0)
%else
BuildRequires:  pkgconfig(libplist)
%endif

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
owntone is a DAAP/DACP (iTunes), MPD (Music Player Daemon)
and RSP (Roku) media server.

It has support for AirPlay devices/speakers, Apple Remote (and compatibles),
MPD clients, Chromecast, network streaming, internet radio, Spotify and LastFM.

It does not support streaming video by AirPlay nor Chromecast.

DAAP stands for Digital Audio Access Protocol, and is the protocol used
by iTunes and friends to share/stream media libraries over the network.

owntone is a complete rewrite of mt-daapd (Firefly Media Server).

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%optflags -fcommon"
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
install -m 0644 owntone.service %{buildroot}%{_unitdir}/%{name}.service
rm -rf %{buildroot}/etc/systemd
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

# try to rescuce former data due to package rename
if test -d /var/cache/forked-daapd -a ! -e %{_localstatedir}/cache/%{name}; then
echo "Package rename: moving database"
mv /var/cache/forked-daapd %{_localstatedir}/cache/%{name}
chown -R %{username}:%{groupname} %{_localstatedir}/cache/%{name}
fi
if test -e  %{_sysconfdir}/forked-daapd.conf -a ! -e %{_sysconfdir}/owntone.conf; then
echo "Package rename: move config and adapting it..."
mv %{_sysconfdir}/forked-daapd.conf %{_sysconfdir}/owntone.conf
sed -i 's,uid = "daapd",uid = "%{username}",' %{_sysconfdir}/owntone.conf
sed -i 's,logfile = "/var/log/forked-daapd.log",logfile = "/var/log/%{name}.log",' %{_sysconfdir}/owntone.conf
fi

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
%config(noreplace) %{_sysconfdir}/owntone.conf
%{_sbindir}/owntone
%{_sbindir}/rcowntone
%{_libdir}/%{name}/
%{_datarootdir}/%{name}/
%{_unitdir}/%{name}.service
%attr(0750,%{username},%{groupname}) %{_localstatedir}/cache/%{name}
%attr(0750,%{username},%{groupname}) %{homedir}
%ghost %{_localstatedir}/log/%{name}.log
%{_mandir}/man?/*
%{_sysconfdir}/logrotate.d/%{name}

%changelog
