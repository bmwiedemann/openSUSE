#
# spec file for package postfix
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
%define pf_uid               51
%define pf_gid               51
%define maildrop_gid         59
%define mail_group	         mail
%define conf_backup_dir      %{_localstatedir}/adm/backup/%{name}
%define vmusr vmail
%define vmgid 303
%define vmid 303
%define vmdir /srv/maildirs
%define unitdir %{_libexecdir}/systemd
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if 0%{?suse_version} >= 1320 || ( 0%{?suse_version} == 1315 && 0%{?is_opensuse} )
%bcond_without lmdb
%bcond_without libnsl
%else
%bcond_with    lmdb
%bcond_with    libnsl
%endif
Name:           postfix
Version:        3.5.2
Release:        0
Summary:        A fast, secure, and flexible mailer
License:        IPL-1.0 OR EPL-2.0
Group:          Productivity/Networking/Email/Servers
URL:            http://www.postfix.org
Source0:        http://cdn.postfix.johnriley.me/mirrors/postfix-release/official/postfix-%{version}.tar.gz
Source2:        %{name}-SuSE.tar.gz
Source3:        %{name}-mysql.tar.bz2
Source10:       %{name}-rpmlintrc
Source11:       check_mail_queue
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
BuildRequires:  ca-certificates
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
BuildRequires:  diffutils
BuildRequires:  fdupes
BuildRequires:  libicu-devel
BuildRequires:  libopenssl-devel
BuildRequires:  m4
BuildRequires:  mysql-devel
BuildRequires:  openldap2-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  shadow
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(systemd)
Requires:       iproute2
Requires(post): permissions
Requires(pre):  %fillup_prereq
Requires(pre):  permissions
Requires(pre):  shadow
Conflicts:      exim
Conflicts:      sendmail
Provides:       smtp_daemon
%{?systemd_requires}
%if %{with lmdb}
BuildRequires:  lmdb-devel
%endif
%if %{with libnsl}
BuildRequires:  libnsl-devel
%endif
%if 0%{?suse_version} >= 1330
Requires:       system-user-nobody
Requires:       group(%{mail_group})
Requires(pre):  group(%{mail_group})
%endif

%description
Postfix aims to be an alternative to the widely-used sendmail program.

%package      devel
Summary:        Development headers for the %{name} package
Group:          Development/Libraries/C and C++
Requires(pre):  %{name} = %{version}

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
Requires(pre):  shadow

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

%if %{with lmdb}
%package      lmdb
Summary:        Postfix plugin to support LMDB maps
Group:          Productivity/Networking/Email/Servers
Requires(pre):  %{name} = %{version}

%description lmdb
Postfix plugin to support LMDB maps. This library will be loaded
by starting %{name} if you'll access a postmap which is stored in
PostgreSQL.
%endif

%prep
%setup -q -a 2 -a 3
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10

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
export CCARGS="${CCARGS} -DHAS_LDAP -DLDAP_DEPRECATED=1 -DUSE_LDAP_SASL"
export AUXLIBS_LDAP="-lldap -llber"
#
export CCARGS="${CCARGS} -DHAS_PCRE"
export AUXLIBS_PCRE="-lpcre"
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
%if %{with lmdb}
export CCARGS="${CCARGS} -DHAS_LMDB -I/usr/local/include" \
export AUXLIBS_LMDB="-llmdb"
%endif
#
# TODO
#export AUXLIBS_SQLITE
#export AUXLIBS_CDB
#export AUXLIBS_SDBM

export PIE=-pie
# using SHLIB_RPATH to specify unrelated linker flags, because LDFLAGS is
# ignored
make makefiles pie=yes shared=yes dynamicmaps=yes \
  shlib_directory=%{_prefix}/lib/%{name} \
  meta_directory=%{_prefix}/lib/%{name} \
  config_directory=%{_sysconfdir}/%{name} \
  SHLIB_RPATH="-Wl,-rpath,%{pf_shlib_directory} -Wl,-z,relro,-z,now"
make %{?_smp_mflags}
# ---------------------------------------------------------------------------

%install
groupadd -g %{pf_gid} -o -r %{name} 2> /dev/null || :
groupadd -g %{maildrop_gid} -o -r maildrop 2> /dev/null || :
useradd -r -o -g %{name} -u %{pf_uid} -s /bin/false -c "Postfix Daemon" -d /%{pf_queue_directory} %{name} 2> /dev/null || :
usermod -a -G %{maildrop_gid},%{mail_group} %{name} 2> /dev/null || :
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp conf/* %{buildroot}%{_sysconfdir}/%{name}
# create our default postfix ssl DIR (/etc/postfix/ssl)
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/ssl/certs
# link cacerts to /etc/ssl/certs
ln -sf ../../ssl/certs %{buildroot}%{_sysconfdir}/%{name}/ssl/cacerts
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
ln -sf ../sbin/sendmail %{buildroot}%{_libexecdir}/sendmail
for i in qmqp-source smtp-sink smtp-source; do
	install -m 755 bin/$i %{buildroot}%{_sbindir}/$i
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
install -m 644 %{name}-SuSE/smtp %{buildroot}%{_sysconfdir}/pam.d/smtp
mkdir -p %{buildroot}%{_fillupdir}
sed -e 's;@lib@;%{_lib};g' %{name}-SuSE/sysconfig.%{name} > %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -m 644 %{name}-SuSE/sysconfig.mail-%{name} %{buildroot}%{_fillupdir}/sysconfig.mail-%{name}
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
    -e 's;@mailq_path@;%{pf_mailq_path};' %{name}-SuSE/config.%{name} > %{buildroot}%{_sbindir}/config.%{name}
chmod 755 %{buildroot}%{_sbindir}/config.%{name}
install -m 644 %{name}-SuSE/dynamicmaps.cf %{buildroot}%{_sysconfdir}/%{name}/dynamicmaps.cf
install -m 644 %{name}-SuSE/ldap_aliases.cf %{buildroot}%{_sysconfdir}/%{name}/ldap_aliases.cf
install -m 644 %{name}-SuSE/helo_access %{buildroot}%{_sysconfdir}/%{name}/helo_access
install -m 644 %{name}-SuSE/permissions %{buildroot}%{_sysconfdir}/permissions.d/%{name}
install -m 644 %{name}-SuSE/sender_canonical %{buildroot}%{_sysconfdir}/%{name}/sender_canonical
install -m 644 %{name}-SuSE/relay %{buildroot}%{_sysconfdir}/%{name}/relay
install -m 644 %{name}-SuSE/relay_ccerts %{buildroot}%{_sysconfdir}/%{name}/relay_ccerts
install -m 600 %{name}-SuSE/sasl_passwd %{buildroot}%{_sysconfdir}/%{name}/sasl_passwd
mkdir -p %{buildroot}%{_sysconfdir}/sasl2
install -m 600 %{name}-SuSE/smtpd.conf %{buildroot}%{_sysconfdir}/sasl2/smtpd.conf
install -m 644 %{name}-SuSE/openssl_%{name}.conf.in %{buildroot}%{_sysconfdir}/%{name}/openssl_%{name}.conf.in
install -m 755 %{name}-SuSE/mk%{name}cert %{buildroot}%{_sbindir}/mk%{name}cert
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
install -m 644 %{name}-SuSE/%{name}-files %{buildroot}%{pf_shlib_directory}/%{name}-files
# postfix-mysql
install -m 644 %{name}-mysql/main.cf-mysql %{buildroot}%{_sysconfdir}/%{name}/main.cf-mysql
install -m 640 %{name}-mysql/*_maps.cf     %{buildroot}%{_sysconfdir}/%{name}/
# create paranoid permissions file
printf '%%-38s %%-18s %%s\n' %{_sbindir}/postdrop "root.%{pf_setgid_group}" "0755" >> %{buildroot}%{_sysconfdir}/permissions.d/%{name}.paranoid
printf '%%-38s %%-18s %%s\n' %{_sbindir}/postqueue "root.%{pf_setgid_group}" "0755" >> %{buildroot}%{_sysconfdir}/permissions.d/%{name}.paranoid
install -m 644 include/*.h %{buildroot}%{_includedir}/%{name}/
# some rpmlint stuff
# remove unneeded examples/chroot-setup
for example in AIX42 BSDI* F* HPUX* IRIX* NETBSD1 NEXTSTEP3 OPENSTEP4 OSF1 Solaris*; do
  rm examples/chroot-setup/${example}
done
cp -a examples/* %{buildroot}%{pf_sample_directory}
cp -a html/*     %{buildroot}%{pf_html_directory}
cp -a auxiliary %{buildroot}%{pf_docdir}
rm %{buildroot}%{pf_docdir}/README_FILES/INSTALL
# Fix build for Leap 42.3.
rm -f %{buildroot}%{_sysconfdir}/%{name}/*.orig
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/system
install -m 0644 %{name}-SuSE/%{name}.service         %{buildroot}%{_unitdir}/%{name}.service
install -m 0755 %{name}-SuSE/config_%{name}.systemd  %{buildroot}%{_sysconfdir}/%{name}/system/config_%{name}
install -m 0755 %{name}-SuSE/update_chroot.systemd   %{buildroot}%{_sysconfdir}/%{name}/system/update_chroot
install -m 0755 %{name}-SuSE/update_postmaps.systemd %{buildroot}%{_sysconfdir}/%{name}/system/update_postmaps
install -m 0755 %{name}-SuSE/wait_qmgr.systemd       %{buildroot}%{_sysconfdir}/%{name}/system/wait_qmgr
install -m 0755 %{name}-SuSE/cond_slp.systemd        %{buildroot}%{_sysconfdir}/%{name}/system/cond_slp
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
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
# ---------------------------------------------------------------------------
install -m 755 %{SOURCE11} %{buildroot}%{_sbindir}/

%pre
%service_add_pre %{name}.service

VERSIONTEST=$(test -x usr/sbin/postconf && usr/sbin/postconf proxy_read_maps 2>/dev/null || :)
if [ -z "$VERSIONTEST" -a -f %{pf_queue_directory}/pid/master.pid ]; then
  if checkproc -p %{pf_queue_directory}/pid/master.pid usr/lib/%{name}/master; then
     echo "%{name} is still running. You have to stop %{name} in order to"
     echo "install a newer version."
     exit 1
  fi
fi
getent group %{name} >/dev/null || groupadd -g %{pf_gid} -o -r %{name}
getent group maildrop >/dev/null || groupadd -g %{maildrop_gid} -o -r maildrop
getent passwd %{name} >/dev/null || useradd -r -o -g %{name} -u %{pf_uid} -s /bin/false -c "Postfix Daemon" -d /%{pf_queue_directory} %{name}
usermod -a -G %{maildrop_gid},%{mail_group} %{name}
# ---------------------------------------------------------------------------

%pre mysql
#echo "PARAM_pre: "$1
# on `rpm -ivh` PARAM is 1
# on `rpm -Uvh` PARAM is 2
if [ "$1" = "1" ]; then
  echo "Adding %{vmusr} user"
  if [ -z "`getent group  %{vmusr} 2>/dev/null`" ]; then
    groupadd -r -g %{vmgid} %{vmusr}
  fi
  if [ -z "`getent passwd  %{vmusr} 2>/dev/null`" ]; then
    useradd -c "maildirs chef" -d %{vmdir} -g %{vmusr} -u %{vmid} -r -s /bin/false %{vmusr}
  fi
fi
# ---------------------------------------------------------------------------

%preun
%stop_on_removal %{name}
%service_del_preun %{name}.service
# ---------------------------------------------------------------------------

%preun mysql
#echo "PARAM_preun: "$1
# on `rpm -e` PARAM is 0
if [ "$1" = "0" ]; then
    FILE=etc/%{name}/dynamicmaps.cf
    if [ -e "$FILE" ] ; then
        if grep -q "^mysql[[:space:]]" ${FILE}; then
             echo "Removing mysql map entry from ${FILE}"
             sed "/^mysql[[:space:]]/d" ${FILE} > ${FILE}.$$ && \
                 cp --remove-destination ${FILE}.$$ ${FILE} && \
                 rm ${FILE}.$$
        fi
    else
        echo "Can not find \"$FILE\". Not updating the file." >&2
    fi
fi
# ---------------------------------------------------------------------------

%preun postgresql
if [ "$1" = 0 ] ; then
    FILE=etc/%{name}/dynamicmaps.cf
    if [ -e "$FILE" ] ; then
        if grep -q "^pgsql[[:space:]]" ${FILE}; then
             echo "Removing pgsql map entry from ${FILE}"
             sed "/^pgsql[[:space:]]/d" ${FILE} > ${FILE}.$$ && \
                 cp --remove-destination ${FILE}.$$ ${FILE} && \
                 rm ${FILE}.$$
        fi
    else
        echo "Can not find \"$FILE\". Not updating the file." >&2
    fi
fi
# ---------------------------------------------------------------------------

%post
# We never have to run suseconfig for postfix after installation
# We only start postfix own upgrade-configuration by update
if [ ${1:-0} -gt 1 ]; then
	touch %{_localstatedir}/adm/%{name}.configured
        # Check if main.cf and master.cf was changed manualy
        MAINCH=0
        if [ -e %{_localstatedir}/adm/SuSEconfig/md5%{_sysconfdir}/%{name}/main.cf ]; then
                MD5SUM1=$( cat %{_localstatedir}/adm/SuSEconfig/md5%{_sysconfdir}/%{name}/main.cf )
                MD5SUM2=$( grep -v "^#" %{_sysconfdir}/%{name}/main.cf | md5sum )
                if [ "$MD5SUM1" != "$MD5SUM2" ]; then
                   MAINCH=1
                fi
        fi
        MASTERCH=0
        if [ -e %{_localstatedir}/adm/SuSEconfig/md5%{_sysconfdir}/%{name}/master.cf ]; then
                MD5SUM1=$( cat %{_localstatedir}/adm/SuSEconfig/md5%{_sysconfdir}/%{name}/master.cf )
                MD5SUM2=$( grep -v "^#" %{_sysconfdir}/%{name}/master.cf | md5sum )
                if [ "$MD5SUM1" != "$MD5SUM2" ]; then
                   MASTERCH=1
                fi
        fi
        echo "Executing upgrade-configuration."
        %{_sbindir}/%{name} set-permissions upgrade-configuration setgid_group=%{pf_setgid_group} || :
        if [ "$(%{_sbindir}/postconf -h daemon_directory)" != "%{pf_daemon_directory}" ]; then
                %{_sbindir}/postconf daemon_directory=%{pf_daemon_directory}
        fi
        if [ $MASTERCH -eq 0 ]; then
           test -e %{_localstatedir}/adm/SuSEconfig/md5%{_sysconfdir}/%{name}/master.cf && grep -v "^#" %{_sysconfdir}/%{name}/master.cf | md5sum > %{_localstatedir}/adm/SuSEconfig/md5%{_sysconfdir}/postfix/master.cf
        fi
        if [ $MAINCH -eq 0 ]; then
           test -e %{_localstatedir}/adm/SuSEconfig/md5%{_sysconfdir}/%{name}/main.cf && grep -v "^#" %{_sysconfdir}/%{name}/main.cf | md5sum > %{_localstatedir}/adm/SuSEconfig/md5%{_sysconfdir}/postfix/main.cf
        fi
fi

%service_add_post %{name}.service

%set_permissions %{_sbindir}/postqueue
%set_permissions %{_sbindir}/postdrop
%set_permissions %{_sysconfdir}/%{name}/sasl_passwd
%set_permissions %{_sbindir}/sendmail

%{fillup_only postfix}
%{fillup_only -an mail}
/sbin/ldconfig

%verifyscript
%verify_permissions -e %{_sbindir}/postqueue
%verify_permissions -e %{_sbindir}/postdrop
%verify_permissions -e %{_sysconfdir}/%{name}/sasl_passwd
%verify_permissions -e %{_sbindir}/sendmail
%{fillup_only postfix}

%postun
%service_del_postun %{name}.service
/sbin/ldconfig

# ---------------------------------------------------------------------------

%post postgresql
FILE=etc/%{name}/dynamicmaps.cf
if ! grep -q "^pgsql[[:space:]]" ${FILE}; then
     echo "Adding pgsql map entry to ${FILE}"
     echo "pgsql   %{pf_shlib_directory}/dict_pgsql.so      dict_pgsql_open" >> ${FILE}
fi
# ---------------------------------------------------------------------------

%post mysql
FILE=etc/%{name}/dynamicmaps.cf
if ! grep -q "^mysql[[:space:]]" ${FILE}; then
     echo "Adding mysql map entry to ${FILE}"
     echo "mysql   %{pf_shlib_directory}/dict_mysql.so      dict_mysql_open" >> ${FILE}
fi
# ---------------------------------------------------------------------------

%files
%license LICENSE
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
%config(noreplace) %{_sysconfdir}/%{name}/ldap_aliases.cf
%config(noreplace) %{_sysconfdir}/%{name}/main.cf
%config(noreplace) %{_sysconfdir}/%{name}/master.cf
%attr(0750,root,root) %config %{_sysconfdir}/%{name}/post-install
%attr(0750,root,root) %config %{_sysconfdir}/%{name}/%{name}-tls-script
%attr(0750,root,root) %config %{_sysconfdir}/%{name}/%{name}-wrapper
%attr(0750,root,root) %config %{_sysconfdir}/%{name}/postmulti-script
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-files
%config(noreplace) %{_sysconfdir}/%{name}/relay
%config(noreplace) %{_sysconfdir}/%{name}/relay_ccerts
%config(noreplace) %{_sysconfdir}/%{name}/sasl_passwd
%config(noreplace) %{_sysconfdir}/%{name}/sender_canonical
%config(noreplace) %{_sysconfdir}/%{name}/virtual

%dir %{_sysconfdir}/sasl2
%config(noreplace) %{_sysconfdir}/sasl2/smtpd.conf
%config %{_sysconfdir}/%{name}/LICENSE
%config %{_sysconfdir}/%{name}/TLS_LICENSE
%config %{_sysconfdir}/permissions.d/%{name}
%config %{_sysconfdir}/permissions.d/%{name}.paranoid
%attr(0644, root, root) %config %{_sysconfdir}/%{name}/makedefs.out
%{pf_shlib_directory}/%{name}-files
# create our default postfix ssl DIR (/etc/postfix/ssl)
%dir %{_sysconfdir}/%{name}/ssl
%dir %{_sysconfdir}/%{name}/ssl/certs
%{_sysconfdir}/%{name}/ssl/cacerts
%dir %{_sysconfdir}/%{name}/system
%config %attr(0755,root,root) %{_sysconfdir}/%{name}/system/*
%{_unitdir}/%{name}.service
%verify(not mode) %attr(2755,root,%{pf_setgid_group}) %{_sbindir}/postdrop
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
%attr(0755,root,root) %{_sbindir}/postlog
%attr(0755,root,root) %{_sbindir}/postmap
%attr(0755,root,root) %{_sbindir}/postmulti
%attr(0755,root,root) %{_sbindir}/postsuper
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
%{pf_shlib_directory}/*[^.so]
%{pf_shlib_directory}/%{name}-ldap.so
%{pf_shlib_directory}/%{name}-pcre.so
%{pf_shlib_directory}/lib%{name}-dns.so
%{pf_shlib_directory}/lib%{name}-global.so
%{pf_shlib_directory}/lib%{name}-master.so
%{pf_shlib_directory}/lib%{name}-tls.so
%{pf_shlib_directory}/lib%{name}-util.so
%{pf_shlib_directory}/main.cf.proto
%{pf_shlib_directory}/master.cf.proto

%{conf_backup_dir}
%dir %attr(0700,%{name},root) %{pf_data_directory}
%{_mandir}/man?/*%{?ext_man}
%dir %attr(0755,root,root) /%{pf_queue_directory}
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

%files postgresql
%{pf_shlib_directory}/%{name}-pgsql.so

%if %{with lmdb}
%files lmdb
%{pf_shlib_directory}/%{name}-lmdb.so
%endif

%changelog
