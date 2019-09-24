#
# spec file for package openmpi
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

# Static libraries are disabled by default
# for non HPC builds
# To enable them, simply uncomment:
# % define build_static_devel 1

%define pname openmpi
%define vers 1.10.7
%define _vers 1_10_7
%define m_f_ver 1
%bcond_with ringdisabled

%if "%flavor" == ""
ExclusiveArch:  do_not_build
 %{bcond_with hpc}
 %define package_name %pname
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
  %define package_name   %{pname}
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

%if %{with hpc}
%{!?compiler_family:%global compiler_family gnu}
%{hpc_init -M -c %compiler_family %{?c_f_ver:-v %{c_f_ver}} -m openmpi %{?mpi_f_ver:-V %{mpi_f_ver}}}

%global hpc_openmpi_dep_version %(VER=%m_f_ver; echo -n ${VER})
%global hpc_openmpi_dir openmpi%{hpc_openmpi_dep_version}
%global hpc_openmpi_pack_version %{hpc_openmpi_dep_version}
%endif

%define git_ver .0.5e373bf1fd

#############################################################################
#
# Preamble Section
#
#############################################################################
Name:           %{package_name}%{?testsuite:-testsuite}
Version:        %{vers}
Release:        0
Summary:        A powerful implementation of MPI
License:        BSD-3-Clause
Group:          Development/Libraries/Parallel
Url:            http://www.open-mpi.org/
Source0:        openmpi-%{version}%{git_ver}.tar.bz2
Source1:        mpivars.sh
Source2:        mpivars.csh
Source3:        macros.hpc-openmpi
Source4:        openmpi-rpmlintrc
Source5:        _multibuild
Patch1:         openmpi-avoid-a-date-string-in-compiled-code.patch
Patch2:         openmpi-no_network_in_build.patch
Patch3:         openmpi-1.8.3-fix-bashisms.patch
Patch4:         openmpi-etc-files.patch
Patch5:         openmpi-btl-openib-backport-device-params-from-master.patch
Patch6:         reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libibumad-devel
BuildRequires:  libibverbs-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
%if 0%{?testsuite}
BuildArch:      noarch
BuildRequires:  %package_name = %{version}
%endif
# Disable hpc builds for SLE12
%if 0%{?sle_version} > 120200 && 0%{?sle_version} < 150000 && %{with hpc}
ExclusiveArch:  do_not_build
%endif
%if 0%{?with_ucx}
BuildRequires:  libucm-devel
BuildRequires:  libucp-devel
BuildRequires:  libucs-devel
BuildRequires:  libuct-devel
%endif
%if %{without hpc}
BuildRequires:  Modules
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  mpi-selector
Requires:       mpi-selector
Requires(preun): mpi-selector
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

%ifarch %{ix86} x86_64
BuildRequires:  infinipath-psm-devel
BuildRequires:  libfabric-devel
%endif

%ifarch x86_64
BuildRequires:  libpsm2-devel
BuildRequires:  numactl
%endif

Requires:       openmpi-runtime-config
Recommends:     openmpi-config

# openmpi < 1.10.7 had no separate config package
%{?with_hpc:Conflicts:    openmpi < 1.10.7}

%if %{without hpc}
%define mpi_prefix %{_libdir}/mpi/gcc/openmpi

%define mpi_bindir %{mpi_prefix}/bin
%define mpi_libdir %{mpi_prefix}/%{_lib}
%define mpi_datadir %{mpi_prefix}/share
%define mpi_helpdir %{mpi_datadir}/%{pname}
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
This package contains the test log in the documentation directory
%else
OpenMPI is an implementation of the Message Passing Interface, a
standardized API typically used for parallel and/or distributed
computing. OpenMPI is the merged result of four prior implementations
where the team found for them to excel in one or more areas,
such as latency or throughput.

This RPM contains all the tools necessary to compile, link, and run
Open MPI jobs.
%endif

%if 0%{!?testsuite:1}
%package        %{!?with_hpc:libs}%{?with_hpc:-n lib%{name}}
Summary:        OpenMPI runtime libraries for OpenMPI %{?with_hpc:HPC} version %{version}
Group:          System/Libraries
Requires:       %{name} = %{version}
%{?with_hpc:%hpc_requires}

%description %{!?with_hpc:libs}%{?with_hpc:-n lib%{name}}
OpenMPI is an implementation of the Message Passing Interface, a
standardized API typically used for parallel and/or distributed
computing. OpenMPI is the merged result of four prior implementations
where the team found for them to excel in one or more areas,
such as latency or throughput.

This subpackage contains the OpenMPI shared libraries.

%package        devel
Summary:        SDK for openMPI %{?with_hpc:HPC} version %{version}
Group:          Development/Libraries/Parallel
Requires:       libibumad-devel
Requires:       libibverbs-devel
%if %{without hpc}
Requires:       libstdc++-devel
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

This RPM contains all the wrappers necessary to compile, link, and run
Open MPI jobs.

%if %{with hpc}
%package        macros-devel
Summary:        HPC Macros for openMPI version %{version}
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}
Provides:       %{pname}-hpc-macros-devel = %{version}
Conflicts:      otherproviders(%{pname}-hpc-macros-devel)

%description macros-devel
HPC Macros for building RPM packages for OpenMPI version %{version}.
%endif

%if 0%{?build_static_devel}
%package        devel-static
Summary:        Static libraries for openMPI %{?with_hpc:HPC} version %{version}
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}

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
%package        -n %{pname}-config
Summary:        Runtime configuration files for openMPI %{?with_hpc:HPC} version %{version}
Group:          Development/Libraries/Parallel
Provides:       %{pname}-runtime-config = %{version}
Conflicts:      otherproviders(openmpi-runtime-config)

%description -n %{pname}-config
OpenMPI is an implementation of the Message Passing Interface, a
standardized API typically used for parallel and/or distributed
computing. OpenMPI is the merged result of four prior implementations
where the team found for them to excel in one or more areas,
such as latency or throughput.

This RPM contains the configuration files for OpenMPI runtime (Version 1 or 2).
%endif

%if %{with hpc}
%{hpc_master_package -L -a}
%{hpc_master_package -l}
%{hpc_master_package -a devel}
%{hpc_master_package macros-devel}
%{hpc_master_package -a devel-static}
%endif # ?with_hpc
%endif # !testsuite

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
%setup -q -n  openmpi-%{version}%{?git_ver}
%patch1 -p1
%patch2
%patch3 -p1
%patch4
%patch5

%if %{without hpc}
cat > %{_sourcedir}/baselibs.conf  <<EOF
openmpi-libs
EOF
%endif
%patch6 -p1
# Live patch the VERSION file
sed -i -e 's/^greek=.*$/greek=%{git_ver}/' -e 's/^repo_rev=.*$/repo_rev=%{version}%{git_ver}/' \
       -e 's/^date=.*$/date="OpenMPI %{version} Distribution for SUSE"/' VERSION

#############################################################################
#
# Build Section
#
#############################################################################

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%{?with_hpc:%hpc_debug}
# To force rebuilding Makefile.in
rm -f ompi/debuggers/Makefile.in
#Remove bad +x rights on NEWS
chmod 644 NEWS
./autogen.sh
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
           --disable-wrapper-rpath \
%if 0%{?with_ucx}
           --with-ucx \
           --with-ucx-libdir=/usr/%_lib \
%endif
%ifarch %{ix86} x86_64
           --with-psm \
%endif
%ifarch x86_64
           --with-psm2 \
%endif
    	   --with-threads \
           --disable-silent-rules \
           --enable-mpirun-prefix-by-default \
           --with-package-string="Open MPI Distribution for %{?is_opensuse:openSUSE}%{!?is_opensuse:SLE}" 

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
chmod a-x NEWS
%{?with_hpc:%{hpc_setup_compiler}}
make install DESTDIR="%buildroot"

for input in `find %{buildroot}/%{mpi_mandir} -type f -o -type l` ; do
	if test -f "$input.gz"; then
		#echo "Remove old file $input.gz"
		rm -f "$input.gz"
	fi
	if test -L "$input"; then
		link=`perl -e 'print readlink($ARGV[0]);' -- "$input"`
		test -d "$link" && continue
		test -d "%{buildroot}/$link" && continue
		rm -f "$input"
		ln -sf "$link.gz" "$input.gz"
	else
		gzip -nf9 "$input"
	fi
	ls -l "$input.gz"
done

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
rm -f %{buildroot}%{mpi_datadir}/vampirtrace/config.log # differs between builds ; not needed

%fdupes %{buildroot}%{mpi_mandir} 
%fdupes %{buildroot}%{mpi_datadir} 
%fdupes %{buildroot}%{mpi_libdir}/pkgconfig

%if %{without hpc}
# make and install mpivars files
sed -e 's,prefix,%{mpi_prefix},g' -e 's,libdir,%{mpi_libdir},g' %{SOURCE1} \
    > %{buildroot}%{mpi_bindir}/mpivars.sh
sed -e 's,prefix,%{mpi_prefix},g' -e 's,libdir,%{mpi_libdir},g' %{SOURCE2} \
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
prepend-path INCLUDE %{mpi_libdir}/lib64
prepend-path MANPATH %{mpi_mandir}
prepend-path LD_LIBRARY_PATH %{mpi_libdir}

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
module load %{hpc_mpi_family}/%{version}
EOF
sed -e "s/export/setenv/" -e "s/=/ /" \
    %{buildroot}/%{mpi_bindir}/mpivars.sh > \
    %{buildroot}/%{mpi_bindir}/mpivars.csh
mkdir -p %{buildroot}%{_sysconfdir}/rpm
cp %{S:3} %{buildroot}%{_sysconfdir}/rpm

# Drop the files that should go into %{pname}-config as we only package them
# in the non HPC build
rm -f %{buildroot}%{_sysconfdir}/openmpi-default-hostfile
rm -f %{buildroot}%{_sysconfdir}/openmpi-mca-params.conf
rm -f %{buildroot}%{_sysconfdir}/openmpi-totalview.tcl
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
	# Deregister the default if we are uninstalling it
	if [ "$(/usr/bin/mpi-selector --system --query)" = "%{name}" ]; then
		/usr/bin/mpi-selector --system --unset --yes
	fi
	/usr/bin/mpi-selector --unregister %{name} --yes
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
%doc NEWS README AUTHORS
%license LICENSE
%dir %{mpi_bindir}
%dir %{mpi_libdir}
%dir %{mpi_datadir}
%dir %{mpi_mandir}
%{mpi_bindir}/mpivars.csh
%{mpi_bindir}/mpivars.sh

%if %{without hpc}
%dir %{_libdir}/mpi
%dir %{_libdir}/mpi/gcc
%dir %{mpi_prefix}
%dir %{_datadir}/modules/gnu-openmpi
%{_datadir}/modules/gnu-openmpi/%{version}
%else # with hpc
%hpc_mpi_dirs
%hpc_modules_files
%endif # with hpc
#
%if 0%{?suse_version} <= 1320
%dir %{mpi_datadir}/openmpi/doc
%{mpi_datadir}/openmpi/doc/COPYRIGHT-ptmalloc2.txt
%endif
#
%{mpi_bindir}/mpirun
%{mpi_bindir}/ompi-clean
%{mpi_bindir}/ompi-ps
%{mpi_bindir}/ompi-server
%{mpi_bindir}/ompi-top
%{mpi_bindir}/ompi_info
%{mpi_bindir}/orte-clean
%{mpi_bindir}/orte-dvm
%{mpi_bindir}/orte-info
%{mpi_bindir}/orte-ps
%{mpi_bindir}/orte-server
%{mpi_bindir}/orte-submit
%{mpi_bindir}/orte-top
%{mpi_bindir}/orted
%{mpi_bindir}/orterun
%{mpi_bindir}/oshmem_info
%{mpi_bindir}/oshrun
%{mpi_bindir}/shmemrun
#
%dir %{mpi_mandir}/man1
%{mpi_mandir}/man1/oshmem_info.1.gz
%{mpi_mandir}/man1/orte-clean.1.gz
%{mpi_mandir}/man1/orte-dvm.1.gz
%{mpi_mandir}/man1/orte-info.1.gz
%{mpi_mandir}/man1/orte-ps.1.gz
%{mpi_mandir}/man1/orte-server.1.gz
%{mpi_mandir}/man1/orte-submit.1.gz
%{mpi_mandir}/man1/orte-top.1.gz
%{mpi_mandir}/man1/orted.1.gz
%{mpi_mandir}/man1/orterun.1.gz
%{mpi_mandir}/man1/mpirun.1.gz
%{mpi_mandir}/man1/ompi-clean.1.gz
%{mpi_mandir}/man1/ompi-ps.1.gz
%{mpi_mandir}/man1/ompi-server.1.gz
%{mpi_mandir}/man1/ompi-top.1.gz
%{mpi_mandir}/man1/ompi_info.1.gz
%{mpi_mandir}/man1/shmemrun.1.gz
%{mpi_mandir}/man7
#
%dir %{mpi_datadir}/openmpi
%{mpi_datadir}/openmpi/help-*.txt

%dir %{mpi_datadir}/openmpi/amca-param-sets
%{mpi_datadir}/openmpi/amca-param-sets/btl-openib-benchmark
%{mpi_datadir}/openmpi/amca-param-sets/example.conf
%{mpi_datadir}/openmpi/mca-btl-openib-device-params.ini
%{mpi_datadir}/openmpi/mca-coll-ml.config

%files %{!?with_hpc:libs}%{?with_hpc:-n lib%{name}}
%defattr(-,root,root)
%dir %mpi_prefix/
%mpi_libdir/*.so.*
%{mpi_libdir}/openmpi/*.so

%files devel
%defattr(-,root,root)
%doc %{mpi_datadir}/vampirtrace
%dir %{mpi_libdir}/pkgconfig
%dir %{mpi_libdir}/openmpi/
%{mpi_libdir}/*mpi*.mod
%{mpi_bindir}/mpiCC
%{mpi_bindir}/mpiCC-vt
%{mpi_bindir}/mpic++
%{mpi_bindir}/mpic++-vt
%{mpi_bindir}/mpicc
%{mpi_bindir}/mpicc-vt
%{mpi_bindir}/mpicxx
%{mpi_bindir}/mpicxx-vt
%{mpi_bindir}/mpiexec
%{mpi_bindir}/mpif77
%{mpi_bindir}/mpif77-vt
%{mpi_bindir}/mpif90
%{mpi_bindir}/mpif90-vt
%{mpi_bindir}/mpifort
%{mpi_bindir}/mpifort-vt
%{mpi_bindir}/opal_wrapper
%{mpi_bindir}/opari
%{mpi_bindir}/ortecc
%{mpi_bindir}/oshcc
%{mpi_bindir}/oshfort
%{mpi_bindir}/otfaux
%{mpi_bindir}/otfconfig
%{mpi_bindir}/otfinfo
%{mpi_bindir}/otfmerge
%{mpi_bindir}/otfmerge-mpi
%{mpi_bindir}/otfprint
%{mpi_bindir}/otfprofile
%{mpi_bindir}/otfprofile-mpi
%{mpi_bindir}/otfshrink
%{mpi_bindir}/otfcompress
%{mpi_bindir}/otfdecompress

%{mpi_bindir}/shmemcc
%{mpi_bindir}/shmemfort
%{mpi_bindir}/vtCC
%{mpi_bindir}/vtc++
%{mpi_bindir}/vtcc
%{mpi_bindir}/vtcxx
%{mpi_bindir}/vtf77
%{mpi_bindir}/vtf90
%{mpi_bindir}/vtfilter
%{mpi_bindir}/vtfilter-mpi
%{mpi_bindir}/vtfiltergen
%{mpi_bindir}/vtfiltergen-mpi
%{mpi_bindir}/vtfort
%{mpi_bindir}/vtrun
%{mpi_bindir}/vtunify
%{mpi_bindir}/vtunify-mpi
%{mpi_bindir}/vtwrapper

#
%{mpi_mandir}/man1/mpiCC.1.gz
%{mpi_mandir}/man1/mpic++.1.gz
%{mpi_mandir}/man1/mpicc.1.gz
%{mpi_mandir}/man1/mpicxx.1.gz
%{mpi_mandir}/man1/mpiexec.1.gz
%{mpi_mandir}/man1/mpif77.1.gz
%{mpi_mandir}/man1/mpif90.1.gz
%{mpi_mandir}/man1/mpifort.1.gz
%{mpi_mandir}/man1/opal_wrapper.1.gz
%{mpi_mandir}/man1/oshcc.1.gz
%{mpi_mandir}/man1/oshfort.1.gz
%{mpi_mandir}/man1/oshrun.1.gz
%{mpi_mandir}/man1/shmemcc.1.gz
%{mpi_mandir}/man1/shmemfort.1.gz
%{mpi_mandir}/man3
#
%{mpi_helpdir}/mpiCC-vt-wrapper-data.txt
%{mpi_helpdir}/mpiCC-wrapper-data.txt
%{mpi_helpdir}/mpic++-vt-wrapper-data.txt
%{mpi_helpdir}/mpic++-wrapper-data.txt
%{mpi_helpdir}/mpicc-vt-wrapper-data.txt
%{mpi_helpdir}/mpicc-wrapper-data.txt
%{mpi_helpdir}/mpicxx-vt-wrapper-data.txt
%{mpi_helpdir}/mpicxx-wrapper-data.txt
%{mpi_helpdir}/mpif77-vt-wrapper-data.txt
%{mpi_helpdir}/mpif77-wrapper-data.txt
%{mpi_helpdir}/mpif90-vt-wrapper-data.txt
%{mpi_helpdir}/mpif90-wrapper-data.txt
%{mpi_helpdir}/mpifort-vt-wrapper-data.txt
%{mpi_helpdir}/mpifort-wrapper-data.txt

%{mpi_helpdir}/openmpi-valgrind.supp
%{mpi_helpdir}/ortecc-wrapper-data.txt
%{mpi_helpdir}/oshcc-wrapper-data.txt
%{mpi_helpdir}/oshfort-wrapper-data.txt
%{mpi_helpdir}/shmemcc-wrapper-data.txt
%{mpi_helpdir}/shmemfort-wrapper-data.txt
#
%{mpi_includedir}
%{mpi_libdir}/*.so
%{mpi_libdir}/pkgconfig/*.pc

%if %{with hpc}
%files macros-devel
%defattr(-,root,root,-)
%config %{_sysconfdir}/rpm/macros.hpc-openmpi
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
%files -n %{pname}-config
%config %{_sysconfdir}/openmpi-default-hostfile
%config %{_sysconfdir}/openmpi-mca-params.conf
%{_sysconfdir}/openmpi-totalview.tcl
%endif

%endif # !?testsuite

%changelog
