#
# spec file for package 389-ds
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


# bcond is confusingly backwards to what you expect - without means
#  to ENABLE the option, with means to DISABLE it.
%if (0%{?sle_version} > 150099) || (0%{?suse_version} > 1549)
%bcond_without lib389
%else
%bcond_with    lib389
%endif

%if (0%{?sle_version} > 150299) || (0%{?suse_version} > 1549)
%bcond_without rust
%else
%bcond_with    rust
%endif

%define use_python python3
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}

# Home directory
%global pkgname   dirsrv
%global groupname %{pkgname}.target

%define homedir %{_localstatedir}/lib/dirsrv
%define logdir %{_localstatedir}/log/dirsrv
%define lockdir %{_localstatedir}/lock/dirsrv
# User and group name that own the home directory
%define user_group dirsrv
%ifnarch s390x s390 ppc64 ppc64le
%global use_tcmalloc 1
%else
%global use_tcmalloc 0
%endif
%define svrcorelib libsvrcore0

Name:           389-ds
Version:        1.4.4.6~git0.71baa8cb2
Release:        0
Summary:        389 Directory Server
License:        GPL-3.0-or-later AND MPL-2.0
Group:          Productivity/Networking/LDAP/Servers
URL:            https://pagure.io/389-ds-base
Source:         389-ds-base-%{version}.tar.bz2
Source1:        extra-schema.tgz
Source2:        LICENSE.openldap
%if %{with rust}
Source3:        vendor.tar.xz
# Source4:        cargo_config
%endif
Source9:        %{name}-rpmlintrc
Source10:       %{user_group}-user.conf
# 389-ds does not support i686
ExcludeArch:    %ix86
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cracklib-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel >= 4.5
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  krb5-devel
BuildRequires:  libcmocka-devel
BuildRequires:  libevent-devel
BuildRequires:  libtalloc-devel
BuildRequires:  libtevent-devel
BuildRequires:  libtool
BuildRequires:  sysuser-tools
# net-snmp-devel is needed to build the snmp ldap-agent
BuildRequires:  net-snmp-devel >= 5.1.2
BuildRequires:  openldap2-devel
# pam-devel is required by the pam passthru auth plug-in
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
%if %{with lib389}
BuildRequires:  %{python_module argcomplete}
BuildRequires:  %{python_module argparse-manpage}
BuildRequires:  %{python_module ldap >= 3}
BuildRequires:  %{python_module pyasn1-modules}
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module six}
%endif
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(systemd)
%if %{use_tcmalloc}
BuildRequires:  pkgconfig(libtcmalloc)
%endif
BuildRequires:  rsync
%if %{with rust}
BuildRequires:  cargo
BuildRequires:  rust
%endif
Requires:       %{_sbindir}/service
Requires:       acl
# This is a requirement as it's the only known "safe" method of
# plaintext password authentication to ldap, beside the use of
# ldaps.
Requires:       cyrus-sasl-plain
Requires:       db-utils
%if %{with lib389}
Requires:       lib389 = %{version}
%else
Requires:       bind-utils
Requires:       perl(Mozilla::LDAP::API)
Requires:       perl(Mozilla::LDAP::Conn)
Requires:       perl(Mozilla::LDAP::Entry)
Requires:       perl(Mozilla::LDAP::LDIF)
Requires:       perl(Mozilla::LDAP::Utils)
Requires:       perl(NetAddr::IP)
Requires:       perl(Socket6)
%endif
# Needed for creating the ccache and some GSSAPI steps in sasl
Requires:       krb5
%sysusers_requires
# 389-ds does not directly require gssapi, but it is needed for
# ldap gssapi auth, so we recommend it.
# This used to be a requirement, but it's actually optional.
Recommends:     cyrus-sasl-gssapi
# This is required by rfc2831, however it's also horribly insecure
# and requires insecure password storage. We really should remove
# it.
Recommends:     cyrus-sasl-digestmd5

Requires(post): fillup
Requires(pre):  shadow
PreReq:         permissions
Obsoletes:      389-ds-base < %{version}-%{release}
Provides:       389-ds-base = %{version}-%{release}
%{?systemd_ordering}

%description
389 Directory Server is a full-featured LDAPv3 compliant server. In
addition to the standard LDAPv3 operations, it supports multi-master
replication, fully online configuration and administration, chaining,
virtual attributes, access control directives in the data, Virtual
List View, server-side sorting, SASL, TLS/SSL, and many other
features. (The server started out as Netscape Directory Server.)

%package devel
Summary:        Development files for the 389 Directory Server
License:        GPL-3.0-or-later AND MPL-2.0
Group:          Development/Libraries/C and C++
Provides:       svrcore-devel = 4.1.4
Obsoletes:      svrcore-devel < 4.1.4
Requires:       %{name} = %{version}
Requires:       %{svrcorelib} = %{version}
Requires:       libevent-devel
Requires:       openldap2-devel
Requires:       pkgconfig
Requires:       pkgconfig(nspr)
Requires:       pkgconfig(nss)
Requires:       pkgconfig(systemd)

%description devel
389 Directory Server is a full-featured LDAPv3 compliant server. In
addition to the standard LDAPv3 operations, it supports multi-master
replication, fully online configuration and administration, chaining,
virtual attributes, access control directives in the data, Virtual
List View, server-side sorting, SASL, TLS/SSL, and many other
features.

This package contains the development files for 389DS.

%package          snmp
Summary:        SNMP Agent for 389 Directory Server
License:        GPL-3.0-or-later AND MPL-2.0
Group:          System/Daemons
Requires:       %{name} = %{version}

Obsoletes:      %{name} <= 1.3.6.2

%description      snmp
SNMP Agent for the 389 Directory Server base package.

%if %{with lib389}
%package -n lib389
Summary:        389 Directory Server administration tools and library
License:        GPL-3.0-or-later AND MPL-2.0
Group:          Development/Languages/Python
Requires:       %{use_python}-argcomplete
Requires:       %{use_python}-argparse-manpage
Requires:       %{use_python}-distro
Requires:       %{use_python}-ldap >= 3.0
Requires:       %{use_python}-pyasn1
Requires:       %{use_python}-pyasn1-modules
Requires:       %{use_python}-python-dateutil
Requires:       %{use_python}-six
Requires:       krb5-client
Requires:       mozilla-nss-tools
# We recommend this here as a supplementary tool for ldap
# server interaction, but it's in no way required.
Recommends:     openldap2-client
# These are recommended if you have selinux on your system
# to allow some supplementary automated interactions during
# setup, but it's not required.
Recommends:     python3-selinux
Recommends:     python3-policycoreutils

Provides:       python3-lib389 = %{version}-%{release}
Obsoletes:      python-lib389 < %{version}-%{release}
Obsoletes:      python3-lib389 < %{version}-%{release}

%description -n lib389
Python library for interacting with and administering 389
Directory Server instances locally or remotely.
%endif

%package -n %{svrcorelib}
Summary:        Secure PIN handling using NSS crypto
License:        MPL-2.0
Group:          System/Libraries

%description -n %{svrcorelib}
svrcore provides applications with several ways to handle secure PIN storage
e.g. in an application that must be restarted, but needs the PIN to unlock
the private key and other crypto material, without user intervention.  svrcore
uses the facilities provided by NSS.

%prep
# Extract the 389-ds sources.
%setup -q -a 1 -n %{name}-base-%{version}

# Extract the vendor.tar.gz. The -D -T here prevents removal of the sources
# from the previous setup step.
%if %{with rust}
# mkdir .cargo
# cp %{SOURCE4} .cargo/config
%setup -q -n %{name}-base-%{version} -D -T -a 3
%endif

%build
%sysusers_generate_pre %{SOURCE10} %{user_group}
# Make sure python3 is used in shebangs
# FIX ME!!  This should be fixed in the source code !!!
sed -r -i '1s|^#!\s*%{_bindir}.*python.*|#!%{_bindir}/%{use_python}|' ldap/admin/src/scripts/{*.py,ds-replcheck} src/lib389/cli/ds*

# TODO:
# seems to have no effect --enable-perl \
# warning that it might lead to instabilities --with-journald \
touch docs/custom.css
autoreconf -fi
export CFLAGS="%{optflags}" # -std=gnu99"
%configure \
  %if 0%{?suse_version} >= 1330
  --enable-gcc-security \
  %endif
  --enable-autobind \
  --enable-auto-dn-suffix \
  --with-openldap \
  --enable-cmocka \
  %if %{use_tcmalloc}
  --enable-tcmalloc \
  %endif
  --with-selinux \
  %if %{with rust}
  --enable-rust-offline \
  %endif
  %if %{with lib389}
  --disable-perl \
  %else
  --enable-perl \
  --with-perldir=%{_bindir} \
  %endif
  --libexecdir=%{_prefix}/lib/dirsrv/ \
  --with-pythonexec="%{_bindir}/%{use_python}" \
  --with-systemd \
  --with-systemdgroupname=%{groupname} \
  --with-systemdsystemunitdir="%{_unitdir}" \
  --with-systemdsystemconfdir="%{_sysconfdir}/systemd/system" \
  --with-tmpfiles-d="%{_sysconfdir}/tmpfiles.d" \
  --with-systemdgroupname=dirsrv.target \

export XCFLAGS="$CFLAGS"
make %{?_smp_mflags}
#make setup.py
%if %{with lib389}
pushd src/lib389
%python_build
popd
%endif

%install
%make_install
%if %{with lib389}
pushd src/lib389
%python_install
mv %{buildroot}/usr/libexec/dirsrv/dscontainer %{buildroot}%{_prefix}/lib/dirsrv/
rmdir %{buildroot}/usr/libexec/dirsrv/
popd
%endif

cp -r man/man3 %{buildroot}%{_mandir}/man3

install -D -d -m 0750 %{buildroot}%{homedir}
mkdir -p %{buildroot}%{logdir}
mkdir -p %{buildroot}%{homedir}
mkdir -p %{buildroot}%{lockdir}
mkdir -p %{buildroot}%{_sysusersdir}

#remove libtool archives and static libs
find %{buildroot} -type f -name "*.la" -delete -print

# make sure perl scripts have a proper shebang
%if ! %{with lib389}
sed -i -e 's|#{{PERL-EXEC}}|#!%{_bindir}/perl|' %{buildroot}%{_datadir}/%{pkgname}/script-templates/template-*.pl
%endif

# install extra schema files
cp -R extra-schema "%{buildroot}/%{_datadir}/dirsrv/"

# bring OpenLDAP copyright notice here because it is referenced by several extra schema files
cp %{SOURCE2} ./

rm -rv %{buildroot}/usr/share/cockpit/
rm -rv %{buildroot}/usr/share/metainfo/389-console/
mv src/svrcore/README{,.svrcore}
mv src/svrcore/LICENSE{,.svrcore}
install -m 0644 %{SOURCE10} %{buildroot}%{_sysusersdir}/

%pre -f %{user_group}.pre

%post
%fillup_only -n dirsrv
%set_permissions %{_sbindir}/ns-slapd

%verifyscript
%verify_permissions -e %{_sbindir}/ns-slapd

%postun
output=/dev/null
# reload to pick up any changes to systemd files
/bin/systemctl daemon-reload >$output 2>&1 || :
# reload to pick up any shared lib changes
%fillup_only -n dirsrv
%fillup_only -n dirsrv.systemd
exit 0

%preun
%service_del_preun %{pkgname}.target

%pre snmp
%service_add_pre dirsrv-snmp.service

%post snmp
%service_add_post %{pkgname}-snmp.service

%preun snmp
%service_del_preun %{pkgname}-snmp.service

%postun snmp
%service_del_postun %{pkgname}-snmp.service

%post -n %{svrcorelib} -p /sbin/ldconfig

%postun -n %{svrcorelib} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README*
%license LICENSE LICENSE.openldap
%{_sysusersdir}/%{user_group}-user.conf
%dir %attr(-,%{user_group},%{user_group}) %{homedir}
%dir %attr(-,%{user_group},%{user_group}) %{logdir}
%config(noreplace) %{_sysconfdir}/dirsrv/config/*
%config(noreplace) %{_sysconfdir}/dirsrv/schema/*
%{_datadir}/dirsrv
%dir %{_libdir}/dirsrv
%dir %{_libdir}/dirsrv/*
%dir %{_sysconfdir}/dirsrv
%dir %{_sysconfdir}/dirsrv/config
%dir %{_sysconfdir}/dirsrv/schema
%{_libdir}/dirsrv/libns-dshttpd-*.so
%{_libdir}/dirsrv/librewriters.so
%if ! %{with lib389}
%{_libdir}/dirsrv/perl/*.pm
%endif
%{_libdir}/dirsrv/plugins/*.so
%{_libdir}/dirsrv/python/*.py
%{_libdir}/dirsrv/*.so.*
%exclude %{_mandir}/man1/ldap-agent*
%{_mandir}/man1/*
%{_mandir}/man5/*
%if %{with lib389}
%{_mandir}/man8/ns-slapd.8.gz
%{_mandir}/man8/openldap_to_ds.8.gz

# With lib389 we don't package all the man pages for deprecated commands. Upstream needs to remove
# these from the build with --disable-perl flag set.
# These are excluded now
%exclude %{_mandir}/man8/bak2db.8.gz
%exclude %{_mandir}/man8/bak2db.pl.8.gz
%exclude %{_mandir}/man8/cleanallruv.pl.8.gz
%exclude %{_mandir}/man8/db2bak.8.gz
%exclude %{_mandir}/man8/db2bak.pl.8.gz
%exclude %{_mandir}/man8/db2index.8.gz
%exclude %{_mandir}/man8/db2index.pl.8.gz
%exclude %{_mandir}/man8/db2ldif.8.gz
%exclude %{_mandir}/man8/db2ldif.pl.8.gz
%exclude %{_mandir}/man8/dbmon.sh.8.gz
%exclude %{_mandir}/man8/dbverify.8.gz
%exclude %{_mandir}/man8/dn2rdn.8.gz
%exclude %{_mandir}/man8/fixup-linkedattrs.pl.8.gz
%exclude %{_mandir}/man8/fixup-memberof.pl.8.gz
%exclude %{_mandir}/man8/ldif2db.8.gz
%exclude %{_mandir}/man8/ldif2db.pl.8.gz
%exclude %{_mandir}/man8/ldif2ldap.8.gz
%exclude %{_mandir}/man8/migrate-ds.pl.8.gz
%exclude %{_mandir}/man8/monitor.8.gz
%exclude %{_mandir}/man8/ns-accountstatus.pl.8.gz
%exclude %{_mandir}/man8/ns-activate.pl.8.gz
%exclude %{_mandir}/man8/ns-inactivate.pl.8.gz
%exclude %{_mandir}/man8/ns-newpwpolicy.pl.8.gz
%exclude %{_mandir}/man8/remove-ds.pl.8.gz
%exclude %{_mandir}/man8/restart-dirsrv.8.gz
%exclude %{_mandir}/man8/restoreconfig.8.gz
%exclude %{_mandir}/man8/saveconfig.8.gz
%exclude %{_mandir}/man8/schema-reload.pl.8.gz
%exclude %{_mandir}/man8/setup-ds.pl.8.gz
%exclude %{_mandir}/man8/start-dirsrv.8.gz
%exclude %{_mandir}/man8/status-dirsrv.8.gz
%exclude %{_mandir}/man8/stop-dirsrv.8.gz
%exclude %{_mandir}/man8/suffix2instance.8.gz
%exclude %{_mandir}/man8/syntax-validate.pl.8.gz
%exclude %{_mandir}/man8/upgradedb.8.gz
%exclude %{_mandir}/man8/upgradednformat.8.gz
%exclude %{_mandir}/man8/usn-tombstone-cleanup.pl.8.gz
%exclude %{_mandir}/man8/verify-db.pl.8.gz
%exclude %{_mandir}/man8/vlvindex.8.gz
%else
%{_mandir}/man8/*
%endif
%{_bindir}/*
# TODO: audit bug running https://bugzilla.opensuse.org/show_bug.cgi?id=1111564
# This also needs a lot more work on the service file
#attr(750,root,dirsrv) #caps(CAP_NET_BIND_SERVICE=pe) #{_sbindir}/ns-slapd
%verify(not caps) %attr(755,root,root) %{_sbindir}/ns-slapd
%{_sbindir}/openldap_to_ds
%if ! %{with lib389}
%{_sbindir}/bak2db
%{_sbindir}/bak2db.pl
%{_sbindir}/cleanallruv.pl
%{_sbindir}/db2bak
%{_sbindir}/db2bak.pl
%{_sbindir}/db2index
%{_sbindir}/db2index.pl
%{_sbindir}/db2ldif
%{_sbindir}/db2ldif.pl
%{_sbindir}/dbmon.sh
%{_sbindir}/dbverify
%{_sbindir}/dn2rdn
%{_sbindir}/fixup-linkedattrs.pl
%{_sbindir}/fixup-memberof.pl
%{_sbindir}/ldif2db
%{_sbindir}/ldif2db.pl
%{_sbindir}/ldif2ldap
%{_sbindir}/migrate-ds.pl
%{_sbindir}/monitor
%{_sbindir}/ns-accountstatus.pl
%{_sbindir}/ns-activate.pl
%{_sbindir}/ns-inactivate.pl
%{_sbindir}/ns-newpwpolicy.pl
%{_sbindir}/remove-ds.pl
%{_sbindir}/restart-dirsrv
%{_sbindir}/restoreconfig
%{_sbindir}/saveconfig
%{_sbindir}/schema-reload.pl
%{_sbindir}/setup-ds.pl
%{_sbindir}/start-dirsrv
%{_sbindir}/status-dirsrv
%{_sbindir}/stop-dirsrv
%{_sbindir}/suffix2instance
%{_sbindir}/syntax-validate.pl
%{_sbindir}/upgradedb
%{_sbindir}/upgradednformat
%{_sbindir}/usn-tombstone-cleanup.pl
%{_sbindir}/verify-db.pl
%{_sbindir}/vlvindex
%endif
%{_unitdir}/dirsrv@.service
%{_unitdir}/dirsrv.target
%exclude %{_unitdir}/dirsrv@.service.d/custom.conf
%{_prefix}/lib/dirsrv/ds_systemd_ask_password_acl
# This has to be hardcoded to /lib - $libdir changes between lib/lib64, but
# sysctl.d is always in /lib.
%{_prefix}/lib/sysctl.d/*
%dir %{_datadir}/gdb/auto-load/usr/sbin/
%{_datadir}/gdb/auto-load/usr/sbin/ns-slapd-gdb.py

%files devel
%defattr(-,root,root)
%doc README*
%doc src/svrcore/README.svrcore
%license LICENSE
%license src/svrcore/LICENSE.svrcore
%{_mandir}/man3/*
%{_includedir}/dirsrv
%{_includedir}/svrcore.h
%{_libdir}/libsvrcore.so
%{_libdir}/dirsrv/libns-dshttpd.so
%{_libdir}/dirsrv/libsds.so
%{_libdir}/dirsrv/libslapd.so
%{_libdir}/dirsrv/libldaputil.so
%{_libdir}/pkgconfig/dirsrv.pc
%{_libdir}/pkgconfig/libsds.pc
%{_libdir}/pkgconfig/svrcore.pc

%files -n %{svrcorelib}
%defattr(-,root,root,-)
%license src/svrcore/LICENSE*
%{_libdir}/libsvrcore.so.*

%files snmp
%defattr(-,root,root,-)
%license LICENSE LICENSE.GPLv3+ LICENSE.openssl
# TODO: README.devel
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/ldap-agent.conf
%{_sbindir}/ldap-agent*
%{_mandir}/man1/ldap-agent.1*
%{_unitdir}/%{pkgname}-snmp.service

%if %{with lib389}
%files -n lib389
%defattr(-,root,root,-)
%license src/lib389/LICENSE
%doc src/lib389/README*
%{_sbindir}/dsconf
%{_sbindir}/dscreate
%{_sbindir}/dsctl
%{_sbindir}/dsidm
%dir %{_prefix}/lib/dirsrv/
%{_prefix}/lib/dirsrv/dscontainer
%{_mandir}/man8/dsconf.8.gz
%{_mandir}/man8/dscreate.8.gz
%{_mandir}/man8/dsctl.8.gz
%{_mandir}/man8/dsidm.8.gz
/usr/lib/python*/site-packages/lib389*
%endif

%changelog
