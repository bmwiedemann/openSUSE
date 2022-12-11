#
# spec file
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


%define run_test_suite 0
%define version_main 2.6.3
%define slapdrundir %{_rundir}/slapd
%define flavor @BUILD_FLAVOR@%{nil}
%if "%flavor" == "contrib"
%define name_suffix -%{flavor}-src
%else
%define name_suffix %{nil}
%endif

Name:           openldap2%{name_suffix}
Summary:        An open source implementation of the Lightweight Directory Access Protocol
License:        OLDAP-2.8
Group:          Productivity/Networking/LDAP/Servers
Version:        %{version_main}
Release:        0
URL:            https://www.openldap.org
Source0:        https://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-%{version_main}.tgz
Source1:        https://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-%{version_main}.tgz.asc
Source2:        openldap2.keyring
Source4:        sasl-slapd.conf
Source5:        README.module-loading
Source6:        schema2ldif
Source7:        baselibs.conf
Source9:        addonschema.tar.gz
Source12:       slapd.conf.example
Source13:       start
Source14:       slapd.service
Source16:       sysconfig.openldap
Source18:       openldap2.conf
Source19:       ldap-user.conf
Source20:       fixup-modulepath.sh
Source21:       slapd-ldif-update-crc.sh
Source22:       update-crc.sh
Source23:       slapd.conf
Source24:       slapd.conf.olctemplate
Patch1:         reproducible.patch
Patch3:         0003-LDAPI-socket-location.dif
Patch5:         0005-pie-compile.dif
Patch8:         0008-In-monitor-backend-do-not-return-Connection0-entries.patch
Patch16:        0016-Clear-shared-key-only-in-close-function.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  argon2-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
BuildRequires:  groff
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  openslp-devel
BuildRequires:  sysuser-tools
BuildRequires:  unixODBC-devel
# avoid cycle with krb5
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(systemd)
%if "%flavor" == "contrib"
BuildRequires:  gcc-c++
BuildRequires:  openldap2-devel
%endif
%if %{suse_version} < 1500
%{?systemd_requires}
%endif
Requires:       /usr/bin/awk
Requires:       libldap2 = %{version_main}
Recommends:     cyrus-sasl
Conflicts:      openldap
PreReq:         %fillup_prereq
%sysusers_requires

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
BuildArch:      noarch

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
authzid       implements RFC 3829 support
cloak
datamorph     store enumerated values and fixed size integers
denyop
lastbind      writes last bind timestamp to entry
noopsrch      handles no-op search control
pw-sha2       generates/validates SHA-2 password hashes
pw-pbkdf2     generates/validates PBKDF2 password hashes
smbk5pwd      generates Samba3 password hashes (heimdal krb disabled)
trace         traces overlay invocation
variant       allows attributes/values to be shared between several entries
vc            implements the verify credentials extended operation

%package doc
Summary:        OpenLDAP Documentation
Group:          Documentation/Other
Provides:       openldap2:/usr/share/doc/packages/openldap2/drafts/README
BuildArch:      noarch

%description doc
The OpenLDAP Admin Guide plus a set of OpenLDAP related IETF internet drafts.

%package client
Summary:        OpenLDAP client utilities
Group:          Productivity/Networking/LDAP/Clients
Requires:       libldap2 = %{version_main}

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
Requires:       libldap2 = %{version_main}
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

%package      -n libldap2
Summary:        OpenLDAP Client Libraries
Group:          Productivity/Networking/LDAP/Clients
Recommends:     libldap-data >= %{version_main}

%description -n libldap2
This package contains the OpenLDAP client libraries.

%package      -n libldapcpp-devel
Summary:        C++ wrapper around openLDAP API
Group:          Development/Libraries/C and C++
Requires:       libldapcpp0 = %{version_main}
Requires:       openldap2-devel

%description -n libldapcpp-devel
This package contains files needed for development with the LDAP C++
library.

%package      -n libldapcpp0
Summary:        C++ wrapper around openLDAP API
Group:          Development/Libraries/C and C++
Provides:       ldapcpplib = %{version_main}
Obsoletes:      ldapcpplib <= 0.0.5

%description -n libldapcpp0
This package provides a C++ library for accessing LDAP (Version 3)
Servers

%prep
%setup -q -a 9 -n openldap-%{version_main}
%patch1 -p1
%patch3 -p1
%patch5 -p1
%patch8 -p1
%patch16 -p1
cp %{SOURCE5} .

%build
%if "%flavor" == "contrib"
cd contrib/ldapc++
%configure --disable-static
%make_build
%else
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags} -Wno-format-extra-args -fno-strict-aliasing -DNDEBUG -DSLAP_CONFIG_DELETE -DSLAP_SCHEMA_EXPOSE -DLDAP_COLLECTIVE_ATTRIBUTES -DLDAP_USE_NON_BLOCKING_TLS"
export STRIP=""
./configure \
        --prefix=/usr \
        --sysconfdir=%{_sysconfdir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libdir} \
        --localstatedir=%{slapdrundir} \
        --enable-wrappers=no \
        --enable-spasswd \
        --enable-modules \
        --enable-shared \
        --enable-dynamic \
        --with-tls=openssl \
        --with-cyrus-sasl \
        --enable-crypt \
        --enable-ipv6=yes \
        --enable-dynacl \
        --enable-aci \
        --enable-ldap=mod \
        --enable-meta=mod \
        --enable-perl=mod \
        --enable-sock=mod \
        --enable-sql=mod \
        --enable-mdb=mod \
        --enable-relay=mod \
        --enable-slp \
        --enable-overlays=mod \
        --enable-syncprov=mod \
        --enable-ppolicy=mod \
        --with-yielding-select \
        --with-argon2=libargon2 \
  || cat config.log
make depend
%make_build
# Build selected contrib overlays
for SLAPO_NAME in addpartial allowed allop autogroup authzid datamorph lastbind denyop cloak noopsrch passwd/sha2 passwd/pbkdf2 trace variant vc
do
  make -C contrib/slapd-modules/${SLAPO_NAME} %{?_smp_mflags} "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libdir}"
done
# slapo-smbk5pwd only for Samba password hashes
make -C contrib/slapd-modules/smbk5pwd %{?_smp_mflags} "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libdir}" DEFS="-DDO_SAMBA" HEIMDAL_LIB=""

# Create ldap user
%sysusers_generate_pre %{SOURCE19} ldap
%endif

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
%if "%flavor" == "contrib"
cd contrib/ldapc++
%make_install
%else
mkdir -p %{buildroot}%{_libdir}/openldap
mkdir -p %{buildroot}/usr/lib/openldap
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
make STRIP="" DESTDIR="%{buildroot}" "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libdir}" install
# Additional symbolic link to slapd executable in /usr/sbin/
ln -s %{_libdir}/slapd %{buildroot}%{_sbindir}/slapd
# Install selected contrib overlays
for SLAPO_NAME in addpartial allowed allop autogroup authzid datamorph lastbind denyop cloak noopsrch passwd/sha2 passwd/pbkdf2 trace variant vc
do
  make -C contrib/slapd-modules/${SLAPO_NAME} STRIP="" DESTDIR="%{buildroot}" "mandir=%{_mandir}" "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libdir}" install
done
# slapo-smbk5pwd only for Samba password hashes
make -C contrib/slapd-modules/smbk5pwd STRIP="" DESTDIR="%{buildroot}" "mandir=%{_mandir}" "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libdir}" install
install -m 755 %{SOURCE13} %{buildroot}/usr/lib/openldap/start
install -m 644 %{SOURCE14} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/openldap/slapd.d
mkdir -p %{buildroot}%{_sysconfdir}/sasl2
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sasl2/slapd.conf
install -m 755 -d %{buildroot}/var/lib/ldap
chmod a+x %{buildroot}%{_libdir}/liblber.so*
chmod a+x %{buildroot}%{_libdir}/libldap.so*
install -m 755 %{SOURCE6} %{buildroot}%{_sbindir}/schema2ldif
mkdir -p  %{buildroot}%{_tmpfilesdir}/
install -m 644 %{SOURCE18} %{buildroot}%{_tmpfilesdir}/
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE19} %{buildroot}%{_sysusersdir}/

install -m 755 %{SOURCE19}  ${RPM_BUILD_ROOT}/usr/lib/openldap/fixup-modulepath
install -m 755 %{SOURCE20}  ${RPM_BUILD_ROOT}/%{_sbindir}/slapd-ldif-update-crc
install -m 755 %{SOURCE21}  ${RPM_BUILD_ROOT}/usr/lib/openldap/update-crc

mkdir -p %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE16} %{buildroot}%{_fillupdir}/sysconfig.openldap
install -m 644 *.ldif %{buildroot}%{_sysconfdir}/openldap/schema
install -m 644 *.schema %{buildroot}%{_sysconfdir}/openldap/schema
# Install default and sample configuration files
install -m 644 %{SOURCE23} %{buildroot}%{_sysconfdir}/openldap
install -m 644 %{SOURCE24} %{buildroot}%{_sysconfdir}/openldap
install -m 644 %{SOURCE12} %{buildroot}%{_sysconfdir}/openldap
find doc/guide '(' ! -name *.html -a ! -name *.gif -a ! -name *.png -a ! -type d ')' -delete
rm -rf doc/guide/release

%define DOCDIR %{_defaultdocdir}/%{name}
# Install default database optimisation
install -d %{buildroot}%{DOCDIR}/adminguide \
           %{buildroot}%{DOCDIR}/images \
           %{buildroot}%{DOCDIR}/drafts
install -m 644 doc/guide/admin/* %{buildroot}%{DOCDIR}/adminguide
install -m 644 doc/guide/images/*.gif %{buildroot}%{DOCDIR}/images
install -m 644 doc/drafts/* %{buildroot}%{DOCDIR}/drafts
install -m 644 ANNOUNCEMENT \
               COPYRIGHT \
               README \
               CHANGES \
               %{SOURCE5} \
               %{buildroot}%{DOCDIR}
install -m 644 servers/slapd/slapd.ldif \
               %{buildroot}%{DOCDIR}/slapd.ldif.default
rm -f %{buildroot}/etc/openldap/schema/README
rm -f %{buildroot}/etc/openldap/slapd.ldif*
mv servers/slapd/back-sql/rdbms_depend servers/slapd/back-sql/examples

ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcslapd

rm -f %{buildroot}%{_libdir}/openldap/*.a
rm -f %{buildroot}/usr/share/man/man5/slapd-dnssrv.5
rm -f %{buildroot}/usr/share/man/man5/slapd-ndb.5
rm -f %{buildroot}/usr/share/man/man5/slapd-null.5
rm -f %{buildroot}/usr/share/man/man5/slapd-passwd.5
rm -f %{buildroot}/usr/share/man/man5/slapd-shell.5
rm -f %{buildroot}/usr/share/man/man5/slapd-tcl.5
# Remove *.la files, libtool does not handle this correct
# Keep .la files for modules in the openldap subdirectory, which are consumed
# in this form.
rm -f  %{buildroot}%{_libdir}/*.la

# Provide a libldap_r for backwards-compatibility with OpenLDAP < 2.5.
ln -fs libldap.so "%{buildroot}%{_libdir}/libldap_r.so"
%endif

%pre -f ldap.pre
%service_add_pre slapd.service

%post
%{fillup_only -n openldap ldap}
%tmpfiles_create %{name}.conf
%service_add_post slapd.service

%post -n libldap2 -p /sbin/ldconfig
%postun -n libldap2 -p /sbin/ldconfig

%preun
%service_del_preun slapd.service

%postun
%service_del_postun slapd.service

%if "%flavor" == "contrib"
%files -n libldapcpp-devel
%doc contrib/ldapc++/README
%_includedir/*.h
%_libdir/libldapcpp.la
%_libdir/libldapcpp.so

%files -n libldapcpp0
%_libdir/libldapcpp.so.0
%_libdir/libldapcpp.so.0.0.0

%else

%files
%config %{_sysconfdir}/openldap/schema/*.schema
%config %{_sysconfdir}/openldap/schema/*.ldif
%config(noreplace) /etc/sasl2/slapd.conf
%config(noreplace) %attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf
%config(noreplace) %attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf.olctemplate
%config %attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf.default
%config %attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf.example
%dir %{_libdir}/openldap
%dir /usr/lib/openldap
%dir %{_sysconfdir}/sasl2
%dir %{_sysconfdir}/openldap
%dir %attr(0770, ldap, ldap) %{_sysconfdir}/openldap/slapd.d
%dir %{_sysconfdir}/openldap/schema
%{_fillupdir}/sysconfig.openldap
%{_sbindir}/slap*
%{_sbindir}/rcslapd
%{_libdir}/openldap/back_ldap*
%{_libdir}/openldap/back_mdb*
%{_libdir}/openldap/back_relay*
%{_libdir}/openldap/accesslog*
%{_libdir}/openldap/auditlog*
%{_libdir}/openldap/autoca*
%{_libdir}/openldap/collect*
%{_libdir}/openldap/constraint*
%{_libdir}/openldap/dds*
%{_libdir}/openldap/deref*
%{_libdir}/openldap/dyngroup*
%{_libdir}/openldap/dynlist*
%{_libdir}/openldap/homedir*
%{_libdir}/openldap/memberof*
%{_libdir}/openldap/otp*
%{_libdir}/openldap/pcache*
%{_libdir}/openldap/ppolicy*
%{_libdir}/openldap/remoteauth*
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
/usr/lib/openldap/start
/usr/lib/openldap/update-crc
/usr/lib/openldap/fixup-modulepath
%{_unitdir}/slapd.service
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/ldap-user.conf
%dir %attr(0750, ldap, ldap) %{_sharedstatedir}/ldap
%ghost %attr(0750, ldap, ldap) %{slapdrundir}
%doc %{_mandir}/man8/sl*
%doc %{_mandir}/man8/lloadd.*
%doc %{_mandir}/man5/lloadd.conf.*
%doc %{_mandir}/man5/slapd.*
%doc %{_mandir}/man5/slapd-asyncmeta.*
%doc %{_mandir}/man5/slapd-config.*
%doc %{_mandir}/man5/slapd-ldap.*
%doc %{_mandir}/man5/slapd-ldif.*
%doc %{_mandir}/man5/slapd-mdb.*
%doc %{_mandir}/man5/slapd-monitor.*
%doc %{_mandir}/man5/slapd-pw-*
%doc %{_mandir}/man5/slapd-relay.*
%doc %{_mandir}/man5/slapd-wt.*
%doc %{_mandir}/man5/slapo-*
%doc %{_mandir}/man5/slappw-argon2.*
%dir %{DOCDIR}
%doc %{DOCDIR}/ANNOUNCEMENT
%doc %{DOCDIR}/COPYRIGHT
%license LICENSE
%doc %{DOCDIR}/README*
%doc %{DOCDIR}/CHANGES
%doc %{DOCDIR}/slapd.ldif.default

%files back-perl
%{_libdir}/openldap/back_perl*
%doc %{_mandir}/man5/slapd-perl.*

%files back-sock
%{_libdir}/openldap/back_sock*
%doc %{_mandir}/man5/slapd-sock.*

%files back-meta
%{_libdir}/openldap/back_meta*
%doc %{_mandir}/man5/slapd-meta.*

%files back-sql
%{_libdir}/openldap/back_sql*
%doc %{_mandir}/man5/slapd-sql.*
%doc servers/slapd/back-sql/examples
%doc servers/slapd/back-sql/docs/bugs
%doc servers/slapd/back-sql/docs/install

%files -n libldap-data
%config(noreplace) %{_sysconfdir}/openldap/ldap.conf
%doc %{_mandir}/man5/ldap.conf*
%{_sysconfdir}/openldap/ldap.conf.default

%files doc
%dir %{DOCDIR}
%doc %{DOCDIR}/drafts
%doc %{DOCDIR}/adminguide
%doc %{DOCDIR}/images

%files contrib
%{_libdir}/openldap/addpartial.*
%{_libdir}/openldap/allop.*
%{_libdir}/openldap/allowed.*
%{_libdir}/openldap/authzid.*
%{_libdir}/openldap/autogroup.*
%{_libdir}/openldap/cloak.*
%{_libdir}/openldap/datamorph.*
%{_libdir}/openldap/denyop.*
%{_libdir}/openldap/lastbind.*
%{_libdir}/openldap/noopsrch.*
%{_libdir}/openldap/pw-pbkdf2.*
%{_libdir}/openldap/pw-sha2.*
%{_libdir}/openldap/smbk5pwd.*
%{_libdir}/openldap/trace.*
%{_libdir}/openldap/variant.*
%{_libdir}/openldap/vc.*

%files client
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
/usr/bin/ldapvc
/usr/bin/ldapwhoami

%files -n libldap2
%{_libdir}/liblber.so.*
%{_libdir}/libldap.so.*

%files devel
%doc %{_mandir}/man3/ber*
%doc %{_mandir}/man3/lber*
%doc %{_mandir}/man3/ld_errno*
%doc %{_mandir}/man3/ldap*
%{_includedir}/*.h
%{_libdir}/liblber.so
%{_libdir}/libldap*.so
%{_libdir}/pkgconfig/*.pc

%files devel-static
%_libdir/liblber.a
%_libdir/libldap*.a

%endif # !flavor:contrib

%changelog
