#
# spec file for package krb5
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           krb5
Version:        1.17
Release:        0
Summary:        MIT Kerberos5 implementation
License:        MIT
Group:          Productivity/Networking/Security
URL:            https://web.mit.edu/kerberos/www/
Obsoletes:      krb5-plugin-preauth-pkinit-nss
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  keyutils
BuildRequires:  keyutils-devel
BuildRequires:  libcom_err-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libselinux-devel
BuildRequires:  libverto-devel
BuildRequires:  ncurses-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(systemd)
# bug437293
%ifarch ppc64
Obsoletes:      krb5-64bit
%endif
Conflicts:      krb5-mini
Source0:        https://web.mit.edu/kerberos/dist/krb5/1.17/krb5-%{version}.tar.gz
Source1:        https://web.mit.edu/kerberos/dist/krb5/1.17/krb5-%{version}.tar.gz.asc
Source2:        krb5.keyring
Source3:        vendor-files.tar.bz2
Source4:        baselibs.conf
Source5:        krb5-rpmlintrc
Source6:        ksu-pam.d
Source7:        krb5.tmpfiles
Patch1:         0001-krb5-1.12-pam.patch
Patch2:         0002-krb5-1.9-manpaths.patch
Patch3:         0003-krb5-1.12-buildconf.patch
Patch4:         0004-krb5-1.6.3-gssapi_improve_errormessages.patch
Patch5:         0005-krb5-1.6.3-ktutil-manpage.patch
Patch6:         0006-krb5-1.12-api.patch
Patch7:         0007-krb5-1.12-ksu-path.patch
Patch8:         0008-krb5-1.12-selinux-label.patch
Patch9:         0009-krb5-1.9-debuginfo.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of clear text passwords.

%package client
Conflicts:      krb5-mini
Summary:        Client programs of the MIT Kerberos5 implementation
Group:          Productivity/Networking/Security

%description client
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of cleartext passwords. This package includes some required
client programs, like kinit, kadmin, ...

%package server
Summary:        Server program of the MIT Kerberos5 implementation
Group:          Productivity/Networking/Security
Requires:       cron
Requires:       libverto-libev1
Requires:       logrotate
Requires:       perl-Date-Calc
%if 0%{?suse_version} >= 1210
%{?systemd_requires}
%else
PreReq:         %insserv_prereq
%endif
PreReq:         %fillup_prereq

%description server
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of cleartext passwords. This package includes the kdc, kadmind
and more.

%package plugin-kdb-ldap
Summary:        LDAP database plugin for MIT Kerberos5
Group:          Productivity/Networking/Security
Requires:       krb5-server = %{version}

%description plugin-kdb-ldap
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of clear text passwords. This package contains the LDAP
database plugin.

%package plugin-preauth-pkinit
Summary:        PKINIT preauthentication plugin for MIT Kerberos5
Group:          Productivity/Networking/Security

%description plugin-preauth-pkinit
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of cleartext passwords. This package includes a PKINIT plugin.

%package plugin-preauth-otp
Summary:        OTP preauthentication plugin for MIT Kerberos5
Group:          Productivity/Networking/Security

%description plugin-preauth-otp
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of cleartext passwords. This package includes a OTP plugin.

%package plugin-preauth-spake
Summary:        SPAKE preauthentication plugin for MIT Kerberos5
Group:          Productivity/Networking/Security

%description plugin-preauth-spake
Kerberos V5 is a trusted-third-party network authentication system,
which can improve network security by eliminating the insecure
practice of cleartext passwords. This package includes a SPAKE plugin.

%package doc
Summary:        Documentation for the MIT Kerberos5 implementation
Group:          Documentation/Other

%description doc
Kerberos V5 is a trusted-third-party network authentication
system,which can improve network security by eliminating the
insecurepractice of clear text passwords. This package includes
extended documentation for MIT Kerberos.

%package devel
Summary:        Development files for MIT Kerberos5
Group:          Development/Libraries/C and C++
PreReq:         %{name} = %{version}
Requires:       keyutils-devel
Requires:       libcom_err-devel
Requires:       libverto-devel
# bug437293
%ifarch ppc64
Obsoletes:      krb5-devel-64bit
%endif
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
%setup -a 3 -T -D -n %{srcRoot}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
# needs to be re-generated
rm -f src/lib/krb5/krb/deltat.c
cd src
autoreconf -fi
DEFCCNAME=DIR:/run/user/%%{uid}/krb5cc; export DEFCCNAME
./configure \
        CC="%{__cc}" \
        CFLAGS="%{optflags} -I%{_includedir}/et -fno-strict-aliasing -D_GNU_SOURCE -fPIC $(getconf LFS_CFLAGS)" \
        CPPFLAGS="-I%{_includedir}/et " \
        SS_LIB="-lss" \
	--prefix=/usr/lib/mit \
	--sysconfdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--libexecdir=/usr/lib/mit/sbin \
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
    --with-system-verto

make %{?_smp_mflags}

# Copy kadmin manual page into kadmin.local's due to the split between client and server package
cp man/kadmin.man man/kadmin.local.8

%install
mkdir -p %{buildroot}/%{_localstatedir}/log/krb5
%make_install -C src
# Munge krb5-config yet again.  This is totally wrong for 64-bit, but chunks
# of the buildconf patch already conspire to strip out /usr/<anything> from the
# list of link flags, and it helps prevent file conflicts on multilib systems.
sed -r -i -e 's|^libdir=/usr/lib(64)?$|libdir=/usr/lib|g' %{buildroot}/usr/lib/mit/bin/krb5-config

# install autoconf macro
mkdir -p %{buildroot}/%{_datadir}/aclocal
install -m 644 src/util/ac_check_krb5.m4 %{buildroot}%{_datadir}/aclocal/
# install sample config files
# I'll probably do something about this later on
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/krb5.conf.d
mkdir -p %{buildroot}/etc/profile.d/
mkdir -p %{buildroot}/var/log/krb5
# create plugin directories
mkdir -p %{buildroot}/%{_libdir}/krb5/plugins/kdb
mkdir -p %{buildroot}/%{_libdir}/krb5/plugins/preauth
mkdir -p %{buildroot}/%{_libdir}/krb5/plugins/libkrb5
mkdir -p %{buildroot}/%{_libdir}/krb5/plugins/tls
install -m 644 %{vendorFiles}/krb5.conf %{buildroot}%{_sysconfdir}
install -m 644 %{vendorFiles}/krb5.csh.profile %{buildroot}/etc/profile.d/krb5.csh
install -m 644 %{vendorFiles}/krb5.sh.profile %{buildroot}/etc/profile.d/krb5.sh

# Do not write directly to /var/lib/kerberos anymore as it breaks transactional
# updates. Use systemd-tmpfiles to copy the files there when it doesn't exist
install -d -m 0755 %{buildroot}/usr/lib/tmpfiles.d/
install -m 644 %{SOURCE7} %{buildroot}/usr/lib/tmpfiles.d/krb5.conf
mkdir -p %{buildroot}/%{_datadir}/kerberos/krb5kdc
# Where per-user keytabs live by default.
mkdir -p %{buildroot}/%{_datadir}/kerberos/krb5/user
install -m 600 %{vendorFiles}/kdc.conf %{buildroot}%{_datadir}/kerberos/krb5kdc/
install -m 600 %{vendorFiles}/kadm5.acl %{buildroot}%{_datadir}/kerberos/krb5kdc/
install -m 600 %{vendorFiles}/kadm5.dict %{buildroot}%{_datadir}/kerberos/krb5kdc/

# all libs must have permissions 0755 
for lib in `find %{buildroot}/%{_libdir}/ -type f -name "*.so*"`
do 
  chmod 0755 ${lib} 
done
# and binaries too
chmod 0755 %{buildroot}/usr/lib/mit/bin/ksu
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
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/sbin/
%if 0%{?suse_version} >= 1210
%if 0%{?suse_version} > 1220
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rckadmind
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rckrb5kdc
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rckpropd
%else
ln -s /sbin/service %{buildroot}%{_sbindir}/rckadmind
ln -s /sbin/service %{buildroot}%{_sbindir}/rckrb5kdc
ln -s /sbin/service %{buildroot}%{_sbindir}/rcpropd
%endif
%else
ln -sf ../../etc/init.d/kadmind %{buildroot}/usr/sbin/rckadmind
ln -sf ../../etc/init.d/krb5kdc %{buildroot}/usr/sbin/rckrb5kdc
ln -sf ../../etc/init.d/kpropd %{buildroot}/usr/sbin/rckpropd
%endif
# create links for kinit and klist, because of the java ones
ln -sf ../../usr/lib/mit/bin/kinit   %{buildroot}/usr/bin/kinit
ln -sf ../../usr/lib/mit/bin/klist   %{buildroot}/usr/bin/klist
# install doc
install -d -m 755 %{buildroot}/%{krb5docdir}
install -m 644 %{_builddir}/%{srcRoot}/README %{buildroot}/%{krb5docdir}/README
install -d -m 755 %{buildroot}/%{_datadir}/kerberos/ldap
install -m 644 %{_builddir}/%{srcRoot}/src/plugins/kdb/ldap/libkdb_ldap/kerberos.schema %{buildroot}/%{_datadir}/kerberos/ldap/kerberos.schema
install -m 644 %{_builddir}/%{srcRoot}/src/plugins/kdb/ldap/libkdb_ldap/kerberos.ldif %{buildroot}/%{_datadir}/kerberos/ldap/kerberos.ldif
# link pam-config for su to ksu 
mkdir -p %{buildroot}/etc/pam.d/
install -m 644 %{S:6} %{buildroot}/etc/pam.d/ksu

# cleanup
rm -f  %{buildroot}/usr/share/man/man1/tmac.doc*
rm -f  /usr/share/man/man1/tmac.doc* html/.doctrees/environment.pickle
rm -rf %{buildroot}/usr/lib/mit/share/examples
# manually remove test plugin since configure doesn't support disabling it at build time
rm -f %{buildroot}/%{_libdir}/krb5/plugins/preauth/test.so

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

%files devel
%defattr(-,root,root)
%dir /usr/lib/mit
%dir /usr/lib/mit/bin
%dir /usr/lib/mit/sbin
%dir /usr/lib/mit/share
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
/usr/lib/mit/bin/krb5-config
/usr/lib/mit/sbin/krb5-send-pr
%{_mandir}/man1/krb5-config.1*
%{_datadir}/aclocal/ac_check_krb5.m4

%files -f mit-krb5.lang
%defattr(-,root,root)
%dir %{krb5docdir}
# add plugin directories
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/kdb
%dir %{_libdir}/krb5/plugins/preauth
%dir %{_libdir}/krb5/plugins/libkrb5
%dir %{_libdir}/krb5/plugins/tls
# add log directory
%attr(0700,root,root) %dir /var/log/krb5
%doc %{krb5docdir}/README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/krb5.conf
%dir %{_sysconfdir}/krb5.conf.d
%attr(0644,root,root) %config /etc/profile.d/krb5*
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
%defattr(-,root,root)
%attr(0700,root,root) %dir /var/log/krb5
%config(noreplace) %{_sysconfdir}/logrotate.d/krb5-server
%if 0%{?suse_version} >= 1210
%{_unitdir}/kadmind.service
%{_unitdir}/krb5kdc.service
%{_unitdir}/kpropd.service
%{_libexecdir}/tmpfiles.d/krb5.conf
%else
%{_sysconfdir}/init.d/kadmind
%{_sysconfdir}/init.d/krb5kdc
%{_sysconfdir}/init.d/kpropd
%endif
%dir %{krb5docdir}
%dir /usr/lib/mit
%dir /usr/lib/mit/sbin
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
/usr/sbin/rc*
/usr/lib/mit/sbin/kadmin.local
/usr/lib/mit/sbin/kadmind
/usr/lib/mit/sbin/kpropd
/usr/lib/mit/sbin/kproplog
/usr/lib/mit/sbin/kprop
/usr/lib/mit/sbin/kdb5_util
/usr/lib/mit/sbin/krb5kdc
/usr/lib/mit/sbin/gss-server
/usr/lib/mit/sbin/sim_server
/usr/lib/mit/sbin/sserver
/usr/lib/mit/sbin/uuserver
%{_libdir}/krb5/plugins/kdb/db2.so
%{_mandir}/man5/kdc.conf.5*
%{_mandir}/man5/kadm5.acl.5*
%{_mandir}/man8/kadmind.8*
%{_mandir}/man8/kadmin.local.8*
%{_mandir}/man8/kpropd.8*
%{_mandir}/man8/kprop.8*
%{_mandir}/man8/kproplog.8.gz
%{_mandir}/man8/kdb5_util.8*
%{_mandir}/man8/krb5kdc.8*
%{_mandir}/man8/sserver.8*

%files client
%defattr(-,root,root)
%dir /usr/lib/mit
%dir /usr/lib/mit/bin
%dir /usr/lib/mit/sbin
%attr(0644,root,root) %config(noreplace) /etc/pam.d/ksu
/usr/lib/mit/bin/kvno
/usr/lib/mit/bin/kinit
/usr/lib/mit/bin/kdestroy
/usr/lib/mit/bin/kpasswd
/usr/lib/mit/bin/klist
/usr/lib/mit/bin/kadmin
/usr/lib/mit/bin/ktutil
/usr/lib/mit/bin/k5srvutil
/usr/lib/mit/bin/gss-client
/usr/lib/mit/bin/ksu
/usr/lib/mit/bin/sclient
/usr/lib/mit/bin/sim_client
/usr/lib/mit/bin/uuclient
/usr/lib/mit/bin/kswitch
/usr/bin/kinit
/usr/bin/klist
%{_mandir}/man1/kvno.1*
%{_mandir}/man1/kinit.1*
%{_mandir}/man1/kdestroy.1*
%{_mandir}/man1/kpasswd.1*
%{_mandir}/man1/klist.1*
%{_mandir}/man1/kadmin.1*
%{_mandir}/man1/ktutil.1*
%{_mandir}/man1/k5srvutil.1*
%{_mandir}/man1/kswitch.1*
%{_mandir}/man5/krb5.conf.5*
%{_mandir}/man5/.k5login.5*
%{_mandir}/man5/.k5identity.5*
%{_mandir}/man5/k5identity.5*
%{_mandir}/man5/k5login.5*
%{_mandir}/man1/ksu.1.gz
%{_mandir}/man1/sclient.1.gz
%{_mandir}/man7/kerberos.7.gz

%files plugin-kdb-ldap
%defattr(-,root,root)
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/kdb
%dir /usr/lib/mit/sbin/
%dir %{_datadir}/kerberos
%dir %{_datadir}/kerberos/ldap
%config %{_datadir}/kerberos/ldap/kerberos.schema
%config %{_datadir}/kerberos/ldap/kerberos.ldif
%{_libdir}/krb5/plugins/kdb/kldap.so
/usr/lib/mit/sbin/kdb5_ldap_util
%{_libdir}/libkdb_ldap*
%{_mandir}/man8/kdb5_ldap_util.8*

%files plugin-preauth-pkinit
%defattr(-,root,root)
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/preauth
%{_libdir}/krb5/plugins/preauth/pkinit.so

%files plugin-preauth-otp
%defattr(-,root,root)
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/preauth
%{_libdir}/krb5/plugins/preauth/otp.so

%files plugin-preauth-spake
%defattr(-,root,root)
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/preauth
%{_libdir}/krb5/plugins/preauth/spake.so

%changelog
