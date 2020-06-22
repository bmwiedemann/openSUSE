#
# spec file for package fftw3
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


%global flavor @BUILD_FLAVOR@%{nil}

%define bname fftw
%define BNAME FFTW
%define pname fftw3
%define vers 3.3.8
%define _ver 3_3_8

#For non HPC builds only
%ifarch ppc ppc64
%define mpi_implem openmpi
%else
%define mpi_implem openmpi2
%endif

%bcond_with ringdisabled

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if !0%{?is_opensuse:1} && 0%{?sle_version:1} && 0%{?sle_version} < 150200
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%define package_name %pname
%endif

# Magic for OBS Staging. Only build the flavors required by
# other packages in the ring.
%if %{with ringdisabled}
 %if "%flavor" != "standard"
ExclusiveArch:  do_not_build
 %endif
%endif

%if "%{flavor}" == "standard"
%define mpi_flavor standard
%bcond_without mpi
%bcond_with hpc
%bcond_without system_packages
%endif

%if "%flavor" == "gnu-hpc"
%define compiler_family gnu
%undefine c_f_ver
%bcond_with mpi
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_vers 1
%bcond_without hpc
%bcond_without mpi
%endif

%if "%{flavor}" == "gnu-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_vers 2
%bcond_without hpc
%bcond_without mpi
%endif

%if "%{flavor}" == "gnu-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_vers 3
%bcond_without hpc
%bcond_without mpi
%endif

%if "%{flavor}" == "gnu-mvapich2-hpc"
%global compiler_family gnu
%undefine c_f_ver
%define mpi_flavor mvapich2
%bcond_without hpc
%bcond_without mpi
%endif

%if "%{flavor}" == "gnu-mpich-hpc"
%global compiler_family gnu
%undefine c_f_ver
%define mpi_flavor mpich
%bcond_without hpc
%bcond_without mpi
%endif

%if "%flavor" == "gnu7-hpc"
%define compiler_family gnu
%define c_f_ver 7
%bcond_with mpi
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%define c_f_ver 7
%global mpi_flavor openmpi
%define mpi_vers 1
%bcond_without hpc
%bcond_without mpi
%endif

%if "%{flavor}" == "gnu7-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%define c_f_ver 7
%global mpi_flavor openmpi
%define mpi_vers 3
%bcond_without hpc
%bcond_without mpi
%endif

%if "%{flavor}" == "gnu7-mvapich2-hpc"
%global compiler_family gnu
%define c_f_ver 7
%define mpi_flavor mvapich2
%bcond_without hpc
%bcond_without mpi
%endif

%if "%{flavor}" == "gnu7-mpich-hpc"
%global compiler_family gnu
%define c_f_ver 7
%define mpi_flavor mpich
%bcond_without hpc
%bcond_without mpi
%endif

# now exchange the paths
%if %{with hpc}
%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_hpc:%{!?compiler_family:%global compiler_family gnu}}
%{?with_mpi:%{!?mpi_flavor:%global mpi_flavor openmpi}}
%{?with_mpi:%global hpc_module_pname p%{pname}}
# needed by the hpc tools
%{hpc_init -c %compiler_family %{?c_f_ver:-v %{c_f_ver}} %{?with_mpi:-m {%mpi_flavor}} %{?mpi_ver:-V %{mpi_ver}} %{?ext:-e %{ext}}}
%define package_base %{hpc_install_path_base}
%define package_prefix %hpc_prefix
%define package_bindir %hpc_bindir
%define package_libdir %hpc_libdir
%define package_datadir %hpc_datadir
%define package_includedir %hpc_includedir
%define package_mandir %hpc_mandir
%define package_docdir %hpc_docdir
%define package_infodir %hpc_infodir
%define package_name %{hpc_package_name %_ver}
%define package_libname lib%{package_name}
%else
%define package_base %{_prefix}
%define package_prefix %{_prefix}
%define package_bindir %{_bindir}
%define package_libdir %{_libdir}
%define package_datadir %{_datadir}
%define package_includedir %{_includedir}
%define package_mandir %{_mandir}
%define package_docdir %{_docdir}
%define package_infodir %{_infodir}
%define package_name   %pname%{?my_suffix}
%define package_libname lib%{pname}-3
%endif

Name:           %package_name
BuildRequires:  fdupes
BuildRequires:  pkgconfig
Version:        %vers
Release:        0
Summary:        Discrete Fourier Transform (DFT) C Subroutine Library
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://www.fftw.org
Source:         ftp://ftp.fftw.org/pub/fftw/fftw-%{version}%{?pl_ext:-%{pl_ext}}.tar.gz
Source1:        %{pname}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with hpc}
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
%endif
%else
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
Requires:       %{package_name}-libs = %{version}
%ifnarch s390 s390x
BuildRequires:  %{mpi_implem}-devel
%endif
%endif

%description
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%if %{with hpc}
%%{hpc_master_package -L}
%{hpc_master_package -l}
%{hpc_master_package -a devel}
%endif

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %package_libname = %{version}-%{release}
Requires:       glibc-devel
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
%if %{with hpc}
%hpc_requires_devel
%endif
Provides:       fftw-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package devel-static
Summary:        Static libraries for %{pname}
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel

%description devel-static
Libraries to build statically linked applications with fftw3.

%package -n %package_libname
Summary:        Discrete Fourier Transform (DFT) C Subroutine Library
# Remove Prov/Obs when appropriate; were added 2011-Nov-21 (post-openSUSE-12.1)
Group:          System/Libraries
Provides:       fftw3 = %{version}-%{release}
Obsoletes:      fftw3 < 3.3
%if %{with hpc}
%hpc_requires
%endif

%description -n %package_libname
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%if %{without hpc}
%package -n libfftw3_threads3
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Productivity/Scientific/Math
Provides:       fftw3-threads = %{version}-%{release}
Obsoletes:      fftw3-threads < 3.3
# libfftw3_threads.so does not have a DT_NEEDED entry for fftw symbols, since it
# may be used with either libfftw3.so or libfftw3f.so. Hence, manual Requires.
#Requires:       libfftw3-3 = %%{version}

%description -n libfftw3_threads3
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package threads-devel
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Development/Libraries/C and C++
Requires:       fftw3-devel = %{version}-%{release}
Requires:       glibc-devel
Requires:       libfftw3_threads3 = %{version}-%{release}

%description threads-devel
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package -n libfftw3_omp3
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Productivity/Scientific/Math
Provides:       fftw3-openmp = %{version}-%{release}
Obsoletes:      fftw3-openmp < 3.3
# Same as libfftw3_threads.so: manual Requires for fftw3 main lib
#Requires:       libfftw3-3 = %%{version}

%description -n libfftw3_omp3
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package openmp-devel
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Development/Libraries/C and C++
Requires:       fftw3-devel = %{version}-%{release}
Requires:       glibc-devel
Requires:       libfftw3_omp3 = %{version}-%{release}

%description openmp-devel
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.
%endif

%ifnarch s390 s390x

%package -n libfftw3_mpi3
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Productivity/Scientific/Math
Provides:       fftw3-mpi = %{version}-%{release}
Obsoletes:      fftw3-mpi < 3.3
# Same as libfftw3_threads.so: manual Requires for fftw3 main lib
#Requires:       libfftw3-3 = %%{version}
#Requires:       openmpi

%description -n libfftw3_mpi3
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package mpi-devel
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Development/Libraries/C and C++
Requires:       %{mpi_implem}-devel
Requires:       fftw3-devel = %{version}
Requires:       glibc-devel
Requires:       libfftw3_mpi3 = %{version}-%{release}

%description mpi-devel
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.
%endif

%prep
%setup -q -n %{bname}-%{version}%{?pl_ext:-%{pl_ext}}

%if %{without hpc}
cat > %{_sourcedir}/baselibs.conf  <<EOF
%{package_libname}
lib%{name}_threads3
lib%{name}_omp3
lib%{name}_mpi3
EOF
%endif

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%if %{with hpc}
%hpc_setup
%endif
%ifnarch s390 s390x
%if "%{mpi_flavor}" == "standard"
source %_libdir/mpi/gcc/%{mpi_implem}/bin/mpivars.sh
%endif
%endif

%if %{without hpc}
%configure \
  --disable-static \
%else
%hpc_configure \
  --enable-static \
%endif
%ifnarch s390 s390x
%if %{with mpi}
  --enable-mpi \
%endif
%ifarch %ix86 x86_64
  --enable-sse2 \
  --enable-avx \
%endif
%endif
  --enable-shared \
  --enable-threads \
  --enable-openmp

make %{?_smp_mflags}

%install
%if %{with hpc}
%{hpc_setup}
%endif
%makeinstall

# remove unneeded files
%{!?with_hpc:rm -f %{buildroot}%{package_libdir}/lib*.*a}

# hack to also compile/install single-precision version:
make distclean

%ifnarch s390 s390x
%if "%{mpi_flavor}" == "standard"
source %_libdir/mpi/gcc/%{mpi_implem}/bin/mpivars.sh
%endif
%endif

%if %{without hpc}
%configure \
%else
%hpc_configure \
%endif
	--enable-shared --enable-threads --enable-float --enable-openmp \
%ifnarch s390 s390x
%if %{with mpi}
  --enable-mpi \
%endif
%endif
%ifarch %ix86 x86_64
  --enable-sse2 \
%endif
  --disable-static

make %{?_smp_mflags}
%makeinstall

# hack to also compile/install long-double-precision version:
make distclean

%ifnarch s390 s390x
%if "%{mpi_flavor}" == "standard"
source %_libdir/mpi/gcc/%{mpi_implem}/bin/mpivars.sh
%endif
%endif
%if %{without hpc}
%configure \
%else
%hpc_configure \
%endif
	--enable-shared --enable-threads --enable-long-double --enable-openmp \
%ifnarch s390 s390x
%if %{with mpi}
  --enable-mpi \
%endif
%endif
  --disable-static

make %{?_smp_mflags}
%makeinstall

# remove unneeded files
%{!?with_hpc:rm -f %{buildroot}%{package_libdir}/lib*.*a}

gzip -9nf %{buildroot}%{package_infodir}/*.info*

# remove Makefiles in doc directory at last
find doc -name 'Makefile*' | xargs rm
%if %{with hpc}
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} toolchain."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} toolchain"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{summary:0}"
module-whatis "URL: %{url}"

set     version                     %{version}

prepend-path    PATH                %{hpc_bindir}
prepend-path    MANPATH             %{hpc_mandir}
prepend-path    INCLUDE             %{hpc_includedir}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}
setenv          %{BNAME}_DIR        %{hpc_prefix}
setenv          %{BNAME}_BIN        %{hpc_bindir}
setenv          %{BNAME}_LIB        %{hpc_libdir}
setenv          %{BNAME}_INC        %{hpc_includedir}
if ([file isdirectory  %{hpc_includedir}]) {
# should work also for fortran
prepend-path    LIBRARY_PATH        %{hpc_libdir}
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}
}

%{hpc_modulefile_add_pkgconfig_path}

EOF
%endif

%fdupes -s doc

%preun devel
%install_info_delete --info-dir=%{package_infodir} %{package_infodir}/fftw3.info.gz

%post devel
%install_info --info-dir=%{package_infodir} %{package_infodir}/fftw3.info.gz

%post -n %package_libname  -p /sbin/ldconfig

%postun -n %package_libname -p /sbin/ldconfig

%if %{without hpc}
%post -n libfftw3_threads3 -p /sbin/ldconfig

%postun -n libfftw3_threads3 -p /sbin/ldconfig

%post -n libfftw3_omp3 -p /sbin/ldconfig

%postun -n libfftw3_omp3 -p /sbin/ldconfig

%ifnarch s390 s390x

%post -n libfftw3_mpi3 -p /sbin/ldconfig

%postun -n libfftw3_mpi3 -p /sbin/ldconfig
%endif
%endif

%files -n %package_libname
%defattr(-,root,root)
%{package_libdir}/libfftw3.so.3*
%{package_libdir}/libfftw3f.so.3*
%{package_libdir}/libfftw3l.so.3*

%if %{without hpc}
%files -n libfftw3_threads3
%defattr(-,root,root)
%endif
# ENDIF FOR {without hpc}
%{package_libdir}/libfftw3_threads.so.3*
%{package_libdir}/libfftw3f_threads.so.3*
%{package_libdir}/libfftw3l_threads.so.3*

%if %{without hpc}
%files -n libfftw3_omp3
%defattr(-,root,root)
%else
%hpc_modules_files
%endif
# ENDIF FOR {without hpc}
%{package_libdir}/libfftw3_omp.so.3*
%{package_libdir}/libfftw3f_omp.so.3*
%{package_libdir}/libfftw3l_omp.so.3*

%ifnarch s390 s390x
%if %{with mpi}
%if %{without hpc}
%files -n libfftw3_mpi3
%defattr(-,root,root)
%endif
# ENDIF FOR {without hpc}
%{package_libdir}/libfftw3_mpi.so.3*
%{package_libdir}/libfftw3f_mpi.so.3*
%{package_libdir}/libfftw3l_mpi.so.3*
%endif
# ENDIF FOR {without mpi}
%endif
# ENDIF FOR ARCH s390 s390x

%files devel
%defattr(-,root,root)
%if %{with hpc}
%{package_infodir}/
%hpc_dirs
%dir %package_libdir/pkgconfig
%dir %package_includedir
%dir %package_mandir
%dir %package_mandir/man1
%dir %package_infodir
%dir %package_bindir
%dir %package_datadir
%endif
%doc AUTHORS CONVENTIONS COPYING COPYRIGHT ChangeLog NEWS README TODO
%doc doc/*
%doc %{package_mandir}/man?/*
%dir %package_libdir/cmake
%dir %package_libdir/cmake/%{pname}
%{package_infodir}/*.info*
%{package_includedir}/fftw3.*
%{package_includedir}/fftw3q.f03
%{package_includedir}/fftw3l.f03
%{package_libdir}/libfftw3.so
%{package_libdir}/libfftw3f.so
%{package_libdir}/libfftw3l.so
%{package_libdir}/pkgconfig/*.pc
%dir %package_libdir/cmake
%dir %package_libdir/cmake/%{pname}
%{package_libdir}/cmake/%{pname}/FFTW3*.cmake
%{package_bindir}/*

%if %{without hpc}
%files threads-devel
%defattr(-,root,root)
%endif
# ENDIF FOR {without hpc}
%{package_libdir}/libfftw3_threads.so
%{package_libdir}/libfftw3f_threads.so
%{package_libdir}/libfftw3l_threads.so

%if %{without hpc}
%files openmp-devel
%defattr(-,root,root)
%endif
# ENDIF FOR {without hpc}
%{package_libdir}/libfftw3_omp.so
%{package_libdir}/libfftw3f_omp.so
%{package_libdir}/libfftw3l_omp.so

%ifnarch s390 s390x
%if %{with mpi}
%if %{without hpc}
%files mpi-devel
%defattr(-,root,root)
%endif
# ENDIF FOR {without hpc}
%{package_libdir}/libfftw3_mpi.so
%{package_libdir}/libfftw3f_mpi.so
%{package_libdir}/libfftw3l_mpi.so
%{package_includedir}/fftw3-mpi.*
%{package_includedir}/fftw3l-mpi.f03
%endif
# ENDIF FOR {with mpi}
%endif
# ENDIF FOR arch s390 s390x

%if %{with hpc}
%files  devel-static
%defattr(-,root,root)
%{package_libdir}/*.*a
%endif

%changelog
