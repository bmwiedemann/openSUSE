#
# spec file for package ocserv
#
# Copyright (c) 2024 SUSE LLC
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


#!BuildIgnore: pkgconfig(libevent)

Name:           ocserv
Version:        1.3.0
Release:        0
Summary:        OpenConnect VPN Server
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://ocserv.gitlab.io/www/
Source:         https://www.infradead.org/%{name}/download/%{name}-%{version}.tar.xz
Source1:        https://www.infradead.org/%{name}/download/%{name}-%{version}.tar.xz.sig
Source2:        ca.tmpl
Source3:        server.tmpl
Source4:        user.tmpl
Source5:        ocserv-forwarding.sh
Source6:        ocserv.firewalld.xml
Source99:       README.SUSE
Source100:      https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x1f42418905d8206aa754ccdc29ee58b996865171#/%{name}.keyring
#PATCH-FIX-UPSTREAM marguerite@opensuse.org $LIBSYSTEMD_DAEMON env is not set on openSUSE
Patch1:         %{name}-enable-systemd.patch
#PATCH-FIX-UPSTREAM marguerite@opensuse.org tweak configuration
Patch2:         %{name}.config.patch
#PATCH-FIX-OPENSUSE marguerite@opensuse.org leap doesn't have LZ4_compress_default
Patch3:         %{name}-LZ4_compress_default.patch
BuildRequires:  autogen
BuildRequires:  firewall-macros
BuildRequires:  firewalld
BuildRequires:  freeradius-client-devel
BuildRequires:  gperf
BuildRequires:  gpg2
BuildRequires:  ipcalc
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  protobuf-c
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gnutls) >= 3.1.10
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(liboath)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  rubygem(ronn-ng)
# /usr/bin/certtool for generating certificates
Requires:       gnutls >= 3.1.10
%{?systemd_requires}

%if 0%{?suse_version} < 1600
ExclusiveArch:  do_not_build
%endif

%description
OpenConnect server (ocserv) is an SSL VPN server. Its purpose is to
be a secure, small, fast and configurable VPN server. It implements
the OpenConnect SSL VPN protocol, and has also (currently experimental)
compatibility with clients using the AnyConnect SSL VPN protocol.
The OpenConnect protocol provides a dual TCP/UDP VPN channel, and
uses the standard IETF security protocols to secure it. The server
is implemented primarily for the GNU/Linux platform but its code
is designed to be portable to other UNIX variants as well.

Ocserv's main features are security through privilege separation
and sandboxing, accounting, and resilience due to a combined use
of TCP and UDP. Authentication occurs in an isolated security
module process, and each user is assigned an unprivileged worker
process, and a networking (tun) device. That not only eases the
control of the resources of each user or group of users, but also
prevents data leak (e.g., heartbleed-style attacks), and privilege
escalation due to any bug on the VPN handling (worker) process.
A management interface allows for viewing and querying logged-in users.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --enable-systemd \
	--enable-seccomp \
	--disable-rpath \
	--enable-local-libopts \
	--enable-libopts-install
%make_build

%install
%make_install DESTDIR=%{buildroot}

install -Dm 0755 %{SOURCE5} %{buildroot}%{_sbindir}/%{name}-forwarding
install -D -m 644 %{SOURCE6} %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml

install -d %{buildroot}%{_sysconfdir}/%{name}/certificates
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/certificates
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}/certificates
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/certificates
install -m 0644 %{SOURCE99} %{buildroot}%{_sysconfdir}/%{name}/
install -m 0644 doc/sample.config %{buildroot}%{_sysconfdir}/ocserv/%{name}.conf
install -m 0644 doc/sample.passwd %{buildroot}%{_sysconfdir}/ocserv/ocpasswd
install -m 0755 doc/scripts/%{name}-script %{buildroot}%{_bindir}

install -d %{buildroot}%{_unitdir}
# if --with-dubs, here should be "standalone"
install -m 0644 doc/systemd/socket-activated/%{name}.socket %{buildroot}%{_unitdir}
install -m 0644 doc/systemd/socket-activated/%{name}.service %{buildroot}%{_unitdir}

sed -i '/^\[Service\].*/a ExecStopPost=%{_sbindir}/%{name}-forwarding --disable' %{buildroot}%{_unitdir}/%{name}.service
sed -i '/^\[Service\].*/a ExecStartPre=%{_sbindir}/%{name}-forwarding --enable' %{buildroot}%{_unitdir}/%{name}.service

%pre
%service_add_pre %{name}.service %{name}.socket

%post
%service_add_post %{name}.service %{name}.socket
%firewalld_reload

%preun
%service_del_preun %{name}.service %{name}.socket

%postun
%service_del_postun %{name}.service %{name}.socket

%files
%doc AUTHORS NEWS README.md
%license COPYING
%config %{_sysconfdir}/%{name}
%{_prefix}/lib/firewalld/services/%{name}.xml
%{_bindir}/occtl
%{_bindir}/ocpasswd
%{_bindir}/%{name}-script
%{_libexecdir}/%{name}-fw
%{_sbindir}/%{name}
%{_sbindir}/%{name}-forwarding
%{_sbindir}/%{name}-worker
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_mandir}/man?/occtl.?%{ext_man}
%{_mandir}/man?/ocpasswd.?%{ext_man}
%{_mandir}/man?/%{name}.?%{ext_man}

%changelog
