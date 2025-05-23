#
# spec file for package openssh
#
# Copyright (c) 2025 SUSE LLC
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


%define sandbox_seccomp 0
%ifnarch ppc loongarch64
%define sandbox_seccomp 1
%endif
%if !%{sandbox_seccomp}
%ifarch loongarch64
%define sandbox_rlimit 0
%else
%define sandbox_rlimit 1
%endif
%endif
%define _fwdir      %{_sysconfdir}/sysconfig/SuSEfirewall2.d
%define _fwdefdir   %{_fwdir}/services
%define _appdefdir  %( grep "configdirspec=" $( which xmkmf ) | sed -r 's,^[^=]+=.*-I(.*)/config.*$,\\1/app-defaults,' )
%define CHECKSUM_SUFFIX .hmac
%define CHECKSUM_HMAC_KEY "HMAC_KEY:OpenSSH-FIPS@SLE"
%bcond_without ldap

%if 0%{?suse_version} >= 1550
%bcond_without wtmpdb
%bcond_with allow_root_password_login_by_default
%else
%bcond_with wtmpdb
%bcond_without allow_root_password_login_by_default
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600
%bcond_without crypto_policies
%else
%bcond_with crypto_policies
%endif

%if 0%{?suse_version} < 1500
%bcond_without openssl11
%else
%bcond_with openssl11
%endif

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           openssh
Version:        10.0p2
%define wrongly_named_version 10.0p1
Release:        0
Summary:        Secure Shell Client and Server (Remote Login Program)
License:        BSD-2-Clause AND MIT
Group:          Productivity/Networking/SSH
URL:            https://www.openssh.com/
Source0:        https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{wrongly_named_version}.tar.gz
Source1:        https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{wrongly_named_version}.tar.gz.asc
Source2:        sshd.pamd
Source3:        README.SUSE
Source4:        README.kerberos
Source5:        ssh.reg
Source6:        ssh-askpass
Source7:        sshd.fw
Source8:        sysconfig.ssh
Source9:        sshd-gen-keys-start
Source10:       sshd.service
Source11:       README.FIPS
Source12:       cavs_driver-ssh.pl
Source13:       https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/RELEASE_KEY.asc#/openssh.keyring
Source14:       sysusers-sshd.conf
Source15:       sshd-sle.pamd
Source16:       sshd@.service
Source17:       sshd.socket
Patch1:         openssh-7.7p1-X11_trusted_forwarding.patch
Patch3:         openssh-7.7p1-enable_PAM_by_default.patch
Patch4:         openssh-7.7p1-eal3.patch
Patch6:         openssh-7.7p1-send_locale.patch
Patch7:         openssh-7.7p1-hostname_changes_when_forwarding_X.patch
Patch8:         openssh-7.7p1-remove_xauth_cookies_on_exit.patch
Patch9:         openssh-7.7p1-pts_names_formatting.patch
Patch10:        openssh-7.7p1-pam_check_locks.patch
# https://bugzilla.mindrot.org/show_bug.cgi?id=2752
Patch14:        openssh-7.7p1-seccomp_stat.patch
# https://bugzilla.mindrot.org/show_bug.cgi?id=2752
Patch15:        openssh-7.7p1-seccomp_ipc_flock.patch
# https://bugzilla.mindrot.org/show_bug.cgi?id=2752
# Local FIPS patchset
Patch17:        openssh-7.7p1-fips.patch
# Local cavs patchset
Patch18:        openssh-7.7p1-cavstest-ctr.patch
# Local cavs patchset
Patch19:        openssh-7.7p1-cavstest-kdf.patch
# Local FIPS patchset
Patch20:        openssh-7.7p1-fips_checks.patch
# https://bugzilla.mindrot.org/show_bug.cgi?id=2641
Patch22:        openssh-7.7p1-systemd-notify.patch
Patch23:        openssh-8.0p1-gssapi-keyex.patch
# https://bugzilla.mindrot.org/show_bug.cgi?id=1402
Patch24:        openssh-8.1p1-audit.patch
# Local patch to disable runtime abi SSL checks, quite pointless for us
Patch26:        openssh-7.7p1-disable_openssl_abi_check.patch
# https://bugzilla.mindrot.org/show_bug.cgi?id=2641
Patch27:        openssh-7.7p1-no_fork-no_pid_file.patch
Patch28:        openssh-7.7p1-host_ident.patch
# https://bugzilla.mindrot.org/show_bug.cgi?id=1844
Patch29:        openssh-7.7p1-sftp_force_permissions.patch
# https://bugzilla.mindrot.org/show_bug.cgi?id=2143
Patch30:        openssh-7.7p1-X_forward_with_disabled_ipv6.patch
Patch31:        openssh-7.7p1-ldap.patch
# https://bugzilla.mindrot.org/show_bug.cgi?id=2213
Patch32:        openssh-7.7p1-IPv6_X_forwarding.patch
Patch33:        openssh-7.7p1-sftp_print_diagnostic_messages.patch
Patch34:        openssh-7.9p1-keygen-preserve-perms.patch
Patch35:        openssh-7.9p1-revert-new-qos-defaults.patch
Patch36:        openssh-8.1p1-seccomp-clock_nanosleep.patch
Patch37:        openssh-8.1p1-seccomp-clock_nanosleep_time64.patch
Patch38:        openssh-8.1p1-seccomp-clock_gettime64.patch
Patch39:        openssh-8.1p1-use-openssl-kdf.patch
Patch40:        openssh-8.1p1-ed25519-use-openssl-rng.patch
Patch41:        openssh-fips-ensure-approved-moduli.patch
Patch42:        openssh-link-with-sk.patch
Patch45:        openssh-8.4p1-ssh_config_d.patch
Patch46:        openssh-whitelist-syscalls.patch
Patch47:        openssh-8.4p1-vendordir.patch
Patch48:        openssh-8.4p1-pam_motd.patch
Patch49:        openssh-do-not-send-empty-message.patch
Patch50:        openssh-openssl-3.patch
Patch52:        logind_set_tty.patch
Patch54:        openssh-mitigate-lingering-secrets.patch
Patch102:       openssh-7.8p1-role-mls.patch
Patch103:       openssh-6.6p1-privsep-selinux.patch
Patch104:       openssh-6.6p1-keycat.patch
Patch105:       openssh-6.6.1p1-selinux-contexts.patch
Patch106:       openssh-7.6p1-cleanup-selinux.patch
Patch107:       openssh-send-extra-term-env.patch
# 200 - 300  --  Patches submitted to upstream
# PATCH-FIX-UPSTREAM -- https://github.com/openssh/openssh-portable/pull/452 boo#1229010
Patch200:       0001-auth-pam-Immediately-report-instructions-to-clients-and-fix-handling-in-ssh-client.patch
# 1000 - 2000  --  Conditional patches
%if %{with crypto_policies}
# PATCH-FIX-OPENSUSE bsc#1211301 Add crypto-policies support
Patch1000:      openssh-9.6p1-crypto-policies.patch
Patch1001:      openssh-9.6p1-crypto-policies-man.patch
%endif
%if %{with allow_root_password_login_by_default}
# PATCH-FIX-SLE Allow root login with password by default (for SLE12 and SLE15)
Patch1002:      openssh-7.7p1-allow_root_password_login.patch
%endif
BuildRequires:  audit-devel
BuildRequires:  automake
%if 0%{?suse_version} < 1600
BuildRequires:  gcc11
%endif
BuildRequires:  groff
BuildRequires:  libedit-devel
BuildRequires:  libselinux-devel
%if %{with ldap}
BuildRequires:  openldap2-devel
%endif
%if %{with openssl11}
BuildRequires:  libopenssl-1_1-devel
BuildRequires:  openssl-1_1
%else
BuildRequires:  openssl-devel
%endif
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libfido2) >= 1.2.0
BuildRequires:  pkgconfig(libsystemd)
Requires:       %{name}-clients = %{version}-%{release}
Requires:       %{name}-server = %{version}-%{release}
%if 0%{?suse_version} >= 1550 || 0%{?suse_version} < 1500
BuildRequires:  pkgconfig(krb5)
%else
BuildRequires:  krb5-mini-devel
%endif
%if %{with wtmpdb}
BuildRequires:  pkgconfig(libwtmpdb)
%endif
Requires(pre):  findutils
Requires(pre):  grep

%description
SSH (Secure Shell) is a program for logging into and executing commands
on a remote machine. It replaces rsh (rlogin and rsh) and
provides secure encrypted communication between two untrusted
hosts over an insecure network.

xorg-x11 (X Window System) connections and arbitrary TCP/IP ports can
also be forwarded over the secure channel.

This is a dummy package that pulls in both the client and server
components.

%package common
Summary:        SSH (Secure Shell) common files
Group:          Productivity/Networking/SSH
Conflicts:      nonfreessh
Provides:       %{name}-fips = %{version}-%{release}
Obsoletes:      %{name}-fips < %{version}-%{release}

%description common
SSH (Secure Shell) is a program for logging into and executing commands
on a remote machine. It replaces rsh (rlogin and rsh) and
provides secure encrypted communication between two untrusted
hosts over an insecure network.

xorg-x11 (X Window System) connections and arbitrary TCP/IP ports can
also be forwarded over the secure channel.

This package contains common files for the Secure Shell server and
clients.

%package server
Summary:        SSH (Secure Shell) server
Group:          Productivity/Networking/SSH
Requires:       %{name}-common = %{version}-%{release}
%if %{with crypto_policies}
Requires:       crypto-policies >= 20220824
%endif
Recommends:     audit
Requires(pre):  findutils
Requires(pre):  grep
Requires(post): %fillup_prereq
Requires(post): permissions
Provides:       openssh:%{_sbindir}/sshd
%if %{with allow_root_password_login_by_default}
# For a brief period of time this package existed in SLE/Leap.
# It was removed before GM but some people might have it from
# a beta distribution version (boo#1227350)
Obsoletes:      openssh-server-config-rootlogin <= %{version}
%endif
%sysusers_requires

%description server
SSH (Secure Shell) is a program for logging into and executing commands
on a remote machine. It replaces rsh (rlogin and rsh) and
provides secure encrypted communication between two untrusted
hosts over an insecure network.

xorg-x11 (X Window System) connections and arbitrary TCP/IP ports can
also be forwarded over the secure channel.

This package contains the Secure Shell daemon, which allows clients to
securely connect to your server.

%if %{with allow_root_password_login_by_default}
%package server-config-disallow-rootlogin
Summary:        Config to disallow password root logins to sshd
Group:          Productivity/Networking/SSH
Requires:       %{name}-server = %{version}-%{release}
Conflicts:      %{name}-server-config-rootlogin

%description server-config-disallow-rootlogin
The openssh-server package by default allows password based
root logins. This package provides a config that disallows root
to log in using the passwor. It's useful to secure your system
preventing password attacks on the root account over ssh.
%else

%package server-config-rootlogin
Summary:        Config to permit root logins to sshd
Group:          Productivity/Networking/SSH
Requires:       %{name}-server = %{version}-%{release}
Conflicts:      %{name}-server-config-disallow-rootlogin

%description server-config-rootlogin
The openssh-server package by default disallows password based
root logins. This package provides a config that does. It's useful
to temporarily have a password based login to be able to use
ssh-copy-id(1).
%endif

%package clients
Summary:        SSH (Secure Shell) client applications
Group:          Productivity/Networking/SSH
%if %{with crypto_policies}
Requires:       crypto-policies >= 20220824
%endif
Requires:       %{name}-common = %{version}-%{release}
Provides:       openssh:%{_bindir}/ssh

%description clients
SSH (Secure Shell) is a program for logging into and executing commands
on a remote machine. It replaces rsh (rlogin and rsh) and
provides secure encrypted communication between two untrusted
hosts over an insecure network.

xorg-x11 (X Window System) connections and arbitrary TCP/IP ports can
also be forwarded over the secure channel.

This package contains clients for making secure connections to Secure
Shell servers.

%if %{with ldap}
%package helpers
Summary:        OpenSSH AuthorizedKeysCommand helpers
Group:          Productivity/Networking/SSH
Requires:       %{name}-common = %{version}-%{release}

%description helpers
SSH (Secure Shell) is a program for logging into and executing commands
on a remote machine. It replaces rsh (rlogin and rsh) and
provides secure encrypted communication between two untrusted
hosts over an insecure network.

xorg-x11 (X Window System) connections and arbitrary TCP/IP ports can
also be forwarded over the secure channel.

This package contains helper applications for OpenSSH which retrieve
keys from various sources.
%endif

%package cavs
Summary:        OpenSSH FIPS crypto module CAVS tests
Group:          Productivity/Networking/SSH
Requires:       %{name}-common = %{version}-%{release}

%description cavs
This package contains the FIPS-140 CAVS (Cryptographic Algorithm
Validation Program/Suite) related tests of OpenSSH.

%prep
%setup -q -n "%{name}-%{wrongly_named_version}"
cp %{SOURCE3} %{SOURCE4} %{SOURCE11} .

%autopatch -p1

# set libexec dir in the LDAP patch
sed -i.libexec 's,@LIBEXECDIR@,%{_libexecdir}/ssh,' \
    $( grep -Rl @LIBEXECDIR@ \
        $( grep "^+++" %{PATCH31} | sed -r 's@^.+/([^/\t ]+).*$@\1@' )
    )

%build
%if 0%{?suse_version} < 1600
export CC=gcc-11
%endif
autoreconf -fiv
%ifarch s390 s390x %{sparc}
PIEFLAGS="-fPIE"
%else
PIEFLAGS="-fpie"
%endif
CFLAGS="%{optflags} $PIEFLAGS -fstack-protector"
CXXFLAGS="%{optflags} $PIEFLAGS -fstack-protector"
LDFLAGS="-pie -Wl,--as-needed"
#CPPFLAGS="%%{optflags} -DUSE_INTERNAL_B64"
export LDFLAGS CFLAGS CXXFLAGS CPPFLAGS
%configure \
    --sysconfdir=%{_sysconfdir}/ssh \
    --libexecdir=%{_libexecdir}/ssh \
    --with-selinux \
    --with-pid-dir=/run \
    --with-systemd \
    --with-ssl-engine \
    --with-pam \
    --with-kerberos5=%{_prefix} \
    --with-privsep-path=%{_localstatedir}/lib/empty \
%if %{sandbox_seccomp}
    --with-sandbox=seccomp_filter \
%else
%if %{sandbox_rlimit}
    --with-sandbox=rlimit \
%endif
%endif
    --disable-strip \
    --with-audit=linux \
%if %{with ldap}
    --with-ldap \
%endif
    --with-xauth=%{_bindir}/xauth \
    --with-libedit \
%if %{with wtmpdb}
    --with-wtmpdb \
%endif
%if 0%{?suse_version} >= 1550
    --disable-lastlog \
%endif
    --with-logind \
    --with-security-key-builtin \
    --target=%{_target_cpu}-suse-linux

%make_build
%sysusers_generate_pre %{SOURCE14} sshd sshd.conf

%install
%make_install
%if %{defined _distconfdir}
install -d -m 755 %{buildroot}%{_pam_vendordir}
install -m 644 %{SOURCE2} %{buildroot}%{_pam_vendordir}/sshd
%else
# SLE has no distconfdir, so use sle PAM config
install -d -m 755 %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE15} %{buildroot}%{_sysconfdir}/pam.d/sshd
%endif
install -d -m 755 %{buildroot}%{_localstatedir}/lib/sshd
install -d -m 755 %{buildroot}%{_sysconfdir}/ssh/ssh_config.d
install -d -m 755 %{buildroot}%{_sysconfdir}/ssh/sshd_config.d
%if 0%{?suse_version} < 1600
install -d -m 755 %{buildroot}%{_sysconfdir}/slp.reg.d/
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/slp.reg.d/
%endif
install -D -m 0644 %{SOURCE10} %{buildroot}%{_unitdir}/sshd.service
install -D -m 0644 %{SOURCE16} %{buildroot}%{_unitdir}/sshd@.service
install -D -m 0644 %{SOURCE17} %{buildroot}%{_unitdir}/sshd.socket
%if 0%{?suse_version} < 1600
ln -s service %{buildroot}%{_sbindir}/rcsshd
%endif
install -d -m 755 %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE8} %{buildroot}%{_fillupdir}
# install shell script to automate the process of adding your public key to a remote machine
install -m 755 contrib/ssh-copy-id %{buildroot}%{_bindir}
install -m 644 contrib/ssh-copy-id.1 %{buildroot}%{_mandir}/man1
sed -i -e s@%{_prefix}/libexec@%{_libexecdir}@g %{buildroot}%{_sysconfdir}/ssh/sshd_config

%if %{with allow_root_password_login_by_default}
echo "PermitRootLogin prohibit-password" > %{buildroot}%{_sysconfdir}/ssh/sshd_config.d/51-permit-root-login.conf
%else
echo "PermitRootLogin yes" > %{buildroot}%{_sysconfdir}/ssh/sshd_config.d/50-permit-root-login.conf
%endif

# Move /etc to /usr/etc/ssh
%if %{defined _distconfdir}
mkdir -p %{buildroot}%{_distconfdir}/ssh/ssh{,d}_config.d
mv %{buildroot}%{_sysconfdir}/ssh/moduli %{buildroot}%{_distconfdir}/ssh/
mv %{buildroot}%{_sysconfdir}/ssh/ssh_config %{buildroot}%{_distconfdir}/ssh/
mv %{buildroot}%{_sysconfdir}/ssh/sshd_config %{buildroot}%{_distconfdir}/ssh/
%if %{with allow_root_password_login_by_default}
mv %{buildroot}%{_sysconfdir}/ssh/sshd_config.d/51-permit-root-login.conf %{buildroot}%{_distconfdir}/ssh/sshd_config.d/51-permit-root-login.conf
%else
mv %{buildroot}%{_sysconfdir}/ssh/sshd_config.d/50-permit-root-login.conf %{buildroot}%{_distconfdir}/ssh/sshd_config.d/50-permit-root-login.conf
%endif
%endif

%if %{with crypto_policies}
install -m 644 ssh_config_suse %{buildroot}%{_sysconfdir}/ssh/ssh_config.d/50-suse.conf
%if %{defined _distconfdir}
install -m 644 sshd_config_suse_cp %{buildroot}%{_distconfdir}/ssh/sshd_config.d/40-suse-crypto-policies.conf
%else
install -m 644 sshd_config_suse_cp %{buildroot}%{_sysconfdir}/ssh/sshd_config.d/40-suse-crypto-policies.conf
%endif
%endif

%if 0%{?suse_version} < 1550
# install firewall definitions
mkdir -p %{buildroot}%{_fwdefdir}
install -m 644 %{SOURCE7} %{buildroot}%{_fwdefdir}/sshd
%endif

# askpass wrapper
sed -e "s,@LIBEXECDIR@,%{_libexecdir},g" < %{SOURCE6} > %{buildroot}%{_libexecdir}/ssh/ssh-askpass
sed -e "s,@LIBEXECDIR@,%{_libexecdir},g" < %{SOURCE12} > %{buildroot}%{_libexecdir}/ssh/cavs_driver-ssh.pl
rm -f %{buildroot}%{_datadir}/Ssh.bin
# sshd keys generator wrapper
install -D -m 0755 %{SOURCE9} %{buildroot}%{_sbindir}/sshd-gen-keys-start

# Install sysusers.d config for sshd user
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE14} %{buildroot}%{_sysusersdir}/sshd.conf

# the hmac hashes - taken from openssl
#
# re-define the __os_install_post macro: the macro strips
# the binaries and thereby invalidates any hashes created earlier.
#
# this shows up earlier because otherwise the %%expand of
# the macro is too late.
%if %{with openssl11}
%define opensslbin openssl-1_1
%else
%define opensslbin openssl
%endif

%{expand:%%global __os_install_post {%__os_install_post
for b in \
        %{_bindir}/ssh \
        %{_sbindir}/sshd \
        %{_libexecdir}/ssh/sftp-server \
        ; do
    %{opensslbin} dgst -sha256 -binary -hmac %{CHECKSUM_HMAC_KEY} < %{buildroot}$b > %{buildroot}$b%{CHECKSUM_SUFFIX}
done

}}

%pre server -f sshd.pre
%if %{defined _distconfdir}
# Prepare for migration to /usr/etc.
test -f /etc/pam.d/sshd.rpmsave && mv -v /etc/pam.d/sshd.rpmsave /etc/pam.d/sshd.rpmsave.old ||:
test -f /etc/ssh/sshd_config.rpmsave && mv -v /etc/ssh/sshd_config.rpmsave /etc/ssh/sshd_config.rpmsave.old ||:
%endif

%service_add_pre sshd.service sshd.socket

%post server
%{fillup_only -n ssh}
%service_add_post sshd.service sshd.socket

%if %{with crypto_policies}
%if ! %{defined _distconfdir}
test -f /etc/ssh/sshd_config && (grep -q "^Include /etc/ssh/sshd_config\.d/\*\.conf" /etc/ssh/sshd_config || ( \
    echo "WARNING: /etc/ssh/sshd_config doesn't include config files from"
    echo " /etc/ssh/sshd_config.d/ . The crypto-policies configuration won't"
    echo "be honored until the following line is added at the start of"
    echo "/etc/ssh/sshd_config :"
    echo "Include /etc/ssh/sshd_config.d/*.conf" ) ) ||:
%endif
%endif

%preun server
%service_del_preun sshd.service sshd.socket

%postun server
%service_del_postun sshd.service sshd.socket

%if %{with crypto_policies}
%if ! %{defined _distconfdir}
%post server-config-disallow-rootlogin
test -f /etc/ssh/sshd_config && (grep -q "^Include /etc/ssh/sshd_config\.d/\*\.conf" /etc/ssh/sshd_config || ( \
    echo "WARNING: /etc/ssh/sshd_config doesn't include config files from"
    echo " /etc/ssh/sshd_config.d/ . The config file installed by"
    echo "openssh-server-config-disallow-rootlogin won't be used until"
    echo "the following line is added at the start of /etc/ssh/sshd_config :"
    echo "Include /etc/ssh/sshd_config.d/*.conf" ) ) ||:
%endif
%endif

%if %{defined _distconfdir}
%posttrans server
# Migration to /usr/etc.
test -f /etc/pam.d/sshd.rpmsave && mv -v /etc/pam.d/sshd.rpmsave /etc/pam.d/sshd ||:
test -f /etc/ssh/sshd_config.rpmsave && mv -v /etc/ssh/sshd_config.rpmsave /etc/ssh/sshd_config ||:
%endif

%if %{defined _distconfdir}
%pre clients
# Prepare for migration to /usr/etc.
test -f /etc/ssh/ssh_config.rpmsave && mv -v /etc/ssh/ssh_config.rpmsave /etc/ssh/ssh_config.rpmsave.old ||:
%endif

%if %{with crypto_policies}
%if ! %{defined _distconfdir}
%post clients
test -f /etc/ssh/ssh_config && (grep -q "^Include /etc/ssh/ssh_config\.d/\*\.conf" /etc/ssh/ssh_config || ( \
    echo "WARNING: /etc/ssh/ssh_config doesn't include config files from"
    echo " /etc/ssh/ssh_config.d/ . The crypto-policies configuration won't"
    echo "be honored until the following line is added at the start of"
    echo "/etc/ssh/ssh_config :"
    echo "Include /etc/ssh/ssh_config.d/*.conf" ) ) ||:
%endif
%endif

%if %{defined _distconfdir}
%posttrans clients
# Migration to /usr/etc.
test -f /etc/ssh/ssh_config.rpmsave && mv -v /etc/ssh/ssh_config.rpmsave /etc/ssh/ssh_config ||:
%endif

%files
# openssh is an empty package that depends on -clients and -server,
# resulting in a clean upgrade path from prior to the split even when
# recommends are disabled.

%files common
%license LICENCE
%doc README.SUSE README.kerberos README.FIPS ChangeLog OVERVIEW README TODO CREDITS
%attr(0755,root,root) %dir %{_sysconfdir}/ssh
%if %{defined _distconfdir}
%attr(0755,root,root) %dir %{_distconfdir}/ssh
%attr(0600,root,root) %{_distconfdir}/ssh/moduli
%attr(0755,root,root) %dir %{_distconfdir}/ssh/ssh_config.d
%else
%attr(0755,root,root) %dir %{_sysconfdir}/ssh
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/ssh/moduli
%attr(0755,root,root) %dir %{_sysconfdir}/ssh/ssh_config.d
%endif
%attr(0444,root,root) %{_mandir}/man1/ssh-keygen.1*
%attr(0444,root,root) %{_mandir}/man5/moduli.5*
%attr(0755,root,root) %{_bindir}/ssh-keygen*

%files server
%attr(0755,root,root) %{_sbindir}/sshd
%attr(0444,root,root) %{_sbindir}/sshd%{CHECKSUM_SUFFIX}
%if 0%{?suse_version} < 1600
%attr(0755,root,root) %{_sbindir}/rcsshd
%endif
%attr(0755,root,root) %{_sbindir}/sshd-gen-keys-start
%dir %attr(0755,root,root) %{_localstatedir}/lib/sshd
%dir %attr(0755,root,root) %{_sysconfdir}/ssh/sshd_config.d
%if %{defined _distconfdir}
%attr(0755,root,root) %dir %{_distconfdir}/ssh
%attr(0755,root,root) %dir %{_distconfdir}/ssh/sshd_config.d
%attr(0640,root,root) %config(noreplace) %{_distconfdir}/ssh/sshd_config
%attr(0644,root,root) %{_pam_vendordir}/sshd
%else
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/ssh/sshd_config
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/sshd
%endif
%if %{with crypto_policies}
%if %{defined _distconfdir}
%attr(0600,root,root) %config(noreplace) %{_distconfdir}/ssh/sshd_config.d/40-suse-crypto-policies.conf
%else
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/ssh/sshd_config.d/40-suse-crypto-policies.conf
%endif
%endif
%attr(0644,root,root) %{_unitdir}/sshd.service
%attr(0644,root,root) %{_unitdir}/sshd@.service
%attr(0644,root,root) %{_unitdir}/sshd.socket
%attr(0644,root,root) %{_sysusersdir}/sshd.conf
%attr(0444,root,root) %{_mandir}/man5/sshd_config*
%attr(0444,root,root) %{_mandir}/man8/sftp-server.8*
%attr(0444,root,root) %{_mandir}/man8/sshd.8*
%attr(0755,root,root) %{_libexecdir}/ssh/sftp-server
%attr(0444,root,root) %{_libexecdir}/ssh/sftp-server%{CHECKSUM_SUFFIX}
%attr(0755,root,root) %{_libexecdir}/ssh/sshd-session
%attr(0755,root,root) %{_libexecdir}/ssh/sshd-auth
%if 0%{?suse_version} < 1600
%dir %{_sysconfdir}/slp.reg.d
%config %{_sysconfdir}/slp.reg.d/ssh.reg
%endif
%{_fillupdir}/sysconfig.ssh
%if 0%{?suse_version} < 1550
%dir %{_fwdir}
%dir %{_fwdefdir}
%config %{_fwdefdir}/sshd
%endif

%if %{with allow_root_password_login_by_default}
%files server-config-disallow-rootlogin
%if %{defined _distconfdir}
%{_distconfdir}/ssh/sshd_config.d/51-permit-root-login.conf
%else
%config(noreplace) %{_sysconfdir}/ssh/sshd_config.d/51-permit-root-login.conf
%endif
%else

%files server-config-rootlogin
%if %{defined _distconfdir}
%{_distconfdir}/ssh/sshd_config.d/50-permit-root-login.conf
%else
%config(noreplace) %{_sysconfdir}/ssh/sshd_config.d/50-permit-root-login.conf
%endif
%endif

%files clients
%if %{with crypto_policies}
%dir %attr(0755,root,root) %{_sysconfdir}/ssh/ssh_config.d
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ssh/ssh_config.d/50-suse.conf
%endif
%if %{defined _distconfdir}
%attr(0644,root,root) %{_distconfdir}/ssh/ssh_config
%else
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ssh/ssh_config
%endif
%attr(0755,root,root) %{_bindir}/ssh
%attr(0444,root,root) %{_bindir}/ssh%{CHECKSUM_SUFFIX}
%attr(0755,root,root) %{_bindir}/scp*
%attr(0755,root,root) %{_bindir}/sftp*
%attr(0755,root,root) %{_bindir}/ssh-add*
%attr(0755,root,root) %{_bindir}/ssh-agent*
%attr(0755,root,root) %{_bindir}/ssh-copy-id*
%attr(0755,root,root) %{_bindir}/ssh-keyscan*
%attr(0755,root,root) %dir %{_libexecdir}/ssh
%attr(0755,root,root) %{_libexecdir}/ssh/ssh-askpass*
%attr(0755,root,root) %{_libexecdir}/ssh/ssh-keysign*
%attr(0755,root,root) %{_libexecdir}/ssh/ssh-pkcs11-helper*
%attr(0755,root,root) %{_libexecdir}/ssh/ssh-sk-helper*
%attr(0444,root,root) %{_mandir}/man1/scp.1*
%attr(0444,root,root) %{_mandir}/man1/sftp.1*
%attr(0444,root,root) %{_mandir}/man1/ssh-add.1*
%attr(0444,root,root) %{_mandir}/man1/ssh-agent.1*
%attr(0444,root,root) %{_mandir}/man1/ssh-keyscan.1*
%attr(0444,root,root) %{_mandir}/man1/ssh.1*
%attr(0444,root,root) %{_mandir}/man1/ssh-copy-id.1*
%attr(0444,root,root) %{_mandir}/man5/ssh_config.5*
%attr(0444,root,root) %{_mandir}/man8/ssh-pkcs11-helper.8*
%attr(0444,root,root) %{_mandir}/man8/ssh-sk-helper.8*
%attr(0444,root,root) %{_mandir}/man8/ssh-keysign.8*

%if %{with ldap}
%files helpers
%attr(0755,root,root) %dir %{_sysconfdir}/ssh
%verify(not mode) %attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ssh/ldap.conf
%attr(0755,root,root) %dir %{_libexecdir}/ssh
%attr(0755,root,root) %{_libexecdir}/ssh/ssh-ldap*
%attr(0444,root,root) %{_mandir}/man5/ssh-ldap*
%attr(0444,root,root) %{_mandir}/man8/ssh-ldap*
%doc HOWTO.ldap-keys openssh-lpk-openldap.schema openssh-lpk-sun.schema
%endif

%files cavs
%attr(0755,root,root) %{_libexecdir}/ssh/cavs*

%changelog
