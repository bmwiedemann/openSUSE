#
# spec file for package pcr-oracle
#
# Copyright (c) 2025 SUSE LLC
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
# needssslcertforbuild


Name:           pcr-oracle
Version:        0.5.4
Release:        0
Summary:        Predict TPM PCR values
License:        GPL-2.0-or-later
Group:          System/Boot
URL:            https://github.com/okirch/pcr-oracle
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM fix_efi_measure_and_shim.patch gh#okirch/pcr-oracle!47
# PATCH-FIX-UPSTREAM fix_efi_measure_and_shim.patch gh#okirch/pcr-oracle!51
Patch0:         fix_efi_measure_and_shim.patch
# PATCH-FIX-UPSTREAM fix_loader_conf.patch gh#okirch/pcr-oracle!50
Patch1:         fix_loader_conf.patch
# PATCH-FIX-UPSTREAM fix_grub_bls_entry.patch gh#okirch/pcr-oracle!52
Patch2:         fix_grub_bls_entry.patch
# PATCH-FIX-UPSTREAM fix_grub_bls_cmdline.patch gh#okirch/pcr-oracle!52 (cont)
Patch3:         fix_grub_bls_cmdline.patch
# PATCH-FIX-UPSTREAM support-ecc-srk.patch gh#okirch/pcr-oracle!56
Patch4:         support-ecc-srk.patch
# PATCH-FIX-UPSTREAM fix-testcase-empty-efi-variables.patch gh#okirch/pcr-oracle!58
Patch5:         fix-testcase-empty-efi-variables.patch
# PATCH-FIX-UPSTREAM fix-event-reshash-for-cryptouuid.patch gh#okirch/pcr-oracle!60
Patch6:         fix-event-reshash-for-cryptouuid.patch
BuildRequires:  libopenssl-devel >= 0.9.8
BuildRequires:  tpm2-0-tss-devel >= 2.4.0
Requires:       libtss2-tcti-device0
ExclusiveArch:  x86_64 aarch64 ppc64le riscv64

%description
This utility tries to predict the values of the TPM's Platform
Configuration Registers following an update of system components
like shim, grub, etc.

%prep
%autosetup -p1

%build
# beware, this is not autoconf
./configure --prefix /usr
make CCOPT="%optflags"

%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}/%{_bindir}
mv %{buildroot}/bin/pcr-oracle %{buildroot}/%{_bindir}
rmdir %{buildroot}/bin

%files
%defattr(-,root,root)
%doc README.md
%doc test-authorized.sh
%{_bindir}/pcr-oracle
%{_mandir}/man8/pcr-oracle.8*

%changelog
