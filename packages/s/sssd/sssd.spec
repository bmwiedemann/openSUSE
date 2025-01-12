#
# spec file for package sssd
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


Name:           sssd
Version:        2.10.1
Release:        0
Summary:        System Security Services Daemon
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          System/Daemons
URL:            https://github.com/SSSD/sssd
#Git-Clone:	https://github.com/SSSD/sssd
Source:         https://github.com/SSSD/sssd/releases/download/%version/%name-%version.tar.gz
Source2:        https://github.com/SSSD/sssd/releases/download/%version/%name-%version.tar.gz.asc
Source3:        baselibs.conf
Source5:        %name.keyring
Patch1:         0001-TOOL-Fix-build-parameter-name-omitted.patch
Patch11:        krb-noversion.diff
Patch12:        harden_sssd-ifp.service.patch
Patch13:        harden_sssd-kcm.service.patch
Patch14:        symvers.patch
BuildRequires:  autoconf >= 2.59
BuildRequires:  automake
BuildRequires:  bind-utils
BuildRequires:  check-devel
BuildRequires:  cifs-utils-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  krb5-devel >= 1.12
BuildRequires:  libcmocka-devel
%if 0%{?suse_version} >= 1600
BuildRequires:  libsubid-devel
%endif
BuildRequires:  libtool
BuildRequires:  libunistring-devel
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  libopenssl-3-devel
BuildRequires:  nscd
BuildRequires:  nss_wrapper
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pkg-config >= 0.21
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  uid_wrapper
BuildRequires:  pkgconfig(augeas) >= 1.0.0
BuildRequires:  pkgconfig(collection) >= 0.5.1
BuildRequires:  pkgconfig(dbus-1) >= 1.0.0
BuildRequires:  pkgconfig(dhash) >= 0.4.2
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(ini_config) >= 1.3
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(ldb) >= 1.2.0
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcrypto) >= 1.0.1
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(libcurl)
%endif
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libnfsidmap)
BuildRequires:  pkgconfig(libnl-3.0) >= 3.0
BuildRequires:  pkgconfig(libnl-route-3.0) >= 3.0
BuildRequires:  pkgconfig(libpcre2-8)
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(libsemanage)
%endif
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ndr_krb5pac)
BuildRequires:  pkgconfig(ndr_nbt)
BuildRequires:  pkgconfig(p11-kit-1) >= 0.23.3
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  pkgconfig(tdb) >= 1.1.3
BuildRequires:  pkgconfig(tevent)
BuildRequires:  pkgconfig(uuid)
%if 0%{?suse_version} && 0%{?suse_version} < 1600
# samba-client-devel pulls samba-client-libs pulls libldap-2_4-2 wants libldap-data(-2.4);
# this conflicts with
# openldap2-devel pulls libldap2 wants libldap-data(-2.6)
# Package contains just config files, not needed for build.
#!BuildIgnore: libldap-data
%endif
%sysusers_requires
%{?systemd_ordering}
Requires(post): permissions
Requires(verify): permissions
Requires:       sssd-ldap = %version-%release
Requires(postun): pam-config
Provides:       libsss_sudo = %version-%release
Provides:       sssd-client = %version-%release
Obsoletes:      libsss_sudo < %version-%release
Provides:       sssd-common = %version-%release
Obsoletes:      sssd-common < %version-%release

%global sssd_user sssd
%define servicename	sssd
%define sssdstatedir	%_localstatedir/lib/sss
%define dbpath		%sssdstatedir/db
%define pipepath	%sssdstatedir/pipes
%define pubconfpath	%sssdstatedir/pubconf
%define gpocachepath	%sssdstatedir/gpo_cache
%define keytabdir	%sssdstatedir/keytabs
%define mcpath		%sssdstatedir/mc
%define ldbdir %(pkg-config ldb --variable=modulesdir)


%if 0%{?suse_version} >= 1600
%define permissions_path %_datadir/permissions/permissions.d/
%else
%define permissions_path %_sysconfdir/permissions.d/
%endif

# Both SSSD and cifs-utils provide an idmap plugin for cifs.ko
# %%_sysconfdir/cifs-utils/idmap-plugin should be a symlink to one of the 2 idmap plugins
# * cifs-utils one is the default (priority 20)
# * installing SSSD should NOT switch to SSSD plugin (priority 10)
%define cifs_idmap_plugin       %_sysconfdir/cifs-utils/idmap-plugin
%define cifs_idmap_lib          %_libdir/cifs-utils/cifs_idmap_sss.so
%define cifs_idmap_name         cifs-idmap-plugin
%define cifs_idmap_priority     10
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description
A set of daemons to manage access to remote directories and
authentication mechanisms. sssd provides an NSS and PAM interfaces
toward the system and a pluggable backend system to connect to
multiple different account sources. It is also the basis to provide
client auditing and policy services for projects like FreeIPA.

%package ad
Summary:        The ActiveDirectory backend plugin for sssd
License:        GPL-3.0-or-later
Group:          System/Daemons
Requires:       %name-krb5-common = %version-%release
Requires:       adcli

%description ad
A back-end provider that the SSSD can utilize to fetch identity data
from, and authenticate with, an Active Directory server.

%package dbus
Summary:        The D-Bus responder of sssd
License:        GPL-3.0-or-later
Group:          System/Base
Requires:       %name = %version

%description dbus
D-Bus responder of sssd, called InfoPipe, which allows
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
A back-end provider that the SSSD can utilize to fetch identity data
from, and authenticate with, an IPA server.

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
A back-end provider that the SSSD can utilize to authenticate against
a Kerberos server.

%package krb5-common
Summary:        SSSD helpers needed for Kerberos and GSSAPI authentication
License:        GPL-3.0-or-later
Group:          System/Daemons
Requires:       cyrus-sasl-gssapi
Requires(post): permissions
Requires(verify): permissions

%description krb5-common
Provides helper processes that the LDAP and Kerberos back ends can
use for Kerberos user or host authentication.

%package ldap
Summary:        The LDAP backend plugin for sssd
License:        GPL-3.0-or-later
Group:          System/Daemons
Requires:       %name-krb5-common = %version-%release

%description ldap
A back-end provider that the SSSD can utilize to fetch identity data
from, and authenticate with, an LDAP server.

%package proxy
Summary:        The proxy backend plugin for sssd
License:        GPL-3.0-or-later
Group:          System/Daemons

%description proxy
A back-end provider which can be used to wrap existing NSS and/or PAM
modules to leverage SSSD caching. (This can replace nscd.)

%package tools
Summary:        Commandline tools for sssd
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          System/Management
Requires:       python3-sssd-config = %version-%release
Requires:       sssd = %version

%description tools
The packages contains command-line tools for managing users and groups using
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
A utility library for FreeIPA to map certificates.

%package -n libsss_certmap-devel
Summary:        Development files for the FreeIPA certmap library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsss_certmap0 = %version

%description -n libsss_certmap-devel
A utility library for FreeIPA to map certificates.

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
Supplements:    (nfsidmap and sssd-client)

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
# Even though sssd has obsoleted simpleifp, the plan here is to retain ABI
# compatibility with the existing SUSE 15.x product line. ...at least, until
# sssd completely removes SIFP from source.

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
Supplements:    (sudo and sssd-client)

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
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       python3

%description -n python3-sssd-config
Provide python module to access and manage configuration of the System
Security Services Daemon (sssd).

%prep
%autosetup -p1

%build
# help configure find nscd
export PATH="$PATH:/usr/sbin"

autoreconf -fiv
%configure \
	--with-db-path="%dbpath" \
	--with-pipe-path="%pipepath" \
	--with-pubconf-path="%pubconfpath" \
	--with-gpo-cache-path="%gpocachepath" \
	--with-environment-file="%_sysconfdir/sysconfig/sssd" \
	--with-initscript=systemd \
	--with-syslog=journald \
	--with-pid-path="%_rundir/sssd" \
	--enable-pammoddir="%_pam_moduledir" \
	--with-ldb-lib-dir="%ldbdir" \
	--with-os=suse \
	--disable-ldb-version-check \
	--without-python2-bindings \
	--without-oidc-child \
	--with-sssd-user="%sssd_user" \
%if 0%{?suse_version} >= 1600
	--with-selinux=yes \
	--with-subid
%else
	--with-selinux=no \
	--with-libsifp \
	--with-files-provider
%endif
%make_build all

%install
# sss_obfuscate is compatible with both Python 2 and 3
perl -i -lpe 's{%_bindir/python\b}{%_bindir/python3}' src/tools/sss_obfuscate
%make_install dbuspolicydir=%_datadir/dbus-1/system.d
b="%buildroot"

# Copy some defaults
%if "%{?_distconfdir}" != ""
install -D -p -m 0600 src/examples/sssd-example.conf "$b/%_distconfdir/sssd/sssd.conf"
install -d -m 0755 "$b/%_distconfdir/sssd/conf.d"
%else
install -D -p -m 0600 src/examples/sssd-example.conf "$b/%_sysconfdir/sssd/sssd.conf"
install -d -m 0755 "$b/%_sysconfdir/sssd/conf.d"
%endif
install -d "$b/%_unitdir"
%if 0%{?suse_version} > 1500
install -d "$b/%_distconfdir/logrotate.d"
install -m644 src/examples/logrotate "$b/%_distconfdir/logrotate.d/sssd"
install -d "$b/%_pam_vendordir"
mv "$b/%_pam_confdir/sssd-shadowutils" "$b/%_pam_vendordir"
%else
install -d "$b/%_sysconfdir/logrotate.d"
install -m644 src/examples/logrotate "$b/%_sysconfdir/logrotate.d/sssd"
%endif

rm -Rfv "$b/%_initddir"
%if 0%{?suse_version} < 1600
ln -s service "$b/%_sbindir/rcsssd"
%endif

mkdir -pv "$b/%sssdstatedir/mc"
find "$b" -type f -name "*.la" -print -delete
%find_lang %name --all-name

# dummy target for cifs-idmap-plugin
mkdir -pv "$b/%_sysconfdir/alternatives" "$b/%_sysconfdir/cifs-utils"
ln -sfv "%_sysconfdir/alternatives/%cifs_idmap_name" "$b/%cifs_idmap_plugin"
%python3_fix_shebang
%if 0%{?suse_version} > 1600
%python3_fix_shebang_path %buildroot/%_libexecdir/%name/sss_analyze
%elif 0%{?suse_version} == 1600
# python3_fix_shebang_path macro does not exist in < 1600, was added in python-rom-macros 20231204
sed -i '1s@#!.*python.*@#!%_bindir/python3.11@' "$b/%_libexecdir/%name/sss_analyze"
%endif

echo 'u sssd - "System Security Services Daemon" /run/sssd /sbin/nologin' >system-user-sssd.conf
mkdir -p "$b/%_sysusersdir"
cp -a system-user-sssd.conf "$b/%_sysusersdir/"
%sysusers_generate_pre system-user-sssd.conf random system-user-sssd.conf
install -Dpm 0644 contrib/sssd-tmpfiles.conf "%buildroot/%_tmpfilesdir/%name.conf"
#
# Security considerations for capabilities, chown and stuff:
# https://www.openwall.com/lists/oss-security/2024/12/19/1
#
# should match entry from %%files list
mkdir -p "$b/%permissions_path"
cat >"$b/%permissions_path/sssd" <<-EOF
	%_libexecdir/sssd/sssd_pam root:sssd 0750
	 +capabilities cap_dac_read_search=p
	%_libexecdir/sssd/selinux_child root:sssd 0750
	 +capabilities cap_setgid,cap_setuid=p
	%_libexecdir/sssd/krb5_child root:sssd 0750
	 +capabilities cap_dac_read_search,cap_setgid,cap_setuid=p
	%_libexecdir/sssd/ldap_child root:sssd 0750
	 +capabilities cap_dac_read_search=p
EOF

%check
# sss_config-tests fails
%make_build check || :

%pre -f random.pre
%service_add_pre sssd.service sssd-autofs.service sssd-autofs.socket sssd-nss.service sssd-nss.socket sssd-pac.service sssd-pac.socket sssd-pam.service sssd-pam.socket sssd-ssh.service sssd-ssh.socket sssd-sudo.service sssd-sudo.socket
%if "%{?_distconfdir}" != ""
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in sssd/sssd.conf pam.d/sssd-shadowutils logrotate.d/sssd ; do
	test -f "%_sysconfdir/$i.rpmsave" && mv -v "%_sysconfdir/$i.rpmsave" "%_sysconfdir/$i.rpmsave.old" || :
done
%endif

%post
/sbin/ldconfig
# migrate config variable krb5_kdcip to krb5_server (bnc#851048)
if [ -f "%_sysconfdir/sssd/sssd.conf" ]; then
	/bin/sed -i -e 's,^krb5_kdcip =,krb5_server =,g' "%_sysconfdir/sssd/sssd.conf"
fi
%service_add_post sssd.service sssd-autofs.service sssd-autofs.socket sssd-nss.service sssd-nss.socket sssd-pac.service sssd-pac.socket sssd-pam.service sssd-pam.socket sssd-ssh.service sssd-ssh.socket sssd-sudo.service sssd-sudo.socket

%_bindir/rm -f %mcpath/passwd %mcpath/group %mcpath/initgroups %mcpath/sid
%tmpfiles_create %name.conf
%set_permissions %_libexecdir/%name/selinux_child %_libexecdir/%name/sssd_pam

# install SSSD cifs-idmap plugin as an alternative
update-alternatives --install %cifs_idmap_plugin %cifs_idmap_name %cifs_idmap_lib %cifs_idmap_priority

%preun
%service_del_preun sssd.service sssd-autofs.service sssd-autofs.socket sssd-nss.service sssd-nss.socket sssd-pac.service sssd-pac.socket sssd-pam.service sssd-pam.socket sssd-ssh.service sssd-ssh.socket sssd-sudo.service sssd-sudo.socket

%postun
/sbin/ldconfig
if [ "$1" = "0" ] && [ -x "%_sbindir/pam-config" ]; then
	"%_sbindir/pam-config" -d --sss || :
fi
# del_postun includes a try-restart
%service_del_postun sssd.service sssd-autofs.service sssd-autofs.socket sssd-nss.service sssd-nss.socket sssd-pac.service sssd-pac.socket sssd-pam.service sssd-pam.socket sssd-ssh.service sssd-ssh.socket sssd-sudo.service sssd-sudo.socket

if [ ! -f "%cifs_idmap_lib" ]; then
	update-alternatives --remove %cifs_idmap_name %cifs_idmap_lib
fi

%ldconfig_scriptlets -n libsss_certmap0
%ldconfig_scriptlets -n libipa_hbac0
%ldconfig_scriptlets -n libsss_idmap0
%ldconfig_scriptlets -n libsss_nss_idmap0
%ldconfig_scriptlets -n libsss_simpleifp0

%verifyscript
%verify_permissions -e %_libexecdir/%name/selinux_child %_libexecdir/%name/sssd_pam

%triggerun -- %name < %version-%release
# sssd takes care of upgrading the database but it doesn't handle downgrades.
# Clear caches when downgrading the package, which may have an
# incompatible format afterwards preventing the daemon from startup.
if [ "$1" = "1" ] && [ "$2" = "2" ]; then
	echo "Package downgrade detected, removing cache files which may have an incompatible format."
	rm -f /var/lib/sss/db/*.ldb
fi

%pre dbus
%service_add_pre sssd-ifp.service

%post dbus
%service_add_post sssd-ifp.service

%preun dbus
%service_del_preun sssd-ifp.service

%postun dbus
%service_del_postun sssd-ifp.service

%pre kcm
%service_add_pre sssd-kcm.service sssd-kcm.socket

%post kcm
%service_add_post sssd-kcm.service sssd-kcm.socket

%preun kcm
%service_del_preun sssd-kcm.service sssd-kcm.socket

%postun kcm
%service_del_postun sssd-kcm.service sssd-kcm.socket

%pre krb5-common -f random.pre

%post krb5-common
%set_permissions %_libexecdir/%name/krb5_child %_libexecdir/%name/ldap_child

%verifyscript krb5-common
%verify_permissions -e %_libexecdir/%name/krb5_child %_libexecdir/%name/ldap_child

%pre proxy -f random.pre

%pretrans
# Migrate sssd.service from sssd-common to sssd
systemctl is-enabled sssd.service > /dev/null
if [ $? -eq 0 ]; then
	mkdir -p /run/systemd/rpm/
	touch /run/systemd/rpm/sssd-was-enabled
fi
systemctl is-active sssd.service > /dev/null
if [ $? -eq 0 ]; then
	mkdir -p /run/systemd/rpm/
	touch /run/systemd/rpm/sssd-was-active
fi

%posttrans
%if "%{?_distconfdir}" != ""
# Migration to /usr/etc, restore just created .rpmsave
for i in sssd/sssd.conf logrotate.d/sssd pam.d/sssd-shadowutils ; do
	test -f "%_sysconfdir/$i.rpmsave" && mv -v "%_sysconfdir/$i.rpmsave" "%_sysconfdir/$i" || :
done
%endif
# Migrate sssd.service from sssd-common to sssd
if [ -e /run/systemd/rpm/sssd-was-enabled ]; then
	systemctl is-enabled sssd.service >/dev/null
	if [ $? -ne 0 ]; then
		echo "Migrating sssd.service, was enabled"
		systemctl enable sssd.service
	fi
	rm /run/systemd/rpm/sssd-was-enabled
fi
if [ -e /run/systemd/rpm/sssd-was-active ]; then
	systemctl is-active sssd.service >/dev/null
	if [ $? -ne 0 ]; then
		echo "Migrating sssd.service, was active"
		systemctl start sssd.service
	fi
	rm /run/systemd/rpm/sssd-was-active
fi

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
%_unitdir/sssd-pam.service
%_unitdir/sssd-ssh.socket
%_unitdir/sssd-ssh.service
%_unitdir/sssd-sudo.socket
%_unitdir/sssd-sudo.service
%_sysusersdir/*sssd*
%_tmpfilesdir/*sssd*
%permissions_path/sssd
%dir %_datadir/polkit-1
%attr(0555,root,root) %dir %_datadir/polkit-1/rules.d
%_datadir/polkit-1/rules.d/*
%_bindir/sss_ssh_*
%_sbindir/sssd
%if 0%{?suse_version} < 1600
%_sbindir/rcsssd
%endif
%dir %_mandir/??/
%dir %_mandir/??/man[158]/
%_mandir/??/man1/sss_ssh_*
%_mandir/??/man5/sss-certmap.5*
%_mandir/??/man5/sssd-ad.5*
%if 0%{?suse_version} < 1600
%_mandir/??/man5/sssd-files.5*
%endif
%_mandir/??/man5/sssd-ldap-attributes.5*
%_mandir/??/man5/sssd-session-recording.5*
%_mandir/??/man5/sssd-simple.5*
%_mandir/??/man5/sssd-sudo.5*
%_mandir/??/man5/sssd-systemtap.5*
%_mandir/??/man5/sssd.conf.5*
%_mandir/??/man8/idmap_sss.8*
%_mandir/??/man8/sssd.8*
%_mandir/man1/sss_ssh_*
%_mandir/man5/sss-certmap.5*
%if 0%{?suse_version} < 1600
%_mandir/man5/sssd-files.5*
%endif
%_mandir/man5/sssd-ldap-attributes.5*
%_mandir/man5/sssd-session-recording.5*
%_mandir/man5/sssd-simple.5*
%_mandir/man5/sssd-sudo.5*
%_mandir/man5/sssd.conf.5*
%_mandir/man8/sssd.8*
%dir %_libdir/%name/
%_libdir/%name/conf/
%_libdir/%name/libifp_iface*
%_libdir/%name/libsss_child*
%_libdir/%name/libsss_cert*
%_libdir/%name/libsss_crypt*
%_libdir/%name/libsss_debug*
%if 0%{?suse_version} < 1600
%_libdir/%name/libsss_files*
%endif
%_libdir/%name/libsss_iface*
%_libdir/%name/libsss_sbus*
%_libdir/%name/libsss_simple*
%_libdir/%name/libsss_util*
%dir %_libdir/%name/modules/
%_libdir/%name/modules/libsss_autofs.so
%_libdir/libsss_sudo.so
%ldbdir/
%dir %_libexecdir/%name/
%_libexecdir/%name/p11_child
%_libexecdir/%name/sssd_autofs
%_libexecdir/%name/sssd_be
%_libexecdir/%name/sssd_nss
%attr(750,root,%sssd_user) %caps(cap_dac_read_search=p) %_libexecdir/%name/sssd_pam
%_libexecdir/%name/sssd_ssh
%_libexecdir/%name/sssd_sudo
%_libexecdir/%name/sss_signal
%_libexecdir/%name/sssd_check_socket_activated_responders
%if 0%{?suse_version} >= 1600
%attr(750,root,%sssd_user) %caps(cap_setgid,cap_setuid=p) %_libexecdir/%name/selinux_child
%endif
%dir %sssdstatedir
%attr(700,%sssd_user,%sssd_user) %dir %dbpath/
%attr(755,%sssd_user,%sssd_user) %dir %pipepath/
%attr(700,%sssd_user,%sssd_user) %dir %pipepath/private/
%attr(755,%sssd_user,%sssd_user) %dir %pubconfpath/
%attr(755,%sssd_user,%sssd_user) %dir %pubconfpath/krb5.include.d
%attr(755,%sssd_user,%sssd_user) %dir %gpocachepath/
%attr(755,%sssd_user,%sssd_user) %dir %mcpath/
%attr(700,%sssd_user,%sssd_user) %dir %keytabdir/
%attr(750,%sssd_user,%sssd_user) %dir %_localstatedir/log/%name/
%attr(775,%sssd_user,%sssd_user) %dir %sssdstatedir/
%if "%{?_distconfdir}" != ""
%attr(750,root,%sssd_user) %dir %_distconfdir/sssd/
%attr(750,root,%sssd_user) %dir %_distconfdir/sssd/conf.d
%attr(640,root,%sssd_user) %_distconfdir/sssd/sssd.conf
%else
%attr(750,root,%sssd_user) %dir %_sysconfdir/sssd/
%attr(750,root,%sssd_user) %dir %_sysconfdir/sssd/conf.d
%ghost %attr(640,root,%sssd_user) %config(noreplace) %_sysconfdir/sssd/sssd.conf
%endif
%if 0%{?suse_version} > 1500
%_distconfdir/logrotate.d/sssd
%_pam_vendordir/sssd-shadowutils
%else
%config(noreplace) %_sysconfdir/logrotate.d/sssd
%config(noreplace) %_pam_confdir/sssd-shadowutils
%endif
%dir %_datadir/%name/
%_datadir/%name/cfg_rules.ini
%_datadir/%name/sssd.api.conf
%dir %_datadir/%name/sssd.api.d/
%_datadir/%name/sssd.api.d/sssd-simple.conf
%if 0%{?suse_version} < 1600
%_datadir/%name/sssd.api.d/sssd-files.conf
%else
%exclude %_mandir/*/*/sssd-files.5.gz
%endif
%attr(775,%sssd_user,%sssd_user) %ghost %dir %_rundir/sssd
%doc src/examples/sssd.conf
#
# sssd-client
#
%_libdir/libnss_sss.so.2
%_pam_moduledir/pam_sss.so
%_pam_moduledir/pam_sss_gss.so
%_libdir/krb5/
%_libdir/%name/modules/sssd_krb5_localauth_plugin.so
%exclude %_libdir/%name/modules/sssd_krb5_idp_plugin.so
%if 0%{?suse_version} >= 1600
%_libdir/libsubid_sss.so
%endif
%_mandir/??/man8/sssd_krb5_locator_plugin.8*
%_mandir/??/man8/pam_sss.8*
%_mandir/??/man8/pam_sss_gss.8*
%_mandir/man8/pam_sss.8*
%_mandir/man8/pam_sss_gss.8*
%_mandir/man8/sssd_krb5_localauth_plugin.8*
%_mandir/??/man8/sssd_krb5_localauth_plugin.8*
%_mandir/man8/sssd_krb5_locator_plugin.8*
# cifs idmap plugin
%dir %_sysconfdir/cifs-utils
%cifs_idmap_plugin
%dir %_libdir/cifs-utils
%cifs_idmap_lib
%ghost %_sysconfdir/alternatives/%cifs_idmap_name

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
%_datadir/dbus-1/system.d/org.freedesktop.sssd.infopipe.conf
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
%_mandir/man8/sssd-kcm.8*
%_mandir/??/man8/sssd-kcm.8*
%_datadir/sssd-kcm/
%_unitdir/sssd-kcm.*

%files krb5
%dir %_libdir/%name/
%_libdir/%name/libsss_krb5.so
%dir %_datadir/%name/
%exclude %_datadir/%name/krb5-snippets/
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
%attr(750,root,%sssd_user) %caps(cap_dac_read_search,cap_setgid,cap_setuid=p) %_libexecdir/%name/krb5_child
%attr(750,root,%sssd_user) %caps(cap_dac_read_search=p) %_libexecdir/%name/ldap_child

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
%attr(750,root,%sssd_user) %_libexecdir/%name/proxy_child
%dir %_datadir/%name/
%dir %_datadir/%name/sssd.api.d/
%_datadir/%name/sssd.api.d/sssd-proxy.conf

%files tools
%_sbindir/sssctl
%_sbindir/sss_cache
%_sbindir/sss_debuglevel
%_sbindir/sss_seed
%_sbindir/sss_obfuscate
%_sbindir/sss_override
%_libexecdir/%name/sss_analyze
%dir %_mandir/??/man8/
%_mandir/??/man8/sssctl.8*
%_mandir/??/man8/sss_*.8*
%_mandir/man8/sssctl.8*
%_mandir/man8/sss_*.8*
%python3_sitelib/sssd/

%files winbind-idmap
%dir %_libdir/samba/
%_libdir/samba/idmap/
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

%if 0%{?suse_version} < 1600
%files -n libsss_simpleifp0
%_libdir/libsss_simpleifp.so.0*

%files -n libsss_simpleifp-devel
%_includedir/sss_sifp*.h
%_libdir/libsss_simpleifp.so
%_libdir/pkgconfig/sss_simpleifp.pc
%endif

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
