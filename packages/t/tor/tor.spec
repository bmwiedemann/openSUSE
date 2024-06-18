#
# spec file for package tor
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


%define toruser %{name}
%define torgroup %{name}
%define home_dir %{_localstatedir}/lib/empty
Name:           tor
Version:        0.4.8.12
Release:        0
Summary:        Anonymizing overlay network for TCP (The onion router)
License:        BSD-3-Clause
URL:            https://www.torproject.org/
Source0:        https://www.torproject.org/dist/%{name}-%{version}.tar.gz
# https://support.torproject.org/little-t-tor/verify-little-t-tor/
Source2:        tor.keyring
Source3:        tor.service
Source4:        tor.tmpfiles
Source5:        defaults-torrc
Source6:        tor-master.service
Source100:      https://www.torproject.org/dist/%{name}-%{version}.tar.gz.sha256sum
Source101:      https://www.torproject.org/dist/%{name}-%{version}.tar.gz.sha256sum.asc
Patch0:         tor-0.2.5.x-logrotate.patch
Patch1:         fix-test.patch
BuildRequires:  openssl-devel >= 1.0.1
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pwdutils
BuildRequires:  python3-base
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libevent) >= 2.0.10
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
Requires:       logrotate
Requires(post): %fillup_prereq
Recommends:     torsocks
Provides:       group(%{torgroup})
Provides:       user(%{toruser})
%systemd_ordering
BuildRequires:  libscrypt-devel

%description
Tor is a connection-based low-latency anonymous communication system.

This package provides the "tor" program, which serves as both a client and
a relay node. Scripts will automatically create a "%{toruser}" user and
a "%{torgroup}" group, and set tor up to run as a daemon when the system
is rebooted.

Applications connect to the local Tor proxy using the SOCKS
protocol. The tor client chooses a path through a set of relays, in
which each relay knows its predecessor and successor, but no
others. Traffic flowing down the circuit is unwrapped by a symmetric
key at each relay, which reveals the downstream relay.

Warnings: Tor does no protocol cleaning.  That means there is a danger
that application protocols and associated programs can be induced to
reveal information about the initiator. Tor depends on Privoxy or
similar protocol cleaners to solve this problem. This is alpha code,
and is even more likely than released code to have anonymity-spoiling
bugs. The present network is small -- this further reduces the
strength of the anonymity provided. Tor is not presently suitable
for high-stakes anonymity.

%prep
( cd $(dirname %{SOURCE0}) && echo "$(cat %{SOURCE100} | cut -d' ' -f1) tor-%{version}.tar.gz" | sha256sum --check )
%autosetup -p1

%build
%configure \
	--disable-silent-rules \
	--with-tor-user=%{toruser} \
	--with-tor-group=%{torgroup} \
	--enable-systemd \
	--enable-lzma \
	--enable-zstd \
	--enable-unittests \
	--enable-gcc-warnings-advisory \
	--docdir=%{_docdir}/%{name}
%make_build

%install
%make_install

# missing dirs
install -d -m 700 \
        %{buildroot}%{_localstatedir}/lib/%{name} \
        %{buildroot}%{_localstatedir}/tmp/%{name}

install -d -m 755 \
        %{buildroot}%{_localstatedir}/log/%{name} \
        %{buildroot}/%{_sbindir}

install -m 644 -D %{SOURCE3} %{buildroot}/%{_unitdir}/%{name}.service
install -m 644 -D %{SOURCE6} %{buildroot}/%{_unitdir}/%{name}-master.service
install -m 644 %{SOURCE5} %{buildroot}%{_datadir}/tor/defaults-torrc
install -d -m 0755 %{buildroot}%{_tmpfilesdir}/
install -m 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
ln -s -f service %{buildroot}%{_sbindir}/rc%{name}
ln -s -f service %{buildroot}%{_sbindir}/rc%{name}-master

# sample config files
install -p -m 644 -D src/config/torrc.{sample,minimal} %{buildroot}/%{_sysconfdir}/%{name}
install -p -m 644 src/config/torrc.minimal %{buildroot}/%{_sysconfdir}/%{name}/torrc

# logrotate conf
sed -i -e "s|_tor|tor|g" contrib/operator-tools/tor.logrotate
install -D -m 644 contrib/operator-tools/tor.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

%check
%ifnarch ppc ppc64 ppc64le aarch64 armv7l i586
%make_build check || (
	find -type f -name test-suite.log -print -exec cat {} +
	exit 42
)
%endif

%pre
getent group %{torgroup} >/dev/null || groupadd -r %{torgroup}
getent passwd %{toruser} >/dev/null || useradd -r -g %{torgroup} -d %{home_dir} -s /sbin/nologin -c "User for %{name}" %{toruser}
%service_add_pre tor.service tor-master.service

%post
%fillup_only
%service_add_post tor.service tor-master.service
systemd-tmpfiles --create %{_tmpfilesdir}/tor.conf || :

%preun
%service_del_preun tor.service tor-master.service

%postun
%service_del_postun tor.service tor-master.service

%files
%license LICENSE
%doc README* ChangeLog doc/HACKING doc/man/*.html
%{_mandir}/man*/*
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/geoip*
%{_datadir}/%{name}/defaults-torrc
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(0755,root,%{torgroup}) %{_sysconfdir}/%{name}
%config(noreplace) %attr(0644,root,%{torgroup}) %{_sysconfdir}/%{name}/torrc
%config %attr(0644,root,%{torgroup}) %{_sysconfdir}/%{name}/torrc.*
%attr(0700,%{toruser},%{torgroup}) %dir %{_localstatedir}/lib/%{name}
%attr(0750,%{toruser},%{torgroup}) %dir %{_localstatedir}/log/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-master.service
%{_tmpfilesdir}/%{name}.conf
%{_sbindir}/rc%{name}
%{_sbindir}/rc%{name}-master

%changelog
