#
# spec file for package hdf5
#
# Copyright (c) 2022 SUSE LLC
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

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if !0%{?is_opensuse} && 0%{?sle_version:1} && 0%{?sle_version} < 150200
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif

%if 0%{?sle_version:1} && 0%{?sle_version} < 150300
%define DisOMPI4 ExclusiveArch:  do_not_build
%endif

# Disable until resource issue is resolved.
%bcond_with check

%define use_sz2 0

%define short_ver 1.12
%define vers %{short_ver}.2
%define _vers %( echo %{vers} | tr '.' '_' )
%define src_ver %{version}
%define pname hdf5
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
 %define package_name %pname
%endif

%if "%{flavor}" == "serial"
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi1"
%{?DisOMPI1}
%global mpi_flavor openmpi
%define mpi_vers 1
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi2"
%{?DisOMPI2}
%global mpi_flavor openmpi
%define mpi_vers 2
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi3"
%{?DisOMPI3}
%global mpi_flavor openmpi
%define mpi_vers 3
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi4"
%{?DisOMPI4}
%global mpi_flavor openmpi
%define mpi_vers 4
%bcond_with hpc
%endif

%if "%{flavor}" == "mvapich2"
%global mpi_flavor %{flavor}
%bcond_with hpc
%endif

%if "%{flavor}" == "gnu-hpc"
%bcond_without hpc
%global compiler_family gnu
%undefine c_f_ver
%endif

%if "%{flavor}" == "gnu-openmpi-hpc"
%{?DisOMPI1}
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_vers 1
%endif

%if "%{flavor}" == "gnu-mvapich2-hpc"
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor mvapich2
%endif

%if "%{flavor}" == "gnu-openmpi2-hpc"
%{?DisOMPI2}
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_vers 2
%endif

%if "%{flavor}" == "gnu-openmpi3-hpc"
%{?DisOMPI3}
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_vers 3
%endif

%if "%{flavor}" == "gnu-openmpi4-hpc"
%{?DisOMPI4}
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_vers 4
%endif

%if "%{flavor}" == "gnu-mpich-hpc"
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor mpich
%endif

%if "%{flavor}" == "gnu7-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%undefine mpi_flavor
%endif

%if "%{flavor}" == "gnu7-openmpi-hpc"
%{?DisOMPI1}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor openmpi
%define mpi_vers 1
%endif

%if "%{flavor}" == "gnu7-openmpi2-hpc"
%{?DisOMPI2}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor openmpi
%define mpi_vers 2
%endif

%if "%{flavor}" == "gnu7-mvapich2-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor mvapich2
%endif

%if "%{flavor}" == "gnu7-openmpi3-hpc"
%{?DisOMPI3}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor openmpi
%define mpi_vers 3
%endif

%if "%{flavor}" == "gnu7-openmpi4-hpc"
%{?DisOMPI4}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor openmpi
%define mpi_vers 4
%endif

%if "%{flavor}" == "gnu7-mpich-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor mpich
%endif

%if "%{flavor}" == "gnu8-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%undefine mpi_flavor
%endif

%if "%{flavor}" == "gnu8-openmpi-hpc"
%{?DisOMPI1}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor openmpi
%define mpi_vers 1
%endif

%if "%{flavor}" == "gnu8-openmpi2-hpc"
%{?DisOMPI2}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor openmpi
%define mpi_vers 2
%endif

%if "%{flavor}" == "gnu8-openmpi3-hpc"
%{?DisOMPI3}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor openmpi
%define mpi_vers 3
%endif

%if "%{flavor}" == "gnu8-openmpi4-hpc"
%{?DisOMPI4}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor openmpi
%define mpi_vers 4
%endif

%if "%{flavor}" == "gnu8-mvapich2-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor mvapich2
%endif

%if "%{flavor}" == "gnu8-mpich-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor mpich
%endif

%if "%{flavor}" == "gnu9-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%undefine mpi_flavor
%endif

%if "%{flavor}" == "gnu9-openmpi-hpc"
%{?DisOMPI1}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor openmpi
%define mpi_vers 1
%endif

%if "%{flavor}" == "gnu9-openmpi2-hpc"
%{?DisOMPI2}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor openmpi
%define mpi_vers 2
%endif

%if "%{flavor}" == "gnu9-openmpi3-hpc"
%{?DisOMPI3}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor openmpi
%define mpi_vers 3
%endif

%if "%{flavor}" == "gnu9-openmpi4-hpc"
%{?DisOMPI4}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor openmpi
%define mpi_vers 4
%endif

%if "%{flavor}" == "gnu9-mvapich2-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor mvapich2
%endif

%if "%{flavor}" == "gnu9-mpich-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor mpich
%endif

%if "%{flavor}" == "gnu10-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%undefine mpi_flavor
%endif

%if "%{flavor}" == "gnu10-openmpi-hpc"
%{?DisOMPI1}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor openmpi
%define mpi_vers 1
%endif

%if "%{flavor}" == "gnu10-openmpi2-hpc"
%{?DisOMPI2}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor openmpi
%define mpi_vers 2
%endif

%if "%{flavor}" == "gnu10-openmpi3-hpc"
%{?DisOMPI3}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor openmpi
%define mpi_vers 3
%endif

%if "%{flavor}" == "gnu10-openmpi4-hpc"
%{?DisOMPI4}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor openmpi
%define mpi_vers 4
%endif

%if "%{flavor}" == "gnu10-mvapich2-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor mvapich2
%endif

%if "%{flavor}" == "gnu10-mpich-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor mpich
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_hpc:%{!?compiler_family:%global compiler_family gnu}}
%{?with_mpi:%{!?mpi_flavor:error "No MPI family specified!"}}

# For compatibility package names
%if "%{flavor}" == "openmpi1" && 0%{?suse_version} <= 1500
%define mpi_ext %{nil}
%else
%define mpi_ext %{?mpi_vers}
%endif

%if %{with hpc}
%{hpc_init -c %compiler_family %{?with_mpi:-m %mpi_flavor} %{?c_f_ver:-v %{c_f_ver}} %{?mpi_vers:-V %{mpi_vers}} %{?ext:-e %{ext}}}
%{?with_mpi:%global hpc_module_pname p%{pname}}
 %define my_prefix %hpc_prefix
 %define my_bindir %hpc_bindir
   %ifarch x86_64
 %define my_libdir %hpc_prefix/lib64
   %else
 %define my_libdir %hpc_libdir
   %endif
 %define my_incdir %hpc_includedir
 %define package_name   %{hpc_package_name %_vers}
 %define libname(l:s:)   lib%{pname}%{-l*}%{hpc_package_name_tail %{?_vers}}
 %define vname %{pname}_%{_vers}-hpc
%else
 %if %{without mpi}
  %define my_prefix %_prefix
  %define my_bindir %_bindir
  %define my_libdir %_libdir
  %define my_incdir %_includedir
 %else
  %define my_prefix %{_libdir}/mpi/gcc/%{mpi_flavor}%{?mpi_ext}
  %define my_suffix -%{mpi_flavor}%{?mpi_ext}
  %define my_bindir %{my_prefix}/bin
  %define my_libdir %{my_prefix}/%{_lib}/
  %define my_incdir %{my_prefix}/include/
 %endif
 %if 0%{!?package_name:1}
  %define package_name   %pname%{?my_suffix}
 %endif
 %define libname(l:s:)   lib%{pname}%{!-l:%{-s:-}}%{-l*}%{-s*}%{?my_suffix}
 %define vname %{pname}
%endif

# Run 'sh ./update_so_version.sh' when updating hdf5!
%include %{_sourcedir}/so_versions

Name:           %{package_name}
Version:        %vers
Release:        0
Summary:        Command-line programs for the HDF5 scientific data format
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            https://www.hdfgroup.org/HDF5/
Source0:        https://www.hdfgroup.org/ftp/HDF5/releases/%{pname}-%{short_ver}/%{pname}-%{src_ver}/src/%{pname}-%{src_ver}.tar.bz2
Source100:      so_versions
Source1000:     update_so_version.sh
Patch0:         hdf5-LD_LIBRARY_PATH.patch
# not really needed but we want to get noticed if hdf5 doesn' t know our host
Patch2:         hdf5-1.8.11-abort_unknown_host_config.patch
%ifarch %arm
Patch4:         hdf5-1.8.10-tests-arm.patch
%endif
Patch5:         PPC64LE-Fix-long-double-handling.patch
Patch6:         hdf5-Remove-timestamps-from-binaries.patch
# Could be ported but it's unknown if it's still needed
Patch7:         hdf5-mpi.patch
Patch8:         Disable-phdf5-tests.patch
Patch9:         Fix-error-message-not-the-name-but-the-link-information-is-parsed.patch
# Imported from Fedora, strip flags from h5cc wrapper
Patch10:        hdf5-wrappers.patch
Patch101:       H5O_fsinfo_decode-Make-more-resilient-to-out-of-bounds-read.patch
Patch102:       H5O__pline_decode-Make-more-resilient-to-out-of-bounds-read.patch
Patch103:       H5O_dtype_decode_helper-Parent-of-enum-needs-to-have-same-size-as-enum-itself.patch
Patch104:       Report-error-if-dimensions-of-chunked-storage-in-data-layout-2.patch
Patch105:       When-evicting-driver-info-block-NULL-the-corresponding-entry.patch
Patch106:       Pass-compact-chunk-size-info-to-ensure-requested-elements-are-within-bounds.patch
Patch107:       Validate-location-offset-of-the-accumulated-metadata-when-comparing.patch
Patch108:       Make-sure-info-block-for-external-links-has-at-least-3-bytes.patch
Patch109:       Hot-fix-for-CVE-2020-10812.patch
Patch110:       Compound-datatypes-may-not-have-members-of-size-0.patch
Patch111:       H5IMget_image_info-H5Sget_simple_extent_dims-does-not-exceed-array-size.patch

BuildRequires:  fdupes
%if 0%{?use_sz2}
BuildRequires:  libsz2-devel
%endif
BuildRequires:  zlib-devel
%if %{without hpc}
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
 %if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_ext}-devel
 %else
Requires:       lib%{pname}_cpp%{sonum_CXX} = %{version}
Requires:       lib%{pname}_hl_cpp%{sonum_HL_CXX} = %{version}
 %endif
Requires:       lib%{pname}-%{sonum} = %{version}
Requires:       lib%{pname}_fortran%{sonum_F} = %{version}
Requires:       lib%{pname}_hl%{sonum_HL} = %{version}
Requires:       lib%{pname}hl_fortran%{sonum_HL_F} = %{version}
%else # hpc
%hpc_requires
Requires:       %{libname -l _fortran}
%if %{without mpi}
Requires:       %{libname -l _cpp}
Requires:       %{libname -l _hl_cpp}
%endif
Requires:       %{libname -l _hl}
Requires:       %{libname -l hl_fortran}
Requires:       %{libname}
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc >= 0.2
 %if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
 %endif
%endif  # ?hpc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if "%{flavor}" == "openmpi1" && 0%{?suse_version} <= 1500
Provides:       %{pname}-openmpi = %{version}-%{release}
Obsoletes:      %{pname}-openmpi < %{version}-%{release}
%endif

%description
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the %{flavor} version utility functions for working
with HDF5 files.

%{?with_hpc:%{hpc_master_package}}

%package -n     %{libname -s %{sonum}}
Summary:        Shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname} = %{version}
Obsoletes:      %{libname} < %{version}
%{?with_hpc:Requires:       %{name}-module = %version}

%description -n %{libname -s %{sonum}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the %{flavor} version of the HDF5 runtime libraries.

%{?with_hpc:%{hpc_master_package -l -n lib%{pname}%{hpc_package_name_tail}}}

%package -n     %{libname -l _hl -s %{sonum_HL}}
Summary:        High-level shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname -l _hl} = %{version}
Obsoletes:      %{libname -l _hl} < %{version}
%{?with_hpc:Requires:       %{name}-module = %version}

%description -n %{libname -l _hl -s %{sonum_HL}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the %{flavor} version of the high-level HDF5
runtime libraries.

%{?with_hpc:%{hpc_master_package -l -n lib%{pname}_hl%{hpc_package_name_tail} -N %{pname}_hl}}

%package -n     %{libname -l _cpp -s %{sonum_CXX}}
Summary:        Shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname -l _cpp} = %{version}
Obsoletes:      %{libname -l _cpp} < %{version}
%{?with_hpc:Requires:       %{name}-module = %version}

%description -n %{libname -l _cpp -s %{sonum_CXX}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the HDF5 runtime libraries.

%{?with_hpc:%{hpc_master_package -l -n lib%{pname}_cpp%{hpc_package_name_tail} -N %{pname}_cpp}}

%package -n     %{libname -l _hl_cpp -s %{sonum_HL_CXX}}
Summary:        High-level shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname -l _hl_cpp} = %{version}
Obsoletes:      %{libname -l _hl_cpp} < %{version}
%{?with_hpc:Requires:       %{name}-module = %version}

%description -n %{libname -l _hl_cpp -s %{sonum_HL_CXX}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the the high-level HDF5 runtime libraries.

%{?with_hpc:%{hpc_master_package -l -n lib%{pname}_hl_cpp%{hpc_package_name_tail} -N %{pname}_hl_cpp}}

%package -n     %{libname -l _fortran -s %{sonum_F}}
Summary:        Shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname -l _fortran} = %{version}
Obsoletes:      %{libname -l _fortran} < %{version}
%{?with_hpc:Requires:       %{name}-module = %version}

%description -n %{libname -l _fortran -s %{sonum_F}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the %{flavor} version of the HDF5 runtime libraries.

%{?with_hpc:%{hpc_master_package -l -n lib%{pname}_fortran%{hpc_package_name_tail} -N %{pname}_fortran}}

%package -n     %{libname -l hl_fortran -s %{sonum_HL_F}}
Summary:        High-level shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname -l hl_fortran} = %{version}
Obsoletes:      %{libname -l hl_fortran} < %{version}
%{?with_hpc:Requires:       %{name}-module = %version}

%description -n %{libname -l hl_fortran -s %{sonum_HL_F}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the %{flavor} version of the high-level HDF5
runtime libraries.

%{?with_hpc:%{hpc_master_package -l -n lib%{pname}_hl_fortran%{hpc_package_name_tail} -N %{pname}hl_fortran}}

%package -n %{pname}-devel-data
Summary:        Development data files for %{name}
Group:          Development/Libraries/Other

%description -n %{pname}-devel-data
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains generic files needed to create projects that use
any version of HDF5.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{libname -l _cpp -s %{sonum_CXX}} = %{version}
Requires:       %{libname -l _hl_cpp -s %{sonum_HL_CXX}} = %{version}
Requires:       %{name} = %{version}
%{!?with_hpc:Requires:       %{pname}-devel-data = %{version}}
Requires:       zlib-devel
%if 0%{?use_sz2}
Requires:       libsz2-devel
%endif
Requires:       %{libname -s %{sonum}} = %{version}
# Required by Fortran programs?
Requires:       %{libname -l _fortran -s %{sonum_F}} = %{version}
Requires:       %{libname -l _hl -s %{sonum_HL}} = %{version}
Requires:       %{libname -l hl_fortran -s %{sonum_HL_F}} = %{version}
%{?with_hpc:%hpc_requires_devel}
%if "%{flavor}" == "openmpi1" && 0%{?suse_version} <= 1500
Provides:       %{pname}-openmpi-devel = %{version}-%{release}
Obsoletes:      %{pname}-openmpi-devel < %{version}-%{release}
%endif

%description devel
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains all files needed to create projects that use
the %{flavor} version of HDF5.

%{?with_hpc:%{hpc_master_package devel}}

%package  devel-static
Summary:        Static development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}

%description devel-static
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package provides the static libraries for the %{flavor} version of HDF5.

%package -n %{vname}-examples
Summary:        Examples for %{name}
Group:          Documentation/Other

%description -n %{vname}-examples
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package provides examples of HDF5 library use.

%{?!with_mpi:%{?with_hpc:%{hpc_master_package -n %{pname}-hpc-examples -M %{vname}-examples}}}

%if %{with hpc}
%package module
Summary:        Module files for %{name}
Group:          Development/Libraries/Parallel
Provides:       %{name}-module = %version
Requires:       lua-lmod

%description module
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the environment module needed for the HDF5
library packages.
%endif

%prep
%{?with_hpc: %hpc_debug}
%setup -q -n %{pname}-%{version}
%patch0 -p1 -b .LD_LIBRARY_PATH
%patch2 -p0 -b .abort_unknown_host_config
%ifarch %arm
%patch4 -p0 -b .tests-arm
%endif
%patch5 -p1
%patch6 -p1
# %%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1

%if %{without hpc}
# baselibs looks different for different flavors - generate it on the fly
cat >  %{_sourcedir}/baselibs.conf <<EOF
libhdf5-%{sonum}%{?my_suffix}
libhdf5_hl%{sonum_HL}%{?my_suffix}
libhdf5_fortran%{sonum_F}%{?my_suffix}
libhdf5hl_fortran%{sonum_HL_F}%{?my_suffix}
libhdf5_cpp%{sonum_CXX}%{?my_suffix}
libhdf5_hl_cpp%{sonum_HL_CXX}%{?my_suffix}
hdf5%{?my_suffix}-devel
   requires %{?my_suffix}-<targettype>
   requires "libhdf5-%{sonum}%{?my_suffix}-<targettype> = <version>"
   requires "libhdf5_hl%{sonum_HL}%{?my_suffix}-<targettype> = <version>"
   requires "libhdf5_fortran%{sonum_F}%{?my_suffix}-<targettype> = <version>"
   requires "libhdf5hl_fortran%{sonum_HL_F}%{?my_suffix}-<targettype> = <version>"
   requires "libhdf5_cpp%{sonum_CXX}%{?my_suffix}-<targettype> = <version>"
   requires "libhdf5_hl_cpp%{sonum_HL_CXX}%{?my_suffix}-<targettype> = <version>"
EOF
%endif

%build

%{?with_hpc:%hpc_setup}
%{?with_hpc:%hpc_debug}

export CC=gcc
export CXX=g++
export F9X=gfortran
export CFLAGS="%{optflags}"
%ifarch %arm
# we want to have useful H5_CFLAGS on arm too
test -e config/linux-gnueabi || cp config/linux-gnu config/linux-gnueabi
%endif

# NOTE: --enable-unsupported is required when --enable-fortran
# and/or --enable-cxx is enabled along with --enable-threadsafe.
# Building with thise combination results in thread-safe C
# libraries and non-thread-safe fotran and/or C++ libraries. So
# you have to explicitly allow building the thread-safe C
# library and the non-thread-safe C++ and fortran libraries in
# order to make sure people don't assume that their fotran or
# C++ code is thread-safe.  Since our users are going to be
# accessing this through other programs, this doesn't matter.

%if %{without hpc}
 %if  %{with mpi}
export CC="%{my_bindir}/mpicc"
export CXX="%{my_bindir}/mpicxx"
export FC="%{my_bindir}/mpif90"
export F77="%{my_bindir}/mpif77"
export LD_LIBRARY_PATH="%{my_libdir}"
 %endif
%configure \
 %if %{with mpi}
  --prefix=%{my_prefix} \
  --exec-prefix=%{_prefix} \
  --bindir=%{my_bindir} \
  --libdir=%{my_libdir} \
  --includedir=%{my_incdir} \
  --datadir=%{_datadir} \
 %endif
  --docdir=%{_docdir}/%{name} \
%else # hpc
%global _hpc_exec_prefix %hpc_exec_prefix
%global hpc_exec_prefix %_prefix
 %if %{with mpi}
export CC=mpicc
export CXX=mpicxx
export F77=mpif77
export FC=mpif90
export MPICC=mpicc
export MPIFC=mpifc
export MPICXX=mpicxx
 %endif
%hpc_configure \
%define hpc_exec_prefix %{expand:%_hpc_exec_prefix}
%endif # ?hpc
  --disable-hltools \
  --disable-dependency-tracking \
  --enable-fortran \
  --enable-unsupported \
  --enable-hl \
  --enable-shared \
  --enable-threadsafe \
  --enable-build-mode=production \
%if %{with mpi}
  --enable-parallel \
%endif
  --enable-cxx \
%if 0%{?use_sz2}
  --with-szlib \
%endif
  --with-pthread \
  %{nil}

# Remove timestamp/buildhost/kernel version
export SDE_DATE=$(date -d @${SOURCE_DATE_EPOCH} -u)
export UNAME_M_O=$(uname -m -o)
sed -i -e "s/\(Configured on: \).*/\1 $SDE_DATE/" \
       -e "s#\(Uname information: \).*#\1 $UNAME_M_O#" \
       -e "s/\(Configured by: \).*/\1 abuild@OBS/" \
       src/libhdf5.settings

make V=1 %{?_smp_mflags}

%install
%{?with_hpc:%hpc_setup}
%{?with_hpc:%hpc_debug}

make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name "*.la" -delete -print

%if %{without mpi}

%if %{with hpc}
# copy to versioned subdir
install -m 755 -d %{buildroot}%{_prefix}/share/%{version}
install -m 755 -d %{buildroot}%{_prefix}/share/hdf5_examples
mv %{buildroot}%{_prefix}/lib/hpc/*/hdf5/*/share/hdf5_examples/* \
    %{buildroot}%{_prefix}/share/%{version}/
mv %{buildroot}%{_prefix}/share/%{version} \
    %{buildroot}%{_prefix}/share/hdf5_examples
%else
# rpm macro for version checking
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.hdf5 <<EOF
#
# RPM macros for hdf5 packaging
#
%_hdf5_sonum  %{sonum}
%_hdf5_version  %{version}
EOF
%endif

%else
# delete examples from parallel builds
find  %{buildroot} -type d -name "hdf5_examples" -exec rm -rf {} +;
%endif

%fdupes -s %{buildroot}/%{_datadir}

%if %{with hpc}
%{hpc_write_pkgconfig -n hdf5 -l hdf5}
%{hpc_write_pkgconfig -n hdf5_hl -l hdf5_hl}
%{hpc_write_pkgconfig -n hdf5_fortran -l hdf5_fortran}
%{hpc_write_pkgconfig -n hdf5_hl_fortran -l hdf5hl_fortran}
%{hpc_write_pkgconfig -n hdf5_cpp -l hdf5_cpp}
%{hpc_write_pkgconfig -n hdf5_hl_cpp -l hdf5_hl_cpp}

%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} compiler toolchain."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} toolchain"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY:0}"
module-whatis "%{url}"

set     version                     %{version}

prepend-path    PATH                %{hpc_bindir}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}

setenv          %{hpc_upcase %pname}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase %pname}_BIN        %{hpc_bindir}
setenv          %{hpc_upcase %pname}_LIB        %{hpc_libdir}

if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    LIBRARY_PATH        %{hpc_libdir}
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}
prepend-path    INCLUDE             %{hpc_includedir}
%hpc_modulefile_add_pkgconfig_path

setenv          %{hpc_upcase %pname}_INC        %{hpc_includedir}
}

family "%pname"

EOF
%endif

%if %{with check}
%check
 %if 0%{?qemu_user_space_build}
# default timeout is 1200 seconds
export HDF5_ALARM_SECONDS=3600
 %endif
 %if %{with mpi}
export HDF5_Make_Ignore=yes
 %endif
%{?with_hpc:%hpc_setup}
 %ifarch ppc ppc64 ppc64le aarch64
  make %{?_smp_mflags} check || { echo "Ignore transient make check failures for PowerPC or aarch64. boo#1058563"; }
 %else
  %if "%{?mpi_flavor}" != "mpich" || ("%_arch" != "s390" && "%_arch" != "s390x")
    make %{?_smp_mflags} check
  %endif
 %endif
%endif

%post -n %{libname -l _cpp -s %{sonum_CXX}} -p /sbin/ldconfig
%postun -n %{libname -l _cpp -s %{sonum_CXX}} -p /sbin/ldconfig
%post -n %{libname -l _hl_cpp -s %{sonum_HL_CXX}} -p /sbin/ldconfig
%postun -n %{libname -l _hl_cpp -s %{sonum_HL_CXX}} -p /sbin/ldconfig
%post -n %{libname -s %{sonum}} -p /sbin/ldconfig
%postun -n %{libname -s %{sonum}} -p /sbin/ldconfig
%post -n %{libname -l _hl -s %{sonum_HL}} -p /sbin/ldconfig
%postun -n %{libname -l _hl -s %{sonum_HL}} -p /sbin/ldconfig
%post -n %{libname -l _fortran -s %{sonum_F}} -p /sbin/ldconfig
%postun -n %{libname -l _fortran -s %{sonum_F}} -p /sbin/ldconfig
%post -n %{libname -l hl_fortran -s %{sonum_HL_F}} -p /sbin/ldconfig
%postun -n %{libname -l hl_fortran -s %{sonum_HL_F}} -p /sbin/ldconfig

%if %{with hpc}
%postun module
%hpc_module_delete_if_default
%endif

%if 0%{?sle_version} > 120200 || 0%{?suse_version} > 1320
%define mylicense %license
%else
%define mylicense %doc
%endif

%if %{without mpi}
%files -n %{vname}-examples
%{?with_hpc:%dir %{_prefix}/share/hdf5_examples}
%{_prefix}/share/hdf5_examples%{?with_hpc:/%{version}}

%if %{without hpc}
%files -n %{pname}-devel-data
%{_rpmconfigdir}/macros.d/macros.hdf5
%endif
%endif # ?mpi

%files -n %{name}
%{?with_hpc:%dir %my_bindir}
%{my_bindir}/h5clear
%{my_bindir}/h5copy
%{my_bindir}/h5debug
%{my_bindir}/h5diff
%{my_bindir}/h5dump
%{my_bindir}/h5format_convert
%{my_bindir}/h5import
%{my_bindir}/h5jam
%{my_bindir}/h5ls
%{my_bindir}/h5mkgrp
%if %{with mpi}
%{my_bindir}/ph5diff
%{my_bindir}/h5perf
%{my_bindir}/perf
%endif
%{my_bindir}/h5perf_serial
%{my_bindir}/h5redeploy
%{my_bindir}/h5repack
%{my_bindir}/h5repart
%{my_bindir}/h5stat
%{my_bindir}/h5unjam

%files -n %{libname -s %{sonum}}
%doc ACKNOWLEDGMENTS README.md
%mylicense COPYING
##
%if %{without mpi}
%doc release_docs/HISTORY-1_10_0-1_12_0.txt
%doc release_docs/RELEASE.txt
%endif
%defattr(0755,root,root)
%{?with_hpc:%hpc_dirs}
%{my_libdir}/libhdf5.so.%{sonum}
%{my_libdir}/libhdf5.so.%{sonum}.*

%files -n %{libname -l _hl -s %{sonum_HL}}
%mylicense COPYING
%defattr(0755,root,root)
%{?with_hpc:%hpc_dirs}
%{my_libdir}/libhdf5_hl.so.%{sonum_HL}
%{my_libdir}/libhdf5_hl.so.%{sonum_HL}.*

%files -n %{libname -l _cpp -s %{sonum_CXX}}
%mylicense COPYING
%defattr(0755,root,root)
%{?with_hpc:%hpc_dirs}
%{my_libdir}/libhdf5_cpp.so.%{sonum_CXX}
%{my_libdir}/libhdf5_cpp.so.%{sonum_CXX}.*

%files -n %{libname -l _hl_cpp -s %{sonum_HL_CXX}}
%mylicense COPYING
%defattr(0755,root,root)
%{?with_hpc:%hpc_dirs}
%{my_libdir}/libhdf5_hl_cpp.so.%{sonum_HL_CXX}
%{my_libdir}/libhdf5_hl_cpp.so.%{sonum_HL_CXX}.*

%files -n %{libname -l _fortran -s %{sonum_F}}
%mylicense COPYING
%defattr(0755,root,root)
%{?with_hpc:%hpc_dirs}
%{my_libdir}/libhdf5_fortran.so.%{sonum_F}
%{my_libdir}/libhdf5_fortran.so.%{sonum_F}.*

%files -n %{libname -l hl_fortran -s %{sonum_HL_F}}
%mylicense COPYING
%defattr(0755,root,root)
%{?with_hpc:%hpc_dirs}
%{my_libdir}/libhdf5hl_fortran.so.%{sonum_HL_F}
%{my_libdir}/libhdf5hl_fortran.so.%{sonum_HL_F}.*

%if %{with hpc}
%files module
%hpc_modules_files
%endif

%files devel
##
%{?with_hpc:%dir %{my_incdir}}
%doc release_docs/HISTORY-1_10_0-1_12_0.txt
%doc release_docs/RELEASE.txt
%doc ACKNOWLEDGMENTS README.md
%{?with_hpc:%{hpc_pkgconfig_file -n hdf5}}
%{?with_hpc:%{hpc_pkgconfig_file -N -n hdf5_hl}}
%{?with_hpc:%{hpc_pkgconfig_file -N -n hdf5_fortran}}
%{?with_hpc:%{hpc_pkgconfig_file -N -n hdf5_hl_fortran}}
%{?with_hpc:%{hpc_pkgconfig_file -N -n hdf5_cpp}}
%{?with_hpc:%{hpc_pkgconfig_file -N -n hdf5_hl_cpp}}
%{my_bindir}/h5c++
%if %{without mpi}
%{my_bindir}/h5cc
%{my_bindir}/h5fc
%else
%{my_bindir}/h5pcc
%{my_bindir}/h5pfc
%endif
%{my_incdir}/*.h
%{my_libdir}/*.so
%{my_libdir}/*.settings
%{my_incdir}/*.mod

%files devel-static
%{my_libdir}/*.a

%changelog
