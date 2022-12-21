#
# spec file for package dovecot23
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


%global _lto_cflags %{nil}

Name:           dovecot23
Version:        2.3.19.1
Release:        0
%define pkg_name dovecot
%define dovecot_version 2.3.19.1
%define dovecot_pigeonhole_version 0.5.19
%define dovecot_branch  2.3
%define dovecot_pigeonhole_source_dir %{pkg_name}-%{dovecot_branch}-pigeonhole-%{dovecot_pigeonhole_version}
%define dovecot_pigeonhole_docdir     %{_docdir}/%{pkg_name}/dovecot-pigeonhole
%define restart_flag /var/run/%{pkg_name}/%{pkg_name}-restart-after-rpm-install
%if 0%{?suse_version} > 1230
%bcond_without systemd
%bcond_with    textcat
%else
%bcond_with    systemd
%bcond_with    textcat
%endif
%bcond_without solr
%if 0%{?suse_version} > 1110
%bcond_without clucene
%bcond_without dcrypt_openssl
%bcond_without icu
%else
%bcond_with    clucene
%bcond_with    dcrypt_openssl
%bcond_with    icu
%endif
%bcond_without sqlite
%if 0%{?suse_version} >= 1110
%bcond_without lzma
%else
%bcond_with    lzma
%endif
%if 0%{?suse_version} >= 1320
%bcond_without argon
%bcond_without lz4
%else
%bcond_with    argon
%bcond_with    lz4
%endif
%if 0%{?suse_version} >= 1110
%bcond_without zstd
%else
%bcond_with    zstd
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
BuildRequires:  flex
BuildRequires:  libapparmor-devel
%if %{with icu}
BuildRequires:  libicu-devel
%endif
BuildRequires:  libtool
%if %{with lzma}
BuildRequires:  xz-devel
%endif
%if %{with lz4}
BuildRequires:  liblz4-devel
%endif
%if %{with zstd}
BuildRequires:  libzstd-devel
%endif
%if %{with argon}
BuildRequires:  libsodium-devel
%endif
%if 0%{?suse_version} >= 1520
BuildRequires:  libmysqlclient-devel
%else
BuildRequires:  mysql-devel
%endif
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel >= 1.0.1
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  tcpd-devel
BuildRequires:  zlib-devel
%if %{with sqlite}
BuildRequires:  sqlite-devel > 3
%endif
%if %{with clucene}
BuildRequires:  clucene-core-devel
BuildRequires:  gcc-c++
%endif
%if 0%{?sles_version} == 9
BuildRequires:  heimdal-devel
BuildRequires:  libcap
%else
BuildRequires:  krb5-devel
BuildRequires:  libcap-devel
%endif
%if 0%{?suse_version} > 1020
BuildRequires:  libbz2-devel
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  lua53-devel
%else
BuildRequires:  lua51-devel
%endif
%if %{with solr}
BuildRequires:  curl-devel
BuildRequires:  libexpat-devel
%endif
%if %{with textcat}
BuildRequires:  libexttextcat-devel
%endif
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%define has_systemd 1
%endif
PreReq:         %fillup_prereq
# bump requires on noarch package to the version which copies the files from /usr/share/dovecot/
Requires:       dovecot >= 2.3
Conflicts:      otherproviders(dovecot-implementation)
Provides:       dovecot-implementation = %{version}-%{release}
%if 0%{?suse_version} >= 1010
Recommends:     %{name}-backend-mysql = %{version}
Recommends:     %{name}-backend-pgsql = %{version}
%if %{with sqlite}
Recommends:     %{name}-backend-sqlite = %{version}
%endif
%endif
Recommends:     %{name}-fts = %{version}
Recommends:     %{name}-fts-squat = %{version}
URL:            https://www.dovecot.org
Source:         https://www.dovecot.org/releases/%{dovecot_branch}/%{pkg_name}-%{dovecot_version}.tar.gz
Source1:        https://pigeonhole.dovecot.org/releases/%{dovecot_branch}/%{dovecot_pigeonhole_source_dir}.tar.gz
Source2:        dovecot-rpmlintrc
Source3:        dovecot-2.0.configfiles
Source4:        dovecot-2.1.configfiles
Source5:        dovecot-2.2.configfiles
Source6:        dovecot-2.3.configfiles
Source7:        dovecot-2.1-pigeonhole.configfiles
Source8:        dovecot-2.2-pigeonhole.configfiles
Source9:        dovecot-2.3-pigeonhole.configfiles
Source10:       https://www.dovecot.org/releases/%{dovecot_branch}/%{pkg_name}-%{dovecot_version}.tar.gz.sig
Source11:       https://pigeonhole.dovecot.org/releases/%{dovecot_branch}/%{dovecot_pigeonhole_source_dir}.tar.gz.sig
Source12:       dovecot23.keyring
Patch:          dovecot-2.3.0-dont_use_etc_ssl_certs.patch
Patch1:         dovecot-2.3.0-better_ssl_defaults.patch
Patch2:         dovecot-2.3.19-fix-doveadm-sync-special-folders.patch
Summary:        IMAP and POP3 Server Written Primarily with Security in Mind
License:        BSD-3-Clause AND LGPL-2.1-or-later AND MIT
Group:          Productivity/Networking/Email/Servers

%description
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

%package backend-mysql
Requires:       %{name} = %{version}
Provides:       dovecot-backend-mysql = %{version}-%{release}
Provides:       dovecot_sql_backend = %{version}-%{release}
Conflicts:      otherproviders(dovecot-backend-mysql)
Summary:        MySQL support for Dovecot
Group:          Productivity/Networking/Email/Servers

%description backend-mysql
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

This package holds the files needed for MySQL support.

%package backend-pgsql
Requires:       %{name} = %{version}
Provides:       dovecot-backend-pgsql = %{version}-%{release}
Provides:       dovecot_sql_backend = %{version}-%{release}
Conflicts:      otherproviders(dovecot-backend-pgsql)
Summary:        PostgreSQL support for Dovecot
Group:          Productivity/Networking/Email/Servers

%description backend-pgsql
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

This package holds the files needed for PostgreSQL support.

%if %{with sqlite}

%package backend-sqlite
Requires:       %{name} = %{version}
Provides:       dovecot-backend-sqlite = %{version}-%{release}
Provides:       dovecot_sql_backend = %{version}-%{release}
Conflicts:      otherproviders(dovecot-backend-sqlite)
Summary:        SQLite support for Dovecot
Group:          Productivity/Networking/Email/Servers

%description backend-sqlite
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

This package holds the files needed for SQLite support.

%endif

%package fts
Requires:       %{name} = %{version}
Summary:        Fulltext search support base plugin
Group:          Productivity/Networking/Email/Servers

%description fts
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

This package holds the base plugin needed for fulltext search support

%package fts-squat
Requires:       %{name} = %{version}
Requires:       %{name}-fts = %{version}
Summary:        Fulltext search support squat plugin
Group:          Productivity/Networking/Email/Servers

%description fts-squat
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

This package holds the files needed for fulltext search support squat plugin.


%if %{with clucene}

%package fts-lucene
Requires:       %{name} = %{version}
Requires:       %{name}-fts = %{version}
Provides:       dovecot-fts-clucene = %{version}-%{release}
Provides:       dovecot_fts_backend = %{version}-%{release}
Conflicts:      otherproviders(dovecot-fts-clucene)
Summary:        Fulltext search support via CLucene
Group:          Productivity/Networking/Email/Servers

%description fts-lucene
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

This package holds the files needed for fulltext search support via CLucene.

%endif

%if %{with solr}

%package fts-solr
Requires:       %{name} = %{version}
Requires:       %{name}-fts = %{version}
Provides:       dovecot-fts-solr = %{version}-%{release}
Provides:       dovecot_fts_backend = %{version}-%{release}
Conflicts:      otherproviders(dovecot-fts-solr)
Summary:        Fulltext search support via solr
Group:          Productivity/Networking/Email/Servers

%description fts-solr
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

This package holds the files needed for fulltext search support via solr.

%endif

%package devel
Requires:       %{name} = %{version}
Provides:       dovecot-devel = %{version}-%{release}
Conflicts:      otherproviders(dovecot-devel)
Summary:        Development files for Dovecot plugins
Group:          Development/Libraries/C and C++

%description devel
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

This package holds the file needed to compile plugins outside of the
dovecot tree.

%prep
%autosetup -p1 -n %{pkg_name}-%{dovecot_version} -a 1

gzip -9v ChangeLog
# Fix plugins dir.
sed -i 's|#mail_plugin_dir = /usr/lib/dovecot|mail_plugin_dir = %{_libdir}/dovecot/modules|' doc/example-config/conf.d/10-mail.conf

%build
export CFLAGS="%{optflags}"
%if %{with clucene}
export CFLAGS="$CFLAGS -I%{_libdir}"
export CXXFLAGS="$CFLAGS -I%{_libdir}"
%endif
export CFLAGS="$CFLAGS -fpic -DPIC"
export LIBS="-pie"
%configure                                          \
    --docdir=%{_docdir}/%{pkg_name}                 \
    --with-moduledir=%{_libdir}/%{pkg_name}/modules \
    --libexecdir=%{_prefix}/lib/                    \
    --with-ioloop=best                              \
    --with-ldap=plugin                              \
    --with-sql=plugin                               \
    --with-gssapi=plugin                            \
    --with-pgsql                                    \
    --with-mysql                                    \
    --with-lua=plugin                               \
    --with-apparmor                                 \
%if %{with sqlite}
    --with-sqlite                                   \
%endif
%if %{with clucene}
    --with-lucene                                   \
%endif
%if %{with textcat}
    --with-textcat                                  \
%endif
%if %{with icu}
    --with-icu                                      \
%endif
%if %{with solr}
    --with-solr                                     \
%endif
    --with-ssl=openssl                              \
    --with-zlib                                     \
    --with-bzlib                                    \
%if %{with lzma}
    --with-lzma                                     \
%endif
%if %{with lz4}
    --with-lz4                                      \
%endif
%if %{with zstd}
    --with-zstd                                     \
%endif
    --with-libcap                                   \
    --with-libwrap                                  \
    --with-docs                                     \
%if %{with systemd}
    --with-systemdsystemunitdir=%{_unitdir}         \
%endif
    --disable-static
make %{?_smp_mflags}

pushd %{dovecot_pigeonhole_source_dir}
    %configure --with-dovecot=../ \
      --with-ldap=plugin \
      --docdir="%{dovecot_pigeonhole_docdir}"
    make %{?_smp_mflags}
popd

%check
make check
make -C %{dovecot_pigeonhole_source_dir} test

%install
%makeinstall
%makeinstall -C %{dovecot_pigeonhole_source_dir} sieve_docdir=%{dovecot_pigeonhole_docdir}

# clean up unused files, as much as I would like to use -delete ... the old find on sles9 doesnt support it
find %{buildroot}%{_libdir}/%{pkg_name}/ -type f \
	'(' -name \*.la -o -name \*.a ')' -print -delete

# create /var directories
install -m 0755 -Dd \
  %{buildroot}%{_var}/run/%{pkg_name}/login/ \
  %{buildroot}%{_var}/lib/%{pkg_name}/

# install the script to create dummy selfsigned certs
pushd %{buildroot}%{_docdir}/%{pkg_name}/
mv -v {*.cnf,mkcert.sh,example-config} ../../../%{pkg_name}/
install -m 755 -d example-config/conf.d/
ln -sv ../../../%{pkg_name}/{*.cnf,mkcert.sh} .
cd example-config/
ln -sv \
    ../../../../%{pkg_name}/example-config/*conf \
    ../../../../%{pkg_name}/example-config/*ext  \
  .
cd conf.d/
ln -sv \
    ../../../../../%{pkg_name}/example-config/conf.d/* \
  .
popd

# additional docs for the main package
install -m 0644 \
       AUTHORS ChangeLog* COPYING* NEWS TODO README* \
%if %{with solr}
    doc/*.xml \
%endif
    %{buildroot}%{_docdir}/%{pkg_name}/

# install sieve docs
install -m 0755 -Dd %{buildroot}%{dovecot_pigeonhole_docdir}
pushd %{dovecot_pigeonhole_source_dir}
sed -i 's/\r$//' doc/rfc/*
cp -av AUTHORS COPYING* INSTALL NEWS README TODO \
       examples/ doc/rfc/ doc/devel \
  %{buildroot}%{dovecot_pigeonhole_docdir}/
  rm %{buildroot}%{dovecot_pigeonhole_docdir}/rfc/Makefile*
popd

for i in $RPM_SOURCE_DIR/*.configfiles ; do
  echo "Creating ghost files for '$i'"
  for j in $(<$i) ; do
    install -D -m 0644 /dev/null %{buildroot}$j
  done
done

# clean up of things that are now in the unversioned package.
%if %{with systemd}
rm %{buildroot}%{_unitdir}/dovecot.{service,socket}
%endif
rm %{buildroot}%{_sysconfdir}/%{pkg_name}/README

%pre
# do not let dovecot run during upgrade rhbz#134325
if [ "$1" -ge "1" ]; then
  rm -f %restart_flag
  %if %{with systemd}
    # we get installed before the unversioned dovecot package is installed
    # in that case we dont need to restart as there was no file to start us before
    if [ -x /bin/systemctl -a -e %{_unitdir}/%{pkg_name}.service ] ; then
      /bin/systemctl is-active %{pkg_name}.service >/dev/null 2>&1 && touch %restart_flag ||:
      /bin/systemctl stop      %{pkg_name}.service >/dev/null 2>&1
    fi
  %else
    # we get installed before the unversioned dovecot package is installed
    # in that case we dont need to restart as there was no file to start us before
    if [ -x /etc/init.d/%{pkg_name} ] ; then
      /etc/init.d/%{pkg_name} status >/dev/null 2>&1 && touch %restart_flag ||:
      /etc/init.d/%{pkg_name} stop >/dev/null 2>&1
    fi
  %endif
fi
# remove !SSLv2 from ssl_protocols (no longer supported in openssl-1.1.0)
if grep -s -q "ssl_protocols .*!SSLv2" /etc/dovecot/conf.d/10-ssl.conf; then
  sed -i 's/^\(ssl_protocols.*\)[[:blank:]]!SSLv2\(.*\)$/\1\2/g' /etc/dovecot/conf.d/10-ssl.conf
fi

%post -p /sbin/ldconfig

%postun
/sbin/ldconfig
# do not let dovecot run during upgrade rhbz#134325
if [ "$1" -ge "1" -a -e %restart_flag ]; then
  %if %{with systemd}
    # we get installed before the unversioned dovecot package is installed
    # in that case we dont need to restart as there was no file to start us before
    if [ -x /bin/systemctl -a -e %{_unitdir}/%{pkg_name}.service ] ; then
      /bin/systemctl start %{pkg_name}.service >/dev/null 2>&1 || :
    fi
  %else
    # we get installed before the unversioned dovecot package is installed
    # in that case we dont need to restart as there was no file to start us before
    if [ -x /etc/init.d/%{pkg_name} ] ; then
      /etc/init.d/%{pkg_name} start >/dev/null 2>&1 || :
    fi
  %endif
  rm -f %restart_flag
fi

# do not let dovecot run during upgrade rhbz#134325
# dovecot should be started again in %%postun, but it's not executed on reinstall
# if it was already started, restart_flag won't be here, so it's ok to test it again
%posttrans
if [ -e %restart_flag ]; then
  %if %{with systemd}
    # we get installed before the unversioned dovecot package is installed
    # in that case we dont need to restart as there was no file to start us before
    if [ -x /bin/systemctl -a -e %{_unitdir}/%{pkg_name}.service ] ; then
      /bin/systemctl start %{pkg_name}.service >/dev/null 2>&1 || :
    fi
  %else
    # we get installed before the unversioned dovecot package is installed
    # in that case we dont need to restart as there was no file to start us before
    if [ -x /etc/init.d/%{pkg_name} ] ; then
      /etc/init.d/%{pkg_name} start >/dev/null 2>&1 || :
    fi
  %endif
  rm -f %restart_flag
fi

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/%{pkg_name}/
%ghost %config(noreplace) /etc/dovecot/*
%{_sbindir}/%{pkg_name}
%{_bindir}/doveadm
%{_bindir}/doveconf
%{_bindir}/dovecot-sysreport
%{_bindir}/dsync
%{_bindir}/sieve-test
%{_bindir}/sievec
%{_bindir}/sieve-dump
%{_bindir}/sieve-filter
# subprocesses
%dir %{_prefix}/lib/%{pkg_name}
%{_prefix}/lib/%{pkg_name}/aggregator
%{_prefix}/lib/%{pkg_name}/anvil
%{_prefix}/lib/%{pkg_name}/auth
%{_prefix}/lib/%{pkg_name}/checkpassword-reply
%{_prefix}/lib/%{pkg_name}/config
%{_prefix}/lib/%{pkg_name}/decode2text.sh
%{_prefix}/lib/%{pkg_name}/deliver
%{_prefix}/lib/%{pkg_name}/dict
%{_prefix}/lib/%{pkg_name}/director
%{_prefix}/lib/%{pkg_name}/dns-client
%{_prefix}/lib/%{pkg_name}/doveadm-server
%{_prefix}/lib/%{pkg_name}/dovecot-lda
%{_prefix}/lib/%{pkg_name}/gdbhelper
%{_prefix}/lib/%{pkg_name}/health-check.sh
%{_prefix}/lib/%{pkg_name}/imap
%{_prefix}/lib/%{pkg_name}/imap-hibernate
%{_prefix}/lib/%{pkg_name}/imap-login
%{_prefix}/lib/%{pkg_name}/imap-urlauth
%{_prefix}/lib/%{pkg_name}/imap-urlauth-login
%{_prefix}/lib/%{pkg_name}/imap-urlauth-worker
%{_prefix}/lib/%{pkg_name}/indexer
%{_prefix}/lib/%{pkg_name}/indexer-worker
%{_prefix}/lib/%{pkg_name}/ipc
%{_prefix}/lib/%{pkg_name}/lmtp
%{_prefix}/lib/%{pkg_name}/log
%{_prefix}/lib/%{pkg_name}/maildirlock
%{_prefix}/lib/%{pkg_name}/managesieve
%{_prefix}/lib/%{pkg_name}/managesieve-login
%{_prefix}/lib/%{pkg_name}/old-stats
%{_prefix}/lib/%{pkg_name}/pop3
%{_prefix}/lib/%{pkg_name}/pop3-login
%{_prefix}/lib/%{pkg_name}/quota-status
%{_prefix}/lib/%{pkg_name}/rawlog
%{_prefix}/lib/%{pkg_name}/replicator
%{_prefix}/lib/%{pkg_name}/script
%{_prefix}/lib/%{pkg_name}/script-login
%{_prefix}/lib/%{pkg_name}/stats
%{_prefix}/lib/%{pkg_name}/submission
%{_prefix}/lib/%{pkg_name}/submission-login
%{_prefix}/lib/%{pkg_name}/tcpwrap
%{_prefix}/lib/%{pkg_name}/xml2text
%{_libdir}/%{pkg_name}/libdovecot.so.*
%{_libdir}/%{pkg_name}/libdovecot-compression.so.*
%{_libdir}/%{pkg_name}/libdovecot-dsync.so.*
%{_libdir}/%{pkg_name}/libdovecot-fts.so.*
%{_libdir}/%{pkg_name}/libdovecot-lda.so.*
%{_libdir}/%{pkg_name}/libdovecot-ldap.so.*
%{_libdir}/%{pkg_name}/libdovecot-login.so.*
%{_libdir}/%{pkg_name}/libdovecot-lua.so.*
%{_libdir}/%{pkg_name}/libdovecot-sieve.so.*
%{_libdir}/%{pkg_name}/libdovecot-sql.so.*
%{_libdir}/%{pkg_name}/libdovecot-storage.so.*
%{_libdir}/%{pkg_name}/libdovecot-storage-lua.so.*
%if %{with dcrypt_openssl}
%{_libdir}/%{pkg_name}/libdcrypt_openssl.so
%endif
# plugins
%dir %{_libdir}/%{pkg_name}
%dir %{_libdir}/%{pkg_name}/modules/
%{_libdir}/%{pkg_name}/modules/lib01_acl_plugin.so
%{_libdir}/%{pkg_name}/modules/lib01_apparmor_plugin.so
%{_libdir}/%{pkg_name}/modules/lib02_lazy_expunge_plugin.so
%{_libdir}/%{pkg_name}/modules/lib05_mail_crypt_acl_plugin.so
%{_libdir}/%{pkg_name}/modules/lib05_pop3_migration_plugin.so
%{_libdir}/%{pkg_name}/modules/lib10_last_login_plugin.so
%{_libdir}/%{pkg_name}/modules/lib01_mail_lua_plugin.so
%{_libdir}/%{pkg_name}/modules/lib10_mail_crypt_plugin.so
%{_libdir}/%{pkg_name}/modules/lib10_quota_plugin.so
%{_libdir}/%{pkg_name}/modules/lib11_trash_plugin.so
%{_libdir}/%{pkg_name}/modules/lib15_notify_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_mail_log_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_mailbox_alias_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_notify_status_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_charset_alias_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_var_expand_crypt.so
%{_libdir}/%{pkg_name}/modules/lib20_zlib_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_push_notification_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_listescape_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_quota_clone_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_replication_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_virtual_plugin.so
%{_libdir}/%{pkg_name}/modules/lib22_push_notification_lua_plugin.so
%{_libdir}/%{pkg_name}/modules/lib30_imap_zlib_plugin.so
%{_libdir}/%{pkg_name}/modules/lib02_imap_acl_plugin.so
%{_libdir}/%{pkg_name}/modules/lib11_imap_quota_plugin.so
%{_libdir}/%{pkg_name}/modules/lib90_sieve_plugin.so
%{_libdir}/%{pkg_name}/modules/lib90_old_stats_plugin.so
%{_libdir}/%{pkg_name}/modules/lib95_imap_sieve_plugin.so
%{_libdir}/%{pkg_name}/modules/lib95_imap_filter_sieve_plugin.so
%{_libdir}/%{pkg_name}/modules/lib95_imap_old_stats_plugin.so
%{_libdir}/%{pkg_name}/modules/lib99_welcome_plugin.so
%{_libdir}/%{pkg_name}/modules/libfs_compress.so
%{_libdir}/%{pkg_name}/modules/libfs_crypt.so
%{_libdir}/%{pkg_name}/modules/libfs_mail_crypt.so
%{_libdir}/%{pkg_name}/modules/libssl_iostream_openssl.so

#
%dir %{_libdir}/%{pkg_name}/modules/auth/
%{_libdir}/%{pkg_name}/modules/auth/libauthdb_imap.so
%{_libdir}/%{pkg_name}/modules/auth/libauthdb_ldap.so
%{_libdir}/%{pkg_name}/modules/auth/libauthdb_lua.so
%{_libdir}/%{pkg_name}/modules/auth/libmech_gssapi.so
%{_libdir}/%{pkg_name}/modules/auth/lib20_auth_var_expand_crypt.so
%dir %{_libdir}/%{pkg_name}/modules/dict/
%{_libdir}/%{pkg_name}/modules/dict/libdict_ldap.so
# more dict modules are in the sql packages
#
%dir %{_libdir}/%{pkg_name}/modules/doveadm
%{_libdir}/%{pkg_name}/modules/doveadm/libdoveadm_mail_crypt_plugin.so
%{_libdir}/%{pkg_name}/modules/doveadm/lib10_doveadm_acl_plugin.so
%{_libdir}/%{pkg_name}/modules/doveadm/lib10_doveadm_quota_plugin.so*
%{_libdir}/%{pkg_name}/modules/doveadm/lib10_doveadm_sieve_plugin.so
#
%dir %{_libdir}/%{pkg_name}/modules/settings/
%{_libdir}/%{pkg_name}/modules/settings/libpigeonhole_settings.so
%{_libdir}/%{pkg_name}/modules/settings/libmanagesieve_login_settings.so
%{_libdir}/%{pkg_name}/modules/settings/libmanagesieve_settings.so
#
%dir %{_libdir}/%{pkg_name}/modules/sieve
%{_libdir}/%{pkg_name}/modules/sieve/lib10_sieve_storage_ldap_plugin.so
%{_libdir}/%{pkg_name}/modules/sieve/lib90_sieve_extprograms_plugin.so
%{_libdir}/%{pkg_name}/modules/sieve/lib90_sieve_imapsieve_plugin.so
#
%dir %{_libdir}/%{pkg_name}/modules/old-stats/
%{_libdir}/%{pkg_name}/modules/old-stats/libstats_auth.so
%{_libdir}/%{pkg_name}/modules/old-stats/libold_stats_mail.so
#
%dir %{_datadir}/%{pkg_name}/
%{_datadir}/%{pkg_name}/*.cnf
%{_datadir}/%{pkg_name}/mkcert.sh
%{_datadir}/%{pkg_name}/example-config
# doc
%{_mandir}/man1/deliver.1*
%{_mandir}/man1/doveadm*.1*
%{_mandir}/man1/doveconf.1*
%{_mandir}/man1/dovecot*.1*
%{_mandir}/man1/dsync.1*
%{_mandir}/man1/sieve-dump.1*
%{_mandir}/man1/sieve-filter.1*
%{_mandir}/man1/sieve-test.1*
%{_mandir}/man1/sievec.1*
%{_mandir}/man1/sieved.1*
%{_mandir}/man7/doveadm*.7*
%{_mandir}/man7/pigeonhole.7*
%doc %{_docdir}/%{pkg_name}
%if %{with solr}
%exclude %{_docdir}/%{pkg_name}/solr-schema.xml
%endif
# setting up permissions
%if ! %{with systemd}
%dir %attr(0755,root,root)        %ghost %{_var}/run/%{pkg_name}/
%dir %attr(0750,root,%{pkg_name}) %ghost %{_var}/run/%{pkg_name}/login/
%endif
%dir %attr(0750,root,root)        %{_var}/lib/%{pkg_name}/

%files fts
%defattr(-,root,root,-)
%{_libdir}/%{pkg_name}/modules/doveadm/lib20_doveadm_fts_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_fts_plugin.so
%{_datadir}/%{pkg_name}/stopwords/

%files fts-squat
%defattr(-,root,root,-)
%{_libdir}/%{pkg_name}/modules/lib21_fts_squat_plugin.so

%files backend-mysql
%defattr(-,root,root,-)
%{_libdir}/%{pkg_name}/modules/libdriver_mysql.so
%{_libdir}/%{pkg_name}/modules/auth/libdriver_mysql.so
%{_libdir}/%{pkg_name}/modules/dict/libdriver_mysql.so

%files backend-pgsql
%defattr(-,root,root,-)
%{_libdir}/%{pkg_name}/modules/libdriver_pgsql.so
%{_libdir}/%{pkg_name}/modules/auth/libdriver_pgsql.so
%{_libdir}/%{pkg_name}/modules/dict/libdriver_pgsql.so

%if %{with sqlite}
%files backend-sqlite
%defattr(-,root,root,-)
%{_libdir}/%{pkg_name}/modules/libdriver_sqlite.so
%{_libdir}/%{pkg_name}/modules/auth/libdriver_sqlite.so
%{_libdir}/%{pkg_name}/modules/dict/libdriver_sqlite.so
%endif

%if %{with clucene}
%files fts-lucene
%defattr(-,root,root,-)
%{_libdir}/%{pkg_name}/modules/lib21_fts_lucene_plugin.so
%{_libdir}/%{pkg_name}/modules/doveadm/lib20_doveadm_fts_lucene_plugin.so
%endif

%if %{with solr}
%files fts-solr
%defattr(-,root,root,-)
%{_libdir}/%{pkg_name}/modules/lib21_fts_solr_plugin.so
%{_docdir}/%{pkg_name}/solr-schema.xml
%endif

%files devel
%defattr(-,root,root,-)
%{_datadir}/aclocal/%{pkg_name}.m4
%{_datadir}/aclocal/dovecot-pigeonhole.m4
%{_includedir}/%{pkg_name}/
%{_libdir}/%{pkg_name}/dovecot-config
%{_libdir}/%{pkg_name}/libdovecot.so
%{_libdir}/%{pkg_name}/libdovecot-compression.so
%{_libdir}/%{pkg_name}/libdovecot-dsync.so
%{_libdir}/%{pkg_name}/libdovecot-fts.so
%{_libdir}/%{pkg_name}/libdovecot-lda.so
%{_libdir}/%{pkg_name}/libdovecot-ldap.so
%{_libdir}/%{pkg_name}/libdovecot-login.so
%{_libdir}/%{pkg_name}/libdovecot-lua.so
%{_libdir}/%{pkg_name}/libdovecot-sieve.so
%{_libdir}/%{pkg_name}/libdovecot-sql.so
%{_libdir}/%{pkg_name}/libdovecot-storage.so
%{_libdir}/%{pkg_name}/libdovecot-storage-lua.so

%changelog
