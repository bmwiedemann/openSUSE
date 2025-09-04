#
# spec file for package scotch
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}

%define base_pname scotch
%define so_ver 7_0
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
 %define package_name %pname
%else
 %if "%{flavor}" == "serial"
 %else
%global mpi_flavor %{flavor}
 %endif
%endif

%if "%{flavor}" == "openmpi5"
ExcludeArch:    %{ix86} %{arm}
%endif

# mvapich2 seems to be broken in :Factory, causing tests to fail
%if "%{flavor}" == "mvapich2" && 0%{?suse_version} > 1650
%bcond_with tests
%else
%bcond_without tests
%endif

%bcond_without mumps

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}

%if %{without mpi}
%define pname %{base_pname}
%define metis metis
%else
%define pt_pref pt
%define pname pt%{base_pname}
%define metis parmetis
%endif

%if %{without mpi}
 %define my_prefix %_prefix
 %define my_bindir %_bindir
 %define my_libdir %_libdir
 %define my_incdir %_includedir
 %define my_mandir %_mandir
%else
 %define my_suffix -%{mpi_flavor}
 %define my_prefix %{_libdir}/mpi/gcc/%{mpi_flavor}
 %define my_bindir %{my_prefix}/bin
 %define my_libdir %{my_prefix}/%{_lib}/
 %define my_incdir %{my_prefix}/include/
 %define my_mandir %{my_prefix}/share/man
%endif
%if 0%{!?package_name:1}
 %define package_name   %pname%{?my_suffix}
%endif
%define libname lib%{pname}%{so_ver}%{?my_suffix}
%define metis_pname  lib%{pname}-metis%{?my_suffix}

Summary:        Graph, mesh and hypergraph partitioning library
License:        CECILL-C
Group:          Productivity/Scientific/Math
Name:           %{package_name}
Version:        7.0.8
Release:        0
URL:            https://gitlab.inria.fr/scotch/scotch
Source0:        https://gitlab.inria.fr/scotch/scotch/-/archive/v%{version}/%{base_pname}-v%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  make
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
 %if %{with mpi}
BuildRequires:  %{mpi_flavor}-devel
 %endif

%description
Scotch is a software package for graph and mesh/hypergraph partitioning and
sparse matrix ordering.

%package     -n %{libname}
Summary:        Graph, mesh and hypergraph partitioning library
Group:          System/Libraries
 %if %{with mpi}
BuildRequires:  libscotch%{so_ver}
Requires:       libscotch%{so_ver}
 %endif

%description -n %{libname}
Scotch is a software package for graph and mesh/hypergraph partitioning and
sparse matrix ordering.

%package     devel
Summary:        Development libraries for scotch
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       gcc-fortran
 %if %{with mpi}
BuildRequires:  scotch-devel
Requires:       %{mpi_flavor}-devel
Requires:       scotch-devel
 %else
Provides:       scotch-devel = %{version}
 %endif

%description devel
This package contains development libraries for libscotch.

%package        devel-static
Summary:        Development libraries for scotch
Group:          Development/Libraries/C and C++
Requires:       %{package_name}-devel = %{version}
Provides:       scotch-devel-static = %{version}

%description devel-static
This package contains libscotch static libraries.

%package     -n %{pname}-%{metis}%{?my_suffix}-devel
Summary:        Development libraries for scotch
Group:          Development/Libraries/C and C++
%{?!with_mpi:Conflicts:      metis-devel}
Requires:       %{libname}
Requires:       %{package_name}-devel = %{version}

%description -n %{pname}-%{metis}%{?my_suffix}-devel
This package contains the devel libraries and header file in the case
scotch is used as a replacement of the metis library.

%prep
%autosetup -n scotch-v%{version}

%build
export CC=gcc
%{?with_mpi:source %{my_bindir}/mpivars.sh}
%{?with_mpi:export CC=mpicc}

# Must not be compiled with -D_FORTIFY_SOURCE=3, see
# https://gitlab.inria.fr/scotch/scotch/-/blob/master/INSTALL.txt
export RPMOPTFLAGS="%(echo '%{optflags}' | sed 's/-D_FORTIFY_SOURCE=3/-D_FORTIFY_SOURCE=2/')"
%global optflags $RPMOPTFLAGS

# Note: We need to re-define the linker flag options to cmake because
# compilation fails with `-Wl,no-undefined`, passed as part of cmake macro
%cmake \
  -DCMAKE_INSTALL_PREFIX=%{my_prefix} \
  -DBUILD_LIBESMUMPS=%{?with_mumps:ON}%{!?with_mumps:OFF} \
  -DBUILD_PTSCOTCH=%{?with_mpi:ON}%{!?with_mpi:OFF} \
  -DBUILD_LIBSCOTCHMETIS=ON \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_EXE_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
  -DCMAKE_MODULE_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
  -DENABLE_TESTS=%{?with_tests:ON}%{!?with_tests:OFF} \
  %{nil}
%cmake_build

%install
%{?with_mpi:source %{my_bindir}/mpivars.sh}
%{?with_mpi:export CC=mpicc}

%cmake_install

%if %{without mpi}
# Rename conflicting or confusing binaries/man-files:
# * Package `mt-st` also provides `/usr/bin/mtst` and its man file; rename to avoid conflict
# * Package `gpart` installs `/usr/sbin/gpart`; rename to avoid confusion (no conflict)
# re-named so that, e.g. mtst<TAB> completes the binary name when in PATH
for exe in mtst gpart;
do
  mv %{buildroot}%{_bindir}/${exe} %{buildroot}%{_bindir}/${exe}-scotch
done
mv %{buildroot}%{_mandir}/man1/mtst.1 %{buildroot}%{_mandir}/man1/mtst-scotch.1
# /Section
%endif

# Convert the license files to utf8
pushd doc
iconv -f iso8859-1 -t utf-8 < CeCILL-C_V1-en.txt > CeCILL-C_V1-en.txt.conv
iconv -f iso8859-1 -t utf-8 < CeCILL-C_V1-fr.txt > CeCILL-C_V1-fr.txt.conv
mv -f CeCILL-C_V1-en.txt.conv CeCILL-C_V1-en.txt
mv -f CeCILL-C_V1-fr.txt.conv CeCILL-C_V1-fr.txt
popd

%fdupes %{buildroot}%{my_bindir}
%fdupes %{buildroot}%{my_mandir}

# Section Tests
%if %{with tests}
%check
%{?with_mpi:source %{my_bindir}/mpivars.sh}
%{?with_mpi:export CC=mpicc}

# Checks are un-reliable when run in parallel, see https://gitlab.inria.fr/scotch/scotch/-/issues/50
export LD_LIBRARY_PATH+=:%{buildroot}%{my_libdir}
%ctest --parallel 1

%endif
# /Section Tests

%if %{without mpi}
%ldconfig_scriptlets -n %{libname}
%else

# MPI package install to non-standard locations: don't update cache
%post -n %{libname}
/sbin/ldconfig -N %{my_libdir}

%postun -n %{libname}
/sbin/ldconfig -N %{my_libdir}
%endif

%files
%doc README.txt doc/scotch*.pdf
%license doc/CeCILL-*
%{my_bindir}/%{!?with_mpi:*}
%{my_mandir}/man1/%{!?with_mpi:*}

%files -n %{libname}
%{my_libdir}/libscotch.so.*
%{my_libdir}/libscotchmetis*.so.*
%{my_libdir}/libscotcherr.so.*
%{my_libdir}/libscotcherrexit.so.*
%if %{with mumps}
%{my_libdir}/libesmumps.so.*
%endif
%if %{with mpi}
%{my_libdir}/libptscotch.so.*
%{my_libdir}/libptscotcherr.so.*
%{my_libdir}/libptscotcherrexit.so.*
%{my_libdir}/libptscotchparmetis*.so.*
%{?with_mumps:%{my_libdir}/libptesmumps.so.*}
%endif

%files devel
%{my_libdir}/libscotch.so
%{my_libdir}/libscotchmetis*.so
%{my_libdir}/libscotcherr.so
%{my_libdir}/libscotcherrexit.so
%{my_libdir}/cmake/scotch/
%if %{with mumps}
%{my_libdir}/libesmumps.so
%endif
%if %{with mpi}
%dir %{my_libdir}/cmake
%{my_libdir}/libptscotch.so
%{my_libdir}/libptscotcherr.so
%{my_libdir}/libptscotcherrexit.so
%{my_libdir}/libptscotchparmetis*.so
%{?with_mumps:%{my_libdir}/libptesmumps.so}
%endif
%{my_incdir}/*.h
%exclude %{my_incdir}/%{metis}.h

%changelog
