#
# spec file for package atheme
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


Name:           atheme
%define lname	libathemecore1
%define rversion	7.2.10-r2
Version:        7.2.10.r2
Release:        0
Summary:        Extensible IRC services
License:        MIT
Group:          Productivity/Networking/IRC
URL:            https://atheme.github.io/atheme.html

Source:         https://github.com/atheme/atheme/releases/download/v%rversion/%name-v%rversion.tar.xz
Source9:        example.conf
Patch1:         atheme-lockmodes.diff
Patch2:         atheme-nodate.diff
Patch3:         atheme-serno.diff
BuildRequires:  cracklib-devel
BuildRequires:  fdupes
BuildRequires:  libopenssl-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libmowgli-2) >= 2.0.0.g185
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libqrencode)
%define atheme_home /var/lib/atheme
%define atheme_log  /var/log/atheme
%define atheme_run  /run/atheme
Requires(pre): shadow

%description
Atheme is a set of modular IRC services (NickServ, ChanServ, etc.)
designed to link with more than 20 kinds of IRCds.
Atheme offers both an C API and a Perl interface.

%package -n %lname
Summary:        The Atheme IRC Services core library
Group:          System/Libraries

%description -n %lname
Atheme is a set of modular IRC services (NickServ, ChanServ, etc.)
designed to link with many kinds of IRCds.

%package devel
Summary:        Development files for the Atheme IRC Services core
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Atheme is a set of modular IRC services (NickServ, ChanServ, etc.)
designed to link with many kinds of IRCds.

This package contains the development headers for the library found
in %lname.

%prep
%autosetup -p1 -n %name-v%rversion
# nudge atheme in the direction of using the system-provided libmowgli
rm -Rf libmowgli-2
# ignore contrib modules
mkdir -p libmowgli-2 modules/contrib
touch libmowgli-2/Makefile modules/contrib/Makefile

%build
export RUNDIR="/run"
%configure \
	--sysconfdir="%_sysconfdir/%name" \
	--bindir="%_sbindir" \
	--docdir="%_docdir/%name" \
	--enable-fhs-paths \
	--enable-warnings \
	--enable-large-net \
	--with-pcre
%make_build

%install
export RUNDIR="/run"
%make_install DOCDIR="%_docdir/%name"
b="%buildroot"

# additional documentation
mkdir -p "$b/%_docdir/%name"
install -m 0644 contrib/*.php contrib/*.pl TODO "$b/%_docdir/%name"

mkdir -p "$b/%_unitdir" "$b/%_prefix/lib/tmpfiles.d"
ln -s service "$b/%_sbindir/rcatheme"
cat >"$b/%_unitdir/atheme.service" <<-EOF
	[Unit]
	Description=Atheme IRC Services
	[Service]
	ExecStart=/usr/sbin/atheme-services -n
	User=atheme
	Group=atheme
	[Install]
	WantedBy=multi-user.target
EOF
cat >"$b/%_prefix/lib/tmpfiles.d/atheme.conf" <<-EOF
	d /run/atheme 0755 atheme atheme -
EOF

mv "$b/%_sysconfdir/%name"/*example "$b/%_docdir/%name/"
install -pm0644 "%{S:9}" "$b/%_sysconfdir/%name/atheme.conf"
%find_lang %name
mv "$b/%_sbindir/ecdsakeygen" "$b/%_sbindir/atheme-ecdsakeygen"
mv "$b/%_sbindir/dbverify" "$b/%_sbindir/atheme-dbverify"
%fdupes %buildroot/%_prefix

%pre
/usr/bin/getent group atheme >/dev/null || \
	/usr/sbin/groupadd -r atheme
/usr/bin/getent passwd atheme >/dev/null || \
	/usr/sbin/useradd -r -g atheme -s /bin/false \
	-c "Atheme IRC Services daemon" -d "%atheme_home" \
	atheme
%service_add_pre atheme.service

%post
%service_add_post atheme.service
systemd-tmpfiles --create atheme.conf || :

%preun
%service_del_preun atheme.service

%postun
%service_del_postun atheme.service

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -f %name.lang
%dir %attr(750,root,atheme) %_sysconfdir/%name/
%config(noreplace) %attr(640,root,atheme) %_sysconfdir/%name/atheme.conf
%config(noreplace) %attr(644,root,atheme) %_sysconfdir/%name/atheme.motd
%_sbindir/atheme-services
%_sbindir/*dbverify
%_sbindir/*ecdsakeygen
%_sbindir/rcatheme
%_libdir/%name/
%_datadir/%name/
%_docdir/%name/
%dir %attr(750,atheme,atheme) %atheme_home
%dir %attr(750,atheme,atheme) %atheme_log
%_unitdir/*.service
%_prefix/lib/tmpfiles.d/

%files -n %lname
%_libdir/libathemecore.so.1*

%files devel
%_includedir/atheme/
%_libdir/libathemecore.so
%_libdir/pkgconfig/atheme-services.pc

%changelog
