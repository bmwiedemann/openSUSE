#
# spec file for package mvapich3
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

# Static libraries are disabled by default
# for non HPC builds
# To enable them, simply uncomment:
# % define build_static_devel 1

%define pname mvapich3
%define rc_ver %nil

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "ucx"
%define build_flavor ucx
%endif
%if "%{flavor}" == "ucx-testsuite"
%define build_flavor ucx
%define testsuite 1
%endif

%if "%{flavor}" == "ofi"
%define build_flavor ofi
%endif
%if "%{flavor}" == "ofi-testsuite"
%define build_flavor ofi
%define testsuite 1
%endif

%define pack_suff %{?build_flavor:-%{build_flavor}}

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

Name:           %{package_name}
Summary:        OSU MVAPICH3 MPI package
License:        BSD-3-Clause
Group:          Development/Libraries/Parallel
Version:        3.0
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
Patch6:         autogen-only-deal-with-json-yaksa-if-enabled.patch

URL:            http://mvapich.cse.ohio-state.edu
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# Exclude 32b archs
ExcludeArch:    %{arm} %ix86

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
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libjson-c-devel
BuildRequires:  libtool
BuildRequires:  mpi-selector
BuildRequires:  python3
BuildRequires:  sysfsutils
%if %{with hwloc}
BuildRequires:  hwloc-devel
%endif
%if %{with pmix}
BuildRequires:  pmix-devel
%endif
%if "%{build_flavor}" == "ofi"
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
Requires:       mpi-selector

%description
This is an MPI-3 implementation which includes all MPI-1 and MPI-2 features. It
is based on MPICH3 and MVICH.

%if 0%{!?testsuite:1}

%package        devel
Summary:        OSU MVAPICH3 MPI package
Group:          Development/Libraries/Parallel
Requires:       %{name} = %{version}
Requires:       gcc-c++
Requires:       gcc-fortran

%description devel
This is an MPI-3 implementation which includes all MPI-1 and MPI-2 features.  It
is based on MPICH3 and MVICH.

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

%endif # ! testsuite

%prep

%setup -q -n mvapich-%{version}%{?rc_ver}
%autopatch -p0

cp /usr/share/automake*/config.* .

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

# GCC10 needs an extra flag to allow badly passed parameters
%if 0%{?suse_version} > 1500
export FFLAGS="-fallow-argument-mismatch $FFLAGS"
%endif

./autogen.sh --without-ucx --without-ofi --without-json
%configure \
    --prefix=%{p_prefix} \
    --exec-prefix=%{p_prefix} \
    --datadir=%{p_datadir} \
    --bindir=%{p_bindir} \
    --includedir=%{p_includedir} \
    --libdir=%{p_libdir} \
    --libexecdir=%{p_libexecdir} \
    --mandir=%{p_mandir} \
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

%post
/sbin/ldconfig
# Always register. We might be already registered in the case of an udate
# but mpi-selector handles it fine
/usr/bin/mpi-selector \
        --register %{name}%{?pack_suff} \
        --source-dir %{p_bindir} \
        --yes

%postun
/sbin/ldconfig
# Only unregister when uninstalling
if [ "$1" = "0" ]; then
	/usr/bin/mpi-selector --unregister %{name}%{?pack_suff} --yes
	# Deregister the default if we are uninstalling it
	if [ "$(/usr/bin/mpi-selector --system --query)" = "%{name}%{?pack_suff}" ]; then
		/usr/bin/mpi-selector --system --unset --yes
	fi
fi

%files
%defattr(-, root, root)
%doc CHANGES CHANGELOG COPYRIGHT README README.envvar README-MVAPICH README_MVP.envvar
%dir /usr/%_lib/mpi
%dir /usr/%_lib/mpi/gcc
%dir /usr/share/modules
%dir %{_moduledir}
%{_moduledir}
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

%endif # !testsuite

%changelog
