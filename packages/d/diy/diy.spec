#
# spec file for package diy
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


# SECTION Multibuild Definitions
%global flavor @BUILD_FLAVOR@%{nil}

%define pname diy

%if "%{flavor}" == ""
%define package_name %{pname}
ExclusiveArch:  do_not_build
%else
ExclusiveArch:  x86_64
%endif

%if "%{flavor}" == "serial"
%undefine suffix
%undefine mpi_flavor
%endif

%if "%{flavor}" == "mpich"
%global mpi_flavor mpich
%global mpi_min_ver 3.3.0
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_mpi:%{!?mpi_flavor:error "No MPI family specified!"}}

%if 0%{!?package_name:1}
 %define package_name   %{pname}%{?my_suffix}
%endif

%if %{without mpi}
 %define my_prefix %{_prefix}
 %define my_bindir %{_bindir}
 %define my_libdir %{_libdir}
 %define my_incdir %{_includedir}
%else
 %define my_prefix %{_libdir}/mpi/gcc/%{mpi_flavor}%{?mpi_ext}
 %define my_bindir %{my_prefix}/bin
 %define my_libdir %{my_prefix}/%{_lib}
 %define my_incdir %{my_prefix}/include
 %define my_suffix -%{mpi_flavor}%{?mpi_ext}
%endif
# /SECTION

Name:           %{package_name}
Version:        3.5.0
Release:        0
Summary:        A block-parallel library
License:        BSD-3-Clause
URL:            https://github.com/diatomic/diy
Source:         https://github.com/diatomic/diy/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM diy-disable-memory-heavy-tests.patch badshah400@gmail.com -- Disable a few tests requiring more than 10 GB memory
Patch0:         diy-disable-memory-heavy-tests.patch
BuildRequires:  cmake >= 3.2
BuildRequires:  gcc-c++
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_ext}-devel
%endif

%description
Diy is a block-parallel library for implementing scalable algorithms
that can execute both in-core and out-of-core. The same program can be
executed with one or more threads per MPI process, seamlessly
combining distributed-memory message passing with shared-memory thread
parallelism.  The abstraction enabling these capabilities is block
parallelism; blocks and their message queues are mapped onto
processing elements (MPI processes or threads) and are migrated
between memory and storage by the diy runtime. Complex communication
patterns, including neighbor exchange, merge reduction, swap
reduction, and all-to-all exchange, are possible in- and out-of-core
in diy.

%package devel
Summary:        A block-parallel library

%description devel
Diy is a block-parallel library for implementing scalable
algorithms that can execute both in-core and out-of-core. The same
program can be executed with one or more threads per MPI process,
seamlessly combining distributed-memory message passing with
shared-memory thread parallelism.  The abstraction enabling these
capabilities is block parallelism; blocks and their message queues
are mapped onto processing elements (MPI processes or threads) and
are migrated between memory and storage by the diy runtime. Complex
communication patterns, including neighbor exchange, merge reduction,
swap reduction, and all-to-all exchange, are possible in- and
out-of-core in diy.

This package provides the header files for development with diy.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
mkdir -p build
pushd build
# %%cmake can't be used directly because of custom INSTALL_PREFIX requirement
cmake .. \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_INSTALL_PREFIX="%{my_prefix}" \
%if %{with mpi}
      -DCMAKE_C_COMPILER="%{my_bindir}/mpicc" \
      -DCMAKE_CXX_COMPILER="%{my_bindir}/mpicxx"
%else
      -DCMAKE_C_COMPILER=gcc \
      -DCMAKE_CXX_COMPILER=g++ \
      -Dmpi=OFF
%endif
%cmake_build
popd

%install
%cmake_install

%check
%if %{with mpi}
source %{my_bindir}/mpivars.sh
%endif
%ctest

%files devel
%doc README.md
%license LICENSE.txt LEGAL.txt
%{my_incdir}/*

%changelog
