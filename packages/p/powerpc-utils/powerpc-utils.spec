#
# spec file for package powerpc-utils
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


Name:           powerpc-utils
Version:        1.3.12
Release:        0
Summary:        Utilities for PowerPC Hardware
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/ibm-power-utilities/powerpc-utils
Source0:        https://github.com/ibm-power-utilities/powerpc-utils/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        nvsetenv
Patch1:         powerpc-utils-lsprop.patch
Patch2:         ofpathname_powernv.patch
Patch3:         fix_kexec_service_name_for_suse.patch
Patch4:         libvirt-service-dep.patch
Patch5:         0001-drmgr-Return-from-get_node_by_name-if-matched-DRC-in.patch
Patch6:         0006-drmgr-Free-nodes-returned-from-configure_connector.patch
Patch7:         0005-ofpathname-skip-devices-with-no-devspec-when-coorela.patch
Patch8:         ppc64_cpu-Support-partial-SMT-level-through-SYS-FS-s.patch
Patch9:         ppc64_cpu-Clean-up-sysfs-smt-control-error-handling.patch
Patch10:        0002-lparstat-Fix-Idle-and-busy-PURR-SPURR.patch
Patch11:        0003-lparstat-app-Use-pic-value-at-boot-for-accurate-boot.patch
Patch12:        0004-lparstat-Use-CLOCK_BOOTTIME-for-get_time-interface-a.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libnuma-devel
BuildRequires:  librtas-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(zlib)
Requires:       bc
Requires:       coreutils
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       kmod-compat
Requires:       systemd-sysvinit
Requires:       udev
Requires:       util-linux
Recommends:     powerpc-utils-python
ExclusiveArch:  ppc ppc64 ppc64le
%{?systemd_requires}

%description
The powerpc-utils package provides a set of tools and utilities and
utilities for maintaining and enabling certain features of Linux on Power.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -fvi
%configure \
    --disable-silent-rules \
    --with-systemd=%{_unitdir}
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
%make_install \
    rasdir=%{_sbindir} \
    mandir=%{_mandir}
%if 0%{?suse_version} < 1550
mkdir %{buildroot}/sbin
ln -sf %{_sbindir}/lsprop %{buildroot}/sbin/lsprop
%endif
install -m 755 %{SOURCE1} %{buildroot}%{_sbindir}/nvsetenv
ln -sf serv_config %{buildroot}%{_sbindir}/uspchrp
ln -sf %{_mandir}/man8/serv_config.8 %{buildroot}%{_mandir}/man8/uspchrp.8
ln -sf drmgr %{buildroot}%{_sbindir}/drslot_chrp_slot
ln -sf drmgr %{buildroot}%{_sbindir}/drslot_chrp_pci
ln -sf drmgr %{buildroot}%{_sbindir}/drslot_chrp_cpu
ln -sf drmgr %{buildroot}%{_sbindir}/drslot_chrp_phb
ln -sf drmgr %{buildroot}%{_sbindir}/drslot_chrp_mem
ln -sf drmgr %{buildroot}%{_sbindir}/drslot_chrp_hea
ln -sf drmgr %{buildroot}%{_sbindir}/drmig_chrp_pmig

ln -s service %{buildroot}%{_sbindir}/rcsmt_off

# remove docu installed by make_install as we hand-install them in %%files
rm -rf %{buildroot}%{_docdir}/%{name}/*

%pre
%service_add_pre hcn-init-wicked.service hcn-init-NetworkManager.service smt_off.service smtstate.service

%post
%service_add_post hcn-init-wicked.service hcn-init-NetworkManager.service smt_off.service smtstate.service

%preun
%service_del_preun hcn-init-wicked.service hcn-init-NetworkManager.service smt_off.service smtstate.service

%postun
%service_del_postun hcn-init-wicked.service hcn-init-NetworkManager.service smt_off.service smtstate.service

%files
%license COPYING
%doc README Changelog
%{_mandir}/man*/*
%{_sbindir}/*
%{_bindir}/*
%if 0%{?suse_version} < 1550
/sbin/lsprop
%endif
%dir %{_localstatedir}/lib/powerpc-utils
%config(noreplace) %{_localstatedir}/lib/powerpc-utils/smt.state
%dir /usr/lib/powerpc-utils
/usr/lib/powerpc-utils/functions.suse
%{_unitdir}/hcn-init-wicked.service
%{_unitdir}/hcn-init-NetworkManager.service
%{_unitdir}/smt_off.service
%{_unitdir}/smtstate.service

%changelog
