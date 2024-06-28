#
# spec file
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2004-2005 The Trustees of Indiana University and Indiana
#                         University Research and Technology
#                         Corporation.  All rights reserved.
# Copyright (c) 2004-2005 The University of Tennessee and The University
#                         of Tennessee Research Foundation.  All rights
#                         reserved.
# Copyright (c) 2004-2005 High Performance Computing Center Stuttgart,
#                         University of Stuttgart.  All rights reserved.
# Copyright (c) 2004-2005 The Regents of the University of California.
#                         All rights reserved.
# Copyright (c) 2006-2016 Cisco Systems, Inc.  All rights reserved.
# Copyright (c) 2013      Mellanox Technologies, Inc.
#                         All rights reserved.
# Copyright (c) 2015      Research Organization for Information Science
#                         and Technology (RIST). All rights reserved.
# Copyright (c) 2003, The Regents of the University of California, through
# Lawrence Berkeley National Laboratory (subject to receipt of any
# required approvals from the U.S. Dept. of Energy).  All rights reserved.
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

# Static libraries are disabled by default
# for non HPC builds
# To enable them, simply uncomment:
# % define build_static_devel 1

%global pname openmpi
%define _vers 4_1_6
%define m_f_ver 4
%bcond_with ringdisabled

%if "%flavor" == ""
ExclusiveArch:  do_not_build
 %{bcond_with hpc}
 %define package_name %pname%{m_f_ver}
%else
 # Trickery for OBS Staging. If _with_ringdisabled is set
 # we only want to build the flavors required by other rings packages.
 # Do not build any other ones
 %if %{with ringdisabled}
  %if "%flavor" != "standard"
ExclusiveArch:  do_not_build
  %endif
 %endif

  %if "%flavor" == "standard" || "%flavor" == "testsuite"
    %define package_name   %{pname}%{m_f_ver}
    %bcond_with hpc
    %if "%flavor" == "testsuite"
      %define testsuite 1
    %endif
  %else
    %bcond_without hpc
# Needs to be defined here to avoid hen/egg problem with test packages.
    %define package_name %{pname}_%{_vers}-%{compiler_family}%{?c_f_ver}-hpc
    %define build_static_devel 1
  %endif
%endif

%if "%flavor" == "gnu-hpc"
%define compiler_family gnu
%undefine c_f_ver
%endif

%if "%flavor" == "gnu7-hpc"
%define compiler_family gnu
%define c_f_ver 7
%endif

%if "%flavor" == "gnu-hpc-testsuite"
%define compiler_family gnu
%undefine c_f_ver
%define testsuite 1
%endif

%if "%flavor" == "gnu7-hpc-testsuite"
%define compiler_family gnu
%define c_f_ver 7
%define testsuite 1
%endif

%if 0%{?suse_version} >= 1320
%ifarch aarch64 %power64 x86_64 s390x
%define with_ucx 1
%endif
%endif

# Detect whether we are the default openMPI implemantation or not
%if "%{flavor}" == "standard" && (%{suse_version} > 1500 || 0%{?sle_version} > 150300)
%define default_openmpi 1
%else
%define default_openmpi 0
%endif

%if %{with hpc}
%{!?compiler_family:%global compiler_family gnu}
%{hpc_init -M -c %compiler_family %{?c_f_ver:-v %{c_f_ver}} -m openmpi %{?mpi_f_ver:-V %{mpi_f_ver}}}

%global hpc_openmpi_dep_version %(VER=%m_f_ver; echo -n ${VER})
%global hpc_openmpi_dir openmpi%{hpc_openmpi_dep_version}
%global hpc_openmpi_pack_version %{hpc_openmpi_dep_version}
%{bcond_without pmix}
%{bcond_without hwloc}
ExcludeArch:    i586 %arm s390
%else
%{bcond_with pmix}
%{bcond_with hwloc}
%endif

%define git_ver .0.439b23db6288

#############################################################################
#
# Preamble Section
#
#############################################################################

Name:           %{package_name}%{?testsuite:-testsuite}
Version:        4.1.6
Release:        0
Summary:        An implementation of MPI/SHMEM (Version %{m_f_ver})
License:        BSD-3-Clause
Group:          Development/Libraries/Parallel
URL:            https://www.open-mpi.org/
Source0:        openmpi-%{version}%{git_ver}.tar.bz2
Source2:        openmpi4-rpmlintrc
Source3:        macros.hpc-openmpi
Source4:        mpivars.sh
Source5:        mpivars.csh
Patch1:         orted-mpir-add-version-to-shared-library.patch
Patch2:         btl-openib-Add-VF-support-for-ConnectX-4-5-and-6.patch
Provides:       mpi
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  hostname
BuildRequires:  libevent-devel
BuildRequires:  libfabric-devel
BuildRequires:  libibumad-devel
BuildRequires:  libibverbs-devel
BuildRequires:  libtool
# net-tools is required to run hostname
BuildRequires:  net-tools
%if 0%{?testsuite}
BuildArch:      noarch
BuildRequires:  %{package_name} = %{version}
%endif
%if 0%{?with_ucx}
BuildRequires:  libucm-devel
BuildRequires:  libucp-devel
BuildRequires:  libucs-devel
BuildRequires:  libuct-devel
%endif
%if %{with hwloc}
BuildRequires:  hwloc-devel
%endif
%if %{with pmix}
BuildRequires:  pmix-devel
%endif
%if %{without hpc}
BuildRequires:  Modules
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  mpi-selector
Requires:       mpi-selector
Requires(preun):mpi-selector
Requires:       %{package_name}-libs = %{version}
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
%if 0%{!?testsuite:1}
Requires:       lib%{package_name} = %{version}
%endif
%hpc_requires
%endif

%ifarch x86_64
BuildRequires:  libnuma-devel
BuildRequires:  libpsm2-devel
BuildRequires:  numactl
%endif

Requires:       openmpi-runtime-config
Recommends:     openmpi%{m_f_ver}-config
%if 0%{?default_openmpi}
Provides:       openmpi = %{version}
%endif
# OpenMPI requires ssh (or rsh) to run even on a single host
# Force ssh to make sure the install works out of the box
Requires:       openssh

%if %{without hpc}
%define mpi_prefix %{_libdir}/mpi/gcc/openmpi%{m_f_ver}

%define mpi_bindir %{mpi_prefix}/bin
%define mpi_libdir %{mpi_prefix}/%{_lib}
%define mpi_datadir %{mpi_prefix}/share
%define mpi_helpdir %{mpi_datadir}/%{pname}%{m_f_ver}
%define mpi_includedir %{mpi_prefix}/include
%define mpi_mandir %{mpi_prefix}/share/man
%else
%define mpi_prefix %hpc_prefix

%define mpi_bindir %hpc_bindir
%define mpi_libdir %hpc_libdir
%define mpi_datadir %hpc_datadir
%define mpi_helpdir %{mpi_datadir}/openmpi
%define mpi_includedir %hpc_includedir
%define mpi_mandir %hpc_mandir

%endif

%description
%if 0%{?testsuite}
This package is just needed to run the testsuite and does not contain
anything interesting.
%else
OpenMPI is an implementation of the Message Passing Interface, a
standardized API typically used for parallel and/or distributed
computing. OpenMPI is the merged result of four prior implementations
where the team found for them to excel in one or more areas,
such as latency or throughput.

OpenMPI also includes an implementation of the OpenSHMEM parallel
programming API, which is a Partitioned Global Address Space (PGAS)
abstraction layer providing inter-process communication using
one-sided communication techniques.

This package provides general tools (mpirun, mpiexec, etc.) and the
Module Component Architecture (MCA) base and plugins necessary for
running Open MPI/OpenSHMEM version %{m_f_ver} jobs.
%endif

%if 0%{!?testsuite:1}
%package        %{!?with_hpc:libs}%{?with_hpc:-n lib%{name}}
Summary:        OpenMPI runtime libraries for OpenMPI %{?with_hpc:HPC} version %{version}
Group:          System/Libraries
Requires:       %{name} = %{version}
%if 0%{?default_openmpi}
Provides:       openmpi-libs = %{version}
%endif
%{?with_hpc:%hpc_requires}

%description %{!?with_hpc:libs}%{?with_hpc:-n lib%{name}}
OpenMPI is an implementation of the Message Passing Interface, a
standardized API typically used for parallel and/or distributed
computing. OpenMPI is the merged result of four prior implementations
where the team found for them to excel in one or more areas,
such as latency or throughput.

OpenMPI also includes an implementation of the OpenSHMEM parallel
programming API, which is a Partitioned Global Address Space (PGAS)
abstraction layer providing inter-process communication using
one-sided communication techniques.

This package provides the Open MPI/OpenSHMEM version %{m_f_ver}
shared libraries.

%package        devel
Summary:        SDK for openMPI %{?with_hpc:HPC} version %{version}
Group:          Development/Libraries/Parallel
Requires:       libibumad-devel
Requires:       libibverbs-devel
%if %{without hpc}
Requires:       libstdc++-devel
%if 0%{?default_openmpi}
Provides:       openmpi-devel = %{version}
%endif
%else
%hpc_requires_devel
%endif
Requires:       %{name} = %{version}

%description devel
OpenMPI is an implementation of the Message Passing Interface, a
standardized API typically used for parallel and/or distributed
computing. OpenMPI is the merged result of four prior implementations
where the team found for them to excel in one or more areas,
such as latency or throughput.

OpenMPI also includes an implementation of the OpenSHMEM parallel
programming API, which is a Partitioned Global Address Space (PGAS)
abstraction layer providing inter-process communication using
one-sided communication techniques.

This package provides the development files for Open MPI/OpenSHMEM
version %{m_f_ver}, such as wrapper compilers and header files for
MPI/OpenSHMEM development.

%package docs
Summary:        Documentation for Open MPI/SHMEM %{?with_hpc:HPC} version %{version}
Group:          Documentation/Man
Requires:       %{name} = %{version}

%description docs
OpenMPI is an implementation of the Message Passing Interface, a
standardized API typically used for parallel and/or distributed
computing. OpenMPI is the merged result of four prior implementations
where the team found for them to excel in one or more areas,
such as latency or throughput.

OpenMPI also includes an implementation of the OpenSHMEM parallel
programming API, which is a Partitioned Global Address Space (PGAS)
abstraction layer providing inter-process communication using
one-sided communication techniques.

This subpackage provides the documentation for Open MPI/OpenSHMEM.

%package        macros-devel
Summary:        Macros for openMPI version %{version}
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}
# Make sure no two openmpi macro file can be installed at once
Provides:       %{pname}-macros-provider = %{version}
Conflicts:      otherproviders(%{pname}-macros-provider)
# Conflict (without providing) with the older openmpi-hpc-macros-devel flag
# to avoid issue with older packages
Conflicts:      otherproviders(%{pname}-hpc-macros-devel)

%if 0%{?default_openmpi}
Provides:       openmpi-macros-devel = %{version}
%endif

%description macros-devel
Macros for building RPM packages for OpenMPI version %{version}.

%if 0%{?build_static_devel}
%package        devel-static
Summary:        Static libraries for openMPI %{?with_hpc:HPC} version %{version}
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}
%if 0%{?default_openmpi}
Provides:       openmpi-devel-static = %{version}
%endif

%description devel-static
OpenMPI is an implementation of the Message Passing Interface, a
standardized API typically used for parallel and/or distributed
computing. OpenMPI is the merged result of four prior implementations
where the team found for them to excel in one or more areas,
such as latency or throughput.

This RPM contains the static library files, which are packaged separately from
the dynamic library and headers.
%endif

%if %{without hpc}
%package        -n %{pname}%{m_f_ver}-config
Summary:        Runtime configuration files for openMPI %{?with_hpc:HPC} version %{version}
Group:          Development/Libraries/Parallel
Provides:       openmpi-runtime-config = %{version}
Conflicts:      otherproviders(openmpi-runtime-config)
%if %{without pmix}
# OpenMPI4 is PMIx enabled
Provides:       pmix-runtime-config = %{version}
Conflicts:      otherproviders(pmix-runtime-config)
%endif

%description -n %{pname}%{m_f_ver}-config
OpenMPI is an implementation of the Message Passing Interface, a
standardized API typically used for parallel and/or distributed
computing. OpenMPI is the merged result of four prior implementations
where the team found for them to excel in one or more areas,
such as latency or throughput.

This RPM contains the configuration files for OpenMPI runtime (Version 3).
%endif

%if %{with hpc}
%{hpc_master_package -L -a}
%{hpc_master_package -l}
%{hpc_master_package devel}
%{hpc_master_package docs}
%{hpc_master_package macros-devel}
%{hpc_master_package -a devel-static}
%endif # ?with_hpc
%endif # !testsuite

%if "%(echo %version | tr '.' '_')" != "%_vers"
%{error: Fix _vers variable to match package version!}
%endif

#############################################################################
#
# Prepatory Section
#
#############################################################################
%prep
echo FLAVOR %{flavor}
%if %{with hpc}
echo with HPC
%endif
%if %{without hpc}
echo without HPC
%endif
%autosetup -p0 -n  openmpi-%{version}%{git_ver}

%if %{without hpc}
cat > %{_sourcedir}/baselibs.conf  <<EOF
openmpi%{m_f_ver}-libs
EOF
%endif

# Live patch the VERSION file
sed -i -e 's/^greek=.*$/greek=%{git_ver}/' -e 's/^repo_rev=.*$/repo_rev=%{version}%{git_ver}/' \
       -e 's/^date=.*$/date="OpenMPI %{version} Distribution for SUSE"/' VERSION

#############################################################################
#
# Build Section
#
#############################################################################

%build
# make build reproducible
export USER=OBS
export HOSTNAME=OBS
# OBS sets SOURCE_DATE_EPOCH
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%{?with_hpc:%hpc_debug}
./autogen.pl --force
%if %{with hpc}
%{hpc_setup}
%{hpc_configure} \
%else
%{configure} \
           --prefix="%{mpi_prefix}" \
           --exec-prefix="%{mpi_prefix}" \
           --bindir="%{mpi_bindir}" \
           --datadir="%{mpi_datadir}" \
           --includedir="%{mpi_includedir}" \
           --libdir="%{mpi_libdir}" \
           --mandir="%{mpi_mandir}" \
%endif
           %{?build_static_devel:--enable-static}  \
           %{!?build_static_devel:--disable-static}  \
           --enable-builtin-atomics \
           --with-libltdl=%{_prefix} \
           --with-verbs \
           --with-libfabric \
           --enable-mpi-thread-multiple \
           --disable-wrapper-rpath \
           --with-slurm \
	   --with-libevent=external \
%if %{with hwloc}
	   --with-hwloc=external \
%endif
%if %{with pmix}
	   --with-pmix=external \
%endif
%if 0%{?with_ucx}
           --with-ucx \
           --with-ucx-libdir=/usr/%_lib \
%endif
%ifarch x86_64
           --with-psm2 \
%endif
           --disable-silent-rules \
           --enable-mpirun-prefix-by-default \
           --with-package-string="Open MPI Distribution for SUSE"  \
           --disable-wrapper-runpath
make %{?_smp_mflags}

%if 0%{?testsuite}
%check
make check

%install

%files
%defattr(-, root, root)
%doc README
%doc test/util/test-suite.log

%else # ?testsuite

#############################################################################
#
# Install Section
#
#############################################################################

%install
%{?with_hpc:%{hpc_setup_compiler}}
make install DESTDIR="%buildroot"

# sanitize .la files
list="$(find %{buildroot} -name "*.la" -printf "%%h\n" | sort | uniq)"
for dir in ${list}
do
    deps="${deps} -L${dir##%{buildroot}}"
done
for dir in ${list}
do
%if !0%{?build_static_devel}
    rm -f ${dir}/*.la
%else
    for file in ${dir}/*.la
    do
        sed -i -e "s@ [^[:space:]]*home[^[:space:]\']*@${deps}@" \
            -e "s@ [^[:space:]]*home[^[:space:]\']*@@g" \
            -e "s@-L.*.libs @@g" ${file}
    done
%endif
done
##even with disable static this one gets generated
%{!?build_static_devel:rm -f %{buildroot}%{mpi_libdir}/libvt-pomp.a}

# GCC 5 builds the ignore-tkr extension and there is no way to
# turn that off
rm -f %{buildroot}%{mpi_libdir}/mpi_ext.mod

%fdupes %{buildroot}%{mpi_mandir}
%fdupes %{buildroot}%{mpi_datadir}
%fdupes %{buildroot}%{mpi_libdir}/pkgconfig

%if %{without hpc}
# make and install mpivars files
sed -e 's,prefix,%{mpi_prefix},g' -e 's,libdir,%{mpi_libdir},g' %{SOURCE4} \
    > %{buildroot}%{mpi_bindir}/mpivars.sh
sed -e 's,prefix,%{mpi_prefix},g' -e 's,libdir,%{mpi_libdir},g' %{SOURCE5} \
    > %{buildroot}%{mpi_bindir}/mpivars.csh

mkdir -p %{buildroot}%{_datadir}/modules/gnu-openmpi
cat << EOF > %{buildroot}%{_datadir}/modules/gnu-openmpi/%{version}
#%%Module
proc ModulesHelp { } {
        global dotversion
        puts stderr "\tLoads the gnu - openmpi %{version}  Environment"
}

module-whatis  "Loads the gnu openmpi %{version} Environment."
conflict gnu-openmpi
prepend-path PATH %{mpi_bindir}
prepend-path INCLUDE %{mpi_includedir}
prepend-path INCLUDE %{mpi_libdir}
prepend-path MANPATH %{mpi_mandir}
prepend-path LD_LIBRARY_PATH %{mpi_libdir}

EOF

mkdir -p %{buildroot}%{_rpmmacrodir}
cat <<EOF >%{buildroot}%{_rpmmacrodir}/macros.openmpi
#
# openmpi
#
%openmpi_prefix %{mpi_prefix}
%setup_openmpi  source %{mpi_bindir}/mpivars.sh

%openmpi_requires Requires: %{name}-libs
%openmpi_devel_requires Requires: %{name}-devel

EOF
%else
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
module-whatis "Description: %{SUMMARY:0}"
module-whatis "URL: %{url}"

set     version                     %{version}

setenv          MPI_DIR             %{hpc_mpi_install_path}
prepend-path    PATH                %{hpc_bindir}
prepend-path    MANPATH             %{hpc_mandir}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}
prepend-path    MODULEPATH          %{hpc_modulepath}
%{hpc_modulefile_add_pkgconfig_path}

family "MPI"
EOF
cat <<EOF >  %{buildroot}/%{mpi_bindir}/mpivars.sh
%hpc_setup_compiler
module load %{hpc_mpi_family}%{?pack_suff}/%{version}
EOF
sed -e "s/export/setenv/" -e "s/=/ /" \
    %{buildroot}/%{mpi_bindir}/mpivars.sh > \
    %{buildroot}/%{mpi_bindir}/mpivars.csh
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmmacrodir}
cp %{S:3} %{buildroot}%{_rpmmacrodir}

# Drop the files that should go into %{pname}-config as we only package them
# in the non HPC build
rm -f %{buildroot}%{_sysconfdir}/openmpi-default-hostfile
rm -f %{buildroot}%{_sysconfdir}/openmpi-mca-params.conf
rm -f %{buildroot}%{_sysconfdir}/openmpi-totalview.tcl
%if %{without pmix}
rm -f %{buildroot}%{_sysconfdir}/pmix-mca-params.conf
%endif
%endif

%if %{without hpc}
%post
# Always register. We might be already registered in the case of an udate
# but mpi-selector handles it fine
/usr/bin/mpi-selector \
        --register %{name} \
        --source-dir %{mpi_bindir} \
        --yes

%preun
# Only unregister when uninstalling
if [ "$1" = "0" ]; then
	/usr/bin/mpi-selector --unregister %{name} --yes
	# Deregister the default if we are uninstalling it
	if [ "$(/usr/bin/mpi-selector --system --query)" = "%{name}" ]; then
		/usr/bin/mpi-selector --system --unset --yes
	fi
fi

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig
%else #!?with_hpc
# make it default
%post -n lib%{name} -p /sbin/ldconfig
%postun -n lib%{name} -p /sbin/ldconfig

%postun
%hpc_module_delete_if_default
%endif #!?with_hpc

%files
%defattr(-, root, root)
%doc NEWS README
%license LICENSE
%dir %{mpi_prefix}
%dir %{mpi_bindir}
%dir %{mpi_libdir}
%dir %{mpi_datadir}
%dir %{mpi_mandir}
%{mpi_bindir}/mpivars.csh
%{mpi_bindir}/mpivars.sh

%if %{without hpc}
%dir %{_libdir}/mpi
%dir %{_libdir}/mpi/gcc
%dir %{_datadir}/modules/gnu-openmpi
%{_datadir}/modules/gnu-openmpi/%{version}
%else # with hpc
%hpc_mpi_dirs
%hpc_modules_files
%endif # with hpc
#
%{mpi_bindir}/mpirun
%{mpi_bindir}/ompi-clean
%{mpi_bindir}/ompi-server
%{mpi_bindir}/ompi_info
%{mpi_bindir}/orte-clean
%{mpi_bindir}/orte-info
%{mpi_bindir}/orte-server
%{mpi_bindir}/orted
%{mpi_bindir}/orterun

%if 0%{?with_ucx}
%{mpi_bindir}/oshmem_info
%{mpi_bindir}/oshrun
%{mpi_bindir}/shmemrun
%endif

%if %{without hpc}
%{mpi_bindir}/aggregate_profile.pl
%{mpi_bindir}/profile2mat.pl
%endif

%dir %{mpi_datadir}/openmpi
%dir %{mpi_datadir}/openmpi/amca-param-sets
%{mpi_datadir}/openmpi/amca-param-sets/btl-openib-benchmark
%{mpi_datadir}/openmpi/amca-param-sets/example.conf
%{mpi_datadir}/openmpi/mca-btl-openib-device-params.ini
%{mpi_datadir}/openmpi/*-data.txt
%{mpi_datadir}/openmpi/help-*.txt
%if %{without pmix}
%dir %{mpi_datadir}/pmix
%{mpi_datadir}/pmix/help-*.txt
%endif

%files %{!?with_hpc:libs}%{?with_hpc:-n lib%{name}}
%defattr(-,root,root)
%dir %mpi_prefix/
%dir %mpi_libdir/
%mpi_libdir/*.so.*
%{mpi_libdir}/openmpi/*.so
%if %{without pmix}
%dir %mpi_libdir/pmix/
%{mpi_libdir}/pmix/*.so
%endif

%files devel
%defattr(-, root, root)
%dir %{mpi_libdir}/openmpi
%dir %{mpi_libdir}/pkgconfig
%{mpi_includedir}
%{mpi_libdir}/*.so
%{mpi_libdir}/pkgconfig/*.pc
%{mpi_libdir}/mpi.mod
%if 0%{?suse_version} >= 1320
%{mpi_libdir}/mpi_f08*.mod
%{mpi_libdir}/pmpi_f08*.mod
%endif
%{mpi_bindir}/mpiCC
%{mpi_bindir}/mpic++
%{mpi_bindir}/mpicc
%{mpi_bindir}/mpicxx
%{mpi_bindir}/mpiexec
%{mpi_bindir}/mpif77
%{mpi_bindir}/mpif90
%{mpi_bindir}/mpifort
%{mpi_bindir}/opal_wrapper
%{mpi_bindir}/ortecc
%if 0%{?with_ucx}
%{mpi_bindir}/oshcc
%{mpi_bindir}/oshCC
%{mpi_bindir}/oshc++
%{mpi_bindir}/oshcxx
%{mpi_bindir}/oshfort
%{mpi_bindir}/shmemcc
%{mpi_bindir}/shmemCC
%{mpi_bindir}/shmemc++
%{mpi_bindir}/shmemcxx
%{mpi_bindir}/shmemfort
%endif
%{mpi_datadir}/openmpi/openmpi-valgrind.supp
%if %{without pmix}
%{mpi_datadir}/pmix/pmix-valgrind.supp
%endif

%files docs
%defattr(-, root, root, -)
%{mpi_mandir}

%files macros-devel
%defattr(-,root,root,-)
%if %{with hpc}
%{_rpmmacrodir}/macros.hpc-openmpi
%else
%{_rpmmacrodir}/macros.openmpi
%endif

%if 0%{?build_static_devel}
%files devel-static
%defattr(-, root, root)
%{mpi_libdir}/*.la
%{mpi_libdir}/openmpi/*.la
%{mpi_libdir}/*.a
%{mpi_libdir}/openmpi/*.a
%endif

%if %{without hpc}
%files -n %{pname}%{m_f_ver}-config
%config %{_sysconfdir}/openmpi-default-hostfile
%config %{_sysconfdir}/openmpi-mca-params.conf
%if %{without pmix}
%config %{_sysconfdir}/pmix-mca-params.conf
%endif
%{_sysconfdir}/openmpi-totalview.tcl
%endif

%endif # !?testsuite

%changelog
