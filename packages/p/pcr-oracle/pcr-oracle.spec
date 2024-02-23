#
# spec file for package pcr-oracle
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
# needssslcertforbuild


Name:           pcr-oracle
Version:        0.5.4
Release:        0
Summary:        Predict TPM PCR values
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://github.com/okirch/pcr-oracle
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM fix_efi_measure.patch gh#okirch/pcr-oracle!47
Patch0:         fix_efi_measure.patch
# PATCH-FIX-UPSTREAM fix_loader_conf.patch gh#okirch/pcr-oracle!50
Patch1:         fix_loader_conf.patch
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
