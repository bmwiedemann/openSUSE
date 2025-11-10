#
# spec file for package mvapich2
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

%define pname mvapich2
%define rc_ver -1

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "standard"
%define build_flavor verbs
%{bcond_with hpc}
%endif
%if "%{flavor}" == "testsuite"
%define build_flavor verbs
%define testsuite 1
%endif

%if "%{flavor}" == "psm2"
%define build_flavor psm2
%endif
%if "%{flavor}" == "psm2-testsuite"
%define build_flavor psm2
%define testsuite 1
%endif

%if "%{build_flavor}" != "verbs"
%define pack_suff %{?build_flavor:-%{build_flavor}}
%endif

%define module_name mvapich2%{?pack_suff}
%define p_prefix /usr/%_lib/mpi/gcc/%{module_name}
%define p_bindir  %{p_prefix}/bin
%define p_datadir %{p_prefix}/share
%define p_includedir %{p_prefix}/include
%define p_mandir  %{p_datadir}/man
%define p_libdir  %{p_prefix}/%{_lib}
%define p_libexecdir %{p_prefix}/%{_lib}
%define _moduledir /usr/share/modules/gnu-%{module_name}
%define package_name mvapich2%{?pack_suff}
%{bcond_with pmix}
%{bcond_with hwloc}

Name:           %{package_name}
Summary:        OSU MVAPICH2 MPI package
License:        BSD-3-Clause
Group:          Development/Libraries/Parallel
Version:        2.3.7
Release:        0
Source0:        http://mvapich.cse.ohio-state.edu/download/mvapich/mv2/mvapich2-%{version}%{?rc_ver}.tar.gz
Source1:        mpivars.sh
Source2:        mpivars.csh
Source100:      _multibuild
Source101:      README.md
Patch0:         mvapich2-s390_get_cycles.patch
Patch2:         mvapich2-arm-support.patch
# PATCH-FIX-UPSTREAM 0001-Drop-GCC-check.patch (bnc#1129421)
# It's been merged upstream, should be removed with the next release
Patch3:         0001-Drop-GCC-check.patch
Patch4:         reproducible.patch
Patch5:         pass-correct-size-to-snprintf.patch
Patch6:         mvapich2-allow-building-with-external-hwloc.patch
Patch7:         mvapich2-openpa-add-memory-barriers.patch
Patch8:         mrail-fix-incompatible-pointer-issues.patch
Patch9:         util-add-missing-include.patch
Patch10:        psm-add-missing-declaration.patch

## Armv7 specific patches
# PATCH-FIX-UPSTREAM 0001-Drop-real128.patch (https://github.com/pmodels/mpich/issues/4005)
Patch50:        0001-Drop-real128.patch
Patch51:        0001-Drop-Real-16.patch

URL:            http://mvapich.cse.ohio-state.edu
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
BuildRequires:  libtool
BuildRequires:  libtool
BuildRequires:  mpi-selector
%if %{with hwloc}
BuildRequires:  hwloc-devel
%endif
%if %{with pmix}
BuildRequires:  pmix-devel
%endif
%if "%{build_flavor}" == "psm2"
ExclusiveArch:  x86_64
BuildRequires:  libpsm2-devel
%endif
%if "%{build_flavor}" == "verbs"
BuildRequires:  infiniband-diags-devel
BuildRequires:  libibumad-devel
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
%if 0%{?sle_version} <= 120200
BuildRequires:  libibmad-devel
%endif
%endif
Requires:       mpi-selector

%if 0%{?testsuite}
BuildRequires:  %package_name-devel = %{version}
%endif

%description
This is an MPI-3 implementation which includes all MPI-1 features. It
is based on MPICH2 and MVICH.

%if 0%{!?testsuite:1}

%package        devel
Summary:        OSU MVAPICH2 MPI package
Group:          Development/Libraries/Parallel
Requires:       %{name} = %{version}
%if "%{build_flavor}" == "psm2"
Requires:       libpsm2-devel
%endif
%if "%{build_flavor}" == "verbs"
Requires:       libibumad-devel
Requires:       libibverbs-devel
Requires:       librdmacm-devel
%endif
Requires:       gcc-c++
Requires:       gcc-fortran

%description devel
This is an MPI-2 implementation which includes all MPI-1 features.  It
is based on MPICH2 and MVICH.

%package        devel-static
Summary:        OSU MVAPICH2 MPI package - static libraries
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}

%description devel-static
This is an MPI-3 implementation which includes all MPI-1 and MPI-2 features.  It
is based on MPICH2 and MVICH. This package contains the static libraries

%package        doc
Summary:        OSU MVAPICH2 MPI package - Documentation
Group:          Development/Libraries/Parallel
Requires:       %{name} = %{version}

%description  doc
This is an MPI-3 implementation which includes all MPI-1 and MPI-2 features.  It
is based on MPICH2 and MVICH. This package contains the static libraries

%endif # ! testsuite

%prep

%setup -q -n mvapich2-%{version}%{?rc_ver}
%autopatch -M 49 -p0

# Only apply these patches on Armv7
%ifarch armv7hl
%autopatch -m 50 -p0
%endif
cp /usr/share/automake*/config.* .

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

# GCC10 needs an extra flag to allow badly passed parameters
%if 0%{?suse_version} > 1500
export FFLAGS="-fallow-argument-mismatch %{optflags}"
export CFLAGS="-std=gnu17 %{optflags}"
%endif

PERL_USE_UNSAFE_INC=1 autoreconf -fi
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
   --disable-wrapper-rpath \
   --enable-yield=sched_yield \
%if %{with hwloc}
   --with-hwloc=external \
%endif
%if %{with pmix}
   --with-pmix=${_prefix} \
%endif
%if "%{build_flavor}" == "psm2"
   --with-device=ch3:psm \
   --with-psm2=/usr \
%endif
%if "%{build_flavor}" == "verbs"
   --disable-ibv-dlopen \
%endif
  --without-mpe

%if 0%{?testsuite}
%install
rm -rf %{buildroot}/*

%check
# Disable CMA. Modern kernels require specific ptrace capabilities
# that are not available in OBS
export MPIR_CVAR_CH4_CMA_ENABLE=0
for dir in src/mpl src/openpa src/pm/hydra/mpl; do
  (
      cd $dir &&  make check
  )
done

%else
make %{?_smp_mflags} V=1

%install
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
        puts stderr "\tLoads the gnu - mvapich2 %{version}  Environment"
}

module-whatis  "Loads the gnu mvapich2 %{version} Environment."
conflict gnu-mvapich2
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
%dir /usr/%_lib/mpi
%dir /usr/%_lib/mpi/gcc
%dir /usr/share/modules
%dir %{_moduledir}
%{_moduledir}
%doc %{_datadir}/doc/%{name}/COPYRIGHT*
%doc %{_datadir}/doc/%{name}/CHANGE*
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

%files devel
%defattr(-,root,root)
%dir %{p_libdir}/pkgconfig
%{p_mandir}/man3/*
%{p_includedir}
%{p_libdir}/*.so
%{p_libdir}/pkgconfig/mvapich2.pc
%{p_libdir}/pkgconfig/openpa.pc

%files devel-static
%defattr(-,root,root)
%{p_libdir}/*.a

%endif # !testsuite

%changelog
