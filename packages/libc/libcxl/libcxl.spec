#
# spec file for package libcxl
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


Name:           libcxl
Version:        1.7
Release:        0
%define soversion 1
Summary:        Coherent accelerator interface
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/ibm-capi/libcxl
Source:         %{name}-%{version}.tar.gz
Patch1:         remove_2_backslashes_in_shell_call.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  glibc
ExclusiveArch:  ppc64 ppc64le

%description
Coherent accelerator interface (refer to lib package with soversion)

%package -n %{name}%{soversion}
Summary:        Coherent accelerator shared library
Group:          System/Libraries

%description -n %{name}%{soversion}
The coherent accelerator interface is designed to allow the coherent
connection of accelerators (FPGAs and other devices) to a POWER system.
Coherent in this context means that the accelerator and CPUs can both access
system memory directly and with the same effective addresses. IBM refers to
this as the Coherent Accelerator Processor Interface (CAPI). In the Linux
world, it is referred to by the name CXL to avoid confusion with the ISDN
CAPI subsystem.

The Linux kernel interacts with the device POWER Service Layer (PSL).
Userland interacts with the device Accelerator Function Unit (AFU). See the
Linux kernel source file Documentation/powerpc/cxl.txt for a detailed
description of the coherent accelerator interface.

The CXL library provides a userland API to coherently attached devices. CXL
devices can be enumerated. Their capabilities can be queried. AFUs can be
opened, attached to the current process, and started. Jobs, described by AFU
specific Work Element Descriptors (WEDs), can be submitted and executed by
AFUs. AFU MMIO space can be mapped into the current process memory, and AFUs
can be configured and controlled via MMIO reads and writes.

%package devel
Summary:        Coherent accelerator interface header files and man pages
Group:          Development/Libraries/C and C++
Requires:       %name%soversion = %version

%description devel
Coherent accelerator interface header files and man pages
only for development purposes.

%prep
%setup -q
%patch1 -p1

%build
make CFLAGS="%{optflags} -fPIC" V=1
mkdir -p build/man3
cp -p man3/*.3 build/man3

%install
make DESTDIR=%{buildroot} prefix=/usr install
mkdir -p %{buildroot}%{_mandir}
cp -a build/man3 %{buildroot}%{_mandir}/

%files -n %{name}%{soversion}
%defattr(-,root,root)
%doc LICENSE
%doc README.md
%{_libdir}/libcxl.so.*

%post -n %{name}%{soversion} -p /sbin/ldconfig

%postun -n %{name}%{soversion} -p /sbin/ldconfig

%files devel
%defattr(-,root,root)
%doc LICENSE
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/libcxl.so

%changelog
