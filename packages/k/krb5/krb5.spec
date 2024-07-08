#
# spec file for package krb5
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
Name:           krb5
Version:        1.21.3
Release:        0
Summary:        MIT Kerberos5 implementation
License:        MIT
URL:            https://kerberos.org/dist/
Source0:        https://kerberos.org/dist/krb5/1.21/krb5-%{version}.tar.gz
Source1:        https://kerberos.org/dist/krb5/1.21/krb5-%{version}.tar.gz.asc
Source2:        krb5.keyring
Source3:        vendor-files.tar.bz2
Source4:        baselibs.conf
Source5:        krb5-rpmlintrc
Source6:        ksu-pam.d
Source7:        krb5.tmpfiles
Patch1:         0001-ksu-pam-integration.patch
Patch2:         0002-krb5-1.9-manpaths.patch
Patch3:         0003-Adjust-build-configuration.patch
Patch4:         0004-krb5-1.6.3-gssapi_improve_errormessages.patch
Patch5:         0005-krb5-1.6.3-ktutil-manpage.patch
Patch6:         0006-krb5-1.12-api.patch
Patch7:         0007-SELinux-integration.patch
Patch8:         0008-krb5-1.9-debuginfo.patch
Patch9:         0009-Fix-three-memory-leaks.patch
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
BuildRequires:  keyutils
BuildRequires:  keyutils-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(com_err)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libverto)
BuildRequires:  pkgconfig(lmdb)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ss)
BuildRequires:  pkgconfig(systemd)
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
BuildRequires:  crypto-policies
Requires:       crypto-policies
%endif
Conflicts:      krb5-mini
Obsoletes:      krb5-plugin-preauth-pkinit-nss

%description
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of clear text passwords.

%package client
Summary:        Client programs of the MIT Kerberos5 implementation
Conflicts:      krb5-mini

%description client
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of cleartext passwords. This package includes some required
client programs, like kinit, kadmin, ...

%package server
Summary:        Server program of the MIT Kerberos5 implementation
Requires:       libverto-libev1
Requires:       logrotate
Requires:       perl-Date-Calc
Requires(post): %fillup_prereq
%{?systemd_requires}

%description server
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of cleartext passwords. This package includes the kdc, kadmind
and more.

%package plugin-kdb-ldap
Summary:        LDAP database plugin for MIT Kerberos5
Requires:       krb5-server = %{version}

%description plugin-kdb-ldap
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of clear text passwords. This package contains the LDAP
database plugin.

%package plugin-preauth-pkinit
Summary:        PKINIT preauthentication plugin for MIT Kerberos5

%description plugin-preauth-pkinit
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of cleartext passwords. This package includes a PKINIT plugin.

%package plugin-preauth-otp
Summary:        OTP preauthentication plugin for MIT Kerberos5

%description plugin-preauth-otp
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of cleartext passwords. This package includes a OTP plugin.

%package plugin-preauth-spake
Summary:        SPAKE preauthentication plugin for MIT Kerberos5

%description plugin-preauth-spake
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of cleartext passwords. This package includes a SPAKE plugin.

%package doc
Summary:        Documentation for the MIT Kerberos5 implementation

%description doc
Kerberos V5 is a trusted-third-party network authentication
system,which can improve network security by eliminating the
insecurepractice of clear text passwords. This package includes
extended documentation for MIT Kerberos.

%package devel
Summary:        Development files for MIT Kerberos5
Requires:       %{name} = %{version}
Requires:       keyutils-devel
Requires:       pkgconfig(com_err)
Requires:       pkgconfig(libverto)
Requires:       pkgconfig(ss)
Conflicts:      krb5-mini-devel

%description devel
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of cleartext passwords. This package includes Libraries and
Include Files for Development

%define srcRoot krb5-%{version}
%define vendorFiles %{_builddir}/%{srcRoot}/vendor-files/
%define krb5docdir  %{_defaultdocdir}/krb5

%prep
%setup -q -n %{srcRoot}
%setup -q -a 3 -T -D -n %{srcRoot}
%autopatch -p1

%build
# needs to be re-generated
rm -f src/lib/krb5/krb/deltat.c
cd src
autoreconf -fi
DEFCCNAME=DIR:/run/user/%%{uid}/krb5cc; export DEFCCNAME
%configure \
        CFLAGS="%{optflags} -I%{_includedir}/et -fno-strict-aliasing -D_GNU_SOURCE -fPIC $(getconf LFS_CFLAGS)" \
        CPPFLAGS="-I%{_includedir}/et " \
        SS_LIB="-lss" \
    --sysconfdir=%{_sysconfdir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir} \
    --localstatedir=%{_localstatedir}/lib/kerberos \
    --localedir=%{_datadir}/locale \
    --enable-shared \
    --disable-static \
    --enable-dns-for-realm \
    --disable-rpath \
    --with-ldap \
    --with-pam \
    --enable-pkinit \
    --with-crypto-impl=openssl \
    --with-selinux \
    --with-system-et \
    --with-system-ss \
    --with-system-verto \
    --with-lmdb

%make_build

# Copy kadmin manual page into kadmin.local's due to the split between client and server package
cp man/kadmin.man man/kadmin.local.8

%install
mkdir -p %{buildroot}/%{_localstatedir}/log/krb5
%make_install -C src
# Munge krb5-config yet again.  This is totally wrong for 64-bit, but chunks
# of the buildconf patch already conspire to strip out /usr/<anything> from the
# list of link flags, and it helps prevent file conflicts on multilib systems.
sed -r -i -e 's|^libdir=%{_prefix}/lib(64)?$|libdir=%{_prefix}/lib|g' %{buildroot}%{_bindir}/krb5-config

# install autoconf macro
mkdir -p %{buildroot}/%{_datadir}/aclocal
install -m 644 src/util/ac_check_krb5.m4 %{buildroot}%{_datadir}/aclocal/
# install sample config files
# I'll probably do something about this later on
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/krb5.conf.d
mkdir -p %{buildroot}%{_localstatedir}/log/krb5
# create plugin directories
mkdir -p %{buildroot}/%{_libdir}/krb5/plugins/kdb
mkdir -p %{buildroot}/%{_libdir}/krb5/plugins/preauth
mkdir -p %{buildroot}/%{_libdir}/krb5/plugins/libkrb5
mkdir -p %{buildroot}/%{_libdir}/krb5/plugins/tls
install -m 644 %{vendorFiles}/krb5.conf %{buildroot}%{_sysconfdir}

# Do not write directly to /var/lib/kerberos anymore as it breaks transactional
# updates. Use systemd-tmpfiles to copy the files there when it doesn't exist
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
install -m 644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/krb5.conf
mkdir -p %{buildroot}/%{_datadir}/kerberos/krb5kdc
# Where per-user keytabs live by default.
mkdir -p %{buildroot}/%{_datadir}/kerberos/krb5/user
install -m 600 %{vendorFiles}/kdc.conf %{buildroot}%{_datadir}/kerberos/krb5kdc/
install -m 600 %{vendorFiles}/kadm5.acl %{buildroot}%{_datadir}/kerberos/krb5kdc/
install -m 600 %{vendorFiles}/kadm5.dict %{buildroot}%{_datadir}/kerberos/krb5kdc/

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
# Default include on this directory
ln -sv %{_sysconfdir}/crypto-policies/back-ends/krb5.config %{buildroot}%{_sysconfdir}/krb5.conf.d/crypto-policies
%endif

# all libs must have permissions 0755
for lib in `find %{buildroot}/%{_libdir}/ -type f -name "*.so*"`
do
  chmod 0755 ${lib}
done
# and binaries too
chmod 0755 %{buildroot}%{_bindir}/ksu
# install systemd files
%if 0%{?suse_version} >= 1210
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{vendorFiles}/kadmind.service %{buildroot}%{_unitdir}
install -m 644 %{vendorFiles}/krb5kdc.service %{buildroot}%{_unitdir}
install -m 644 %{vendorFiles}/kpropd.service %{buildroot}%{_unitdir}
%else
# install init scripts
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 755 %{vendorFiles}/kadmind.init %{buildroot}%{_sysconfdir}/init.d/kadmind
install -m 755 %{vendorFiles}/krb5kdc.init %{buildroot}%{_sysconfdir}/init.d/krb5kdc
install -m 755 %{vendorFiles}/kpropd.init  %{buildroot}%{_sysconfdir}/init.d/kpropd
%endif
# install sysconfig templates
mkdir -p %{buildroot}/%{_fillupdir}
install -m 644 %{vendorFiles}/sysconfig.kadmind %{buildroot}/%{_fillupdir}/
install -m 644 %{vendorFiles}/sysconfig.krb5kdc %{buildroot}/%{_fillupdir}/
# install logrotate files
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 %{vendorFiles}/krb5-server.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/krb5-server
find . -type f -name '*.ps' -exec gzip -9 {} +
# create rc* links
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_sbindir}/
ln -s service %{buildroot}%{_sbindir}/rckadmind
ln -s service %{buildroot}%{_sbindir}/rckrb5kdc
ln -s service %{buildroot}%{_sbindir}/rckpropd
# install doc
install -d -m 755 %{buildroot}/%{krb5docdir}
install -m 644 %{_builddir}/%{srcRoot}/README %{buildroot}/%{krb5docdir}/README
install -d -m 755 %{buildroot}/%{_datadir}/kerberos/ldap
install -m 644 %{_builddir}/%{srcRoot}/src/plugins/kdb/ldap/libkdb_ldap/kerberos.schema %{buildroot}/%{_datadir}/kerberos/ldap/kerberos.schema
install -m 644 %{_builddir}/%{srcRoot}/src/plugins/kdb/ldap/libkdb_ldap/kerberos.ldif %{buildroot}/%{_datadir}/kerberos/ldap/kerberos.ldif
# link pam-config for su to ksu
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
install -m 644 %{SOURCE6} %{buildroot}%{_pam_vendordir}/ksu
%else
mkdir -p %{buildroot}%{_sysconfdir}/pam.d/
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/pam.d/ksu
%endif

# cleanup
rm -f  %{buildroot}%{_mandir}/man1/tmac.doc*
rm -f  %{_mandir}/man1/tmac.doc* html/.doctrees/environment.pickle
rm -rf %{buildroot}%{_datadir}/examples
# manually remove test plugin since configure doesn't support disabling it at build time
rm -f %{buildroot}/%{_libdir}/krb5/plugins/preauth/test.so

%if "%{_lto_cflags}" != ""
# Don't add the lto flags to the public link flags.
sed -i "s/%{_lto_cflags}//" %{buildroot}%{_bindir}/krb5-config
%endif

%find_lang mit-krb5

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%preun server
%service_del_preun krb5kdc.service kadmind.service kpropd.service

%postun server
%service_del_postun krb5kdc.service kadmind.service kpropd.service

%post server
%service_add_post krb5kdc.service kadmind.service kpropd.service
%tmpfiles_create krb5.conf
%{fillup_only -n kadmind}
%{fillup_only -n krb5kdc}
%{fillup_only -n kpropd}

%pre server
%service_add_pre krb5kdc.service kadmind.service kpropd.service

%post plugin-kdb-ldap -p /sbin/ldconfig
%postun plugin-kdb-ldap -p /sbin/ldconfig

%if 0%{?suse_version} > 1500
%pre client
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in pam.d/ksu ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans client
# Migration to /usr/etc, restore just created .rpmsave
for i in pam.d/ksu ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%files devel
%dir %{_datadir}/aclocal
%{_libdir}/libgssrpc.so
%{_libdir}/libk5crypto.so
%{_libdir}/libkadm5clnt_mit.so
%{_libdir}/libkadm5clnt.so
%{_libdir}/libkadm5srv_mit.so
%{_libdir}/libkadm5srv.so
%{_libdir}/libkdb5.so
%{_libdir}/libkrb5.so
%{_libdir}/libkrb5support.so
%{_libdir}/libkrad.so
%{_libdir}/pkgconfig/gssrpc.pc
%{_libdir}/pkgconfig/kadm-client.pc
%{_libdir}/pkgconfig/kadm-server.pc
%{_libdir}/pkgconfig/kdb.pc
%{_libdir}/pkgconfig/krb5-gssapi.pc
%{_libdir}/pkgconfig/krb5.pc
%{_libdir}/pkgconfig/mit-krb5-gssapi.pc
%{_libdir}/pkgconfig/mit-krb5.pc
%{_includedir}/*
%{_bindir}/krb5-config
%{_sbindir}/krb5-send-pr
%{_mandir}/man1/krb5-config.1%{?ext_man}
%{_datadir}/aclocal/ac_check_krb5.m4

%files -f mit-krb5.lang
%dir %{krb5docdir}
# add plugin directories
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/kdb
%dir %{_libdir}/krb5/plugins/preauth
%dir %{_libdir}/krb5/plugins/libkrb5
%dir %{_libdir}/krb5/plugins/tls
# add log directory
%attr(0700,root,root) %dir %{_localstatedir}/log/krb5
%doc %{krb5docdir}/README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/krb5.conf
%dir %{_sysconfdir}/krb5.conf.d
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
%config(noreplace,missingok) %{_sysconfdir}/krb5.conf.d/crypto-policies
%endif
%{_libdir}/libgssapi_krb5.*
%{_libdir}/libgssrpc.so.*
%{_libdir}/libk5crypto.so.*
%{_libdir}/libkadm5clnt_mit.so.*
%{_libdir}/libkadm5srv_mit.so.*
%{_libdir}/libkdb5.so.*
%{_libdir}/libkrb5.so.*
%{_libdir}/libkrb5support.so.*
%{_libdir}/libkrad.so.*
%{_libdir}/krb5/plugins/tls/*.so

%files server
%attr(0700,root,root) %dir %{_localstatedir}/log/krb5
%config(noreplace) %{_sysconfdir}/logrotate.d/krb5-server
%{_unitdir}/kadmind.service
%{_unitdir}/krb5kdc.service
%{_unitdir}/kpropd.service
%{_tmpfilesdir}/krb5.conf
%dir %{krb5docdir}
%dir %{_datadir}/kerberos/
%dir %{_datadir}/kerberos/krb5kdc
%dir %{_datadir}/kerberos/krb5
%dir %{_datadir}/kerberos/krb5/user
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/kdb
%dir %{_libdir}/krb5/plugins/tls
%attr(0600,root,root) %config(noreplace) %{_datadir}/kerberos/krb5kdc/kdc.conf
%attr(0600,root,root) %config(noreplace) %{_datadir}/kerberos/krb5kdc/kadm5.acl
%attr(0600,root,root) %config(noreplace) %{_datadir}/kerberos/krb5kdc/kadm5.dict
%ghost %dir %{_sharedstatedir}/kerberos/
%ghost %dir %{_sharedstatedir}/kerberos/krb5kdc
%ghost %dir %{_sharedstatedir}/kerberos/krb5
%ghost %dir %{_sharedstatedir}/kerberos/krb5/user
%ghost %attr(0600,root,root) %config(noreplace) %{_sharedstatedir}/kerberos/krb5kdc/kdc.conf
%ghost %attr(0600,root,root) %config(noreplace) %{_sharedstatedir}/kerberos/krb5kdc/kadm5.acl
%ghost %attr(0600,root,root) %config(noreplace) %{_sharedstatedir}/kerberos/krb5kdc/kadm5.dict
%{_fillupdir}/sysconfig.*
%{_sbindir}/rc*
%{_sbindir}/kadmin.local
%{_sbindir}/kadmind
%{_sbindir}/kpropd
%{_sbindir}/kproplog
%{_sbindir}/kprop
%{_sbindir}/kdb5_util
%{_sbindir}/krb5kdc
%{_sbindir}/gss-server
%{_sbindir}/sim_server
%{_sbindir}/sserver
%{_sbindir}/uuserver
%{_libdir}/krb5/plugins/kdb/db2.so
%{_libdir}/krb5/plugins/kdb/klmdb.so
%{_mandir}/man5/kdc.conf.5%{?ext_man}
%{_mandir}/man5/kadm5.acl.5%{?ext_man}
%{_mandir}/man8/kadmind.8%{?ext_man}
%{_mandir}/man8/kadmin.local.8%{?ext_man}
%{_mandir}/man8/kpropd.8%{?ext_man}
%{_mandir}/man8/kprop.8%{?ext_man}
%{_mandir}/man8/kproplog.8%{?ext_man}
%{_mandir}/man8/kdb5_util.8%{?ext_man}
%{_mandir}/man8/krb5kdc.8%{?ext_man}
%{_mandir}/man8/sserver.8%{?ext_man}

%files client
%if 0%{?suse_version} > 1500
%attr(0644,root,root) %{_pam_vendordir}/ksu
%else
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/ksu
%endif
%{_bindir}/kvno
%{_bindir}/kinit
%{_bindir}/kdestroy
%{_bindir}/kpasswd
%{_bindir}/klist
%{_bindir}/kadmin
%{_bindir}/ktutil
%{_bindir}/k5srvutil
%{_bindir}/gss-client
%{_bindir}/ksu
%{_bindir}/sclient
%{_bindir}/sim_client
%{_bindir}/uuclient
%{_bindir}/kswitch
%{_bindir}/kinit
%{_bindir}/klist
%{_mandir}/man1/kvno.1%{?ext_man}
%{_mandir}/man1/kinit.1%{?ext_man}
%{_mandir}/man1/kdestroy.1%{?ext_man}
%{_mandir}/man1/kpasswd.1%{?ext_man}
%{_mandir}/man1/klist.1%{?ext_man}
%{_mandir}/man1/kadmin.1%{?ext_man}
%{_mandir}/man1/ktutil.1%{?ext_man}
%{_mandir}/man1/k5srvutil.1%{?ext_man}
%{_mandir}/man1/kswitch.1%{?ext_man}
%{_mandir}/man5/krb5.conf.5%{?ext_man}
%{_mandir}/man5/.k5login.5%{?ext_man}
%{_mandir}/man5/.k5identity.5%{?ext_man}
%{_mandir}/man5/k5identity.5%{?ext_man}
%{_mandir}/man5/k5login.5%{?ext_man}
%{_mandir}/man1/ksu.1%{?ext_man}
%{_mandir}/man1/sclient.1%{?ext_man}
%{_mandir}/man7/kerberos.7%{?ext_man}

%files plugin-kdb-ldap
%{_sbindir}/kdb5_ldap_util
%dir %{_datadir}/kerberos
%dir %{_datadir}/kerberos/ldap
%config %{_datadir}/kerberos/ldap/kerberos.schema
%config %{_datadir}/kerberos/ldap/kerberos.ldif
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/kdb
%{_libdir}/krb5/plugins/kdb/kldap.so
%{_libdir}/libkdb_ldap*
%{_mandir}/man8/kdb5_ldap_util.8%{?ext_man}

%files plugin-preauth-pkinit
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/preauth
%{_libdir}/krb5/plugins/preauth/pkinit.so

%files plugin-preauth-otp
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/preauth
%{_libdir}/krb5/plugins/preauth/otp.so

%files plugin-preauth-spake
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/preauth
%{_libdir}/krb5/plugins/preauth/spake.so

%changelog
