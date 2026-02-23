#
# spec file for package proftpd
#
# Copyright (c) 2026 SUSE LLC
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


%define with_redis 1

%if 0%{?suse_version} == 1500
%define with_redis 0
%endif

Name:           proftpd
Summary:        Configurable GPL-licensed FTP server software
# Please save your time and do not update to "rc" versions.
# We only accept updates for "STABLE" Versions
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Ftp/Servers
Version:        1.3.9
Release:        0
URL:            http://www.proftpd.org/
Source0:        %{name}-%{version}.tar.xz
Source12:       %{name}.passwd
Source13:       %{name}.service
Source14:       %{name}.tmpfile
Source15:       %{name}.keyring
Source16:       %{name}-tls.template
Source17:       %{name}-limit.template
Source18:       %{name}-ssl.README
#PATCH-FIX-openSUSE: pam, logrotate, xinet
Patch100:       %{name}_dist.patch
#PATCH-FIX-openSUSE: provide a useful default config
Patch101:       %{name}_basic.conf.patch
#PATCH-FIX: provide more info on usage ;)
Patch102:       %{name}_ftpasswd.patch
#PATCH-FIX: fix strip
Patch103:       %{name}_strip.patch
#PATCH-FIX-openSUSE: file-contains-date-and-time
Patch104:       %{name}_no-BuildDate.patch
#RPMLINT-FIX-openSUSE: env-script-interpreter
Patch105:       %{name}_env-script-interpreter.patch
#openSUSE:Security_Features#Systemd_hardening_effort
Patch106:       harden_proftpd.service.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#
BuildRequires:  cyrus-sasl-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if 0%{?with_redis}
BuildRequires:  hiredis-devel
%endif
BuildRequires:  krb5-devel
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libmemcached-devel
#BuildRequires:  libGeoIP-devel
BuildRequires:  libmysqld-devel
BuildRequires:  libsodium-devel
BuildRequires:  ncurses-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkg-config
BuildRequires:  postgresql-devel
BuildRequires:  sqlite3-devel
BuildRequires:  unixODBC-devel
BuildRequires:  pkgconfig(libssl)
#
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}
#
Requires(pre):  group(ftp)
Requires(pre):  user(ftp)
Requires:       logrotate

%if 0%{?lang_package:1} > 0
Recommends:     %{name}-lang
%endif

%description
ProFTPD is a configurable FTP daemon for Unix and Unix-like
operating systems.

%{?lang_package}

%package devel
Summary:        Development files for ProFTPD
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains Development files for ProFTPD

%package ldap
Summary:        LDAP Module for ProFTPD
Group:          Productivity/Networking/Ftp/Servers
Requires:       %{name} = %{version}

%description ldap
This is the LDAP Module for ProFTPD

%package mysql
Summary:        MySQL Module for ProFTPD
Group:          Productivity/Networking/Ftp/Servers
Requires:       %{name} = %{version}

%description mysql
This is the MySQL Module for ProFTPD

%package pgsql
Summary:        PostgreSQL Module for ProFTPD
Group:          Productivity/Networking/Ftp/Servers
Requires:       %{name} = %{version}

%description pgsql
This is the PostgreSQL Module for ProFTPD

%package radius
Summary:        Radius Module for ProFTPD
Group:          Productivity/Networking/Ftp/Servers
Requires:       %{name} = %{version}

%description radius
This is the Radius Module for ProFTPD

%package sqlite
Summary:        SQLite Module for ProFTPD
Group:          Productivity/Networking/Ftp/Servers
Requires:       %{name} = %{version}

%description sqlite
This is the SQLite Module for ProFTPD

%package doc
Summary:        Documentation for ProFTPD
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description doc
Here are Documentation for ProFTPD

%prep
%autosetup -p0

%build
rm contrib/mod_wrap.c
rm contrib/mod_geoip.c
PROFTPD_SHARED_MODS="$(for spec_mod in $(find contrib -name mod_\*.c|sort); do echo "$(basename ${spec_mod%%.c})"; done | tr '\n' ':' | sed -e 's|:$||')"
export CFLAGS="%{optflags} -D_GNU_SOURCE -DLDAP_DEPRECATED"
export CXXFLAGS="$CFLAGS"
%configure \
    --bindir=%{_sbindir} \
    --libexecdir=%{_libdir}/%{name} \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --localstatedir=/run/%{name} \
    --enable-sendfile \
    --enable-ctrls \
    --enable-dso \
    --enable-facl \
    --enable-ipv6 \
    --enable-memcache \
    --enable-nls \
    --enable-openssl \
    --enable-pcre2 \
%if 0%{?with_redis}
    --enable-redis \
%endif
    --enable-shadow \
    --with-lastlog \
    --with-includes="%{_includedir}/mysql:%{_includedir}/pgsql" \
    --with-shared="${PROFTPD_SHARED_MODS}" \
    --disable-ident \
    --disable-strip

make %{?_smp_mflags}

%install
%make_install INSTALL_USER=`id -un` INSTALL_GROUP=`id -gn`
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
install -D -m 0644 contrib/dist/rpm/ftp.pamd   %{buildroot}/%{_pam_vendordir}/%{name}
%else
install -D -m 0644 contrib/dist/rpm/ftp.pamd   %{buildroot}/%{_sysconfdir}/pam.d/%{name}
%endif
install -D -m 0644 contrib/dist/rpm/%{name}.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
#
rm -fv %{buildroot}/%{_libdir}/%{name}/*.{a,la}

# install ftpasswd
install -D -m 0755 contrib/ftpasswd %{buildroot}/%{_sbindir}/

# some needed dirs
install -D -m 0440 %{S:12} %{buildroot}/%{_sysconfdir}/%{name}/auth/passwd
install -D -m 0644 %{S:16} %{buildroot}/%{_sysconfdir}/%{name}/conf.d/tls.template
install -D -m 0644 %{S:18} %{buildroot}/%{_sysconfdir}/%{name}/conf.d/README
install -D -m 0644 %{S:17} %{buildroot}/%{_sysconfdir}/%{name}/includes/limit.template
install -D -m 0644 %{S:18} %{buildroot}/%{_sysconfdir}/%{name}/ssl/README
install -d -m 0750 %{buildroot}/var/log/%{name}

# systemd
install -D -m 0644 %{S:13} %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}
# systemd need to create a tmp dir: /run/proftpd
install -D -m 0644 %{S:14} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%fdupes -s %{buildroot}%{_sysconfdir}/%{name}

%find_lang %{name}

%pre
%service_add_pre %{name}.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/proftpd ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/proftpd ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%postun
%service_del_postun %{name}.service

%if 0%{?lang_package:1} > 0
%files lang -f %{name}.lang
%if 0%{?sles_version} == 11
%defattr(-,root,root)
%dir %{_datadir}/locale/bg_BG
%dir %{_datadir}/locale/bg_BG/LC_MESSAGES
%dir %{_datadir}/locale/ja_JP
%dir %{_datadir}/locale/ja_JP/LC_MESSAGES
%dir %{_datadir}/locale/ko_KR
%dir %{_datadir}/locale/ko_KR/LC_MESSAGES
%endif

%files
%else

%files -f %{name}.lang
%endif
%defattr(-,root,root)
%license COPYING
%doc CREDITS NEWS README* RELEASE_NOTES
%doc contrib/README.*
%doc sample-configurations/*.conf
%dir %attr(0755,root,root) %{_sysconfdir}/%{name}/
%dir %attr(0750,ftp,ftp) %{_sysconfdir}/%{name}/auth/
%config(noreplace) %attr(0440,root,ftp) %{_sysconfdir}/%{name}/auth/passwd
%dir %attr(0755,root,root) %{_sysconfdir}/%{name}/conf.d/
%config %{_sysconfdir}/%{name}/conf.d/tls.template
%config %{_sysconfdir}/%{name}/conf.d/README
%dir %attr(0755,root,root) %{_sysconfdir}/%{name}/includes/
%config %{_sysconfdir}/%{name}/includes/limit.template
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/%{name}/%{name}.conf
%config %{_sysconfdir}/%{name}/PROFTPD-MIB.txt
%dir %attr(0700,ftp,ftp) %{_sysconfdir}/%{name}/ssl/
%config %{_sysconfdir}/%{name}/ssl/README
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/%{name}
%else
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%endif
%config(noreplace) %{_sysconfdir}/%{name}/blacklist.dat
%config(noreplace) %{_sysconfdir}/%{name}/dhparams.pem
%dir %attr(0750,root,root) %{_localstatedir}/log/%{name}
%{_sbindir}/*
%{_mandir}/man?/*
%dir %attr(0755,root,root) %{_libdir}/%{name}/
%{_libdir}/%{name}/mod_auth_otp.so
%{_libdir}/%{name}/mod_ban.so
%{_libdir}/%{name}/mod_copy.so
%{_libdir}/%{name}/mod_ctrls_admin.so
%{_libdir}/%{name}/mod_deflate.so
%{_libdir}/%{name}/mod_digest.so
%{_libdir}/%{name}/mod_dnsbl.so
%{_libdir}/%{name}/mod_dynmasq.so
%{_libdir}/%{name}/mod_exec.so
%{_libdir}/%{name}/mod_ifsession.so
%{_libdir}/%{name}/mod_ifversion.so
%{_libdir}/%{name}/mod_load.so
%{_libdir}/%{name}/mod_log_forensic.so
%{_libdir}/%{name}/mod_qos.so
%{_libdir}/%{name}/mod_quotatab.so
%{_libdir}/%{name}/mod_quotatab_file.so
%{_libdir}/%{name}/mod_quotatab_ldap.so
%{_libdir}/%{name}/mod_quotatab_radius.so
%{_libdir}/%{name}/mod_quotatab_sql.so
%{_libdir}/%{name}/mod_ratio.so
%{_libdir}/%{name}/mod_readme.so
%{_libdir}/%{name}/mod_rewrite.so
%{_libdir}/%{name}/mod_sftp.so
%{_libdir}/%{name}/mod_sftp_pam.so
%{_libdir}/%{name}/mod_sftp_sql.so
%{_libdir}/%{name}/mod_shaper.so
%{_libdir}/%{name}/mod_site_misc.so
%{_libdir}/%{name}/mod_snmp.so
%{_libdir}/%{name}/mod_sql.so
%{_libdir}/%{name}/mod_sql_odbc.so
%{_libdir}/%{name}/mod_sql_passwd.so
%{_libdir}/%{name}/mod_statcache.so
%{_libdir}/%{name}/mod_tls.so
%{_libdir}/%{name}/mod_tls_fscache.so
%{_libdir}/%{name}/mod_tls_memcache.so
%{_libdir}/%{name}/mod_tls_redis.so
%{_libdir}/%{name}/mod_tls_shmcache.so
%{_libdir}/%{name}/mod_unique_id.so
%{_libdir}/%{name}/mod_wrap2.so
%{_libdir}/%{name}/mod_wrap2_file.so
%{_libdir}/%{name}/mod_wrap2_redis.so
%{_libdir}/%{name}/mod_wrap2_sql.so
%exclude %{_libdir}/%{name}/mod_ldap.so
%exclude %{_libdir}/%{name}/mod_sql_mysql.so
%exclude %{_libdir}/%{name}/mod_sql_postgres.so
%exclude %{_libdir}/%{name}/mod_radius.so
%exclude %{_libdir}/%{name}/mod_sql_sqlite.so
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%ghost %dir /run/%{name}

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%files ldap
%defattr(-,root,root)
%{_libdir}/%{name}/mod_ldap.so

%files mysql
%defattr(-,root,root)
%{_libdir}/%{name}/mod_sql_mysql.so

%files pgsql
%defattr(-,root,root)
%{_libdir}/%{name}/mod_sql_postgres.so

%files radius
%defattr(-,root,root)
%{_libdir}/%{name}/mod_radius.so

%files sqlite
%defattr(-,root,root)
%{_libdir}/%{name}/mod_sql_sqlite.so

%files doc
%defattr(-,root,root)
%doc doc/*.html doc/contrib doc/howto doc/modules

%changelog
