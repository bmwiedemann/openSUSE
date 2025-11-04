#
# spec file for package OpenSMTPD
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 SUSE Software Solutions
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


Name:           OpenSMTPD
%global         name_lowercase %(echo -n "%{name}" | tr '[:upper:]' '[:lower:]')
Version:        7.8.0p0
Release:        0
Summary:        A free implementation of the server-side SMTP protocol
License:        BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND ISC
URL:            https://www.opensmtpd.org/
Group:          Productivity/Networking/Email/Servers
Source:         https://www.opensmtpd.org/archives/opensmtpd-%{version}.tar.gz
Source1:        %{name}-user.conf
Source2:        %{name}.service
# PATCH-FIX-OPENSUSE OpenSMTPD-reduced-permissions-on-SMTPD_SOCKET.patch boo#1247781
Patch1:         OpenSMTPD-reduced-permissions-on-SMTPD_SOCKET.patch
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
%sysusers_requires
Requires(pre):  permissions
Requires:       filesystem
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  libtool
BuildRequires:  netcfg
BuildRequires:  sed
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libopenssl)
BuildRequires:  pkgconfig(zlib)
Provides:       smtp_daemon
Conflicts:      busybox-sendmail
Conflicts:      exim
Conflicts:      msmtp-mta
Conflicts:      postfix
Conflicts:      postfix-bdb
Conflicts:      sendmail
%define         dir_mail /var/spool/mail

%description
OpenSMTPD is a FREE implementation of the server-side SMTP protocol as defined by RFC 5321, with some additional standard extensions.

It allows ordinary machines to exchange e-mails with other systems speaking the SMTP protocol.

%prep
%setup -q -n %{name_lowercase}-%{version}
./bootstrap
%patch -P 1 -p1

%build
%sysusers_generate_pre %{SOURCE1} %{name} %{name}-user.conf
sed -i "s;@rundir@;%{_rundir};g" %{SOURCE2}
%configure --with-path-empty=%{_sharedstatedir}/empty --with-path-pidfile=%{_rundir} --with-path-mbox=%{dir_mail}
%make_build
sed -i "s;^listen on localhost;listen on 127.0.0.1\\nlisten on ::1;g" usr.sbin/smtpd/smtpd.conf

%install
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}-user.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_sysconfdir}/mail
ln -s %{_sysconfdir}/aliases %{buildroot}%{_sysconfdir}/mail/aliases
mkdir -m 711 -p %{buildroot}%{_localstatedir}/spool/smtpd
mkdir -m 755 -p %{buildroot}%{dir_mail}
%make_install
# We rename the following man page to resolve a conflict with an existing Factory package (vacation)
mv %{buildroot}%{_mandir}/man5/forward.5 %{buildroot}%{_mandir}/man5/forward.5%{name_lowercase}

%check
make check

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%set_permissions %{_libexecdir}/%{name_lowercase}/lockspool
%set_permissions %{_sbindir}/smtpctl

%verifyscript
%verify_permissions -e %{_libexecdir}/%{name_lowercase}/lockspool
%verify_permissions -e %{_sbindir}/smtpctl

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%{_sysusersdir}/%{name}-user.conf
%config(noreplace) %{_sysconfdir}/smtpd.conf
%dir %{_sysconfdir}/mail
%config(noreplace) %{_sysconfdir}/mail/aliases
%{_unitdir}/%{name}.service
%{_bindir}/smtp
%dir %{_libexecdir}/%{name_lowercase}
%{_libexecdir}/%{name_lowercase}/encrypt
%attr(4755,-,-) %{_libexecdir}/%{name_lowercase}/lockspool
%{_libexecdir}/%{name_lowercase}/mail.lmtp
%{_libexecdir}/%{name_lowercase}/mail.local
%{_libexecdir}/%{name_lowercase}/mail.maildir
%{_libexecdir}/%{name_lowercase}/mail.mboxfile
%{_libexecdir}/%{name_lowercase}/mail.mda
%attr(2755,-,_smtpq) %{_sbindir}/smtpctl
%{_sbindir}/smtpd
%dir %{_localstatedir}/spool/smtpd
# We leave it to the administrator to create a group for users that need to
# have access to dir_mail and adjust ownership and privileges accordingly.
%dir %{dir_mail}
%{_mandir}/man1/lockspool.1%{?ext_man}
%{_mandir}/man1/smtp.1%{?ext_man}
%{_mandir}/man5/aliases.5%{?ext_man}
%{_mandir}/man5/forward.5%{name_lowercase}%{?ext_man}
%{_mandir}/man5/smtpd.conf.5%{?ext_man}
%{_mandir}/man5/table.5%{?ext_man}
%{_mandir}/man7/smtpd-filters.7%{?ext_man}
%{_mandir}/man7/smtpd-tables.7%{?ext_man}
%{_mandir}/man8/mail.lmtp.8%{?ext_man}
%{_mandir}/man8/mail.local.8%{?ext_man}
%{_mandir}/man8/mail.maildir.8%{?ext_man}
%{_mandir}/man8/mail.mboxfile.8%{?ext_man}
%{_mandir}/man8/mail.mda.8%{?ext_man}
%{_mandir}/man8/makemap.8%{?ext_man}
%{_mandir}/man8/newaliases.8%{?ext_man}
%{_mandir}/man8/sendmail.8%{?ext_man}
%{_mandir}/man8/smtpctl.8%{?ext_man}
%{_mandir}/man8/smtpd.8%{?ext_man}
%license LICENSE

%changelog
