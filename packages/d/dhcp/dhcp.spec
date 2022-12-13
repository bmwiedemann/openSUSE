#
# spec file for package dhcp
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


%define isc_version   4.4.2-P1
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if 0%{?usrmerged}
%define sbindir %{_sbindir}
%else
%define sbindir /sbin
%endif
%if 0%{?suse_version} >= 1330
%bcond_without sysusers
%else
%bcond_with sysusers
%endif
Name:           dhcp
Version:        4.4.2.P1
Release:        0
Summary:        Common Files Used by ISC DHCP Software
License:        MPL-2.0
Group:          Productivity/Networking/Boot/Servers
URL:            https://www.isc.org/software/dhcp
Source0:        https://ftp.isc.org/isc/dhcp/%{isc_version}/dhcp-%{isc_version}.tar.gz
Source1:        https://ftp.isc.org/isc/dhcp/%{isc_version}/dhcp-%{isc_version}.tar.gz.asc
Source2:        %{name}.keyring
#
Source10:       dhcpd.script
Source11:       dhcrelay.script
Source12:       dhcpd.service
Source13:       dhcpd6.service
Source14:       dhcrelay.service
Source15:       dhcrelay6.service
Source17:       sysconfig.dhcpd
Source18:       sysconfig.dhcrelay
Source19:       if-up.d.dhcpd-restart-hook
#
Source20:       dhclient.conf
Source21:       dhclient6.conf
Source22:       dhcpd.conf
Source23:       dhcpd6.conf
Source26:       sysconfig.syslog-dhcpd
Source27:       dhclient-script
#
Source41:       dhcp.README
Source43:       DDNS-howto.txt
Source44:       contrib.tar.gz
Source45:       examples.tar.gz
Source46:       slp.reg.d.dhcp.reg
Source47:       dhcp-user.conf
Patch1:         0001-dhcp-4.1.1-default-paths.patch
# paranoia patch is included now, but not the
# additional patch by thomas@suse.de not ...
Patch2:         0002-dhcp-4.1.1-paranoia.patch
Patch3:         0003-dhcp-4.2.2-man-includes.patch
Patch4:         0004-dhcp-4.1.1-tmpfile.patch
Patch5:         0005-dhcp-4.1.1-dhclient-exec-filedes.patch
Patch6:         0006-dhcp-4.3.2-dhclient-send-hostname-or-fqdn.patch
# PATCH-FIX-UPSTREAM lpf-bind-msg-fix bnc#617795
Patch7:         0007-dhcp-4.1.1-P1-lpf-bind-msg-fix.patch
# PATCH-FIX-SLE dhclient-option-checks bnc#675052
Patch8:         0008-dhcp-4.2.2-dhclient-option-checks.patch
# PATCH-FIX-OPENSUSE close-on-exec bnc#732910
Patch9:         0009-dhcp-4.2.6-close-on-exec.patch
# PATCH-FIX-OPENSUSE quiet-dhclient bnc#711420
Patch10:        0010-dhcp-4.2.2-quiet-dhclient.patch
# PATCH-FIX-OPENSUSE dhcp-4.2.x-chown-server-leases bnc#868253
Patch12:        0012-dhcp-4.2.x-chown-server-leases.bnc868253.patch
# PATCH-FIX-SLE dhclient6-unsigned-lifetimes-for-script bsc#926159
Patch14:        0014-dhclient6-unsigned-lifetimes-for-script-bsc-926159.patch
# PATCH-FIX-SLE Expose-next-server-DHCPv4-option-to-dhclient-script bsc#928390
Patch15:        0015-Expose-next-server-DHCPv4-option-to-dhclient-script.patch
# PATCH-FIX-SLE infiniband-support bnc#870535,bsc#909189,bsc#910984
Patch16:        0016-infiniband-support.patch
# PATCH-FIX-SLE server-no-success-report-before-send bsc#919959
Patch17:        0017-server-no-success-report-before-send.919959.patch
# PATCH-FIX-SLE client-fail-on-script-pre-init-error bsc#912098
Patch18:        0018-client-fail-on-script-pre-init-error-bsc-912098.patch
# PATCH-FIX-SLE dhcp-4.2.4-P1-interval bsc#947780
Patch20:        0020-dhcp-4.x.x-fixed-improper-lease-duration-checking.patch
Patch21:        0021-dhcp-ip-family-symlinks.patch
Patch22:        dhcp-CVE-2022-2928.patch
Patch23:        dhcp-CVE-2022-2929.patch
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  libtool
BuildRequires:  openldap2-devel
%if %{with sysusers}
BuildRequires:  sysuser-tools
%endif

%package server
Summary:        ISC DHCP Server
Group:          Productivity/Networking/Boot/Servers
Requires:       dhcp = %{version}
Requires(post): %fillup_prereq
%{?systemd_ordering}
%if 0%{?suse_version} < 1500
Requires:       net-tools
%endif
%if %{with sysusers}
%sysusers_requires
%else
Requires(pre):  shadow
%endif

%package client
Summary:        ISC DHCP Client
Group:          Productivity/Networking/Boot/Clients
Requires:       %{_bindir}/getent
Requires:       dhcp = %{version}
Requires:       iproute2
Requires:       iputils
%if 0%{?suse_version} >= 1330
Requires:       /usr/bin/hostname
%else
Requires:       net-tools
%endif

%package relay
Summary:        ISC DHCP Relay Agent
Group:          Productivity/Networking/Boot/Servers
Requires:       dhcp = %{version}
Requires(post): %fillup_prereq
%{?systemd_ordering}
%if 0%{?suse_version} < 1500
Requires:       net-tools
%endif

%package devel
Summary:        Header Files and Libraries for dhcpctl API
Group:          Development/Libraries/C and C++
Requires:       dhcp = %{version}

%package doc
Summary:        Documentation
Group:          Productivity/Networking/Boot/Servers

%description
This package contains common programs used by both the ISC DHCP
server ("dhcp-server" package) and client ("dhcp-client") as the
omshell and common manual pages.

%description server
This package contains the ISC DHCP server.

%description client
This is an alternative DHCP client, the ISC DHCP client for Linux. Like
"dhcpcd" (the client that is installed by default), it can be used to
configure the network setup.  IP address, hostname, routing,
nameserver, netmask, and broadcast can be dynamically assigned while
booting the machine.

It is configurable via the configuration file %{_sysconfdir}/dhclient.conf and
you can define your own 'hooks' to be used by the /sbin/dhclient-script
(which is called by the daemon).

%description relay
This is the ISC DHCP relay agent. It can be used as a 'gateway' for
DHCP messages across physical network segments. This is necessary
because requests can be broadcast, and they will normally not be
routed.

%description doc
This package contains additional documentation files provided with
the software. The manual pages are in the corresponding packages.

%description devel
This package contains all of the libraries and headers for developing
with the Internet Software Consortium (ISC) dhcpctl API.

%prep
if test "%version" != $(echo %isc_version | tr "-" "."); then
   echo "error: %%version and %%isc_version are not in sync."
   exit 1
fi
%setup -q -n %{name}-%{isc_version} -a 44 -a 45
##
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9
%patch10 -p1
%patch12 -p1
%patch14
%patch15 -p1
%patch16
%patch17 -p1
%patch18 -p1
%patch20
%patch21
%patch22
%patch23
##
find . -type f -name \*.cat\* -exec rm -f {} \;
dos2unix contrib/ms2isc/*
# Remove GPL licensed files to make sure,
# they're not used to build (bnc#714004).
pushd bind
gunzip -c bind.tar.gz | tar xf -
rm -rf bind-*/contrib/dbus
bind_dir=$(ls -1d bind-*)
for i in %{_datadir}/automake-*/config.{sub,guess} ; do
	install -v -m755 $i $bind_dir/
done
# use the year from source gzip header instead of current one to make reproducible rpms
year=$(perl -e 'sysread(STDIN, $h, 8); print (1900+(gmtime(unpack("l",substr($h,4))))[5])' < bind.tar.gz)
sed -i "s/stdout, copyright, year/stdout, copyright, \"-$year\"/" $bind_dir/lib/dns/gen.c
popd
##

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
CFLAGS="%{optflags} -D_GNU_SOURCE -W -Wall -Wno-unused -fcommon -fno-strict-aliasing"
%ifarch ppc ppc64 s390x
  # bugs 134590, 171532
  CFLAGS="$CFLAGS -fsigned-char"
%endif
%ifarch ia64 %{sparc} alpha s390x ppc64 x86_64
  CFLAGS="$CFLAGS -fPIE"
%else
  CFLAGS="$CFLAGS -fpie"
%endif
LDFLAGS="-Wl,-z,relro,-z,now -pie"
FFLAGS="$CFLAGS"
CXXFLAGS="$CFLAGS"
export CFLAGS LDFLAGS FFLAGS CXXFLAGS
%configure \
	--enable-dhcpv6 \
	--enable-failover \
	--enable-paranoia \
	--enable-early-chroot \
	--disable-libtool \
	--enable-log-pid \
	--enable-binary-leases \
	--with-ldap \
	--with-ldapcrypto \
	--with-cli-pid-file=%{_rundir}/dhclient.pid \
	--with-cli-lease-file=%{_localstatedir}/lib/dhcp/dhclient.leases \
	--with-cli6-pid-file=%{_rundir}/dhclient6.pid \
	--with-cli6-lease-file=%{_localstatedir}/lib/dhcp6/dhclient.leases \
	--with-srv-pid-file=%{_rundir}/dhcpd.pid \
	--with-srv-lease-file=%{_localstatedir}/lib/dhcp/db/dhcpd.leases \
	--with-srv6-pid-file=%{_rundir}/dhcpd6.pid \
	--with-srv6-lease-file=%{_localstatedir}/lib/dhcp6/db/dhcpd6.leases
#
: building bind sources
%if 0%{?!make_build:1}
# SLE-12 compatbility still needed as of October 2021
%define make_build %{__make} %{?_smp_mflags}
%endif
%make_build -j1 -C bind all
cat bind/configure.log
cat bind/build.log
cat bind/install.log
: building dhcp sources
%make_build
%if %{with sysusers}
%sysusers_generate_pre %{SOURCE47} dhcp-server dhcp-user.conf
%endif

%check
# check example config, see if it runs
./server/dhcpd -4 -t -cf $RPM_SOURCE_DIR/dhcpd.conf
./server/dhcpd -6 -t -cf $RPM_SOURCE_DIR/dhcpd6.conf
# check syntax in our scripts
bash -n $RPM_SOURCE_DIR/dhcpd.script
bash -n $RPM_SOURCE_DIR/dhcrelay.script
bash -n $RPM_SOURCE_DIR/dhclient-script

%install
%make_install
#
# directories
install -d -m0755 %{buildroot}/sbin
install -d -m0755 %{buildroot}%{_sysconfdir}/dhcpd{,6}.d
install -d -m0755 %{buildroot}%{_sysconfdir}/openldap/schema
install -d -m0755 %{buildroot}%{_localstatedir}/run
install -d -m0755 %{buildroot}%{_fillupdir}
# chroot jail
install -d -m0755 %{buildroot}%{_localstatedir}/lib/{dhcp,dhcp6}%{_sysconfdir}
install -d -m0755 %{buildroot}%{_localstatedir}/lib/{dhcp,dhcp6}/dev
install -d -m0755 %{buildroot}%{_localstatedir}/lib/{dhcp,dhcp6}/%{_lib}
install -d -m0755 %{buildroot}%{_localstatedir}/lib/{dhcp,dhcp6}/run
install -d -m0755 %{buildroot}%{_localstatedir}/lib/{dhcp,dhcp6}/db
%if !0%{?usrmerged}
# move the dhclient binary to /sbin
mv -f %{buildroot}%{_sbindir}/dhclient %{buildroot}/sbin/
%endif
# provide a ...6 link, so we know it supports DHCPv6
ln -sf dhcpd      %{buildroot}%{_sbindir}/dhcpd6
ln -sf dhcrelay   %{buildroot}%{_sbindir}/dhcrelay6
ln -sf dhclient   %{buildroot}%{sbindir}/dhclient6
# install our adopted config examples and dhclient-script:
install    -m0644 $RPM_SOURCE_DIR/dhcpd.conf      %{buildroot}%{_sysconfdir}/
install    -m0644 $RPM_SOURCE_DIR/dhcpd6.conf     %{buildroot}%{_sysconfdir}/
install    -m0644 $RPM_SOURCE_DIR/dhclient.conf   %{buildroot}%{_sysconfdir}/
install    -m0644 $RPM_SOURCE_DIR/dhclient6.conf  %{buildroot}%{_sysconfdir}/
install    -m0754 $RPM_SOURCE_DIR/dhclient-script %{buildroot}%{sbindir}/
# helper / wrapper scripts
install -d -m0755 %{buildroot}%{_libexecdir}/dhcp
install    -m0755 $RPM_SOURCE_DIR/dhcpd.script              \
                  %{buildroot}%{_libexecdir}/dhcp/dhcpd
sed -e 's,@LIBDIR@,%{_lib},g' -i %{buildroot}%{_libexecdir}/dhcp/dhcpd
install    -m0755 $RPM_SOURCE_DIR/dhcrelay.script           \
                  %{buildroot}%{_libexecdir}/dhcp/dhcrelay
# service units
install -d -m0755 %{buildroot}%{_unitdir}
install    -m0644 $RPM_SOURCE_DIR/dhcpd.service             \
                  %{buildroot}%{_unitdir}/dhcpd.service
install    -m0644 $RPM_SOURCE_DIR/dhcpd6.service            \
                  %{buildroot}%{_unitdir}/dhcpd6.service
install    -m0644 $RPM_SOURCE_DIR/dhcrelay.service          \
                  %{buildroot}%{_unitdir}/dhcrelay.service
install    -m0644 $RPM_SOURCE_DIR/dhcrelay6.service         \
                  %{buildroot}%{_unitdir}/dhcrelay6.service
sed -e 's,@LIBEXECDIR@,%{_libexecdir},g' -i %{buildroot}%{_unitdir}/d*
# rcservice links
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcdhcpd
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcdhcpd6
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcdhcrelay
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcdhcrelay6
# rcservice actions
legacy_actionsdir=%{buildroot}%{_libexecdir}/initscripts/legacy-actions
cat >dhcpd.action <<'EOF'
#!/bin/bash
exec %{_libexecdir}/dhcp/dhcpd -4 ${0##*/}
EOF
install -d -m0755 ${legacy_actionsdir}/dhcpd
install    -m0755 dhcpd.action  ${legacy_actionsdir}/dhcpd/syntax-check
ln -sf            syntax-check  ${legacy_actionsdir}/dhcpd/check-syntax
ln -sf            syntax-check  ${legacy_actionsdir}/dhcpd/check-lease
rm -f             dhcpd.action
cat >dhcpd.action <<'EOF'
#!/bin/bash
exec %{_libexecdir}/dhcp/dhcpd -6 ${0##*/}
EOF
install -d -m0755 ${legacy_actionsdir}/dhcpd6
install    -m0755 dhcpd.action  ${legacy_actionsdir}/dhcpd6/syntax-check
ln -sf            syntax-check  ${legacy_actionsdir}/dhcpd6/check-syntax
ln -sf            syntax-check  ${legacy_actionsdir}/dhcpd6/check-lease
rm -f             dhcpd.action
# sysconfig files
install    -m0644 $RPM_SOURCE_DIR/sysconfig.dhcpd           \
                  %{buildroot}%{_fillupdir}/
install    -m0644 $RPM_SOURCE_DIR/sysconfig.syslog-dhcpd    \
                  %{buildroot}%{_fillupdir}/
install    -m0644 $RPM_SOURCE_DIR/sysconfig.dhcrelay        \
                  %{buildroot}%{_fillupdir}/
# another config files and scripts
install    -m0644 contrib/ldap/dhcp.schema                       \
                  %{buildroot}%{_sysconfdir}/openldap/schema
install -d -m0755 %{buildroot}%{_sysconfdir}/sysconfig/network/if-up.d
install -d -m0755 %{buildroot}%{_sysconfdir}/sysconfig/network/scripts
install    -m0755 $RPM_SOURCE_DIR/if-up.d.dhcpd-restart-hook \
                  %{buildroot}%{_sysconfdir}/sysconfig/network/scripts/dhcpd-restart-hook
sed 's,@LIBEXECDIR@,%{_libexecdir},g' -i \
                  %{buildroot}%{_sysconfdir}/sysconfig/network/scripts/dhcpd-restart-hook
ln -sf            ../scripts/dhcpd-restart-hook \
                  %{buildroot}%{_sysconfdir}/sysconfig/network/if-up.d/60-dhcpd-restart-hook
# slp support
install -d -m0755 %{buildroot}%{_sysconfdir}/slp.reg.d
install    -m0644 $RPM_SOURCE_DIR/slp.reg.d.dhcp.reg           \
                  %{buildroot}%{_sysconfdir}/slp.reg.d/dhcp.reg
# fix manual page permissions
find %{buildroot}/%{_mandir} -type f | xargs chmod 644
# copy some documentation and examples from src dir
install    -m0644 $RPM_SOURCE_DIR/dhcp.README         README.SUSE
install    -m0644 $RPM_SOURCE_DIR/DDNS-howto.txt      .
cp                doc/examples/* ./examples/
rm -f             doc/{References.xml,Makefile*}
rm -f             contrib/dhcp.spec
rm -f             %{buildroot}%{_sysconfdir}/{dhcpd,dhclient}.conf.example
find contrib doc/examples -type f | xargs chmod -x
# install bind libs+includes needed for dhcp-devel
pushd bind
install -d -m0755 %{buildroot}%{_includedir}/dhcp/
for i in include/* ; do
	cp -r $i %{buildroot}%{_includedir}/dhcp/
done
install -d -m0755 %{buildroot}%{_libdir}/dhcp/
for l in lib/lib*.a ; do
	install -m0644 $l %{buildroot}%{_libdir}/dhcp/
done
popd
# move also all dhcp-devel files to dhcp subdirectories
mv %{buildroot}%{_includedir}/{dhcpctl,omapip} \
   %{buildroot}%{_includedir}/dhcp/
mv %{buildroot}%{_libdir}/lib*.* \
   %{buildroot}%{_libdir}/dhcp/
%if %{with sysusers}
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE47} %{buildroot}%{_sysusersdir}/
%endif

%if %{with sysusers}
%pre server -f dhcp-server.pre
%else

%pre server
getent passwd dhcpd >/dev/null || useradd -r -g nogroup -s /bin/false -c "DHCP server daemon" -d %{_localstatedir}/lib/dhcp dhcpd
%endif
%service_add_pre dhcpd.service
%service_add_pre dhcpd6.service

%post server
%{fillup_only -n   dhcpd dhcpd}
%{fillup_only -ans syslog dhcpd}
%service_add_post dhcpd.service
%service_add_post dhcpd6.service
# FIXME: update?
if [ $1 -gt 1 ]; then
    if grep -q '^DHCPD_RUN_AS=.*nobody' etc/sysconfig/dhcpd; then
	tmpfile=$(mktemp -q etc/sysconfig/dhcpd.XXXXXX)
	sed 's|^DHCPD_RUN_AS=.*|DHCPD_RUN_AS="dhcpd"|' etc/sysconfig/dhcpd \
	  > $tmpfile && mv $tmpfile etc/sysconfig/dhcpd
	rm -f $tmpfile
    fi
    if grep -q '^DHCPD_BINARY=.*dhcpd\..*' etc/sysconfig/dhcpd; then
	tmpfile=$(mktemp -q etc/sysconfig/dhcpd.XXXXXX)
	sed 's|^DHCPD_BINARY=.*|DHCPD_BINARY=""|' etc/sysconfig/dhcpd \
	  > $tmpfile && mv $tmpfile etc/sysconfig/dhcpd
	rm -f $tmpfile
    fi
fi

%preun server
%service_del_preun dhcpd.service
%service_del_preun dhcpd6.service

%postun server
%service_del_postun dhcpd.service
%service_del_postun dhcpd6.service

%pre relay
%service_add_pre dhcrelay.service
%service_add_pre dhcrelay6.service

%post relay
#
%{rename_sysconfig_variable -f etc/sysconfig/dhcrelay
	DHCRELAY6_LOWER_INTERFACES_ARGS DHCRELAY6_LOWER_INTERFACES}
%{rename_sysconfig_variable -f etc/sysconfig/dhcrelay
	DHCRELAY6_UPPER_INTERFACES_ARGS DHCRELAY6_UPPER_INTERFACES}
#
%{fillup_only -n dhcrelay dhcrelay}
%service_add_post dhcrelay.service
%service_add_post dhcrelay6.service

%preun relay
%service_del_preun dhcrelay.service
%service_del_preun dhcrelay6.service

%postun relay
%service_del_postun dhcrelay.service
%service_del_postun dhcrelay6.service

%files
%license LICENSE
%{_bindir}/omshell
%{_mandir}/man1/omshell.1%{?ext_man}
%{_mandir}/man5/dhcp-eval.5%{?ext_man}
%{_mandir}/man5/dhcp-options.5%{?ext_man}

%files server
%{_sbindir}/dhcpd
%{_sbindir}/dhcpd6
%{_sbindir}/rcdhcpd
%{_sbindir}/rcdhcpd6
%{_unitdir}/dhcpd.service
%{_unitdir}/dhcpd6.service
%if %{with sysusers}
%{_sysusersdir}/dhcp-user.conf
%endif
%dir %{_libexecdir}/initscripts/legacy-actions/dhcpd
%{_libexecdir}/initscripts/legacy-actions/dhcpd/*
%dir %{_libexecdir}/initscripts/legacy-actions/dhcpd6
%{_libexecdir}/initscripts/legacy-actions/dhcpd6/*
%config(noreplace) %{_sysconfdir}/dhcpd.conf
%config(noreplace) %{_sysconfdir}/dhcpd6.conf
%attr(755,root,root) %dir %config(noreplace) %ghost %{_sysconfdir}/dhcpd.d/
%attr(755,root,root) %dir %config(noreplace) %ghost %{_sysconfdir}/dhcpd6.d/
%dir %{_libexecdir}/dhcp
%{_libexecdir}/dhcp/dhcpd
%dir %{_localstatedir}/lib/dhcp
%dir %{_localstatedir}/lib/dhcp%{_sysconfdir}
%dir %{_localstatedir}/lib/dhcp/dev
%dir %{_localstatedir}/lib/dhcp/%{_lib}
%dir %{_localstatedir}/lib/dhcp/run
%attr(755,dhcpd,root) %dir %{_localstatedir}/lib/dhcp/db
%dir %{_localstatedir}/lib/dhcp6
%dir %{_localstatedir}/lib/dhcp6%{_sysconfdir}
%dir %{_localstatedir}/lib/dhcp6/dev
%dir %{_localstatedir}/lib/dhcp6/%{_lib}
%dir %{_localstatedir}/lib/dhcp6/run
%attr(755,dhcpd,root) %dir %{_localstatedir}/lib/dhcp6/db
%{_mandir}/man8/dhcpd.8%{?ext_man}
%{_mandir}/man5/dhcpd.conf.5%{?ext_man}
%{_mandir}/man5/dhcpd.leases.5%{?ext_man}
%dir %{_sysconfdir}/openldap
%dir %{_sysconfdir}/openldap/schema
%attr(0644, root, root) %config %{_sysconfdir}/openldap/schema/dhcp.schema
%dir %{_sysconfdir}/slp.reg.d
%config(noreplace) %{_sysconfdir}/slp.reg.d/dhcp.reg
%dir %{_sysconfdir}/sysconfig/network
%dir %{_sysconfdir}/sysconfig/network/scripts
%dir %{_sysconfdir}/sysconfig/network/if-up.d
%{_sysconfdir}/sysconfig/network/scripts/dhcpd-restart-hook
%{_sysconfdir}/sysconfig/network/if-up.d/60-dhcpd-restart-hook
%{_fillupdir}/sysconfig.dhcpd
%{_fillupdir}/sysconfig.syslog-dhcpd

%files doc
%doc README RELNOTES
%doc README.* DDNS-howto.txt doc/*
%doc contrib examples

%files client
%{sbindir}/dhclient
%{sbindir}/dhclient6
%{sbindir}/dhclient-script
%config(noreplace) %{_sysconfdir}/dhclient.conf
%config(noreplace) %{_sysconfdir}/dhclient6.conf
%{_mandir}/man5/dhclient.conf.5%{?ext_man}
%{_mandir}/man5/dhclient.leases.5%{?ext_man}
%{_mandir}/man8/dhclient.8%{?ext_man}
%{_mandir}/man8/dhclient-script.8%{?ext_man}
%dir %{_localstatedir}/lib/dhcp
%dir %{_localstatedir}/lib/dhcp6

%files relay
%{_sbindir}/dhcrelay
%{_sbindir}/dhcrelay6
%{_sbindir}/rcdhcrelay
%{_sbindir}/rcdhcrelay6
%dir %{_libexecdir}/dhcp
%{_libexecdir}/dhcp/dhcrelay
%{_unitdir}/dhcrelay.service
%{_unitdir}/dhcrelay6.service
%{_mandir}/man8/dhcrelay.8%{?ext_man}
%{_fillupdir}/sysconfig.dhcrelay

%files devel
%dir %{_libdir}/dhcp
%{_libdir}/dhcp/lib*
%dir %{_includedir}/dhcp
%{_includedir}/dhcp/*
%{_mandir}/man3/omapi.3%{?ext_man}
%{_mandir}/man3/dhcpctl.3%{?ext_man}

%changelog
