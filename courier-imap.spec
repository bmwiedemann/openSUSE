#
# spec file for package courier-imap
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


Name:           courier-imap
Version:        5.0.11
Release:        0
Summary:        An IMAP and POP3 Server for Maildir MTAs
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Servers
URL:            https://www.courier-mta.org/imap/
Source0:        https://downloads.sourceforge.net/project/courier/imap/%{version}/%{name}-%{version}.tar.bz2
Source1:        https://downloads.sourceforge.net/project/courier/imap/%{version}/%{name}-%{version}.tar.bz2.sig
Source2:        pop3.pamd
Source3:        imap.pamd
# Keyring downloaded from https://www.courier-mta.org/KEYS.bin#/%{name}.keyring
Source4:        %{name}.keyring
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
BuildRequires:  audit-libs
BuildRequires:  courier-authlib-devel >= 0.71
BuildRequires:  courier-unicode-devel >= 2.1
BuildRequires:  db-devel
BuildRequires:  gamin-devel
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  libidn-devel
BuildRequires:  libstdc++-devel
BuildRequires:  ncurses-devel
# openssl itself for /usr/bin/openssl configure check
BuildRequires:  postfix
BuildRequires:  procps
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd)
Requires:       courier-authlib >= 0.71
Requires:       fam-server
Requires:       gdbm
Requires:       openssl
Conflicts:      cyrus-imapd
Conflicts:      imap
Conflicts:      qpopper
%{?systemd_requires}

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
%setup -q
%patch0
%patch2
%patch3

%build
%configure \
	--with-notice=unicode \
	--libexecdir=%{_prefix}/lib/%{name} \
	--datadir=%{_datadir}/%{name} \
	--sysconfdir=%{_sysconfdir}/courier \
	--sharedstatedir=%{_sharedstatedir}/%{name} \
	--with-piddir=%{_rundir} \
	--disable-static \
	--disable-root-check \
	--enable-unicode \
	--with-notice=unicode \
	--with-authdaemonvar=%{_rundir}/courier-authlib \
	--with-certdb=%{_sysconfdir}/ssl/certs \
	--with-certsdir=%{_sysconfdir}/ssl/private \
	--enable-workarounds-for-imap-client-bugs
make %{?_smp_mflags}

%install
%make_install
# Move daemons into sbin
mv %{buildroot}%{_bindir}/{couriertls,imapd,pop3d} %{buildroot}%{_sbindir}/
# Rename imapd.8 to courier-imapd.8
mv  %{buildroot}%{_mandir}/man8/imapd.8 %{buildroot}%{_mandir}/man8/%{name}d.8
# Install PAM config files
install -D -m 644 $RPM_SOURCE_DIR/pop3.pamd %{buildroot}%{_sysconfdir}/pam.d/pop3
install -D -m 644 $RPM_SOURCE_DIR/imap.pamd %{buildroot}%{_sysconfdir}/pam.d/imap
# Install init scripts
for i in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  ln -s -f service %{buildroot}%{_sbindir}/rccourier-$i
done
# Install service files
for j in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  install -D -m 0644 $RPM_SOURCE_DIR/courier-$j.service %{buildroot}/%{_unitdir}/courier-$j.service
done
# Remove original init scripts, will not work longer
rm %{buildroot}%{_prefix}/lib/%{name}/imapd.rc
rm %{buildroot}%{_prefix}/lib/%{name}/imapd-ssl.rc
rm %{buildroot}%{_prefix}/lib/%{name}/pop3d.rc
rm %{buildroot}%{_prefix}/lib/%{name}/pop3d-ssl.rc
#
# Fix imapd.dist
#
sed -i -e 's/^IMAPDSTART=.*/IMAPDSTART=YES/' %{buildroot}%{_sysconfdir}/courier/imapd.dist
sed -i -e 's/^ADDRESS=.*/ADDRESS=127.0.0.1/' %{buildroot}%{_sysconfdir}/courier/imapd.dist
sed -i -e 's/^MAXPERIP=.*/MAXPERIP=20/' %{buildroot}%{_sysconfdir}/courier/imapd.dist
sed -i -e 's/^IMAPDSSLSTART=.*/IMAPDSSLSTART=YES/' %{buildroot}%{_sysconfdir}/courier/imapd-ssl.dist
#sed -i -e 's/^#\ \+\(TLS_CIPHER_LIST=.*\)/\1/' %{buildroot}%{_sysconfdir}/courier/imapd-ssl.dist
sed -i -e 's/^POP3DSTART=.*/POP3DSTART=YES/' %{buildroot}%{_sysconfdir}/courier/pop3d.dist
sed -i -e 's/^POP3DSSLSTART=.*/POP3DSSLSTART=YES/' %{buildroot}%{_sysconfdir}/courier/pop3d-ssl.dist
#sed -i -e 's/^#\ \+\(TLS_CIPHER_LIST=.*\)/\1/' %{buildroot}%{_sysconfdir}/courier/pop3d-ssl.dist
# For %doc macro
install -m 0644 libs/imap/ChangeLog ChangeLog
install -m 0644 libs/imap/README README.imap
install -m 0644 libs/imap/README.proxy README.proxy
install -m 0644 libs/maildir/README.maildirquota.txt README.maildirquota
install -m 0644 libs/maildir/README.sharedfolders.txt README.sharedfolders
install -D -m 0755 sysconftool %{buildroot}%{_datadir}/%{name}/sysconftool
chmod 755 %{buildroot}%{_datadir}/%{name}/sysconftool
cat >%{buildroot}%{_datadir}/%{name}/configlist <<EOF
%{_sysconfdir}/courier/imapd.dist
%{_sysconfdir}/courier/imapd-ssl.dist
%{_sysconfdir}/courier/pop3d.dist
%{_sysconfdir}/courier/pop3d-ssl.dist
EOF

%pre
for i in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  %service_add_pre courier-$i.service
done

%preun
for i in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  %service_del_preun courier-$i.service
done
if [ "$1" = "0" ]; then
  rm -f %{_localstatedir}/couriersslcache
  rm -f %{_localstatedir}/imapd.pid
  rm -f %{_localstatedir}/imapd-ssl.pid
  rm -f %{_localstatedir}/imapd.pid.lock
  rm -f %{_localstatedir}/imapd-ssl.pid.lock
  rm -f %{_localstatedir}/pop3d.pid
  rm -f %{_localstatedir}/pop3d-ssl.pid
  rm -f %{_localstatedir}/pop3d.pid.lock
  rm -f %{_localstatedir}/pop3d-ssl.pid.lock
fi

%post
%{_datadir}/%{name}/sysconftool `cat %{_datadir}/%{name}/configlist` >/dev/null
for i in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  %service_add_post courier-$i.service
done

%postun
for i in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  %service_del_postun courier-$i.service
done

%files
%defattr(-,root,root,755)
%license COPYING*
%doc AUTHORS libs/imap/ChangeLog libs/imap/BUGS README README.imap README.maildirquota README.proxy
%doc README.sharedfolders
%config %attr(644,root,root) %{_sysconfdir}/pam.d/imap
%config %attr(644,root,root) %{_sysconfdir}/pam.d/pop3
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
%{_unitdir}/courier-*.service

%changelog
