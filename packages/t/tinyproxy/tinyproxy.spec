#
# spec file for package tinyproxy
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


Name:           tinyproxy
Version:        1.11.2
Release:        0
Summary:        Minimalist WWW proxy
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Proxy
URL:            https://tinyproxy.github.io/
Source:         https://github.com/tinyproxy/tinyproxy/releases/download/%version/%name-%version.tar.xz
Source1:        %name.logrotate
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  xz
Requires:       logrotate
%sysusers_requires

%description
Tinyproxy is a light-weight HTTP/HTTPS proxy daemon for POSIX
operating systems. Designed from the ground up to be fast and yet
small, it is an ideal solution for use cases such as embedded
deployments where a full featured HTTP proxy is required, but the
system resources for a larger proxy are unavailable.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
b="%buildroot"
install -d -m0750 "$b/%_localstatedir/log/%name"
install -D -m0644 "%SOURCE1" "$b/%_sysconfdir/logrotate.d/%name"

mkdir -p "$b/%_unitdir" "$b/%_tmpfilesdir" "$b/%_sysusersdir"
cat >>"$b/%_unitdir/tinyproxy.service" <<-EOF
	[Unit]
	Description=A small HTTP/1 proxy
	After=network.target named.service nss-lookup.service
	[Service]
	Type=simple
	User=tinyproxy
	Group=tinyproxy
	ExecStart=%_bindir/tinyproxy -d
	[Install]
	WantedBy=multi-user.target
EOF
cat >>"$b/%_tmpfilesdir/%name.conf" <<-EOF
	d /run/tinyproxy 0755 tinyproxy tinyproxy -
EOF
echo 'u tinyproxy - "Tinyproxy" %_datadir/%name' >system-user-tinyproxy.conf
cp -a system-user-tinyproxy.conf "$b/%_sysusersdir/"
%sysusers_generate_pre system-user-tinyproxy.conf random system-user-tinyproxy.conf

rm -rf "$b/%_datadir/doc/%name"

%pre -f random.pre
%service_add_pre tinyproxy.service

%post
systemd-tmpfiles --create tinyproxy.conf || :
%service_add_post tinyproxy.service

%preun
%service_del_preun tinyproxy.service

%postun
%service_del_postun tinyproxy.service

%files
%license COPYING
%doc NEWS README README.md
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*.conf
%config %_sysconfdir/logrotate.d/%name
%_bindir/tinyproxy
%_mandir/man*/*
%_datadir/%name
%_unitdir/*.service
%_tmpfilesdir/*
%_sysusersdir/*
%attr(750,%name,root) %_localstatedir/log/%name

%changelog
