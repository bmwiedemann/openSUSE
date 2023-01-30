#
# spec file for package exim
#
# Copyright (c) 2023 SUSE LLC
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
  %define _fillupdir /var/adm/fillup-templates
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
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
BuildRequires:  libidn-devel
%if 0%{?suse_version} >= 1330 && 0%{?suse_version} < 1599
BuildRequires:  libnsl-devel
%endif
BuildRequires:  libspf2-devel
BuildRequires:  pam-devel
%if %{with_ldap}
BuildRequires:  openldap2-devel
%endif
BuildRequires:  pcre2-devel
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
URL:            http://www.exim.org/
Conflicts:      postfix
Conflicts:      sendmail
Conflicts:      sendmail-tls
Provides:       smtp_daemon
%if %{?suse_version:%suse_version}%{?!suse_version:0} > 800
Requires:       logrotate
%if 0%{?suse_version} > 1220
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%else
Requires(pre):  %insserv_prereq
%endif
Requires(pre):  %fillup_prereq permissions
%if 0%{?suse_version} >= 1330
BuildRequires:  group(mail)
BuildRequires:  user(mail)
Requires(pre):  user(mail)
Requires(pre):  group(mail)
%endif
Requires(pre):  fileutils textutils
%endif
Version:        4.96
Release:        0
%if %{with_mysql}
BuildRequires:  mysql-devel
%endif
%if %{with_pgsql}
BuildRequires:  postgresql-devel
%endif
%if %{with_sqlite}
BuildRequires:  sqlite3-devel
%endif
Summary:        The Exim Mail Transfer Agent, a Replacement for sendmail
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Servers
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         http://ftp.exim.org/pub/exim/exim4/exim-%{version}.tar.bz2
Source3:        http://ftp.exim.org/pub/exim/exim4/exim-%{version}.tar.bz2.asc
# http://ftp.exim.org/pub/exim/Exim-Maintainers-Keyring.asc
Source4:        exim.keyring
Source1:        sysconfig.exim
Source2:        exim.logrotate
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
Patch2:         patch-no-exit-on-rewrite-malformed-address.patch
Patch3:         patch-cve-2022-3559

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
EXIM_REPORT_WEEKLY_HTML in /etc/sysconfig/exim, logrotate/cron will
create HTML reports in /srv/www/eximstats.

You can edit /etc/apache2/conf.d/eximstats.conf to configure your
webserver for the reports.

The script /usr/sbin/eximstats-html-update.py can create the reports
for log files that were rotated in the past. (You would only run this
once, if at all. The rest is done by logrotate / cron.)

%prep
%setup -q -n exim-%{version}
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
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
	BIN_DIRECTORY=/usr/sbin
	CONFIGURE_FILE=/etc/exim/exim.conf
	EXIM_USER=ref:mail
	EXIM_GROUP=ref:mail
	SPOOL_DIRECTORY=/var/spool/exim
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
	CYRUS_SASLAUTHD_SOCKET=/var/run/sasl2/mux
%if %{with_ldap}
	LDAP_LIB_TYPE=OPENLDAP2
	LOOKUP_LIBS+=-llber -lldap
%endif
%if %{with_mysql}
	LOOKUP_INCLUDE+=-I /usr/include/mysql
	LOOKUP_LIBS+=-L %{_libdir}/mysql -lmysqlclient
%endif
%if %{with_pgsql}
	LOOKUP_INCLUDE+=-I /usr/include/pgsql
	LOOKUP_LIBS+=-lpq
%endif
%if %{with_sqlite}
	LOOKUP_INCLUDE+=-I /usr/include/sqlite3
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
	LOG_FILE_PATH=/var/log/exim/%%s.log
	EXICYCLOG_MAX=10
	SYSLOG_LOG_PID=yes
    SYSLOG_LONG_LINES=yes
	COMPRESS_COMMAND=/bin/gzip
	COMPRESS_SUFFIX=gz
	ZCAT_COMMAND=/usr/bin/zcat
	SUPPORT_PAM=yes
	# You probably need to add -lpam to EXTRALIBS
	# RADIUS_CONFIG_FILE=/etc/radiusclient/radiusclient.conf
	# CYRUS_PWCHECK_SOCKET=/var/pwcheck/pwcheck
	# USE_TCP_WRAPPERS=yes
	NO_SYMLINK=yes
	CHOWN_COMMAND=/bin/chown
	CHGRP_COMMAND=/bin/chgrp
	MV_COMMAND=/bin/mv
	RM_COMMAND=/bin/rm
	PERL_COMMAND=/usr/bin/perl
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
	PID_FILE_PATH=/var/run/exim.pid
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
	SYSTEM_ALIASES_FILE=/etc/aliases
%if %{with dane}
    SUPPORT_DANE=yes
%endif
	EXPERIMENTAL_SOCKS=yes
%if %{with i18n}
	EXPERIMENTAL_INTERNATIONAL=yes
%endif
	LDFLAGS += -lidn
	CFLAGS=$RPM_OPT_FLAGS -std=gnu99 -Wall $CFLAGS_OPT_WERROR -fno-strict-aliasing -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -DLDAP_DEPRECATED $fPIE
	EXTRALIBS=-ldl -lpam -L/usr/X11R6/%{_lib} $pie
EOF
touch Local/eximon.conf
rm -f doc/*.{orig,txt~}

%build
make

%install
%if 0%{?suse_version} > 1220
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
%else
mkdir -p $RPM_BUILD_ROOT/etc/init.d
%endif
%if 0%{?suse_version} > 1500
mkdir -p $RPM_BUILD_ROOT%{_distconfdir}/logrotate.d
%else
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
%endif
mkdir -p $RPM_BUILD_ROOT/usr/{bin,sbin,lib}
mkdir -p $RPM_BUILD_ROOT/var/log/exim
mkdir -p $RPM_BUILD_ROOT/var/spool/mail/
ln -s spool/mail $RPM_BUILD_ROOT/var
mkdir -p $RPM_BUILD_ROOT%{_fillupdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT/usr/bin
make 	inst_dest=$RPM_BUILD_ROOT/usr/sbin \
	inst_conf=$RPM_BUILD_ROOT/etc/exim/exim.conf \
	inst_info=$RPM_BUILD_ROOT/%{_infodir} \
	INSTALL_ARG=-no_chown 	install
#mv $RPM_BUILD_ROOT/usr/sbin/exim-%{version}* $RPM_BUILD_ROOT/usr/sbin/exim
mv $RPM_BUILD_ROOT/usr/sbin/exim-4.9* $RPM_BUILD_ROOT/usr/sbin/exim
mv $RPM_BUILD_ROOT/etc/exim/exim.conf src/configure.default # with all substitutions done
%if 0%{?suse_version} > 1220
install -m 0644 %{S:40} $RPM_BUILD_ROOT/%{_unitdir}/exim.service
%else
install -m 0755 %{S:11} $RPM_BUILD_ROOT/etc/init.d/exim
%endif
# aka...
for i in \
	/usr/lib/sendmail \
	/usr/bin/runq \
	/usr/bin/rsmtp \
	/usr/bin/mailq \
	/usr/bin/newaliases
do
	ln -sf ../sbin/exim $RPM_BUILD_ROOT$i
done
ln -sf exim $RPM_BUILD_ROOT/usr/sbin/sendmail
%if 0%{?suse_version} > 1220
ln -sv service $RPM_BUILD_ROOT/usr/sbin/rcexim
%else
ln -sv ../../etc/init.d/exim $RPM_BUILD_ROOT/usr/sbin/rcexim
%endif
mv $RPM_BUILD_ROOT/usr/sbin/eximon* $RPM_BUILD_ROOT/usr/bin/
cp -p %{S:1} $RPM_BUILD_ROOT%{_fillupdir}/sysconfig.exim
%if 0%{?suse_version} > 1500
install -m 0644 %{S:2} $RPM_BUILD_ROOT%{_distconfdir}/logrotate.d/exim
%else
install -m 0644 %{S:2} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/exim
%endif
# man pages
mv doc/exim.8 $RPM_BUILD_ROOT/%{_mandir}/man8/
cp $RPM_SOURCE_DIR/exim_db.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8
gunzip $RPM_BUILD_ROOT/%{_mandir}/man8/exim_db.8.gz
pod2man --center=EXIM --section=8 $RPM_BUILD_ROOT/usr/sbin/eximstats > $RPM_BUILD_ROOT/%{_mandir}/man8/eximstats.8
for i in \
	sendmail \
	runq \
	rsmtp \
	mailq \
	newaliases
do
	ln -sf exim.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8/$i.8.gz
done
for i in \
	exim_dumpdb \
	exim_fixdb \
	exim_tidydb
do
	ln -sf exim_db.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8/$i.8.gz
done
perl -pi -e 's%/usr/share/doc/exim4%/usr/share/doc/packages/exim%g' `find $RPM_BUILD_ROOT/%{_mandir}/man8 -name "*.8"`
gzip -9 doc/*.txt
#
# package the utilities without executable permissions, to silence rpmlint warnings
chmod 644 util/*.{pl,sh} src/convert4r*
#
# eximstats-html files
mkdir -p $RPM_BUILD_ROOT/srv/www/eximstats
mkdir -p $RPM_BUILD_ROOT/etc/apache2/conf.d/
%if 0%{?suse_version} == 0 || 0%{?suse_version} > 1310
	cp -p %{S:31} $RPM_BUILD_ROOT/etc/apache2/conf.d/
%else
	cp -p %{S:32} $RPM_BUILD_ROOT/etc/apache2/conf.d/eximstats.conf
%endif
install -m 0755 $RPM_SOURCE_DIR/eximstats-html-update.py $RPM_BUILD_ROOT/%{_sbindir}
# apparmor profile
install -D -m 0644 $RPM_SOURCE_DIR/apparmor.usr.sbin.exim $RPM_BUILD_ROOT/usr/share/apparmor/extra-profiles/usr.sbin.exim

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
%set_permissions /usr/sbin/exim
%endif
if ! test -s etc/exim/exim.conf; then
	if test -s etc/exim.conf; then
		mv etc/exim.conf etc/exim/
		echo moving exim.conf to /etc/exim/
	else
		cp -p usr/share/doc/packages/%{name}/configure.default etc/exim/exim.conf
		echo copying default config file to /etc/exim/exim.conf
	fi
fi
%if 0%{?suse_version} > 1220
%{fillup_only}
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
%verify_permissions -e /usr/sbin/exim

%files
%defattr(-,root,root)
%ghost %{_docdir}/%{name}/doc/cve-2019-13917.rpmmoved
%doc ACKNOWLEDGMENTS CHANGES LICENCE NOTICE README.UPDATING README
%doc doc
%doc src/configure.default
%doc build-Linux-*/convert4r{3,4}
%doc util
%doc %{_mandir}/man8/*
/usr/sbin/exicyclog
/usr/sbin/exigrep
/usr/sbin/exiqgrep
%verify(not mode) %attr(4755,root,root) /usr/sbin/exim
/usr/sbin/exim_*
/usr/sbin/eximstats
/usr/sbin/exinext
/usr/sbin/exipick
/usr/sbin/exiqsumm
/usr/sbin/exiwhat
%dir /etc/exim
%if 0%{?suse_version} > 1220
%{_unitdir}/exim.service
%else
%config /etc/init.d/exim
%endif
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/exim
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/exim
%endif
%if %{?suse_version:%suse_version}%{?!suse_version:99999} < 1000
%config(noreplace) /etc/permissions.d/exim
%endif
%dir /usr/share/apparmor
%dir /usr/share/apparmor/extra-profiles
%config(noreplace) /usr/share/apparmor/extra-profiles/usr.sbin.exim
/usr/sbin/rcexim
/usr/bin/mailq
/usr/bin/runq
/usr/bin/rsmtp
/usr/bin/newaliases
/usr/sbin/sendmail
/usr/lib/sendmail
%{_fillupdir}/sysconfig.exim
%dir %attr(750,mail,mail) /var/log/exim
%dir %attr(1777,root,root) /var/spool/mail
/var/mail

%files -n eximon
%defattr(-,root,root)
/usr/bin/eximon
/usr/bin/eximon.bin

%files -n eximstats-html
%defattr(-,root,root)
%attr(0750,root,www) /srv/www/eximstats
%dir /etc/apache2
%dir /etc/apache2/conf.d
%config /etc/apache2/conf.d/eximstats.conf
%{_sbindir}/eximstats-html-update.py

%changelog
