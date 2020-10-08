#
# spec file for package gnu-efi
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


Name:           gnu-efi
Version:        3.0.12
Release:        0
Summary:        Library for EFI Applications
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Development/Libraries/Other
URL:            http://sourceforge.net/projects/gnu-efi
Source:         http://sourceforge.net/projects/gnu-efi/files/gnu-efi-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
BuildRequires:  kernel-source
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  ia64 %ix86 x86_64 aarch64 %arm

%description
Library to develop EFI applications for IA-64 (IPF), IA-32 (x86), x86_64,
ARM-32, and ARM-64 platforms using the GNU toolchain and the EFI development
environment.

%prep
%setup -q

%build
##########################
## DO NOT ADD RPM OPT FLAGS! THIS DOES NOT BUILD AGAINST GLIBC
##
##########################
make %{?_smp_mflags} LINUX_HEADERS=%{_prefix}/src/linux

%install
make install INSTALLROOT=%{buildroot} LIBDIR=%{_libdir} PREFIX=%{_prefix}
%if 0
mkdir %{buildroot}%{_libdir}/%{name}
cp -p apps/*.efi %{buildroot}%{_libdir}/%{name}
%endif

%files
%doc README.*
%{_includedir}/efi
%{_libdir}/crt0-efi-*.o
%{_libdir}/elf_*_efi.lds
%{_libdir}/libefi.a
%{_libdir}/libgnuefi.a
%if 0
%{_libdir}/%{name}
%endif

%changelog
