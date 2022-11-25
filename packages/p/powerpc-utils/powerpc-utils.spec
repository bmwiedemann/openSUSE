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
Version:        1.3.10
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
Patch5:         lsslot-Explicity-declare-that-lmb_address-be-display.patch
Patch6:         lsslot-Fix-lsslot-c-mem-output-when-using-4GB-LMB-si.patch
Patch7:         bootlist-Add-install-boot-support-for-nvmf-devices.patch
Patch8:         ofpathname-Fix-several-issues-in-nvmf-boot-install-s.patch
Patch9:         ofpathname-Handle-nsid-as-hex-in-nvmf-boot-install-s.patch
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
%config(noreplace) %{_localstatedir}/lib/powerpc-utils/smt.state
%dir /usr/lib/powerpc-utils
/usr/lib/powerpc-utils/functions.suse
%{_unitdir}/hcn-init.service
%{_unitdir}/smt_off.service
%{_unitdir}/smtstate.service

%changelog
