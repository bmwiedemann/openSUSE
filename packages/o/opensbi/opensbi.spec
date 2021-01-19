#
# spec file for package opensbi
#
# Copyright (c) 2021 SUSE LLC
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


%define target @BUILD_FLAVOR@%{nil}

%if "%{target}" == ""
Name:           opensbi
%else
Name:           opensbi-%{target}
%endif
Version:        0.9
Release:        0
Summary:        RISC-V Open Source Supervisor Binary Interface
License:        BSD-2-Clause
Group:          System/Boot
URL:            https://github.com/riscv/opensbi
Source:         https://github.com/riscv/opensbi/archive/v%{version}.tar.gz#/opensbi-%{version}.tar.gz
ExclusiveArch:  riscv64

%description
The RISC-V Supervisor Binary Interface (SBI) is the recommended interface
between:

1. A platform-specific firmware running in M-mode and a bootloader, a
hypervisor or a general-purpose OS executing in S-mode or HS-mode.
2. A hypervisor running in HS-mode and a bootloader or a general-purpose
OS executing in VS-mode.

The RISC-V SBI specification is maintained as an independent project by
the RISC-V Foundation on Github (https://github.com/riscv/riscv-sbi-doc).

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++

%description devel
The RISC-V Supervisor Binary Interface (SBI) is the recommended interface
between:

1. A platform-specific firmware running in M-mode and a bootloader, a
hypervisor or a general-purpose OS executing in S-mode or HS-mode.
2. A hypervisor running in HS-mode and a bootloader or a general-purpose
OS executing in VS-mode.

The RISC-V SBI specification is maintained as an independent project by
the RISC-V Foundation on Github (https://github.com/riscv/riscv-sbi-doc).

This package provides the development files for %{name}.

%prep
%setup -q -n opensbi-%{version}

%build
%if "%{target}" == ""
%make_build PLATFORM=generic
%endif
%if "%{target}" == "sifivefu540"
%make_build PLATFORM=sifive/fu540
%endif

%install
%if "%{target}" == ""
make install I=%{buildroot}%{_prefix} INSTALL_LIB_PATH=%{_lib}
install -D -m 644 build/platform/generic/firmware/fw_dynamic.bin %{buildroot}%{_datadir}/opensbi/opensbi.bin
%endif
%if "%{target}" == "sifivefu540"
install -D -m 644 build/platform/sifive/fu540/firmware/fw_dynamic.bin %{buildroot}%{_datadir}/opensbi/opensbi-sifive-fu540.bin
%endif

%files
%{_datadir}/opensbi

%if "%{target}" == ""
%files devel
%{_includedir}/*
%{_libdir}/*
%endif

%changelog
