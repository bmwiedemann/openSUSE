#
# spec file for package bind
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


%define _buildshell /bin/bash
%bcond_with check

# DLZ modules
%bcond_without modules_bdbhpt
%bcond_without modules_ldap
%bcond_without modules_mysql
%bcond_without modules_sqlite3
%bcond_without modules_perl
%bcond_without modules_generic
# end DLZ modules

%define	VENDOR SUSE
%if 0%{?suse_version} >= 1500
%define with_systemd 1
%else
%define with_systemd 0
# Defines for user and group add
%define	NAMED_UID 44
%define	NAMED_UID_NAME named
%define	NAMED_GID 44
%define	NAMED_GID_NAME named
%define	NAMED_COMMENT Name server daemon
%define	NAMED_HOMEDIR %{_localstatedir}/lib/named
%define	NAMED_SHELL /bin/false
%define	GROUPADD_NAMED getent group %{NAMED_GID_NAME} >/dev/null || %{_sbindir}/groupadd -g %{NAMED_GID} -o -r %{NAMED_GID_NAME}
%define	USERADD_NAMED getent passwd %{NAMED_UID_NAME} >/dev/null || %{_sbindir}/useradd -r -o -g %{NAMED_GID_NAME} -u %{NAMED_UID} -s %{NAMED_SHELL} -c "%{NAMED_COMMENT}" -d %{NAMED_HOMEDIR} %{NAMED_UID_NAME}
%define	USERMOD_NAMED getent passwd %{NAMED_UID_NAME} >/dev/null || %{_sbindir}/usermod -s %{NAMED_SHELL} -d  %{NAMED_HOMEDIR} %{NAMED_UID_NAME}
%endif
%if 0%{?suse_version} < 1315
%define with_sfw2 1
%else
%define with_sfw2 0
%endif

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           bind
Version:        9.18.10
Release:        0
Summary:        Domain Name System (DNS) Server (named)
License:        MPL-2.0
Group:          Productivity/Networking/DNS/Servers
URL:            https://www.isc.org/bind/
Source:         https://downloads.isc.org/isc/bind9/%{version}/bind-%{version}.tar.xz
Source1:        https://downloads.isc.org/isc/bind9/%{version}/bind-%{version}.tar.xz.sha512.asc
Source2:        vendor-files.tar.bz2
# from http://www.isc.org/about/openpgp/ ... changes yearly apparently.
Source3:        %{name}.keyring
Source9:        ftp://ftp.internic.net/domain/named.root
Source40:       dnszone-schema.txt
Source60:       dlz-schema.txt
# configuration file for systemd-tmpfiles
Source70:       bind.conf
# configuation file for systemd-sysusers
Source72:       named.conf
Patch56:        bind-ldapdump-use-valid-host.patch
BuildRequires:  libcap-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  openssl
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-Sphinx
BuildRequires:  python3-ply
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       %{name}-utils
Requires(post): %fillup_prereq
Requires(post): bind-utils
Provides:       bind8 = %{version}
Provides:       bind9 = %{version}
Provides:       dns_daemon
Obsoletes:      bind8 < %{version}
Obsoletes:      bind9 < %{version}
%if %{with_systemd}
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%sysusers_requires
%else
Requires(post): %insserv_prereq
Requires(pre):  shadow
%endif

%description
Berkeley Internet Name Domain (BIND) is an implementation of the Domain
Name System (DNS) protocols and provides an openly redistributable
reference implementation of the major components of the Domain Name
System.  This package includes the components to operate a DNS server.

%package doc
Summary:        BIND documentation
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Documentation of the Berkeley Internet Name Domain (BIND) Domain Name
System implementation of the Domain Name System (DNS) protocols.  This
includes also the BIND Administrator Reference Manual (ARM).

%package utils
Summary:        Libraries for "bind" and utilities to query and test DNS
# Needed for dnssec parts
Group:          Productivity/Networking/DNS/Utilities
Provides:       bind9-utils
Provides:       bindutil
Provides:       dns_utils
Obsoletes:      bind-devel < %{version}
Obsoletes:      bind9-utils < %{version}
Obsoletes:      bindutil < %{version}
Obsoletes:      libirs-devel < %{version}

%description utils
This package includes the utilities "host", "dig", and "nslookup" used to
test and query the Domain Name System (DNS) and also the libraries rquired
for the base "bind" package. The Berkeley Internet
Name Domain (BIND) DNS server is found in the package named bind.

%if %{with_modules_perl}
%package modules-perl
Summary:        A dynamically loadable zone (DLZ) plugin embedding a Perl interpreter in BIND
Group:          Productivity/Networking/DNS/Servers
BuildRequires:  perl

%description modules-perl
This package includes a dynamically loadable zone (DLZ) plugin
embedding a Perl interpreter in BIND, allowing Perl scripts
to be written to integrate with BIND and serve DNS data.
%endif

%if %{with_modules_mysql}
%package modules-mysql
Summary:        DLZ modules which store zone data in a MySQL database
Group:          Productivity/Networking/DNS/Servers
BuildRequires:  libmysqlclient-devel

%description modules-mysql
This package includes dynamically loadable zone (DLZ) plugins
which store zone data in a MySQL database
The dlz_mysql_dynamic.so plugin does not support dynamic updates
the dlz_mysqldyn_mod.so plugin is a dynamically loadable zone (DLZ)
plugin that uses a fixed-schema MySQL database for back-end storage.
It allows zone data to be updated via dynamic DNS updates, and
sends DNS NOTIFY packets to other name servers when appropriate.
%endif

%if %{with_modules_ldap}
%package modules-ldap
Summary:        A DLZ module which stores zone data in an LDAP directory
Group:          Productivity/Networking/DNS/Servers
BuildRequires:  openldap2-devel

%description modules-ldap
This package provides the externally loadable ldap DLZ module, without
update support
%endif

%if %{with_modules_bdbhpt}
%package modules-bdbhpt
Summary:        A DLZ module which stores zone data in a BerkeleyDB
Group:          Productivity/Networking/DNS/Servers
BuildRequires:  libdb-4_8-devel

%description modules-bdbhpt
This package provides the externally loadable bdbhpt DLZ driver, without
update support
%endif

%if %{with_modules_sqlite3}
%package modules-sqlite3
Summary:        A DLZ module which stores zone data in an sqlite3 db
Group:          Productivity/Networking/DNS/Servers
BuildRequires:  sqlite3-devel

%description modules-sqlite3
This package provides the externally loadable SQLitee DLZ module, without
update support.
%endif

%if %{with_modules_generic}
%package modules-generic
Summary:        DLZ module which store zone data in plain files
Group:          Productivity/Networking/DNS/Servers

%description modules-generic
This package provides the externally loadable filesystem DLZ module, without
update support and the externally loadable wildcard DLZ module.
The "wildcard" DLZ module provides a "template" zone for domains matching
a wildcard name.
For any zone name matching the wildcard, it would return the data from
the template.  "$zone$" is replaced with zone name: i.e., the shortest
possible string of labels in the query name that matches the wildcard.
%endif

%prep
%autosetup -p1 -a2

# use the year from source gzip header instead of current one to make reproducible rpms
year=$(perl -e 'sysread(STDIN, $h, 8); print (1900+(gmtime(unpack("l",substr($h,4))))[5])' < %{SOURCE0})
sed -i "s/stdout, copyright, year/stdout, copyright, \"-$year\"/" lib/dns/gen.c

# modify settings of some files regarding to OS version and vendor
function replaceStrings()
{
	file="$1"
	sed -e "s@__NSD__@/lib@g" \
		-e "s@__BIND_PACKAGE_NAME__@%{name}@g" \
		-e "s@__VENDOR__@%{VENDOR}@g" \
                -e "s@__openssl__@$(pkg-config --variable=enginesdir libcrypto)@g" \
		-i "${file}"
}
pushd vendor-files
for file in docu/README* config/{README,named.conf} sysconfig/named-named; do
	replaceStrings ${file}
done
popd

%if 0%{?sle_version} >= 150000 && 0%{?sle_version} <= 150400
# the Administration Reference Manual doesn't build with Leap/SLES due to an way too old Sphinx package
# that is missing sphinx.util.docutils.ReferenceRole.
# patch68 disables this extension, and here, we're removing the :gl: tags in the notes
sed -i 's|:gl:||g' doc/notes/notes*.rst
%endif

%build
autoreconf -fvi
export CFLAGS="%{optflags} -fPIE -DNO_VERSION_DATE"
export LDFLAGS="-pie"
%configure \
	--with-python=%{_bindir}/python3 \
	--includedir=%{_includedir}/bind \
	--disable-static \
	--with-openssl \
	--enable-threads \
	--with-libtool \
	--with-libxml2 \
	--with-dlz_filesystem \
	--with-json-c \
	--with-libidn2 \
	--with-randomdev=/dev/urandom \
	--enable-ipv6 \
	--with-pic \
	--disable-openssl-version-check \
	--with-tuning=large \
	--with-maxminddb \
	--with-dlopen=auto \
	--with-gssapi=yes \
	--disable-isc-spnego \
	--enable-fixed-rrset \
	--enable-filter-aaaa \
%if %{with_systemd}
        --with-systemd \
%endif
%if %{with check}
	--enable-querytrace \
%endif
	--enable-full-report
# disable rpath
sed -i '
  s|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g
  s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g
' libtool
%make_build
# special make for the Administrators Reference Manual
for d in arm; do
	make -C doc/${d} SPHINXBUILD=sphinx-build doc
done
%if %{with_systemd}
%sysusers_generate_pre %{SOURCE72} named named.conf
%endif
# special build for the plugins
for d in contrib/dlz/modules/*; do
	[ -e $d/Makefile ] && make -C $d
done

%install
mkdir -p \
	%{buildroot}/%{_sysconfdir}/init.d \
	%{buildroot}/%{_sysconfdir}/named.d \
	%{buildroot}/%{_sysconfdir}/openldap/schema \
	%{buildroot}/%{_sysconfdir}/slp.reg.d \
	%{buildroot}%{_prefix}/{bin,%{_lib},sbin,include} \
	%{buildroot}/%{_datadir}/bind \
	%{buildroot}/%{_datadir}/susehelp/meta/Administration/System \
	%{buildroot}/%{_defaultdocdir}/bind \
	%{buildroot}%{_localstatedir}/lib/named/{etc/named.d,dev,dyn,master,slave,var/{lib,run/named}} \
	%{buildroot}%{_mandir}/{man1,man3,man5,man8} \
	%{buildroot}%{_fillupdir} \
	%{buildroot}/%{_rundir} \
	%{buildroot}%{_includedir}/bind/dns \
	%{buildroot}%{_libexecdir}/bind
%if %{with_sfw2}
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services
%endif
%make_install
# remove useless .h files
rm -rf %{buildroot}%{_includedir}

# Install the plugins
mkdir -p %{buildroot}/%{_libdir}/bind-plugins
%if %{with_modules_perl}
    install -m 0644 contrib/dlz/modules/perl/*.so %{buildroot}/%{_libdir}/bind-plugins
%endif
%if %{with_modules_mysql}
    install -m 0644 contrib/dlz/modules/mysql/*.so %{buildroot}/%{_libdir}/bind-plugins
    install -m 0644 contrib/dlz/modules/mysqldyn/*.so %{buildroot}/%{_libdir}/bind-plugins
%endif
%if %{with_modules_ldap}
    install -m 0644 contrib/dlz/modules/ldap/*.so %{buildroot}/%{_libdir}/bind-plugins
%endif
%if %{with_modules_bdbhpt}
    install -m 0644 contrib/dlz/modules/bdbhpt/*.so %{buildroot}/%{_libdir}/bind-plugins
%endif
%if %{with_modules_sqlite3}
    install -m 0644 contrib/dlz/modules/sqlite3/*.so %{buildroot}/%{_libdir}/bind-plugins
%endif
%if %{with_modules_generic}
    install -m 0644 contrib/dlz/modules/{filesystem,wildcard}/*.so %{buildroot}/%{_libdir}/bind-plugins
%endif
# remove useless .la files
rm -f %{buildroot}/%{_libdir}/lib*.{la,a} %{buildroot}/%{_libdir}/bind/*.la
mv vendor-files/config/named.conf %{buildroot}/%{_sysconfdir}
mv vendor-files/config/bind.reg %{buildroot}/%{_sysconfdir}/slp.reg.d
mv vendor-files/config/rndc-access.conf %{buildroot}/%{_sysconfdir}/named.d

%if %{with_systemd}
	for file in named; do
        	install -D -m 0644 vendor-files/system/${file}.service %{buildroot}%{_unitdir}/${file}.service
                sed -e "s,@LIBEXECDIR@,%{_libexecdir},g" -i %{buildroot}%{_unitdir}/${file}.service
		install -m 0755 vendor-files/system/${file}.prep %{buildroot}%{_libexecdir}/bind/${file}.prep
		ln -s /sbin/service %{buildroot}%{_sbindir}/rc${file}
	done
	install -D -m 0644 %{SOURCE70} %{buildroot}%{_prefix}/lib/tmpfiles.d/bind.conf
	install -D -m 0644 %{_sourcedir}/named.root %{buildroot}%{_datadir}/factory%{_localstatedir}/lib/named/root.hint
	install -m 0644 vendor-files/config/{127.0.0,localhost}.zone %{buildroot}%{_datadir}/factory%{_localstatedir}/lib/named
	install -m 0644 bind.keys %{buildroot}%{_datadir}/factory%{_localstatedir}/lib/named/named.root.key
	install -d -m 0755 %{buildroot}/%{_unitdir}/named.service.d
%else
	for file in named; do
		install -m 0754 vendor-files/init/${file} %{buildroot}%{_initddir}/${file}
		ln -sf %{_initddir}/${file} %{buildroot}%{_sbindir}/rc${file}
	done
%endif
install -m 0644 %{_sourcedir}/named.root %{buildroot}%{_localstatedir}/lib/named/root.hint
mv vendor-files/config/{127.0.0,localhost}.zone %{buildroot}%{_localstatedir}/lib/named
install -m 0755 vendor-files/tools/bind.genDDNSkey %{buildroot}/%{_bindir}/genDDNSkey
cp -a vendor-files/docu/BIND.desktop %{buildroot}/%{_datadir}/susehelp/meta/Administration/System
cp -p %{_sourcedir}/dnszone-schema.txt %{buildroot}/%{_sysconfdir}/openldap/schema/dnszone.schema
cp -p "%{SOURCE60}" "%{buildroot}/%{_sysconfdir}/openldap/schema/dlz.schema"
install -m 0754 vendor-files/tools/ldapdump %{buildroot}/%{_datadir}/bind
find %{buildroot}/%{_libdir} -type f -name '*.so*' -exec chmod 0755 {} +
for file in named-named; do
	install -m 0644 vendor-files/sysconfig/${file} %{buildroot}%{_fillupdir}/sysconfig.${file}
done
%if %{with_sfw2}
install -m 644 vendor-files/sysconfig/SuSEFirewall.named %{buildroot}/%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/bind
%endif
%if ! %{with check}
# Cleanup doc
rm doc/misc/Makefile*
find doc/arm -type f ! -name '*.html' -delete
%endif
# Create doc as we want it in bind and not bind-doc
for file in vendor-files/docu/README*; do
	basename=$( basename ${file})
	cp -a ${file} %{buildroot}/%{_defaultdocdir}/bind/${basename}.%{VENDOR}
done
# mkdir -p vendor-files/config/ISC-examples
# cp -a bin/tests/*.conf* vendor-files/config/ISC-examples
for d in arm; do
	cp -a doc/${d}/_build %{buildroot}/%{_defaultdocdir}/bind/${d}
	echo "%doc %{_defaultdocdir}/bind/${d}" >>filelist-bind-doc
done
for file in CHANGES COPYRIGHT README* version contrib/README* doc/misc vendor-files/config; do
	[ -r ${file} ] || continue
	basename=$( basename ${file})
	cp -a ${file} %{buildroot}/%{_defaultdocdir}/bind/${basename}
	echo "%doc %{_defaultdocdir}/bind/${basename}" >>filelist-bind-doc
done
# ---------------------------------------------------------------------------
# remove useless Makefiles and Makefile skeletons
find %{buildroot}/%{_defaultdocdir}/bind \( -name Makefile -o -name Makefile.in \) -exec rm {} +
install -m 0644 bind.keys %{buildroot}%{_localstatedir}/lib/named/named.root.key
%if %{with_systemd}
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE72} %{buildroot}%{_sysusersdir}/
%endif
find %{buildroot}/usr/share/doc/packages/bind -name cfg_test* -exec rm {} \;
rm -rf %{buildroot}/usr/share/doc/packages/bind/misc/.libs

%if %{with_systemd}
%pre -f named.pre
%service_add_pre named.service
%else

%pre
%{GROUPADD_NAMED}
%{USERADD_NAMED}
# Might be an update.
%{USERMOD_NAMED}
%endif

%if %{with check}
%check
sudo bin/tests/system/ifconfig.sh up
make test
%endif

%preun
%if %{with_systemd}
%service_del_preun named.service
%else
%stop_on_removal named
%endif

%post
%if %{with_systemd}
%{fillup_only -nsa named named}
%service_add_post named.service
%tmpfiles_create bind.conf
%else
%{fillup_and_insserv -nf named}
if [ -x %{_bindir}/systemctl ]; then
# make sure systemctl knows about the service
# Without this, systemctl status named would return
#     Unit named.service could not be found.
# until systemctl daemon-reload has been executed
    %{_bindir}/systemctl daemon-reload || :
fi
%endif

%postun
%if %{with_systemd}
%service_del_postun named.service
%else
%restart_on_update named
%insserv_cleanup
%endif

%post   -n bind-utils -p /sbin/ldconfig
%postun -n bind-utils -p /sbin/ldconfig

%files
%license LICENSE
%attr(0644,root,named) %config(noreplace) /%{_sysconfdir}/named.conf
%dir %{_sysconfdir}/slp.reg.d
%attr(0644,root,root) %config /%{_sysconfdir}/slp.reg.d/bind.reg
%if %{with_systemd}
%{_unitdir}/named.service
%dir %{_unitdir}/named.service.d
%{_prefix}/lib/tmpfiles.d/bind.conf
%{_sysusersdir}/named.conf
%{_datadir}/factory
%else
%config /%{_sysconfdir}/init.d/named
%endif
%if %{with_sfw2}
%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/bind
%endif
%{_bindir}/named-rrchecker
%{_sbindir}/rcnamed
%{_sbindir}/named
%{_bindir}/named-checkconf
%{_bindir}/named-checkzone
%{_bindir}/named-compilezone
%{_bindir}/named-journalprint
%{_bindir}/nsec3hash
%dir %{_libdir}/bind
%{_libdir}/bind/filter-aaaa.so
%{_libdir}/bind/filter-a.so
%{_mandir}/man1/named-rrchecker.1%{ext_man}
%{_mandir}/man5/named.conf.5%{ext_man}
%{_mandir}/man1/named-checkconf.1%{ext_man}
%{_mandir}/man1/named-checkzone.1%{ext_man}
%{_mandir}/man8/named.8%{ext_man}
%{_mandir}/man8/filter-aaaa.8%{ext_man}
%{_mandir}/man8/filter-a.8%{ext_man}
%dir %{_datadir}/bind
%{_datadir}/bind/ldapdump
%ghost %{_rundir}/named
%{_fillupdir}/sysconfig.named-named
%attr(1775,root,named) %dir %{_var}/lib/named
%dir %{_var}/lib/named/master
%attr(-,named,named) %dir %{_var}/lib/named/dyn
%attr(-,named,named) %dir %{_var}/lib/named/slave
%config %{_var}/lib/named/root.hint
%config %{_var}/lib/named/127.0.0.zone
%config %{_var}/lib/named/localhost.zone
%config %{_var}/lib/named/named.root.key
%dir %{_libexecdir}/bind
%{_libexecdir}/bind/named.prep
%dir %{_libdir}/bind-plugins

%if %{with_modules_perl}
%files modules-perl
%{_libdir}/bind-plugins/dlz_perl_driver.so
%endif
%if %{with_modules_mysql}
%files modules-mysql
%{_libdir}/bind-plugins/dlz_mysql_dynamic.so
%{_libdir}/bind-plugins/dlz_mysqldyn_mod.so
%endif
%if %{with_modules_ldap}
%files modules-ldap
%{_libdir}/bind-plugins/dlz_ldap_dynamic.so
%endif
%if %{with_modules_bdbhpt}
%files modules-bdbhpt
%{_libdir}/bind-plugins/dlz_bdbhpt_dynamic.so
%endif
%if %{with_modules_sqlite3}
%files modules-sqlite3
%{_libdir}/bind-plugins/dlz_sqlite3_dynamic.so
%endif
%if %{with_modules_generic}
%files modules-generic
%{_libdir}/bind-plugins/dlz_filesystem_dynamic.so
%{_libdir}/bind-plugins/dlz_wildcard_dynamic.so
%endif

%files doc -f filelist-bind-doc
%dir %doc %{_defaultdocdir}/bind
%doc %{_datadir}/susehelp

%files utils
%dir %{_sysconfdir}/named.d
%config(noreplace) %{_sysconfdir}/named.d/rndc-access.conf
%config(noreplace) %{_sysconfdir}/bind.keys
%dir %{_sysconfdir}/openldap
%dir %{_sysconfdir}/openldap/schema
%attr(0444,root,root) %config %{_sysconfdir}/openldap/schema/dnszone.schema
%attr(0444,root,root) %config %{_sysconfdir}/openldap/schema/dlz.schema
%{_bindir}/delv
%{_bindir}/dig
%{_bindir}/host
%{_bindir}/mdig
%{_bindir}/nslookup
%{_bindir}/nsupdate
%{_bindir}/genDDNSkey
%{_bindir}/arpaname
%{_bindir}/dnssec-dsfromkey
%{_bindir}/dnssec-importkey
%{_bindir}/dnssec-keyfromlabel
%{_bindir}/dnssec-keygen
%{_bindir}/dnssec-revoke
%{_bindir}/dnssec-settime
%{_bindir}/dnssec-signzone
%{_bindir}/dnssec-verify
%{_bindir}/dnssec-cds
%{_sbindir}/ddns-confgen
%{_sbindir}/rndc
%{_sbindir}/rndc-confgen
%{_sbindir}/tsig-keygen
%{_libdir}/libbind9-%{version}.so
%{_libdir}/libdns-%{version}.so
%{_libdir}/libirs-%{version}.so
%{_libdir}/libisc-%{version}.so
%{_libdir}/libisccc-%{version}.so
%{_libdir}/libisccfg-%{version}.so
%{_libdir}/libns-%{version}.so
%{_libdir}/libbind9.so
%{_libdir}/libdns.so
%{_libdir}/libirs.so
%{_libdir}/libisc.so
%{_libdir}/libisccc.so
%{_libdir}/libisccfg.so
%{_libdir}/libns.so
%dir %doc %{_defaultdocdir}/bind
%{_defaultdocdir}/bind/README*.%{VENDOR}
%{_mandir}/man1/arpaname.1%{ext_man}
%{_mandir}/man1/delv.1%{ext_man}
%{_mandir}/man1/dig.1%{ext_man}
%{_mandir}/man1/host.1%{ext_man}
%{_mandir}/man1/mdig.1%{ext_man}
%{_mandir}/man1/nslookup.1%{ext_man}
%{_mandir}/man1/nsupdate.1%{ext_man}
%{_mandir}/man1/dnssec-dsfromkey.1%{ext_man}
%{_mandir}/man1/dnssec-importkey.1%{ext_man}
%{_mandir}/man1/dnssec-keyfromlabel.1%{ext_man}
%{_mandir}/man1/dnssec-keygen.1%{ext_man}
%{_mandir}/man1/dnssec-revoke.1%{ext_man}
%{_mandir}/man1/dnssec-settime.1%{ext_man}
%{_mandir}/man1/dnssec-signzone.1%{ext_man}
%{_mandir}/man1/dnssec-verify.1%{ext_man}
%{_mandir}/man1/dnssec-cds.1%{ext_man}
%{_mandir}/man1/named-compilezone.1%{ext_man}
%{_mandir}/man1/named-journalprint.1%{ext_man}
%{_mandir}/man1/nsec3hash.1%{ext_man}
%{_mandir}/man5/rndc.conf.5%{ext_man}
%{_mandir}/man8/ddns-confgen.8%{ext_man}
%{_mandir}/man8/rndc.8%{ext_man}
%{_mandir}/man8/rndc-confgen.8%{ext_man}
%{_mandir}/man8/tsig-keygen.8%{ext_man}

%changelog
