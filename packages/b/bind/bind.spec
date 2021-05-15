#
# spec file for package bind
#
# Copyright (c) 2021 SUSE LLC
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
Version:        9.16.15
Release:        0
Summary:        Domain Name System (DNS) Server (named)
License:        MPL-2.0
Group:          Productivity/Networking/DNS/Servers
URL:            https://www.isc.org/bind/
Source0:        https://downloads.isc.org/isc/bind9/%{version}/bind-%{version}.tar.xz
Source1:        https://downloads.isc.org/isc/bind9/%{version}/bind-%{version}.tar.xz.sha512.asc
Source2:        vendor-files.tar.bz2
# from http://www.isc.org/about/openpgp/ ... changes yearly apparently.
Source4:        %{name}.keyring
Source9:        ftp://ftp.internic.net/domain/named.root
Source40:       dnszone-schema.txt
Source60:       dlz-schema.txt
# configuation file for systemd-tmpfiles
Source70:       bind.conf
# configuation file for systemd-sysusers
Source72:       named.conf
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
BuildRequires:  python3-Sphinx
BuildRequires:  python3-ply
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libidn2)
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
%make_build
# special make for the Administrators Reference Manual
for d in arm; do
	make -C doc/${d} SPHINXBUILD=sphinx-build doc
done
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
install -m 0644 .clang-format.headers %{buildroot}/%{_defaultdocdir}/bind
# remove useless .h files
rm -rf %{buildroot}%{_includedir}

# remove useless .la files
rm -f %{buildroot}/%{_libdir}/lib*.{la,a}
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
# Cleanup doc
rm doc/misc/Makefile*
find doc/arm -type f ! -name '*.html' -delete
# Create doc as we want it in bind and not bind-doc
for file in vendor-files/docu/README*; do
	basename=$( basename ${file})
	cp -a ${file} %{buildroot}/%{_defaultdocdir}/bind/${basename}.%{VENDOR}
done

mkdir -p vendor-files/config/ISC-examples
cp -a bin/tests/*.conf* vendor-files/config/ISC-examples
for d in arm; do
	cp -a doc/${d}/_build %{buildroot}/%{_defaultdocdir}/bind/${d}
	echo "%doc %{_defaultdocdir}/bind/${d}" >>filelist-bind-doc
done
for file in CHANGES COPYRIGHT README version contrib doc/misc vendor-files/config; do
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

%post   -n bind-utils -p /sbin/ldconfig
%postun -n bind-utils -p /sbin/ldconfig

%files
%license LICENSE
%attr(0644,root,named) %config(noreplace) /%{_sysconfdir}/named.conf
%dir %{_sysconfdir}/slp.reg.d
%attr(0644,root,root) %config /%{_sysconfdir}/slp.reg.d/bind.reg
%if %{with_systemd}
%config %{_unitdir}/named.service
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
# Library files, formerly in their own, separate packages:
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
