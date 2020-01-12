#
# spec file for package openldap2
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

%define run_test_suite 0
%define version_main 2.4.48

%if %{suse_version} >= 1310 && %{suse_version} != 1315
%define  _rundir /run/slapd
%else
%define  _rundir /var/run/slapd
%endif

%define name_ppolicy_check_module ppolicy-check-password
%define version_ppolicy_check_module 1.2
%define ppolicy_docdir %{_docdir}/openldap-%{name_ppolicy_check_module}-%{version_ppolicy_check_module}

Name:           openldap2
Summary:        An open source implementation of the Lightweight Directory Access Protocol
License:        OLDAP-2.8
Group:          Productivity/Networking/LDAP/Servers
Version:        %{version_main}
Release:        0
Url:            http://www.openldap.org
Source:         ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/openldap-%{version_main}.tgz
Source1:        slapd.conf
Source2:        slapd.conf.olctemplate
Source3:        DB_CONFIG
Source4:        sasl-slapd.conf
Source5:        README.module-loading
Source6:        schema2ldif
Source7:        baselibs.conf
Source9:        addonschema.tar.gz
Source12:       slapd.conf.example
Source13:       start
Source14:       slapd.service
Source16:       sysconfig.openldap
Source17:       openldap_update_modules_path.sh
Source18:       openldap2.conf
Patch1:         0001-ITS-8866-slapo-unique-to-return-filter-used-in-diagn.patch
Patch3:         0003-LDAPI-socket-location.dif
Patch5:         0005-pie-compile.dif
Patch7:         0007-Recover-on-DB-version-change.dif
Patch8:         0008-In-monitor-backend-do-not-return-Connection0-entries.patch
Patch9:         0009-Fix-ldap-host-lookup-ipv6.patch
Patch11:        0011-openldap-re24-its7796.patch
Patch13:        0013_openldap-its9124_fix_crash_with_cancel_exop.patch
Patch15:        openldap-r-only.dif
Patch16:        0016-Clear-shared-key-only-in-close-function.patch
Source200:      %{name_ppolicy_check_module}-%{version_ppolicy_check_module}.tar.gz
Source201:      %{name_ppolicy_check_module}.Makefile
Source202:      %{name_ppolicy_check_module}.conf
Source203:      %{name_ppolicy_check_module}.5
Patch200:       0200-Fix-incorrect-calculation-of-consecutive-number-of-c.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
BuildRequires:  groff
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  openslp-devel
BuildRequires:  unixODBC-devel
%if %{suse_version} >= 1310 && %{suse_version} != 1315
# avoid cycle with krb5
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(systemd)
%if %{suse_version} < 1500
%{?systemd_requires}
%endif
%endif
Requires:       libldap-2_4-2 = %{version_main}
Recommends:     cyrus-sasl
Conflicts:      openldap
PreReq:         %fillup_prereq /usr/sbin/useradd /usr/sbin/groupadd /usr/bin/grep

%description
OpenLDAP is a client and server reference implementation of the
Lightweight Directory Access Protocol v3 (LDAPv3).

The server provides several database backends and overlays.

%package back-perl
Summary:        OpenLDAP Perl Back-End
Group:          Productivity/Networking/LDAP/Servers
Requires:       openldap2 = %{version_main}
Requires:       perl = %{perl_version}

%description back-perl
The OpenLDAP Perl back-end allows you to execute Perl code specific to
different LDAP operations.

%package back-sock
Summary:        OpenLDAP Socket Back-End
Group:          Productivity/Networking/LDAP/Servers
Requires:       openldap2 = %{version_main}
Provides:       openldap2:/usr/share/man/man5/slapd-sock.5.gz

%description back-sock
The OpenLDAP socket back-end allows you to handle LDAP requests and
results with an external process listening on a Unix domain socket.

%package back-meta
Summary:        OpenLDAP Meta Back-End
Group:          Productivity/Networking/LDAP/Servers
Requires:       openldap2 = %{version_main}
Provides:       openldap2:/usr/share/man/man5/slapd-meta.5.gz

%description back-meta
The OpenLDAP Meta back-end is able to perform basic LDAP proxying with
respect to a set of remote LDAP servers. The information contained in
these servers can be presented as belonging to a single Directory
Information Tree (DIT).

%package back-sql
Summary:        OpenLDAP SQL Back-End
Group:          Productivity/Networking/LDAP/Servers
Requires:       openldap2 = %{version_main}

%description back-sql
The primary purpose of this OpenLDAP backend is to present information
stored in a Relational (SQL) Database as an LDAP subtree without the need
to do any programming.

%package -n libldap-data
Summary:        Configuration file for system-wide defaults for all uses of libldap
Group:          Productivity/Networking/LDAP/Clients
%if 0%{?suse_version} != 1110
BuildArch:      noarch
%endif

%description -n libldap-data
The subpackage contains a configuration file used to set system-wide defaults
to be applied with all usages of libldap.

%package contrib
Summary:        OpenLDAP Contrib Modules
Group:          Productivity/Networking/LDAP/Servers
Requires:       openldap2 = %{version_main}

%description contrib
Various overlays found in contrib/:
addpartial    Intercepts ADD requests, applies changes to existing entries
allop
allowed       Generates attributes indicating access rights
autogroup
cloak
denyop
lastbind      writes last bind timestamp to entry
noopsrch      handles no-op search control
pw-sha2       generates/validates SHA-2 password hashes
pw-pbkdf2     generates/validates PBKDF2 password hashes
smbk5pwd      generates Samba3 password hashes (heimdal krb disabled)
trace         traces overlay invocation

%package doc
Summary:        OpenLDAP Documentation
Group:          Documentation/Other
Provides:       openldap2:/usr/share/doc/packages/openldap2/drafts/README
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description doc
The OpenLDAP Admin Guide plus a set of OpenLDAP related IETF internet drafts.

%package client
Summary:        OpenLDAP client utilities
Group:          Productivity/Networking/LDAP/Clients
Requires:       libldap-2_4-2 = %{version_main}

%description client
OpenLDAP client utilities such as ldapadd, ldapsearch, ldapmodify.

%package devel
Summary:        Libraries, Header Files and Documentation for OpenLDAP
# bug437293
Group:          Development/Libraries/C and C++
%ifarch ppc64
Obsoletes:      openldap2-devel-64bit
%endif
#
Conflicts:      openldap-devel
Requires:       libldap-2_4-2 = %{version_main}
Recommends:     cyrus-sasl-devel

%description devel
This package provides the OpenLDAP libraries, header files, and
documentation.

%package devel-static
Summary:        Static libraries for the OpenLDAP libraries
Group:          Development/Libraries/C and C++
Requires:       cyrus-sasl-devel
Requires:       libopenssl-devel
Requires:       openldap2-devel = %version

%description devel-static
This package provides the static versions of the OpenLDAP libraries
for development.

%package      -n libldap-2_4-2
Summary:        OpenLDAP Client Libraries
Group:          Productivity/Networking/LDAP/Clients
Recommends:     libldap-data >= %{version_main}

%description -n libldap-2_4-2
This package contains the OpenLDAP client libraries.

%package ppolicy-check-password
Version:        %{version_ppolicy_check_module}
Release:        0
Summary:        Password quality check module for OpenLDAP
Group:          Productivity/Networking/LDAP/Servers
Url:            https://github.com/onyxpoint/ppolicy-check-password
BuildRequires:  cracklib-devel
Requires:       openldap2 = %version_main
Recommends:     cracklib cracklib-dict-full

%description ppolicy-check-password
An implementation of password quality check module, based on the original
work done by LDAP Toolbox Project (https://ltd-project.org), that works
together with OpenLDAP password policy overlay (ppolicy), to enforce
password strength policies.

%prep
# Unpack ppolicy check module
%setup -b 200 -q -n %{name_ppolicy_check_module}-%{version_ppolicy_check_module}
%patch200 -p1
cd ..
# Compress the manual page of ppolicy check module
gzip -k %{S:203}

# Unpack and patch OpenLDAP 2.4
%setup -q -a 9 -n openldap-%{version_main}
%patch1 -p1
%patch3 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch11 -p1
%patch13 -p1
%patch15 -p1
%patch16 -p1
cp %{SOURCE5} .

# Move ppolicy check module and its Makefile into openldap-2.4/contrib/slapd-modules/
mv ../%{name_ppolicy_check_module}-%{version_ppolicy_check_module} contrib/slapd-modules/%{name_ppolicy_check_module}
cp %{S:201} contrib/slapd-modules/%{name_ppolicy_check_module}/Makefile

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags} -Wno-format-extra-args -fno-strict-aliasing -DNDEBUG -DSLAP_CONFIG_DELETE -DSLAP_SCHEMA_EXPOSE -DLDAP_COLLECTIVE_ATTRIBUTES -DLDAP_USE_NON_BLOCKING_TLS"
export STRIP=""
./configure \
        --prefix=/usr \
        --sysconfdir=%{_sysconfdir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libdir} \
        --localstatedir=%{_rundir} \
        --enable-wrappers=no \
        --enable-spasswd \
        --enable-modules \
        --enable-shared \
        --enable-dynamic \
        --with-tls=openssl \
        --with-cyrus-sasl \
        --enable-crypt \
        --enable-ipv6=yes \
        --enable-aci \
        --enable-bdb=mod \
        --enable-hdb=mod \
        --enable-rewrite \
        --enable-ldap=mod \
        --enable-meta=mod \
        --enable-monitor=mod \
        --enable-perl=mod \
        --enable-sock=mod \
        --enable-sql=mod \
        --enable-mdb=mod \
        --enable-relay=mod \
        --enable-slp \
        --enable-overlays=mod \
        --enable-syncprov=mod \
        --enable-ppolicy=mod \
        --enable-lmpasswd \
        --with-yielding-select \
  || cat config.log
make depend
make %{?_smp_mflags}
# Build selected contrib overlays
for SLAPO_NAME in addpartial allowed allop autogroup lastbind denyop cloak noopsrch passwd/sha2 passwd/pbkdf2 trace
do
  make -C contrib/slapd-modules/${SLAPO_NAME} %{?_smp_mflags} "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libdir}"
done
# slapo-smbk5pwd only for Samba password hashes
make -C contrib/slapd-modules/smbk5pwd %{?_smp_mflags} "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libdir}" DEFS="-DDO_SAMBA" HEIMDAL_LIB=""

# Build ppolicy-check-password module
make -C contrib/slapd-modules/%{name_ppolicy_check_module} %{?_smp_mflags} "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libdir}"

%check
%if %run_test_suite
# calculate the base port to be use in the test-suite
SLAPD_BASEPORT=10000
if [ -f /.buildenv ] ; then
    . /.buildenv
    SLAPD_BASEPORT=$(($SLAPD_BASEPORT + ${BUILD_INCARNATION:-0} * 10))
fi
export SLAPD_BASEPORT
%ifnarch %arm alpha
rm -f tests/scripts/test019-syncreplication-cascade
rm -f tests/scripts/test022-ppolicy
rm -f tests/scripts/test023-refint
rm -f tests/scripts/test033-glue-syncrepl
#rm -f tests/scripts/test036-meta-concurrency
#rm -f tests/scripts/test039-glue-ldap-concurrency
rm -f tests/scripts/test043-delta-syncrepl
#rm -f tests/scripts/test045-syncreplication-proxied
rm -f tests/scripts/test048-syncrepl-multiproxy
rm -f tests/scripts/test050-syncrepl-multimaster
rm -f tests/scripts/test058-syncrepl-asymmetric
make SLAPD_DEBUG=0 test
%endif
%endif

%install
mkdir -p %{buildroot}/%{_libdir}/openldap
mkdir -p %{buildroot}/usr/lib/openldap
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/%{_unitdir}
make STRIP="" DESTDIR="%{buildroot}" "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libdir}" install
# Additional symbolic link to slapd executable in /usr/sbin/
ln -s %{_libdir}/slapd %{buildroot}/usr/sbin/slapd
# Install selected contrib overlays
for SLAPO_NAME in addpartial allowed allop autogroup lastbind denyop cloak noopsrch passwd/sha2 passwd/pbkdf2 trace
do
  make -C contrib/slapd-modules/${SLAPO_NAME} STRIP="" DESTDIR="%{buildroot}" "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libdir}" install
done
# slapo-smbk5pwd only for Samba password hashes
make -C contrib/slapd-modules/smbk5pwd STRIP="" DESTDIR="%{buildroot}" "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libdir}" install
install -m 755 %{SOURCE13} %{buildroot}/usr/lib/openldap/start
install -m 644 %{SOURCE14} %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_sysconfdir}/openldap/slapd.d
mkdir -p %{buildroot}/%{_sysconfdir}/sasl2
install -m 644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/sasl2/slapd.conf
install -m 755 -d %{buildroot}/var/lib/ldap
chmod a+x %{buildroot}/%{_libdir}/liblber.so*
chmod a+x %{buildroot}/%{_libdir}/libldap_r.so*
install -m 755 %{SOURCE6} %{buildroot}/usr/sbin/schema2ldif
install -m 755 %{SOURCE17} %{buildroot}/usr/sbin
mkdir -p  %{buildroot}/usr/lib/tmpfiles.d/
install -m 644 %{SOURCE18} %{buildroot}/usr/lib/tmpfiles.d/
install -m 644 %{SOURCE3}  %{buildroot}/%{_libexecdir}/openldap/

# Install ppolicy check module
make -C contrib/slapd-modules/ppolicy-check-password STRIP="" DESTDIR="%{buildroot}" "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libexecdir}" install
install -m 0644 %{S:202}  %{buildroot}%{_sysconfdir}/openldap/check_password.conf
# Install ppolicy check module's doc files
pushd contrib/slapd-modules/%{name_ppolicy_check_module}
mkdir -p "%{buildroot}%ppolicy_docdir"
install -m 0644 README "%{buildroot}%ppolicy_docdir"
install -m 0644 LICENSE "%{buildroot}%ppolicy_docdir"
popd
# Install ppolicy check module's manual page
install -m 0644 %{S:203}.gz %{buildroot}%{_mandir}/man5/

mkdir -p %{buildroot}/%{_fillupdir}
install -m 644 %{SOURCE16} %{buildroot}/%{_fillupdir}/sysconfig.openldap
install -m 644 *.ldif %{buildroot}/%{_sysconfdir}/openldap/schema
install -m 644 *.schema %{buildroot}/%{_sysconfdir}/openldap/schema
# Install default and sample configuration files
install -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/openldap
install -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/openldap
install -m 644 %{SOURCE12} %{buildroot}/%{_sysconfdir}/openldap
find doc/guide '(' ! -name *.html -a ! -name *.gif -a ! -name *.png -a ! -type d ')' -delete
rm -rf doc/guide/release

%define DOCDIR %{_defaultdocdir}/%{name}
# Install default database optimisation
install -d %{buildroot}/%{DOCDIR}/adminguide \
           %{buildroot}/%{DOCDIR}/images \
           %{buildroot}/%{DOCDIR}/drafts
install -m 644 %{buildroot}/etc/openldap/DB_CONFIG.example %{buildroot}/%{DOCDIR}/
install -m 644 doc/guide/admin/* %{buildroot}/%{DOCDIR}/adminguide
install -m 644 doc/guide/images/*.gif %{buildroot}/%{DOCDIR}/images
install -m 644 doc/drafts/* %{buildroot}/%{DOCDIR}/drafts
install -m 644 ANNOUNCEMENT \
               COPYRIGHT \
               README \
               CHANGES \
               %{SOURCE5} \
               %{buildroot}/%{DOCDIR}
install -m 644 servers/slapd/slapd.ldif \
               %{buildroot}/%{DOCDIR}/slapd.ldif.default
rm -f %{buildroot}/etc/openldap/DB_CONFIG.example
rm -f %{buildroot}/etc/openldap/schema/README
rm -f %{buildroot}/etc/openldap/slapd.ldif*
rm -f %{buildroot}/%{_rundir}/openldap-data/DB_CONFIG.example
mv servers/slapd/back-sql/rdbms_depend servers/slapd/back-sql/examples

ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcslapd

rm -f %{buildroot}/%{_libdir}/openldap/*.a
rm -f %{buildroot}/usr/share/man/man5/slapd-dnssrv.5
rm -f %{buildroot}/usr/share/man/man5/slapd-ndb.5
rm -f %{buildroot}/usr/share/man/man5/slapd-null.5
rm -f %{buildroot}/usr/share/man/man5/slapd-passwd.5
rm -f %{buildroot}/usr/share/man/man5/slapd-shell.5
rm -f %{buildroot}/usr/share/man/man5/slapd-tcl.5
# Remove *.la files, libtool does not handle this correct
rm -f  %{buildroot}/%{_libdir}/lib*.la

# Make ldap_r the only copy in the system [rh#1370065].
# libldap.so is only for `gcc/ld -lldap`. Make no libldap-2.4.so.2.
rm -f "%{buildroot}/%{_libdir}"/libldap-2.4.so*
ln -fs libldap_r.so "%{buildroot}/%{_libdir}/libldap.so"
gcc -shared -o "%{buildroot}/%{_libdir}/libldap-2.4.so.2" -Wl,--no-as-needed \
       -Wl,-soname -Wl,libldap-2.4.so.2 -L "%{buildroot}/%{_libdir}" -lldap_r

%pre
getent group ldap >/dev/null || /usr/sbin/groupadd -g 70 -o -r ldap
getent passwd ldap >/dev/null || /usr/sbin/useradd -r -o -g ldap -u 76 -s /bin/false -c "User for OpenLDAP" -d /var/lib/ldap ldap
%service_add_pre slapd.service

%post
if [ ${1:-0} -gt 1 ] && [ -f %{_libdir}/sasl2/slapd.conf ] ; then
  cp /etc/sasl2/slapd.conf /etc/sasl2/slapd.conf.rpmnew
  cp %{_libdir}/sasl2/slapd.conf /etc/sasl2/slapd.conf
fi

if [ ${1:-0} -gt 1 ] && [ ! -f /var/adm/openldap_modules_path_updated ] ; then
    /usr/sbin/openldap_update_modules_path.sh
fi
%{fillup_only -n openldap ldap}
%tmpfiles_create %{name}.conf
%service_add_post slapd.service

%post -n libldap-2_4-2 -p /sbin/ldconfig

%postun -n libldap-2_4-2 -p /sbin/ldconfig

%preun
%service_del_preun slapd.service

%postun
%service_del_postun slapd.service

%files
%defattr(-,root,root)
%config %{_sysconfdir}/openldap/schema/*.schema
%config %{_sysconfdir}/openldap/schema/*.ldif
%config(noreplace) /etc/sasl2/slapd.conf
%config(noreplace) %attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf
%config(noreplace) %attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf.olctemplate
%config %attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf.default
%config %attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf.example
%config(noreplace) %attr(640, ldap, ldap) %{_libexecdir}/openldap/DB_CONFIG
%dir %{_libdir}/openldap
%dir %{_libexecdir}/openldap
%dir %{_sysconfdir}/sasl2
%dir %{_sysconfdir}/openldap
%dir %attr(0770, ldap, ldap) %{_sysconfdir}/openldap/slapd.d
%dir %{_sysconfdir}/openldap/schema
%{_fillupdir}/sysconfig.openldap
%{_sbindir}/slap*
%{_sbindir}/rcslapd
%{_sbindir}/openldap_update_modules_path.sh
%{_libdir}/openldap/back_bdb*
%{_libdir}/openldap/back_hdb*
%{_libdir}/openldap/back_ldap*
%{_libdir}/openldap/back_mdb*
%{_libdir}/openldap/back_monitor*
%{_libdir}/openldap/back_relay*
%{_libdir}/openldap/accesslog*
%{_libdir}/openldap/auditlog*
%{_libdir}/openldap/collect*
%{_libdir}/openldap/constraint*
%{_libdir}/openldap/dds*
%{_libdir}/openldap/deref*
%{_libdir}/openldap/dyngroup*
%{_libdir}/openldap/dynlist*
%{_libdir}/openldap/memberof*
%{_libdir}/openldap/pcache*
%{_libdir}/openldap/ppolicy-2.4.*
%{_libdir}/openldap/ppolicy.*
%{_libdir}/openldap/refint*
%{_libdir}/openldap/retcode*
%{_libdir}/openldap/rwm*
%{_libdir}/openldap/seqmod*
%{_libdir}/openldap/sssvlv*
%{_libdir}/openldap/syncprov*
%{_libdir}/openldap/translucent*
%{_libdir}/openldap/unique*
%{_libdir}/openldap/valsort*
%{_libdir}/slapd
%{_libexecdir}/openldap/start
%{_unitdir}/slapd.service
/usr/lib/tmpfiles.d/%{name}.conf
%dir %attr(0750, ldap, ldap) /var/lib/ldap
%ghost %attr(0750, ldap, ldap) %{_rundir}
%doc %{_mandir}/man8/sl*
%doc %{_mandir}/man5/slapd.*
%doc %{_mandir}/man5/slapd-bdb.*
%doc %{_mandir}/man5/slapd-config.*
%doc %{_mandir}/man5/slapd-hdb.*
%doc %{_mandir}/man5/slapd-ldap.*
%doc %{_mandir}/man5/slapd-ldif.*
%doc %{_mandir}/man5/slapd-mdb.*
%doc %{_mandir}/man5/slapd-monitor.*
%doc %{_mandir}/man5/slapd-relay.*
%doc %{_mandir}/man5/slapo-*
%dir %{DOCDIR}
%doc %{DOCDIR}/ANNOUNCEMENT
%doc %{DOCDIR}/COPYRIGHT
%license LICENSE
%doc %{DOCDIR}/README*
%doc %{DOCDIR}/CHANGES
%doc %{DOCDIR}/slapd.ldif.default
%doc %{DOCDIR}/DB_CONFIG.example

%files back-perl
%defattr(-,root,root)
%{_libdir}/openldap/back_perl*
%doc %{_mandir}/man5/slapd-perl.*

%files back-sock
%defattr(-,root,root)
%{_libdir}/openldap/back_sock*
%doc %{_mandir}/man5/slapd-sock.*

%files back-meta
%defattr(-,root,root)
%{_libdir}/openldap/back_meta*
%doc %{_mandir}/man5/slapd-meta.*

%files back-sql
%defattr(-,root,root)
%{_libdir}/openldap/back_sql*
%doc %{_mandir}/man5/slapd-sql.*
%doc servers/slapd/back-sql/examples
%doc servers/slapd/back-sql/docs/bugs
%doc servers/slapd/back-sql/docs/install

%files -n libldap-data
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/openldap/ldap.conf
%doc %{_mandir}/man5/ldap.conf*
%{_sysconfdir}/openldap/ldap.conf.default

%files doc
%defattr(-,root,root)
%dir %{DOCDIR}
%doc %{DOCDIR}/drafts
%doc %{DOCDIR}/adminguide
%doc %{DOCDIR}/images

%files contrib
%defattr(-,root,root)
%{_libdir}/openldap/addpartial.*
%{_libdir}/openldap/allowed.*
%{_libdir}/openldap/allop.*
%{_libdir}/openldap/autogroup.*
%{_libdir}/openldap/lastbind.*
%{_libdir}/openldap/noopsrch.*
%{_libdir}/openldap/pw-sha2.*
%{_libdir}/openldap/pw-pbkdf2.*
%{_libdir}/openldap/denyop.*
%{_libdir}/openldap/cloak.*
%{_libdir}/openldap/smbk5pwd.*
%{_libdir}/openldap/trace.*

%files client
%defattr(-,root,root)
%doc %{_mandir}/man1/ldap*
%doc %{_mandir}/man5/ldif.*
%dir /etc/openldap
/usr/sbin/schema2ldif
/usr/bin/ldapadd
/usr/bin/ldapcompare
/usr/bin/ldapdelete
/usr/bin/ldapexop
/usr/bin/ldapmodify
/usr/bin/ldapmodrdn
/usr/bin/ldapsearch
/usr/bin/ldappasswd
/usr/bin/ldapurl
/usr/bin/ldapwhoami

%files -n libldap-2_4-2
%defattr(-,root,root)
%{_libdir}/liblber*2.4.so.*
%{_libdir}/libldap*2.4.so.*

%files devel
%defattr(-,root,root)
%doc %{_mandir}/man3/ber*
%doc %{_mandir}/man3/lber*
%doc %{_mandir}/man3/ld_errno*
%doc %{_mandir}/man3/ldap*
%{_includedir}/*.h
%{_libdir}/liblber.so
%{_libdir}/libldap*.so

%files devel-static
%defattr(-,root,root)
%_libdir/liblber.a
%_libdir/libldap*.a

%files ppolicy-check-password
%defattr(-,root,root)
%doc %{ppolicy_docdir}/
%config(noreplace) /etc/openldap/check_password.conf
%{_libdir}/openldap/ppolicy-check-password.*
%{_mandir}/man5/ppolicy-check-password.*

%changelog
