#
# spec file for package rpcbind
#
# Copyright (c) 2021 SUSE LLC
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
Version:        1.2.6
Release:        0
Summary:        Transport independent RPC portmapper
# Git-Web:      http://git.linux-nfs.org/?p=steved/rpcbind.git;a=summary
License:        BSD-4-Clause
Group:          Productivity/Networking/System
URL:            http://rpcbind.sourceforge.net
Source:         https://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Source2:        sysconfig.rpcbind
Source5:        rpc-user.conf
Patch1:         0001-systemd-unit-files.patch
Patch2:         0001-change-lockingdir-to-run.patch
BuildRequires:  libtirpc-devel >= 1.0.1
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libsystemd)
Requires(post): %fillup_prereq
Provides:       portmap
%{?systemd_ordering}
%if 0%{?suse_version} >= 1330
BuildRequires:  libnsl-devel
%endif
%sysusers_requires

%description
Rpcbind is a replacement for portmap. Whereas portmap supports only UDP
and TCP transports over INET (IPv4), rpcbind can be configured to work
on various transports supported by the TI-RPC. This includes TCP and
UDP over IPv6. Moreover, rpcbind provides additional functions in
regards to portmap.

%prep
%autosetup -p1

%build
autoreconf -fiv
export  CFLAGS="%{optflags} -fpie"
export LDFLAGS="-pie -Wl,-z,relro,-z,now"
%configure \
	    --enable-libwrap \
	    --enable-warmstarts \
	    --enable-debug \
	    --with-statedir=%{_rundir}/%{name} \
	    --with-rpcuser=rpc \
	    --with-systemdsystemunitdir=%{_unitdir} \
	    --with-nss-modules="files usrfiles"

make %{?_smp_mflags}
%sysusers_generate_pre %{SOURCE5} rpc rpc-user.conf

%install
%make_install
# fillup template
mkdir -p %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/
# sysusers.d config
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE5} %{buildroot}%{_sysusersdir}/
# create symlink for rcrpcbind
mkdir -p %{buildroot}/%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_bindir}/rpcinfo %{buildroot}%{_sbindir}/rpcinfo
%if 0%{?suse_version} < 1550
mkdir %{buildroot}/sbin
mkdir %{buildroot}/bin
ln -s %{_bindir}/rpcinfo %{buildroot}/sbin/rpcinfo
ln -s %{_bindir}/rpcinfo %{buildroot}/bin/rpcinfo
ln -s %{_sbindir}/%{name} %{buildroot}/sbin/%{name}
%endif

%pre -f rpc.pre
%service_add_pre %{name}.service %{name}.socket

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
%if 0%{?suse_version} < 1550
/sbin/%{name}
/bin/rpcinfo
/sbin/rpcinfo
%endif
%{_sbindir}/%{name}
%{_bindir}/rpcinfo
%{_sbindir}/rpcinfo
%{_sbindir}/rc%{name}
%{_mandir}/*/*
%{_fillupdir}/sysconfig.%{name}
%{_sysusersdir}/rpc-user.conf
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket

%changelog
