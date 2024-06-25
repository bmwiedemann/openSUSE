#
# spec file for package tboot
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


Name:           tboot
%define ver 1.11.4
Version:        20210614_%{ver}
Release:        0
Summary:        Program for performing a verified launch using Intel TXT
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://sourceforge.net/projects/tboot/
Source0:        https://downloads.sourceforge.net/project/tboot/tboot/tboot-%{ver}.tar.gz
Source1:        tboot.rpmlintrc
Patch3:         tboot-grub2-fix-menu-in-xen-host-server.patch
Patch4:         tboot-grub2-fix-xen-submenu-name.patch
Patch7:         tboot-distributor.patch
Patch8:         tboot-grub2-refuse-secure-boot.patch
Patch9:         tboot-bsc#1207833-copy-mbi.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%if 0%{?suse_version} > 1320
BuildRequires:  update-bootloader-rpm-macros
%endif

%if 0%{?update_bootloader_requires:1}
%update_bootloader_requires
%else
Requires:       perl-Bootloader
%endif

%description
Trusted Boot (tboot) is a pre-kernel/VMM module that uses Intel
Trusted Execution Technology (Intel(R) TXT) to perform a measured and
verified launch of an OS kernel/VMM.

%prep
%setup -q -n %name-%ver
%autopatch -p1

%build
# Tumbleweed now uses -flto=3 by default which gives us trouble with the
# statically linked C and assembler code in tboot. Better to be conservative
# here since tboot is low level stuff -> disable LTO for us (boo#1141323).
%define _lto_cflags %{nil}
export TBOOT_CFLAGS="$CFLAGS"
make debug=y %{?_smp_mflags}

%install
make debug=y install DISTDIR="%{buildroot}" MANPATH="%{buildroot}/%{_mandir}"

%files
%defattr(-,root,root,-)
%doc README.md COPYING docs/* lcptools-v2/lcptools.txt
%{_sbindir}/txt-acminfo
%{_sbindir}/txt-parse_err
%{_sbindir}/tb_polgen
%{_sbindir}/txt-stat
%{_sbindir}/lcp2_crtpol
%{_sbindir}/lcp2_crtpolelt
%{_sbindir}/lcp2_crtpollist
%{_sbindir}/lcp2_mlehash
/boot/tboot.gz
/boot/tboot-syms
%{_mandir}/man8/*
%dir %{_sysconfdir}/grub.d/
%config(noreplace) %{_sysconfdir}/grub.d/20_linux_tboot
%config(noreplace) %{_sysconfdir}/grub.d/20_linux_xen_tboot

%post
%if 0%{?update_bootloader_check_type_reinit_post:1}
%update_bootloader_check_type_reinit_post grub2 grub2-efi
%else
/sbin/update-bootloader --reinit || true
%endif

%postun
%if 0%{?update_bootloader_check_type_reinit_post:1}
# there is no clean solution for refresh during package removal at the moment.
# %%posttrans is not executed during package removal.
%update_bootloader_check_type_reinit_post grub2 grub2-efi
%update_bootloader_posttrans
%else
/sbin/update-bootloader --reinit || true
%endif

%posttrans
%{?update_bootloader_posttrans}

%changelog
