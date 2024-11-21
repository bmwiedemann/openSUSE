#
# spec file for package 389-ds
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


%define use_python python3
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}

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
Version:        3.1.1~git13.a9c7ff9
Release:        0
Summary:        389 Directory Server
License:        GPL-3.0-or-later AND MPL-2.0
Group:          Productivity/Networking/LDAP/Servers
URL:            https://pagure.io/389-ds-base
Source:         389-ds-base-%{version}.tar.zst
Source1:        extra-schema.tgz
Source2:        LICENSE.openldap
Source3:        vendor.tar.zst
Source4:        supportutils-plugin-dirsrv.tar.zst
Source5:        70yast.ldif
Source9:        %{name}-rpmlintrc
Source10:       %{user_group}-user.conf
Source11:       krbkdcbefore.conf
Patch0:         389-ds-link-icu-uc.patch
# 389-ds does not support i686
ExcludeArch:    %ix86
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cracklib-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel >= 4.5
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  krb5-devel
BuildRequires:  libcmocka-devel
BuildRequires:  libevent-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libtalloc-devel
BuildRequires:  libtevent-devel
BuildRequires:  libtool
BuildRequires:  lmdb-devel
BuildRequires:  procps
BuildRequires:  sysuser-tools
# net-snmp-devel is needed to build the snmp ldap-agent
BuildRequires:  net-snmp-devel >= 5.1.2
BuildRequires:  openldap2-devel
# Libressl is incompatible with our rust cryptographic needs.
BuildRequires:  openssl-devel
# pam-devel is required by the pam passthru auth plug-in
BuildRequires:  %use_python-argcomplete
BuildRequires:  %use_python-argparse-manpage
BuildRequires:  %use_python-cryptography
BuildRequires:  %use_python-devel
BuildRequires:  %use_python-ldap >= 3
BuildRequires:  %use_python-pyasn1
BuildRequires:  %use_python-pyasn1-modules
BuildRequires:  %use_python-python-dateutil
BuildRequires:  %use_python-setuptools
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  zlib-devel
BuildRequires:  zstd
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(systemd)
%if %{use_tcmalloc}
BuildRequires:  pkgconfig(libtcmalloc)
%endif
BuildRequires:  cargo
BuildRequires:  rsync
BuildRequires:  rust
Requires:       %{_sbindir}/service
Requires:       acl
# This is a requirement as it's the only known "safe" method of
# plaintext password authentication to ldap, beside the use of
# ldaps.
Requires:       cyrus-sasl-plain
Requires:       db-utils
Requires:       lib389 = %{version}
# Needed for creating the ccache and some GSSAPI steps in sasl
Requires:       krb5
%sysusers_requires
# 389-ds does not directly require gssapi, but it is needed for
# ldap gssapi auth, so we recommend it.
# This used to be a requirement, but it's actually optional.
Recommends:     cyrus-sasl-gssapi

Requires(post): fillup
Requires(post): permissions
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

%package        snmp
Summary:        SNMP Agent for 389 Directory Server
License:        GPL-3.0-or-later AND MPL-2.0
Group:          System/Daemons
Requires:       %{name} = %{version}

Obsoletes:      %{name} <= 1.3.6.2

%description    snmp
SNMP Agent for the 389 Directory Server base package.

%package -n lib389
Summary:        389 Directory Server administration tools and library
License:        GPL-3.0-or-later AND MPL-2.0
Group:          Development/Languages/Python
Requires:       %{use_python}-argcomplete
Requires:       %{use_python}-argparse-manpage
Requires:       %{use_python}-cryptography
Requires:       %{use_python}-distro
Requires:       %{use_python}-ldap >= 3.0
Requires:       %{use_python}-pyasn1
Requires:       %{use_python}-pyasn1-modules
Requires:       %{use_python}-python-dateutil
Requires:       %{use_python}-python-slugify
Requires:       iproute2
Requires:       krb5-client
Requires:       mozilla-nss-tools
# Tools like dscreate would call out to /usr/bin/openssl
Requires:       openssl(cli)
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
%setup -q -n %{name}-base-%{version} -D -T -a 3
# Setup support utils
%setup -q -n %{name}-base-%{version} -D -T -a 4

%autopatch -p1

# Debugging for if anything goes south.
lscpu
free -h
df -h

%build
%sysusers_generate_pre %{SOURCE10} %{user_group} %{user_group}-user.conf
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
  --enable-rust-offline \
  --disable-perl \
  --libexecdir=%{_prefix}/lib/dirsrv/ \
  --with-pythonexec="%{_bindir}/%{use_python}" \
  --with-systemd \
  --with-systemdgroupname=dirsrv.target \
  --with-systemdsystemunitdir="%{_unitdir}" \
  --with-systemdsystemconfdir="%{_sysconfdir}/systemd/system" \
  --with-tmpfiles-d="%{_sysconfdir}/tmpfiles.d" \
  --with-systemdgroupname=dirsrv.target \

export XCFLAGS="$CFLAGS"
make src/lib389/setup.py
make %{?_smp_mflags}
pushd src/lib389
%python3_build
popd

%install
%make_install
pushd src/lib389
%python3_install
mv %{buildroot}/usr/libexec/dirsrv/dscontainer %{buildroot}%{_prefix}/lib/dirsrv/
rmdir %{buildroot}/usr/libexec/dirsrv/
popd

cp -r man/man3 %{buildroot}%{_mandir}/man3

install -D -d -m 0750 %{buildroot}%{homedir}
mkdir -p %{buildroot}%{logdir}
mkdir -p %{buildroot}%{homedir}
mkdir -p %{buildroot}%{lockdir}
mkdir -p %{buildroot}%{_sysusersdir}
mkdir -p %{buildroot}/usr/lib/supportconfig/plugins/
mkdir -p %{buildroot}%{_unitdir}/dirsrv@.service.d/

#remove libtool archives and static libs
find %{buildroot} -type f -name "*.la" -delete -print

# install extra schema files
cp -R extra-schema "%{buildroot}/%{_datadir}/dirsrv/"
cp %{SOURCE5} "%{buildroot}/%{_datadir}/dirsrv/schema/"

# Install the support utils plugin.
cp supportutils-plugin-dirsrv*/dirsrv "%{buildroot}/usr/lib/supportconfig/plugins/dirsrv"

# bring OpenLDAP copyright notice here because it is referenced by several extra schema files
cp %{SOURCE2} ./

rm -rv %{buildroot}/usr/share/cockpit/
rm -rv %{buildroot}/usr/share/metainfo/389-console/
mv src/svrcore/README{,.svrcore}
mv src/svrcore/LICENSE{,.svrcore}
install -m 0644 %{SOURCE10} %{buildroot}%{_sysusersdir}/
install -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/dirsrv@.service.d/krbkdcbefore.conf

# For the purposes of our krb integration, we enable this by default.
mv %{buildroot}%{_datadir}/dirsrv/data/60kerberos.ldif %{buildroot}%{_datadir}/dirsrv/schema/60kerberos.ldif

# Sssshhh duplicate checker ...
%fdupes %{buildroot}/%{_prefix}

%pre -f %{user_group}.pre
%service_add_pre dirsrv.target

%post
%service_add_post dirsrv.target
%fillup_only -n dirsrv
%set_permissions %{_sbindir}/ns-slapd

%verifyscript
%verify_permissions -e %{_sbindir}/ns-slapd

%preun
%service_del_preun dirsrv.target

%postun
%service_del_postun dirsrv.target
output=/dev/null
# reload to pick up any changes to systemd files
/bin/systemctl daemon-reload >$output 2>&1 || :
# reload to pick up any shared lib changes
%fillup_only -n dirsrv
%fillup_only -n dirsrv.systemd
exit 0

%pre snmp
%service_add_pre dirsrv-snmp.service

%post snmp
%service_add_post dirsrv-snmp.service

%preun snmp
%service_del_preun dirsrv-snmp.service

%postun snmp
%service_del_postun dirsrv-snmp.service

%post -n %{svrcorelib} -p /sbin/ldconfig

%postun -n %{svrcorelib} -p /sbin/ldconfig

%files
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
%{_libdir}/dirsrv/librewriters.so
%{_libdir}/dirsrv/plugins/*.so
%{_libdir}/dirsrv/python/*.py
%{_libdir}/dirsrv/*.so.*
%exclude %{_mandir}/man1/ldap-agent*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/ns-slapd.8.gz
%{_mandir}/man8/openldap_to_ds.8.gz
%{_bindir}/*
# TODO: audit bug running https://bugzilla.opensuse.org/show_bug.cgi?id=1111564
# This also needs a lot more work on the service file
#attr(750,root,dirsrv) #caps(CAP_NET_BIND_SERVICE=pe) #{_sbindir}/ns-slapd
%verify(not caps) %attr(755,root,root) %{_sbindir}/ns-slapd
%{_sbindir}/openldap_to_ds
%{_unitdir}/dirsrv@.service
%dir %{_unitdir}/dirsrv@.service.d
%{_unitdir}/dirsrv@.service.d/krbkdcbefore.conf
%{_unitdir}/dirsrv.target
%exclude %{_unitdir}/dirsrv@.service.d/custom.conf
%{_prefix}/lib/dirsrv/ds_systemd_ask_password_acl
%{_prefix}/lib/dirsrv/ds_selinux_restorecon.sh
# This has to be hardcoded to /lib - $libdir changes between lib/lib64, but
# sysctl.d is always in /lib.
%{_prefix}/lib/sysctl.d/*
%dir %{_datadir}/gdb/auto-load/usr/sbin/
%{_datadir}/gdb/auto-load/usr/sbin/ns-slapd-gdb.py
%dir %{_prefix}/lib/supportconfig
%dir %{_prefix}/lib/supportconfig/plugins
%attr(750,root,root) %{_prefix}/lib/supportconfig/plugins/dirsrv

%files devel
%doc README*
%doc src/svrcore/README.svrcore
%license LICENSE
%license src/svrcore/LICENSE.svrcore
%{_mandir}/man3/*
%{_includedir}/dirsrv
%{_includedir}/svrcore.h
%{_libdir}/libsvrcore.so
%{_libdir}/dirsrv/libslapd.so
%{_libdir}/dirsrv/libns-dshttpd.so
%{_libdir}/dirsrv/libldaputil.so
%{_libdir}/pkgconfig/dirsrv.pc
%{_libdir}/pkgconfig/svrcore.pc

%files -n %{svrcorelib}
%license src/svrcore/LICENSE*
%{_libdir}/libsvrcore.so.*

%files snmp
%license LICENSE LICENSE.GPLv3+ LICENSE.openssl
# TODO: README.devel
%config(noreplace)%{_sysconfdir}/dirsrv/config/ldap-agent.conf
%{_sbindir}/ldap-agent*
%{_mandir}/man1/ldap-agent.1*
%{_unitdir}/dirsrv-snmp.service

%files -n lib389
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
%{python3_sitelib}/lib389*

%changelog
