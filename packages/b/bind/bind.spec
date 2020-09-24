#
# spec file for package bind
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


# Don't forget to update the package names also in baselibs.conf
# Note that the sonums are LIBINTERFACE - LIBAGE
%define bind9_sonum 1600
%define libbind9 libbind9-%{bind9_sonum}
%define dns_sonum 1605
%define libdns libdns%{dns_sonum}
%define irs_sonum 1601
%define libirs libirs%{irs_sonum}
%define isc_sonum 1606
%define libisc libisc%{isc_sonum}
%define isccc_sonum 1600
%define libisccc libisccc%{isccc_sonum}
%define isccfg_sonum 1600
%define libisccfg libisccfg%{isccfg_sonum}
%define libns_sonum 1604
%define libns libns%{libns_sonum}

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
Version:        9.16.6
Release:        0
Summary:        Domain Name System (DNS) Server (named)
License:        MPL-2.0
Group:          Productivity/Networking/DNS/Servers
URL:            http://isc.org/sw/bind/
Source:         ftp://ftp.isc.org/isc/bind9/%{version}/bind-%{version}.tar.xz
Source1:        vendor-files.tar.bz2
Source2:        baselibs.conf
Source3:        ftp://ftp.isc.org/isc/bind9/%{version}/bind-%{version}.tar.xz.sha512.asc
# from http://www.isc.org/about/openpgp/ ... changes yearly apparently.
Source4:        %{name}.keyring
Source9:        ftp://ftp.internic.net/domain/named.root
Source40:       dnszone-schema.txt
Source60:       dlz-schema.txt
# configuation files for systemd-tmpfiles
Source70:       bind.conf
Source71:       bind-chrootenv.conf
Source72:       named.conf
Patch51:        pie_compile.diff
Patch52:        named-bootconf.diff
Patch56:        bind-ldapdump-use-valid-host.patch
BuildRequires:  libcap-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  openldap2-devel
BuildRequires:  openssl
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-ply
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       %{name}-chrootenv
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
# named.init (systemd) calls start_daemon, so require it when using systemd
Requires:       (/sbin/start_daemon if systemd)
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

%package -n %{libbind9}
Summary:        BIND9 shared library used by BIND
Group:          System/Libraries

%description -n %{libbind9}
This library contains a few utility functions used by the BIND
server and utilities.

%package -n %{libdns}
Summary:        DNS library used by BIND
Group:          System/Libraries

%description -n %{libdns}
This subpackage contains the "DNS client" module. This is a higher
level API that provides an interface to name resolution, single DNS
transaction with a particular server, and dynamic update. Regarding
name resolution, it supports advanced features such as DNSSEC
validation and caching. This module supports both synchronous and
asynchronous mode.

It also contains the Advanced Database (ADB) and Simple Database
(SDB) APIs. ADB allows user-written routines to replace BIND’s
internal database function for both nominated and all zones. SDB
allows a user-written driver to supply zone data either from
alternate data sources (for instance, a relational database) or using
specialized algorithms (for instance, for load-balancing).
[Book links for SDB: "Pro DNS and BIND 10", R. Aitchison, Apress]

%package -n %{libirs}
Summary:        The BIND Information Retrieval System library
Group:          System/Libraries

%description -n %{libirs}
libirs provides an interface to parse the traditional resolv.conf file and an
"advanced" configuration file related to the DNS library for configuration
parameters that would be beyond the capability of the resolv.conf file.
Specifically, it is intended to provide DNSSEC related configuration
parameters. By default, the path to this configuration file is %{_sysconfdir}/dns.conf.

%package -n libirs-devel
Summary:        Development files for IRS
Group:          Development/Libraries/C and C++
Requires:       %{libirs} = %{version}

%description -n libirs-devel
libirs provides an interface to parse the traditional resolv.conf file and an
"advanced" configuration file related to the DNS library for configuration
parameters that would be beyond the capability of the resolv.conf file.  This
subpackage contains the header files needed for building programs with it.

%package -n %{libisc}
Summary:        ISC shared library used by BIND
Group:          System/Libraries
Provides:       bind-libs = %{version}-%{release}
Obsoletes:      bind-libs < %{version}-%{release}

%description -n %{libisc}
This library contains miscellaneous utility function used by the BIND
server and utilities. It includes functions for assertion handling,
balanced binary (AVL) trees, bit masks comparison, event based
programs, heap-based priority queues, memory handling, and program
logging.

%package -n %{libns}
Summary:        NS shared library used by BIND
Group:          System/Libraries

%description -n %{libns}
This library contains miscellaneous utility function used by the BIND
server and utilities.

%package -n %{libisccc}
Summary:        Command Channel Library used by BIND
Group:          System/Libraries

%description -n %{libisccc}
This library is used for communicating with BIND servers'
administrative command channel (port 953 by default).

%package -n %{libisccfg}
Summary:        Exported ISC configuration shared library
Group:          System/Libraries

%description -n %{libisccfg}
This BIND library contains the configuration file parser.

%package chrootenv
Summary:        Chroot environment for BIND named
# We need the named user and group, have only one authoritative place
Group:          Productivity/Networking/DNS/Servers
Requires(pre):  %{name}

%description chrootenv
This package contains all directories and files which are common to the
chroot environment of BIND named.  Most is part of the
structure below %{_localstatedir}/lib/named.

%package devel
Summary:        Development Libraries and Header Files of BIND
Group:          Development/Libraries/C and C++
Requires:       %{libbind9} = %{version}
Requires:       %{libdns} = %{version}
Requires:       %{libirs} = %{version}
Requires:       %{libisccc} = %{version}
Requires:       %{libisccfg} = %{version}
Requires:       %{libisc} = %{version}
Requires:       %{libns} = %{version}
Provides:       bind8-devel
Provides:       bind9-devel
Obsoletes:      bind8-devel < %{version}
Obsoletes:      bind9-devel < %{version}

%description devel
This package contains the header files, libraries, and documentation
for building programs using the libraries of the Berkeley Internet Name
Domain (BIND) Domain Name System implementation of the Domain Name
System (DNS) protocols.

%package doc
Summary:        BIND documentation
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Documentation of the Berkeley Internet Name Domain (BIND) Domain Name
System implementation of the Domain Name System (DNS) protocols.  This
includes also the BIND Administrator Reference Manual (ARM).

%package utils
Summary:        Utilities to query and test DNS
# Needed for dnssec parts
Group:          Productivity/Networking/DNS/Utilities
Requires:       python3-bind = %{version}
Provides:       bind9-utils
Provides:       bindutil
Provides:       dns_utils
Obsoletes:      bind9-utils < %{version}
Obsoletes:      bindutil < %{version}

%description utils
This package includes the utilities "host", "dig", and "nslookup" used to
test and query the Domain Name System (DNS).  The Berkeley Internet
Name Domain (BIND) DNS server is found in the package named bind.

%package -n python3-bind
Summary:        A module allowing rndc commands to be sent from Python programs
Group:          Development/Languages/Python
Requires:       python3
Requires:       python3-ply
BuildArch:      noarch

%description -n python3-bind
This package provides a module which allows commands to be sent to rndc directly from Python programs.

%prep
%setup -q -a1
%patch51 -p1
%patch52 -p1
%patch56 -p1

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
for file in docu/README tools/createNamedConfInclude config/{README,named.conf} init/named system/named.init sysconfig/{named-common,named-named,syslog-named}; do
	replaceStrings ${file}
done
popd

%build
autoreconf -fvi
export CFLAGS="%{optflags} -DNO_VERSION_DATE"
%configure \
	--with-python=%{_bindir}/python3 \
	--includedir=%{_includedir}/bind \
	--disable-static \
	--with-openssl \
	--enable-threads \
	--with-libtool \
	--with-libxml2 \
	--with-libjson \
	--with-libidn2 \
	--with-dlz-mysql \
	--with-dlz-ldap \
	--with-randomdev=/dev/urandom \
	--enable-ipv6 \
	--with-pic \
	--disable-openssl-version-check \
	--with-tuning=large \
	--with-geoip \
	--with-dlopen \
	--with-gssapi=yes \
	--disable-isc-spnego \
	--enable-fixed-rrset \
	--enable-filter-aaaa \
%if %{with_systemd}
        --with-systemd \
%endif
	--enable-full-report
# disable rpath
sed -i '
  s|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g
  s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g
' libtool
make %{?_smp_mflags}
%if %{with_systemd}
%sysusers_generate_pre %{SOURCE72} named
%endif

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
	%{buildroot}%{_localstatedir}/lib/named/{etc/named.d,dev,dyn,log,master,slave,var/{lib,run/named}} \
	%{buildroot}%{_mandir}/{man1,man3,man5,man8} \
	%{buildroot}%{_fillupdir} \
	%{buildroot}/%{_rundir} \
	%{buildroot}%{_includedir}/bind/dns \
	%{buildroot}%{_libexecdir}/bind
%if %{with_sfw2}
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services
%endif
%make_install
# install errno2result.h, some dynamic DB plugins could use it.
install -m 0755 -d %{buildroot}%{_includedir}/isc/
install -m 0644 lib/isc/unix/errno2result.h %{buildroot}%{_includedir}/isc/
install -m 0644 .clang-format.headers %{buildroot}/%{_defaultdocdir}/bind

# remove useless .la files
rm -f %{buildroot}/%{_libdir}/lib*.{la,a}
mv vendor-files/config/named.conf %{buildroot}/%{_sysconfdir}
mv vendor-files/config/bind.reg %{buildroot}/%{_sysconfdir}/slp.reg.d
mv vendor-files/config/rndc-access.conf %{buildroot}/%{_sysconfdir}/named.d
for file in named.conf.include; do
	touch %{buildroot}/%{_sysconfdir}/${file}
done

%if %{with_systemd}
	for file in named; do
        	install -D -m 0644 vendor-files/system/${file}.service %{buildroot}%{_unitdir}/${file}.service
                install -m 0755 vendor-files/system/${file}.init %{buildroot}/usr/sbin/${file}.init
		ln -s /sbin/service %{buildroot}%{_sbindir}/rc${file}
	done
	install -D -m 0644 %{SOURCE70} %{buildroot}%{_prefix}/lib/tmpfiles.d/bind.conf
	install -D -m 0644 %{SOURCE71} %{buildroot}%{_prefix}/lib/tmpfiles.d/bind-chrootenv.conf
	install -D -m 0644 ${RPM_SOURCE_DIR}/named.root %{buildroot}%{_datadir}/factory%{_localstatedir}/lib/named/root.hint
	install -m 0644 vendor-files/config/{127.0.0,localhost}.zone %{buildroot}%{_datadir}/factory%{_localstatedir}/lib/named
	install -m 0644 bind.keys %{buildroot}%{_datadir}/factory%{_localstatedir}/lib/named/named.root.key
%else
	for file in named; do
		install -m 0754 vendor-files/init/${file} %{buildroot}%{_initddir}/${file}
		ln -sf %{_initddir}/${file} %{buildroot}%{_sbindir}/rc${file}
	done
%endif
install -m 0644 ${RPM_SOURCE_DIR}/named.root %{buildroot}%{_localstatedir}/lib/named/root.hint
mv vendor-files/config/{127.0.0,localhost}.zone %{buildroot}%{_localstatedir}/lib/named
install -m 0754 vendor-files/tools/createNamedConfInclude %{buildroot}/%{_datadir}/bind
install -m 0755 vendor-files/tools/bind.genDDNSkey %{buildroot}/%{_bindir}/genDDNSkey
cp -a vendor-files/docu/BIND.desktop %{buildroot}/%{_datadir}/susehelp/meta/Administration/System
cp -p ${RPM_SOURCE_DIR}/dnszone-schema.txt %{buildroot}/%{_sysconfdir}/openldap/schema/dnszone.schema
cp -p "%{SOURCE60}" "%{buildroot}/%{_sysconfdir}/openldap/schema/dlz.schema"
install -m 0754 vendor-files/tools/ldapdump %{buildroot}/%{_datadir}/bind
find %{buildroot}/%{_libdir} -type f -name '*.so*' -print0 | xargs -0 chmod 0755
touch %{buildroot}%{_localstatedir}/lib/named%{_sysconfdir}/{localtime,named.conf.include,named.d/rndc.access.conf}
touch %{buildroot}%{_localstatedir}/lib/named/dev/log
ln -s ../.. %{buildroot}%{_localstatedir}/lib/named%{_localstatedir}/lib/named
ln -s ../log %{buildroot}%{_localstatedir}/lib/named%{_localstatedir}
ln -s ..%{_localstatedir}/lib/named%{_localstatedir}/run/named %{buildroot}/run
for file in named-common named-named syslog-named; do
	install -m 0644 vendor-files/sysconfig/${file} %{buildroot}%{_fillupdir}/sysconfig.${file}
done
%if %{with_sfw2}
install -m 644 vendor-files/sysconfig/SuSEFirewall.named %{buildroot}/%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/bind
%endif
# Cleanup doc
rm doc/misc/Makefile*
find doc/arm -type f ! -name '*.html' -print0 | xargs -0 rm -f
# Create doc as we want it in bind and not bind-doc
cp -a vendor-files/docu/README %{buildroot}/%{_defaultdocdir}/bind/README.%{VENDOR}
mkdir -p vendor-files/config/ISC-examples
cp -a bin/tests/*.conf* vendor-files/config/ISC-examples
for file in CHANGES COPYRIGHT README version contrib doc/{arm,misc} vendor-files/config; do
	basename=$( basename ${file})
	cp -a ${file} %{buildroot}/%{_defaultdocdir}/bind/${basename}
	echo "%doc %{_defaultdocdir}/bind/${basename}" >>filelist-bind-doc
done
# ---------------------------------------------------------------------------
install -m 0644 bind.keys %{buildroot}%{_localstatedir}/lib/named/named.root.key
%if %{with_systemd}
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE72} %{buildroot}%{_sysusersdir}/
%endif

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
# make sure systemctl knows about the service even though it's not a systemd service
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

%post   -n %{libbind9} -p /sbin/ldconfig
%postun -n %{libbind9} -p /sbin/ldconfig
%post   -n %{libdns} -p /sbin/ldconfig
%postun -n %{libdns} -p /sbin/ldconfig
%post   -n %{libirs} -p /sbin/ldconfig
%postun -n %{libirs} -p /sbin/ldconfig
%post   -n %{libisc} -p /sbin/ldconfig
%postun -n %{libisc} -p /sbin/ldconfig
%post   -n %{libns} -p /sbin/ldconfig
%postun -n %{libns} -p /sbin/ldconfig
%post   -n %{libisccc} -p /sbin/ldconfig
%postun -n %{libisccc} -p /sbin/ldconfig
%post   -n %{libisccfg} -p /sbin/ldconfig
%postun -n %{libisccfg} -p /sbin/ldconfig
%post chrootenv
%{fillup_only -nsa named common}
%{fillup_only -nsa syslog named}
%if %{with_systemd}
%tmpfiles_create bind-chrootenv.conf
%endif

%files
%license LICENSE
%attr(0644,root,named) %config(noreplace) /%{_sysconfdir}/named.conf
%dir %{_sysconfdir}/slp.reg.d
%attr(0644,root,root) %config /%{_sysconfdir}/slp.reg.d/bind.reg
%attr(0644,root,named) %ghost /%{_sysconfdir}/named.conf.include
%if %{with_systemd}
%config %{_unitdir}/named.service
%{_sbindir}/named.init
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
%{_sbindir}/named-checkconf
%{_sbindir}/named-checkzone
%{_sbindir}/named-compilezone
%dir %{_libdir}/named
%{_libdir}/named/filter-aaaa.so
%{_mandir}/man1/named-rrchecker.1%{ext_man}
%{_mandir}/man5/named.conf.5%{ext_man}
%{_mandir}/man8/named-checkconf.8%{ext_man}
%{_mandir}/man8/named-checkzone.8%{ext_man}
%{_mandir}/man8/named.8%{ext_man}
%{_mandir}/man8/filter-aaaa.8%{ext_man}
%dir %{_datadir}/bind
%{_datadir}/bind/createNamedConfInclude
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

%files -n %{libbind9}
%{_libdir}/libbind9.so.%{bind9_sonum}*

%files -n %{libdns}
%{_libdir}/libdns.so.%{dns_sonum}*

%files -n %{libirs}
%{_libdir}/libirs.so.%{irs_sonum}*

%files -n libirs-devel
%{_libdir}/libirs.so

%files -n %{libisc}
%{_libdir}/libisc.so.%{isc_sonum}*

%files -n %{libns}
%{_libdir}/libns.so.%{libns_sonum}*

%files -n %{libisccc}
%{_libdir}/libisccc.so.%{isccc_sonum}*

%files -n %{libisccfg}
%{_libdir}/libisccfg.so.%{isccfg_sonum}*

%files chrootenv
%if %{with_systemd}
%{_prefix}/lib/tmpfiles.d/bind-chrootenv.conf
%endif
%dir %{_var}/lib/named%{_sysconfdir}
%dir %{_var}/lib/named%{_sysconfdir}/named.d
%dir %{_var}/lib/named/dev
%dir %{_var}/lib/named%{_localstatedir}
%dir %{_var}/lib/named%{_localstatedir}/lib
%dir %{_var}/lib/named%{_localstatedir}/run
%attr(-,named,named) %dir %{_var}/lib/named/log
%ghost %{_var}/lib/named%{_sysconfdir}/named.d/rndc.access.conf
%ghost %{_var}/lib/named/dev/log
%attr(0666, root, root) %dev(c, 1, 3) %{_var}/lib/named/dev/null
%attr(0666, root, root) %dev(c, 1, 8) %{_var}/lib/named/dev/random
%attr(0664, root, root) %dev(c, 1, 9) %{_var}/lib/named/dev/urandom
%{_var}/lib/named%{_localstatedir}/lib/named
%{_var}/lib/named%{_localstatedir}/log
%{_fillupdir}/sysconfig.named-common
%{_fillupdir}/sysconfig.syslog-named
%ghost %{_var}/lib/named%{_sysconfdir}/localtime
%attr(0644,root,named) %ghost %{_var}/lib/named%{_sysconfdir}/named.conf.include
%attr(-,named,named) %dir %{_var}/lib/named%{_localstatedir}/run/named

%files devel
%dir %{_includedir}/isc
%{_includedir}/isc/errno2result.h
%{_libdir}/libbind9.so
%{_libdir}/libdns.so
%{_libdir}/libisc*.so
%{_libdir}/libns.so
%{_includedir}/bind

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
%{_sbindir}/ddns-confgen
%{_sbindir}/dnssec-dsfromkey
%{_sbindir}/dnssec-importkey
%{_sbindir}/dnssec-keyfromlabel
%{_sbindir}/dnssec-keygen
%{_sbindir}/dnssec-revoke
%{_sbindir}/dnssec-settime
%{_sbindir}/dnssec-signzone
%{_sbindir}/dnssec-verify
%{_sbindir}/dnssec-checkds
%{_sbindir}/dnssec-coverage
%{_sbindir}/dnssec-keymgr
%{_sbindir}/dnssec-cds
# %%{_sbindir}/genrandom
# %%{_sbindir}/isc-hmac-fixup
%{_sbindir}/named-journalprint
%{_sbindir}/nsec3hash
%{_sbindir}/rndc
%{_sbindir}/rndc-confgen
%{_sbindir}/tsig-keygen
%dir %doc %{_defaultdocdir}/bind
%{_defaultdocdir}/bind/README.%{VENDOR}
%{_defaultdocdir}/bind/.clang-format.headers
%{_mandir}/man1/arpaname.1%{ext_man}
%{_mandir}/man1/delv.1%{ext_man}
%{_mandir}/man1/dig.1%{ext_man}
%{_mandir}/man1/host.1%{ext_man}
%{_mandir}/man1/mdig.1%{ext_man}
%{_mandir}/man1/nslookup.1%{ext_man}
%{_mandir}/man1/nsupdate.1%{ext_man}
# %%{_mandir}/man1/dnstap-read.1%%{ext_man}
%{_mandir}/man5/rndc.conf.5%{ext_man}
%{_mandir}/man8/ddns-confgen.8%{ext_man}
%{_mandir}/man8/dnssec-dsfromkey.8%{ext_man}
%{_mandir}/man8/dnssec-importkey.8%{ext_man}
%{_mandir}/man8/dnssec-keyfromlabel.8%{ext_man}
%{_mandir}/man8/dnssec-keygen.8%{ext_man}
%{_mandir}/man8/dnssec-revoke.8%{ext_man}
%{_mandir}/man8/dnssec-settime.8%{ext_man}
%{_mandir}/man8/dnssec-signzone.8%{ext_man}
%{_mandir}/man8/dnssec-verify.8%{ext_man}
%{_mandir}/man8/dnssec-checkds.8%{ext_man}
%{_mandir}/man8/dnssec-coverage.8%{ext_man}
%{_mandir}/man8/dnssec-keymgr.8%{ext_man}
%{_mandir}/man8/dnssec-cds.8%{ext_man}
# %%{_mandir}/man8/named-nzd2nzf.8%%{ext_man}
# %%{_mandir}/man8/genrandom.8%%{ext_man}
# %%{_mandir}/man8/isc-hmac-fixup.8%%{ext_man}
%{_mandir}/man8/named-journalprint.8%{ext_man}
%{_mandir}/man8/nsec3hash.8%{ext_man}
%{_mandir}/man8/rndc.8%{ext_man}
%{_mandir}/man8/rndc-confgen.8%{ext_man}
%{_mandir}/man8/named-compilezone.8%{ext_man}
%{_mandir}/man8/tsig-keygen.8%{ext_man}

%files -n python3-bind
%{python3_sitelib}/isc
%{python3_sitelib}/isc-*.egg-info

%changelog
