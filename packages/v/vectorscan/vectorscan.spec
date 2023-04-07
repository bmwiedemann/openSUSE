#
# spec file for package vectorscan
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


%define _lto_cflags %{nil}
%define sover 5
%define so_suffix -vectorscan

Name:           vectorscan
Version:        5.4.9
Release:        0
Summary:        Regular expression matching library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/VectorCamp/vectorscan
Source:         https://github.com/VectorCamp/vectorscan/archive/refs/tags/vectorscan/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  boost-devel >= 1.57
BuildRequires:  cmake
%if 0%{?suse_version} > 1500
BuildRequires:  gcc-c++ >= 9
%else
# Leap 15.x still uses gcc7 by default
BuildRequires:  gcc9-c++
%endif
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  ragel
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(sqlite3)
Conflicts:      hyperscan
# Do not support 32-bit Arm - https://github.com/VectorCamp/vectorscan/issues/61
# Same for 32-bit x86 - https://github.com/VectorCamp/vectorscan/issues/130
ExcludeArch:    %{ix86} %{arm}

%description
A fork of Intel's Hyperscan, modified to run on more platforms.

Vectorscan will follow Intel's API and internal algorithms where possible,
but will not hesitate to make code changes where it is thought of giving
better performance or better portability. In addition, the code will be
gradually simplified and made more uniform and all architecture specific
-currently Intel- #ifdefs will be removed and abstracted away.

%package -n libhs%{sover}%{so_suffix}%{sover}
Summary:        Regular expression matching library
Group:          System/Libraries
# Conflicts with libhs from Hyperscan
Conflicts:      libhs%{sover}

%description -n libhs%{sover}%{so_suffix}%{sover}
A fork of Intel's Hyperscan, modified to run on more platforms.

Vectorscan will follow Intel's API and internal algorithms where possible,
but will not hesitate to make code changes where it is thought of giving
better performance or better portability. In addition, the code will be
gradually simplified and made more uniform and all architecture specific
-currently Intel- #ifdefs will be removed and abstracted away.

%package examples
Summary:        Example binaries for the vectorscan library
Group:          Development/Libraries/C and C++

%description examples
Example binaries for the vectorscan library:
  benchmarks, hsbench, hscheck, hscollider, patbench,
  pcapscan, simplegrep, unit-hyperscan, unit-internal

%package devel
Summary:        Libraries and header files for the vectorscan library
Group:          Development/Libraries/C and C++
Conflicts:      hyperscan-devel

%description devel
A fork of Intel's Hyperscan, modified to run on more platforms.

This package provides the libraries, include files and other resources
needed for developing Hyperscan applications.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%if 0%{?suse_version} <= 1500
export CC=gcc-9
export CXX=g++-9
%endif
%cmake \
  -DFAT_RUNTIME=ON \
  -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name} \
%ifarch %{ix86} x86_64
  -DBUILD_AVX512=ON \
%endif
  -DCMAKE_SKIP_RPATH=ON \
%ifarch aarch64
  -DBUILD_STATIC_LIBS:BOOL=ON \
  -DBUILD_STATIC_AND_SHARED=ON \
%endif

%cmake_build

%install
%cmake_install
# Install examples
pushd build/
mkdir -p  %{buildroot}%{_bindir}
install bin/* %{buildroot}%{_bindir}
popd

%post -n libhs%{sover}%{so_suffix}%{sover} -p /sbin/ldconfig
%postun -n libhs%{sover}%{so_suffix}%{sover} -p /sbin/ldconfig

%files -n libhs%{sover}%{so_suffix}%{sover}
%license COPYING LICENSE
%{_libdir}/libhs.so.%{sover}*
%{_libdir}/libhs_runtime.so.%{sover}*

%files examples
%{_bindir}/*

%files devel
%{_libdir}/libhs.so
%{_libdir}/libhs_runtime.so
%{_libdir}/pkgconfig/libhs.pc
%{_includedir}/hs/
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/examples
%doc %{_defaultdocdir}/%{name}/examples/README.md
%doc %{_defaultdocdir}/%{name}/examples/*.cc
%doc %{_defaultdocdir}/%{name}/examples/*.c

%changelog
