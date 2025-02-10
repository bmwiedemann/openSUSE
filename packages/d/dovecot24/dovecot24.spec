#
# spec file for package dovecot24
#
# Copyright (c) 2025 SUSE LLC
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


%define pkg_name dovecot
%define dovecot_version 2.4.0
%define dovecot_pigeonhole_version 2.4.0
%define dovecot_branch  2.4
%define dovecot_pigeonhole_source_dir %{pkg_name}-pigeonhole-%{dovecot_pigeonhole_version}
%define dovecot_pigeonhole_docdir     %{_docdir}/%{pkg_name}/dovecot-pigeonhole
%define restart_flag %{_localstatedir}/run/%{pkg_name}/%{pkg_name}-restart-after-rpm-install

%bcond_without systemd
%bcond_without textcat
%bcond_without solr
%bcond_without dcrypt_openssl
%bcond_without icu
%bcond_without sqlite
%bcond_without lzma
%bcond_without argon
%bcond_without lz4
%bcond_without zstd
%bcond_without xapian
%bcond_without libstemmer
%bcond_without run_tests
%if %{is_opensuse}
%bcond_without apparmor
%else
%bcond_with apparmor
%endif

Name:           dovecot24
Version:        2.4.0
Release:        0
Summary:        IMAP and POP3 Server Written Primarily with Security in Mind
License:        BSD-3-Clause AND LGPL-2.1-or-later AND MIT
# https://dovecot.org/mailman3/archives/list/dovecot@dovecot.org/message/PCUTU3IE6RZXQQMWCAB7UP4XN6SPFPFX/
ExcludeArch:    %ix86 %arm
Group:          Productivity/Networking/Email/Servers
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
Source12:       dovecot24.keyring
Source13:       dovecot-2.4.configfiles
Source14:       dovecot-2.4-pigeonhole.configfiles
# PATCH-FIX-OPENSUSE - boo#932386
Patch0:         dovecot-2.3.0-dont_use_etc_ssl_certs.patch
# PATCH-FIX-OPENSUSE - use lua-dkjson instead of lua-json
Patch1:         dovecot-2.4.0-lua_json.patch
# PATCH-FIX-OPENSUSE
Patch2:         dovecot-2.3.17-env_script_interpreter.patch
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  lua-devel
BuildRequires:  lua-dkjson
BuildRequires:  pkgconfig
BuildRequires:  rpcgen
BuildRequires:  pkgconfig(krb5)
%if %{with apparmor}
BuildRequires:  pkgconfig(libapparmor)
%endif
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(openssl)
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(ldap) >= 2.6.8
BuildRequires:  pkgconfig(mysqlclient)
BuildRequires:  pkgconfig(pam)
%else
BuildRequires:  libmysqlclient-devel
BuildRequires:  openldap2-devel >= 2.6.8
BuildRequires:  pam-devel
%endif
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
%if %{with icu}
BuildRequires:  pkgconfig(icu-i18n)
%endif
%if %{with lzma}
BuildRequires:  pkgconfig(liblzma)
%endif
%if %{with lz4}
BuildRequires:  pkgconfig(liblz4)
%endif
%if %{with zstd}
BuildRequires:  pkgconfig(libzstd)
%endif
%if %{with argon}
BuildRequires:  pkgconfig(libsodium)
%endif
%if %{with libstemmer}
BuildRequires:  libstemmer-devel
%endif
%if %{with sqlite}
BuildRequires:  pkgconfig(sqlite3)
%endif
%if %{with xapian}
BuildRequires:  pkgconfig(xapian-core)
%endif
BuildRequires:  pkgconfig(bzip2)
%if %{with solr}
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libcurl)
%endif
%if %{with textcat}
BuildRequires:  pkgconfig(libexttextcat)
%endif
# bump requires on noarch package to the version which copies the files from /usr/share/%%{pkg_name}/
Requires:       dovecot >= 2.4
Recommends:     %{name}-fts = %{version}
Recommends:     %{name}-fts-flatcurve = %{version}
Conflicts:      dovecot-implementation
Provides:       dovecot-implementation = %{version}-%{release}
Recommends:     %{name}-backend-mysql = %{version}
Recommends:     %{name}-backend-pgsql = %{version}
Recommends:     %{name}-backend-sqlite = %{version}
%{?systemd_ordering}

%description
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

%package backend-mysql
Summary:        MySQL support for Dovecot
Group:          Productivity/Networking/Email/Servers
Requires:       %{name} = %{version}
Conflicts:      dovecot-backend-mysql
Provides:       dovecot-backend-mysql = %{version}-%{release}
Provides:       dovecot_sql_backend = %{version}-%{release}

%description backend-mysql
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

This package holds the files needed for MySQL support.

%package backend-pgsql
Summary:        PostgreSQL support for Dovecot
Group:          Productivity/Networking/Email/Servers
Requires:       %{name} = %{version}
Conflicts:      dovecot-backend-pgsql
Provides:       dovecot-backend-pgsql = %{version}-%{release}
Provides:       dovecot_sql_backend = %{version}-%{release}

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
Summary:        SQLite support for Dovecot
Group:          Productivity/Networking/Email/Servers
Requires:       %{name} = %{version}
Conflicts:      dovecot-backend-sqlite
Provides:       dovecot-backend-sqlite = %{version}-%{release}
Provides:       dovecot_sql_backend = %{version}-%{release}

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
Summary:        Fulltext search support base plugin
Group:          Productivity/Networking/Email/Servers
Requires:       %{name} = %{version}

%description fts
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

This package holds the base plugin needed for fulltext search support

%if %{with xapian}
%package fts-flatcurve
Summary:        Fulltext search support flatcurve plugin
Group:          Productivity/Networking/Email/Servers
Requires:       %{name} = %{version}
Requires:       %{name}-fts = %{version}
Conflicts:      dovecot-fts-flatcurve
Provides:       dovecot-fts-flatcurve = %{version}-%{release}
Provides:       dovecot_fts_backend = %{version}-%{release}

%description fts-flatcurve
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

This package holds the files needed for fulltext search support squat plugin.

%endif

%if %{with solr}
%package fts-solr
Summary:        Fulltext search support via solr
Group:          Productivity/Networking/Email/Servers
Requires:       %{name} = %{version}
Requires:       %{name}-fts = %{version}
Conflicts:      dovecot-fts-solr
Provides:       dovecot-fts-solr = %{version}-%{release}
Provides:       dovecot_fts_backend = %{version}-%{release}

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
Summary:        Development files for Dovecot plugins
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Conflicts:      dovecot-devel
Provides:       dovecot-devel = %{version}-%{release}

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

%build
# export CFLAGS="%%{optflags} -Wno-sign-compare"
%configure                                          \
    --docdir=%{_docdir}/%{pkg_name}                 \
    --with-moduledir=%{_libdir}/%{pkg_name}/modules \
    --libexecdir=%{_prefix}/lib/                    \
    --enable-experimental-mail-utf8                 \
    --with-ioloop=best                              \
    --with-ldap=plugin                              \
    --with-sql=plugin                               \
    --with-gssapi=plugin                            \
    --with-pgsql                                    \
    --with-mysql                                    \
    --with-lua=plugin                               \
%if %{with apparmor}
    --with-apparmor                                 \
%endif
%if %{with sqlite}
    --with-sqlite                                   \
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
    --with-bzlib                                    \
%if %{with lz4}
    --with-lz4                                      \
%endif
%if %{with zstd}
    --with-zstd                                     \
%endif
    --with-libcap                                   \
    --disable-static
%make_build

pushd %{dovecot_pigeonhole_source_dir}
    %configure --with-dovecot=../ \
      --with-ldap=plugin \
      --docdir="%{dovecot_pigeonhole_docdir}"
    %make_build
popd

%if %{with run_tests}
%check
%make_build check
%make_build -C %{dovecot_pigeonhole_source_dir} test
%endif

%install
%make_install
%make_install -C %{dovecot_pigeonhole_source_dir} sieve_docdir=%{dovecot_pigeonhole_docdir}

# clean up unused files, as much as I would like to use -delete ... the old find on sles9 doesnt support it
find %{buildroot}%{_libdir}/%{pkg_name}/ -type f \
	'(' -name \*.la -o -name \*.a ')' -print -delete

# create /var directories
install -m 0755 -Dd \
  %{buildroot}%{_var}/run/%{pkg_name}/login/ \
  %{buildroot}%{_var}/lib/%{pkg_name}/

install -D -m 0644 doc/dovecot.conf %{buildroot}%{_docdir}/%{pkg_name}/example-config/

# install the script to create dummy selfsigned certs
pushd %{buildroot}%{_docdir}/%{pkg_name}/
chmod +x mkcert.sh
mv -v {*.cnf,mkcert.sh,example-config} ../../../%{pkg_name}/

install -m 755 -d example-config/{,conf.d/}
ln -sv ../../../%{pkg_name}/{*.cnf,mkcert.sh} .
cd example-config/
ln -sv \
    ../../../../%{pkg_name}/example-config/*conf \
  .
cd conf.d/
ln -sv \
    ../../../../../%{pkg_name}/example-config/conf.d/* \
  .
popd

# additional docs for the main package
install -m 0644 \
       AUTHORS ChangeLog* COPYING* NEWS README* \
%if %{with solr}
    doc/*.xml \
%endif
    %{buildroot}%{_docdir}/%{pkg_name}/

# install sieve docs
install -m 0755 -Dd %{buildroot}%{dovecot_pigeonhole_docdir}
pushd %{dovecot_pigeonhole_source_dir}
sed -i 's/\r$//' doc/rfc/*
cp -av AUTHORS COPYING* INSTALL NEWS README \
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
rm %{buildroot}%{_unitdir}/dovecot.{service,socket}
rm %{buildroot}%{_sysconfdir}/%{pkg_name}/README

# create symlinks for man pages
%fdupes -s %{buildroot}/%{_mandir}
# create hardlinks for the rest
%fdupes %{buildroot}/%{_docdir}

%pre
# do not let dovecot run during upgrade rhbz#134325
if [ "$1" -ge "1" ]; then
  rm -f %{restart_flag}
    # we get installed before the unversioned dovecot package is installed
    # in that case we dont need to restart as there was no file to start us before
    if [ -x /bin/systemctl -a -e %{_unitdir}/%{pkg_name}.service ] ; then
      /bin/systemctl is-active %{pkg_name}.service >/dev/null 2>&1 && touch %{restart_flag} ||:
      /bin/systemctl stop      %{pkg_name}.service >/dev/null 2>&1
    fi
fi

%post -p /sbin/ldconfig

%postun
/sbin/ldconfig
# do not let dovecot run during upgrade rhbz#134325
if [ "$1" -ge "1" -a -e %{restart_flag} ]; then
    # we get installed before the unversioned dovecot package is installed
    # in that case we dont need to restart as there was no file to start us before
    if [ -x /bin/systemctl -a -e %{_unitdir}/%{pkg_name}.service ] ; then
      /bin/systemctl start %{pkg_name}.service >/dev/null 2>&1 || :
    fi
  rm -f %{restart_flag}
fi

# do not let dovecot run during upgrade rhbz#134325
# dovecot should be started again in %%postun, but it's not executed on reinstall
# if it was already started, restart_flag won't be here, so it's ok to test it again
%posttrans
if [ -e %{restart_flag} ]; then
    # we get installed before the unversioned dovecot package is installed
    # in that case we dont need to restart as there was no file to start us before
    if [ -x /bin/systemctl -a -e %{_unitdir}/%{pkg_name}.service ] ; then
      /bin/systemctl start %{pkg_name}.service >/dev/null 2>&1 || :
    fi
  rm -f %{restart_flag}
fi

%files
%dir %{_sysconfdir}/%{pkg_name}/
%ghost %config(noreplace) %{_sysconfdir}/%{pkg_name}/*
%{_sbindir}/dovecot
%{_bindir}/doveconf
%{_bindir}/dovecot-sysreport
%{_bindir}/doveadm
%{_bindir}/sievec
%{_bindir}/sieve-dump
%{_bindir}/sieve-test
%{_bindir}/sieve-filter
# subprocesses
%dir %{_prefix}/lib/%{pkg_name}/
%{_prefix}/lib/%{pkg_name}/anvil
%{_prefix}/lib/%{pkg_name}/auth
%{_prefix}/lib/%{pkg_name}/dict
%{_prefix}/lib/%{pkg_name}/dict-expire
%{_prefix}/lib/%{pkg_name}/dns-client
%{_prefix}/lib/%{pkg_name}/indexer
%{_prefix}/lib/%{pkg_name}/indexer-worker
%{_prefix}/lib/%{pkg_name}/imap-hibernate
%{_prefix}/lib/%{pkg_name}/imap-login
%{_prefix}/lib/%{pkg_name}/imap
%{_prefix}/lib/%{pkg_name}/imap-urlauth
%{_prefix}/lib/%{pkg_name}/imap-urlauth-worker
%{_prefix}/lib/%{pkg_name}/imap-urlauth-login
%{_prefix}/lib/%{pkg_name}/pop3-login
%{_prefix}/lib/%{pkg_name}/pop3
%{_prefix}/lib/%{pkg_name}/submission-login
%{_prefix}/lib/%{pkg_name}/submission
%{_prefix}/lib/%{pkg_name}/deliver
%{_prefix}/lib/%{pkg_name}/dovecot-lda
%{_prefix}/lib/%{pkg_name}/lmtp
%{_prefix}/lib/%{pkg_name}/log
%{_prefix}/lib/%{pkg_name}/config
%{_prefix}/lib/%{pkg_name}/rawlog
%{_prefix}/lib/%{pkg_name}/script
%{_prefix}/lib/%{pkg_name}/script-login
%{_prefix}/lib/%{pkg_name}/gdbhelper
%{_prefix}/lib/%{pkg_name}/health-check.sh
%{_prefix}/lib/%{pkg_name}/doveadm-server
%{_prefix}/lib/%{pkg_name}/stats
%{_prefix}/lib/%{pkg_name}/xml2text
%{_prefix}/lib/%{pkg_name}/decode2text.sh
%{_prefix}/lib/%{pkg_name}/quota-status
%{_prefix}/lib/%{pkg_name}/managesieve
%{_prefix}/lib/%{pkg_name}/managesieve-login
%{_libdir}/%{pkg_name}/libdovecot.so.*
%{_libdir}/%{pkg_name}/libdovecot-ldap.so.*
%{_libdir}/%{pkg_name}/libdovecot-lua.so.*
%{_libdir}/%{pkg_name}/libdovecot-language.so.*
%{_libdir}/%{pkg_name}/libdovecot-compression.so.*
%{_libdir}/%{pkg_name}/libdovecot-storage.so.*
%{_libdir}/%{pkg_name}/libdovecot-storage-lua.so.*
%{_libdir}/%{pkg_name}/libdovecot-sql.so.*
%{_libdir}/%{pkg_name}/libdovecot-lda.so.*
%{_libdir}/%{pkg_name}/libdovecot-login.so.*
%{_libdir}/%{pkg_name}/libdovecot-dsync.so.*
%{_libdir}/%{pkg_name}/libdovecot-sieve.so.*
%{_libdir}/%{pkg_name}/libdovecot-managesieve.so.*
# plugins
%dir %{_libdir}/%{pkg_name}
%dir %{_libdir}/%{pkg_name}/modules/
%if %{with apparmor}
%{_libdir}/%{pkg_name}/modules/lib01_apparmor_plugin.so
%endif
%{_libdir}/%{pkg_name}/modules/lib01_acl_plugin.so
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
%{_libdir}/%{pkg_name}/modules/lib20_notify_status_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_charset_alias_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_push_notification_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_quota_clone_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_virtual_plugin.so
%{_libdir}/%{pkg_name}/modules/lib22_push_notification_lua_plugin.so
%{_libdir}/%{pkg_name}/modules/lib02_imap_acl_plugin.so
%{_libdir}/%{pkg_name}/modules/lib11_imap_quota_plugin.so
%{_libdir}/%{pkg_name}/modules/lib90_sieve_plugin.so
%{_libdir}/%{pkg_name}/modules/lib95_imap_sieve_plugin.so
%{_libdir}/%{pkg_name}/modules/lib95_imap_filter_sieve_plugin.so
%{_libdir}/%{pkg_name}/modules/lib99_welcome_plugin.so
%{_libdir}/%{pkg_name}/modules/libfs_compress.so
%{_libdir}/%{pkg_name}/modules/libfs_crypt.so
%{_libdir}/%{pkg_name}/modules/libssl_iostream_openssl.so
%{_libdir}/%{pkg_name}/modules/lib20_mail_compress_plugin.so
%{_libdir}/%{pkg_name}/modules/var_expand_crypt.so

#
%dir %{_libdir}/%{pkg_name}/modules/auth/
%{_libdir}/%{pkg_name}/modules/auth/libauthdb_imap.so
%{_libdir}/%{pkg_name}/modules/auth/libauthdb_ldap.so
%{_libdir}/%{pkg_name}/modules/auth/libauthdb_lua.so
%{_libdir}/%{pkg_name}/modules/auth/libmech_gssapi.so
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
%dir %{_datadir}/%{pkg_name}/
%{_datadir}/%{pkg_name}/*.cnf
%{_datadir}/%{pkg_name}/mkcert.sh
%{_datadir}/%{pkg_name}/example-config
%{_mandir}/man1/deliver.1%{?ext_man}
%{_mandir}/man1/doveadm-acl.1%{?ext_man}
%{_mandir}/man1/doveadm-altmove.1%{?ext_man}
%{_mandir}/man1/doveadm-auth.1%{?ext_man}
%{_mandir}/man1/doveadm-backup.1%{?ext_man}
%{_mandir}/man1/doveadm-compress-connect.1%{?ext_man}
%{_mandir}/man1/doveadm-config.1%{?ext_man}
%{_mandir}/man1/doveadm-copy.1%{?ext_man}
%{_mandir}/man1/doveadm-deduplicate.1%{?ext_man}
%{_mandir}/man1/doveadm-dict.1%{?ext_man}
%{_mandir}/man1/doveadm-dump.1%{?ext_man}
%{_mandir}/man1/doveadm-exec.1%{?ext_man}
%{_mandir}/man1/doveadm-expunge.1%{?ext_man}
%{_mandir}/man1/doveadm-fetch.1%{?ext_man}
%{_mandir}/man1/doveadm-flags.1%{?ext_man}
%{_mandir}/man1/doveadm-force-resync.1%{?ext_man}
%{_mandir}/man1/doveadm-fs.1%{?ext_man}
%{_mandir}/man1/doveadm-fts.1%{?ext_man}
%{_mandir}/man1/doveadm-help.1%{?ext_man}
%{_mandir}/man1/doveadm-import.1%{?ext_man}
%{_mandir}/man1/doveadm-index.1%{?ext_man}
%{_mandir}/man1/doveadm-indexer.1%{?ext_man}
%{_mandir}/man1/doveadm-instance.1%{?ext_man}
%{_mandir}/man1/doveadm-kick.1%{?ext_man}
%{_mandir}/man1/doveadm-log.1%{?ext_man}
%{_mandir}/man1/doveadm-mail-dict.1%{?ext_man}
%{_mandir}/man1/doveadm-mail-fs.1%{?ext_man}
%{_mandir}/man1/doveadm-mailbox-cryptokey.1%{?ext_man}
%{_mandir}/man1/doveadm-mailbox.1%{?ext_man}
%{_mandir}/man1/doveadm-move.1%{?ext_man}
%{_mandir}/man1/doveadm-penalty.1%{?ext_man}
%{_mandir}/man1/doveadm-process-status.1%{?ext_man}
%{_mandir}/man1/doveadm-proxy.1%{?ext_man}
%{_mandir}/man1/doveadm-purge.1%{?ext_man}
%{_mandir}/man1/doveadm-pw.1%{?ext_man}
%{_mandir}/man1/doveadm-quota.1%{?ext_man}
%{_mandir}/man1/doveadm-rebuild.1%{?ext_man}
%{_mandir}/man1/doveadm-reload.1%{?ext_man}
%{_mandir}/man1/doveadm-save.1%{?ext_man}
%{_mandir}/man1/doveadm-search.1%{?ext_man}
%{_mandir}/man1/doveadm-service-status.1%{?ext_man}
%{_mandir}/man1/doveadm-service-stop.1%{?ext_man}
%{_mandir}/man1/doveadm-stats.1%{?ext_man}
%{_mandir}/man1/doveadm-stop.1%{?ext_man}
%{_mandir}/man1/doveadm-sync.1%{?ext_man}
%{_mandir}/man1/doveadm-user.1%{?ext_man}
%{_mandir}/man1/doveadm-who.1%{?ext_man}
%{_mandir}/man1/doveadm.1%{?ext_man}
%{_mandir}/man1/doveconf.1%{?ext_man}
%{_mandir}/man1/dovecot-lda.1%{?ext_man}
%{_mandir}/man1/dovecot-sysreport.1%{?ext_man}
%{_mandir}/man1/dovecot.1%{?ext_man}
%{_mandir}/man1/doveadm-sieve.1%{?ext_man}
%{_mandir}/man1/sieve-dump.1%{?ext_man}
%{_mandir}/man1/sieve-filter.1%{?ext_man}
%{_mandir}/man1/sieve-test.1%{?ext_man}
%{_mandir}/man1/sievec.1%{?ext_man}
%{_mandir}/man1/sieved.1%{?ext_man}
%{_mandir}/man7/doveadm-search-query.7%{?ext_man}
%{_mandir}/man7/pigeonhole.7%{?ext_man}
# doc
%doc %{_docdir}/%{pkg_name}
%if %{with solr}
%exclude %{_docdir}/%{pkg_name}/solr*.xml
%endif
# setting up permissions
%dir %attr(0750,root,root) %{_var}/lib/%{pkg_name}/

%files fts
%{_libdir}/%{pkg_name}/modules/doveadm/lib20_doveadm_fts_plugin.so
%{_libdir}/%{pkg_name}/modules/lib20_fts_plugin.so
%{_datadir}/%{pkg_name}/stopwords/

%files fts-flatcurve
%{_libdir}/%{pkg_name}/modules/lib21_fts_flatcurve_plugin.so
%{_libdir}/%{pkg_name}/modules/doveadm/libdoveadm_fts_flatcurve_plugin.so

%files backend-mysql
%{_libdir}/%{pkg_name}/modules/libdriver_mysql.so
%{_libdir}/%{pkg_name}/modules/auth/libdriver_mysql.so
%{_libdir}/%{pkg_name}/modules/dict/libdriver_mysql.so

%files backend-pgsql
%{_libdir}/%{pkg_name}/modules/libdriver_pgsql.so
%{_libdir}/%{pkg_name}/modules/auth/libdriver_pgsql.so
%{_libdir}/%{pkg_name}/modules/dict/libdriver_pgsql.so

%if %{with sqlite}
%files backend-sqlite
%{_libdir}/%{pkg_name}/modules/libdriver_sqlite.so
%{_libdir}/%{pkg_name}/modules/auth/libdriver_sqlite.so
%{_libdir}/%{pkg_name}/modules/dict/libdriver_sqlite.so
%endif

%if %{with solr}
%files fts-solr
%{_libdir}/%{pkg_name}/modules/lib21_fts_solr_plugin.so
%{_docdir}/%{pkg_name}/solr*.xml
%endif

%files devel
%{_datadir}/aclocal/%{pkg_name}.m4
%{_datadir}/aclocal/dovecot-pigeonhole.m4
%{_includedir}/%{pkg_name}/
%{_libdir}/%{pkg_name}/dovecot-config
%{_libdir}/%{pkg_name}/libdcrypt_openssl.so
%{_libdir}/%{pkg_name}/libdovecot.so
%{_libdir}/%{pkg_name}/libdovecot-ldap.so
%{_libdir}/%{pkg_name}/libdovecot-lua.so
%{_libdir}/%{pkg_name}/libdovecot-language.so
%{_libdir}/%{pkg_name}/libdovecot-compression.so
%{_libdir}/%{pkg_name}/libdovecot-storage.so
%{_libdir}/%{pkg_name}/libdovecot-storage-lua.so
%{_libdir}/%{pkg_name}/libdovecot-sql.so
%{_libdir}/%{pkg_name}/libdovecot-lda.so
%{_libdir}/%{pkg_name}/libdovecot-login.so
%{_libdir}/%{pkg_name}/libdovecot-dsync.so
%{_libdir}/%{pkg_name}/libdovecot-sieve.so
%{_libdir}/%{pkg_name}/libdovecot-managesieve.so

%changelog
