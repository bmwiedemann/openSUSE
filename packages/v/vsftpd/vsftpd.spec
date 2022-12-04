#
# spec file for package vsftpd
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


%if 0%{?suse_version} > 1210
%global with_systemd  1
%else
%global with_systemd  0
%endif
%if 0%{?suse_version} >= 1500
%define use_firewalld 1
%else
%define use_firewalld 0
%endif
Name:           vsftpd
Version:        3.0.5
Release:        0
Summary:        Very Secure FTP Daemon - Written from Scratch
License:        SUSE-GPL-2.0-with-openssl-exception
Group:          Productivity/Networking/Ftp/Servers
URL:            https://security.appspot.com/vsftpd.html
Source0:        https://security.appspot.com/downloads/%{name}-%{version}.tar.gz
Source1:        %{name}.pam
Source2:        %{name}.logrotate
Source3:        %{name}.init
Source4:        README.SUSE
Source6:        %{name}.firewall
Source7:        vsftpd.service
Source8:        vsftpd@.service
Source9:        %{name}.keyring
Source10:       vsftpd.socket
Source11:       %{name}.firewalld
Source1000:     https://security.appspot.com/downloads/%{name}-%{version}.tar.gz.asc
Patch1:         vsftpd-2.0.4-lib64.diff
Patch3:         vsftpd-2.0.4-xinetd.diff
Patch4:         vsftpd-2.0.4-enable-ssl.patch
Patch5:         vsftpd-2.0.4-dmapi.patch
Patch6:         vsftpd-2.0.5-vuser.patch
Patch7:         vsftpd-2.0.5-enable-debuginfo.patch
Patch8:         vsftpd-2.0.5-utf8-log-names.patch
Patch9:         vsftpd-2.3.5-conf.patch
Patch10:        vsftpd-3.0.0_gnu_source_defines.patch
Patch11:        vsftpd-3.0.0-optional-seccomp.patch
#PATCH-FIX-OPENSUSE: bnc#786024, second issue with pam_login_acct
Patch13:        vsftpd-drop-newpid-from-clone.patch
#PATCH-FIX-OPENSUSE: bnc#812406
Patch14:        vsftpd-enable-fcntl-f_setfl.patch
#PATCH-FIX-OPENSUSE: bnc#812406
Patch15:        vsftpd-enable-dev-log-sendto.patch
#PATCH-FEATURE-SUSE: FATE#311051, call chroot with user credentials to enable nsf with squash_root option
Patch16:        vsftpd-root-squashed-chroot.patch
#PATCH-FIX-UPSTREAM: bnc#870122
Patch17:        vsftpd-enable-gettimeofday-sec.patch
#PATCH-FIX-UPSTREAM: bnc#890469 fix broken syscall on s390
Patch18:        vsftpd-3.0.2-s390.patch
#PATCH-FIX-UPSTREAM: bnc#900326 deny_file filtering acts weirdly (19-22)
Patch19:        vsftpd-2.1.0-filter.patch
Patch20:        vsftpd-2.2.0-wildchar.patch
Patch21:        vsftpd-2.3.4-sqb.patch
Patch22:        vsftpd-path-normalize.patch
Patch23:        vsftpd-ls-memleak.patch
#PATCH-FIX-UPSTREAM: bnc#970982
Patch24:        vsftpd-3.0.2-wnohang.patch
Patch25:        vsftpd-3.0.2-fix-chown-uploads.patch
#FIX-FIX-OPENSUSE: bsc#1042673
Patch26:        vsftpd-3.0.3-build-with-openssl-1.1.patch
Patch27:        vsftpd-mdtm-in-utc.patch
Patch28:        vsftpd-die-with-session.patch
Patch29:        vsftpd-append-seek-pipe.patch
Patch30:        vsftpd-3.0.3-address_space_limit.patch
Patch31:        vsftpd-enable-syscalls-needed-by-sle15.patch
Patch32:        vsftpd-support-dsa-only-setups.patch
Patch33:        vsftpd-avoid-bogus-ssl-write.patch
Patch35:        0001-When-handling-FEAT-command-check-ssl_tlsv1_1-and-ssl.patch
# PATCH-FIX-UPSTREAM https://bugzilla.suse.com/show_bug.cgi?id=1179553
Patch36:        seccomp-fixes.patch
Patch37:        vsftpd-openlog-force.patch
Patch38:        vsftpd-seccomp-getrandom.patch
Patch39:        vsftpd-seccomp-ssl.patch
Patch40:        vsftpd-seccomp-wait4.patch
Patch41:        revert-undocumented-config-file-format-changes.patch
Patch42:        use-system-wide-tls-cipher-policy.patch
Patch43:        vsftpd-allow-dev-log-socket.patch
Patch44:        vsftpd-enable-sendto-for-prelogin-syslog.patch
Patch45:        disable-tls13-to-support-older-openssl-versions.patch
BuildRequires:  libcap-devel
%if 0%{?suse_version} == 1315
BuildRequires:  libopenssl-1_1-devel >= 1.1.1
%else
%if 0%{?sle_version} == 150000
BuildRequires:  libopenssl-1_1-devel >= 1.1.0
%else
BuildRequires:  libopenssl-devel >= 1.1.1
%endif
%endif
BuildRequires:  pam-devel
Requires:       logrotate
Requires(pre):  shadow
Provides:       ftp-server
%if %{use_firewalld}
BuildRequires:  firewall-macros
%endif
%if 0%{?suse_version} >= 1330
Requires:       group(nobody)
Requires:       user(ftp)
Requires(pre):  group(nobody)
%endif
%if %{with_systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%else
Requires(post): %insserv_prereq
%endif

%description
Vsftpd is an FTP server, or daemon. The "vs" stands for Very Secure.
Obviously this is not a guarantee, but the entire codebase was written
with security in mind, and carefully designed to be resilient to
attack.

Recent evidence suggests that vsftpd is also extremely fast (and this
is before any explicit performance tuning!). In tests against wu-ftpd,
vsftpd was always faster, supporting over twice as many users in some
tests.

%prep
%setup -q
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1

%if 0%{?sle_version} == 150000
%patch45 -p1
%endif

%build
%define seccomp_opts -D_GNU_SOURCE -DUSE_SECCOMP
rm dummyinc/sys/capability.h vsf_findlibs.sh
make CFLAGS="%{optflags} -DOPENSSL_NO_SSL_INTERN -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -fPIE -fstack-protector --param=ssp-buffer-size=4 %{seccomp_opts}" \
     LIBS="-lpam -lcap -lssl -lcrypto"

%install
mkdir -p %{buildroot}%{_datadir}/empty
cp %{SOURCE4} .
install -D -m 755 %{name}  %{buildroot}%{_sbindir}/%{name}
install -D -m 600 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
%if 0%{?suse_version} < 1330
install -D -m 600 xinetd.d/%{name} %{buildroot}%{_sysconfdir}/xinetd.d/%{name}
%endif
install -D -m 644 $RPM_SOURCE_DIR/%{name}.pam %{buildroot}%{_sysconfdir}/pam.d/%{name}
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
install -D -m 644 $RPM_SOURCE_DIR/%{name}.logrotate %{buildroot}%{_distconfdir}/logrotate.d/%{name}
%else
install -D -m 644 $RPM_SOURCE_DIR/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%endif
install -D -m 644 %{name}.conf.5 %{buildroot}/%{_mandir}/man5/%{name}.conf.5
install -D -m 644 %{name}.8 %{buildroot}/%{_mandir}/man8/%{name}.8
%if %{with_systemd}
ln -sf service %{buildroot}/%{_sbindir}/rc%{name}
install -D -m 0644 %{SOURCE7} %{buildroot}/%{_unitdir}/%{name}.service
%if 0%{?sle_version} && 0%{?sle_version} < 150300
sed -r -i '/^(Protect(Home|Hostname|KernelLogs|Clock|KernelTunables|KernelModules|ControlGroups)|RestrictRealtime|PrivateMounts)=/d' %{buildroot}/%{_unitdir}/%{name}.service
%endif
install -D -m 0644 %{SOURCE8} %{buildroot}/%{_unitdir}/%{name}@.service
install -D -m 0644 %{SOURCE10} %{buildroot}/%{_unitdir}/%{name}.socket
%else
install -D -m 755 %{SOURCE3} %{buildroot}%{_initddir}/%{name}
ln -sf %{_initddir}/%{name} %{buildroot}/%{_sbindir}/rc%{name}
%endif
# install firewall information file
%if %{use_firewalld}
install -D -m 644 %{SOURCE11} %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml
%else
install -d %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}
%endif

%pre
getent passwd ftpsecure >/dev/null || useradd -r -g nobody -s /bin/false -c "Secure FTP User" -d %{_localstatedir}/lib/empty ftpsecure
%if %{with_systemd}
%service_add_pre %{name}.service %{name}.socket
%endif
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/%{name} ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/%{name} ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%preun
%if %{with_systemd}
%service_del_preun %{name}.service %{name}.socket
%else
%stop_on_removal %{name}
%endif

%post
%if %{with_systemd}
%service_add_post %{name}.service %{name}.socket
%else
%insserv_cleanup
%restart_on_update %{name}
%endif
%if %{use_firewalld}
%{firewalld_reload}
%endif

%postun
%if %{with_systemd}
%service_del_postun %{name}.service %{name}.socket
%else
%insserv_cleanup
%restart_on_update %{name}
%endif

%files
%if %{with_systemd}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_unitdir}/%{name}@.service
%else
%{_initddir}/%{name}
%endif
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%dir %{_datadir}/empty
%if 0%{?suse_version} < 1330
%config(noreplace) %{_sysconfdir}/xinetd.d/%{name}
%endif
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config %{_sysconfdir}/pam.d/%{name}
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/%{name}
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%endif
%{_mandir}/man5/%{name}.conf.*
%{_mandir}/man8/%{name}.*
%license LICENSE
%doc BUGS AUDIT Changelog README README.security
%license COPYING
%doc REWARD SPEED TODO SECURITY TUNING SIZE FAQ EXAMPLE
%doc README.SUSE
%if %{use_firewalld}
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/%{name}.xml
%else
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}
%endif

%changelog
