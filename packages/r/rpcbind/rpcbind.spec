#
# spec file for package rpcbind
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           rpcbind
Version:        1.2.5
Release:        0
Summary:        Transport independent RPC portmapper
# Git-Web:      http://git.linux-nfs.org/?p=steved/rpcbind.git;a=summary
License:        BSD-4-Clause
Group:          Productivity/Networking/System
URL:            http://rpcbind.sourceforge.net
Source:         https://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Source2:        sysconfig.rpcbind
Source4:        pmap_set.c
Patch1:         0001-systemd-unit-files.patch
Patch2:         0001-change-lockingdir-to-run.patch
Patch31:        0031-rpcbind-manpage.patch
BuildRequires:  libtirpc-devel >= 1.0.1
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libsystemd)
Requires(post): %fillup_prereq
Requires(pre):  shadow
Provides:       portmap
%{?systemd_requires}
%if 0%{?suse_version} >= 1330
BuildRequires:  libnsl-devel
Requires(pre):  group(nobody)
%endif

%description
Rpcbind is a replacement for portmap. Whereas portmap supports only UDP
and TCP transports over INET (IPv4), rpcbind can be configured to work
on various transports supported by the TI-RPC. This includes TCP and
UDP over IPv6. Moreover, rpcbind provides additional functions in
regards to portmap.

%prep
%setup -q
cp %{SOURCE4} .
%patch1 -p1
%patch2 -p1
%patch31 -p1

%build
autoreconf -fiv
export  CFLAGS="%{optflags} -fpie"
export LDFLAGS="-pie -Wl,-z,relro,-z,now"
%configure \
	    --bindir=/bin \
	    --sbindir=/sbin \
	    --enable-libwrap \
	    --enable-warmstarts \
	    --disable-debug \
	    --with-statedir=%{_rundir}/%{name} \
	    --with-rpcuser=rpc \
	    --with-systemdsystemunitdir=%{_unitdir}

make %{?_smp_mflags}
gcc -I/usr/include/tirpc -pie -fpie -fwhole-program -Wl,-z,relro,-z,now %{optflags} pmap_set.c -o pmap_set -ltirpc

%install
%make_install
# fillup template
mkdir -p %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/
#
install -m 755 pmap_set %{buildroot}/sbin/pmap_set2
# create symlink for rcrpcbind
mkdir -p %{buildroot}/%{_sbindir}
ln -s service %{buildroot}/%{_sbindir}/rc%{name}
ln -s /bin/rpcinfo %{buildroot}/sbin/rpcinfo

%pre
%service_add_pre %{name}.service %{name}.socket

# Add "rpc" user
getent passwd rpc >/dev/null || %{_sbindir}/useradd -r -g nobody -d %{_localstatedir}/lib/empty -s /sbin/nologin -c "user for rpcbind" rpc
exit 0

%preun
%service_del_preun %{name}.service %{name}.socket

%post
%{fillup_only -n rpcbind}
%service_add_post %{name}.socket %{name}.service

%postun
%service_del_postun %{name}.socket %{name}.service

%files
%license COPYING
%doc AUTHORS README
/sbin/pmap_set2
/sbin/%{name}
/bin/rpcinfo
/sbin/rpcinfo
%{_sbindir}/rc%{name}
%{_mandir}/*/*
%{_fillupdir}/sysconfig.%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket

%changelog
