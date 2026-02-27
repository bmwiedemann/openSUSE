#
# spec file for package postfix
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%define pf_meta_directory    %{_prefix}/lib/%{name}
%define pf_systemd_directory %{_prefix}/lib/%{name}/systemd
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
%define mail_group           mail
%define unitdir %{_prefix}/lib/systemd
%if 0%{?suse_version} < 1599
%bcond_without libnsl
%else
%bcond_with libnsl
%endif
%bcond_without ldap
Name:           postfix
Version:        3.10.8
Release:        0
Summary:        A fast, secure, and flexible mailer
License:        EPL-2.0 OR IPL-1.0
Group:          Productivity/Networking/Email/Servers
URL:            https://www.postfix.org/
Source0:        http://ftp.porcupine.org/mirrors/postfix-release/official/postfix-%{version}.tar.gz
Source1:        http://ftp.porcupine.org/mirrors/postfix-release/official/postfix-%{version}.tar.gz.gpg2#/postfix-%{version}.tar.gz.asc
Source2:        %{name}-SUSE.tar.gz
Source3:        %{name}-mysql.tar.bz2
Source4:        postfix.keyring
Source10:       postfix-rpmlintrc
Source11:       check_mail_queue
Source12:       postfix-user.conf
Source13:       postfix-vmail-user.conf
Source14:       tmpfiles.conf
Patch1:         %{name}-no-md5.patch
Patch2:         pointer_to_literals.patch
Patch3:         ipv6_disabled.patch
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
%if 0%{?suse_version} >= 1600
BuildRequires:  pam-devel
%endif
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  shadow
BuildRequires:  sysuser-tools
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(systemd)
Requires:       iproute2
Requires(post): permissions

Requires(pre):  group(%{mail_group})
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
# /usr/lib/postfix/bin//postfix-script: line 400: cmp: command not found
Requires:       /usr/bin/cmp
# /usr/lib/postfix/bin//post-install: line 667: ed: command not found
Requires(pre):  /usr/bin/ed
Requires(preun): /usr/bin/ed
Requires(post): /usr/bin/ed
Requires(postun): /usr/bin/ed

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
cp lib/lib%{name}-*  %{buildroot}/%{_libdir}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}/%{_libdir}
sh postfix-install -non-interactive \
       install_root=%{buildroot} \
       shlib_directory=%{_prefix}/lib/%{name} \
       meta_directory=%{_prefix}/lib/%{name} \
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
mkdir -p %{buildroot}/%{pf_sample_directory}
mkdir -p %{buildroot}/%{pf_html_directory}
mkdir -p %{buildroot}%{_includedir}/%{name}
%if 0%{?suse_version} >= 1600
    mkdir -p %{buildroot}%{_pam_vendordir}
    install -pm 0644 %{name}-SUSE/smtp %{buildroot}%{_pam_vendordir}/smtp
%else
    mkdir -p %{buildroot}%{_sysconfdir}/pam.d
    install -pm 0644 %{name}-SUSE/smtp %{buildroot}%{_sysconfdir}/pam.d/smtp
%endif
mkdir -p %{buildroot}/%{pf_queue_directory}
mkdir -p %{buildroot}%{_sysconfdir}/sasl2
install -pm 0600 %{name}-SUSE/smtpd.conf %{buildroot}%{_sysconfdir}/sasl2/smtpd.conf
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
install -pm 0644 %{name}-SUSE/permissions %{buildroot}%{_sysconfdir}/permissions.d/%{name}
install -pm 0644 %{name}-SUSE/permissions.paranoid %{buildroot}%{_sysconfdir}/permissions.d/%{name}.paranoid
sed -i	-e 's/\(.*ldap.*\)/#\1/g' \
	-e 's/\(.*mysql.*\)/#\1/g' \
	-e 's/\(.*pgsql.*\)/#\1/g' \
	-e 's/\(.*LICENSE.*\)/#\1/g' \
	-e '/html_directory/d' \
	-e '/manpage_directory/d' \
	-e '/readme_directory/d' \
	%{buildroot}%{pf_meta_directory}/postfix-files
mkdir -p %{buildroot}%{pf_meta_directory}/postfix-files.d
# postfix-mysql
install -pm 0644 %{name}-mysql/main.cf-mysql %{buildroot}%{_sysconfdir}/%{name}/main.cf-mysql
install -pm 0640 %{name}-mysql/*_maps.cf     %{buildroot}%{_sysconfdir}/%{name}/
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
mkdir -p %{buildroot}%{pf_systemd_directory}
install -pm 0644 %{name}-SUSE/%{name}.service         %{buildroot}%{_unitdir}/%{name}.service
install -pm 0755 %{name}-SUSE/wait_qmgr.systemd       %{buildroot}%{pf_systemd_directory}/wait_qmgr
%if 0%{?suse_version} < 1599
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%endif
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
sed -n -e '/^#/p' -e '/mysql/p' %{buildroot}%{pf_meta_directory}/dynamicmaps.cf > %{buildroot}%{pf_meta_directory}/dynamicmaps.cf.d/%{name}-mysql.cf
sed -i -e '/mysql/d' %{buildroot}%{pf_meta_directory}/dynamicmaps.cf
sed -n -e '/^#/p' -e '/pgsql/p' %{buildroot}%{pf_meta_directory}/dynamicmaps.cf > %{buildroot}%{pf_meta_directory}/dynamicmaps.cf.d/%{name}-pgsql.cf
sed -i -e '/pgsql/d' %{buildroot}%{pf_meta_directory}/dynamicmaps.cf
%if %{with ldap}
sed -n -e '/^#/p' -e "/ldap/p" %{buildroot}%{pf_meta_directory}/dynamicmaps.cf > %{buildroot}%{pf_meta_directory}/dynamicmaps.cf.d/%{name}-ldap.cf
sed -i -e '/ldap/d' %{buildroot}%{pf_meta_directory}/dynamicmaps.cf
%endif

install -m 755 %{SOURCE11} %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_sysusersdir}
mkdir -p %{buildroot}%{_tmpfilesdir}/
install -m 644 %{SOURCE12} %{buildroot}%{_sysusersdir}/
install -m 644 %{SOURCE13} %{buildroot}%{_sysusersdir}/
install -m 644 %{SOURCE14} %{buildroot}%{_tmpfilesdir}/postfix.conf
# posttls-finger is built but not installed
install -m 755 bin/posttls-finger %{buildroot}%{_sbindir}/

sed -i 's/hash:/lmdb:/g' %{buildroot}%{_sysconfdir}/%{name}/main.cf
# ---------------------------------------------------------------------------

%pre -f postfix.pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%tmpfiles_create %{_tmpfilesdir}/postfix.conf
%service_add_post %{name}.service
%set_permissions %{_sbindir}/postdrop
%set_permissions %{_sbindir}/postlog
%set_permissions %{_sbindir}/postqueue

%verifyscript
%verify_permissions -e %{_sbindir}/postdrop
%verify_permissions -e %{_sbindir}/postlog
%verify_permissions -e %{_sbindir}/postqueue

%postun
%service_del_postun %{name}.service

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
%exclude %{_sysconfdir}/%{name}/*mysql*
%exclude %{_sysconfdir}/%{name}/LICENSE
%exclude %{_sysconfdir}/%{name}/TLS_LICENSE
%exclude %{_mandir}/man5/ldap_table.5*
%exclude %{_mandir}/man5/mysql_table.5*
%exclude %{_mandir}/man5/pgsql_table.5*
%if 0%{?suse_version} >= 1600
%{_pam_vendordir}/smtp
%else
%config %{_sysconfdir}/pam.d/*
%endif
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%ghost %attr(0644,root,root) %{_sysconfdir}/%{name}/*.lmdb
%ghost %attr(0644,root,root) %{_sysconfdir}/aliases.lmdb
%dir %{_sysconfdir}/sasl2
%config(noreplace) %{_sysconfdir}/sasl2/smtpd.conf
%config %{_sysconfdir}/permissions.d/%{name}
%config %{_sysconfdir}/permissions.d/%{name}.paranoid
%{pf_meta_directory}/%{name}-files
%dir %{pf_systemd_directory}
%attr(0755,root,root) %{pf_systemd_directory}/*
%{_unitdir}/%{name}.service
%{_unitdir}/mail-transfer-agent.target.wants
%{_tmpfilesdir}/postfix.conf
%{_sysusersdir}/postfix-user.conf
%{_bindir}/mailq
%{_bindir}/newaliases
%verify(not mode) %attr(2755,root,%{pf_setgid_group}) %{_sbindir}/postdrop
%verify(not mode) %attr(2755,root,%{pf_setgid_group}) %{_sbindir}/postlog
%verify(not mode) %attr(2755,root,%{pf_setgid_group}) %{_sbindir}/postqueue
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
%attr(0755,root,root) %{_sbindir}/posttls-finger
%attr(0755,root,root) %{_sbindir}/qshape
%attr(0755,root,root) %{_sbindir}/qmqp-source
%attr(0755,root,root) %{_sbindir}/smtp-sink
%attr(0755,root,root) %{_sbindir}/smtp-source
%attr(0755,root,root) %{_sbindir}/check_mail_queue
%if 0%{?suse_version} < 1599
%{_sbindir}/rc%{name}
%endif
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
%{pf_meta_directory}/dynamicmaps.cf
%{pf_meta_directory}/main.cf.proto
%{pf_meta_directory}/makedefs.out
%{pf_meta_directory}/master.cf.proto
%dir %{pf_daemon_directory}
%{pf_daemon_directory}/*
%dir %{pf_meta_directory}/dynamicmaps.cf.d
%dir %{pf_meta_directory}/postfix-files.d
%ghost /var/lib/postfix
%ghost /var/spool/postfix
%ghost /var/mail
%ghost %dir /var/spool/mail

%{_mandir}/man?/*%{?ext_man}

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
%{pf_meta_directory}/dynamicmaps.cf.d/%{name}-mysql.cf
%{_mandir}/man5/mysql_table.5%{?ext_man}
%{_sysusersdir}/postfix-vmail-user.conf

%files postgresql
%{pf_shlib_directory}/%{name}-pgsql.so
%{pf_meta_directory}/dynamicmaps.cf.d/%{name}-pgsql.cf
%{_mandir}/man5/pgsql_table.5%{?ext_man}

%if %{with ldap}
%files ldap
%{pf_shlib_directory}/%{name}-ldap.so
%{pf_meta_directory}/dynamicmaps.cf.d/%{name}-ldap.cf
%{_mandir}/man5/ldap_table.5%{?ext_man}
%endif

%changelog
