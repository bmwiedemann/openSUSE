#
# spec file for package cyrus-imapd
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


# support for the berkeley database
%bcond_without bdb
# support for HTTP (CalDAV/CardDAV/etc)
%bcond_without http
# support for Simple Network Management Protocol
%bcond_without snmp
# unit tests
%bcond_without tests

%global cyrus_user      cyrus
%global cyrus_group     mail
%global _servicename    cyrus-imapd
%define _sover 0
Name:           cyrus-imapd
Version:        3.8.4
Release:        0
Summary:        The Cyrus IMAP and POP Mail Server
License:        BSD-3-Clause
Group:          Productivity/Networking/Email/Servers
URL:            http://www.cyrusimap.org
# Upstream sources
Source0:        https://github.com/cyrusimap/cyrus-imapd/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source90:       https://github.com/cyrusimap/cyrus-imapd/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz.sig
# Vanished source: http://ftp.andrew.cmu.edu/pub/mibs/cmu/cmu.mib
Source1:        cmu.mib
# Distribution specific sources
Source10:       cyrus-imapd-rc-3.tar.gz
Source11:       cyrus-user.conf

# PATCH-FIX-OPENSUSE -- Use the right syslog facility in docs
Patch7:         cyrus-imapd-3.8.2_syslog-facility-doc.patch

# PATCH-FIX-FEDORA -- Link Perl components against pcre2
# pending upstream discussion
Patch8:         perl-pcre2.patch

BuildRequires:  autoconf >= 2.63
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libical)
BuildRequires:  libtool >= 2.2.6
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  sysuser-tools

# optionals:
BuildRequires:  pkgconfig(libclamav)
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(jansson)
BuildRequires:  krb5-devel
BuildRequires:  openldap2-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  tcpd-devel
# transfig
# valgrind
BuildRequires:  zlib

# for Xapian
#BuildRequires:  rsync
#BuildRequires:  pkgconfig(xapian-core)

%if %{with bdb}
BuildRequires:  db-devel >= 3.0.55
%endif
%if %{with http}
BuildRequires:  pkgconfig(libical) >= 3.0.10
BuildRequires:  pkgconfig(libxml-2.0)
%endif
%if %{with snmp}
BuildRequires:  net-snmp-devel
%endif

%if %{with tests}
BuildRequires:  pkgconfig(cunit)
BuildRequires:  cyrus-sasl-plain
BuildRequires:  cyrus-sasl-digestmd5
%if %{with bdb}
BuildRequires:  db-utils >= 3.0.55
%endif
%endif

%sysusers_requires
Prereq:         system-user-mail
Requires:       perl-Cyrus-Annotator = %{version}
Requires:       perl-Cyrus-IMAP = %{version}
Requires:       perl-Cyrus-SIEVE-managesieve = %{version}
Requires(post): cyrus-sasl
Requires(post): fileutils
Requires(pre):  %fillup_prereq
Recommends:     cyradm
Recommends:     perl-TermReadLine-Gnu
Conflicts:      courier-imap
Conflicts:      dovecot23
Conflicts:      dovecot24
Conflicts:      dump
Conflicts:      imap
Conflicts:      leafnode
Conflicts:      mailutils-delivery
Conflicts:      quota

%description
This package contains the core of the Cyrus IMAP server. It is a mail
system designed for use with standards-based Internet mail
technologies.

A full Cyrus IMAP implementation allows a mail and bulletin
board environment to be set up across multiple servers. It differs from
other IMAP server implementations in that it is run on "sealed"
servers, where users are not normally permitted to log in and have no
system account on the server. The mailbox database is stored in parts
of the filesystem that are private to the Cyrus IMAP server. All user
access to mail is through software using the IMAP, POP3 or KPOP
protocols. It also includes support for virtual domains, NNTP, and
mailbox annotations. Multiple concurrent read/write connections to the
same mailbox are permitted. The server supports access control lists on
mailboxes and storage quotas on mailbox hierarchies.

The Cyrus IMAP server supports the IMAP4rev1 protocol described
in RFC 3501. IMAP4rev1 has been approved as a proposed standard.
It supports any authentication mechanism available from the SASL
library, imaps/pop3s/nntps (IMAP/POP3/NNTP encrypted using SSL and
TLSv1) can be used for security. The server supports single instance
store where possible when an email message is addressed to multiple
recipients. SIEVE provides server side email filtering.

%package devel
Summary:        Libraries and Includes for %{name}
Group:          Development/Libraries/C and C++
Requires:       libcyrus%{?_sover} = %{version}

%description devel
The %{name}-devel package contains header files and libraries
necessary for developing applications which use the imclient library.

%package snmp
Summary:        SNMP support for the Cyrus IMAP and POP Mail Server
Group:          Productivity/Networking/Email/Utilities
Requires:       %{name} = %{version}
Requires:       %{name}-snmp-mibs = %{version}
Requires:       net-snmp >= 5.0

%description snmp
This package contains the core of the Cyrus IMAP server. It is a mail
system designed for use with standards-based Internet mail
technologies.

This package pulls in dependencies to enable SNMP support for %{name}.

%package snmp-mibs
Summary:        MIBs for the Cyrus IMAP and POP Mail Server
Group:          Productivity/Networking/Email/Utilities

%description snmp-mibs
This package contains MIBs for the Cyrus IMAP server. They are required to use %{name} with SNMP.

%package utils
Summary:        Test tools for mail servers
Group:          Productivity/Networking/Email/Utilities
Requires:       cyrus-sasl-plain
Conflicts:      %{name} <= 2.3.18

%description utils
This package contains test tools for mail protocols (not only %{name} specific).

%package -n cyradm
Summary:        Administration tool for the Cyrus IMAP server
Group:          Productivity/Networking/Email/Utilities
Requires:       cyrus-imapd = %{version}
Requires:       libcyrus%{?_sover} = %{version}
Requires:       perl(Cyrus::IMAP::Shell)
Conflicts:      %{name} <= 2.3.18

%description -n cyradm
This package contains an administration tool for the Cyrus IMAP server.

%package -n perl-Cyrus-Annotator
Summary:        Cyrus Annotator Perl Module
Group:          Development/Libraries/Perl
%{perl_requires}

%package -n libcyrus%{?_sover}
Summary:        Cyrus IMAP Shared Libraries
Group:          System/Libraries

%description -n libcyrus%{?_sover}
Shared libraries used by the Cyrus IMAP server.

%description -n perl-Cyrus-Annotator
Cyrus::Annotator::Daemon provides a framework for writing daemons which can
be used to add annotations or flags to messages which are delivered into the
Cyrus mail server.

Cyrus::Annotator::Message encapsulates a message which is being processed by the
annotator daemon.

%package -n perl-Cyrus-IMAP
Summary:        Cyrus IMAP Perl Module
Group:          Development/Libraries/Perl
%{perl_requires}

%description -n perl-Cyrus-IMAP
This package contains a Perl module for the Cyrus IMAP server.

%package -n perl-Cyrus-SIEVE-managesieve
Summary:        Cyrus SIEVE Perl Module
Group:          Development/Libraries/Perl
Recommends:     perl-TermReadLine-Gnu
# provides same binary: /usr/bin/sieveshell
Conflicts:      python-managesieve
%{perl_requires}

%description -n perl-Cyrus-SIEVE-managesieve
This package contains a Perl module for Cyrus SIEVE.

%prep
%autosetup -a 10 -p1

# remove executable permission
find doc -type f -name '*.html' -exec chmod -x {} +
chmod -x perl/annotator/Daemon.pm

# remove cruft
find doc -type f -a -name '.cvsignore' -delete

# set perl script interpreter
sed -i 's|^#!/usr/bin/env perl|#!%__perl|' tools/rehash

# use packaged socket and home directory
sed -i -e s?/run/cyrus?/run/cyrus-imapd? -e s?/var/lib/cyrus?/var/lib/imap? doc/examples/*/*.conf
sed -i -e s?/var/spool/cyrus/mail?/var/spool/imap? -e s?/var/spool/sieve?/var/lib/sieve? doc/examples/imapd_conf/*.conf

%build
#Generate cyrus user
%sysusers_generate_pre %{SOURCE11} cyrus cyrus-user.conf

# configure
autoreconf -iv
export CFLAGS="%{?optflags} -fno-strict-aliasing -fPIC"
#export CFLAGS='-W -Wno-unused-parameter -g -O0 -Wall -Wextra -Werror -fPIC' # for debugging
%configure --localstatedir=%{_var}/lib \
             --enable-autocreate \
             --enable-idled \
             --enable-murder \
             --enable-nntp \
             --enable-replication \
             --enable-gssapi \
             %{?with_http:--enable-http} \
             %{?with_tests:--enable-unit-tests} \
             --with-com_err \
             --with-cyrus-user=%{cyrus_user} \
             --prefix=%{_prefix} \
             --libexecdir=%{_libexecdir}/cyrus \
             --with-gnu-ld \
             --with-gss_impl=auto \
             --with-ldap \
             --with-libwrap \
             --with-lock=fcntl \
             --with-openssl \
             --with-perl=perl \
             --with-sasl \
             %{!?with_bdb:--without-bdb} \
             %{!?with_snmp:--without-snmp} \
             --with-syslogfacility=DAEMON \
             --with-zlib \
             --disable-pcre # force pcre2, Perl modules will wrongly link to legacy pcre and fail at runtime otherwise
#             --enable-xapian \

%make_build


%install
put () {
  sed s?__LIBEXECDIR__?%{_libexecdir}/cyrus? "$1" > "$2"
}

# Cyrus IMAP
%make_install

# make install results in make install within the perl modules subdir, so
# remove the stuff from buildroot to satisfy the picky rpm4, as we don't need
# it and use install_vendor for perl modules below
rm -rf %{buildroot}%{perl_sitelib}
rm -rf %{buildroot}%{perl_sitearch}

# Cyrus ANNOTATOR Perl modules
cd perl/annotator
%perl_make_install
%perl_process_packlist -n perl-Cyrus-Annotator
cd -

# Cyrus IMAP Perl modules
cd perl/imap
%perl_make_install
%perl_process_packlist -n perl-Cyrus-IMAP
cd -

# Cyrus SIEVE managesieve Perl modules
cd perl/sieve/managesieve
%perl_make_install
%perl_process_packlist -n perl-Cyrus-SIEVE-managesieve
cd -

# after make install we can remove stuff we don't want in our packages
rm -rf doc/man/
#rm -f tools/config2*
# http://www.spinics.net/lists/info-cyrus/msg17473.html, See https://lists.andrew.cmu.edu/pipermail/info-cyrus/2016-August/039075.html
rm -f tools/htmlstrip.c

# create /var/* directories
install -d -m 750 %{buildroot}%{_var}/lib/imap/{db,log,msg,proc,quota,socket,user}
install -d -m 700 %{buildroot}%{_var}/lib/imap/ptclient
install -d -m 750 %{buildroot}%{_var}/lib/sieve
install -d -m 750 %{buildroot}%{_var}/spool/imap
install -d -m 750 %{buildroot}%{_var}/adm/backup/imap
for i in a b c d e f g h i j k l m n o p q r s t u v w x y z; do
    install -d -m 755 %{buildroot}%{_var}/lib/imap/user/$i
    install -d -m 755 %{buildroot}%{_var}/lib/imap/quota/$i
    install -d -m 750 %{buildroot}%{_var}/lib/sieve/$i
done

# sysconfig
install -d %{buildroot}%{_fillupdir}
install -m 644 SUSE/sysconfig.cyrus-imapd %{buildroot}%{_fillupdir}/sysconfig.%{_servicename}

# systemd
install -d %{buildroot}{%{_unitdir},%{_sbindir},%{_sysconfdir}/profile.d,%{_tmpfilesdir}}
put SUSE/cyrus-imapd.service %{buildroot}%{_unitdir}/%{_servicename}.service
ln -s service %{buildroot}%{_sbindir}/rc%{_servicename}
ln -s service %{buildroot}%{_sbindir}/rcbackup-cyrus
echo 'alias rccyrus >/dev/null 2>&1 || alias rccyrus=%{_sbindir}/rc%{_servicename}' > %{buildroot}%{_sysconfdir}/profile.d/%{name}.alias.sh

# tmpfiles
install -m 644 SUSE/tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{_servicename}.conf

# tools
install -d %{buildroot}%{_libexecdir}/cyrus/tools
install -m 755 tools/* %{buildroot}%{_libexecdir}/cyrus/tools

# cron
install -m 755 SUSE/cron.daily.cyrus %{buildroot}%{_libexecdir}/cyrus/tools/daily-backup.sh
install -m 644 SUSE/backup-cyrus.timer %{buildroot}%{_unitdir}
put SUSE/backup-cyrus.service %{buildroot}%{_unitdir}/backup-cyrus.service

# pam
install -d %{buildroot}%{_sysconfdir}/pam.d
install -m 644 SUSE/imap %{buildroot}%{_sysconfdir}/pam.d/imap
install -m 644 SUSE/pop %{buildroot}%{_sysconfdir}/pam.d/pop
install -m 644 SUSE/sieve %{buildroot}%{_sysconfdir}/pam.d/sieve

# default config
install -m 644 doc/examples/imapd_conf/normal.conf %{buildroot}%{_sysconfdir}/imapd.conf
install -m 644 SUSE/imapd.annotations.conf %{buildroot}%{_sysconfdir}/imapd.annotations.conf
install -m 644 doc/examples/cyrus_conf/normal.conf %{buildroot}%{_sysconfdir}/cyrus.conf

# DB_CONFIG
install -m 644 SUSE/DB_CONFIG %{buildroot}%{_var}/lib/imap/db

# snmp
%if %{with snmp}
install -d %{buildroot}%{_datadir}/snmp/mibs/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/snmp/mibs/CMU.mib
%endif

# rename manual to avoid conflicts
mv %{buildroot}%{_mandir}/man8/master.8 %{buildroot}%{_mandir}/man8/cyrus_master.8
mv %{buildroot}%{_mandir}/man8/idled.8 %{buildroot}%{_mandir}/man8/cyrus_idled.8
mv %{buildroot}%{_mandir}/man8/fetchnews.8 %{buildroot}%{_mandir}/man8/cyrus_fetchnews.8
%if %{with http}
mv %{buildroot}%{_mandir}/man8/httpd.8 %{buildroot}%{_mandir}/man8/cyrus_httpd.8
%endif

# cyrus user
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE11} %{buildroot}%{_sysusersdir}/

# remove pointless libtool archives
rm %{buildroot}/%{_libdir}/*.la

%check
%if %{with tests}
%{__make} %{?_smp_mflags} check
%endif

%pre -f cyrus.pre
%service_add_pre %{_servicename}.service backup-cyrus.service backup-cyrus.timer

%preun
%service_del_preun %{_servicename}.service backup-cyrus.service backup-cyrus.timer

%post
SIEVEUP=
IMAPUP=
test $1 -gt 1 && test -d usr/sieve -a ! -L usr/sieve && SIEVEUP=yes
test $1 -gt 1 && test -d var/imap  -a ! -L var/imap  && IMAPUP=yes
test -n "`find var/lib/sieve -type f`" && {
     SIEVEUP=
}
test -n "`find var/lib/imap -type f`" && {
     IMAPUP=
}
test -n "$SIEVEUP" && {
     echo "Creating compatibility symlink %{_localstatedir}/lib/sieve -> %{_prefix}/sieve"
     rm -rf var/lib/sieve
     ln -sf ../..%{_prefix}/sieve var/lib/sieve
}
test -n "$IMAPUP" && {
     echo "Creating compatibility symlink %{_localstatedir}/lib/imap -> %{_localstatedir}/imap"
     rm -rf var/lib/imap
     ln -sf  ../imap %{_localstatedir}/lib/imap
}
%{fillup_only %{_servicename}}
%tmpfiles_create %{_tmpfilesdir}/%{_servicename}.conf
%service_add_post %{_servicename}.service backup-cyrus.service backup-cyrus.timer

%postun
%service_del_postun %{_servicename}.service backup-cyrus.service backup-cyrus.timer

%post   -n libcyrus%{?_sover} -p /sbin/ldconfig
%postun -n libcyrus%{?_sover} -p /sbin/ldconfig

%files
%license COPYING
%doc README.md doc/examples master/README
%doc SUSE/README.SUSE
%config %{_sysconfdir}/pam.d/*
%config(noreplace) %{_sysconfdir}/imapd.conf
%config(noreplace) %{_sysconfdir}/imapd.annotations.conf
%config(noreplace) %{_sysconfdir}/cyrus.conf
%dir %attr(0750, %{cyrus_user}, %{cyrus_group}) %{_var}/lib/imap
%attr(0750, %{cyrus_user}, %{cyrus_group}) %{_var}/lib/imap/log
%attr(0750, %{cyrus_user}, %{cyrus_group}) %{_var}/lib/imap/msg
%attr(0750, %{cyrus_user}, %{cyrus_group}) %{_var}/lib/imap/proc
%attr(0700, %{cyrus_user}, %{cyrus_group}) %{_var}/lib/imap/ptclient
%attr(0750, %{cyrus_user}, %{cyrus_group}) %{_var}/lib/imap/quota
%attr(0750, %{cyrus_user}, %{cyrus_group}) %{_var}/lib/imap/socket
%attr(0750, %{cyrus_user}, %{cyrus_group}) %{_var}/lib/imap/user
%dir %attr(0750, %{cyrus_user}, %{cyrus_group}) %{_var}/lib/imap/db
%config(noreplace) %{_var}/lib/imap/db/DB_CONFIG
%attr(0750, %{cyrus_user}, %{cyrus_group}) %{_var}/lib/sieve
%attr(0750, %{cyrus_user}, %{cyrus_group}) %{_var}/spool/imap
%attr(0750, %{cyrus_user}, %{cyrus_group}) %{_var}/adm/backup/imap
%{_fillupdir}/sysconfig.%{_servicename}
%{_unitdir}/*
%{_tmpfilesdir}/%{_servicename}.conf
%ghost %dir %{_rundir}/%{name}
%ghost %dir %{_rundir}/%{name}/lock
%ghost %dir %{_rundir}/%{name}/proc
%ghost %dir %{_rundir}/%{name}/socket
%config %{_sysconfdir}/profile.d/%{name}.alias.sh
%{_sbindir}/rc%{_servicename}
%{_sbindir}/rcbackup-cyrus
%{_libexecdir}/cyrus
%if %{with http}
%{_mandir}/man1/dav_reconstruct.1%{ext_man}
%endif
%{_mandir}/man3/imclient.3%{ext_man}
%{_mandir}/man5/*%{ext_man}
%{_mandir}/man8/*%{ext_man}
%{_sysusersdir}/cyrus-user.conf
%{_sbindir}/arbitron
%{_sbindir}/{chk,ctl,cvt,cyr}_*
%{_sbindir}/cyrdump
%if %{with http}
%{_sbindir}/dav_reconstruct
%endif
%{_sbindir}/deliver
%{_sbindir}/fetchnews
%{_sbindir}/ipurge
%{_sbindir}/mbexamine
%{_sbindir}/mbpath
%{_sbindir}/mbtool
%{_sbindir}/ptdump
%{_sbindir}/ptexpire
%{_sbindir}/quota
%{_sbindir}/reconstruct
%{_sbindir}/relocate_by_id
%{_sbindir}/sievec
%{_sbindir}/sieved
%{_sbindir}/squatter
%{_sbindir}/sync_client
%{_sbindir}/sync_reset
%{_sbindir}/tls_prune
%{_sbindir}/unexpunge

%files devel
%dir %{_includedir}/cyrus
%dir %{_includedir}/cyrus/sieve
%{_includedir}/cyrus/*.h
%{_includedir}/cyrus/sieve/*.h
%{_libdir}/libcyrus*.so
%{_libdir}/pkgconfig/*.pc

%if %{with snmp}
%files snmp
%doc SUSE/README.SNMP
%endif

%if %{with snmp}
%files snmp-mibs
%dir %{_datadir}/snmp
%dir %{_datadir}/snmp/mibs
%{_datadir}/snmp/mibs/CMU.mib
%endif

%files utils
%{_bindir}/httptest
%{_bindir}/imtest
%{_bindir}/lmtptest
%{_bindir}/mupdatetest
%{_bindir}/nntptest
%{_bindir}/pop3test
%{_bindir}/sivtest
%{_bindir}/smtptest
%{_bindir}/synctest
%{_mandir}/man1/httptest.1%{ext_man}
%{_mandir}/man1/imtest.1%{ext_man}
%{_mandir}/man1/lmtptest.1%{ext_man}
%{_mandir}/man1/mupdatetest.1%{ext_man}
%{_mandir}/man1/nntptest.1%{ext_man}
%{_mandir}/man1/pop3test.1%{ext_man}
%{_mandir}/man1/sivtest.1%{ext_man}
%{_mandir}/man1/smtptest.1%{ext_man}
%{_mandir}/man1/synctest.1%{ext_man}

%files -n cyradm
%{_bindir}/cyradm
%{_mandir}/man1/cyradm.1%{ext_man}

%files -n libcyrus%{?_sover}
%{_libdir}/libcyrus*.so.*

%files -n perl-Cyrus-Annotator
%dir %{perl_vendorlib}/Cyrus
%dir %{perl_vendorlib}/Cyrus/Annotator
%{perl_vendorlib}/Cyrus/Annotator/*.pm
%{_mandir}/man3/Cyrus::Annotator*

%files -n perl-Cyrus-IMAP
%dir %{perl_vendorarch}/Cyrus
%{perl_vendorarch}/Cyrus/IMAP
%{perl_vendorarch}/Cyrus/IMAP.pm
%dir %{perl_vendorarch}/auto/Cyrus
%{perl_vendorarch}/auto/Cyrus/IMAP
%{_mandir}/man3/Cyrus::IMAP*

%files -n perl-Cyrus-SIEVE-managesieve
%{_bindir}/installsieve
%{_bindir}/sieveshell
%{_mandir}/man1/installsieve.1%{ext_man}
%{_mandir}/man1/sieveshell.1%{ext_man}
%dir %{perl_vendorarch}/Cyrus
%{perl_vendorarch}/Cyrus/SIEVE
%dir %{perl_vendorarch}/auto/Cyrus
%{perl_vendorarch}/auto/Cyrus/SIEVE
%{_mandir}/man3/Cyrus::SIEVE::managesieve.3pm%{ext_man}

%changelog
