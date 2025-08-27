#
# spec file for package openmpi4
#
# Copyright (c) 2025 SUSE LLC
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
# To enable them, simply uncomment:
# % define build_static_devel 1

%bcond_with ringdisabled

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif

# Trickery for OBS Staging. If _with_ringdisabled is set
# we only want to build the flavors required by other rings packages.
# Do not build any other ones
 %if %{with ringdisabled} && "%flavor" != "standard"
ExclusiveArch:  do_not_build
%endif

%if "%flavor" == "testsuite"
%define testsuite 1
%endif

%ifarch aarch64 %power64 x86_64 s390x
%define with_ucx 1
%endif

# Detect whether we are the default openMPI implemantation or not
%if "%{flavor}" == "standard" && (%{suse_version} > 1500 || 0%{?sle_version} > 150300) &&  (%{suse_version} < 1600)
%define default_openmpi 1
%else
%define default_openmpi 0
%endif

%{bcond_with pmix}
%{bcond_with hwloc}

%define git_ver .0.ea8f4d030890

#############################################################################
#
# Preamble Section
#
#############################################################################

Name:           openmpi4%{?testsuite:-testsuite}
Version:        4.1.8
Release:        0
Summary:        An implementation of MPI/SHMEM (Version 4)
License:        BSD-3-Clause
Group:          Development/Libraries/Parallel
URL:            https://www.open-mpi.org/
Source0:        openmpi-%{version}%{git_ver}.tar.bz2
Source2:        openmpi4-rpmlintrc
Source4:        mpivars.sh
Source5:        mpivars.csh
Patch1:         orted-mpir-add-version-to-shared-library.patch
Patch2:         btl-openib-Add-VF-support-for-ConnectX-4-5-and-6.patch
Patch3:         openmpi4-C99.diff
Patch4:         test-datatype-partial.c-fix-compiler-warnings.patch
Patch5:         mtl-ofi-fix-missing-definition-of-container_of.patch
Patch6:         Fix-type-mismatch-error.patch
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
BuildRequires:  openmpi4 = %{version}
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
BuildRequires:  Modules
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  mpi-selector
Requires:       mpi-selector
Requires(preun): mpi-selector
%if !0%{?testsuite}
Requires:       %{name}-libs = %{version}
%endif

%ifarch x86_64
BuildRequires:  libnuma-devel
BuildRequires:  libpsm2-devel
BuildRequires:  numactl
%endif

Requires:       openmpi-runtime-config
Recommends:     %{name}-config
%if 0%{?default_openmpi}
Provides:       openmpi = %{version}
%endif
# OpenMPI requires ssh (or rsh) to run even on a single host
# Force ssh to make sure the install works out of the box
Requires:       openssh

%define mpi_prefix %{_libdir}/mpi/gcc/%{name}

%define mpi_bindir %{mpi_prefix}/bin
%define mpi_libdir %{mpi_prefix}/%{_lib}
%define mpi_datadir %{mpi_prefix}/share
%define mpi_helpdir %{mpi_datadir}/%{name}
%define mpi_includedir %{mpi_prefix}/include
%define mpi_mandir %{mpi_prefix}/share/man

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
running Open MPI/OpenSHMEM version %{version} jobs.
%endif

%if 0%{!?testsuite:1}
%package        libs
Summary:        OpenMPI runtime libraries for OpenMPI version %{version}
Group:          System/Libraries
Requires:       %{name} = %{version}
%if 0%{?default_openmpi}
Provides:       openmpi-libs = %{version}
%endif

%description libs
OpenMPI is an implementation of the Message Passing Interface, a
standardized API typically used for parallel and/or distributed
computing. OpenMPI is the merged result of four prior implementations
where the team found for them to excel in one or more areas,
such as latency or throughput.

OpenMPI also includes an implementation of the OpenSHMEM parallel
programming API, which is a Partitioned Global Address Space (PGAS)
abstraction layer providing inter-process communication using
one-sided communication techniques.

This package provides the Open MPI/OpenSHMEM version %{version}
shared libraries.

%package        devel
Summary:        SDK for openMPI version %{version}
Group:          Development/Libraries/Parallel
Requires:       libibumad-devel
Requires:       libibverbs-devel
Requires:       libstdc++-devel
%if 0%{?default_openmpi}
Provides:       openmpi-devel = %{version}
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
version %{version}, such as wrapper compilers and header files for
MPI/OpenSHMEM development.

%package docs
Summary:        Documentation for Open MPI/SHMEM version %{version}
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
Provides:       openmpi-macros-provider = %{version}
Conflicts:      otherproviders(openmpi-macros-provider)
# Conflict (without providing) with the older openmpi-hpc-macros-devel flag
# to avoid issue with older packages
Conflicts:      otherproviders(openmpi-hpc-macros-devel)

%if 0%{?default_openmpi}
Provides:       openmpi-macros-devel = %{version}
%endif

%description macros-devel
Macros for building RPM packages for OpenMPI version %{version}.

%if 0%{?build_static_devel}
%package        devel-static
Summary:        Static libraries for openMPI version %{version}
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

%package        config
Summary:        Runtime configuration files for openMPI version %{version}
Group:          Development/Libraries/Parallel
Provides:       openmpi-runtime-config = %{version}
Conflicts:      otherproviders(openmpi-runtime-config)
%if %{without pmix}
# OpenMPI4 is PMIx enabled
Provides:       pmix-runtime-config = %{version}
Conflicts:      otherproviders(pmix-runtime-config)
%endif

%description config
OpenMPI is an implementation of the Message Passing Interface, a
standardized API typically used for parallel and/or distributed
computing. OpenMPI is the merged result of four prior implementations
where the team found for them to excel in one or more areas,
such as latency or throughput.

This RPM contains the configuration files for OpenMPI runtime (Version 3).

%endif # !testsuite

#############################################################################
#
# Prepatory Section
#
#############################################################################
%prep
echo FLAVOR %{flavor}
%autosetup -p0 -n  openmpi-%{version}%{git_ver}

cat > %{_sourcedir}/baselibs.conf  <<EOF
openmpi%{m_f_ver}-libs
EOF

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
./autogen.pl --force
%{configure} \
           --prefix="%{mpi_prefix}" \
           --exec-prefix="%{mpi_prefix}" \
           --bindir="%{mpi_bindir}" \
           --datadir="%{mpi_datadir}" \
           --includedir="%{mpi_includedir}" \
           --libdir="%{mpi_libdir}" \
           --mandir="%{mpi_mandir}" \
           %{?build_static_devel:--enable-static}  \
           %{!?build_static_devel:--disable-static}  \
           --enable-builtin-atomics \
           --with-libltdl=%{_prefix} \
           --with-verbs \
           --with-libfabric \
           --enable-mpi-thread-multiple \
           --disable-wrapper-rpath \
           --with-slurm \
           --with-sge \
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
%dir %{_libdir}/mpi
%dir %{_libdir}/mpi/gcc
%dir %{_datadir}/modules/gnu-openmpi
%{_datadir}/modules/gnu-openmpi/%{version}
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
%{mpi_bindir}/aggregate_profile.pl
%{mpi_bindir}/profile2mat.pl

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

%files libs
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
%{mpi_libdir}/mpi_f08*.mod
%{mpi_libdir}/pmpi_f08*.mod
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
%{_rpmmacrodir}/macros.openmpi

%if 0%{?build_static_devel}
%files devel-static
%defattr(-, root, root)
%{mpi_libdir}/*.la
%{mpi_libdir}/openmpi/*.la
%{mpi_libdir}/*.a
%{mpi_libdir}/openmpi/*.a
%endif

%files config
%config %{_sysconfdir}/openmpi-default-hostfile
%config %{_sysconfdir}/openmpi-mca-params.conf
%if %{without pmix}
%config %{_sysconfdir}/pmix-mca-params.conf
%endif
%{_sysconfdir}/openmpi-totalview.tcl

%endif # !?testsuite

%changelog
