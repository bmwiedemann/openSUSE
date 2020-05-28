#
# spec file for package powerpc-utils
#
# Copyright (c) 2020 SUSE LLC
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


%define realversion 1.3.7

Name:           powerpc-utils
Version:        %{realversion}.1
Release:        0
Summary:        Utilities for PowerPC Hardware
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/ibm-power-utilities/powerpc-utils
Source0:        https://github.com/ibm-power-utilities/powerpc-utils/archive/v%{realversion}.tar.gz#/%{name}-%{realversion}.tar.gz
Source1:        nvsetenv
Patch1:         powerpc-utils-lsprop.patch
Patch2:         ofpathname_powernv.patch
Patch3:         systemd-dir.patch
Patch4:         libvirt-service-dep.patch
# This adds field in the middle of tool output so revert it again in < 15.1
Patch5:         Revert-lparstat-Show-available-physical-processors-i.patch
Patch6:         bug-1158312-parse-ibm-drc-info-property.patch
Patch7:         0001-powerpc-utils-Suppress-errors-reading-kernel-files.patch
Patch9:         bsc1164726-search-only-part-of-sys.patch
Patch10:        bsc1171892-get-rid-of-trainling-NUL.patch
Patch11:        Fix-ofpathname-Could-not-retrieve-logical-device-nam.patch
Patch12:        ofpathname-Fix-udevadm-location.patch
BuildRequires:  autoconf
BuildRequires:  automake
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
%setup -q -n %{name}-%{realversion}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%if 0%{?sle_version} <= 120400 || 0%{?sle_version} == 150000
%patch5 -p1
%endif
%patch6 -p1
%patch7 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
autoreconf -fvi
%configure \
    --disable-silent-rules \
    --with-systemd=%{buildroot}%{_unitdir}
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
%make_install \
    rasdir=%{_sbindir} \
    mandir=%{_mandir}
mkdir %{buildroot}/sbin
ln -sf %{_sbindir}/lsprop %{buildroot}/sbin/lsprop
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

# remove docu installed by make_install as we hand-install them in %files
rm -rf %{buildroot}%{_docdir}/%{name}/*

%pre
%service_add_pre smt_off.service

%post
%service_add_post smt_off.service

%preun
%service_del_preun smt_off.service

%postun
%service_del_postun smt_off.service

%files
%license COPYING
%doc README Changelog
%{_mandir}/man*/*
%{_sbindir}/*
%{_bindir}/*
/sbin/lsprop
%attr(644, -, -) %{_unitdir}/smt_off.service

%changelog
