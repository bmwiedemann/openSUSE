#
# spec file for package scotch
#
# Copyright (c) 2025 SUSE LLC
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
%define so_ver 0
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
Version:        6.1.0
Release:        0
URL:            https://gitlab.inria.fr/scotch/scotch
Source0:        https://gitlab.inria.fr/scotch/scotch/-/archive/v%{version}/%{base_pname}-v%{version}.tar.gz
Source1:        scotch-Makefile.inc.in
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libbz2-devel
BuildRequires:  make
BuildRequires:  zlib-devel
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
%setup -q -n scotch-v%{version}
cp %SOURCE1 src/Makefile.inc

%build
export CC=gcc
%{?with_mpi:source %{my_bindir}/mpivars.sh}
%{?with_mpi:export CC=mpicc}

export SUSE_ASNEEDED=0

%define CCP mpicc
%define CCD mpicc
%define CFLAGS %{optflags} -fPIC -O3 -Drestrict=__restrict -DCOMMON_FILE_COMPRESS_GZ -DCOMMON_PTHREAD -DCOMMON_RANDOM_FIXED_SEED -DSCOTCH_DETERMINISTIC -DSCOTCH_RENAME
%define LDFLAGS -pie -pthread -lz -lbz2 -lm -lrt
cd src/
make %{?_smp_mflags} %{pname} %{?with_mumps:%{?pt_pref}esmumps} CFLAGS="%CFLAGS" LDFLAGS="%LDFLAGS" CC=$CC CCP=%CCP CCD=%CCD
$CC %{LDFLAGS} -shared -Wl,-soname=lib%{pname}err.so.0 -o ../lib/lib%{pname}err.so.0.0	\
	libscotch/library_error.o
$CC %{LDFLAGS} -shared -Wl,-soname=lib%{pname}errexit.so.0 -o	\
	../lib/lib%{pname}errexit.so.0.0	libscotch/library_error_exit.o
rm -f libscotch/library_error*.o
$CC %{LDFLAGS} -shared -Wl,-soname=lib%{pname}.so.0 -o ../lib/lib%{pname}.so.0.0	\
	libscotch/*.o ../lib/lib%{pname}err.so.0.0 -lpthread -lgfortran -lz -lrt
$CC %{LDFLAGS} -shared -Wl,-soname=lib%{pname}%{metis}.so.0 -o ../lib/lib%{pname}%{metis}.so.0.0\
	libscotchmetis/*.o ../lib/lib%{pname}.so.0.0 ../lib/lib%{pname}err.so.0.0 -lz -lm -lrt
%if %{with mumps}
$CC %{LDFLAGS} -shared -Wl,-soname=lib%{?pt_pref}esmumps.so.0 -o ../lib/lib%{?pt_pref}esmumps.so.0.0	\
	esmumps/*.o
%endif
cd ..

%install
export CC=gcc
%{?with_mpi:source %{my_bindir}/mpivars.sh}
%{?with_mpi:export CC=mpicc}

pushd src/
make install prefix=%{buildroot}%{my_prefix} libdir=%{buildroot}%{my_libdir}
popd
for static_libs in lib/lib%{pname}*.a %{?with_mumps:lib/lib%{?pt_pref}esmumps.a}; do
	libs=`basename $static_libs .a`
	ln -s $libs.so.0.0 lib/$libs.so.0
	ln -s $libs.so.0.0 lib/$libs.so
done
pushd %{buildroot}%{my_libdir}
ln -s lib%{?pt_pref}scotch%{metis}.a lib%{metis}.a
ln -s lib%{?pt_pref}scotch%{metis}.so lib%{metis}.so
%if %{with mpi}
	# We create link in order to have the serial libs available in the
	# same directory as the parallel libs. A lot of software using scotch
        # can't manage different dirs for serial and parallel files during
	# their build process.
	for libs in libscotch libscotcherr libscotcherrexit libscotchmetis %{?with_mumps:libesmumps} ; do
		ln -sf %{_libdir}/$libs.so $libs.so
		ln -sf %{_libdir}/$libs.so.%{so_ver} $libs.so.%{so_ver}
		ln -sf %{_libdir}/$libs.so.%{so_ver}.0 $libs.so.%{so_ver}.0
	done
%endif
popd
%if %{without mpi}
# Add "scotch_" prefix to binaries and man pages to avoid name conficts
pushd %{buildroot}%{my_bindir}
for prog in *; do
    mv $prog scotch_${prog}
    chmod 755 scotch_$prog
done
popd
pushd %{buildroot}%{my_mandir}/man1/
for man in *; do
    mv ${man} scotch_${man}
done
popd
%endif # without mpi
cp -dp lib/lib*scotch*.so* %{?with_mumps:lib/lib*esmumps.*} %{buildroot}%{my_libdir}/
%{?with_mumps:cp include/esmumps.h %{buildroot}%{my_incdir}/}
cp src/libscotchmetis/%{metis}.h %{buildroot}%{my_incdir}/

# Convert the license files to utf8
pushd doc
iconv -f iso8859-1 -t utf-8 < CeCILL-C_V1-en.txt > CeCILL-C_V1-en.txt.conv
iconv -f iso8859-1 -t utf-8 < CeCILL-C_V1-fr.txt > CeCILL-C_V1-fr.txt.conv
mv -f CeCILL-C_V1-en.txt.conv CeCILL-C_V1-en.txt
mv -f CeCILL-C_V1-fr.txt.conv CeCILL-C_V1-fr.txt
popd

%fdupes %{buildroot}%{my_bindir}
%fdupes %{buildroot}%{my_mandir}

%if %{without mpi}
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
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
%{my_libdir}/libscotcherr.so.*
%{my_libdir}/libscotcherrexit.so.*
%{my_libdir}/libscotchmetis.so.*
%if %{with mumps}
%{my_libdir}/libesmumps.so.*
%endif
%if %{with mpi}
%{my_libdir}/libptscotch.so.*
%{my_libdir}/libptscotcherr.so.*
%{my_libdir}/libptscotcherrexit.so.*
%{my_libdir}/libptscotchparmetis.so.*
%{?with_mumps:%{my_libdir}/libptesmumps.so.*}
%endif

%files devel
%{my_libdir}/libscotch.so
%{my_libdir}/libscotcherr.so
%{my_libdir}/libscotcherrexit.so
%{my_libdir}/libscotchmetis.so
%if %{with mumps}
%{my_libdir}/libesmumps.so
%endif
%if %{with mpi}
%{my_libdir}/libptscotch.so
%{my_libdir}/libptscotcherr.so
%{my_libdir}/libptscotcherrexit.so
%{my_libdir}/libptscotchparmetis.so
%{?with_mumps:%{my_libdir}/libptesmumps.so}
%endif
%{my_incdir}/*.h
%exclude %{my_incdir}/%{metis}.h

%files -n %{pname}-%{metis}%{?my_suffix}-devel
%{my_libdir}/lib%{metis}.so
%{my_incdir}/%{metis}.h

%files devel-static
%{my_libdir}/libscotch.a
%{my_libdir}/libscotcherr.a
%{my_libdir}/libscotcherrexit.a
%{my_libdir}/libscotchmetis.a
%if %{with mpi}
%{my_libdir}/libptscotch.a
%{my_libdir}/libptscotcherr.a
%{my_libdir}/libptscotcherrexit.a
%{my_libdir}/libptscotchparmetis.a
%{my_libdir}/libparmetis.a
%else
%{my_libdir}/libmetis.a
%endif
%if %{with mumps}
%{my_libdir}/lib%{?pt_pref}esmumps.a
%endif

%changelog
