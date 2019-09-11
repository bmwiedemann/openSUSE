#
# spec file for package ypserv
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           ypserv
Version:        4.1
Release:        0
Summary:        YP - (NIS)-Server
License:        GPL-2.0-only
Group:          Productivity/Networking/NIS
URL:            https://github.com/thkukuk/ypserv
Source:         ypserv-%{version}.tar.xz
Source1:        ypserv.init
Source2:        yppasswdd.init
Source3:        ypxfrd.init
Source4:        sysconfig.ypserv
Source6:        ypserv.service
Source7:        yppasswdd.service
Source8:        ypxfrd.service
Source9:        yppasswdd-systemd-exec
Source10:       ypserv.tmpfiles
Patch1:         ypserv-4.1.diff
BuildRequires:  gdbm-devel
BuildRequires:  openslp-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnsl)
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(libtirpc)
Requires:       gawk
Requires:       make
Requires:       rpcbind
Requires(post): %fillup_prereq
%{?systemd_requires}

%description
The Network Information Service (NIS) provides a simple network
lookup service consisting of databases and processes. It was formerly
known as Sun Yellow Pages (YP). The functionality of the two remains
the same; only the name has changed. Its purpose is to provide
information, that has to be known throughout the network, to all
machines on the network. Information likely to be distributed by
NIS is:

    login names/passwords/home directories (%{_sysconfdir}/passwd)
    group information (%{_sysconfdir}/group)
    host names and IP numbers (%{_sysconfdir}/hosts)

So, for example, if your password entry is recorded in the NIS passwd
database, you will be able to login on all machines on the net which
have the NIS client programs running.

%prep
%setup -q
%patch1

%build
%configure --enable-fqdn --libexecdir="%{_libexecdir}/yp"
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_libexecdir}/yp
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_initddir}
DOCDIR=%{_defaultdocdir}/yp
install -d -m 755 $RPM_BUILD_ROOT${DOCDIR}
install -d -m 755 $RPM_BUILD_ROOT${DOCDIR}/ypserv
#install contrib/ypslave $RPM_BUILD_ROOT/usr/sbin
install -m 644 etc/ypserv.conf %{buildroot}%{_sysconfdir}/
install -m 644 etc/securenets %{buildroot}%{_libexecdir}/yp/securenets.example
mv %{buildroot}%{_localstatedir}/yp/Makefile %{buildroot}%{_libexecdir}/yp/ypMakefile
# install sysconfig.ypserv
install -m 644 %{SOURCE4} %{buildroot}%{_fillupdir}
# install ypserv.conf in tmpfiles.d
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 644 %{SOURCE10} %{buildroot}%{_prefix}/lib/tmpfiles.d/ypserv.conf
# install systemd files
install -m 644 %{SOURCE6} %{buildroot}%{_unitdir}/ypserv.service
install -m 644 %{SOURCE7} %{buildroot}%{_unitdir}/yppasswdd.service
install -m 644 %{SOURCE8} %{buildroot}%{_unitdir}/ypxfrd.service
install -m 755 %{SOURCE9} %{buildroot}%{_libexecdir}/yp/yppasswdd-systemd-exec
# create symlink for rcypserv, rcyppasswdd, rcypxfrd
ln -s /sbin/service %{buildroot}%{_sbindir}/rcypserv
ln -s /sbin/service %{buildroot}%{_sbindir}/rcyppasswdd
ln -s /sbin/service %{buildroot}%{_sbindir}/rcypxfrd
# Remove files which should not be included:
rm %{buildroot}%{_prefix}/lib*/yp/match_printcap

# Systemd services
%pre
%service_add_pre ypserv.service
%service_add_pre yppasswdd.service
%service_add_pre ypxfrd.service

%post
%{fillup_only -n ypserv}
%service_add_post ypserv.service
%service_add_post yppasswdd.service
%service_add_post ypxfrd.service

%preun
%service_del_preun ypserv.service
%service_del_preun yppasswdd.service
%service_del_preun ypxfrd.service

%postun
if [ "$1" = "0" ]; then
   test -L %{_localstatedir}/yp/Makefile && rm -f %{_localstatedir}/yp/Makefile ||:
   test -L %{_localstatedir}/yp/securenets && rm -f %{_localstatedir}/yp/securenets ||:
fi
%service_del_postun ypserv.service
%service_del_postun yppasswdd.service
%service_del_postun ypxfrd.service

%posttrans
# Update "Fix"
if [ -f %{_localstatedir}/yp/Makefile.rpmsave -a ! -e %{_localstatedir}/yp/Makefile ]; then
  mv %{_localstatedir}/yp/Makefile.rpmsave %{_localstatedir}/yp/Makefile
fi
%tmpfiles_create ypserv.conf

%files
%license COPYING
%doc NEWS README
%{_fillupdir}/sysconfig.ypserv
%config(noreplace) %{_sysconfdir}/ypserv.conf
%dir %{_libexecdir}/yp
%{_libexecdir}/yp/yppasswdd-systemd-exec
%{_libexecdir}/yp/securenets.example
%{_libexecdir}/yp/ypMakefile
%{_prefix}/lib/tmpfiles.d/ypserv.conf
%{_unitdir}/ypserv.service
%{_unitdir}/yppasswdd.service
%{_unitdir}/ypxfrd.service
%{_mandir}/man5/netgroup.5%{ext_man}
%{_mandir}/man5/ypserv.conf.5%{ext_man}
%{_mandir}/man8/makedbm.8%{ext_man}
%{_mandir}/man8/mknetid.8%{ext_man}
%{_mandir}/man8/pwupdate.8%{ext_man}
%{_mandir}/man8/revnetgroup.8%{ext_man}
%{_mandir}/man8/rpc.yppasswdd.8%{ext_man}
%{_mandir}/man8/rpc.ypxfrd.8%{ext_man}
%{_mandir}/man8/yphelper.8%{ext_man}
%{_mandir}/man8/ypinit.8%{ext_man}
%{_mandir}/man8/yppasswdd.8%{ext_man}
%{_mandir}/man8/yppush.8%{ext_man}
%{_mandir}/man8/ypserv.8%{ext_man}
%{_mandir}/man8/ypxfr.8%{ext_man}
%{_mandir}/man8/ypxfrd.8%{ext_man}
%{_includedir}/rpcsvc/ypxfrd.x
%{_libexecdir}/yp/makedbm
%{_libexecdir}/yp/create_printcap
%{_libexecdir}/yp/mknetid
%{_libexecdir}/yp/pwupdate
%{_libexecdir}/yp/revnetgroup
%{_libexecdir}/yp/yphelper
%{_libexecdir}/yp/ypinit
%{_libexecdir}/yp/ypxfr
%{_libexecdir}/yp/ypxfr_*
%{_sbindir}/rpc.ypxfrd
%{_sbindir}/rpc.yppasswdd
%{_sbindir}/yppush
%{_sbindir}/ypserv
%{_sbindir}/rcypserv
%{_sbindir}/rcyppasswdd
%{_sbindir}/rcypxfrd

%changelog
