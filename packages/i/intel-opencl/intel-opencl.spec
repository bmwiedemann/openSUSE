#
# spec file for package intel-opencl
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


%if 0%{?suse_version} >= 1600 || 0%{?sle_version} > 150600
%bcond_without level_zero
%else
%bcond_with level_zero
%endif

Name:           intel-opencl
Version:        24.13.29138.7
Release:        1%{?dist}
Summary:        Intel Graphics Compute Runtime for OpenCL
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/intel/compute-runtime
Source0:        https://github.com/intel/compute-runtime/archive/%{version}/compute-runtime-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if %{with level_zero}
BuildRequires:  level-zero-devel
%endif
BuildRequires:  libigc-devel
BuildRequires:  libigdgmm-devel >= 22.3.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(igc-opencl)
BuildRequires:  pkgconfig(libva)
Requires:       libigc1
Requires:       libigdfcl1
Requires:       libopencl-clang14
Recommends:     libOpenCL1
ExclusiveArch:  x86_64

%description
Intel Graphics Compute Runtime for OpenCL.

%package devel
Summary:        Headers for the Intel Graphics Compute Runtime OpenCL Driver
Requires:       %{name} = %{version}-%{release}

%description devel
Development package for Intel Graphics Compute Runtime for OpenCL.

%if %{with level_zero}
%package -n libze_intel_gpu1
Summary:        Intel GPU support for oneAPI level zero
Requires:       level-zero
Requires:       libigc1

%description -n libze_intel_gpu1
This package provides offloading to an Intel GPU via the oneAPI level zero interface.
%endif

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
%if 0%{?suse_version} > 1600
mkdir -p %{buildroot}/%{_datadir}/OpenCL/vendors
mv %{buildroot}/%{_sysconfdir}/OpenCL/vendors/intel.icd %{buildroot}/%{_datadir}/OpenCL/vendors/
%endif
rm -Rf %{buildroot}%{_prefix}/lib/debug

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%if %{with level_zero}
%post -n libze_intel_gpu1 -p /sbin/ldconfig
%postun -n libze_intel_gpu1 -p /sbin/ldconfig
%endif

%files
%{_libdir}/intel-opencl/libigdrcl.so
%{_libdir}/libocloc.so
%{_bindir}/ocloc
%{_libdir}/intel-opencl
%if 0%{?suse_version} > 1600
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

%if %{with level_zero}
%files -n libze_intel_gpu1
%{_libdir}/libze_intel_gpu.so.1
%{_libdir}/libze_intel_gpu.so.1.3.*
%exclude %{_includedir}/level_zero/zet_intel_gpu_debug.h
%endif

%changelog
