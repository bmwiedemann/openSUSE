#
# spec file for package autofs
#
# Copyright (c) 2026 SUSE LLC
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


%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if 0%{?suse_version} >= 1230
%define with_udisks 1
%else
%define with_udisks 0
%endif
%if 0%{?suse_version} >= 1230
%define with_sssd 1
%else
%define with_sssd 0
%endif
Name:           autofs
Version:        5.1.9
Release:        0
Summary:        A Kernel-Based Automounter
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://www.kernel.org/pub/linux/daemons/autofs/v5/
Source:         https://www.kernel.org/pub/linux/daemons/autofs/v5/%{name}-%{version}.tar.xz
Source1:        sysconfig.autofs
Source3:        autofs.schema
Source4:        README.SUSE.ldap
Source5:        README.SUSE
Source7:        NetworkManager-autofs
Source8:        get-upstream-patches
Source9:        https://www.kernel.org/pub/linux/daemons/autofs/v5/%{name}-%{version}.tar.sign
Source10:       autofs.keyring
Source42:       org.freedesktop.AutoMount.conf
# PATCH-FIX-OPENSUSE autofs-suse-auto_master_default.patch
Patch100:       autofs-5.1.1-suse-auto_master_default.patch
# PATCH-FIX-OPENSUSE autofs-debuginfo-fix.patch
Patch101:       autofs-5.1.1-debuginfo-fix.patch
# PATCH-EXTEND-OPENSUSE autofs-dbus-udisks-monitor.patch
Patch102:       autofs-5.1.1-dbus-udisks-monitor.patch
# bsc#1175238 - Use /usr/etc/nsswitch.conf if /etc/nsswitch.conf is not available
Patch106:       autofs-nsswitch-usr-etc.patch
# bsc#1207881 - Obsolete and incorrect manual page details for autofs(8)
Patch108:       autofs-suse-manpage-remove-initdir.patch
# bsc#1221682 - GCC 14: autofs package fails
Patch109:       autofs-5.1.9-fix-ldap_parse_page_control-check.patch
Patch110:       autofs-5.1.9-Fix-incompatible-function-pointer-types.patch
# bsc#1246325 - fix map entry removal regression. queued for upstream.
Patch111:       0001-autofs-5.1.9-fix-get-parent-multi-mount-check-in-try.patch
Patch112:       0002-autofs-5.1.9-fix-deadlock-in-remount.patch
Patch113:       0003-CHANGELOG-add-a-few-missing-entries.patch
Patch114:       0004-autofs-5.1.9-quiet-possibly-noisy-log-message.patch
Patch115:       0005-autofs-5.1.9-fix-devid-update-on-reload.patch
Patch116:       0006-autofs-5.1.9-fix-cache-writelock-must-be-taken-in-up.patch
Patch117:       0007-autofs-5.1.9-fix-skip-valid-map-entries-on-expire-cl.patch
Patch118:       0008-autofs-5.1.9-remove-unnecessary-call-to-set_direct_m.patch
Patch119:       0009-autofs-5.1.9-remove-unnecessary-assignment-in-umount.patch
Patch120:       0010-autofs-5.1.9-fix-direct-mount-trigger-umount-failure.patch
Patch121:       0011-autofs-5.1.9-refactor-do_umount_autofs_direct.patch
Patch122:       0012-autofs-5.1.9-fix-stale-direct-mount-trigger-not-umou.patch
Patch123:       0013-autofs-5.1.9-add-function-table_lookup_ino.patch
Patch124:       0014-autofs-5.1.9-improve-handling-of-missing-map-entry-f.patch
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
BuildRequires:  dbus-1-devel
BuildRequires:  e2fsprogs
BuildRequires:  flex
BuildRequires:  krb5-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libxml2-devel
BuildRequires:  module-init-tools
BuildRequires:  nfs-client
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  pkgconfig(libsystemd)
Requires(pre):  %fillup_prereq
Requires(pre):  aaa_base
Recommends:     nfs-client
%{?systemd_ordering}
%if %{with_sssd}
BuildRequires:  sssd
%endif
%if %{with_udisks}
BuildRequires:  pkgconfig(udisks2)
%endif

%description
AutoFS is a kernel-based automounter for Linux.  It automatically
mounts filesystems when you use them, and unmounts them later when
you are not using them.  This can include network filesystems, CD-ROMs,
floppies, and so forth.

%prep
%autosetup -p1
cp %{SOURCE3} .
cp %{SOURCE4} .
cp %{SOURCE5} .

%build
autoreconf -fiv

SUSE_ASNEEDED=0
%configure %{_target_cpu}-suse-linux \
            --libdir=%{_libdir} --mandir=%{_mandir} \
            --with-confdir=%{_sysconfdir}/sysconfig \
            --disable-mount-locking \
            --enable-forced-shutdown \
            --enable-ignore-busy \
            --with-systemd \
            --with-libtirpc \
            --with-hesiod=no \
            --with-sasl
%make_build all DONTSTRIP=1 LOCAL_CFLAGS="%{optflags} %(getconf LFS_CFLAGS)" \
	%{?_smp_mflags}

%install
%make_install INSTALLROOT=%{buildroot} install_samples
install -d -m 755 %{buildroot}%{_sysconfdir}/auto.master.d
install -D -m 644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.autofs
install -D -m 755 %{SOURCE7} %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d/autofs
%if %{with_udisks}
install -D -m 644 %{SOURCE42} %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.AutoMount.conf
%endif
# will be installed by fillup scripts
rm -f %{buildroot}%{_sysconfdir}/sysconfig/autofs

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%fillup_only

%preun
%{stop_on_removal autofs}
%service_del_preun %{name}.service
%fillup_only

%postun
%service_del_postun %{name}.service

%files
%license COPYRIGHT
%{_fillupdir}/sysconfig.autofs
%config(noreplace) %{_sysconfdir}/autofs.conf
%config(noreplace) %{_sysconfdir}/auto.master
%config(noreplace) %{_sysconfdir}/auto.misc
%config(noreplace) %{_sysconfdir}/auto.net
%config(noreplace) %{_sysconfdir}/auto.smb
%config(noreplace) %{_sysconfdir}/autofs_ldap_auth.conf
%if %{with_udisks}
%{_datadir}/dbus-1/system.d/org.freedesktop.AutoMount.conf
%endif
%dir %{_sysconfdir}/auto.master.d
%dir %{_prefix}/lib/NetworkManager
%dir %{_prefix}/lib/NetworkManager/dispatcher.d
%attr(0755,root,root) %{_prefix}/lib/NetworkManager/dispatcher.d/autofs
%doc README README.changer README.ncpfs README.replicated-server
%doc README.smbfs README.v5.release autofs.schema README.active-restart
%doc README.SUSE README.SUSE.ldap
%dir %{_libdir}/autofs/
%{_libdir}/libautofs.so
%{_libdir}/autofs/
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_sbindir}/automount
%{_unitdir}/autofs.service

%changelog
