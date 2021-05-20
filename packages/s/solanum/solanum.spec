#
# spec file for package solanum
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


Name:           solanum
Version:        0~ch448
Release:        0
Summary:        Scalable IRCv3.2 compliant chat daemon
License:        GPL-2.0-or-later
Group:          Productivity/Networking/IRC
URL:            https://github.com/solanum-ircd/solanum

Source:         %name-%version.tar.xz
Source9:        example.conf
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
BuildRequires:  sqlite3-devel
Requires(pre):  shadow
Obsoletes:      charybdis

%description
Solanum is an IRCv3.2 compatible chat server. It is a continuation of the
Charybdis server and has good documentation and ease of configuration.

Charybdis was used on various networks either as itself, or as
the basis of a customized IRC server implementation. One such
customization is ircd-seven which powers Freenode, the largest IRC
network in the world.

%prep
%autosetup -p1 -n %name-%version

%build
autoreconf -fiv
%configure --sysconfdir="%_sysconfdir/%name" \
	--with-logdir="%_localstatedir/log/%name" \
	--with-rundir="/run" --localstatedir="%_localstatedir/lib"
%make_build

%install
b="%buildroot"
%make_install
mv "$b/%_bindir"/* "$b/%_libexecdir/%name/"
find "$b/%_libdir" -type f -name "*.la" -delete

# Move config file samples/documentation out of the way
mv "$b/%_sysconfdir/%name"/*.conf "$b/%_datadir/%name/"
# Place some config file that will make it run out of the box on localhost
cp "%{S:9}" "$b/%_sysconfdir/%name/ircd.conf"

mkdir -p "$b/%_localstatedir/lib/solanum" \
	"$b/%_localstatedir/log/solanum" "$b/%_sbindir" \
	"$b/%_unitdir" "$b/%_sysusersdir" "$b/%_tmpfilesdir"
cat >"$b/%_unitdir/solanum.service" <<-EOF
	[Unit]
	Description=Solanum Inter Relay Chat server
	[Service]
	ExecStart=%_libexecdir/%name/%name -foreground
	User=solanum
	Group=solanum
	[Install]
	WantedBy=multi-user.target
EOF
cat >"$b/%_sysusersdir/solanum.conf" <<-EOF
	u solanum - "Solanum ircd"
EOF
cat >"$b/%_tmpfilesdir/solanum.conf" <<-EOF
	d /run/%name 0755 solanum solanum -
EOF
# There are no headers installed, so the .pc and devel .so is useless
rm -Rf "$b/%_libdir/pkgconfig" "$b/%_libdir/libratbox.so"

%pre
%sysusers_create_inline 'u solanum - "Solanum ircd"'
%service_add_pre %name.service

%post
%service_add_post %name.service
%sysusers_create %name.conf
%tmpfiles_create %name.conf

%preun
%service_del_preun %name.service

%postun
%service_del_postun %name.service

%files
%attr(0750,root,solanum) %dir %_sysconfdir/%name
%attr(0640,root,solanum) %config %_sysconfdir/%name/*
%_libexecdir/%name/
%_libdir/%name/
%_libdir/libircd.so
%_libdir/librb.so
%_datadir/%name/
%_sysusersdir/*
%_tmpfilesdir/*
%_unitdir/*.service
%attr(0750,solanum,solanum) %_localstatedir/log/%name/
%attr(0750,solanum,solanum) %_localstatedir/lib/%name/
%license LICENSE
%doc NEWS.md

%changelog
