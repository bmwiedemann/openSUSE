#
# spec file for package scotch
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


%global flavor @BUILD_FLAVOR@%{nil}

%define base_pname scotch
%define vers 6.0.7
%define _vers 6_0_7
%define so_ver 0
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%if 0%{?is_opensuse} || 0%{?is_backports}
%undefine DisOMPI1
%undefine DisOMPI2
%undefine DisOMPI3
%else
%define DisOMPI1 ExclusiveArch:  do_not_build
%undefine DisOMPI2
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
 %define package_name %pname
%endif

%if "%{flavor}" == "serial"
%undefine suffix
%undefine mpi_family
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi"
%{?DisOMPI1}
%global mpi_family openmpi
%bcond_with hpc
%define mpi_vers 1
%endif

%if "%{flavor}" == "openmpi2"
%{?DisOMPI2}
%global mpi_family openmpi
%bcond_with hpc
%define mpi_vers 2
%endif

%if "%{flavor}" == "openmpi3"
%{?DisOMPI3}
%global mpi_family openmpi
%bcond_with hpc
%define mpi_vers 3
%endif

%if "%{flavor}" == "mvapich2"
%global mpi_family %{flavor}
%bcond_with hpc
%endif

%if "%{flavor}" == "mpich"
%global mpi_family %{flavor}
%bcond_with hpc
%endif

%if "%{flavor}" == "gnu-hpc"
%bcond_without hpc
%global compiler_family gnu
%undefine c_f_ver
%endif

%if "%{flavor}" == "gnu-mvapich2-hpc"
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_family mvapich2
%endif

%if "%{flavor}" == "gnu-mpich-hpc"
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_family mpich
%endif

%if "%{flavor}" == "gnu-openmpi-hpc"
%{?DisOMPI1}
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_family openmpi
%define mpi_vers 1
%endif

%if "%{flavor}" == "gnu-openmpi2-hpc"
%{?DisOMPI2}
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_family openmpi
%define mpi_vers 2
%endif

%if "%{flavor}" == "gnu-openmpi3-hpc"
%{?DisOMPI3}
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_family openmpi
%define mpi_vers 3
%endif

# Don't build non-HPC on SLE
%if !0%{?is_opensuse}
 %if !0%{?with_hpc:1}
ExclusiveArch:  do_not_build
 %endif
%bcond_with mumps
%else
%bcond_without mumps
%endif

%{?mpi_family:%{bcond_without mpi}}%{!?mpi_family:%{bcond_with mpi}}
%{?with_hpc:%{!?compiler_family:%global compiler_family gnu}}
%{?with_mpi:%{!?mpi_family:error "No MPI family specified!"}}

# For compatibility package names
%if "%{mpi_family}" != "openmpi" || "%{mpi_vers}" != "1"
%define mpi_ext %{?mpi_vers}
%endif

%if %{without mpi}
%define pname %{base_pname}
%define metis metis
%else
%define pt_pref pt
%define pname pt%{base_pname}
%define metis parmetis
%endif

%if %{with hpc}
%{hpc_init -c %compiler_family %{?with_mpi:-m %mpi_family} %{?c_f_ver:-v %{c_f_ver}} %{?mpi_vers:-V %{mpi_vers}} %{?ext:-e %{ext}}}
 %define my_prefix %hpc_prefix
 %define my_bindir %hpc_bindir
 %define my_libdir %hpc_libdir
 %define my_incdir %hpc_includedir
 %define my_mandir %hpc_mandir
 %define package_name   %{hpc_package_name %_vers}
 %define f_name(ln:s:)   %{-l:lib}%{pname}%{-n*}%{hpc_package_name_tail %{?_vers}}
%else
 %if %{without mpi}
  %define my_prefix %_prefix
  %define my_bindir %_bindir
  %define my_libdir %_libdir
  %define my_incdir %_includedir
  %define my_mandir %_mandir
 %else
  %define my_suffix -%{mpi_family}%{?mpi_ext}
  %define my_prefix %{_libdir}/mpi/gcc/%{mpi_family}%{?mpi_ext}
  %define my_bindir %{my_prefix}/bin
  %define my_libdir %{my_prefix}/%{_lib}/
  %define my_incdir %{my_prefix}/include/
  %define my_mandir %{my_prefix}/share/man
 %endif
 %if 0%{!?package_name:1}
  %define package_name   %pname%{?my_suffix}
 %endif
 %define f_name(ln:s:)   %{-l:lib}%{pname}%{-n*}%{-s*}%{?my_suffix}
%endif

Summary:        Graph, mesh and hypergraph partitioning library
License:        CECILL-C
Group:          Productivity/Scientific/Math
Name:           %{package_name}
Version:        %{vers}
Release:        0
Url:            http://www.labri.fr/perso/pelegrin/scotch/
Source0:        https://gforge.inria.fr/frs/download.php/latestfile/298/scotch_%{version}.tar.gz
Source1:        scotch-Makefile.inc.in
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libbz2-devel
BuildRequires:  make
BuildRequires:  zlib-devel
%if %{without hpc}
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
 %if %{with mpi}
BuildRequires:  %{mpi_family}%{?mpi_ext}-devel
 %endif
%else # hpc
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  lua-lmod  >= 7.6.1
BuildRequires:  suse-hpc >= 0.2
Requires:       %{f_name -l -s %{so_ver}} = %version
 %if %{with mpi}
BuildRequires:  %{mpi_family}%{?mpi_vers}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
 %endif
%endif

%description
Scotch is a software package for graph and mesh/hypergraph partitioning and
sparse matrix ordering.

%{?with_hpc:%{hpc_master_package -L}}

%package     -n %{f_name -l -s %{so_ver}}
Summary:        Graph, mesh and hypergraph partitioning library
Group:          System/Libraries
%if %{without hpc}
 %if %{with mpi}
BuildRequires:  libscotch%{so_ver}
Requires:       libscotch%{so_ver}
 %endif
%else
%hpc_requires
Requires:       lua-lmod  >= 7.6.1
%endif

%description -n %{f_name -l -s %{so_ver}}
Scotch is a software package for graph and mesh/hypergraph partitioning and
sparse matrix ordering.

%{?with_hpc:%{hpc_master_package -L -l -n lib%{pname}%{hpc_package_name_tail}}}

%package     devel
Summary:        Development libraries for scotch
Group:          Development/Libraries/C and C++
Requires:       %{f_name -l -s %{so_ver}} = %{version}
%if %{without hpc}
Requires:       gcc-fortran
 %if %{with mpi}
BuildRequires:  scotch-devel
Requires:       %{mpi_family}%{?mpi_ext}-devel
Requires:       scotch-devel
 %else
Provides:       scotch-devel = %{version}
 %endif
%else
Requires:       %{f_name -l -s %{so_ver}}
%hpc_requires_devel
%endif

%description devel
This package contains development libraries for libscotch.

%{?with_hpc:%{hpc_master_package -L devel}}

%package        devel-static
Summary:        Development libraries for scotch
Group:          Development/Libraries/C and C++
Requires:       %{f_name}-devel = %{version}
%{?!with_hpc:Provides:       scotch-devel-static = %{version}}

%description devel-static
This package contains libscotch static libraries.

%package     -n %{f_name -n -%{metis}}-devel
Summary:        Development libraries for scotch
Group:          Development/Libraries/C and C++
%{?!with_hpc:Conflicts:      metis-devel}
Requires:       %{f_name -l -s %{so_ver}}
Requires:       %{f_name}-devel = %{version}

%description -n %{f_name -n -%{metis}}-devel
This package contains the devel libraries and header file in the case
scotch is used as a replacement of the metis library.

%prep
%setup -q -n scotch_%{version}
cp %SOURCE1 src/Makefile.inc

%build

%if %{with hpc}
%hpc_setup
%hpc_debug
%else
export CC=gcc
%{?with_mpi:source %{my_bindir}/mpivars.sh}
%endif
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
%if %{with hpc}
%hpc_setup
%else
export CC=gcc
%{?with_mpi:source %{my_bindir}/mpivars.sh}
%endif
%{?with_mpi:export CC=mpicc}

pushd src/
make install prefix=%{buildroot}%{my_prefix} libdir=%{buildroot}%{my_libdir}
popd
for static_libs in lib/lib%{pname}*.a %{?with_mumps:lib/lib%{?pt_pref}esmumps.a}; do
	libs=`basename $static_libs .a`
	ln -s $libs.so.0.0 lib/$libs.so.0
	ln -s $libs.so.0.0 lib/$libs.so
done
%if %{without hpc}
pushd %{buildroot}%{my_libdir}
ln -s libscotch%{metis}.a lib%{metis}.a
ln -s libscotch%{metis}.so lib%{metis}.so
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
%else
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the Scotch library built with the %{compiler_family} compiler"
puts stderr "toolchain and the %{mpi_family}%{?mpi_vers} MPI stack."
puts stderr " "

puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} compiler and %{mpi_family}%{?mpi_vers} MPI"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY:0}"
module-whatis "%{url}"

set     version                     %{version}

if {[file isdirectory  %{hpc_bindir}]} {
prepend-path    PATH                %{hpc_bindir}
}
prepend-path    MANPATH             %{hpc_mandir}
if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    INCLUDE             %{hpc_includedir}
}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}

setenv          %{hpc_upcase %pname}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase %pname}_BIN        %{hpc_bindir}
if {[file isdirectory  %{hpc_includedir}]} {
setenv          %{hpc_upcase %pname}_LIB        %{hpc_libdir}
}
setenv          %{hpc_upcase %pname}_INC        %{hpc_includedir}
EOF

%endif # without hpc
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

%if %{without mpi} && %{without hpc}
%post -n %{f_name -l -s %so_ver} -p /sbin/ldconfig
%postun -n %{f_name -l -s %so_ver} -p /sbin/ldconfig
%else
# HPC and MPI package install to non-standard locations: don't update cache
%post -n %{f_name -l -s %so_ver}
/sbin/ldconfig -N %{my_libdir}

%postun -n %{f_name -l -s %so_ver}
/sbin/ldconfig -N %{my_libdir}
%{?with_hpc:%hpc_module_delete_if_default}
%endif

%files
%doc README.txt doc/scotch*.pdf
%license doc/CeCILL-*
%if %{with hpc}
%{my_bindir}
%dir %{hpc_datadir}
%{my_mandir}
%else
%{my_bindir}/%{!?with_mpi:*}
%{my_mandir}/man1/%{!?with_mpi:*}
%endif

%files -n %{f_name -l -s %{so_ver}}
%{?with_hpc:%hpc_dirs}
%{?with_hpc:%hpc_modules_files}
%if %{without mpi} || %{without hpc}
%{my_libdir}/libscotch.so.*
%{my_libdir}/libscotcherr.so.*
%{my_libdir}/libscotcherrexit.so.*
 %if %{with mumps}
%{my_libdir}/libscotchmetis.so.*
%{my_libdir}/libesmumps.so.*
 %endif
%endif
%if %{with mpi}
%{my_libdir}/libptscotch.so.*
%{my_libdir}/libptscotcherr.so.*
%{my_libdir}/libptscotcherrexit.so.*
%{my_libdir}/libptscotchparmetis.so.*
%{?with_mumps:%{my_libdir}/libptesmumps.so.*}
%endif

%files devel
%{?with_hpc:%dir %{my_incdir}}
%if %{without mpi} || %{without hpc}
%{my_libdir}/libscotch.so
%{my_libdir}/libscotcherr.so
%{my_libdir}/libscotcherrexit.so
 %if %{with mumps}
%{my_libdir}/libscotchmetis.so
%{my_libdir}/libesmumps.so
 %endif
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

%if %{without hpc}
%files -n %{f_name -n -%{metis}}-devel
%{my_libdir}/lib%{metis}.so
%endif
%{my_incdir}/%{metis}.h

%files devel-static
%{my_libdir}/libscotch.a
%{my_libdir}/libscotcherr.a
%{my_libdir}/libscotcherrexit.a
%if %{with mpi}
%{my_libdir}/libptscotch.a
%{my_libdir}/libptscotcherr.a
%{my_libdir}/libptscotcherrexit.a
%{my_libdir}/libptscotchparmetis.a
%{!?with_hpc:%{my_libdir}/libparmetis.a}
%else
%{my_libdir}/libmetis.a
%endif
%if %{with mumps}
%{my_libdir}/libscotchmetis.a
%{my_libdir}/lib%{?pt_pref}esmumps.a
%endif

%changelog
