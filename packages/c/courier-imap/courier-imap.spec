#
# spec file for package courier-imap
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_with     valgrind

Name:           courier-imap
Version:        5.2.0
Release:        0
Summary:        An IMAP and POP3 Server for Maildir MTAs
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Servers
URL:            https://www.courier-mta.org/imap/
Source0:        https://downloads.sourceforge.net/courier/%{name}-%{version}.tar.bz2
Source1:        https://downloads.sourceforge.net/courier/%{name}-%{version}.tar.bz2.sig
Source2:        pop3.pamd
Source3:        imap.pamd
# Keyring downloaded from https://www.courier-mta.org/KEYS.bin#/%%{name}.keyring
Source4:        %{name}.keyring
Source15:       courier-imap.service
Source16:       courier-imap-ssl.service
Source17:       courier-imap-gencert.service
Source18:       courier-pop.service
Source19:       courier-pop-ssl.service
Source20:       courier-pop-gencert.service
Patch0:         %{name}-sbindir.patch
Patch2:         %{name}-ulimit_conf.patch
### Patch for upstream:
# Apply (open)SUSE specific changes to configuration
Patch4:         %{name}-config.patch
BuildRequires:  audit-libs
BuildRequires:  courier-authlib-devel >= 0.71
BuildRequires:  courier-unicode-devel >= 2.1
BuildRequires:  db-devel
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  libstdc++-devel
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  procps
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd)
%if %{with valgrind}
BuildRequires:  valgrind
%endif
Requires:       courier-authlib >= 0.71
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
%autosetup -p0

# For %%doc macro
mv libs/maildir/README.sharedfolders{.txt,}
mv libs/maildir/README.maildirquota{.txt,}

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
%if %{without valgrind}
	--enable-workarounds-for-imap-client-bugs
%endif

%make_build

%install
%make_install
# Move daemons into sbin
mv %{buildroot}%{_bindir}/{couriertls,imapd,pop3d} %{buildroot}%{_sbindir}/
# Rename imapd.8 to courier-imapd.8
mv  %{buildroot}%{_mandir}/man8/imapd.8 %{buildroot}%{_mandir}/man8/%{name}d.8
# Install PAM config files
install -D -m 644 %{S:2} %{buildroot}%{_sysconfdir}/pam.d/pop3
install -D -m 644 %{S:3} %{buildroot}%{_sysconfdir}/pam.d/imap
# Install init scripts
for i in imap imap-ssl imap-gencert pop pop-ssl pop-gencert; do
  ln -s -f service %{buildroot}%{_sbindir}/rccourier-$i
done
# Install service files
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 %{S:15} %{S:16} %{S:17} %{S:18} %{S:19} %{S:20} %{buildroot}%{_unitdir}
# Remove original init scripts, will not work longer
rm %{buildroot}%{_prefix}/lib/%{name}/imapd.rc
rm %{buildroot}%{_prefix}/lib/%{name}/imapd-ssl.rc
rm %{buildroot}%{_prefix}/lib/%{name}/pop3d.rc
rm %{buildroot}%{_prefix}/lib/%{name}/pop3d-ssl.rc
#
install -D -m 0755 sysconftool %{buildroot}%{_datadir}/%{name}/sysconftool
chmod 755 %{buildroot}%{_datadir}/%{name}/sysconftool
cat >%{buildroot}%{_datadir}/%{name}/configlist <<EOF
%{_sysconfdir}/courier/imapd.dist
%{_sysconfdir}/courier/imapd-ssl.dist
%{_sysconfdir}/courier/pop3d.dist
%{_sysconfdir}/courier/pop3d-ssl.dist
EOF
# SSL state cache directory
install -d %{buildroot}%{_localstatedir}/cache/%{name}/

%if %{with valgrind}
%check
make check
%endif

%pre
%service_add_pre courier-imap-gencert.service courier-imap-ssl.service courier-imap.service
%service_add_pre courier-pop-gencert.service courier-pop-ssl.service courier-pop.service

%preun
%service_del_preun courier-imap-gencert.service courier-imap-ssl.service courier-imap.service
%service_del_preun courier-pop-gencert.service courier-pop-ssl.service courier-pop.service

%post
%{_datadir}/%{name}/sysconftool `cat %{_datadir}/%{name}/configlist` >/dev/null
%service_add_post courier-imap-gencert.service courier-imap-ssl.service courier-imap.service
%service_add_post courier-pop-gencert.service courier-pop-ssl.service courier-pop.service

%postun
%service_del_postun courier-imap-gencert.service courier-imap-ssl.service courier-imap.service
%service_del_postun courier-pop-gencert.service courier-pop-ssl.service courier-pop.service

%files
%defattr(-,root,root,755)
%license COPYING*
%doc AUTHORS README
%doc libs/imap/ChangeLog libs/imap/BUGS libs/imap/README.proxy
%doc libs/maildir/README.sharedfolders libs/maildir/README.maildirquota
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
%dir %attr(750,root,root) %{_localstatedir}/cache/%{name}/
%ghost %{_localstatedir}/cache/%{name}/sslpop3cache
%ghost %{_localstatedir}/cache/%{name}/sslimapcache

%changelog
