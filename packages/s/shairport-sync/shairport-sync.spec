#
# spec file for package shairport-sync
#
# Copyright (c) 2025 SUSE LLC
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


Name:           shairport-sync
Version:        4.3.7
Release:        0
Summary:        An AirPlay audio player
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/mikebrady/shairport-sync
Source0:        https://github.com/mikebrady/shairport-sync/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        airplay-server.xml
Source2:        README.SUSE
Patch1:         harden_shairport-sync.service.patch
BuildRequires:  fdupes
BuildRequires:  firewall-macros
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xxd
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libdaemon)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
Requires:       avahi
Requires:       firewalld
Requires:       nqptp
Requires(pre):  shadow
%{?systemd_ordering}

%description
Shairport Sync is an AirPlay audio player – it plays audio streamed from iTunes,
iOS, Apple TV and macOS devices and AirPlay sources such as Quicktime Player and
ForkedDaapd, among others.

Audio played by a Shairport Sync-powered device stays synchronised with the
source and hence with similar devices playing the same source. In this way,
synchronised multi-room audio is possible for players that support it, such as
iTunes.

Shairport Sync runs on Linux, FreeBSD and OpenBSD. It does not support AirPlay
video or photo streaming.

%prep
%autosetup -p1

cp %{SOURCE2} .

%build
autoreconf -i -f
%configure --with-systemd \
           --with-ssl=openssl \
           --with-alsa \
           --with-pa \
           --with-pw \
           --with-pipe \
           --with-avahi \
           --with-soxr \
           --with-metadata \
           --with-configfiles \
           --with-convolution \
           --with-airplay-2 \
           --without-create-user-group
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_prefix}/lib/firewalld/services
install -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/services/
rm %{buildroot}%{_sysconfdir}/shairport-sync.conf.sample
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
getent group audio >/dev/null || %{_sbindir}/groupadd --system audio
getent group %{name} >/dev/null || %{_sbindir}/groupadd --system %{name}
getent passwd %{name} >/dev/null || %{_sbindir}/useradd --system -c "%{name} User" \
        -d %{_localstatedir}/%{name} -m -g %{name} -s %{_sbindir}/nologin \
        -G audio %{name}
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%firewalld_reload

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md RELEASENOTES.md TROUBLESHOOTING.md README.SUSE
%license LICENSES
%config(noreplace) %{_sysconfdir}/shairport-sync.conf
%{_bindir}/%{name}
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/airplay-server.xml
%{_mandir}/man1/shairport-sync.1%{?ext_man}
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}

%changelog
