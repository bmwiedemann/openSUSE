#
# spec file for package strongswan
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


Name:           strongswan
Version:        5.9.14
Release:        0
%define         upstream_version     %{version}
%define         strongswan_docdir    %{_docdir}/%{name}
%define         strongswan_libdir    %{_libdir}/ipsec
%define         strongswan_configs   %{_sysconfdir}/strongswan.d
%define         strongswan_datadir   %{_datadir}/strongswan
%define         strongswan_plugins   %{strongswan_libdir}/plugins
%define         strongswan_templates %{strongswan_datadir}/templates
%if 0
%bcond_without  tests
%else
%bcond_with     tests
%endif
%bcond_without  fipscheck
%ifarch %{ix86} ppc64le
%bcond_without  integrity
%else
%bcond_with     integrity
%endif
%bcond_without  farp
%bcond_without  afalg
%bcond_without  mysql
%bcond_without  sqlite
%bcond_without  gcrypt
%bcond_without  nm
%bcond_without  systemd
Summary:        IPsec-based VPN solution
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.strongswan.org/
Source0:        http://download.strongswan.org/strongswan-%{upstream_version}.tar.bz2
Source1:        http://download.strongswan.org/strongswan-%{upstream_version}.tar.bz2.sig
Source2:        %{name}.init.in
Source3:        %{name}-rpmlintrc
Source4:        README.SUSE
Source5:        %{name}.keyring
%if %{with fipscheck}
Source7:        fips-enforce.conf
%endif
Patch2:         %{name}_ipsec_service.patch
Patch5:         0005-ikev1-Don-t-retransmit-Aggressive-Mode-response.patch
Patch6:         harden_strongswan.service.patch
BuildRequires:  bison
BuildRequires:  curl-devel
BuildRequires:  flex
BuildRequires:  gmp-devel
BuildRequires:  gperf
BuildRequires:  libcap-devel
BuildRequires:  libopenssl-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libsoup-2.4)
%if %{with mysql}
BuildRequires:  libmysqlclient-devel
%endif
%if %{with sqlite}
BuildRequires:  sqlite3-devel
%endif
%if %{with gcrypt}
BuildRequires:  libgcrypt-devel
%endif
%if %{with nm}
BuildRequires:  pkgconfig(libnm)
%endif
%{?systemd_requires}
BuildRequires:  iptables
BuildRequires:  pkgconfig(libsystemd)
%{!?_rundir: %global _rundir /run}
%{!?_tmpfilesdir: %global _tmpfilesdir /usr/lib/tmpfiles.d}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Requires:       strongswan-ipsec = %{version}

%description
StrongSwan is an IPsec-based VPN solution for Linux.

* Implements both the IKEv1 and IKEv2 (RFC 4306) key exchange protocols
* Fully tested support of IPv6 IPsec tunnel and transport connections
* Dynamic IP address and interface update with IKEv2 MOBIKE (RFC 4555)
* Automatic insertion and deletion of IPsec-policy-based firewall rules
* Strong 128/192/256 bit AES or Camellia encryption, 3DES support
* NAT Traversal via UDP encapsulation and port floating (RFC 3947)
* Dead Peer Detection (DPD, RFC 3706) takes care of dangling tunnels
* Static virtual IP addresses and IKEv1 ModeConfig pull and push modes
* XAUTH server and client functionality on top of IKEv1 Main Mode authentication
* Virtual IP address pool managed by IKE daemon or SQL database
* Secure IKEv2 EAP user authentication (EAP-SIM, EAP-AKA, EAP-MSCHAPv2, etc.)
* Optional relaying of EAP messages to AAA server via EAP-RADIUS plugin
* Support of IKEv2 Multiple Authentication Exchanges (RFC 4739)
* Authentication based on X.509 certificates or preshared keys
* Generation of a default self-signed certificate during first strongSwan startup
* Retrieval and local caching of Certificate Revocation Lists via HTTP or LDAP
* Full support of the Online Certificate Status Protocol (OCSP, RCF 2560).
* CA management (OCSP and CRL URIs, default LDAP server)
* Powerful IPsec policies based on wildcards or intermediate CAs
* Group policies based on X.509 attribute certificates (RFC 3281)
* Storage of RSA private keys and certificates on a smartcard (PKCS #11 interface)
* Modular plugins for crypto algorithms and relational database interfaces
* Support of elliptic curve DH groups and ECDSA certificates (Suite B, RFC 4869)
* Optional built-in integrity and crypto tests for plugins and libraries
* Linux desktop integration via the strongSwan NetworkManager applet

This package triggers the installation of both, IKEv1 and IKEv2 daemons.

%package doc
Summary:        Documentation for strongSwan
Group:          Documentation/Man
BuildArch:      noarch

%description doc
StrongSwan is an IPsec-based VPN solution for Linux.

This package provides the StrongSwan documentation.

%package libs0
Summary:        strongSwan core libraries and basic plugins
Group:          Productivity/Networking/Security
Conflicts:      strongswan < %{version}

%description libs0
StrongSwan is an IPsec-based VPN solution for Linux.

This package provides the strongswan library and plugins.

%package hmac
Summary:        Config file to disable non FIPS-140-2 algos in strongSwan
Group:          Productivity/Networking/Security
Requires:       strongswan-ipsec = %{version}
Requires:       strongswan-libs0 = %{version}

%description hmac
The package provides a config file disabling alternative algorithm
implementation when FIPS-140-2 compliant operation mode is enabled.

%package ipsec
Summary:        IPsec-based VPN solution
Group:          Productivity/Networking/Security
Requires:       strongswan-libs0 = %{version}
Provides:       VPN
Provides:       ipsec
Provides:       strongswan = %{version}
Obsoletes:      strongswan < %{version}
Conflicts:      freeswan
Conflicts:      openswan

%description ipsec
StrongSwan is an IPsec-based VPN solution for Linux.

This package provides the systemd service definition and allows
to maintain both IKEv1 and IKEv2 using the /etc/ipsec.conf and the
/etc/ipsec.secrets files.

%package mysql
Summary:        MySQL plugin for strongSwan
Group:          Productivity/Networking/Security
Requires:       strongswan-libs0 = %{version}

%description mysql
StrongSwan is an IPsec-based VPN solution for Linux.

This package provides the strongswan mysql plugin.

%package sqlite
Summary:        SQLite plugin for strongSwan
Group:          Productivity/Networking/Security
Requires:       strongswan-libs0 = %{version}

%description sqlite
StrongSwan is an OpenSource IPsec-based VPN solution for Linux.

This package provides the strongswan sqlite plugin.

%package nm
Summary:        NetworkManager plugin for strongSwan
Group:          Productivity/Networking/Security
Requires:       strongswan-libs0 = %{version}

%description nm
StrongSwan is an OpenSource IPsec-based VPN solution for Linux.

This package provides the NetworkManager plugin to control the
charon IKEv2 daemon through D-Bus, designed to work using the
NetworkManager-strongswan graphical user interface.

%package tests
Summary:        Testing plugins for strongSwan
Group:          Productivity/Networking/Security
Requires:       strongswan-libs0 = %{version}

%description tests
StrongSwan is an OpenSource IPsec-based VPN solution for Linux.

This package provides the strongswan crypto test vectors plugin
and the load testing plugin for IKEv2 daemon.

%prep
%setup -q -n %{name}-%{upstream_version}
%patch -P 2 -p1
%patch -P 5 -p1
sed -e 's|@libexecdir@|%_libexecdir|g'    \
     < %{_sourcedir}/strongswan.init.in \
     > strongswan.init
%patch -P 6 -p1

%build
CFLAGS="%{optflags} -W -Wall -Wno-pointer-sign -Wno-strict-aliasing -Wno-unused-parameter"
export CFLAGS
autoreconf --force --install
%configure \
%if %{with integrity}
	--enable-integrity-test \
%endif
	--with-capabilities=libcap \
	--with-plugindir=%{strongswan_plugins} \
	--with-resolv-conf=%{_rundir}/%{name}/resolv.conf \
	--with-piddir=%{_rundir}/%{name} \
	--enable-systemd \
	--with-systemdsystemunitdir=%{_unitdir} \
	--enable-pkcs11 \
	--enable-openssl \
	--enable-agent \
%if %{with gcrypt}
	--enable-gcrypt \
%else
	--disable-gcrypt \
%endif
	--enable-blowfish \
	--enable-ctr \
	--enable-ccm \
	--enable-gcm \
	--enable-unity \
	--enable-md4 \
%if %{with afalg}
	--enable-af-alg \
%endif
	--enable-eap-sim \
	--enable-eap-sim-file \
	--enable-eap-sim-pcsc \
	--enable-eap-aka \
	--enable-eap-aka-3gpp2 \
	--enable-eap-simaka-sql \
	--enable-eap-simaka-pseudonym \
	--enable-eap-simaka-reauth \
	--enable-eap-identity \
	--enable-eap-md5 \
	--enable-eap-gtc \
	--enable-eap-mschapv2 \
	--enable-eap-tls \
	--enable-eap-ttls \
	--enable-eap-peap \
	--enable-eap-tnc \
	--enable-eap-dynamic \
	--enable-eap-radius \
	--enable-xauth-eap \
	--enable-xauth-pam \
	--enable-tnc-pdp \
	--enable-tnc-imc \
	--enable-tnc-imv \
	--enable-tnccs-11 \
	--enable-tnccs-20 \
	--enable-tnccs-dynamic \
	--enable-imc-test \
	--enable-imv-test \
	--enable-imc-scanner \
	--enable-imv-scanner \
	--enable-ha \
	--enable-dhcp \
%if %{with farp}
	--enable-farp \
%endif
	--enable-smp \
	--enable-sql \
	--enable-attr-sql \
	--enable-addrblock \
	--enable-radattr \
	--enable-mediation \
	--enable-led \
	--enable-certexpire \
	--enable-duplicheck \
	--enable-coupling \
%if %{with mysql}
	--enable-mysql \
%endif
%if %{with sqlite}
	--enable-sqlite \
%endif
%if %{with nm}
	--enable-nm \
%else
	--disable-nm \
%endif
%if %{with tests}
	--enable-conftest \
	--enable-load-tester \
	--enable-test-vectors \
%endif
	--enable-ldap \
	--enable-soup \
	--enable-curl \
	--enable-bypass-lan \
	--disable-static
%make_build

%install
install -d -m755              %{buildroot}/%{_sbindir}/
install -d -m755              %{buildroot}/%{_sysconfdir}/ipsec.d/
#
# Ensure, plugin -> library dependencies can be resolved
# (e.g. libtls) to avoid plugin segment checksum errors.
#
LD_LIBRARY_PATH="%{buildroot}-$$/%{strongswan_libdir}" \
%make_install
#
# checksums are calculated during make install using the
# installed binaries/libraries... but find-debuginfo.sh
# extracts debuginfo/debugsource breaking file checksums.
# let find-debuginfo.sh run on a build root copy and then
# calculate the checksums.
#
%if %{with integrity}
%{?__debug_package:
	if test -x %{_rpmconfigdir}/find-debuginfo.sh ; then
		cp -a "%{buildroot}" "%{buildroot}-$$"
		RPM_BUILD_ROOT="%{buildroot}-$$" \
		%{_rpmconfigdir}/find-debuginfo.sh  \
			%{?_find_debuginfo_opts} "%{buildroot}-$$"
		make -C src/checksum clean
		rm -f   src/checksum/checksum_builder
		LD_LIBRARY_PATH="%{buildroot}-$$/%{strongswan_libdir}" \
		make -C src/checksum install DESTDIR="%{buildroot}-$$"
		mv "%{buildroot}-$$/%{strongswan_libdir}/libchecksum.so" \
		   "%{buildroot}/%{strongswan_libdir}/libchecksum.so"
		rm -rf "%{buildroot}-$$"
	fi
}
%endif
#
rm -f %{buildroot}/%{_sysconfdir}/ipsec.secrets
cat << EOT > %{buildroot}/%{_sysconfdir}/ipsec.secrets
#
# ipsec.secrets
#
# This file holds the RSA private keys or the PSK preshared secrets for
# the IKE/IPsec authentication. See the ipsec.secrets(5) manual page.
#
EOT
#
%if ! %{with mysql}
rm -f %{buildroot}/%{strongswan_templates}/database/sql/mysql.sql
%endif
%if ! %{with sqlite}
rm -f %{buildroot}/%{strongswan_templates}/database/sql/sqlite.sql
%endif
rm -f %{buildroot}/%{strongswan_libdir}/lib{charon,hydra,strongswan,pttls}.so
rm -f %{buildroot}/%{strongswan_libdir}/lib{radius,simaka,tls,tnccs,imcv}.so
find %{buildroot}/%{strongswan_libdir} -type f -name "*.la" -delete
#
install -d -m755 %{buildroot}/%{strongswan_docdir}/
install -c -m644 TODO NEWS README COPYING LICENSE \
		 AUTHORS ChangeLog \
		 %{buildroot}/%{strongswan_docdir}/
install -c -m644 %{_sourcedir}/README.SUSE \
		 %{buildroot}/%{strongswan_docdir}/
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
echo 'd %{_rundir}/%{name} 0770 root root' > %{buildroot}%{_tmpfilesdir}/%{name}.conf
%if %{with fipscheck}
install -c -m644 %{_sourcedir}/fips-enforce.conf \
                 %{buildroot}/%{strongswan_configs}/charon/zzz_fips-enforce.conf
# disable bypass-lan plugin by default
sed -i 's/\(load[ ]*=[ ]*\)yes/\1no/g' %{buildroot}/%{strongswan_configs}/charon/bypass-lan.conf
%endif

%post libs0
/sbin/ldconfig
%{?tmpfiles_create:%tmpfiles_create %{_tmpfilesdir}/%{name}.conf}
%{!?tmpfiles_create:test -d %{_rundir}/%{name} || mkdir -p %{_rundir}/%{name}}

%postun libs0 -p /sbin/ldconfig

%pre ipsec
%service_add_pre %{name}-starter.service

%post ipsec
# Following code does the migration from strongwan.service (ver < 5.8.0) to
# strongswan-starter.service (ver >= 5.8.0) during update. The systemd service
# units have been renamed. The modern unit, which was called strongswan-swanctl,
# is now called strongswan (the previous name is configured as alias in the unit,
# for which a symlink is created when the unit is enabled). The legacy unit is now
# called strongswan-starter.
_ipsec_active=`/usr/bin/systemctl is-active %{name}-starter.service 2>/dev/null` || :
_swanctl_active=`/usr/bin/systemctl is-active %{name}.service 2>/dev/null` || :
_ipsec_enable=`/usr/bin/systemctl is-enabled %{name}-starter.service 2>/dev/null` || :
_swanctl_enable=`/usr/bin/systemctl is-enabled %{name}.service 2>/dev/null` || :
if [[ "$_swanctl_enable" == "enabled" || "$_swanctl_active" == "active" ]]; then
        /usr/bin/systemctl disable --now %{name}.service || :
        /usr/bin/systemctl mask %{name}.service || :
fi
if [[ "$_swanctl_enable" == "enabled" || "$_ipsec_enable" == "enabled" ]]; then
        /usr/bin/systemctl daemon-reload
        /usr/bin/systemctl enable %{name}-starter.service || :
fi
if [[ "$_swanctl_active" == "active" || "$_ipsec_active" == "active" ]]; then
        /usr/bin/systemctl start %{name}-starter.service || :
fi

%preun ipsec
%service_del_preun %{name}-starter.service
if test -s %{_sysconfdir}/ipsec.secrets.rpmsave ; then
	cp -p --backup=numbered %{_sysconfdir}/ipsec.secrets.rpmsave \
	                        %{_sysconfdir}/ipsec.secrets.rpmsave.old
fi
if test -s %{_sysconfdir}/ipsec.conf.rpmsave ; then
	cp -p --backup=numbered %{_sysconfdir}/ipsec.conf.rpmsave \
	                        %{_sysconfdir}/ipsec.conf.rpmsave.old
fi

%postun ipsec
%service_del_postun %{name}-starter.service

%files
%dir %{strongswan_docdir}
%{strongswan_docdir}/README.SUSE

%if %{with fipscheck}

%files hmac
%dir %{strongswan_configs}
%dir %{strongswan_configs}/charon
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/zzz_fips-enforce.conf
%endif

%files ipsec
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/ipsec.conf
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/ipsec.secrets
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/swanctl/swanctl.conf
%dir %{_sysconfdir}/swanctl
%dir %{_sysconfdir}/ipsec.d
%dir %{_sysconfdir}/ipsec.d/crls
%dir %{_sysconfdir}/ipsec.d/reqs
%dir %{_sysconfdir}/ipsec.d/certs
%dir %{_sysconfdir}/ipsec.d/acerts
%dir %{_sysconfdir}/ipsec.d/aacerts
%dir %{_sysconfdir}/ipsec.d/cacerts
%dir %{_sysconfdir}/ipsec.d/ocspcerts
%dir %attr(700,root,root) %{_sysconfdir}/ipsec.d/private
%{_unitdir}/strongswan-starter.service
%{_unitdir}/strongswan.service
%{_sbindir}/charon-systemd
%{_bindir}/pki
%{_bindir}/pt-tls-client
%{_bindir}/tpm_extendpcr
%{_sbindir}/ipsec
%{_sbindir}/swanctl
%{_mandir}/man1/pki*.1*
%{_mandir}/man1/pt-tls-client.1*
%{_mandir}/man8/ipsec.8*
%{_mandir}/man5/ipsec.conf.5*
%{_mandir}/man5/ipsec.secrets.5*
%{_mandir}/man5/strongswan.conf.5*
%dir %{_libexecdir}/ipsec
%{_libexecdir}/ipsec/_updown
%if %{with test}
%{_libexecdir}/ipsec/conftest
%endif
%{_libexecdir}/ipsec/xfrmi
%{_libexecdir}/ipsec/duplicheck
%{_libexecdir}/ipsec/pool
%{_libexecdir}/ipsec/starter
%{_libexecdir}/ipsec/stroke
%{_libexecdir}/ipsec/charon
%{_libexecdir}/ipsec/_imv_policy
%{_libexecdir}/ipsec/imv_policy_manager
%dir %{strongswan_plugins}
%{strongswan_plugins}/libstrongswan-drbg.so
%{strongswan_plugins}/libstrongswan-stroke.so
%{strongswan_plugins}/libstrongswan-updown.so

%files doc
%dir %{strongswan_docdir}
%{strongswan_docdir}/TODO
%{strongswan_docdir}/NEWS
%{strongswan_docdir}/README
%{strongswan_docdir}/COPYING
%{strongswan_docdir}/LICENSE
%{strongswan_docdir}/AUTHORS
%{strongswan_docdir}/ChangeLog
%{_mandir}/man5/swanctl.conf.5.*
%{_mandir}/man8/swanctl.8.*

%files libs0
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/strongswan.conf
%dir %{strongswan_configs}
%dir %{strongswan_configs}/charon
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon-systemd.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon-logging.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/imcv.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/pki.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/pool.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/starter.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/tnc.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/swanctl.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/addrblock.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/aes.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/counters.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/curve25519.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/drbg.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/vici.conf
%if %{with afalg}
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/af-alg.conf
%endif
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/agent.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/attr.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/attr-sql.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/blowfish.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/ccm.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/certexpire.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/cmac.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/constraints.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/coupling.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/ctr.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/curl.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/des.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/dhcp.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/dnskey.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/duplicheck.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-aka-3gpp2.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-aka.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-dynamic.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-gtc.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-identity.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-md5.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-mschapv2.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-peap.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-radius.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-simaka-pseudonym.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-simaka-reauth.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-simaka-sql.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-sim.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-sim-file.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-sim-pcsc.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-tls.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-tnc.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/eap-ttls.conf
%if %{with farp}
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/farp.conf
%endif
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/fips-prf.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/gcm.conf
%if %{with gcrypt}
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/gcrypt.conf
%endif
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/gmp.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/ha.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/hmac.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/kdf.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/kernel-netlink.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/ldap.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/led.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/md4.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/md5.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/mgf1.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/nonce.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/openssl.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/pem.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/pgp.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/pkcs11.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/pkcs12.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/pkcs1.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/pkcs7.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/pkcs8.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/pubkey.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/radattr.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/random.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/rc2.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/resolve.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/revocation.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/sha1.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/sha2.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/smp.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/socket-default.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/soup.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/sql.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/sshkey.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/stroke.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/tnccs-11.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/tnccs-20.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/tnccs-dynamic.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/tnc-imc.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/tnc-imv.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/tnc-pdp.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/tnc-tnccs.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/unity.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/updown.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/x509.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/xauth-eap.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/xauth-generic.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/xauth-pam.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/xcbc.conf
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/bypass-lan.conf
%dir %{strongswan_libdir}
%if %{with integrity}
%{strongswan_libdir}/libchecksum.so
%endif
%{strongswan_libdir}/libcharon.so.*
%{strongswan_libdir}/libtpmtss.so.*
%{strongswan_libdir}/libtpmtss.so
%{strongswan_libdir}/libvici.so
%{strongswan_libdir}/libvici.so.*
%{strongswan_libdir}/libpttls.so.*
%{strongswan_libdir}/libradius.so.*
%{strongswan_libdir}/libsimaka.so.*
%{strongswan_libdir}/libstrongswan.so.*
%{strongswan_libdir}/libtls.so.*
%{strongswan_libdir}/libtnccs.so.*
%{strongswan_libdir}/libimcv.so.*
%dir %{strongswan_libdir}/imcvs
%{strongswan_libdir}/imcvs/imc-scanner.so
%{strongswan_libdir}/imcvs/imc-test.so
%{strongswan_libdir}/imcvs/imv-scanner.so
%{strongswan_libdir}/imcvs/imv-test.so
%dir %{strongswan_plugins}
%{strongswan_plugins}/libstrongswan-addrblock.so
%{strongswan_plugins}/libstrongswan-aes.so
%if %{with afalg}
%{strongswan_plugins}/libstrongswan-af-alg.so
%endif
%{strongswan_plugins}/libstrongswan-agent.so
%{strongswan_plugins}/libstrongswan-attr.so
%{strongswan_plugins}/libstrongswan-attr-sql.so
%{strongswan_plugins}/libstrongswan-blowfish.so
%{strongswan_plugins}/libstrongswan-ccm.so
%{strongswan_plugins}/libstrongswan-certexpire.so
%{strongswan_plugins}/libstrongswan-cmac.so
%{strongswan_plugins}/libstrongswan-counters.so
%{strongswan_plugins}/libstrongswan-constraints.so
%{strongswan_plugins}/libstrongswan-coupling.so
%{strongswan_plugins}/libstrongswan-ctr.so
%{strongswan_plugins}/libstrongswan-curl.so
%{strongswan_plugins}/libstrongswan-des.so
%{strongswan_plugins}/libstrongswan-dhcp.so
%{strongswan_plugins}/libstrongswan-dnskey.so
%{strongswan_plugins}/libstrongswan-duplicheck.so
%{strongswan_plugins}/libstrongswan-eap-aka-3gpp2.so
%{strongswan_plugins}/libstrongswan-eap-aka.so
%{strongswan_plugins}/libstrongswan-eap-dynamic.so
%{strongswan_plugins}/libstrongswan-eap-gtc.so
%{strongswan_plugins}/libstrongswan-eap-identity.so
%{strongswan_plugins}/libstrongswan-eap-md5.so
%{strongswan_plugins}/libstrongswan-eap-mschapv2.so
%{strongswan_plugins}/libstrongswan-eap-peap.so
%{strongswan_plugins}/libstrongswan-eap-radius.so
%{strongswan_plugins}/libstrongswan-eap-sim-file.so
%{strongswan_plugins}/libstrongswan-eap-sim-pcsc.so
%{strongswan_plugins}/libstrongswan-eap-sim.so
%{strongswan_plugins}/libstrongswan-eap-simaka-pseudonym.so
%{strongswan_plugins}/libstrongswan-eap-simaka-reauth.so
%{strongswan_plugins}/libstrongswan-eap-simaka-sql.so
%{strongswan_plugins}/libstrongswan-eap-tls.so
%{strongswan_plugins}/libstrongswan-eap-tnc.so
%{strongswan_plugins}/libstrongswan-eap-ttls.so
%if %{with farp}
%{strongswan_plugins}/libstrongswan-farp.so
%endif
%{strongswan_plugins}/libstrongswan-fips-prf.so
%{strongswan_plugins}/libstrongswan-gcm.so
%if %{with gcrypt}
%{strongswan_plugins}/libstrongswan-gcrypt.so
%endif
%{strongswan_plugins}/libstrongswan-gmp.so
%{strongswan_plugins}/libstrongswan-ha.so
%{strongswan_plugins}/libstrongswan-hmac.so
%{strongswan_plugins}/libstrongswan-kdf.so
%{strongswan_plugins}/libstrongswan-kernel-netlink.so
%{strongswan_plugins}/libstrongswan-ldap.so
%{strongswan_plugins}/libstrongswan-led.so
%{strongswan_plugins}/libstrongswan-md4.so
%{strongswan_plugins}/libstrongswan-md5.so
%{strongswan_plugins}/libstrongswan-mgf1.so
%{strongswan_plugins}/libstrongswan-nonce.so
%{strongswan_plugins}/libstrongswan-openssl.so
%{strongswan_plugins}/libstrongswan-pem.so
%{strongswan_plugins}/libstrongswan-pgp.so
%{strongswan_plugins}/libstrongswan-pkcs1.so
%{strongswan_plugins}/libstrongswan-pkcs11.so
%{strongswan_plugins}/libstrongswan-pkcs12.so
%{strongswan_plugins}/libstrongswan-pkcs7.so
%{strongswan_plugins}/libstrongswan-pkcs8.so
%{strongswan_plugins}/libstrongswan-pubkey.so
%{strongswan_plugins}/libstrongswan-radattr.so
%{strongswan_plugins}/libstrongswan-random.so
%{strongswan_plugins}/libstrongswan-rc2.so
%{strongswan_plugins}/libstrongswan-resolve.so
%{strongswan_plugins}/libstrongswan-revocation.so
%{strongswan_plugins}/libstrongswan-sha1.so
%{strongswan_plugins}/libstrongswan-sha2.so
%{strongswan_plugins}/libstrongswan-smp.so
%{strongswan_plugins}/libstrongswan-socket-default.so
%{strongswan_plugins}/libstrongswan-soup.so
%{strongswan_plugins}/libstrongswan-sql.so
%{strongswan_plugins}/libstrongswan-sshkey.so
%{strongswan_plugins}/libstrongswan-tnc-imc.so
%{strongswan_plugins}/libstrongswan-tnc-imv.so
%{strongswan_plugins}/libstrongswan-tnc-pdp.so
%{strongswan_plugins}/libstrongswan-tnc-tnccs.so
%{strongswan_plugins}/libstrongswan-tnccs-11.so
%{strongswan_plugins}/libstrongswan-tnccs-20.so
%{strongswan_plugins}/libstrongswan-tnccs-dynamic.so
%{strongswan_plugins}/libstrongswan-unity.so
%{strongswan_plugins}/libstrongswan-x509.so
%{strongswan_plugins}/libstrongswan-xauth-eap.so
%{strongswan_plugins}/libstrongswan-xauth-generic.so
%{strongswan_plugins}/libstrongswan-xauth-pam.so
%{strongswan_plugins}/libstrongswan-xcbc.so
%{strongswan_plugins}/libstrongswan-curve25519.so
%{strongswan_plugins}/libstrongswan-vici.so
%{strongswan_plugins}/libstrongswan-bypass-lan.so
%dir %{strongswan_datadir}
%dir %{strongswan_templates}
%dir %{strongswan_templates}/config
%dir %{strongswan_templates}/config/plugins
%dir %{strongswan_templates}/config/strongswan.d
%dir %{strongswan_templates}/database
%dir %{strongswan_templates}/database/imv
%dir %{strongswan_templates}/database/sql
%{strongswan_templates}/config/strongswan.conf
%{strongswan_templates}/config/plugins/addrblock.conf
%{strongswan_templates}/config/plugins/aes.conf
%if %{with afalg}
%{strongswan_templates}/config/plugins/af-alg.conf
%endif
%{strongswan_templates}/config/plugins/agent.conf
%{strongswan_templates}/config/plugins/attr-sql.conf
%{strongswan_templates}/config/plugins/attr.conf
%{strongswan_templates}/config/plugins/blowfish.conf
%{strongswan_templates}/config/plugins/ccm.conf
%{strongswan_templates}/config/plugins/certexpire.conf
%{strongswan_templates}/config/plugins/cmac.conf
%{strongswan_templates}/config/plugins/counters.conf
%{strongswan_templates}/config/plugins/constraints.conf
%{strongswan_templates}/config/plugins/coupling.conf
%{strongswan_templates}/config/plugins/ctr.conf
%{strongswan_templates}/config/plugins/curl.conf
%{strongswan_templates}/config/plugins/des.conf
%{strongswan_templates}/config/plugins/dhcp.conf
%{strongswan_templates}/config/plugins/dnskey.conf
%{strongswan_templates}/config/plugins/drbg.conf
%{strongswan_templates}/config/plugins/duplicheck.conf
%{strongswan_templates}/config/plugins/eap-aka-3gpp2.conf
%{strongswan_templates}/config/plugins/eap-aka.conf
%{strongswan_templates}/config/plugins/eap-dynamic.conf
%{strongswan_templates}/config/plugins/eap-gtc.conf
%{strongswan_templates}/config/plugins/eap-identity.conf
%{strongswan_templates}/config/plugins/eap-md5.conf
%{strongswan_templates}/config/plugins/eap-mschapv2.conf
%{strongswan_templates}/config/plugins/eap-peap.conf
%{strongswan_templates}/config/plugins/eap-radius.conf
%{strongswan_templates}/config/plugins/eap-sim-file.conf
%{strongswan_templates}/config/plugins/eap-sim-pcsc.conf
%{strongswan_templates}/config/plugins/eap-sim.conf
%{strongswan_templates}/config/plugins/eap-simaka-pseudonym.conf
%{strongswan_templates}/config/plugins/eap-simaka-reauth.conf
%{strongswan_templates}/config/plugins/eap-simaka-sql.conf
%{strongswan_templates}/config/plugins/eap-tls.conf
%{strongswan_templates}/config/plugins/eap-tnc.conf
%{strongswan_templates}/config/plugins/eap-ttls.conf
%if %{with farp}
%{strongswan_templates}/config/plugins/farp.conf
%endif
%{strongswan_templates}/config/plugins/fips-prf.conf
%{strongswan_templates}/config/plugins/gcm.conf
%if %{with gcrypt}
%{strongswan_templates}/config/plugins/gcrypt.conf
%endif
%{strongswan_templates}/config/plugins/gmp.conf
%{strongswan_templates}/config/plugins/ha.conf
%{strongswan_templates}/config/plugins/hmac.conf
%{strongswan_templates}/config/plugins/kdf.conf
%{strongswan_templates}/config/plugins/kernel-netlink.conf
%{strongswan_templates}/config/plugins/ldap.conf
%{strongswan_templates}/config/plugins/led.conf
%{strongswan_templates}/config/plugins/md4.conf
%{strongswan_templates}/config/plugins/md5.conf
%{strongswan_templates}/config/plugins/mgf1.conf
%{strongswan_templates}/config/plugins/nonce.conf
%{strongswan_templates}/config/plugins/openssl.conf
%{strongswan_templates}/config/plugins/pem.conf
%{strongswan_templates}/config/plugins/pgp.conf
%{strongswan_templates}/config/plugins/pkcs1.conf
%{strongswan_templates}/config/plugins/pkcs11.conf
%{strongswan_templates}/config/plugins/pkcs12.conf
%{strongswan_templates}/config/plugins/pkcs7.conf
%{strongswan_templates}/config/plugins/pkcs8.conf
%{strongswan_templates}/config/plugins/pubkey.conf
%{strongswan_templates}/config/plugins/radattr.conf
%{strongswan_templates}/config/plugins/random.conf
%{strongswan_templates}/config/plugins/rc2.conf
%{strongswan_templates}/config/plugins/resolve.conf
%{strongswan_templates}/config/plugins/revocation.conf
%{strongswan_templates}/config/plugins/sha1.conf
%{strongswan_templates}/config/plugins/sha2.conf
%{strongswan_templates}/config/plugins/smp.conf
%{strongswan_templates}/config/plugins/socket-default.conf
%{strongswan_templates}/config/plugins/soup.conf
%{strongswan_templates}/config/plugins/sql.conf
%{strongswan_templates}/config/plugins/sshkey.conf
%{strongswan_templates}/config/plugins/stroke.conf
%{strongswan_templates}/config/plugins/tnc-imc.conf
%{strongswan_templates}/config/plugins/tnc-imv.conf
%{strongswan_templates}/config/plugins/tnc-pdp.conf
%{strongswan_templates}/config/plugins/tnc-tnccs.conf
%{strongswan_templates}/config/plugins/tnccs-11.conf
%{strongswan_templates}/config/plugins/tnccs-20.conf
%{strongswan_templates}/config/plugins/tnccs-dynamic.conf
%{strongswan_templates}/config/plugins/unity.conf
%{strongswan_templates}/config/plugins/updown.conf
%{strongswan_templates}/config/plugins/x509.conf
%{strongswan_templates}/config/plugins/xauth-eap.conf
%{strongswan_templates}/config/plugins/xauth-generic.conf
%{strongswan_templates}/config/plugins/xauth-pam.conf
%{strongswan_templates}/config/plugins/xcbc.conf
%{strongswan_templates}/config/plugins/curve25519.conf
%{strongswan_templates}/config/plugins/vici.conf
%{strongswan_templates}/config/plugins/bypass-lan.conf
%{strongswan_templates}/config/strongswan.d/charon-systemd.conf
%{strongswan_templates}/config/strongswan.d/charon-logging.conf
%{strongswan_templates}/config/strongswan.d/charon.conf
%{strongswan_templates}/config/strongswan.d/imcv.conf
%{strongswan_templates}/config/strongswan.d/pki.conf
%{strongswan_templates}/config/strongswan.d/pool.conf
%{strongswan_templates}/config/strongswan.d/starter.conf
%{strongswan_templates}/config/strongswan.d/tnc.conf
%{strongswan_templates}/config/strongswan.d/swanctl.conf
%{strongswan_templates}/database/imv/data.sql
%{strongswan_templates}/database/imv/tables.sql

%if %{with nm}

%files nm
%dir %{_libexecdir}/ipsec
%dir %{strongswan_plugins}
%{_libexecdir}/ipsec/charon-nm
%{_datadir}/dbus-1/system.d/nm-strongswan-service.conf
%endif

%if %{with mysql}

%files mysql
%dir %{strongswan_libdir}
%dir %{strongswan_plugins}
%{strongswan_plugins}/libstrongswan-mysql.so
%dir %{strongswan_configs}
%dir %{strongswan_configs}/charon
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/mysql.conf
%dir %{strongswan_datadir}
%dir %{strongswan_templates}
%dir %{strongswan_templates}/config
%dir %{strongswan_templates}/config/plugins
%dir %{strongswan_templates}/database
%dir %{strongswan_templates}/database/sql
%{strongswan_templates}/config/plugins/mysql.conf
%{strongswan_templates}/database/imv/tables-mysql.sql
%{strongswan_templates}/database/sql/mysql.sql
%endif

%if %{with sqlite}

%files sqlite
%dir %{strongswan_libdir}
%dir %{strongswan_plugins}
%{strongswan_plugins}/libstrongswan-sqlite.so
%dir %{strongswan_configs}
%dir %{strongswan_configs}/charon
%config(noreplace) %attr(600,root,root) %{strongswan_configs}/charon/sqlite.conf
%dir %{strongswan_datadir}
%dir %{strongswan_templates}
%dir %{strongswan_templates}/config
%dir %{strongswan_templates}/config/plugins
%dir %{strongswan_templates}/database
%dir %{strongswan_templates}/database/sql
%{strongswan_templates}/config/plugins/sqlite.conf
%{strongswan_templates}/database/sql/sqlite.sql
%endif

%if %{with tests}

%files tests
%dir %{strongswan_configs}
%dir %{strongswan_configs}/charon
%{strongswan_configs}/charon/load-tester.conf
%{strongswan_configs}/charon/test-vectors.conf
%dir %{strongswan_templates}
%dir %{strongswan_templates}/config
%dir %{strongswan_templates}/config/plugins
%{strongswan_templates}/config/plugins/load-tester.conf
%{strongswan_templates}/config/plugins/test-vectors.conf
%dir %{_libexecdir}/ipsec
%{_libexecdir}/ipsec/conftest
%{_libexecdir}/ipsec/load-tester
%dir %{strongswan_libdir}
%dir %{strongswan_plugins}
%{strongswan_plugins}/libstrongswan-load-tester.so
%{strongswan_plugins}/libstrongswan-test-vectors.so
%endif

%changelog
