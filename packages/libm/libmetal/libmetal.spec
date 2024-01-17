#
# spec file for package libmetal
#
# Copyright (c) 2023 SUSE LLC
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


%define libname libmetal0
Name:           libmetal
Version:        2020.10.0
Release:        0
Summary:        Bare metal interaction APIs
License:        BSD-3-Clause
URL:            https://github.com/OpenAMP/libmetal
Source:         https://github.com/OpenAMP/libmetal/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  libhugetlbfs-devel
BuildRequires:  sysfsutils-devel
ExclusiveArch:  x86_64 %{arm} aarch64 %{ix86} riscv64

%description
Libmetal provides common user APIs to access devices, handle device interrupts
and request memory across the following operating environments:
  * Linux user space (based on UIO and VFIO support in the kernel)
  * RTOS (with and without virtual memory)
  * Bare-metal environments

%package -n %{libname}
Summary:        Bare metal interaction APIs
Provides:       %{name} = %{version}

%description -n %{libname}
Libmetal provides common user APIs to access devices, handle device interrupts
and request memory across the following operating environments:
  * Linux user space (based on UIO and VFIO support in the kernel)
  * RTOS (with and without virtual memory)
  * Bare-metal environments

%package devel
Summary:        Include Files and Libraries mandatory for Development
Requires:       libmetal0 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q -n libmetal-%{version}
# set up our cpu names
ln -s arm lib/processor/armv6l
ln -s arm lib/processor/armv7l
ln -s riscv lib/processor/riscv64
for i in %ix86; do
  ln -s x86 lib/processor/$i
done

%build
%cmake \
  -DWITH_TEST=ON \
  -DWITH_STATIC_LIB=OFF
%cmake_build

%install
%cmake_install
# do not install test binaries
rm %{buildroot}%{_bindir}/test-metal*

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/metal/
%{_libdir}/*.so

%changelog
