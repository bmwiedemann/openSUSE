#
# spec file for package beignet
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


Name:           beignet
Version:        1.3.2
Release:        0
Summary:        OpenCL implementation for Intel GPUs
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://01.org/beignet/
Source0:        https://01.org/sites/default/files/%{name}-%{version}-source.tar.gz
Source99:       beignet-rpmlintrc
Patch0:         beignet-llvm6.patch
Patch1:         0008-Add-preliminary-LLVM-7-support.patch
Patch2:         beignet-disable-NegAddOptimization.patch
Patch3:         0004-Enable-Coffee-Lake-support.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  memory-constraints
BuildRequires:  ncurses-devel
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(zlib)
# exclusive to Intel GPU
ExclusiveArch:  %{ix86} x86_64
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:  clang7-devel
%else
BuildRequires:  clang-devel >= 3.3
%endif

%description
Beignet is an implementation of the OpenCL specification - a generic
compute oriented API. This code base contains the code to run OpenCL programs
on Intel GPUs, which basically defines and implements the OpenCL host functions
required to initialize the device, create the command queues, the kernels and
the programs and run them on the GPU.

%package devel
Summary:        Development files for Beignet, a OpenCL implementation for Intel GPUs
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       opencl-headers

%description devel
Devel package for Beignet, an implementation of the OpenCL
specification, a generic compute oriented API.

%prep
%setup -q -n Beignet-%{version}-Source
%autopatch -p1
rm README.md
cp docs/Beignet.mdwn README.md

%build
%limit_build -m 2000
%cmake \
	-DLLVM_INSTALL_DIR=%{_bindir}/
%cmake_build

%install
%cmake_install
find %{buildroot}%{_includedir}/CL/ -regextype posix-egrep -not -regex ".*(cl_intel.h)" -type f -delete
rm %{buildroot}%{_libdir}/beignet/beignet*.pch

%files
%doc README.md
%license COPYING
%{_libdir}/beignet/
%{_sysconfdir}/OpenCL/vendors/intel-beignet.icd
%dir %{_sysconfdir}/OpenCL
%dir %{_sysconfdir}/OpenCL/vendors

%files devel
%doc docs/*
%{_includedir}/CL/cl_intel.h

%changelog
