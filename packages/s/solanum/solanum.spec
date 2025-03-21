#
# spec file for package solanum
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


Name:           solanum
Version:        0~ch670
Release:        0
Summary:        Scalable IRCv3.2 compliant chat daemon
License:        GPL-2.0-or-later
Group:          Productivity/Networking/IRC
URL:            https://github.com/solanum-ircd/solanum
%define rev 1669c6406cea5092f5ac25634136341a92c6373b
Source:         https://github.com/solanum-ircd/solanum/archive/%rev.tar.gz
# git tag ch efe1f312b5e7e7fab9f713b92a96d7a2b14a5b64 (charybdis 4.1.2); git describe --tags => version
Source9:        example.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  sqlite3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(libcrypto) >= 0.9.7
BuildRequires:  pkgconfig(libssl) >= 0.9.7
BuildRequires:  pkgconfig(zlib)
%sysusers_requires
Obsoletes:      charybdis

%description
Solanum is an IRCv3.2 compatible chat server. It is a continuation of the
Charybdis server and has good documentation and ease of configuration.
It is used by Libera, the largest (as of 2023) IRC network in the world.

%prep
%autosetup -p1 -n %name-%rev

%build
mkdir libltdl
autoreconf -fiv
%configure --sysconfdir="%_sysconfdir/%name" \
	--with-logdir="%_localstatedir/log/%name" \
	--with-rundir="/run" --localstatedir="%_localstatedir/lib"
%make_build

%install
b="%buildroot"
%make_install
mv -v "$b/%_bindir"/* "$b/%_libexecdir/%name/"
find "$b/%_libdir" -type f -name "*.la" -delete

# Move config file samples/documentation out of the way
mv -v "$b/%_sysconfdir/%name"/*.conf "$b/%_datadir/%name/"
# Place some config file that will make it run out of the box on localhost
cp -av "%{S:9}" "$b/%_sysconfdir/%name/ircd.conf"

mkdir -pv "$b/%_localstatedir/lib/solanum" \
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
cat >"$b/%_tmpfilesdir/solanum.conf" <<-EOF
	d /run/%name 0755 solanum solanum -
EOF
echo 'u solanum - "Solanum ircd"' >system-user-solanum.conf
cp -av system-user-solanum.conf "$b/%_sysusersdir/"
%sysusers_generate_pre system-user-solanum.conf random system-user-solanum.conf
# There are no headers installed, so the .pc and devel .so is useless
rm -Rfv "$b/%_libdir/pkgconfig" "$b/%_libdir/libratbox.so"

%pre -f random.pre
%service_add_pre %name.service

%post
%service_add_post %name.service
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
