#
# spec file for package gmmlib
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


%global somajor 11
%global libname libigdgmm%{somajor}
Name:           gmmlib
Version:        20.3.2
Release:        0
Summary:        Intel(R) Graphics Memory Management Library Package
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/intel/gmmlib
Source0:        https://github.com/intel/gmmlib/archive/intel-gmmlib-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
ExclusiveArch:  x86_64

%description
The Intel(R) Graphics Memory Management Library provides device specific
and buffer management for the Intel(R) Graphics Compute Runtime for
OpenCL(TM) and the Intel(R) Media Driver for VAAPI.

%package -n %{libname}
Summary:        Intel(R) Graphics Memory Management Library development package
Group:          Development/Libraries/C and C++

%description -n %{libname}
The Intel(R) Graphics Memory Management Library provides device specific
and buffer management for the Intel(R) Graphics Compute Runtime for
OpenCL(TM) and the Intel(R) Media Driver for VAAPI.

This package contains shared library.

%package    devel
Summary:        Intel(R) Graphics Memory Management Library development package
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Provides:       libigdgmm-devel = %{version}
Obsoletes:      libigdgmm-devel < %{version}

%description   devel
The Intel(R) Graphics Memory Management Library provides device specific
and buffer management for the Intel(R) Graphics Compute Runtime for
OpenCL(TM) and the Intel(R) Media Driver for VAAPI.

This package provides development files.

%prep
%autosetup -n %{name}-intel-%{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE.md
%{_libdir}/libigdgmm.so.%{somajor}*

%files devel
%{_includedir}/igdgmm
%{_libdir}/libigdgmm.so
%{_libdir}/pkgconfig/igdgmm.pc

%changelog
