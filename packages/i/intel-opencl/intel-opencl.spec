#
# spec file for package intel-opencl
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


Name:           intel-opencl
Version:        21.43.21438
Release:        1%{?dist}
Summary:        Intel(R) Graphics Compute Runtime for OpenCL(TM)
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/intel/compute-runtime
Source0:        https://github.com/intel/compute-runtime/archive/%{version}/compute-runtime-%{version}.tar.gz
Patch0:         0001-Include-memory-in-generate_cpp_array.cpp.patch
Patch1:         0001-include-cstdint-needed-when-compiling-with-gcc13.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libigc-devel
BuildRequires:  libigdgmm-devel >= 21.2.2
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(igc-opencl)
BuildRequires:  pkgconfig(libva)
Requires:       libigc1
Requires:       libigdfcl1
Requires:       libopencl-clang11
ExclusiveArch:  x86_64

%description
Intel(R) Graphics Compute Runtime for OpenCL(TM).

%package devel
Summary:        Intel Graphics Compute Runtime for OpenCL Driver
Requires:       %{name} = %{version}-%{release}

%description devel
Development package for Intel Graphics Compute Runtime for OpenCL.

%prep
%autosetup -p1 -n compute-runtime-%{version}

%build
%define __builder ninja

# Needed for gcc12+
%if 0%{?suse_version} > 1500
export CXXFLAGS="-Wno-error=maybe-uninitialized -Wno-error=mismatched-new-delete"
%endif

%cmake \
  -DSKIP_UNIT_TESTS=1
%cmake_build

%install
%cmake_install
chmod +x %{buildroot}%{_libdir}/intel-opencl/libigdrcl.so
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}/%{_datadir}/OpenCL/vendors
mv %{buildroot}/%{_sysconfdir}/OpenCL/vendors/intel.icd %{buildroot}/%{_datadir}/OpenCL/vendors/
%endif
rm -Rf %{buildroot}%{_prefix}/lib/debug

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/intel-opencl/libigdrcl.so
%{_libdir}/libocloc.so
%{_bindir}/ocloc
%{_libdir}/intel-opencl
%if 0%{?suse_version} > 1500
%{_datadir}/OpenCL
%{_datadir}/OpenCL/vendors
%{_datadir}/OpenCL/vendors/intel.icd
%else
%{_sysconfdir}/OpenCL
%{_sysconfdir}/OpenCL/vendors
%{_sysconfdir}/OpenCL/vendors/intel.icd
%endif

%files devel
%{_includedir}/ocloc_api.h

%changelog
