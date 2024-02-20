#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}

# Static libraries are disabled by default
# for non HPC builds
# To enable them, simply uncomment:
# % define build_static_devel 1

%define pname mvapich3
%define vers  3.0
%define _vers 3_0
%define rc_ver %nil

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%{bcond_with hpc}
%endif

%if "%{flavor}" == "ucx"
%define build_flavor ucx
%{bcond_with hpc}
%endif
%if "%{flavor}" == "ucx-testsuite"
%define build_flavor ucx
%define testsuite 1
%{bcond_with hpc}
%endif

%if "%{flavor}" == "ofi"
%define build_flavor ofi
%{bcond_with hpc}
%endif
%if "%{flavor}" == "ofi-testsuite"
%define build_flavor ofi
%define testsuite 1
%{bcond_with hpc}
%endif

%if "%flavor" == "gnu-hpc-ucx"
%define compiler_family gnu
%undefine c_f_ver
%define build_flavor ucx
%define build_static_devel 1
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu-hpc-ofi"
%define compiler_family gnu
%undefine c_f_ver
%define build_flavor ofi
%define build_static_devel 1
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu7-hpc-ucx"
%define compiler_family gnu
%define c_f_ver 7
%define build_flavor ucx
%define build_static_devel 1
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu7-hpc-ofi"
%define compiler_family gnu
%define c_f_ver 7
%define build_flavor ofi
%define build_static_devel 1
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu8-hpc-ucx"
%define compiler_family gnu
%define c_f_ver 8
%define build_flavor ucx
%define build_static_devel 1
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu8-hpc-ofi"
%define compiler_family gnu
%define c_f_ver 8
%define build_flavor ofi
%define build_static_devel 1
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu9-hpc-ucx"
%define compiler_family gnu
%define c_f_ver 9
%define build_flavor ucx
%define build_static_devel 1
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu9-hpc-ofi"
%define compiler_family gnu
%define c_f_ver 9
%define build_flavor ofi
%define build_static_devel 1
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu10-hpc-ucx"
%define compiler_family gnu
%define c_f_ver 10
%define build_flavor ucx
%define build_static_devel 1
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu10-hpc-ofi"
%define compiler_family gnu
%define c_f_ver 10
%define build_flavor psm2
%define build_static_devel 1
%{bcond_without hpc}
%endif

%define pack_suff %{?build_flavor:-%{build_flavor}}

%if %{without hpc}
%define module_name mvapich3%{?pack_suff}
%define p_prefix /usr/%_lib/mpi/gcc/%{module_name}
%define p_bindir  %{p_prefix}/bin
%define p_datadir %{p_prefix}/share
%define p_includedir %{p_prefix}/include
%define p_mandir  %{p_datadir}/man
%define p_libdir  %{p_prefix}/%{_lib}
%define p_libexecdir %{p_prefix}/%{_lib}
%define _moduledir /usr/share/modules/gnu-%{module_name}
%define package_name mvapich3%{?pack_suff}
%{bcond_with pmix}
%{bcond_with hwloc}
%else
%{hpc_init -M -c %compiler_family %{?c_f_ver:-v %{c_f_ver}} -m mvapich3 %{?pack_suff:-e %{build_flavor}}}
%define p_prefix   %{hpc_prefix}
%define p_bindir   %{hpc_bindir}
%define p_datadir  %{hpc_datadir}
%define p_includedir  %{hpc_includedir}
%define p_mandir   %{hpc_mandir}
%define p_libdir   %{hpc_libdir}
%define p_libexecdir  %{hpc_libexecdir}
%define package_name %{hpc_package_name %{_vers}}

%global hpc_mvapich3_dep_version %(VER=%{?m_f_ver}; echo -n ${VER})
%global hpc_mvapich3_dir mvapich3
%global hpc_mvapich3_pack_version %{hpc_mvapich3_dep_version}
%{bcond_without pmix}
%{bcond_without hwloc}
%endif

# Disable hpc builds for SLE12
%if 0%{?sle_version} > 120200 && 0%{?sle_version} < 150000 && %{with hpc}
%{bcond_with skip_hpc_build}
%else
%{bcond_without skip_hpc_build}
%endif

Name:           %{package_name}
Summary:        OSU MVAPICH3 MPI package
License:        BSD-3-Clause
Group:          Development/Libraries/Parallel
Version:        %{vers}
Release:        0
Source0:        http://mvapich.cse.ohio-state.edu/download/mvapich/mv2/mvapich-%{version}%{?rc_ver}.tar.gz
Source1:        mpivars.sh
Source2:        mpivars.csh
Source3:        macros.hpc-mvapich3
Source100:      _multibuild
Patch0:         mvapich3-s390_get_cycles.patch
Patch1:         pass-correct-size-to-snprintf.patch
# Backport from mpich
Patch2:         mpl-warnings-missing-return.patch
Patch3:         mpi-coll-missing-return.patch
Patch4:         autoconf-pull-dynamic-and-not-static-libs-from-pkg-config.patch
Patch5:         config-replace-AC_TRY_-COMPILE-LINK-RUN.patch

URL:            http://mvapich.cse.ohio-state.edu
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# Exclude 32b archs
ExcludeArch:    %{arm} %ix86
%if %{without skip_hpc_build}
ExclusiveArch:  do_not_build
%endif

BuildRequires:  autoconf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  hwloc-devel >= 2.0
%ifnarch s390 s390x %{arm}
BuildRequires:  libnuma-devel
%endif
BuildRequires:  libtool
BuildRequires:  libtool
BuildRequires:  sysfsutils
BuildRequires:  python3
%if %{without hpc}
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  mpi-selector
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
%endif
%if %{with hwloc}
BuildRequires:  hwloc-devel
%endif
%if %{with pmix}
BuildRequires:  pmix-devel
%endif
%if "%{build_flavor}" == "ofi" && %{with skip_hpc_build}
BuildRequires:  libfabric-devel
%endif
%if "%{build_flavor}" == "ucx"
BuildRequires:  libucm-devel
BuildRequires:  libucp-devel
BuildRequires:  libucs-devel
BuildRequires:  libuct-devel
# UCX is only available for 64b archs
ExcludeArch:    %ix86 %arm
%endif

%if %{without hpc}
Requires:       mpi-selector
%else
%hpc_requires
%endif

%description
This is an MPI-3 implementation which includes all MPI-1 and MPI-2 features. It
is based on MPICH3 and MVICH.

%{!?testsuite:%{?with_hpc:%{hpc_master_package -a -L}}}

%if 0%{!?testsuite:1}

%package        devel
Summary:        OSU MVAPICH3 MPI package
Group:          Development/Libraries/Parallel
Requires:       %{name} = %{version}
%if %{without hpc}
Requires:       gcc-c++
Requires:       gcc-fortran
%else
%hpc_requires_devel
%endif

%description devel
This is an MPI-3 implementation which includes all MPI-1 and MPI-2 features.  It
is based on MPICH3 and MVICH.

%{?with_hpc:%{hpc_master_package -a devel}}

%if 0%{?build_static_devel}
%package        devel-static
Summary:        OSU MVAPICH3 MPI package - static libraries
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}

%description devel-static
This is an MPI-3 implementation which includes all MPI-1 and MPI-2 features.  It
is based on MPICH3. This package contains the static libraries
%endif

%package        doc
Summary:        OSU MVAPICH3 MPI package - Documentation
Group:          Development/Libraries/Parallel
Requires:       %{name} = %{version}

%description  doc
This is an MPI-3 implementation which includes all MPI-1 and MPI-2 features.  It
is based on MPICH3 and MVICH. This package contains the static libraries

%{?with_hpc:%{hpc_master_package doc}}

%package        macros-devel
Summary:        OSU MVAPICH3 MPI package - HPC build macros
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}
Provides:       %{pname}-hpc-macros-devel = %{version}
Conflicts:      otherproviders(%{pname}-hpc-macros-devel)

%description macros-devel
This is an MPI-3 implementation which includes all MPI-1 and MPI-2 features.  It
is based on MPICH2 and MVICH. This package contains the static libraries

%{?with_hpc:%{hpc_master_package macros-devel}}

%endif # ! testsuite

%prep

%{?with_hpc:%hpc_debug}
%setup -q -n mvapich-%{version}%{?rc_ver}
%autopatch -p0

cp /usr/share/automake*/config.* .


%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

# GCC10 needs an extra flag to allow badly passed parameters
%if 0%{?suse_version} > 1500 || 0%{?hpc_gnu_dep_version} >= 10
export FFLAGS="-fallow-argument-mismatch $FFLAGS"
%endif

./autogen.sh --without-ucx --without-ofi
%if %{with hpc}
%{hpc_setup}
%{hpc_configure} \
%else
%configure \
    --prefix=%{p_prefix} \
    --exec-prefix=%{p_prefix} \
    --datadir=%{p_datadir} \
    --bindir=%{p_bindir} \
    --includedir=%{p_includedir} \
    --libdir=%{p_libdir} \
    --libexecdir=%{p_libexecdir} \
    --mandir=%{p_mandir} \
%endif
   --docdir=%{_datadir}/doc/%{name} \
   --disable-rpath      \
   --disable-wrapper-rpath \
%if %{with hwloc}
   --with-hwloc-prefix=%{_prefix} \
%endif
%if %{with pmix}
   --with-pmix=${_prefix} \
%endif
%if "%{build_flavor}" == "ofi"
   --with-ofi \
   --with-device=ch4:ofi \
%endif
%if "%{build_flavor}" == "ucx"
   --with-ucx \
   --with-device=ch4:ucx \
%endif
  --without-mpe
make %{?_smp_mflags} V=1

%if 0%{?testsuite}
%check
make V=1 check
%endif

%install

%if 0%{?testsuite}
# Remove everything from testsuite package
# It is all contained by mvapich3 packages
rm -rf %{buildroot}/*

%else
make DESTDIR=%{buildroot} V=1 install

rm -f %{buildroot}%{p_libdir}/libfmpich.la \
      %{buildroot}%{p_libdir}/libmpich.la \
      %{buildroot}%{p_libdir}/libmpichcxx.la \
      %{buildroot}%{p_libdir}/libmpichf90.la \
      %{buildroot}%{p_libdir}/libmpl.la \
      %{buildroot}%{p_libdir}/libopa.la \
      %{buildroot}%{p_libdir}/libmpi.la \
      %{buildroot}%{p_libdir}/libmpicxx.la \
      %{buildroot}%{p_libdir}/libmpifort.la

%if !0%{?build_static_devel}
find %{buildroot} -name "*.a" -delete
%endif

install -m 0755 -d %{buildroot}%{_datadir}/doc/%{name}
install -m 0644 COPYRIGHT* %{buildroot}%{_datadir}/doc/%{name}
install -m 0644 CHANGE* %{buildroot}%{_datadir}/doc/%{name}

%if %{without hpc}
# make and install mpivars files
install -m 0755 -d %{buildroot}%{_bindir}
sed -e 's,prefix,%p_prefix,g' -e 's,libdir,%{p_libdir},g' %{S:1} > %{buildroot}%{p_bindir}/mpivars.sh
sed -e 's,prefix,%p_prefix,g' -e 's,libdir,%{p_libdir},g' %{S:2} > %{buildroot}%{p_bindir}/mpivars.csh

mkdir -p %{buildroot}%{_moduledir}

cat << EOF > %{buildroot}%{_moduledir}/%{version}
#%%Module
proc ModulesHelp { } {
        global dotversion
        puts stderr "\tLoads the gnu - mvapich3 %{version}  Environment"
}

module-whatis  "Loads the gnu mvapich3 %{version} Environment."
conflict gnu-mvapich3
prepend-path PATH %{%p_bindir}
prepend-path INCLUDE %{p_includedir}
prepend-path INCLUDE %{p_libdir}
prepend-path MANPATH %{p_mandir}
prepend-path LD_LIBRARY_PATH %{p_libdir}

EOF

cat << EOF > %{buildroot}%{_moduledir}/.version
#%%Module1.0
set ModulesVersion "%{version}"

EOF
%else # with hpc

install -d -m 755 %{buildroot}%{_rpmmacrodir}
cp %{S:3} %{buildroot}%{_rpmmacrodir}

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

prepend-path    PATH                %{hpc_bindir}
prepend-path    MANPATH             %{hpc_mandir}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}
prepend-path    MODULEPATH          %{hpc_modulepath}
prepend-path    MPI_DIR             %{hpc_prefix}
%{hpc_modulefile_add_pkgconfig_path}

family "MPI"
EOF
cat <<EOF >  %{buildroot}/%{p_bindir}/mpivars.sh
%hpc_setup_compiler
module load %{hpc_mpi_family}%{?pack_suff}/%{version}
EOF
sed -e "s/export/setenv/" -e "s/=/ /" \
    %{buildroot}/%{p_bindir}/mpivars.sh > \
    %{buildroot}/%{p_bindir}/mpivars.csh
mkdir -p %{buildroot}%{_sysconfdir}/rpm

%endif # with hpc

%post
/sbin/ldconfig
%if %{without hpc}
# Always register. We might be already registered in the case of an udate
# but mpi-selector handles it fine
/usr/bin/mpi-selector \
        --register %{name}%{?pack_suff} \
        --source-dir %{p_bindir} \
        --yes
%endif

%postun
/sbin/ldconfig
%if %{without hpc}
# Only unregister when uninstalling
if [ "$1" = "0" ]; then
	/usr/bin/mpi-selector --unregister %{name}%{?pack_suff} --yes
	# Deregister the default if we are uninstalling it
	if [ "$(/usr/bin/mpi-selector --system --query)" = "%{name}%{?pack_suff}" ]; then
		/usr/bin/mpi-selector --system --unset --yes
	fi
fi
%else
%hpc_module_delete_if_default
%endif

%files
%defattr(-, root, root)
%doc CHANGES CHANGELOG COPYRIGHT README README.envvar README-MVAPICH README_MVP.envvar
%if %{without hpc}
%dir /usr/%_lib/mpi
%dir /usr/%_lib/mpi/gcc
%dir /usr/share/modules
%dir %{_moduledir}
%{_moduledir}
%else
%hpc_mpi_dirs
%hpc_modules_files
%endif
%dir %{p_prefix}
%dir %{p_bindir}
%dir %{p_datadir}
%dir %{p_includedir}
%dir %{p_mandir}
%dir %{p_mandir}/man1
%dir %{p_mandir}/man3
%dir %{p_libdir}
%dir %{p_libexecdir}
%{p_bindir}/*
%{p_libexecdir}/osu-micro-benchmarks
%{p_mandir}/man1/*
%{p_libdir}/*.so.*

%files doc
%defattr(-, root, root)
%doc %{_datadir}/doc/%{name}
%exclude /%{_datadir}/doc/%{name}/COPYRIGHT*
%exclude /%{_datadir}/doc/%{name}/CHANGE*
%exclude /%{_datadir}/doc/%{name}/README*

%files devel
%defattr(-,root,root)
%dir %{p_libdir}/pkgconfig
%{p_mandir}/man3/*
%{p_includedir}
%{p_libdir}/*.so
%{p_libdir}/pkgconfig/mvapich.pc
%{p_libdir}/pkgconfig/yaksa.pc

%if 0%{?build_static_devel}
%files devel-static
%defattr(-,root,root)
%{p_libdir}/*.a
%endif

%if %{with hpc}
%files macros-devel
%defattr(-,root,root)
%config %{_rpmmacrodir}/macros.hpc-mvapich3
%endif # with hpc

%endif # !testsuite

%changelog
