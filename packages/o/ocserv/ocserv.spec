#
# spec file for package ocserv
#
# Copyright (c) 2023 SUSE LLC
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


Name:           ocserv
Version:        1.3.0
Release:        0
Summary:        OpenConnect VPN Server
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://ocserv.gitlab.io/www/
#Git-Clone:     https://gitlab.com/openconnect/ocserv.git
Source:         ftp://ftp.infradead.org/pub/ocserv/%{name}-%{version}.tar.xz
Source1:        ftp://ftp.infradead.org/pub/ocserv/%{name}-%{version}.tar.xz.sig
Source2:        ca.tmpl
Source3:        server.tmpl
Source4:        user.tmpl
Source5:        ocserv-forwarding.sh
Source6:        ocserv.firewalld.xml
Source99:       README.SUSE
Source100:      gpgkey-1F42418905D8206AA754CCDC29EE58B996865171.gpg
#PATCH-FIX-UPSTREAM marguerite@opensuse.org $LIBSYSTEMD_DAEMON env is not set on openSUSE
Patch1:         %{name}-enable-systemd.patch
#PATCH-FIX-UPSTREAM marguerite@opensuse.org tweak configuration
Patch2:         %{name}.config.patch
#PATCH-FIX-OPENSUSE marguerite@opensuse.org leap doesn't have LZ4_compress_default
Patch3:         %{name}-LZ4_compress_default.patch
BuildRequires:  autogen
BuildRequires:  dbus-1-devel
BuildRequires:  firewall-macros
BuildRequires:  freeradius-client-devel
BuildRequires:  gperf
BuildRequires:  gpg2
BuildRequires:  ipcalc
BuildRequires:  libev-devel
#!BuildIgnore:  libevent-devel
BuildRequires:  libgnutls-devel >= 3.1.10
BuildRequires:  liblz4-devel
BuildRequires:  libmaxminddb-devel
BuildRequires:  libnl3-devel
BuildRequires:  libprotobuf-c-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libtalloc-devel
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  protobuf-c
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(liboath)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  rubygem(ronn)
# /usr/bin/certtool for generating certificates
Requires:       gnutls >= 3.1.10
%{?systemd_requires}

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
make V=1 %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

install -Dm 0755 %{SOURCE5} %{buildroot}%{_sbindir}/ocserv-forwarding
install -D -m 644 %{SOURCE6} %{buildroot}%{_prefix}/lib/firewalld/services/ocserv.xml

install -d %{buildroot}%{_sysconfdir}/ocserv/certificates
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/ocserv/certificates
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/ocserv/certificates
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/ocserv/certificates
install -m 0644 %{SOURCE99} %{buildroot}%{_sysconfdir}/ocserv/
install -m 0644 doc/sample.config %{buildroot}%{_sysconfdir}/ocserv/ocserv.conf
install -m 0644 doc/sample.passwd %{buildroot}%{_sysconfdir}/ocserv/ocpasswd
install -m 0755 doc/scripts/ocserv-script %{buildroot}%{_bindir}

install -d %{buildroot}%{_unitdir}
# if --with-dubs, here should be "standalone"
install -m 0644 doc/systemd/socket-activated/ocserv.socket %{buildroot}%{_unitdir}
install -m 0644 doc/systemd/socket-activated/ocserv.service %{buildroot}%{_unitdir}

sed -i '/^\[Service\].*/a ExecStopPost=%{_sbindir}/ocserv-forwarding --disable' %{buildroot}%{_unitdir}/ocserv.service
sed -i '/^\[Service\].*/a ExecStartPre=%{_sbindir}/ocserv-forwarding --enable' %{buildroot}%{_unitdir}/ocserv.service

%pre
%service_add_pre ocserv.service ocserv.socket

%post
%service_add_post ocserv.service ocserv.socket
%firewalld_reload

%preun
%service_del_preun ocserv.service ocserv.socket

%postun
%service_del_postun ocserv.service ocserv.socket

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README.md
%license COPYING
%config %{_sysconfdir}/ocserv
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/ocserv.xml
%{_bindir}/occtl
%{_bindir}/ocpasswd
%{_bindir}/ocserv-script
%{_libexecdir}/ocserv-fw
%{_sbindir}/ocserv
%{_sbindir}/ocserv-forwarding
%{_sbindir}/ocserv-worker
%{_unitdir}/ocserv.service
%{_unitdir}/ocserv.socket
%{_mandir}/man8/occtl.8%{ext_man}
%{_mandir}/man8/ocpasswd.8%{ext_man}
%{_mandir}/man8/ocserv.8%{ext_man}

%changelog
