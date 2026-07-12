#
# spec file for package powerpc-utils
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.3.14
Release:        0
Summary:        Utilities for PowerPC Hardware
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/ibm-power-utilities/powerpc-utils
Source0:        https://github.com/ibm-power-utilities/powerpc-utils/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        nvsetenv
Patch1:         0001-drmgr-Update-cpuless_lmb_count-NUMA-counter-during-L.patch
Patch2:         0002-drmgr-Remove-only-available-LMBs-from-CPU-less-NUMA-.patch
Patch3:         0003-drmgr-Move-numa_topology-code-to-common_numa.c.patch
Patch4:         0004-drmgr-Move-read-lmb-size-property-code-to-common_ofd.patch
Patch5:         0005-drmgr-Add-get_next_cpu-to-identify-the-removable-CPU.patch
Patch6:         0006-drmgr-Allocate-CPU-bitmap-for-each-NUMA-node.patch
Patch7:         0007-drmgr-Add-NUMA-configuration-update-for-CPU-remove.patch
Patch8:         0008-drmgr-Add-NUMA-based-CPU-removal.patch
Patch9:         0009-drmgr-Allow-signals-mentioned-in-new-sigset_t.patch
Patch10:        0010-drmgr-Add-timeout-signal-handling-for-NUMA-memory-RE.patch
Patch11:        0011-drmgr-Do-not-remove-LMBs-when-the-timer-expires.patch
Patch12:        bootlist-set-ethernet-using-open-firmware-path-as-bo.patch
Patch13:        ppc64_cpu-bring-power-mode-reporting-inline-with-PAP.patch
Patch41:        powerpc-utils-lsprop.patch
Patch42:        ofpathname_powernv.patch
Patch43:        fix_kexec_service_name_for_suse.patch
Patch44:        libvirt-service-dep.patch
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
%if 0%{?suse_version} < 1550
Requires:       systemd-sysvinit
%endif
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
ln -s service %{buildroot}%{_sbindir}/rcsmt_off
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
