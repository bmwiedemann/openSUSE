#
# spec file for package autofs
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
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
URL:            http://www.kernel.org/pub/linux/daemons/autofs/v5/
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
BuildRequires:  dbus-1-devel
BuildRequires:  e2fsprogs
BuildRequires:  flex
BuildRequires:  krb5-devel
BuildRequires:  libnsl-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libxml2-devel
BuildRequires:  module-init-tools
BuildRequires:  nfs-client
BuildRequires:  openldap2-devel
BuildRequires:  pkg-config
%if 0%{?suse_version} >= 1330
BuildRequires:  rpcgen
%endif
BuildRequires:  xz
%if %{with_sssd}
BuildRequires:  sssd
%endif
%if %{with_udisks}
BuildRequires:  pkgconfig(udisks2)
%endif
BuildRequires:  pkgconfig(libsystemd)
Version:        5.1.7
Release:        0
Summary:        A Kernel-Based Automounter
License:        GPL-2.0-or-later
Group:          System/Daemons
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
# PATCH-FIX-OPENSUSE autofs-use-libldap_r-instead-of-libldap-for-thread-safety.patch [bsc#955477]
Patch104:       autofs-use-libldap_r-instead-of-libldap-for-thread-safety.patch
# PATCH-FIX-OPENSUSE autofs-5-1-3-fix-unset-tsd-group-name-handling.patch
Patch105:       autofs-5-1-3-fix-unset-tsd-group-name-handling.patch
# bsc#1175238 - Use /usr/etc/nsswitch.conf if /etc/nsswitch.conf is not available
Patch106:       autofs-nsswitch-usr-etc.patch
Patch107:       autofs-5.1.7-Fix-option-for-master_read_wait.patch
Requires(pre):  %fillup_prereq
Requires(pre):  aaa_base
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}
Recommends:     nfs-client

%description
AutoFS is a kernel-based automounter for Linux.  It automatically
mounts filesystems when you use them, and unmounts them later when
you are not using them.  This can include network filesystems, CD-ROMs,
floppies, and so forth.

%prep
%setup -q
cp %{SOURCE3} .
cp %{SOURCE4} .
cp %{SOURCE5} .
#
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1

%build
autoreconf -fiv

SUSE_ASNEEDED=0
%configure %{_target_cpu}-suse-linux \
            --libdir=%{_libdir} --mandir=%{_mandir} \
            --with-confdir=/etc/sysconfig \
            --disable-mount-locking \
            --enable-forced-shutdown \
            --enable-ignore-busy \
            --with-systemd \
            --with-libtirpc \
            --with-hesiod=no \
            --with-sasl
make all DONTSTRIP=1 LOCAL_CFLAGS="%{optflags} %(getconf LFS_CFLAGS)" \
	%{?_smp_mflags}

%install
%make_install INSTALLROOT=%{buildroot} install_samples
install -d -m 755 %{buildroot}%{_sysconfdir}/auto.master.d
install -D -m 644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.autofs
install -D -m 755 %{SOURCE7} %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/autofs
ln -s %{_mandir}/man8/autofs.8.gz %{buildroot}/%{_mandir}/man8/rcautofs.8.gz
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcautofs
%if %{with_udisks}
install -D -m 644 %{SOURCE42} %{buildroot}%{_sysconfdir}/dbus-1/system.d/org.freedesktop.AutoMount.conf
%endif
# will be installed by fillup scripts
rm -f %{buildroot}%{_sysconfdir}/sysconfig/autofs

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%{fillup_only}

%preun
%{stop_on_removal autofs}
%service_del_preun %{name}.service
%{fillup_only}

%postun
%service_del_postun %{name}.service

%files
%defattr (-, root, root)
%license COPYRIGHT
%{_fillupdir}/sysconfig.autofs
%config(noreplace) %{_sysconfdir}/autofs.conf
%config(noreplace) %{_sysconfdir}/auto.master
%config(noreplace) %{_sysconfdir}/auto.misc
%config(noreplace) %{_sysconfdir}/auto.net
%config(noreplace) %{_sysconfdir}/auto.smb
%config(noreplace) %{_sysconfdir}/autofs_ldap_auth.conf
%if %{with_udisks}
%config %{_sysconfdir}/dbus-1/system.d/org.freedesktop.AutoMount.conf
%endif
%dir %{_sysconfdir}/auto.master.d
%dir %{_sysconfdir}/NetworkManager
%dir %{_sysconfdir}/NetworkManager/dispatcher.d
%{_sysconfdir}/NetworkManager/dispatcher.d/autofs
%doc README README.changer README.ncpfs README.replicated-server
%doc README.smbfs README.v5.release autofs.schema README.active-restart
%doc README.SUSE README.SUSE.ldap
%dir %{_libdir}/autofs/
%{_libdir}/libautofs.so
%{_libdir}/autofs/
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_sbindir}/automount
%{_sbindir}/rcautofs
%{_unitdir}/autofs.service

%changelog
