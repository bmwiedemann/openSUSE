#
# spec file for package limine
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Marvin Friedrich
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

Name:           limine
Version:        10.8.0
Release:        0
Summary:        Modern, advanced, portable, multiprotocol bootloader and boot manager
License:        BSD-2-Clause
Group:          System/Boot
URL:            https://codeberg.org/limine/limine
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  nasm
BuildRequires:  mtools
BuildRequires:  clang
BuildRequires:  lld
BuildRequires:  llvm
ExclusiveArch:  x86_64 riscv64 aarch64 loongarch64

%description
Limine is a modern, advanced, portable, multiprotocol bootloader and boot manager,
also used as the reference implementation for the Limine boot protocol.

%prep
%setup -q

%build
%configure --enable-all --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install

%files
%{_bindir}/limine
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/BOOTAA64.EFI
%{_datadir}/%{name}/BOOTIA32.EFI
%{_datadir}/%{name}/BOOTLOONGARCH64.EFI
%{_datadir}/%{name}/BOOTRISCV64.EFI
%{_datadir}/%{name}/BOOTX64.EFI
%{_datadir}/%{name}/limine-bios-cd.bin
%{_datadir}/%{name}/limine-bios-pxe.bin
%{_datadir}/%{name}/limine-bios.sys
%{_datadir}/%{name}/limine-uefi-cd.bin
%{_mandir}/man1/limine.1.gz
%doc %{_docdir}/%{name}

%changelog
