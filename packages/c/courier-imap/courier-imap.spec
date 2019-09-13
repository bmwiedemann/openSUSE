#
# spec file for package courier-imap
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           courier-imap
Summary:        An IMAP and POP3 Server for Maildir MTAs
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Servers
Version:        4.18.2
Release:        0
Url:            http://www.courier-mta.org/imap/
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-%{version}.tar.bz2.sig
Source2:        pop3.pamd
Source3:        imap.pamd
Source11:       courier-imap.init
Source12:       courier-imap-ssl.init
Source13:       courier-pop.init
Source14:       courier-pop-ssl.init
Source15:       courier-imap.service
Source16:       courier-imap-ssl.service
Source17:       courier-imap-gencert.service
Source18:       courier-pop.service
Source19:       courier-pop-ssl.service
Source20:       courier-pop-gencert.service
Patch0:         %{name}-sbindir.patch
Patch2:         %{name}-ulimit_conf.patch
### Patch for upstream:
## fixes typo in Makefile.am
Patch3:         %{name}-Makefile.patch
# PATCH-FIX-UPSTEAM https://github.com/svarshavchik/courier-libs/pull/10
Patch4:         reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 910
BuildRequires:  audit-libs
%endif
BuildRequires:  courier-authlib-devel >= 0.68
BuildRequires:  courier-unicode-devel >= 2.0
BuildRequires:  db-devel
%if 0%{?suse_version} >= 1220
BuildRequires:  gamin-devel
%else
BuildRequires:  fam-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  libstdc++-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  postfix
BuildRequires:  procps
BuildRequires:  zlib-devel
# openssl itself for /usr/bin/openssl configure check
BuildRequires:  openssl
Conflicts:      imap qpopper cyrus-imapd
Requires:       courier-authlib >= 0.68
Requires:       fam-server
Requires:       gdbm
Requires:       openssl

%if 0%{?suse_version} >= 1210
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%define has_systemd 1
%endif

%description
Courier-IMAP is a fast, scalable, enterprise IMAP server that uses
Maildirs. Many E-mail service providers use Courier-IMAP to easy handle
hundreds of thousands of mail accounts. With its built-in IMAP and POP3
aggregation proxy, Courier-IMAP has practically infinite horizontal
scalability. In a proxy configuration, a pool of Courier servers service
initial IMAP and POP3 connections from clients. They wait to receive the
client's log in request, look up the server that actually holds this mail
account's mailbox, and establish a proxy connection to the server, all in
a single, seamless process. Mail accounts can be moved between different
servers, to achieve optimum resource usage.

The only practical limitation on Courier-IMAP is available network and I/O
bandwidth. If you are new to Courier-IMAP, this may sound a bit
intimidating. But you do not need to tackle everything at once. Start by
taking small, easy steps. Your first step will be to set up a small
Courier-IMAP server, using it like any other traditional IMAP service, on
a single server. After you gain experience and become comfortable with
Courier, you can then begin exploring its advanced features.

This is the same IMAP server that's included in the Courier mail server,
but configured as a standalone IMAP server that can be used with other
mail servers - such as Qmail, Exim, or Postfix - that deliver to maildirs.
If you already have Courier installed, you do not need to download this
version. If you install this version, you must remove it if you later
install the entire Courier server.


%prep
%setup -n %{name}-%{version}
%patch0
%patch2
%patch3
%patch4 -p1

%build
%configure \
	--libexecdir=%{_prefix}/lib/%{name} \
	--datadir=%{_datadir}/%{name} \
	--sysconfdir=%{_sysconfdir}/courier \
	--sharedstatedir=%{_sharedstatedir}/%{name} \
%if 0%{?has_systemd}
	--with-piddir=/run \
%else
	--with-piddir=%{_localstatedir}/run \
%endif
	--disable-static \
	--disable-root-check \
	--enable-unicode \
%if 0%{?has_systemd}
	--with-authdaemonvar=/run/courier-authlib \
%else
	--with-authdaemonvar=%{_localstatedir}/run/courier-authlib \
%endif
	--with-certdb=%{_sysconfdir}/ssl/certs \
	--with-certsdir=%{_sysconfdir}/ssl/private \
	--enable-workarounds-for-imap-client-bugs
%{__make} %{_smp_mflags}

%install
%{__make} install DESTDIR=%{buildroot}
# Move daemons into sbin
%{__mv} %{buildroot}%{_prefix}/bin/{couriertls,imapd,pop3d} %{buildroot}%{_prefix}/sbin/
# Rename imapd.8 to courier-imapd.8
%{__mv}  %{buildroot}%{_mandir}/man8/imapd.8 %{buildroot}%{_mandir}/man8/%{name}d.8
# Install PAM config files
%{__install} -D -m 644 $RPM_SOURCE_DIR/pop3.pamd %{buildroot}/etc/pam.d/pop3
%{__install} -D -m 644 $RPM_SOURCE_DIR/imap.pamd %{buildroot}/etc/pam.d/imap
# Install init scripts
%if 0%{?has_systemd}
for i in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  %{__ln_s} -f service %{buildroot}%{_prefix}/sbin/rccourier-$i
done
%else
for i in imap imap-ssl pop pop-ssl ; do
  %{__install} -D -m 0755 $RPM_SOURCE_DIR/courier-$i.init %{buildroot}/etc/init.d/courier-$i
  %{__ln_s} -f /etc/init.d/courier-$i %{buildroot}%{_prefix}/sbin/rccourier-$i
done
%endif
# Install service files
%if 0%{?has_systemd}
for j in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  %{__install} -D -m 0644 $RPM_SOURCE_DIR/courier-$j.service %{buildroot}/%{_unitdir}/courier-$j.service
done
%endif
# Remove original init scripts, will not work longer
%{__rm} %{buildroot}%{_prefix}/lib/%{name}/imapd.rc
%{__rm} %{buildroot}%{_prefix}/lib/%{name}/imapd-ssl.rc
%{__rm} %{buildroot}%{_prefix}/lib/%{name}/pop3d.rc
%{__rm} %{buildroot}%{_prefix}/lib/%{name}/pop3d-ssl.rc
#
# Fix imapd.dist
#
%{__sed} -i -e 's/^IMAPDSTART=.*/IMAPDSTART=YES/' %{buildroot}%{_sysconfdir}/courier/imapd.dist
%{__sed} -i -e 's/^ADDRESS=.*/ADDRESS=127.0.0.1/' %{buildroot}%{_sysconfdir}/courier/imapd.dist
%{__sed} -i -e 's/^MAXPERIP=.*/MAXPERIP=20/' %{buildroot}%{_sysconfdir}/courier/imapd.dist
%{__sed} -i -e 's/^IMAPDSSLSTART=.*/IMAPDSSLSTART=YES/' %{buildroot}%{_sysconfdir}/courier/imapd-ssl.dist
#%{__sed} -i -e 's/^#\ \+\(TLS_CIPHER_LIST=.*\)/\1/' %{buildroot}%{_sysconfdir}/courier/imapd-ssl.dist
%{__sed} -i -e 's/^POP3DSTART=.*/POP3DSTART=YES/' %{buildroot}%{_sysconfdir}/courier/pop3d.dist
%{__sed} -i -e 's/^POP3DSSLSTART=.*/POP3DSSLSTART=YES/' %{buildroot}%{_sysconfdir}/courier/pop3d-ssl.dist
#%{__sed} -i -e 's/^#\ \+\(TLS_CIPHER_LIST=.*\)/\1/' %{buildroot}%{_sysconfdir}/courier/pop3d-ssl.dist
# For %doc macro
%{__install} -m 0644 libs/imap/ChangeLog ChangeLog
%{__install} -m 0644 libs/imap/README README.imap
%{__install} -m 0644 libs/imap/README.proxy README.proxy
%{__install} -m 0644 libs/maildir/README.maildirquota.txt README.maildirquota
%{__install} -m 0644 libs/maildir/README.sharedfolders.txt README.sharedfolders
%{__install} -D -m 0755 sysconftool %{buildroot}%{_datadir}/%{name}/sysconftool
%{__chmod} 755 %{buildroot}%{_datadir}/%{name}/sysconftool
%{__cat} >%{buildroot}%{_datadir}/%{name}/configlist <<EOF
%{_sysconfdir}/courier/imapd.dist
%{_sysconfdir}/courier/imapd-ssl.dist
%{_sysconfdir}/courier/pop3d.dist
%{_sysconfdir}/courier/pop3d-ssl.dist
EOF

%pre
%if 0%{?has_systemd}
for i in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  %service_add_pre courier-$i.service
done
%endif

%preun
%if 0%{?has_systemd}
for i in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  %service_del_preun courier-$i.service
done
%else
%if 0%{?suse_version}
for i in imap imap-ssl pop pop-ssl; do
  %stop_on_removal courier-$i
done
%endif
%endif
if [ "$1" = "0" ]; then
  %{__rm} -f %{_localstatedir}/couriersslcache
  %{__rm} -f %{_localstatedir}/imapd.pid
  %{__rm} -f %{_localstatedir}/imapd-ssl.pid
  %{__rm} -f %{_localstatedir}/imapd.pid.lock
  %{__rm} -f %{_localstatedir}/imapd-ssl.pid.lock
  %{__rm} -f %{_localstatedir}/pop3d.pid
  %{__rm} -f %{_localstatedir}/pop3d-ssl.pid
  %{__rm} -f %{_localstatedir}/pop3d.pid.lock
  %{__rm} -f %{_localstatedir}/pop3d-ssl.pid.lock
fi

%post
%{_datadir}/%{name}/sysconftool `%{__cat} %{_datadir}/%{name}/configlist` >/dev/null
%if 0%{?has_systemd}
for i in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  %service_add_post courier-$i.service
done
%endif

%postun
%if 0%{?has_systemd}
for i in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  %service_del_postun courier-$i.service
done
%else
for i in imap imap-ssl pop pop-ssl; do
  %restart_on_update courier-$i
done
%insserv_cleanup
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,755)
%doc AUTHORS libs/imap/ChangeLog COPYING* libs/imap/BUGS README README.imap README.maildirquota README.proxy
%doc README.sharedfolders
%if !0%{?has_systemd}
%attr(755,root,root) /etc/init.d/courier-*
%endif
%config %attr(644,root,root) /etc/pam.d/imap
%config %attr(644,root,root) /etc/pam.d/pop3
%dir %{_sysconfdir}/courier
%dir %{_sysconfdir}/courier/imapaccess
%dir %{_sysconfdir}/courier/shared
%dir %{_sysconfdir}/courier/shared.tmp
%config %attr(600,root,root) %{_sysconfdir}/courier/imapd*
%config %attr(600,root,root) %{_sysconfdir}/courier/pop3*
%config %{_sysconfdir}/courier/quotawarnmsg.example
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/makedatprog
%{_prefix}/lib/%{name}/couriertcpd
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man?/*
%if 0%{?has_systemd}
%{_unitdir}/courier-*.service
%endif

%changelog
