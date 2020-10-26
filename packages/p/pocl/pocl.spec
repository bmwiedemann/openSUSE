#
# spec file for package pocl
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2014 Guillaume GARDET <guillaume@opensuse.org>
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


%define sover  2.5.0
Name:           pocl
Version:        1.5
Release:        0
Summary:        Portable Computing Language - an OpenCL implementation
# The whole code is under MIT
# except include/utlist.h which is under BSD (and unbundled) and
# except lib/kernel/vecmath which is under GPLv3+ or LGPLv3+ (and unbundled in future)
License:        MIT
Group:          Development/Tools/Other
URL:            http://portablecl.org/
Source0:        https://github.com/pocl/pocl/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       pocl-rpmlintrc
Patch0:         link_against_libclang-cpp_so.patch
BuildConflicts: clang-devel >= 11
BuildRequires:  clang-devel >= 6
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(hwloc)
# Autoreq does not look into the ICD file
Requires:       libpocl2
# PPC has limited support/testing from upstream
# s390(x) is also not supported, so use ExclusiveArch
ExclusiveArch:  %{ix86} x86_64 %arm aarch64

%description
Portable Computing Language (pocl) is an implementation of the OpenCL standard
which can be adapted for new targets and devices, both for homogeneous CPU and
heterogenous GPUs/accelerators.

pocl uses Clang as an OpenCL C frontend and LLVM for the kernel compiler
implementation, and as a portability layer. If your desired target has an LLVM
backend, it should be possible to get OpenCL support by using pocl.

pocl yields improved performance portability by using a kernel compiler that
can generate multi-work-item work-group functions that exploit various types of
parallel hardware resources, such as VLIW, superscalar, SIMD, SIMT, multicore
and multithread.

%package -n libpocl2
Summary:        Shared Library part of pocl
Group:          System/Libraries

%description -n libpocl2
Portable Computing Language (pocl) is an implementation of the OpenCL standard
which can be adapted for new targets and devices, both for homogeneous CPU and
heterogenous GPUs/accelerators.

This subpackage contains the shared library part of pocl.

%package devel
Summary:        Development files for the Portable Computing Language
Group:          Development/Languages/Other
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libpocl2 = %{version}-%{release}
Requires:       opencl-headers

%description devel
Portable Computing Language (pocl) is an implementation of the OpenCL standard
which can be adapted for new targets and devices, both for homogeneous CPU and
heterogenous GPUs/accelerators.

This subpackage provides the development files needed for pocl.

%prep
%setup -q
%patch0 -p1

%build
%define __builder ninja
%cmake \
  -DENABLE_CUDA=0 \
  -DENABLE_ICD=ON \
  -DPOCL_INSTALL_ICD_VENDORDIR=%{_datadir}/OpenCL/vendors \
%ifarch %{ix86} x86_64
  -DKERNELLIB_HOST_CPU_VARIANTS=distro \
%endif
%ifarch %{arm}
  -DLLC_HOST_CPU=cortex-a9 \
%endif
%ifarch aarch64
  -DLLC_HOST_CPU=cortex-a53 \
%endif
  -DWITH_LLVM_CONFIG=%{_bindir}/llvm-config

sed -i 's/-Wl,--no-undefined//g' CMakeCache.txt
sed -i 's/-Wl,--no-undefined//g' build.ninja

%make_jobs

%install
%cmake_install
# TODO: check packaging instructions
sed -i 's|%{_prefix}%{_prefix}/|%{_prefix}/|g' %{buildroot}%{_datadir}/OpenCL/vendors/pocl.icd
# Unbundle vecmath
#rm -vf %%{buildroot}/%%{_libdir}/pocl/vecmath/
#ln -vs %%{_includedir}/vecmath %%{buildroot}/%%{_libdir}/pocl/vecmath
# <visit0r> but you need to run the .py to generate the files under the pocl dir

%post -n libpocl2 -p /sbin/ldconfig
%postun -n libpocl2 -p /sbin/ldconfig

%files
%doc CHANGES README doc/sphinx/source/*.rst
%license LICENSE
%dir %{_datadir}/OpenCL/
%dir %{_datadir}/OpenCL/vendors
%{_datadir}/OpenCL/vendors/pocl.icd
%{_bindir}/poclcc
%dir %{_libdir}/pocl/
%{_libdir}/pocl/libllvmopencl.so
%{_datadir}/pocl/

%files -n libpocl2
%{_libdir}/libpocl.so.2
%{_libdir}/libpocl.so.%{sover}

%files devel
%{_libdir}/libpocl.so
%{_libdir}/pkgconfig/pocl.pc

%changelog
