#
# spec file for package tinyproxy
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           tinyproxy
Version:        1.8.4
Release:        0
Summary:        Minimalist WWW proxy
License:        GPL-2.0+
Group:          Productivity/Networking/Web/Proxy
Url:            https://banu.com/tinyproxy/

#Git-Clone:	git://git.banu.com/tinyproxy
#Source:         https://banu.com/pub/tinyproxy/1.8/%name-%version.tar.bz2
#1.8.4 made from Git tag
Source:         %name-%version.tar.xz
Source1:        %name.logrotate
Patch1:         tinyproxy-conf.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libxslt
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
Requires:       logrotate

%description
Tinyproxy is a light-weight HTTP/HTTPS proxy daemon for POSIX
operating systems. Designed from the ground up to be fast and yet
small, it is an ideal solution for use cases such as embedded
deployments where a full featured HTTP proxy is required, but the
system resources for a larger proxy are unavailable.

%prep
%setup -qn %name
%patch -P 1 -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
b="%buildroot"
install -d -m0750 "%buildroot/var/log/%name"
install -D -m0644 "%{S:1}" "$b/%_sysconfdir/logrotate.d/%name"

mkdir -p "$b/%_unitdir" "$b/%_prefix/lib/tmpfiles.d"
cat >>"$b/%_unitdir/tinyproxy.service" <<-EOF
	[Unit]
	Description=A small HTTP/1 proxy
	After=network.target named.service nss-lookup.service
	[Service]
	Type=simple
	ExecStart=/usr/sbin/tinyproxy -d
	CapabilityBoundingSet=CAP_NET_BIND_SERVICE CAP_SETGID CAP_SETUID
	[Install]
	WantedBy=multi-user.target
EOF
cat >>"$b/%_prefix/lib/tmpfiles.d/tinyproxy.conf" <<-EOF
	d /run/tinyproxy 0755 tinyproxy tinyproxy -
EOF
ln -sf service "$b/%_sbindir/rc%name"

%pre
getent group tinyproxy >/dev/null || groupadd -r tinyproxy || :
getent passwd tinyproxy >/dev/null || \
	useradd -c "Tinyproxy" -d "%_datadir/%name" -g tinyproxy \
	-r -s /bin/false tinyproxy || :
%service_add_pre tinyproxy.service

%post
systemd-tmpfiles --create tinyproxy.conf || :
%service_add_post tinyproxy.service

%preun
%service_del_preun tinyproxy.service

%postun
%service_del_postun tinyproxy.service

%files
%defattr(-,root,root)
%config(noreplace) %_sysconfdir/*.conf
%config %_sysconfdir/logrotate.d/%name
%_sbindir/*
%_mandir/man*/*
%_datadir/%name
%_unitdir/*.service
%_prefix/lib/tmpfiles.d/
%attr(750,%name,root) /var/log/%name

%changelog
