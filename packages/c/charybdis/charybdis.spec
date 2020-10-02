#
# spec file for package charybdis
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


Name:           charybdis
Version:        4.1.2
Release:        0
Summary:        Scalable IRCv3.2 compliant chat daemon
License:        GPL-2.0-or-later
Group:          Productivity/Networking/IRC
URL:            https://github.com/charybdis-ircd/charybdis

#Git-Clone:	https://github.com/charybdis-ircd/charybdis
Source:         https://github.com/charybdis-ircd/charybdis/archive/%name-%version.tar.gz
Source9:        example.conf
Patch1:         0001-Set-EXTERNAL_BUILD_TIMESTAMP-from-SOURCE_DATE_EPOCH.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libcrypto) >= 0.9.7
BuildRequires:  pkgconfig(libssl) >= 0.9.7
BuildRequires:  pkgconfig(zlib)
Requires(pre):  shadow

%description
Charybdis is the IRCv3 reference implementation. It has good
documentation and ease of configuration.

Charybdis is used on various networks either as itself, or as the
basis of a customized IRC server implementation. One such
customization is ircd-seven which powers Freenode, the largest IRC
network in the world.

%prep
%autosetup -p1 -n %name-%name-%version

%build
autoreconf -fiv
%configure --sysconfdir="%_sysconfdir/%name" \
	--with-logdir="%_localstatedir/log/%name" \
	--with-rundir="/run" --localstatedir="%_localstatedir/lib"
%make_build CHARYBDIS_VERSION="%version"

%install
b="%buildroot"
%make_install
mv "$b/%_bindir"/* "$b/%_libexecdir/%name/"
find "$b/%_libdir" -type f -name "*.la" -delete

# Move config file samples/documentation out of the way
mv "$b/%_sysconfdir/%name"/*.conf "$b/%_datadir/%name/"
# Place some config file that will make it run out of the box on localhost
cp "%{S:9}" "$b/%_sysconfdir/%name/ircd.conf"

mkdir -p "$b/%_localstatedir/lib/charybdis" \
	"$b/%_localstatedir/log/charybdis" "$b/%_sbindir" \
	"$b/%_unitdir" "$b/%_prefix/lib/tmpfiles.d"
ln -s service "$b/%_sbindir/rc%name"
cat >"$b/%_unitdir/charybdis.service" <<-EOF
	[Unit]
	Description=Charybdis Inter Relay Chat server
	[Service]
	ExecStart=%_libexecdir/%name/%name -foreground
	User=charybdis
	Group=charybdis
	[Install]
	WantedBy=multi-user.target
EOF
cat >"$b/%_prefix/lib/tmpfiles.d/charybdis.conf" <<-EOF
	d /run/%name 0755 charybdis charybdis -
EOF
# There are no headers installed, so the .pc and devel .so is useless
rm -Rf "$b/%_libdir/pkgconfig" "$b/%_libdir/libratbox.so"

%pre
getent group charybdis >/dev/null || \
	/usr/sbin/groupadd -r charybdis
getent passwd charybdis >/dev/null || \
	/usr/sbin/useradd -r -g charybdis -s /bin/false \
	-c "Charybdis Inter Relay Chat daemon" \
	-d "%_localstatedir/lib/charybdis" charybdis
%service_add_pre %name.service

%post
%service_add_post %name.service
systemd-tmpfiles --create %name.conf || :

%preun
%service_del_preun %name.service

%postun
%service_del_postun %name.service

%files
%attr(0750,root,charybdis) %dir %_sysconfdir/%name
%attr(0640,root,charybdis) %config %_sysconfdir/%name/*
%_sbindir/rc%name
%_libexecdir/%name/
%_libdir/%name/
%_libdir/libircd.so
%_libdir/librb.so
%_datadir/%name/
%_prefix/lib/tmpfiles.d/
%_unitdir/*.service
%attr(0750,charybdis,charybdis) %_localstatedir/log/%name/
%attr(0750,charybdis,charybdis) %_localstatedir/lib/%name/
%license LICENSE
%doc NEWS.md

%changelog
