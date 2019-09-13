#
# spec file for package cyrus-imapd
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%global cyrus_user      cyrus
%global cyrus_group     mail
%global cyrus_uid       96

#
# sysvinit -- build for SysVinit and not for systemd
#
%if %{defined systemd_requires}
%global         with_systemd 1
%endif
%bcond_with     systemd

%if %{with systemd}
%global _servicename    cyrus-imapd
%else
%global _servicename    cyrus
%endif
Name:           cyrus-imapd
Version:        2.4.20
Release:        0
Summary:        The Cyrus IMAP and POP Mail Server
License:        BSD-3-Clause
Group:          Productivity/Networking/Email/Servers
Url:            http://www.cyrusimap.org
# Upstream sources
Source0:        http://cyrusimap.org/releases/%{name}-%{version}.tar.gz
Source90:       http://cyrusimap.org/releases/%{name}-%{version}.tar.gz.sig
Source1:        http://ftp.andrew.cmu.edu/pub/mibs/cmu/cmu.mib
# Distribution specific sources
Source10:       cyrus-imapd-rc-2.tar.gz
# PATCH-FEATURE-UPSTREAM -- Autocreate INBOX folders // included in 2.5
Patch1:         cyrus-imapd-2.4.19_autocreate-0.10-0.patch
# PATCH-FEATURE-UPSTREAM -- Add support to define a catchall mailbox
Patch4:         cyrus-imapd-2.4.17_lmtp_catchall_mailbox.patch
# PATCH-FIX-OPENSUSE -- Use the right syslog facility in docs
Patch7:         cyrus-imapd-2.3.16_syslog-facility-doc.patch
# PATCH-FEATURE-UPSTREAM -- Add support for OpenSLP
Patch10:        cyrus-imapd-2.4.17_openslp.patch
# PATCH-FIX-UPSTREAM -- Fix compiling with -fPIE
Patch12:        cyrus-imapd-2.4.17_pie.patch
# PATCH-FIX-UPSTREAM -- Support db-6.0
Patch25:        cyrus-imapd-2.4.17_db6.patch
# PATCH-FEATURE-UPSTREAM -- Allow a result attribute to be specified with ptclient/ldap.c // included in 2.5
Patch27:        cyrus-imapd-2.4.17_ptloader-ldap_user_attribute.patch
# PATCH-FIX-UPSTREAM -- Have the correct #include when using implicit definitions
Patch28:        cyrus-imapd-2.4.19-implicit_definitions.patch
# PATCH-FIX-UPSTREAM -- Outlook 2013-compatible XLIST behaviour
Patch31:        cyrus-imapd-2.4.18-D19-Outlook_2013_XLIST.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
BuildRequires:  ed
BuildRequires:  flex
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  net-snmp-devel
BuildRequires:  openldap2-devel
BuildRequires:  openslp-devel
BuildRequires:  openssl-devel
BuildRequires:  opie
BuildRequires:  perl-Digest-SHA1
BuildRequires:  pwdutils
BuildRequires:  tcpd-devel
BuildRequires:  zlib
Requires:       perl-Cyrus-IMAP = %{version}
Requires:       perl-Cyrus-SIEVE-managesieve = %{version}
Requires(post): cyrus-sasl
Requires(post): fileutils
Requires(pre):  pwdutils
Recommends:     cyradm
Recommends:     perl-TermReadLine-Gnu
Conflicts:      courier-imap
Conflicts:      cyrus-imapd-kolab
Conflicts:      imap
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with systemd}
BuildRequires:  systemd
Requires(pre):  %fillup_prereq
%systemd_requires
%else
Recommends:     cron
Requires(pre):  %insserv_prereq
%endif

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
Conflicts:      cyrus-imapd <= 2.3.18

%description utils
This package contains test tools for mail protocols (not only %{name} specific).

%package -n perl-Cyrus-IMAP
Summary:        Cyrus IMAP Perl Module
Group:          Development/Libraries/Perl
Conflicts:      perl-Cyrus-IMAP-kolab
%if 0%{?suse_version} < 1140
Requires:       perl = %{perl_version}
%else
%{perl_requires}
%endif

%description -n perl-Cyrus-IMAP
This package contains a Perl module for the Cyrus IMAP server.

%package -n cyradm
Summary:        Administration tool for the Cyrus IMAP server
Group:          Productivity/Networking/Email/Utilities
Requires:       perl(Cyrus::IMAP::Shell)
Conflicts:      cyrus-imapd <= 2.3.18

%description -n cyradm
This package contains an administration tool for the Cyrus IMAP server.

%package -n perl-Cyrus-SIEVE-managesieve
Summary:        Cyrus SIEVE Perl Module
Group:          Development/Libraries/Perl
Recommends:     perl-TermReadLine-Gnu
Conflicts:      perl-Cyrus-SIEVE-managesieve-kolab
Conflicts:      python-managesieve
%if 0%{?suse_version} < 1140
Requires:       perl = %{perl_version}
%else
%{perl_requires}
%endif

%description -n perl-Cyrus-SIEVE-managesieve
This package contains a Perl module for Cyrus SIEVE.

%package devel
Summary:        Libraries and Includes for %{name}
Group:          Development/Libraries/C and C++
Conflicts:      cyrus-imapd-kolab-devel

%description devel
The %{name}-devel package contains header files and libraries
necessary for developing applications which use the imclient library.

%prep
%setup -q -a 10
%patch1 -p1
%patch4 -p1
%patch7 -p1
%patch10 -p1
%patch12 -p1
%patch25 -p1
%patch27 -p1
%patch28 -p1
%patch31 -p1

# remove executable bit from docs
find doc -type f -name '*.html' -exec chmod -x {} +

# remove cruft
find doc -type f -a -name '.cvsignore' -delete

%build
rm -fr aclocal.m4 configure config.h.in autom4te.cache
# this is basically autoreconf
sh SMakefile

export CFLAGS="%{?optflags} -fno-strict-aliasing"
%configure --localstatedir=%{_var}/lib \
             --enable-idled \
             --enable-murder \
             --enable-netscapehack \
             --enable-nntp \
             --enable-replication \
             --enable-gssapi \
             --with-bdb \
             --with-com_err \
             --with-cyrus-user=%{cyrus_user} \
             --with-cyrus-group=%{cyrus_group} \
             --with-cyrus-prefix=%{_prefix}/lib/cyrus \
             --with-gss_impl=auto \
             --with-ldap \
             --with-libwrap \
             --with-lock=fcntl \
             --with-openslp \
             --with-openssl \
             --with-perl=perl \
             --with-sasl \
             --with-snmp \
             --with-syslogfacility=DAEMON \
             --with-zlib

make depend %{?_smp_mflags}

# unpredictable parallel build; fails if sieve_err.h isn't ready in time
#make %%{?_smp_mflags}
make -j1

%install
# Cyrus IMAP
make %{?_smp_mflags} DESTDIR=%{buildroot} install

# make install results in make install within the perl modules subdir, so
# remove the stuff from buildroot to satisfy the picky rpm4, as we don't need
# it and use install_vendor for perl modules below
rm -rf %{buildroot}%{perl_sitelib}
rm -rf %{buildroot}%{perl_sitearch}

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
rm -f doc/Makefile.dist*
rm -rf doc/man
rm -f doc/text/htmlstrip.c
rm -f doc/text/Makefile
rm -f tools/config2*

# remove Perl bootstrap files
find %{buildroot}%{perl_vendorarch}/ -name '*.bs' -type f -delete

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

%if %{with systemd}
# systemd
install -d %{buildroot}{%{_unitdir},%{_sbindir},%{_sysconfdir}/profile.d}
install -m 644 SUSE/cyrus-imapd.service %{buildroot}%{_unitdir}/%{_servicename}.service
ln -s service %{buildroot}%{_sbindir}/rc%{_servicename}
echo 'alias rccyrus >/dev/null 2>&1 || alias rccyrus=%{_sbindir}/rc%{_servicename}' > %{buildroot}%{_sysconfdir}/profile.d/%{name}.alias.sh
%else
# sysvinit
install -d %{buildroot}{%{_sysconfdir}/init.d,%{_sbindir}}
install -m 755 SUSE/rc.cyrus %{buildroot}%{_initddir}/%{_servicename}
ln -s %{_initddir}/%{_servicename} %{buildroot}%{_sbindir}/rc%{_servicename}
%endif

# tools
install -d %{buildroot}%{_prefix}/lib/cyrus/tools
install -m 755 tools/* %{buildroot}%{_prefix}/lib/cyrus/tools/

%if %{with systemd}
install -m 755 SUSE/cron.daily.cyrus %{buildroot}%{_prefix}/lib/cyrus/tools/daily-backup.sh
install -m 644 SUSE/backup-cyrus.*   %{buildroot}%{_unitdir}
%else
# cron
install -d %{buildroot}%{_sysconfdir}/cron.daily
install -m 755 SUSE/cron.daily.cyrus %{buildroot}%{_sysconfdir}/cron.daily/suse.de-%{name}
%endif
# pam
install -d %{buildroot}%{_sysconfdir}/pam.d
install -m 644 SUSE/imap %{buildroot}%{_sysconfdir}/pam.d/imap
install -m 644 SUSE/pop %{buildroot}%{_sysconfdir}/pam.d/pop
install -m 644 SUSE/sieve %{buildroot}%{_sysconfdir}/pam.d/sieve

# default config
install -m 644 SUSE/imapd.conf %{buildroot}%{_sysconfdir}/imapd.conf
install -m 644 SUSE/imapd.annotations.conf %{buildroot}%{_sysconfdir}/imapd.annotations.conf
install -m 644 SUSE/cyrus.conf %{buildroot}%{_sysconfdir}/cyrus.conf

# DB_CONFIG
install -m 644 SUSE/DB_CONFIG %{buildroot}%{_var}/lib/imap/db

# snmp
install -d %{buildroot}%{_datadir}/snmp/mibs/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/snmp/mibs/CMU.mib
install -m 644 master/CYRUS-MASTER.mib %{buildroot}%{_datadir}/snmp/mibs/CYRUS-MASTER.mib

# rename manual to avoid conflicts
mv %{buildroot}%{_mandir}/man8/master.8 %{buildroot}%{_mandir}/man8/cyrus_master.8
mv %{buildroot}%{_mandir}/man8/idled.8 %{buildroot}%{_mandir}/man8/cyrus_idled.8
mv %{buildroot}%{_mandir}/man8/fetchnews.8 %{buildroot}%{_mandir}/man8/cyrus_fetchnews.8

%pre
getent group %{cyrus_group} >/dev/null || groupadd -r %{cyrus_group}
getent passwd %{cyrus_user} >/dev/null || useradd -r -o -g %{cyrus_group} -u %{cyrus_uid} -d %{_localstatedir}/lib/imap -s /sbin/nologin -c "user for %{name}" %{cyrus_user}
usermod -d %{_localstatedir}/lib/imap %{cyrus_user} || :
%if %{with systemd}
%service_add_pre %{_servicename}.service backup-cyrus.service backup-cyrus.timer
%endif

%preun
%if %{with systemd}
%service_del_preun %{_servicename}.service backup-cyrus.service backup-cyrus.timer
%else
%stop_on_removal %{_servicename}
%endif

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
%if %{with systemd}
%{fillup_only %{_servicename}}
%service_add_post %{_servicename}.service backup-cyrus.service backup-cyrus.timer
%else
%{fillup_and_insserv %{_servicename}}
%endif

%postun
%if %{with systemd}
%service_del_postun %{_servicename}.service backup-cyrus.service backup-cyrus.timer
%else
%restart_on_update %{_servicename}
%insserv_cleanup
%endif

%files
%defattr(-, root, root)
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
%config %{_fillupdir}/sysconfig.%{_servicename}
%if %{with systemd}
%{_unitdir}/*
%config %{_sysconfdir}/profile.d/%{name}.alias.sh
%else
%config %{_sysconfdir}/cron.daily/suse.de-%{name}
%{_initddir}/%{_servicename}
%endif
%{_sbindir}/rc%{_servicename}
%{_prefix}/lib/cyrus
%{_mandir}/man3/imclient.3%{ext_man}
%{_mandir}/man5/*%{ext_man}
%{_mandir}/man8/*%{ext_man}
%doc COPYRIGHT README README.andrew doc master/conf
%doc SUSE/README.SUSE

%files snmp
%defattr(-, root, root)
%doc SUSE/README.SNMP

%files snmp-mibs
%defattr(-, root, root)
%dir %{_datadir}/snmp
%dir %{_datadir}/snmp/mibs
%{_datadir}/snmp/mibs/CMU.mib
%{_datadir}/snmp/mibs/CYRUS-MASTER.mib

%files utils
%defattr(-, root, root)
%{_bindir}/imtest
%{_bindir}/lmtptest
%{_bindir}/mupdatetest
%{_bindir}/nntptest
%{_bindir}/pop3test
%{_bindir}/sivtest
%{_bindir}/smtptest
%{_bindir}/synctest
%{_mandir}/man1/imtest.1%{ext_man}
%{_mandir}/man1/lmtptest.1%{ext_man}
%{_mandir}/man1/mupdatetest.1%{ext_man}
%{_mandir}/man1/nntptest.1%{ext_man}
%{_mandir}/man1/pop3test.1%{ext_man}
%{_mandir}/man1/sivtest.1%{ext_man}
%{_mandir}/man1/smtptest.1%{ext_man}

%files -n cyradm
%defattr(-, root, root)
%{_bindir}/cyradm
%{_mandir}/man1/cyradm.1%{ext_man}

%files -n perl-Cyrus-IMAP
%defattr(-, root, root)
%dir %{perl_vendorarch}/Cyrus
%{perl_vendorarch}/Cyrus/IMAP
%{perl_vendorarch}/Cyrus/IMAP.pm
%dir %{perl_vendorarch}/auto/Cyrus
%{perl_vendorarch}/auto/Cyrus/IMAP
%if 0%{?suse_version} < 1140
%{_var}/adm/perl-modules/perl-Cyrus-IMAP
%endif
%{_mandir}/man3/Cyrus::IMAP*

%files -n perl-Cyrus-SIEVE-managesieve
%defattr(-, root, root)
%{_bindir}/installsieve
%{_bindir}/sieveshell
%{_mandir}/man1/installsieve.1%{ext_man}
%{_mandir}/man1/sieveshell.1%{ext_man}
%dir %{perl_vendorarch}/Cyrus
%{perl_vendorarch}/Cyrus/SIEVE
%dir %{perl_vendorarch}/auto/Cyrus
%{perl_vendorarch}/auto/Cyrus/SIEVE
%if 0%{?suse_version} < 1140
%{_var}/adm/perl-modules/perl-Cyrus-SIEVE-managesieve
%endif
%{_mandir}/man3/Cyrus::SIEVE::managesieve.3pm%{ext_man}

%files devel
%defattr(-, root, root)
%dir %{_includedir}/cyrus
%{_includedir}/cyrus/*.h
%{_libdir}/libcyrus.a
%{_libdir}/libcyrus_min.a

%changelog
