#
# spec file for package gmmlib
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define so_ver	9

Name:           gmmlib
Version:        19.2.4
Release:        0
Summary:        Intel Graphics Memory Management Library
License:        MIT
Group:          System/Libraries
URL:            https://github.com/intel/gmmlib
Source:         https://github.com/intel/gmmlib/archive/intel-gmmlib-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
ExclusiveArch:  x86_64

%description
The Intel Graphics Memory Management Library provides device specific and
buffer management for the Intel Graphics Compute Runtime for OpenCL and
the Intel Media Driver for VAAPI.

%package -n libigdgmm%{so_ver}
Summary:        Intel Graphics Memory Management Library
Group:          System/Libraries

%description -n libigdgmm%{so_ver}
The Intel Graphics Memory Management Library provides device specific and
buffer management for the Intel Graphics Compute Runtime for OpenCL and
the Intel Media Driver for VAAPI.

%package -n libigdgmm-devel
Summary:        Development files for Intel Graphics Memory Management Library
Group:          Development/Libraries/C and C++
Requires:       libigdgmm%{so_ver} = %{version}
Provides:       gmmlib-devel

%description -n libigdgmm-devel
The Intel Graphics Memory Management Library provides device specific and
buffer management for the Intel Graphics Compute Runtime for OpenCL and
the Intel Media Driver for VAAPI.

This package contains the development headers for the library found in
libigdgmm%{so_ver}.

%prep
%setup -q -c -a 0
mv gmmlib-intel-gmmlib-* gmmlib
chmod -x gmmlib/*.md gmmlib/*.rst

%define __sourcedir gmmlib

%build
srcroot=`pwd`
%cmake
%make_jobs

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/*.a

%post -n libigdgmm%{so_ver} -p /sbin/ldconfig
%postun -n libigdgmm%{so_ver} -p /sbin/ldconfig

%files -n libigdgmm%{so_ver}
%doc gmmlib/README.rst
%license gmmlib/LICENSE.md
%{_libdir}/libigdgmm.so.*

%files -n libigdgmm-devel
%{_includedir}/igdgmm
%{_libdir}/libigdgmm.so
%{_libdir}/pkgconfig/igdgmm.pc

%changelog
