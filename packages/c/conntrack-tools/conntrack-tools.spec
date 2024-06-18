#
# spec file for package conntrack-tools
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


%if !%{defined _fillupdir}
# Leap/TW 15+
%define _fillupdir /var/adm/fillup-templates
%endif

Name:           conntrack-tools
Version:        1.4.8
Release:        0
Summary:        Userspace tools for interacting with the Connection Tracking System
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://conntrack-tools.netfilter.org/
#Git-Clone:	git://git.netfilter.org/conntrack-tools
Source:         https://www.netfilter.org/projects/conntrack-tools/files/conntrack-tools-%version.tar.xz
Source2:        https://www.netfilter.org/projects/conntrack-tools/files/conntrack-tools-%version.tar.xz.sig
Source3:        %name.keyring
Source5:        conntrackd.service
Source6:        conntrackd.README.SUSE
Source7:        conntrackd.logrotate
Source8:        conntrackd.sysconfig
Source9:        conntrackd.conf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex >= 2.5.33
BuildRequires:  libtool
BuildRequires:  pkg-config >= 0.21
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  pkgconfig(libmnl) >= 1.0.3
BuildRequires:  pkgconfig(libnetfilter_conntrack) >= 1.0.9
BuildRequires:  pkgconfig(libnetfilter_cthelper) >= 1.0.0
BuildRequires:  pkgconfig(libnetfilter_cttimeout) >= 1.0.0
BuildRequires:  pkgconfig(libnetfilter_queue) >= 1.0.2
BuildRequires:  pkgconfig(libnfnetlink) >= 1.0.1
BuildRequires:  pkgconfig(libsystemd) >= 227
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libtirpc)
%endif

%description
The conntrack/nfct utilities provide the userspace interface to the
Netfilter connection tracking, replacing
/proc/net/ip_conntrack. The tools can be used to search, list,
inspect and maintain the connection tracking subsystem of the Linux
kernel.

%package -n conntrackd
Summary:        Connection tracking daemon
Group:          Productivity/Networking/Security
Provides:       conntrack-tools:/usr/sbin/conntrackd
Requires:       conntrack-tools = %version-%release
Requires(post): fillup
Recommends:     logrotate

%description -n conntrackd
conntrackd is the user-space daemon for the Netfilter connection tracking
system. This daemon synchronizes connection tracking states between several
replica firewalls.

%prep
%setup -q
find doc -type f -name "*.orig" -delete
find doc -type f -exec chmod -x "{}" "+"

%build
autoreconf -vif
%configure --disable-static --enable-systemd
# CC       read_config_lex.o
#read_config_lex.l:24:28: fatal error: read_config_yy.h: No such file or
#directory
%make_build -j1

%install
%make_install
b="%buildroot"
find "$b/%_libdir" -type f -name "*.la" -delete
install -Dpm0644 "%_sourcedir"/conntrackd.service "$b/%_unitdir/conntrackd.service"
install -Dpm0644 "%_sourcedir/conntrackd.sysconfig" "$b/%_fillupdir/sysconfig.conntrackd"
install -Dpm0644 "%_sourcedir/conntrackd.logrotate" "$b/%_sysconfdir/logrotate.d/conntrackd"
b="%buildroot/%_docdir/%name"
mkdir -p "$b"
cp -a "%_sourcedir/conntrackd.README.SUSE" "%_sourcedir/conntrackd.conf" "$b/"

%pre -n conntrackd
%service_add_pre conntrackd.service

%post -n conntrackd
%fillup_only -n conntrackd
if [ "$1" -eq 1 -a ! -e "%_sysconfdir/conntrackd/conntrackd.conf" ]; then
	install -Dpm0644 "%_docdir/%name/conntrackd.conf" "%_sysconfdir/conntrackd/conntrackd.conf"
fi
%service_add_post conntrackd.service

%preun -n conntrackd
%service_del_preun conntrackd.service

%postun -n conntrackd
%service_del_postun conntrackd.service

%files
%_sbindir/conntrack
%_sbindir/nfct
%_mandir/man8/conntrack.8*
%_mandir/man8/nfct.8*
# Shared betweenn nfct and conntrackd:
%_libdir/%name/

%files -n conntrackd
%_sysconfdir/logrotate.d/conntrackd*
%_sbindir/conntrackd
%_mandir/man5/conntrackd*
%_mandir/man8/conntrackd*
%dir %_docdir/%name
%_docdir/%name/conntrackd*
%_unitdir/conntrackd*
%_fillupdir/*conntrackd

%changelog
