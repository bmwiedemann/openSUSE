#
# spec file for package exim
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%bcond_without  mysql
%bcond_without  pgsql
%bcond_without  sqlite
%bcond_without  ldap
%bcond_without  i18n
%if 0%{?suse_version} > 1199 || 0%{?centos_version} > 599 || 0%{?rhel_version} > 599
%bcond_without  dane
%else
%bcond_with     dane
%endif
Name:           exim
Version:        4.98
Release:        0
Summary:        The Exim Mail Transfer Agent, a Replacement for sendmail
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Servers
URL:            https://www.exim.org/
Source:         https://ftp.exim.org/pub/exim/exim4/exim-%{version}.tar.bz2
Source1:        sysconfig.exim
Source2:        exim.logrotate
Source3:        https://ftp.exim.org/pub/exim/exim4/exim-%{version}.tar.bz2.asc
# http://ftp.exim.org/pub/exim/Exim-Maintainers-Keyring.asc
Source4:        exim.keyring
Source11:       exim.rc
Source12:       permissions.exim
Source13:       apparmor.usr.sbin.exim
Source30:       eximstats-html-update.py
Source31:       eximstats.conf
Source32:       eximstats.conf-2.2
Source40:       exim.service
Source41:       exim_db.8.gz
Patch0:         exim-tail.patch
Patch1:         gnu_printf.patch
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
BuildRequires:  libidn-devel
BuildRequires:  libspf2-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
Conflicts:      postfix
Conflicts:      sendmail
Conflicts:      sendmail-tls
Provides:       smtp_daemon
%if 0%{?suse_version} >= 1330 && 0%{?suse_version} < 1599
BuildRequires:  libnsl-devel
%endif
%if %{with_ldap}
BuildRequires:  openldap2-devel
%endif
%if %{?suse_version:%suse_version}%{?!suse_version:0} > 800
BuildRequires:  perl-File-FcntlLock
Requires:       logrotate
Requires:       perl-File-FcntlLock
Requires(pre):  %fillup_prereq
Requires(pre):  fileutils
Requires(pre):  permissions
Requires(pre):  textutils
%if 0%{?suse_version} > 1220
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%else
Requires(pre):  %insserv_prereq
%endif
%if 0%{?suse_version} >= 1330
BuildRequires:  group(mail)
BuildRequires:  user(mail)
Requires(pre):  group(mail)
Requires(pre):  user(mail)
%endif
%endif
%if %{with_mysql}
BuildRequires:  mysql-devel
%endif
%if %{with_pgsql}
BuildRequires:  postgresql-devel
%endif
%if %{with_sqlite}
BuildRequires:  sqlite3-devel
%endif

%package -n eximon
Summary:        Eximon, an graphical frontend to administer Exim's mail queue
Group:          Productivity/Networking/Email/Servers

%package -n eximstats-html
Summary:        Create HTML reports of exim logs
Group:          Productivity/Networking/Email/Servers
Requires:       perl-GD
Requires:       perl-GDGraph
Requires:       perl-GDTextUtil

%description
Exim is a mail transport agent (MTA) developed at the University of
Cambridge for use on Unix systems connected to the Internet. It is
freely available under the terms of the GNU General Public Licence. In
style, it is similar to Smail 3, but its facilities are more extensive.
In particular, it has options for verifying incoming sender and
recipient addresses, for refusing mail from specified hosts, networks,
or senders, and for controlling mail relaying.

%description -n eximon
This allows administrators to view the exim agent's mail queue and
logs, and perform a variety of actions on queued messages, such as
freezing, bouncing and thawing messages, and even editing body and
header of mails.

%description -n eximstats-html
If this package is installed alongside the exim MTA, and you enable
EXIM_REPORT_WEEKLY_HTML in %{_sysconfdir}/sysconfig/exim, logrotate/cron will
create HTML reports in /srv/www/eximstats.

You can edit %{_sysconfdir}/apache2/conf.d/eximstats.conf to configure your
webserver for the reports.

The script %{_sbindir}/eximstats-html-update.py can create the reports
for log files that were rotated in the past. (You would only run this
once, if at all. The rest is done by logrotate / cron.)

%prep
%setup -q -n exim-%{version}
%patch -P 0
%patch -P 1 -p1
# build with fPIE/pie on SUSE 10.0 or newer, or on any other platform
%if %{?suse_version:%suse_version}%{?!suse_version:99999} > 930
fPIE="-fPIE"
pie="-pie"
%endif
%if 0%{?suse_version} > 1100 || 0%{?centos_version} > 599 || 0%{?rhel_version} > 599
CFLAGS_OPT_WERROR="-Werror=format-security -Werror=missing-format-attribute"
%endif
cat <<-EOF > Local/Makefile
	# see src/EDITME for comments.
	BIN_DIRECTORY=%{_sbindir}
	CONFIGURE_FILE=%{_sysconfdir}/exim/exim.conf
	EXIM_USER=ref:mail
	EXIM_GROUP=ref:mail
	SPOOL_DIRECTORY=%{_localstatedir}/spool/exim
	ROUTER_ACCEPT=yes
	ROUTER_DNSLOOKUP=yes
	ROUTER_IPLITERAL=yes
	ROUTER_MANUALROUTE=yes
	ROUTER_QUERYPROGRAM=yes
	ROUTER_REDIRECT=yes
	# ROUTER_IPLOOKUP=yes
	TRANSPORT_APPENDFILE=yes
	TRANSPORT_AUTOREPLY=yes
	TRANSPORT_PIPE=yes
	TRANSPORT_SMTP=yes
	TRANSPORT_LMTP=yes
	SUPPORT_MAILDIR=yes
	SUPPORT_MAILSTORE=yes
	SUPPORT_MBX=yes
	LOOKUP_DBM=yes
	LOOKUP_LSEARCH=yes
	LOOKUP_CDB=yes
	LOOKUP_DNSDB=yes
	LOOKUP_DSEARCH=yes
%if %{with_ldap}
	LOOKUP_LDAP=yes
%endif
%if %{with_mysql}
	LOOKUP_MYSQL=yes
%endif
%if %{with_pgsql}
	LOOKUP_PGSQL=yes
%endif
%if %{with_sqlite}
	LOOKUP_SQLITE=yes
%endif
%if 0%{?suse_version} < 1599
	LOOKUP_NIS=yes
        LOOKUP_LIBS=-lnsl
%else
        # LOOKUP_NIS=yes
%endif
	# LOOKUP_NISPLUS=yes
	LOOKUP_PASSWD=yes
	# LOOKUP_WHOSON=yes
	CYRUS_SASLAUTHD_SOCKET=%{_localstatedir}/run/sasl2/mux
%if %{with_ldap}
	LDAP_LIB_TYPE=OPENLDAP2
	LOOKUP_LIBS+=-llber -lldap
%endif
%if %{with_mysql}
	LOOKUP_INCLUDE+=-I %{_includedir}/mysql
	LOOKUP_LIBS+=-L %{_libdir}/mysql -lmysqlclient
%endif
%if %{with_pgsql}
	LOOKUP_INCLUDE+=-I %{_includedir}/pgsql
	LOOKUP_LIBS+=-lpq
%endif
%if %{with_sqlite}
	LOOKUP_INCLUDE+=-I %{_includedir}/sqlite3
	LOOKUP_LIBS+=-lsqlite3
%endif
	EXIM_MONITOR=eximon.bin
	WITH_CONTENT_SCAN=yes
	#WITH_OLD_DEMIME=yes
	AUTH_CRAM_MD5=yes
    AUTH_CYRUS_SASL=yes
	AUTH_PLAINTEXT=yes
	AUTH_SPA=yes
	AUTH_DOVECOT=yes
    AUTH_TLS=yes
	AUTH_LIBS=-lsasl2
    USE_OPENSSL=yes
	TLS_LIBS=-lssl -lcrypto
	INFO_DIRECTORY=%{_infodir}
	LOG_FILE_PATH=%{_localstatedir}/log/exim/%%s.log
	EXICYCLOG_MAX=10
	SYSLOG_LOG_PID=yes
    SYSLOG_LONG_LINES=yes
	COMPRESS_COMMAND=/bin/gzip
	COMPRESS_SUFFIX=gz
	ZCAT_COMMAND=%{_bindir}/zcat
	SUPPORT_PAM=yes
	# You probably need to add -lpam to EXTRALIBS
	# RADIUS_CONFIG_FILE=%{_sysconfdir}/radiusclient/radiusclient.conf
	# CYRUS_PWCHECK_SOCKET=%{_localstatedir}/pwcheck/pwcheck
	# USE_TCP_WRAPPERS=yes
	NO_SYMLINK=yes
	CHOWN_COMMAND=/bin/chown
	CHGRP_COMMAND=/bin/chgrp
	MV_COMMAND=/bin/mv
	RM_COMMAND=/bin/rm
	PERL_COMMAND=%{_bindir}/perl
	# APPENDFILE_MODE=0600
	# APPENDFILE_DIRECTORY_MODE=0700
	# APPENDFILE_LOCKFILE_MODE=0600
	# CONFIGURE_FILE_USE_NODE=yes
	# CONFIGURE_FILE_USE_EUID=yes
	# DELIVER_BUFFER_SIZE=8192
	# EXIMDB_DIRECTORY_MODE=0750
	# EXIMDB_MODE=0640
	# EXIMDB_LOCKFILE_MODE=0640
	# HEADER_MAXSIZE="(1024*1024)"
	# INPUT_DIRECTORY_MODE=0750
	# LOG_DIRECTORY_MODE=0750
	# LOG_MODE=0640
	# LOOKUP_TESTDB=yes
	MAKE_SHELL=/bin/bash
	MAX_NAMED_LIST=64
	# MAXINTERFACES=250
	# MSGLOG_DIRECTORY_MODE=0750
	# PERL_CC=
	# PERL_CCOPTS=
	# PERL_LIBS=
	PID_FILE_PATH=%{_localstatedir}/run/exim.pid
	# SPOOL_DIRECTORY_MODE=0750
	# SPOOL_MODE=0640
	SUPPORT_MOVE_FROZEN_MESSAGES=yes
	HAVE_IPV6=YES
    SUPPORT_SPF=yes
	LOOKUP_LIBS+=-lspf2
    #SUPPORT_DMARC=yes
	#CFLAGS += -I/usr/local/include
	#LDFLAGS += -lopendmarc
	EXPERIMENTAL_EVENT=yes
	EXPERIMENTAL_PROXY=yes
	EXPERIMENTAL_CERTNAMES=yes
	EXPERIMENTAL_DSN=yes
	SYSTEM_ALIASES_FILE=%{_sysconfdir}/aliases
    # enable SRS
    SUPPORT_SRS=yes
%if %{with dane}
    SUPPORT_DANE=yes
%endif
	EXPERIMENTAL_SOCKS=yes
%if %{with i18n}
	EXPERIMENTAL_INTERNATIONAL=yes
%endif
	LDFLAGS += -lidn
	CFLAGS=%{optflags} -std=gnu99 -Wall $CFLAGS_OPT_WERROR -fno-strict-aliasing -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -DLDAP_DEPRECATED $fPIE
	EXTRALIBS=-ldl -lpam -L/usr/X11R6/%{_lib} $pie
EOF
touch Local/eximon.conf
rm -f doc/*.{orig,txt~}

%build
%make_build

%install
%if 0%{?suse_version} > 1220
mkdir -p %{buildroot}/%{_unitdir}
%else
mkdir -p %{buildroot}%{_initddir}
%endif
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
%else
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
%endif
mkdir -p %{buildroot}%{_prefix}/{bin,sbin,lib}
mkdir -p %{buildroot}%{_localstatedir}/log/exim
mkdir -p %{buildroot}%{_localstatedir}/spool/mail/
ln -s spool/mail %{buildroot}%{_localstatedir}
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_bindir}
make 	inst_dest=%{buildroot}%{_sbindir} \
	inst_conf=%{buildroot}%{_sysconfdir}/exim/exim.conf \
	inst_info=%{buildroot}/%{_infodir} \
	INSTALL_ARG=-no_chown 	install
#mv $RPM_BUILD_ROOT/usr/sbin/exim-%{version}* $RPM_BUILD_ROOT/usr/sbin/exim
mv %{buildroot}%{_sbindir}/exim-4.9* %{buildroot}%{_sbindir}/exim
mv %{buildroot}%{_sysconfdir}/exim/exim.conf src/configure.default # with all substitutions done
%if 0%{?suse_version} > 1220
install -m 0644 %{SOURCE40} %{buildroot}/%{_unitdir}/exim.service
%else
install -m 0755 %{SOURCE11} %{buildroot}%{_initddir}/exim
%endif
# aka...
for i in \
	%{_prefix}/lib/sendmail \
	%{_bindir}/runq \
	%{_bindir}/rsmtp \
	%{_bindir}/mailq \
	%{_bindir}/newaliases
do
	ln -sf ../sbin/exim $RPM_BUILD_ROOT$i
done
ln -sf exim %{buildroot}%{_sbindir}/sendmail
%if 0%{?suse_version} > 1220
ln -sv service %{buildroot}%{_sbindir}/rcexim
%else
ln -sv ../..%{_initddir}/exim %{buildroot}%{_sbindir}/rcexim
%endif
mv %{buildroot}%{_sbindir}/eximon* %{buildroot}%{_bindir}/
cp -p %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.exim
%if 0%{?suse_version} > 1500
install -m 0644 %{SOURCE2} %{buildroot}%{_distconfdir}/logrotate.d/exim
%else
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/exim
%endif
# man pages
mv doc/exim.8 %{buildroot}/%{_mandir}/man8/
cp $RPM_SOURCE_DIR/exim_db.8.gz %{buildroot}/%{_mandir}/man8
gunzip %{buildroot}/%{_mandir}/man8/exim_db.8.gz
pod2man --center=EXIM --section=8 %{buildroot}%{_sbindir}/eximstats > %{buildroot}/%{_mandir}/man8/eximstats.8
for i in \
	sendmail \
	runq \
	rsmtp \
	mailq \
	newaliases
do
	ln -sf exim.8.gz %{buildroot}/%{_mandir}/man8/$i.8.gz
done
for i in \
	exim_dumpdb \
	exim_fixdb \
	exim_tidydb
do
	ln -sf exim_db.8.gz %{buildroot}/%{_mandir}/man8/$i.8.gz
done
sed -i -e 's,%{_datadir}/doc/exim4,%{_docdir}/exim,g' $(find %{buildroot}/%{_mandir}/man8 -name "*.8")
gzip -9 doc/*.txt
#
# package the utilities without executable permissions, to silence rpmlint warnings
chmod 644 util/*.{pl,sh} src/convert4r*
#
# eximstats-html files
mkdir -p %{buildroot}/srv/www/eximstats
mkdir -p %{buildroot}%{_sysconfdir}/apache2/conf.d/
%if 0%{?suse_version} == 0 || 0%{?suse_version} > 1310
	cp -p %{SOURCE31} %{buildroot}%{_sysconfdir}/apache2/conf.d/
%else
	cp -p %{SOURCE32} %{buildroot}%{_sysconfdir}/apache2/conf.d/eximstats.conf
%endif
install -m 0755 $RPM_SOURCE_DIR/eximstats-html-update.py %{buildroot}/%{_sbindir}
# apparmor profile
install -D -m 0644 $RPM_SOURCE_DIR/apparmor.usr.sbin.exim %{buildroot}%{_datadir}/apparmor/extra-profiles/usr.sbin.exim

%pretrans -p <lua>
docdir = rpm.expand('%{_docdir}')
pkgname = rpm.expand('%{name}')
path = docdir .. '/' .. pkgname .. '/doc/cve-2019-13917'
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

%pre
%if 0%{?suse_version} > 1220
%service_add_pre exim.service
%endif
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/exim ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/exim ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%if 0%{?suse_version} < 1131
%run_permissions
%else
%set_permissions %{_sbindir}/exim
%endif
if ! test -s etc/exim/exim.conf; then
	if test -s etc/exim.conf; then
		mv etc/exim.conf etc/exim/
		echo moving exim.conf to %{_sysconfdir}/exim/
	else
		cp -p usr/share/doc/packages/%{name}/configure.default etc/exim/exim.conf
		echo copying default config file to %{_sysconfdir}/exim/exim.conf
	fi
fi
%if 0%{?suse_version} > 1220
%fillup_only
%service_add_post exim.service
%else
%{fillup_and_insserv exim}
%endif
exit 0
%if %{?suse_version:1}%{?!suse_version:0}
%preun
%if 0%{?suse_version} > 1220
%service_del_preun exim.service
%else
%stop_on_removal exim
%endif
%endif

%postun
%if %{?suse_version:1}%{?!suse_version:0}
%if 0%{?suse_version} > 1220
%service_del_postun exim.service
%else
%restart_on_update exim
%insserv_cleanup
%endif
%endif

%verifyscript
%verify_permissions -e %{_sbindir}/exim

%files
%ghost %{_docdir}/%{name}/doc/cve-2019-13917.rpmmoved
%license LICENCE
%doc ACKNOWLEDGMENTS CHANGES NOTICE README.UPDATING README
%doc doc
%doc src/configure.default
%doc build-Linux-*/convert4r{3,4}
%doc util
%{_mandir}/man8/*
%{_sbindir}/exicyclog
%{_sbindir}/exigrep
%{_sbindir}/exiqgrep
%verify(not mode) %attr(4755,root,root) %{_sbindir}/exim
%{_sbindir}/exim_*
%{_sbindir}/eximstats
%{_sbindir}/exinext
%{_sbindir}/exipick
%{_sbindir}/exiqsumm
%{_sbindir}/exiwhat
%dir %{_sysconfdir}/exim
%if 0%{?suse_version} > 1220
%{_unitdir}/exim.service
%else
%config %{_initddir}/exim
%endif
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/exim
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/exim
%endif
%if %{?suse_version:%suse_version}%{?!suse_version:99999} < 1000
%config(noreplace) %{_sysconfdir}/permissions.d/exim
%endif
%dir %{_datadir}/apparmor
%dir %{_datadir}/apparmor/extra-profiles
%config(noreplace) %{_datadir}/apparmor/extra-profiles/usr.sbin.exim
%{_sbindir}/rcexim
%{_bindir}/mailq
%{_bindir}/runq
%{_bindir}/rsmtp
%{_bindir}/newaliases
%{_sbindir}/sendmail
%{_prefix}/lib/sendmail
%{_fillupdir}/sysconfig.exim
%dir %attr(750,mail,mail) %{_localstatedir}/log/exim
%dir %attr(1777,root,root) %{_localstatedir}/spool/mail
%{_localstatedir}/mail

%files -n eximon
%{_bindir}/eximon
%{_bindir}/eximon.bin

%files -n eximstats-html
%dir /srv/www
%attr(0750,root,www) /srv/www/eximstats
%dir %{_sysconfdir}/apache2
%dir %{_sysconfdir}/apache2/conf.d
%config %{_sysconfdir}/apache2/conf.d/eximstats.conf
%{_sbindir}/eximstats-html-update.py

%changelog
