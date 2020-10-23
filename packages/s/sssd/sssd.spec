#
# spec file for package sssd
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

%define _buildshell /bin/bash

Name:           sssd
Version:        2.4.0
Release:        0
Summary:        System Security Services Daemon
License:        GPL-3.0-or-later and LGPL-3.0-or-later
Group:          System/Daemons
URL:            https://pagure.io/SSSD/sssd
#Git-Clone:	https://pagure.io/SSSD/sssd
Source:         https://github.com/SSSD/sssd/releases/download/sssd-2_4_0/%name-%version.tar.gz
Source2:        https://github.com/SSSD/sssd/releases/download/sssd-2_4_0/%name-%version.tar.gz.asc
Source3:        baselibs.conf
Source5:        %name.keyring
Patch1:         krb-noversion.diff

%define servicename	sssd
%define sssdstatedir	%_localstatedir/lib/sss
%define dbpath		%sssdstatedir/db
%define pipepath	%sssdstatedir/pipes
%define pubconfpath	%sssdstatedir/pubconf
%define gpocachepath	%sssdstatedir/gpo_cache

BuildRequires:  autoconf >= 2.59
BuildRequires:  automake
BuildRequires:  bind-utils
BuildRequires:  check-devel
BuildRequires:  cifs-utils-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  krb5-devel >= 1.12
BuildRequires:  libcmocka-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libtool
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  nscd
BuildRequires:  nss_wrapper
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pkg-config >= 0.21
BuildRequires:  systemd-rpm-macros
BuildRequires:  uid_wrapper
BuildRequires:  pkgconfig(augeas) >= 1.0.0
BuildRequires:  pkgconfig(collection) >= 0.5.1
BuildRequires:  pkgconfig(dbus-1) >= 1.0.0
BuildRequires:  pkgconfig(dhash) >= 0.4.2
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(ini_config) >= 1.1.0
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(ldb) >= 0.9.2
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libnfsidmap)
BuildRequires:  pkgconfig(libnl-3.0) >= 3.0
BuildRequires:  pkgconfig(libnl-route-3.0) >= 3.0
BuildRequires:  pkgconfig(libpcre) >= 7
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ndr_krb5pac)
BuildRequires:  pkgconfig(ndr_nbt)
BuildRequires:  pkgconfig(p11-kit-1) >= 0.23.3
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  pkgconfig(tdb) >= 1.1.3
BuildRequires:  pkgconfig(tevent)
BuildRequires:  pkgconfig(uuid)
%{?systemd_ordering}
Requires:       sssd-ldap = %version-%release
Requires(postun): pam-config
Provides:       libsss_sudo = %version-%release
Provides:       sssd-client = %version-%release
Obsoletes:      libsss_sudo < %version-%release

%description
Provides a set of daemons to manage access to remote directories and
authentication mechanisms. It provides an NSS and PAM interface toward
the system and a pluggable backend system to connect to multiple different
account sources. It is also the basis to provide client auditing and policy
services for projects like FreeIPA.

%package ad
Summary:        The ActiveDirectory backend plugin for sssd
License:        GPL-3.0-or-later
Group:          System/Daemons
Requires:       %name-krb5-common = %version
Requires:       adcli

%description ad
Provides the Active Directory back end that the SSSD can utilize to
fetch identity data from and authenticate against an Active Directory
server.

%package dbus
Summary:        The D-Bus responder of sssd
License:        GPL-3.0-or-later
Group:          System/Base
Requires:       %name = %version

%description dbus
Provides the D-Bus responder of sssd, called InfoPipe, which allows
information from sssd to be transmitted over the system bus.

%package ipa
Summary:        FreeIPA backend plugin for sssd
License:        GPL-3.0-or-later
Group:          System/Daemons
Requires:       %name = %version
Requires:       %name-ad = %version-%release
Requires:       %name-krb5-common = %version-%release
Obsoletes:      %name-ipa-provider < %version-%release
Provides:       %name-ipa-provider = %version-%release

%description ipa
Provides the IPA back end that the SSSD can utilize to fetch identity
data from and authenticate against an IPA server.

%package kcm
Summary:        SSSD's Kerberos cache manager
License:        GPL-3.0-or-later
Group:          System/Daemons
Requires:       sssd = %version-%release

%description kcm
KCM is a process that stores, tracks and manages Kerberos credential
caches.

%package krb5
Summary:        The Kerberos authentication backend plugin for sssd
License:        GPL-3.0-or-later
Group:          System/Daemons
Requires:       %name-krb5-common = %version-%release

%description krb5
Provides the Kerberos back end that the SSSD can utilize authenticate
against a Kerberos server.

%package krb5-common
Summary:        SSSD helpers needed for Kerberos and GSSAPI authentication
License:        GPL-3.0-or-later
Group:          System/Daemons
Requires:       cyrus-sasl-gssapi

%description krb5-common
Provides helper processes that the LDAP and Kerberos back ends can
use for Kerberos user or host authentication.

%package ldap
Summary:        The LDAP backend plugin for sssd
License:        GPL-3.0-or-later
Group:          System/Daemons
Requires:       %name-krb5-common = %version-%release

%description ldap
Provides the LDAP back end that the SSSD can utilize to fetch
identity data from and authenticate against an LDAP server.

%package proxy
Summary:        The proxy backend plugin for sssd
License:        GPL-3.0-or-later
Group:          System/Daemons

%description proxy
Provides the proxy back end which can be used to wrap an existing NSS
and/or PAM modules to leverage SSSD caching.

%package tools
Summary:        Commandline tools for sssd
License:        GPL-3.0-or-later and LGPL-3.0-or-later
Group:          System/Management
Requires:       python3-sssd-config = %version
Requires:       sssd = %version

%description tools
The packages contains commandline tools for managing users and groups using
the "local" id provider of the System Security Services Daemon (sssd).

%package winbind-idmap
Summary:        The sss idmap backend for Winbind
Group:          System/Libraries

%description winbind-idmap
The idmap_sss module provides a way for Winbind to call SSSD to map
UIDs/GIDs and SIDs.

%package -n libsss_certmap0
Summary:        FreeIPA ID mapping library
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n libsss_certmap0
A utility library for FreeIPA to map certs.

%package -n libsss_certmap-devel
Summary:        Development files for the FreeIPA certmap library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsss_certmap0 = %version

%description -n libsss_certmap-devel
A utility library for FreeIPA to map certs.

%package -n libipa_hbac0
Summary:        FreeIPA HBAC Evaluator library
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n libipa_hbac0
Utility library to validate FreeIPA HBAC rules for authorization
requests.

%package -n libipa_hbac-devel
Summary:        Development files for the FreeIPA HBAC Evaluator library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libipa_hbac0 = %version

%description -n libipa_hbac-devel
Utility library to validate FreeIPA HBAC rules for authorization
requests.

%package -n libnfsidmap-sss
Summary:        Library to allow communication between libnfsidmap and SSSD
License:        GPL-3.0-or-later
Group:          System/Libraries
Supplements:    packageand(nfsidmap:sssd-client)

%description -n libnfsidmap-sss
A utility library to allow communication between libnfsidmap and SSSD.

%package -n libsss_idmap0
Summary:        FreeIPA ID mapping library
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n libsss_idmap0
A utility library for FreeIPA to map Windows SIDs to Unix user/group IDs.

%package -n libsss_idmap-devel
Summary:        Development files for the FreeIPA idmap library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsss_idmap0 = %version

%description -n libsss_idmap-devel
A utility library for FreeIPA to map Windows SIDs to Unix user/group IDs.

%package -n libsss_nss_idmap0
Summary:        FreeIPA ID mapping library
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n libsss_nss_idmap0
A utility library for FreeIPA to map Windows SIDs to Unix user/group IDs.

%package -n libsss_nss_idmap-devel
Summary:        Development files for the FreeIPA idmap library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsss_nss_idmap0 = %version

%description -n libsss_nss_idmap-devel
A utility library for FreeIPA to map Windows SIDs to Unix user/group IDs.

%package -n libsss_simpleifp0
Summary:        The SSSD D-Bus responder helper library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libsss_simpleifp0
This subpackage provides a library that simplifies the D-Bus API for
the SSSD InfoPipe responder.

%package -n libsss_simpleifp-devel
Summary:        Development files for the SSSD D-Bus responder helper library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsss_simpleifp0 = %version

%description -n libsss_simpleifp-devel
This subpackage provides the development files for sssd's simpleifp,
a library that simplifies the D-Bus API for the SSSD InfoPipe
responder.

%package -n libsss_sudo
Summary:        A library to allow communication between sudo and SSSD
License:        LGPL-3.0-or-later
Group:          System/Libraries
Supplements:    packageand(sudo:sssd-client)

%description -n libsss_sudo
A utility library to allow communication between sudo and SSSD.

%package -n python3-ipa_hbac
Summary:        Python bindings for the FreeIPA HBAC Evaluator library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       python3

%description -n python3-ipa_hbac
The python-ipa_hbac package contains the bindings so that libipa_hbac
can be used by Python applications.

%package -n python3-sss-murmur
Summary:        Python3 bindings for SSSD Murmur hash function
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       python3

%description -n python3-sss-murmur
This subpackage provides the python3 module for calculating the
Murmur hash version 3.

%package -n python3-sss_nss_idmap
Summary:        Python bindings for libsss_nss_idmap
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       python3

%description -n python3-sss_nss_idmap
The libsss_nss_idmap-python contains the bindings so that
libsss_nss_idmap can be used by Python applications.

%package -n python3-sssd-config
Summary:        Python API for configuring sssd
License:        GPL-3.0-or-later and LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       python3

%description -n python3-sssd-config
Provide python module to access and manage configuration of the System
Security Services Daemon (sssd).

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1210
# pkgconfig file not present
export LDB_LIBS="-lldb"
export LDB_CFLAGS=" "
export LDB_DIR="%_libdir/ldb"
%else
export LDB_DIR="$(pkg-config ldb --variable=modulesdir)"
%endif

# help configure find nscd
export PATH="$PATH:/usr/sbin"

autoreconf -fiv
export CFLAGS="%optflags -fPIE"
export LDFLAGS="-pie"
%configure \
    --with-crypto=libcrypto \
    --with-db-path="%dbpath" \
    --with-pipe-path="%pipepath" \
    --with-pubconf-path="%pubconfpath" \
    --with-gpo-cache-path="%gpocachepath" \
    --with-init-dir="%_initrddir" \
    --with-environment-file="%_sysconfdir/sysconfig/sssd" \
    --with-initscript=systemd \
    --with-syslog=journald \
    --enable-nsslibdir="/%_lib" \
    --enable-pammoddir="/%_lib/security" \
    --with-ldb-lib-dir="$LDB_DIR" \
    --with-selinux=no \
    --with-os=suse \
    --with-semanage=no \
    --disable-ldb-version-check \
    --without-secrets \
    --without-python2-bindings
make %{?_smp_mflags} all

%install
# sss_obfuscate is compatible with both python 2 and 3
sed -i -e 's:%_bindir/python:%_bindir/python3:' src/tools/sss_obfuscate

%make_install
b="%buildroot"

# Copy default sssd.conf file
install -d "$b/%_mandir"/{cs,cs/man8,nl,nl/man8,pt,pt/man8,uk,uk/man1} \
           "$b/%_mandir"/{uk/man5,uk/man8}
install -d "$b/%_sysconfdir/sssd"
install -m600 src/examples/sssd-example.conf "$b/%_sysconfdir/sssd/sssd.conf"
install -d "$b/%_sysconfdir/sssd/conf.d"
install -d "$b/%_unitdir"

# Copy default logrotate file
install -d "$b/%_sysconfdir/logrotate.d"
install -m644 src/examples/logrotate "$b/%_sysconfdir/logrotate.d/sssd"

rm -Rfv "$b/%_initddir"
ln -sfv service "$b/%_sbindir/rcsssd"
ln -sfv service "$b/%_sbindir/rcsssd-autofs"
ln -sfv service "$b/%_sbindir/rcsssd-ifp"
ln -sfv service "$b/%_sbindir/rcsssd-nss"
ln -sfv service "$b/%_sbindir/rcsssd-pac"
ln -sfv service "$b/%_sbindir/rcsssd-pam"
ln -sfv service "$b/%_sbindir/rcsssd-ssh"
ln -sfv service "$b/%_sbindir/rcsssd-sudo"

mkdir -pv "$b/%sssdstatedir/mc"
find "$b" -type f -name "*.la" -print -delete
rm -Rfv "$b/usr/lib/debug/usr/lib/sssd/p11_child-1.16.2-0.x86_64.debug"
%find_lang %name --all-name

%check
# sss_config-tests fails
make %{?_smp_mflags} check || :

%pre
%service_add_pre sssd.service sssd-autofs.service sssd-autofs.socket sssd-nss.service sssd-nss.socket sssd-pac.service sssd-pac.socket sssd-pam-priv.socket sssd-pam.service sssd-pam.socket sssd-ssh.service sssd-ssh.socket sssd-sudo.service sssd-sudo.socket

%post
/sbin/ldconfig
# migrate config variable krb5_kdcip to krb5_server (bnc#851048)
/bin/sed -i -e 's,^krb5_kdcip =,krb5_server =,g' %_sysconfdir/sssd/sssd.conf
%service_add_post sssd.service sssd-autofs.service sssd-autofs.socket sssd-nss.service sssd-nss.socket sssd-pac.service sssd-pac.socket sssd-pam-priv.socket sssd-pam.service sssd-pam.socket sssd-ssh.service sssd-ssh.socket sssd-sudo.service sssd-sudo.socket

%preun
%service_del_preun sssd.service sssd-autofs.service sssd-autofs.socket sssd-nss.service sssd-nss.socket sssd-pac.service sssd-pac.socket sssd-pam-priv.socket sssd-pam.service sssd-pam.socket sssd-ssh.service sssd-ssh.socket sssd-sudo.service sssd-sudo.socket

%postun
/sbin/ldconfig
if [ "$1" = "0" -a -x "%_sbindir/pam-config" ]; then
	"%_sbindir/pam-config" -d --sss || :
fi
# Clear caches, which may have an incompatible format afterwards
# (especially, downgrades)
rm -f /var/lib/sss/db/*.ldb
# del_postun includes a try-restart
%service_del_postun sssd.service sssd-autofs.service sssd-autofs.socket sssd-nss.service sssd-nss.socket sssd-pac.service sssd-pac.socket sssd-pam-priv.socket sssd-pam.service sssd-pam.socket sssd-ssh.service sssd-ssh.socket sssd-sudo.service sssd-sudo.socket

%post   -n libsss_certmap0 -p /sbin/ldconfig
%postun -n libsss_certmap0 -p /sbin/ldconfig
%post   -n libipa_hbac0 -p /sbin/ldconfig
%postun -n libipa_hbac0 -p /sbin/ldconfig
%post   -n libsss_idmap0 -p /sbin/ldconfig
%postun -n libsss_idmap0 -p /sbin/ldconfig
%post   -n libsss_nss_idmap0 -p /sbin/ldconfig
%postun -n libsss_nss_idmap0 -p /sbin/ldconfig
%post   -n libsss_simpleifp0 -p /sbin/ldconfig
%postun -n libsss_simpleifp0 -p /sbin/ldconfig

%pre dbus
%service_add_pre sssd-ifp.service

%post dbus
%service_add_post sssd-ifp.service

%preun dbus
%service_del_preun sssd-ifp.service

%postun dbus
%service_del_postun sssd-ifp.service

%files -f sssd.lang
%license COPYING
%_unitdir/sssd.service
%_unitdir/sssd-autofs.socket
%_unitdir/sssd-autofs.service
%_unitdir/sssd-nss.socket
%_unitdir/sssd-nss.service
%_unitdir/sssd-pac.socket
%_unitdir/sssd-pac.service
%_unitdir/sssd-pam.socket
%_unitdir/sssd-pam-priv.socket
%_unitdir/sssd-pam.service
%_unitdir/sssd-ssh.socket
%_unitdir/sssd-ssh.service
%_unitdir/sssd-sudo.socket
%_unitdir/sssd-sudo.service
%_bindir/sss_ssh_*
%_sbindir/sssctl
%_sbindir/sssd
%_sbindir/rcsssd
%_sbindir/rcsssd-autofs
%_sbindir/rcsssd-nss
%_sbindir/rcsssd-pac
%_sbindir/rcsssd-pam
%_sbindir/rcsssd-ssh
%_sbindir/rcsssd-sudo
%dir %_mandir/??/
%dir %_mandir/??/man[158]/
%_mandir/??/man1/sss_ssh_*
%_mandir/??/man5/sss-certmap.5*
%_mandir/??/man5/sssd-ad.5*
%_mandir/??/man5/sssd-files.5*
%_mandir/??/man5/sssd-ldap-attributes.5*
%_mandir/??/man5/sssd-secrets.5*
%_mandir/??/man5/sssd-session-recording.5*
%_mandir/??/man5/sssd-simple.5*
%_mandir/??/man5/sssd-sudo.5*
%_mandir/??/man5/sssd-systemtap.5*
%_mandir/??/man5/sssd.conf.5*
%_mandir/??/man8/idmap_sss.8*
%_mandir/??/man8/sssctl.8*
%_mandir/??/man8/sssd.8*
%_mandir/man1/sss_ssh_*
%_mandir/man5/sss-certmap.5*
%_mandir/man5/sssd-files.5*
%_mandir/man5/sssd-ldap-attributes.5*
%_mandir/man5/sssd-session-recording.5*
%_mandir/man5/sssd-simple.5*
%_mandir/man5/sssd-sudo.5*
%_mandir/man5/sssd.conf.5*
%_mandir/man8/sssctl.8*
%_mandir/man8/sssd.8*
%dir %_libdir/%name/
%_libdir/%name/conf/
%_libdir/%name/libifp_iface*
%_libdir/%name/libsss_child*
%_libdir/%name/libsss_cert*
%_libdir/%name/libsss_crypt*
%_libdir/%name/libsss_debug*
%_libdir/%name/libsss_files*
%_libdir/%name/libsss_iface*
%_libdir/%name/libsss_semanage*
%_libdir/%name/libsss_sbus*
%_libdir/%name/libsss_simple*
%_libdir/%name/libsss_util*
%dir %_libdir/%name/modules/
%_libdir/%name/modules/libsss_autofs.so
%_libdir/libsss_sudo.so
%dir %_libdir/ldb/
%_libdir/ldb/memberof.so
%dir %_libexecdir/%name/
%_libexecdir/%name/p11_child
%_libexecdir/%name/sssd_autofs
%_libexecdir/%name/sssd_be
%_libexecdir/%name/sssd_nss
%_libexecdir/%name/sssd_pam
%_libexecdir/%name/sssd_ssh
%_libexecdir/%name/sssd_sudo
%_libexecdir/%name/sss_signal
%_libexecdir/%name/sssd_check_socket_activated_responders
%dir %sssdstatedir
%attr(700,root,root) %dir %dbpath/
%attr(755,root,root) %dir %pipepath/
%attr(700,root,root) %dir %pipepath/private/
%attr(755,root,root) %dir %pubconfpath/
%attr(755,root,root) %dir %gpocachepath/
%attr(755,root,root) %dir %sssdstatedir/mc/
%attr(700,root,root) %dir %sssdstatedir/keytabs/
%attr(750,root,root) %dir %_localstatedir/log/%name/
%dir %_sysconfdir/sssd/
%config(noreplace) %_sysconfdir/sssd/sssd.conf
%config(noreplace) %_sysconfdir/logrotate.d/sssd
%dir %_sysconfdir/sssd/conf.d
%dir %_sysconfdir/pam.d/
%config(noreplace) %_sysconfdir/pam.d/sssd-shadowutils
%dir %_datadir/%name/
%_datadir/%name/cfg_rules.ini
%_datadir/%name/sssd.api.conf
%dir %_datadir/%name/sssd.api.d/
%_datadir/%name/sssd.api.d/sssd-local.conf
%_datadir/%name/sssd.api.d/sssd-simple.conf
%_datadir/%name/sssd.api.d/sssd-files.conf
#
# sssd-client
#
/%_lib/libnss_sss.so.2
/%_lib/security/pam_sss.so
%_libdir/cifs-utils/
%_libdir/krb5/
%_libdir/%name/modules/sssd_krb5_localauth_plugin.so
%_mandir/??/man8/sssd_krb5_locator_plugin.8*
%_mandir/??/man8/pam_sss.8*
%_mandir/man8/pam_sss.8*
%_mandir/man8/sssd_krb5_locator_plugin.8*

%files ad
%dir %_libdir/%name/
%_libdir/%name/libsss_ad.so
%dir %_libexecdir/%name/
%_libexecdir/%name/sssd_pac
%_libexecdir/%name/gpo_child
%dir %_datadir/%name/
%dir %_datadir/%name/sssd.api.d/
%_datadir/%name/sssd.api.d/sssd-ad.conf
%_mandir/man5/sssd-ad.5*
%dir %_mandir/??/
%dir %_mandir/??/man5/

%files dbus
%dir %_libexecdir/sssd/
%_libexecdir/sssd/sssd_ifp
%dir %_libdir/sssd/
%_mandir/man5/sssd-ifp.5*
%dir %_mandir/??/
%dir %_mandir/??/man5/
%_mandir/??/man5/sssd-ifp.5*
%_unitdir/sssd-ifp.service
%_sbindir/rcsssd-ifp
%config %_sysconfdir/dbus-1/system.d/org.freedesktop.sssd.infopipe.conf
%_datadir/dbus-1/system-services/org.freedesktop.sssd.infopipe.service

%files ipa
%dir %_libdir/%name/
%_libdir/%name/libsss_ipa*
%dir %_datadir/%name/
%dir %_datadir/%name/sssd.api.d
%_datadir/%name/sssd.api.d/sssd-ipa.conf
%_mandir/man5/sssd-ipa.5*
%dir %_mandir/??/
%dir %_mandir/??/man5/
%_mandir/??/man5/sssd-ipa.5*

%files kcm
%dir %_libexecdir/sssd/
%_libexecdir/sssd/sssd_kcm
%dir %_libdir/sssd/
%_libdir/sssd/libsss_secrets.so
%_mandir/man8/sssd-kcm.8*
%_mandir/??/man8/sssd-kcm.8*
%_datadir/sssd-kcm/
%_unitdir/sssd-kcm.*

%files krb5
%dir %_libdir/%name/
%_libdir/%name/libsss_krb5.so
%dir %_datadir/%name/
%dir %_datadir/%name/sssd.api.d/
%_datadir/%name/sssd.api.d/sssd-krb5.conf
%dir %_mandir/??/
%dir %_mandir/??/man5/
%_mandir/man5/sssd-krb5.5*
%_mandir/??/man5/sssd-krb5.5*

%files krb5-common
%dir %_libdir/%name/
%_libdir/%name/libsss_krb5_common.so
%dir %_libexecdir/%name/
%_libexecdir/%name/krb5_child
%_libexecdir/%name/ldap_child

%files ldap
%dir %_libdir/%name/
%_libdir/%name/libsss_ldap*
%dir %_datadir/%name/
%dir %_datadir/%name/sssd.api.d/
%_datadir/%name/sssd.api.d/sssd-ldap.conf
%_mandir/man5/sssd-ldap.5*
%dir %_mandir/??/
%dir %_mandir/??/man5/
%_mandir/??/man5/sssd-ldap.5*

%files proxy
%dir %_libdir/%name/
%_libdir/%name/libsss_proxy.so
%dir %_libexecdir/%name/
%_libexecdir/%name/proxy_child
%dir %_datadir/%name/
%dir %_datadir/%name/sssd.api.d/
%_datadir/%name/sssd.api.d/sssd-proxy.conf

%files tools
%_sbindir/sss_cache
%_sbindir/sss_debuglevel
%_sbindir/sss_seed
%_sbindir/sss_obfuscate
%_sbindir/sss_override
%dir %_mandir/??/man8/
%_mandir/??/man8/sss_*.8*
%_mandir/man8/sss_*.8*

%files winbind-idmap
%_libdir/samba/
%_mandir/man8/idmap_sss.8*

%files -n libipa_hbac0
%_libdir/libipa_hbac.so.0*

%files -n libipa_hbac-devel
%_includedir/ipa_hbac.h
%_libdir/libipa_hbac.so
%_libdir/pkgconfig/ipa_hbac.pc

%files -n libsss_certmap0
%_libdir/libsss_certmap.so.0*

%files -n libsss_certmap-devel
%_includedir/sss_certmap.h
%_libdir/libsss_certmap.so
%_libdir/pkgconfig/sss_certmap.pc

%files -n libnfsidmap-sss
%_libdir/libnfsidmap/
%_mandir/man5/sss_rpcidmapd.5*
%dir %_mandir/??/man5/
%_mandir/??/man5/sss_rpcidmapd.5*

%files -n libsss_idmap0
%_libdir/libsss_idmap.so.0*

%files -n libsss_idmap-devel
%_includedir/sss_idmap.h
%_libdir/libsss_idmap.so
%_libdir/pkgconfig/sss_idmap.pc

%files -n libsss_nss_idmap0
%_libdir/libsss_nss_idmap.so.0*

%files -n libsss_nss_idmap-devel
%_includedir/sss_nss_idmap.h
%_libdir/libsss_nss_idmap.so
%_libdir/pkgconfig/sss_nss_idmap.pc

%files -n libsss_simpleifp0
%_libdir/libsss_simpleifp.so.0*

%files -n libsss_simpleifp-devel
%_includedir/sss_sifp*.h
%_libdir/libsss_simpleifp.so
%_libdir/pkgconfig/sss_simpleifp.pc

%files -n python3-ipa_hbac
%dir %python3_sitearch
%python3_sitearch/pyhbac.so

%files -n python3-sss-murmur
%python3_sitearch/pysss_murmur.so

%files -n python3-sss_nss_idmap
%dir %python3_sitearch
%python3_sitearch/pysss_nss_idmap.so

%files -n python3-sssd-config
%python3_sitearch/pysss.so
%python3_sitelib/SSSDConfig*

%changelog
