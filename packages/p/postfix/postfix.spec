#
# spec file for package postfix
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


%define pf_docdir            %{_docdir}/%{name}-doc
%define pf_config_directory  %{_sysconfdir}/%{name}
%define pf_daemon_directory  %{_prefix}/lib/%{name}/bin/
%define _libexecdir          %{_prefix}/lib
%define pf_shlib_directory   %{_prefix}/lib/%{name}
%define pf_command_directory %{_sbindir}
%define pf_queue_directory   var/spool/%{name}
%define pf_sendmail_path     %{_sbindir}/sendmail
%define pf_newaliases_path   %{_bindir}/newaliases
%define pf_mailq_path        %{_bindir}/mailq
%define pf_setgid_group      maildrop
%define pf_readme_directory  %{_docdir}/%{name}-doc/README_FILES
%define pf_html_directory    %{_docdir}/%{name}-doc/html
%define pf_sample_directory  %{_docdir}/%{name}-doc/samples
%define pf_data_directory    %{_localstatedir}/lib/%{name}
%define pf_database_convert  %{_rundir}/%{name}-needs-convert
%define mail_group           mail
%define conf_backup_dir      %{_localstatedir}/adm/backup/%{name}
%define unitdir %{_prefix}/lib/systemd
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if 0%{?suse_version} < 1599
%bcond_without libnsl
%else
%bcond_with libnsl
%endif
%bcond_without ldap
Name:           postfix
Version:        3.9.0
Release:        0
Summary:        A fast, secure, and flexible mailer
License:        EPL-2.0 OR IPL-1.0
Group:          Productivity/Networking/Email/Servers
URL:            http://www.postfix.org
Source0:        https://de.postfix.org/ftpmirror/official/postfix-%{version}.tar.gz
Source1:        https://de.postfix.org/ftpmirror/official/postfix-%{version}.tar.gz.gpg2#/postfix-%{version}.tar.gz.asc
Source2:        %{name}-SUSE.tar.gz
Source3:        %{name}-mysql.tar.bz2
Source4:        postfix.keyring
Source10:       %{name}-rpmlintrc
Source11:       check_mail_queue
Source12:       postfix-user.conf
Source13:       postfix-vmail-user.conf
Patch1:         %{name}-no-md5.patch
Patch2:         pointer_to_literals.patch
Patch3:         ipv6_disabled.patch
Patch4:         %{name}-main.cf.patch
Patch5:         %{name}-master.cf.patch
Patch6:         %{name}-linux45.patch
Patch7:         %{name}-ssl-release-buffers.patch
Patch8:         %{name}-vda-v14-3.0.3.patch
Patch9:         fix-postfix-script.patch
Patch10:        %{name}-avoid-infinit-loop-if-no-permission.patch
Patch11:        set-default-db-type.patch
BuildRequires:  ca-certificates
BuildRequires:  cyrus-sasl-devel
BuildRequires:  diffutils
BuildRequires:  fdupes
BuildRequires:  libicu-devel
BuildRequires:  libopenssl-devel >= 1.1.1
BuildRequires:  lmdb-devel
BuildRequires:  m4
BuildRequires:  mysql-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  shadow
BuildRequires:  sysuser-tools
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(systemd)
Requires:       iproute2
Requires(post): permissions
Requires(pre):  %fillup_prereq
Requires(pre):  group(%{mail_group})
Requires(pre):  permissions
Requires(pre):  user(nobody)
Conflicts:      exim
Conflicts:      postfix-bdb
Conflicts:      sendmail
Provides:       postfix-lmdb = %{version}-%{release}
Obsoletes:      postfix-lmdb < %{version}-%{release}
Provides:       smtp_daemon
%{?systemd_ordering}
%sysusers_requires
%if %{with ldap}
BuildRequires:  openldap2-devel
%endif
%if %{with libnsl}
BuildRequires:  libnsl-devel
%endif
# /usr/lib/postfix/bin//post-install: line 667: ed: command not found
Requires(pre):  /usr/bin/ed
Requires(preun): /usr/bin/ed
Requires(post): /usr/bin/ed
Requires(postun): /usr/bin/ed
# /usr/sbin/config.postfix needs perl
Requires(pre):  perl
Requires(preun): perl
Requires(post): perl
Requires(postun): perl

%description
Postfix aims to be an alternative to the widely-used sendmail program.

%package      devel
Summary:        Development headers for the %{name} package
Group:          Development/Libraries/C and C++
Requires(pre):  %{name} = %{version}
BuildArch:      noarch

%description devel
Postfix aims to be an alternative to the widely-used sendmail program.

%package      doc
Summary:        Documentations for the %{name} package
Group:          Productivity/Networking/Email/Servers
BuildArch:      noarch

%description doc
Postfix aims to be an alternative to the widely-used sendmail program.
This package contains the documentation for %{name}

%package      mysql
Summary:        Postfix plugin to support MySQL maps
Group:          Productivity/Networking/Email/Servers
Requires(pre):  %{name} = %{version}
%sysusers_requires
%if 0%{?suse_version} < 1550
Provides:       group(vmail)
%endif

%description mysql
Postfix plugin to support MySQL maps. This library will be loaded by
starting %{name} if you'll access a postmap which is stored in mysql.

%package      postgresql
Summary:        Postfix plugin to support PostgreSQL maps
Group:          Productivity/Networking/Email/Servers
Requires(pre):  %{name} = %{version}

%description postgresql
Postfix plugin to support PostgreSQL maps. This library will be loaded
by starting %{name} if you'll access a postmap which is stored in
PostgreSQL.

%if %{with ldap}
%package      ldap
Summary:        Postfix LDAP map support
Group:          Productivity/Networking/Email/Servers
Requires:       %{name} = %{version}
Provides:       postfix:/usr/lib/postfix/postfix-ldap.so

%description ldap
This provides support for LDAP maps in Postfix. If you plan to use LDAP
maps with Postfix, you need this.
%endif

%prep
%setup -q -a 2 -a 3
%autopatch -p0

# ---------------------------------------------------------------------------

%build
unset AUXLIBS AUXLIBS_LDAP AUXLIBS_PCRE AUXLIBS_MYSQL AUXLIBS_PGSQL AUXLIBS_SQLITE AUXLIBS_CDB

export CCARGS="${CCARGS} %{optflags} -fcommon -Wno-comments -Wno-missing-braces -fPIC"
%ifarch s390 s390x ppc
export CCARGS="${CCARGS} -fsigned-char"
%endif
#
if pkg-config openssl ; then
  export CCARGS="${CCARGS} -DUSE_TLS $(pkg-config --cflags openssl)"
  export AUXLIBS="$AUXLIBS $(pkg-config --libs openssl)"
else
  export CCARGS="${CCARGS} -DUSE_TLS"
  export AUXLIBS="${AUXLIBS} -lssl -lcrypto"
fi
#
%if %{without libnsl}
export CCARGS="${CCARGS} -DNO_NIS"
%endif
%if %{with ldap}
export CCARGS="${CCARGS} -DHAS_LDAP -DLDAP_DEPRECATED=1 -DUSE_LDAP_SASL"
export AUXLIBS_LDAP="-lldap -llber"
%endif
#
export CCARGS="${CCARGS} -DHAS_PCRE=2"
export AUXLIBS_PCRE="-lpcre2-8"
#
export CCARGS="${CCARGS} -DUSE_SASL_AUTH -DUSE_CYRUS_SASL -I%{_includedir}/sasl"
if pkg-config libsasl2 ; then
  export AUXLIBS="$AUXLIBS $(pkg-config --libs libsasl2)"
else
  export AUXLIBS="$AUXLIBS -lsasl2"
fi
#
export CCARGS="${CCARGS} -DHAS_MYSQL $(mysql_config --cflags)"
export AUXLIBS_MYSQL="$(mysql_config --libs)"
#
if pkg-config --exists libpq ; then
  export CCARGS="${CCARGS} -DHAS_PGSQL $(pkg-config libpq --cflags)"
  export AUXLIBS_PGSQL="$(pkg-config libpq --libs)"
else
  export CCARGS="${CCARGS} -DHAS_PGSQL -I$(pg_config --includedir)"
  export AUXLIBS_PGSQL="-lpq"
fi
#
export CCARGS="${CCARGS} -DHAS_LMDB -I/usr/local/include" \
export AUXLIBS_LMDB="-llmdb"
#
# TODO
#export AUXLIBS_SQLITE
#export AUXLIBS_CDB
#export AUXLIBS_SDBM
# Remove berkeley DB and set lmdb as default
export CCARGS="${CCARGS} -DNO_DB -DDEF_DB_TYPE=\\\"lmdb\\\""

export PIE=-pie
# using SHLIB_RPATH to specify unrelated linker flags, because LDFLAGS is
# ignored
%make_build makefiles pie=yes shared=yes dynamicmaps=yes \
  daemon_directory=%{pf_daemon_directory} \
  shlib_directory=%{_prefix}/lib/%{name} \
  meta_directory=%{_prefix}/lib/%{name} \
  config_directory=%{pf_config_directory} \
  command_directory=%{pf_command_directory} \
  queue_directory=/%{pf_queue_directory} \
  sendmail_path=%{pf_sendmail_path} \
  newaliases_path=%{pf_newaliases_path} \
  mailq_path=%{pf_mailq_path} \
  manpage_directory=%{_mandir} \
  setgid_group=%{pf_setgid_group} \
  readme_directory=%{pf_readme_directory} \
  data_directory=%{pf_data_directory} \
  SHLIB_RPATH="-Wl,-rpath,%{pf_shlib_directory} -Wl,-z,relro,-z,now"
%make_build
# Create postfix user
%sysusers_generate_pre %{SOURCE12} postfix postfix-user.conf
%sysusers_generate_pre %{SOURCE13} vmail postfix-vmail-user.conf
# ---------------------------------------------------------------------------

%install
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
# create our default postfix ssl DIR (/etc/postfix/ssl)
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/ssl/certs
# link cacerts to /etc/ssl/certs
ln -s ../../ssl/certs %{buildroot}%{_sysconfdir}/%{name}/ssl/cacerts
cp lib/lib%{name}-*  %{buildroot}/%{_libdir}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}/%{_libdir}
sh postfix-install -non-interactive \
       install_root=%{buildroot} \
       config_directory=%{pf_config_directory} \
       daemon_directory=%{pf_daemon_directory} \
       command_directory=%{pf_command_directory} \
       queue_directory=/%{pf_queue_directory} \
       sendmail_path=%{pf_sendmail_path} \
       newaliases_path=%{pf_newaliases_path} \
       mailq_path=%{pf_mailq_path} \
       manpage_directory=%{_mandir} \
       setgid_group=%{pf_setgid_group} \
       readme_directory=%{pf_readme_directory} \
       data_directory=%{pf_data_directory}
ln -s ../sbin/sendmail %{buildroot}%{_libexecdir}/sendmail
for i in qmqp-source smtp-sink smtp-source; do
	install -pm 0755 bin/$i %{buildroot}%{_sbindir}/$i
done
mkdir -p %{buildroot}/sbin/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/permissions.d
mkdir -p %{buildroot}/%{_libdir}/sasl2
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}/%{conf_backup_dir}
mkdir -p %{buildroot}/%{pf_sample_directory}
mkdir -p %{buildroot}/%{pf_html_directory}
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
mkdir -p %{buildroot}/var/spool/mail
ln -s spool/mail %{buildroot}/var/mail
install -pm 0644 %{name}-SUSE/smtp %{buildroot}%{_sysconfdir}/pam.d/smtp
mkdir -p %{buildroot}%{_fillupdir}
sed -e 's;@lib@;%{_lib};g' %{name}-SUSE/sysconfig.%{name} > %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -pm 0644 %{name}-SUSE/sysconfig.mail-%{name} %{buildroot}%{_fillupdir}/sysconfig.mail-%{name}
sed -e 's;@lib@;%{_lib};g' \
    -e 's;@conf_backup_dir@;%{conf_backup_dir};' \
    -e 's;@daemon_directory@;%{pf_daemon_directory};' \
    -e 's;@readme_directory@;%{pf_readme_directory};' \
    -e 's;@html_directory@;%{pf_html_directory};' \
    -e 's;@sendmail_path@;%{pf_sendmail_path};' \
    -e 's;@setgid_group@;%{pf_setgid_group};' \
    -e 's;@manpage_directory@;%{_mandir};' \
    -e 's;@newaliases_path@;%{pf_newaliases_path};' \
    -e 's;@sample_directory@;%{pf_sample_directory};' \
    -e 's;@mailq_path@;%{pf_mailq_path};' %{name}-SUSE/config.%{name} > %{buildroot}%{_sbindir}/config.%{name}
chmod 0755 %{buildroot}%{_sbindir}/config.%{name}
install -pm 0644 %{name}-SUSE/ldap_aliases.cf %{buildroot}%{_sysconfdir}/%{name}/ldap_aliases.cf
install -pm 0644 %{name}-SUSE/helo_access %{buildroot}%{_sysconfdir}/%{name}/helo_access
install -pm 0644 %{name}-SUSE/permissions %{buildroot}%{_sysconfdir}/permissions.d/%{name}
install -pm 0644 %{name}-SUSE/sender_canonical %{buildroot}%{_sysconfdir}/%{name}/sender_canonical
install -pm 0644 %{name}-SUSE/relay %{buildroot}%{_sysconfdir}/%{name}/relay
install -pm 0644 %{name}-SUSE/relay_ccerts %{buildroot}%{_sysconfdir}/%{name}/relay_ccerts
install -pm 0644 %{name}-SUSE/relay_recipients %{buildroot}%{_sysconfdir}/%{name}/relay_recipients
install -pm 0600 %{name}-SUSE/sasl_passwd %{buildroot}%{_sysconfdir}/%{name}/sasl_passwd
mkdir -p %{buildroot}%{_sysconfdir}/sasl2
install -pm 0600 %{name}-SUSE/smtpd.conf %{buildroot}%{_sysconfdir}/sasl2/smtpd.conf
install -pm 0644 %{name}-SUSE/openssl_%{name}.conf.in %{buildroot}%{_sysconfdir}/%{name}/openssl_%{name}.conf.in
install -pm 0755 %{name}-SUSE/mk%{name}cert %{buildroot}%{_sbindir}/mk%{name}cert
{
cat<<EOF
#
# -----------------------------------------------------------------------
# NOTE: Many parameters have already been added to the end of this file
#       by config.postfix. So take care that you don't uncomment
#       and set a parameter without checking whether it has been added
#       to the end of this file.
# -----------------------------------------------------------------------
#
EOF
cat conf/main.cf
} > %{buildroot}%{_sysconfdir}/%{name}/main.cf
%{buildroot}%{_sbindir}/postconf -c %{buildroot}%{_sysconfdir}/%{name} \
        -e "manpage_directory = %{_mandir}" \
           "setgid_group      = %{pf_setgid_group}" \
           "mailq_path        = %{pf_mailq_path}" \
           "newaliases_path   = %{pf_newaliases_path}" \
           "sendmail_path     = %{pf_sendmail_path}" \
           "readme_directory  = %{pf_readme_directory}" \
           "html_directory    = %{pf_html_directory}" \
           "sample_directory  = %{pf_sample_directory}" \
	   "daemon_directory  = %{pf_daemon_directory}" \
	   "smtpd_helo_required  = yes" \
	   "smtpd_delay_reject   = yes" \
	   "disable_vrfy_command = yes" \
	   'smtpd_banner      = $myhostname ESMTP'
#Set Permissions
sed -i	-e 's/\(.*ldap.*\)/#\1/g' \
	-e 's/\(.*mysql.*\)/#\1/g' \
	-e 's/\(.*pgsql.*\)/#\1/g' \
	-e 's/\(.*LICENSE.*\)/#\1/g' \
	-e '/html_directory/d' \
	-e '/manpage_directory/d' \
	-e '/readme_directory/d' \
	%{buildroot}%{pf_shlib_directory}/postfix-files
mkdir -p %{buildroot}%{pf_shlib_directory}/postfix-files.d
# postfix-mysql
install -pm 0644 %{name}-mysql/main.cf-mysql %{buildroot}%{_sysconfdir}/%{name}/main.cf-mysql
install -pm 0640 %{name}-mysql/*_maps.cf     %{buildroot}%{_sysconfdir}/%{name}/
# create paranoid permissions file
printf '%%-38s %%-18s %%s\n' %{_sbindir}/postdrop "root.%{pf_setgid_group}" "0755" >> %{buildroot}%{_sysconfdir}/permissions.d/%{name}.paranoid
printf '%%-38s %%-18s %%s\n' %{_sbindir}/postqueue "root.%{pf_setgid_group}" "0755" >> %{buildroot}%{_sysconfdir}/permissions.d/%{name}.paranoid
install -pm 0644 include/*.h %{buildroot}%{_includedir}/%{name}/
# some rpmlint stuff
# remove unneeded examples/chroot-setup
for example in AIX42 BSDI* F* HPUX* IRIX* NETBSD1 NEXTSTEP3 OPENSTEP4 OSF1 Solaris*; do
  rm examples/chroot-setup/${example}
done
cp -a examples/* %{buildroot}%{pf_sample_directory}
cp -a html/*     %{buildroot}%{pf_html_directory}
cp -a auxiliary %{buildroot}%{pf_docdir}
rm %{buildroot}%{pf_docdir}/README_FILES/INSTALL
rm -r %{buildroot}%{pf_docdir}/auxiliary/qshape
install -p auxiliary/qshape/qshape.pl %{buildroot}%{_sbindir}/qshape
mantools/srctoman - auxiliary/qshape/qshape.pl > %{buildroot}%{_mandir}/man1/qshape.1
# Fix build for Leap 42.3.
rm -f %{buildroot}%{_sysconfdir}/%{name}/*.orig
mkdir -p %{buildroot}%{_unitdir}/mail-transfer-agent.target.wants/
mkdir -p %{buildroot}%{pf_shlib_directory}/systemd
install -pm 0644 %{name}-SUSE/%{name}.service         %{buildroot}%{_unitdir}/%{name}.service
install -pm 0755 %{name}-SUSE/config_%{name}.systemd  %{buildroot}%{pf_shlib_directory}/systemd/config_%{name}
install -pm 0755 %{name}-SUSE/update_chroot.systemd   %{buildroot}%{pf_shlib_directory}/systemd/update_chroot
install -pm 0755 %{name}-SUSE/update_postmaps.systemd %{buildroot}%{pf_shlib_directory}/systemd/update_postmaps
install -pm 0755 %{name}-SUSE/wait_qmgr.systemd       %{buildroot}%{pf_shlib_directory}/systemd/wait_qmgr
install -pm 0755 %{name}-SUSE/cond_slp.systemd        %{buildroot}%{pf_shlib_directory}/systemd/cond_slp
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -sv %{_unitdir}/%{name}.service %{buildroot}%{_unitdir}/mail-transfer-agent.target.wants/%{name}.service
%fdupes %{buildroot}%{pf_docdir}
%fdupes %{buildroot}%{_mandir}
for path in %{buildroot}%{pf_shlib_directory}/lib%{name}-*.so
do
  test -e "$path" || continue
  name=${path##*/}
  cmp "$path" %{buildroot}%{_libdir}/$name || continue
  rm -vf $path
  ln -sf %{_libdir}/$name $path
done

# create dynamicmaps.cf.d entries for optional modules
sed -n -e '/^#/p' -e '/mysql/p' %{buildroot}%{pf_shlib_directory}/dynamicmaps.cf > %{buildroot}%{pf_shlib_directory}/dynamicmaps.cf.d/%{name}-mysql.cf
sed -i -e '/mysql/d' %{buildroot}%{pf_shlib_directory}/dynamicmaps.cf
sed -n -e '/^#/p' -e '/pgsql/p' %{buildroot}%{pf_shlib_directory}/dynamicmaps.cf > %{buildroot}%{pf_shlib_directory}/dynamicmaps.cf.d/%{name}-pgsql.cf
sed -i -e '/pgsql/d' %{buildroot}%{pf_shlib_directory}/dynamicmaps.cf
%if %{with ldap}
sed -n -e '/^#/p' -e "/ldap/p" %{buildroot}%{pf_shlib_directory}/dynamicmaps.cf > %{buildroot}%{pf_shlib_directory}/dynamicmaps.cf.d/%{name}-ldap.cf
sed -i -e '/ldap/d' %{buildroot}%{pf_shlib_directory}/dynamicmaps.cf
%endif

install -m 755 %{SOURCE11} %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE12} %{buildroot}%{_sysusersdir}/
install -m 644 %{SOURCE13} %{buildroot}%{_sysusersdir}/

# ---------------------------------------------------------------------------

%pre -f postfix.pre
# If existing default database type is hash, we need to convert the
# databases because hash (and btree) is no longer supported after
# the upgrade
if [ -x %{_sbindir}/postconf ]; then
	DEF_DB_TYPE=$(postconf default_database_type)
	case $DEF_DB_TYPE in *hash)
		touch %{pf_database_convert}
	esac
fi
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
# We never have to run suseconfig for postfix after installation
# We only start postfix own upgrade-configuration by update
#
# If the default database type of the previous installation was
# hash, we also need to rebuild the databases in the new lmdb
# format
if [ ${1:-0} -gt 1 ]; then
	touch %{_localstatedir}/adm/%{name}.configured
	echo "Executing upgrade-configuration."
	%{_sbindir}/%{name} set-permissions upgrade-configuration setgid_group=%{pf_setgid_group} || :
	if [ "$(%{_sbindir}/postconf -h daemon_directory)" != "%{pf_daemon_directory}" ]; then
		%{_sbindir}/postconf daemon_directory=%{pf_daemon_directory}
	fi
	if [ -e %{pf_database_convert} ]; then
		sed -i -E "s/(btree|hash):/lmdb:/g" %{pf_config_directory}/{main.cf,master.cf}
		for i in $(find %{pf_config_directory} -name "*.db"); do
			postmap ${i%.db}
		done
		for i in $(find %{_sysconfdir}/aliases.d/ -name "*.db"); do
			postalias ${i%.db}
		done
		if [ -e %{_sysconfdir}/aliases.db ]; then
			postalias %{_sysconfdir}/aliases
		fi
		rm %{pf_database_convert}
	fi
fi
%set_permissions %{_sbindir}/postdrop
%set_permissions %{_sbindir}/postlog
%set_permissions %{_sbindir}/postqueue
%set_permissions %{_sysconfdir}/%{name}/sasl_passwd
%set_permissions %{_sbindir}/sendmail
%{fillup_only postfix}
%{fillup_only -an mail}
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%verifyscript
%verify_permissions -e %{_sbindir}/postdrop
%verify_permissions -e %{_sbindir}/postlog
%verify_permissions -e %{_sbindir}/postqueue
%verify_permissions -e %{_sysconfdir}/%{name}/sasl_passwd
%verify_permissions -e %{_sbindir}/sendmail

# ---------------------------------------------------------------------------

%pre    mysql -f vmail.pre
%post   mysql -p /sbin/ldconfig
%postun mysql -p /sbin/ldconfig
%post   postgresql -p /sbin/ldconfig
%postun postgresql -p /sbin/ldconfig

%if %{with ldap}
%post   ldap -p /sbin/ldconfig
%postun ldap -p /sbin/ldconfig
%endif

%files
%license LICENSE TLS_LICENSE
%doc RELEASE_NOTES
%config %{_sysconfdir}/pam.d/*
%{_fillupdir}/sysconfig.%{name}
%{_fillupdir}/sysconfig.mail-%{name}
%{_sbindir}/config.%{name}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/main.cf.default
%config(noreplace) %{_sysconfdir}/%{name}/[^mysql]*[^mysql]
%config(noreplace) %{_sysconfdir}/%{name}/access
%config(noreplace) %{_sysconfdir}/%{name}/aliases
%config(noreplace) %{_sysconfdir}/%{name}/canonical
%config(noreplace) %{_sysconfdir}/%{name}/header_checks
%config(noreplace) %{_sysconfdir}/%{name}/helo_access
%config(noreplace) %{_sysconfdir}/%{name}/main.cf
%config(noreplace) %{_sysconfdir}/%{name}/master.cf
%config(noreplace) %{_sysconfdir}/%{name}/relay
%config(noreplace) %{_sysconfdir}/%{name}/relay_ccerts
%config(noreplace) %{_sysconfdir}/%{name}/relay_recipients
%config(noreplace) %{_sysconfdir}/%{name}/sasl_passwd
%config(noreplace) %{_sysconfdir}/%{name}/sender_canonical
%config(noreplace) %{_sysconfdir}/%{name}/virtual
%ghost %{_sysconfdir}/%{name}/*.lmdb
%ghost %{_sysconfdir}/aliases.lmdb
%dir %{_sysconfdir}/sasl2
%config(noreplace) %{_sysconfdir}/sasl2/smtpd.conf
%exclude %{_sysconfdir}/%{name}/LICENSE
%exclude %{_sysconfdir}/%{name}/TLS_LICENSE
%config %{_sysconfdir}/permissions.d/%{name}
%config %{_sysconfdir}/permissions.d/%{name}.paranoid
%{pf_shlib_directory}/%{name}-files
# create our default postfix ssl DIR (/etc/postfix/ssl)
%dir %{_sysconfdir}/%{name}/ssl
%dir %{_sysconfdir}/%{name}/ssl/certs
%{_sysconfdir}/%{name}/ssl/cacerts
%dir %{pf_shlib_directory}/systemd
%attr(0755,root,root) %{pf_shlib_directory}/systemd/*
%{_unitdir}/%{name}.service
%{_unitdir}/mail-transfer-agent.target.wants
%verify(not mode) %attr(2755,root,%{pf_setgid_group}) %{_sbindir}/postdrop
%verify(not mode) %attr(2755,root,%{pf_setgid_group}) %{_sbindir}/postlog
%verify(not mode) %attr(2755,root,%{pf_setgid_group}) %{_sbindir}/postqueue
%{_bindir}/mailq
%{_bindir}/newaliases
%attr(0755,root,root) %{_sbindir}/sendmail
%attr(0755,root,root) %{_sbindir}/postalias
%attr(0755,root,root) %{_sbindir}/postcat
%attr(0755,root,root) %{_sbindir}/postconf
%attr(0755,root,root) %{_sbindir}/%{name}
%attr(0755,root,root) %{_sbindir}/postkick
%attr(0755,root,root) %{_sbindir}/postlock
%attr(0755,root,root) %{_sbindir}/postmap
%attr(0755,root,root) %{_sbindir}/postmulti
%attr(0755,root,root) %{_sbindir}/postsuper
%attr(0755,root,root) %{_sbindir}/qshape
%attr(0755,root,root) %{_sbindir}/qmqp-source
%attr(0755,root,root) %{_sbindir}/smtp-sink
%attr(0755,root,root) %{_sbindir}/smtp-source
%attr(0755,root,root) %{_sbindir}/mk%{name}cert
%attr(0755,root,root) %{_sbindir}/check_mail_queue
%attr(0755,root,root) %{_sbindir}/config.%{name}
%{_sbindir}/rc%{name}
%{_libdir}/lib*
%{_libexecdir}/sendmail
%dir %{pf_shlib_directory}
%{pf_shlib_directory}/%{name}-pcre.so
%{pf_shlib_directory}/%{name}-lmdb.so
%{pf_shlib_directory}/lib%{name}-dns.so
%{pf_shlib_directory}/lib%{name}-global.so
%{pf_shlib_directory}/lib%{name}-master.so
%{pf_shlib_directory}/lib%{name}-tls.so
%{pf_shlib_directory}/lib%{name}-util.so
%{pf_shlib_directory}/dynamicmaps.cf
%{pf_shlib_directory}/main.cf.proto
%{pf_shlib_directory}/makedefs.out
%{pf_shlib_directory}/master.cf.proto
%dir %{pf_daemon_directory}
%{pf_daemon_directory}/*
%dir %{pf_shlib_directory}/dynamicmaps.cf.d
%dir %{pf_shlib_directory}/postfix-files.d

%{conf_backup_dir}
%dir %attr(0700,%{name},root) %{pf_data_directory}
%exclude %{_mandir}/man5/ldap_table.5*
%exclude %{_mandir}/man5/mysql_table.5*
%exclude %{_mandir}/man5/pgsql_table.5*
%{_mandir}/man?/*%{?ext_man}
%dir %attr(0755,root,root) /%{pf_queue_directory}
%dir %attr(0755,root,root) /%{pf_queue_directory}/pid
%dir %attr(0700,%{name},root) /%{pf_queue_directory}/active
%dir %attr(0700,%{name},root) /%{pf_queue_directory}/bounce
%dir %attr(0700,%{name},root) /%{pf_queue_directory}/corrupt
%dir %attr(0700,%{name},root) /%{pf_queue_directory}/defer
%dir %attr(0700,%{name},root) /%{pf_queue_directory}/deferred
%dir %attr(0700,%{name},root) /%{pf_queue_directory}/flush
%dir %attr(0700,%{name},root) /%{pf_queue_directory}/hold
%dir %attr(0700,%{name},root) /%{pf_queue_directory}/incoming
%dir %attr(0700,%{name},root) /%{pf_queue_directory}/private
%dir %attr(0700,%{name},root) /%{pf_queue_directory}/saved
%dir %attr(0700,%{name},root) /%{pf_queue_directory}/trace
%dir %attr(0730,%{name},maildrop) /%{pf_queue_directory}/maildrop
%dir %attr(0710,%{name},maildrop) /%{pf_queue_directory}/public
%{_sysusersdir}/postfix-user.conf
%dir %attr(1777,root,root) /var/spool/mail
/var/mail

%files devel
%{_includedir}/%{name}/

%files doc
%defattr(0644,root,root,0755)
%{pf_docdir}/

%files mysql
%doc %{name}-mysql/%{name}-mysql.sql
%config(noreplace) %attr(640, root, %{name}) %{_sysconfdir}/%{name}/*_maps.cf
%config(noreplace) %{_sysconfdir}/%{name}/main.cf-mysql
%{pf_shlib_directory}/%{name}-mysql.so
%{pf_shlib_directory}/dynamicmaps.cf.d/%{name}-mysql.cf
%{_mandir}/man5/mysql_table.5%{?ext_man}
%{_sysusersdir}/postfix-vmail-user.conf

%files postgresql
%{pf_shlib_directory}/%{name}-pgsql.so
%{pf_shlib_directory}/dynamicmaps.cf.d/%{name}-pgsql.cf
%{_mandir}/man5/pgsql_table.5%{?ext_man}

%if %{with ldap}
%files ldap
%config(noreplace) %{_sysconfdir}/%{name}/ldap_aliases.cf
%{pf_shlib_directory}/%{name}-ldap.so
%{pf_shlib_directory}/dynamicmaps.cf.d/%{name}-ldap.cf
%{_mandir}/man5/ldap_table.5%{?ext_man}
%endif

%changelog
