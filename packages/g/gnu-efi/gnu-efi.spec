#
# spec file for package gnu-efi
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


Name:           gnu-efi
Version:        4.0.0
Release:        0
Summary:        Library for EFI Applications
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Development/Libraries/Other
URL:            https://github.com/ncroxon/gnu-efi
Source0:        https://github.com/ncroxon/gnu-efi/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  kernel-source
ExclusiveArch:  ia64 %{ix86} x86_64 aarch64 %{arm} riscv64

%description
Library to develop EFI applications for IA-64 (IPF), IA-32 (x86), x86_64,
ARM-32, and ARM-64 platforms using the GNU toolchain and the EFI development
environment.

%package devel
Summary:        Development files for gnu-efi
Group:          Development/Libraries/Other
Provides:       gnu-efi = %{version}-%{release}
Obsoletes:      gnu-efi < %{version}-%{release}

%description devel
A package containing the development files for gnu-efi,
which is used for developing EFI applications using the GNU toolchain

%package apps
Summary:        Example and test files for gnu-efi
Group:          Development/Tools/Other

%description apps
A package containing the example and UEFI testing files created by gnu-efi


%prep
%autosetup -p1

%build
# DO NOT ADD RPM OPTFLAGS! UEFI is freestanding only!!
%make_build LINUX_HEADERS=%{_prefix}/src/linux LIBDIR=%{_libdir} PREFIX=%{_prefix}

%install
%make_install INSTALLROOT=%{buildroot} LIBDIR=%{_libdir} PREFIX=%{_prefix}

%files devel
%{_includedir}/efi
%{_libdir}/crt0-efi-*.o
%{_libdir}/elf_*_efi.lds
%ifarch %{ix86} riscv64 aarch64
%{_libdir}/elf_*_efi_local.lds
%endif
%{_libdir}/libefi.a
%{_libdir}/libgnuefi.a
%{_libdir}/pkgconfig/%{name}.pc

%files apps
%doc README.md SECURITY.md docs/*
%license LICENSE licenses/*
%{_libdir}/gnuefi

%changelog
