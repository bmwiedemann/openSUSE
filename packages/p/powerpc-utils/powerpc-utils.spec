#
# spec file for package powerpc-utils
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


Name:           powerpc-utils
Version:        1.3.9
Release:        0
Summary:        Utilities for PowerPC Hardware
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/ibm-power-utilities/powerpc-utils
Source0:        https://github.com/ibm-power-utilities/powerpc-utils/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        nvsetenv
Patch1:         powerpc-utils-lsprop.patch
Patch2:         ofpathname_powernv.patch
Patch4:         libvirt-service-dep.patch
Patch5:         lsdevinfo-optimize-criteria-filtering.patch
Patch6:         hcnmgr-Avoid-hexdum-squeezing-consecutive-identical-.patch
Patch7:         0001-hcnmgr-Support-vNIC-as-backup-device.patch
Patch8:         0002-hcnmgr-Remove-some-dead-code.patch
Patch9:         0003-ofpathname-Fix-nvme-support-in-ANA-mode.patch
Patch10:        0004-ofpathname-Add-support-for-NVMf-devices.patch
Patch11:        lparstat-Fix-reported-online-memory-in-legacy-format.patch
Patch12:        errinjct-sanitize-devspec-output-of-a-newline-if-one.patch
Patch14:        fix_kexec_service_name_for_suse.patch
Patch15:        0001-Validate-connection-manager.patch
Patch16:        0002-factor-out-NetworkManager-nmcli-code.patch
Patch17:        0003-Add-new-wicked-functions-from-suse-to-manage-bonding.patch
Patch18:        0004-Support-wicked-HNV-using-new-wicked-interfaces-for.patch
Patch19:        0005-Set-modprobe-bonding-max_bonds-0-option.patch
Patch20:        0006-cleanup-hcnmgr-distro-and-service-detection.patch
Patch21:        0007-Remove-wicked-ifup-calls-that-just-run-into-timeouts.patch
Patch22:        0008-add-note-about-comma-in-hcnmgr-BONDOPTIONS.patch
Patch23:        0009-Fix-to-call-wicked-ifreload-directly.patch
Patch24:        0010-Fix-incorrect-parameters-to-suse_ifcfg_bond_create.patch
Patch25:        0011-Fix-comment-about-setting-primary.patch
Patch26:        0012-Description-and-indenting-corrections.patch
Patch27:        0013-adjust-sourcing-path-of-the-functions.suse-library.patch
Patch28:        0014-Enable-the-network-service-checks.patch
Patch29:        0015-add-hcn-init.service.suse-service-covering-wicked.patch
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
%if !0%{?usrmerged}
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

install -m 644 systemd/hcn-init.service.suse %{buildroot}%{_unitdir}/hcn-init.service
mkdir -p %{buildroot}/usr/lib/powerpc-utils
install -m 644 scripts/functions.suse  %{buildroot}/usr/lib/powerpc-utils/functions.suse

# remove docu installed by make_install as we hand-install them in %%files
rm -rf %{buildroot}%{_docdir}/%{name}/*

%pre
%service_add_pre hcn-init.service smt_off.service smtstate.service

%post
%service_add_post hcn-init.service smt_off.service smtstate.service

%preun
%service_del_preun hcn-init.service smt_off.service smtstate.service

%postun
%service_del_postun hcn-init.service smt_off.service smtstate.service

%files
%license COPYING
%doc README Changelog
%{_mandir}/man*/*
%{_sbindir}/*
%{_bindir}/*
%if !0%{?usrmerged}
/sbin/lsprop
%endif
%dir %{_localstatedir}/lib/powerpc-utils
%ghost %{_localstatedir}/lib/powerpc-utils/smt.state
%dir /usr/lib/powerpc-utils
/usr/lib/powerpc-utils/functions.suse
%{_unitdir}/hcn-init.service
%{_unitdir}/smt_off.service
%{_unitdir}/smtstate.service

%changelog
