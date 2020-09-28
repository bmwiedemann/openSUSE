#
# spec file for package openssh
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
%ifnarch ppc
%define sandbox_seccomp 1
%endif
%if 0%{?suse_version} >= 1500
%bcond_without tirpc
%else
%bcond_with tirpc
%endif
%define _fwdir      %{_sysconfdir}/sysconfig/SuSEfirewall2.d
%define _fwdefdir   %{_fwdir}/services
%define _appdefdir  %( grep "configdirspec=" $( which xmkmf ) | sed -r 's,^[^=]+=.*-I(.*)/config.*$,\\1/app-defaults,' )
%define CHECKSUM_SUFFIX .hmac
%define CHECKSUM_HMAC_KEY "HMAC_KEY:OpenSSH-FIPS@SLE"
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           openssh
Version:        8.3p1
Release:        0
Summary:        Secure Shell Client and Server (Remote Login Program)
License:        BSD-2-Clause AND MIT
Group:          Productivity/Networking/SSH
URL:            https://www.openssh.com/
Source0:        http://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz
Source1:        http://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz.asc
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
Patch0:         openssh-7.7p1-allow_root_password_login.patch
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
BuildRequires:  audit-devel
BuildRequires:  autoconf
BuildRequires:  groff
BuildRequires:  libedit-devel
BuildRequires:  libselinux-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libfido2)
BuildRequires:  pkgconfig(libsystemd)
Requires(post): %fillup_prereq
Requires(pre):  shadow
Recommends:     %{name}-helpers = %{version}-%{release}
Recommends:     audit
Conflicts:      %{name}-fips < %{version}-%{release}
Conflicts:      %{name}-fips > %{version}-%{release}
Conflicts:      nonfreessh
%{?systemd_requires}
%if %{with tirpc}
BuildRequires:  libtirpc-devel
%endif
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(krb5)
%else
BuildRequires:  krb5-mini-devel
%endif

%description
SSH (Secure Shell) is a program for logging into and executing commands
on a remote machine. It is intended to replace rsh (rlogin and rsh) and
provides openssl (secure encrypted communication) between two untrusted
hosts over an insecure network.

xorg-x11 (X Window System) connections and arbitrary TCP/IP ports can
also be forwarded over the secure channel.

%package helpers
Summary:        OpenSSH AuthorizedKeysCommand helpers
Group:          Productivity/Networking/SSH
Requires:       %{name} = %{version}-%{release}

%description helpers
Helper applications for OpenSSH which retrieve keys from various sources.

%package fips
Summary:        OpenSSH FIPS cryptomodule HMACs
Group:          Productivity/Networking/SSH
Requires:       %{name} = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
Conflicts:      %{name} > %{version}-%{release}
Obsoletes:      %{name}-hmac

%description fips
Hashes that together with the main package form the FIPS certifiable
cryptomodule.

%package cavs
Summary:        OpenSSH FIPS cryptomodule CAVS tests
Group:          Productivity/Networking/SSH
Requires:       %{name} = %{version}-%{release}

%description cavs
FIPS140 CAVS tests related parts of the OpenSSH package

%prep
%setup -q
cp %{SOURCE3} %{SOURCE4} %{SOURCE11} .

%autopatch -p1

# set libexec dir in the LDAP patch
sed -i.libexec 's,@LIBEXECDIR@,%{_libexecdir}/ssh,' \
    $( grep -Rl @LIBEXECDIR@ \
        $( grep "^+++" openssh-7.7p1-ldap.patch | sed -r 's@^.+/([^/\t ]+).*$@\1@' )
    )

%build
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
    --with-sandbox=rlimit \
%endif
    --disable-strip \
    --with-audit=linux \
    --with-ldap \
    --with-xauth=%{_bindir}/xauth \
    --with-libedit \
    --with-security-key-builtin \
    --target=%{_target_cpu}-suse-linux

%make_build

%install
%make_install

install -d -m 755 %{buildroot}%{_sysconfdir}/pam.d
install -d -m 755 %{buildroot}%{_localstatedir}/lib/sshd
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/sshd
install -d -m 755 %{buildroot}%{_sysconfdir}/slp.reg.d/
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/slp.reg.d/
install -D -m 0644 %{SOURCE10} %{buildroot}%{_unitdir}/sshd.service
ln -s service %{buildroot}%{_sbindir}/rcsshd
install -d -m 755 %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE8} %{buildroot}%{_fillupdir}
# install shell script to automate the process of adding your public key to a remote machine
install -m 755 contrib/ssh-copy-id %{buildroot}%{_bindir}
install -m 644 contrib/ssh-copy-id.1 %{buildroot}%{_mandir}/man1
sed -i -e s@%{_prefix}/libexec@%{_libexecdir}@g %{buildroot}%{_sysconfdir}/ssh/sshd_config

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

# the hmac hashes - taken from openssl
#
# re-define the __os_install_post macro: the macro strips
# the binaries and thereby invalidates any hashes created earlier.
#
# this shows up earlier because otherwise the %%expand of
# the macro is too late.
%{expand:%%global __os_install_post {%__os_install_post
for b in \
        %{_bindir}/ssh \
        %{_sbindir}/sshd \
        %{_libexecdir}/ssh/sftp-server \
        ; do
    openssl dgst -sha256 -binary -hmac %{CHECKSUM_HMAC_KEY} < %{buildroot}$b > %{buildroot}$b%{CHECKSUM_SUFFIX}
done

}}

%pre
getent group sshd >/dev/null || %{_sbindir}/groupadd -r sshd
getent passwd sshd >/dev/null || %{_sbindir}/useradd -r -g sshd -d %{_localstatedir}/lib/sshd -s /bin/false -c "SSH daemon" sshd
%service_add_pre sshd.service

%post
%{fillup_only -n ssh sshd}
%service_add_post sshd.service
%set_permissions %{_sysconfdir}/ssh/sshd_config

%preun
%service_del_preun sshd.service

%postun
# The openssh-fips trigger script for openssh will normally restart sshd once
# it gets installed, so only restart the service here is openssh-fips is not
# present
rpm -q openssh-fips >& /dev/null && DISABLE_RESTART_ON_UPDATE=yes
%service_del_postun sshd.service

%triggerin -n openssh-fips -- %{name} = %{version}-%{release}
%restart_on_update sshd

%verifyscript
%verify_permissions -e %{_sysconfdir}/ssh/sshd_config

%files
%exclude %{_bindir}/ssh%{CHECKSUM_SUFFIX}
%exclude %{_sbindir}/sshd%{CHECKSUM_SUFFIX}
%exclude %{_libexecdir}/ssh/sftp-server%{CHECKSUM_SUFFIX}
%exclude %{_libexecdir}/ssh/cavs*
%dir %attr(755,root,root) %{_localstatedir}/lib/sshd
%license LICENCE
%doc README.SUSE README.kerberos README.FIPS ChangeLog OVERVIEW README TODO CREDITS
%attr(0755,root,root) %dir %{_sysconfdir}/ssh
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/ssh/moduli
%verify(not mode) %attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ssh/ssh_config
%verify(not mode) %attr(0600,root,root) %config(noreplace) %{_sysconfdir}/ssh/sshd_config
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/sshd
%attr(0644,root,root) %{_unitdir}/sshd.service
%attr(0755,root,root) %{_bindir}/*
%attr(0755,root,root) %{_sbindir}/*
%attr(0755,root,root) %dir %{_libexecdir}/ssh
%exclude %{_libexecdir}/ssh/ssh-ldap*
%attr(0755,root,root) %{_libexecdir}/ssh/*
%attr(0444,root,root) %{_mandir}/man1/*
%attr(0444,root,root) %{_mandir}/man5/*
%attr(0444,root,root) %{_mandir}/man8/*
%exclude %{_mandir}/man5/ssh-ldap*
%exclude %{_mandir}/man8/ssh-ldap*
%dir %{_sysconfdir}/slp.reg.d
%config %{_sysconfdir}/slp.reg.d/ssh.reg
%{_fillupdir}/sysconfig.ssh
%if 0%{?suse_version} < 1550
%dir %{_fwdir}
%dir %{_fwdefdir}
%config %{_fwdefdir}/sshd
%endif

%files helpers
%attr(0755,root,root) %dir %{_sysconfdir}/ssh
%verify(not mode) %attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ssh/ldap.conf
%attr(0755,root,root) %dir %{_libexecdir}/ssh
%attr(0755,root,root) %{_libexecdir}/ssh/ssh-ldap*
%attr(0444,root,root) %{_mandir}/man5/ssh-ldap*
%attr(0444,root,root) %{_mandir}/man8/ssh-ldap*
%doc HOWTO.ldap-keys openssh-lpk-openldap.schema openssh-lpk-sun.schema

%files fips
%attr(0444,root,root) %{_bindir}/ssh%{CHECKSUM_SUFFIX}
%attr(0444,root,root) %{_sbindir}/sshd%{CHECKSUM_SUFFIX}
%attr(0444,root,root) %{_libexecdir}/ssh/sftp-server%{CHECKSUM_SUFFIX}

%files cavs
%attr(0755,root,root) %{_libexecdir}/ssh/cavs*

%changelog
