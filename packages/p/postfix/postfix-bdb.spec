#
# spec file for package postfix-bdb
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


%define pf_docdir            %{_docdir}/postfix-doc
%define pf_config_directory  %{_sysconfdir}/postfix
%define pf_daemon_directory  %{_prefix}/lib/postfix/bin/
%define _libexecdir          %{_prefix}/lib
%define pf_shlib_directory   %{_prefix}/lib/postfix
%define pf_command_directory %{_sbindir}
%define pf_queue_directory   var/spool/postfix
%define pf_sendmail_path     %{_sbindir}/sendmail
%define pf_newaliases_path   %{_bindir}/newaliases
%define pf_mailq_path        %{_bindir}/mailq
%define pf_setgid_group      maildrop
%define pf_readme_directory  %{_docdir}/postfix-doc/README_FILES
%define pf_html_directory    %{_docdir}/postfix-doc/html
%define pf_sample_directory  %{_docdir}/postfix-doc/samples
%define pf_data_directory    %{_localstatedir}/lib/postfix
%if 0%{?suse_version} < 1330
%define pf_uid               51
%define pf_gid               51
%define maildrop_gid         59
%define vmusr                vmail
%define vmgid                303
%define vmid                 303
%define vmdir                /srv/maildirs
%endif
%define mail_group           mail
%define conf_backup_dir      %{_localstatedir}/adm/backup/postfix
%define unitdir %{_prefix}/lib/systemd
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if 0%{?suse_version} >= 1320 || ( 0%{?suse_version} == 1315 && 0%{?is_opensuse} )
%bcond_without lmdb
%else
%bcond_with    lmdb
%endif
%if 0%{?suse_version} >= 1320 && 0%{?suse_version} < 1599
%bcond_without libnsl
%else
%bcond_with    libnsl
%endif
%bcond_without ldap
Name:           postfix-bdb
Version:        3.9.0
Release:        0
Summary:        A fast, secure, and flexible mailer
License:        EPL-2.0 OR IPL-1.0
Group:          Productivity/Networking/Email/Servers
URL:            http://www.postfix.org
Source0:        https://de.postfix.org/ftpmirror/official/postfix-%{version}.tar.gz
Source1:        https://de.postfix.org/ftpmirror/official/postfix-%{version}.tar.gz.gpg2#/postfix-%{version}.tar.gz.asc
Source2:        postfix-SUSE.tar.gz
Source3:        postfix-mysql.tar.bz2
#Source4:        http://cdn.postfix.johnriley.me/mirrors/postfix-release/wietse.pgp#/postfix.keyring
Source4:        postfix.keyring
Source10:       postfix-rpmlintrc
Source11:       check_mail_queue
Source12:       postfix-user.conf
Source13:       postfix-vmail-user.conf
Patch1:         postfix-no-md5.patch
Patch2:         pointer_to_literals.patch
Patch3:         ipv6_disabled.patch
Patch4:         postfix-bdb-main.cf.patch
Patch5:         postfix-master.cf.patch
Patch6:         postfix-linux45.patch
Patch7:         postfix-ssl-release-buffers.patch
Patch8:         postfix-vda-v14-3.0.3.patch
Patch9:         fix-postfix-script.patch
Patch10:        postfix-avoid-infinit-loop-if-no-permission.patch
BuildRequires:  ca-certificates
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
BuildRequires:  diffutils
BuildRequires:  fdupes
BuildRequires:  libicu-devel
BuildRequires:  libopenssl-devel >= 1.1.1
BuildRequires:  m4
BuildRequires:  mysql-devel
%if %{with ldap}
BuildRequires:  openldap2-devel
%endif
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  shadow
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(systemd)
Requires:       iproute2
Requires(post): permissions
Requires(pre):  %fillup_prereq
Requires(pre):  permissions
Conflicts:      exim
Conflicts:      postfix
Conflicts:      sendmail
Provides:       smtp_daemon
%{?systemd_ordering}
%if %{with lmdb}
BuildRequires:  lmdb-devel
%endif
%if %{with libnsl}
BuildRequires:  libnsl-devel
%endif
%if 0%{?suse_version} >= 1330
BuildRequires:  sysuser-tools
Requires(pre):  user(nobody)
Requires(pre):  group(%{mail_group})
%sysusers_requires
%else
Requires(pre):  shadow
%endif
# /usr/lib/postfix/bin//post-install: line 667: ed: command not found
Requires(pre):  ed
Requires(preun): ed
Requires(post): ed
Requires(postun): ed
# /usr/sbin/config.postfix needs perl
Requires(pre):  perl
Requires(preun): perl
Requires(post): perl
Requires(postun): perl

%description
Postfix aims to be an alternative to the widely-used sendmail program with bdb support

%if %{with lmdb}
%package    lmdb
Summary:        Postfix plugin to support LMDB maps
Group:          Productivity/Networking/Email/Servers
Requires(pre):  postfix-bdb = %{version}
Conflicts:      postfix
Provides:       postfix-lmdb = %{version}-%{release}
Obsoletes:      postfix-lmdb < %{version}-%{release}
Conflicts:      postfix-lmdb < %{version}-%{release}

%description lmdb
Postfix plugin to support LMDB maps. This library will be loaded
by starting postfix if you'll access a postmap which is stored in
lmdb.
%endif

%prep
%setup -q -n postfix-%{version} -a 2 -a 3
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
#
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
  shlib_directory=%{_prefix}/lib/postfix \
  meta_directory=%{_prefix}/lib/postfix \
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
  data_directory=%{pf_data_directory} \
  SHLIB_RPATH="-Wl,-rpath,%{pf_shlib_directory} -Wl,-z,relro,-z,now"
make %{?_smp_mflags}
%if 0%{?suse_version} >= 1330
# Create postfix user
%sysusers_generate_pre %{SOURCE12} postfix postfix-user.conf
%sysusers_generate_pre %{SOURCE13} vmail postfix-vmail-user.conf
%endif
# ---------------------------------------------------------------------------

%install
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}%{_sysconfdir}/postfix
cp conf/* %{buildroot}%{_sysconfdir}/postfix
# create our default postfix ssl DIR (/etc/postfix/ssl)
mkdir -p %{buildroot}%{_sysconfdir}/postfix/ssl/certs
# link cacerts to /etc/ssl/certs
ln -sf ../../ssl/certs %{buildroot}%{_sysconfdir}/postfix/ssl/cacerts
cp lib/libpostfix-*  %{buildroot}/%{_libdir}
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
mkdir -p %{buildroot}%{_includedir}/postfix
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
mkdir -p %{buildroot}/var/spool/mail
ln -s spool/mail %{buildroot}/var/mail
install -m 644 postfix-SUSE/smtp %{buildroot}%{_sysconfdir}/pam.d/smtp
mkdir -p %{buildroot}%{_fillupdir}
sed -e 's;@lib@;%{_lib};g' postfix-SUSE/sysconfig.postfix > %{buildroot}%{_fillupdir}/sysconfig.postfix
install -m 644 postfix-SUSE/sysconfig.mail-postfix %{buildroot}%{_fillupdir}/sysconfig.mail-postfix
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
    -e 's;@mailq_path@;%{pf_mailq_path};' postfix-SUSE/config.postfix > %{buildroot}%{_sbindir}/config.postfix
chmod 755 %{buildroot}%{_sbindir}/config.postfix
install -m 644 postfix-SUSE/dynamicmaps.cf %{buildroot}%{_sysconfdir}/postfix/dynamicmaps.cf
install -m 644 postfix-SUSE/ldap_aliases.cf %{buildroot}%{_sysconfdir}/postfix/ldap_aliases.cf
install -m 644 postfix-SUSE/helo_access %{buildroot}%{_sysconfdir}/postfix/helo_access
install -m 644 postfix-SUSE/permissions %{buildroot}%{_sysconfdir}/permissions.d/postfix
install -m 644 postfix-SUSE/sender_canonical %{buildroot}%{_sysconfdir}/postfix/sender_canonical
install -m 644 postfix-SUSE/relay %{buildroot}%{_sysconfdir}/postfix/relay
install -m 644 postfix-SUSE/relay_ccerts %{buildroot}%{_sysconfdir}/postfix/relay_ccerts
install -m 600 postfix-SUSE/sasl_passwd %{buildroot}%{_sysconfdir}/postfix/sasl_passwd
mkdir -p %{buildroot}%{_sysconfdir}/sasl2
install -m 600 postfix-SUSE/smtpd.conf %{buildroot}%{_sysconfdir}/sasl2/smtpd.conf
install -m 644 postfix-SUSE/openssl_postfix.conf.in %{buildroot}%{_sysconfdir}/postfix/openssl_postfix.conf.in
install -m 755 postfix-SUSE/mkpostfixcert %{buildroot}%{_sbindir}/mkpostfixcert
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
} > %{buildroot}%{_sysconfdir}/postfix/main.cf
%{buildroot}%{_sbindir}/postconf -c %{buildroot}%{_sysconfdir}/postfix \
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
install -m 644 postfix-SUSE/postfix-files %{buildroot}%{pf_shlib_directory}/postfix-files
# create paranoid permissions file
printf '%%-38s %%-18s %%s\n' %{_sbindir}/postdrop "root.%{pf_setgid_group}" "0755" >> %{buildroot}%{_sysconfdir}/permissions.d/postfix.paranoid
printf '%%-38s %%-18s %%s\n' %{_sbindir}/postqueue "root.%{pf_setgid_group}" "0755" >> %{buildroot}%{_sysconfdir}/permissions.d/postfix.paranoid
install -m 644 include/*.h %{buildroot}%{_includedir}/postfix/
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
rm -f %{buildroot}%{_sysconfdir}/postfix/*.orig
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{pf_shlib_directory}/systemd
install -m 0644 postfix-SUSE/postfix.service         %{buildroot}%{_unitdir}/postfix.service
install -m 0755 postfix-SUSE/config_postfix.systemd  %{buildroot}%{pf_shlib_directory}/systemd/config_postfix
install -m 0755 postfix-SUSE/update_chroot.systemd   %{buildroot}%{pf_shlib_directory}/systemd/update_chroot
install -m 0755 postfix-SUSE/update_postmaps.systemd %{buildroot}%{pf_shlib_directory}/systemd/update_postmaps
install -m 0755 postfix-SUSE/wait_qmgr.systemd       %{buildroot}%{pf_shlib_directory}/systemd/wait_qmgr
install -m 0755 postfix-SUSE/cond_slp.systemd        %{buildroot}%{pf_shlib_directory}/systemd/cond_slp
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rcpostfix
%fdupes %{buildroot}%{pf_docdir}
%fdupes %{buildroot}%{_mandir}
for path in %{buildroot}%{pf_shlib_directory}/libpostfix-*.so
do
  test -e "$path" || continue
  name=${path##*/}
  cmp "$path" %{buildroot}%{_libdir}/$name || continue
  rm -vf $path
  ln -sf %{_libdir}/$name $path
done
# ---------------------------------------------------------------------------
install -m 755 %{SOURCE11} %{buildroot}%{_sbindir}/
%if 0%{?suse_version} >= 1330
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE12} %{buildroot}%{_sysusersdir}/
install -m 644 %{SOURCE13} %{buildroot}%{_sysusersdir}/
%endif

#Clean up for postfix-bdb
rm -rf %{buildroot}/etc/postfix/ldap_aliases.cf
rm -rf %{buildroot}/usr/lib/debug/usr/lib/postfix/postfix-ldap.so-3.5.8-2.11.1.x86_64.debug
rm -rf %{buildroot}/usr/lib/debug/usr/lib/postfix/postfix-mysql.so-3.5.8-2.11.1.x86_64.debug
rm -rf %{buildroot}/usr/lib/debug/usr/lib/postfix/postfix-pgsql.so-3.5.8-2.11.1.x86_64.debug
rm -rf %{buildroot}/usr/lib/postfix/postfix-ldap.so
rm -rf %{buildroot}/usr/lib/postfix/postfix-mysql.so
rm -rf %{buildroot}/usr/lib/postfix/postfix-pgsql.so
rm -rf %{buildroot}/usr/lib/sysusers.d/postfix-vmail-user.conf
rm -rf %{buildroot}/usr/share/doc/packages/postfix-doc/
rm -rf %{buildroot}/%{_includedir}/postfix/

%if 0%{?suse_version} >= 1330
%pre -f postfix.pre
%else

%pre
getent group postfix >/dev/null || groupadd -g %{pf_gid} -o -r postfix
getent group maildrop >/dev/null || groupadd -g %{maildrop_gid} -o -r maildrop
getent passwd postfix >/dev/null || useradd -r -o -g postfix -u %{pf_uid} -s /bin/false -c "Postfix Daemon" -d /%{pf_queue_directory} postfix
usermod -a -G %{maildrop_gid},%{mail_group} postfix
%endif

%service_add_pre postfix.service

VERSIONTEST=$(test -x usr/sbin/postconf && usr/sbin/postconf proxy_read_maps 2>/dev/null || :)
if [ -z "$VERSIONTEST" -a -f %{pf_queue_directory}/pid/master.pid ]; then
  if checkproc -p %{pf_queue_directory}/pid/master.pid usr/lib/postfix/master; then
     echo "postfix is still running. You have to stop postfix in order to"
     echo "install a newer version."
     exit 1
  fi
fi
# ---------------------------------------------------------------------------

%preun
%stop_on_removal postfix
%service_del_preun postfix.service
# ---------------------------------------------------------------------------

%post
# We never have to run suseconfig for postfix after installation
# We only start postfix own upgrade-configuration by update
if [ ${1:-0} -gt 1 ]; then
	touch %{_localstatedir}/adm/postfix.configured
        echo "Executing upgrade-configuration."
        %{_sbindir}/postfix set-permissions upgrade-configuration setgid_group=%{pf_setgid_group} || :
        if [ "$(%{_sbindir}/postconf -h daemon_directory)" != "%{pf_daemon_directory}" ]; then
                %{_sbindir}/postconf daemon_directory=%{pf_daemon_directory}
        fi
fi

%service_add_post postfix.service

%set_permissions %{_sbindir}/postdrop
%set_permissions %{_sbindir}/postlog
%set_permissions %{_sbindir}/postqueue
%set_permissions %{_sysconfdir}/postfix/sasl_passwd
%set_permissions %{_sbindir}/sendmail

%{fillup_only postfix}
%{fillup_only -an mail}
/sbin/ldconfig

%verifyscript
%verify_permissions -e %{_sbindir}/postdrop
%verify_permissions -e %{_sbindir}/postlog
%verify_permissions -e %{_sbindir}/postqueue
%verify_permissions -e %{_sysconfdir}/postfix/sasl_passwd
%verify_permissions -e %{_sbindir}/sendmail

%postun
%service_del_postun postfix.service
/sbin/ldconfig

# ---------------------------------------------------------------------------

%files
%license LICENSE TLS_LICENSE
%doc RELEASE_NOTES
%config %{_sysconfdir}/pam.d/*
%{_fillupdir}/sysconfig.postfix
%{_fillupdir}/sysconfig.mail-postfix
%{_sbindir}/config.postfix
%dir %{_sysconfdir}/postfix
%config %{_sysconfdir}/postfix/main.cf.default
%config(noreplace) %{_sysconfdir}/postfix/[^mysql]*[^mysql]
%config(noreplace) %{_sysconfdir}/postfix/access
%config(noreplace) %{_sysconfdir}/postfix/aliases
%config(noreplace) %{_sysconfdir}/postfix/canonical
%config(noreplace) %{_sysconfdir}/postfix/header_checks
%config(noreplace) %{_sysconfdir}/postfix/helo_access
%config(noreplace) %{_sysconfdir}/postfix/main.cf
%config(noreplace) %{_sysconfdir}/postfix/master.cf
%attr(0750,root,root) %config %{_sysconfdir}/postfix/post-install
%attr(0750,root,root) %config %{_sysconfdir}/postfix/postfix-tls-script
%attr(0750,root,root) %config %{_sysconfdir}/postfix/postfix-wrapper
%attr(0750,root,root) %config %{_sysconfdir}/postfix/postmulti-script
%config(noreplace) %{_sysconfdir}/postfix/postfix-files
%config(noreplace) %{_sysconfdir}/postfix/relay
%config(noreplace) %{_sysconfdir}/postfix/relay_ccerts
%config(noreplace) %{_sysconfdir}/postfix/sasl_passwd
%config(noreplace) %{_sysconfdir}/postfix/sender_canonical
%config(noreplace) %{_sysconfdir}/postfix/virtual

%dir %{_sysconfdir}/sasl2
%config(noreplace) %{_sysconfdir}/sasl2/smtpd.conf
%config %{_sysconfdir}/postfix/LICENSE
%config %{_sysconfdir}/postfix/TLS_LICENSE
%config %{_sysconfdir}/permissions.d/postfix
%config %{_sysconfdir}/permissions.d/postfix.paranoid
%attr(0644, root, root) %config %{_sysconfdir}/postfix/makedefs.out
%{pf_shlib_directory}/postfix-files
# create our default postfix ssl DIR (/etc/postfix/ssl)
%dir %{_sysconfdir}/postfix/ssl
%dir %{_sysconfdir}/postfix/ssl/certs
%{_sysconfdir}/postfix/ssl/cacerts
%dir %{pf_shlib_directory}/systemd
%attr(0755,root,root) %{pf_shlib_directory}/systemd/*
%{_unitdir}/postfix.service
%verify(not mode) %attr(2755,root,%{pf_setgid_group}) %{_sbindir}/postdrop
%verify(not mode) %attr(2755,root,%{pf_setgid_group}) %{_sbindir}/postlog
%verify(not mode) %attr(2755,root,%{pf_setgid_group}) %{_sbindir}/postqueue
%{_bindir}/mailq
%{_bindir}/newaliases
%attr(0755,root,root) %{_sbindir}/sendmail
%attr(0755,root,root) %{_sbindir}/postalias
%attr(0755,root,root) %{_sbindir}/postcat
%attr(0755,root,root) %{_sbindir}/postconf
%attr(0755,root,root) %{_sbindir}/postfix
%attr(0755,root,root) %{_sbindir}/postkick
%attr(0755,root,root) %{_sbindir}/postlock
%attr(0755,root,root) %{_sbindir}/postmap
%attr(0755,root,root) %{_sbindir}/postmulti
%attr(0755,root,root) %{_sbindir}/postsuper
%attr(0755,root,root) %{_sbindir}/qshape
%attr(0755,root,root) %{_sbindir}/qmqp-source
%attr(0755,root,root) %{_sbindir}/smtp-sink
%attr(0755,root,root) %{_sbindir}/smtp-source
%attr(0755,root,root) %{_sbindir}/mkpostfixcert
%attr(0755,root,root) %{_sbindir}/check_mail_queue
%attr(0755,root,root) %{_sbindir}/config.postfix
%{_sbindir}/rcpostfix
%{_libdir}/lib*
%{_libexecdir}/sendmail
%dir %{pf_shlib_directory}
%{pf_shlib_directory}/*[^.so]
%{pf_shlib_directory}/postfix-pcre.so
%{pf_shlib_directory}/libpostfix-dns.so
%{pf_shlib_directory}/libpostfix-global.so
%{pf_shlib_directory}/libpostfix-master.so
%{pf_shlib_directory}/libpostfix-tls.so
%{pf_shlib_directory}/libpostfix-util.so
%{pf_shlib_directory}/main.cf.proto
%{pf_shlib_directory}/master.cf.proto

%{conf_backup_dir}
%dir %attr(0700,postfix,root) %{pf_data_directory}
%exclude %{_mandir}/man5/ldap_table.5*
%exclude %{_mandir}/man5/lmdb_table.5*
%exclude %{_mandir}/man5/mysql_table.5*
%exclude %{_mandir}/man5/pgsql_table.5*
%{_mandir}/man?/*%{?ext_man}
%dir %attr(0755,root,root) /%{pf_queue_directory}
%dir %attr(0755,root,root) /%{pf_queue_directory}/pid
%dir %attr(0700,postfix,root) /%{pf_queue_directory}/active
%dir %attr(0700,postfix,root) /%{pf_queue_directory}/bounce
%dir %attr(0700,postfix,root) /%{pf_queue_directory}/corrupt
%dir %attr(0700,postfix,root) /%{pf_queue_directory}/defer
%dir %attr(0700,postfix,root) /%{pf_queue_directory}/deferred
%dir %attr(0700,postfix,root) /%{pf_queue_directory}/flush
%dir %attr(0700,postfix,root) /%{pf_queue_directory}/hold
%dir %attr(0700,postfix,root) /%{pf_queue_directory}/incoming
%dir %attr(0700,postfix,root) /%{pf_queue_directory}/private
%dir %attr(0700,postfix,root) /%{pf_queue_directory}/saved
%dir %attr(0700,postfix,root) /%{pf_queue_directory}/trace
%dir %attr(0730,postfix,maildrop) /%{pf_queue_directory}/maildrop
%dir %attr(0710,postfix,maildrop) /%{pf_queue_directory}/public
%if 0%{?suse_version} >= 1330
%{_sysusersdir}/postfix-user.conf
%endif
%dir %attr(1777,root,root) /var/spool/mail
/var/mail

%if %{with lmdb}
%files lmdb
%{pf_shlib_directory}/postfix-lmdb.so
%{_mandir}/man5/lmdb_table.5%{?ext_man}
%endif

%changelog
