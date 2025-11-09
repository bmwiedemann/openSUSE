#
# spec file for package mpich
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%nil

# Static libraries are disabled by default
# for non HPC builds
# To enable them, simply uncomment:
# % define build_static_devel 1

%define pname mpich

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

%if "%{build_flavor}" != "ucx"
%define pack_suff %{?build_flavor:-%{build_flavor}}
%endif

%if "%{build_flavor}" == "ucx"
%ifarch %ix86 %arm
# UCX is not available on 32b system so silently fallback
# on ch4:ofi
%define build_flavor ofi
%endif
%endif

%define module_name mpich%{?pack_suff}
%define p_prefix /usr/%_lib/mpi/gcc/%{module_name}
%define p_bindir  %{p_prefix}/bin
%define p_datadir %{p_prefix}/share
%define p_includedir %{p_prefix}/include
%define p_mandir  %{p_datadir}/man
%define p_libdir  %{p_prefix}/%{_lib}
%define p_libexecdir %{p_prefix}/%{_lib}
%define p_sysconfdir %{p_prefix}/%{_sysconfdir}
%define _moduledir /usr/share/modules/gnu-%{module_name}
%define package_name %{pname}%{?pack_suff}

Name:           %{package_name}%{?testsuite:-testsuite}
Version:        4.3.2
Release:        0
Summary:        High-performance and widely portable implementation of MPI
License:        MIT
Group:          Development/Libraries/Parallel
URL:            http://www.mpich.org/
Source0:        http://www.mpich.org/static/downloads/%{version}/mpich-%{version}.tar.gz
Source1:        mpivars.sh
Source2:        mpivars.csh
Source100:      _multibuild
Source101:      README.md
Patch1:         autogen-only-deal-with-json-yaksa-if-enabled.patch
Patch2:         autoconf-pull-dynamic-and-not-static-libs-from-pkg-config.patch
Patch3:         romio-test-fix-bad-snprintf-arguments.patch
Patch4:         ch4-shm-fix-data-type-for-recv_bytes-in-MPIDI_POSIX_mpi_release_gather_release.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  fdupes
BuildRequires:  libjson-c-devel
BuildRequires:  libtool
BuildRequires:  pkg-config

%ifnarch s390 s390x %{arm} ppc64
BuildRequires:  valgrind-devel
%endif
%ifnarch s390 s390x armv7hl
BuildRequires:  libnuma-devel
%endif
BuildRequires:  libtool
BuildRequires:  libtool
BuildRequires:  mpi-selector
BuildRequires:  python3-devel
BuildRequires:  hwloc-devel >= 2.0

%if "%{build_flavor}" == "ofi"
BuildRequires:  libfabric-devel
%endif

%if "%{build_flavor}" == "ucx"
BuildRequires:  libucm-devel >= 1.7.0
BuildRequires:  libucp-devel >= 1.7.0
BuildRequires:  libucs-devel >= 1.7.0
BuildRequires:  libuct-devel >= 1.7.0
# UCX is only available for 64b archs
ExcludeArch:    %ix86 %arm
%endif
Provides:       mpi
BuildRequires:  Modules
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  mpi-selector
Requires:       mpi-selector
Requires(preun): mpi-selector

%if 0%{?testsuite}
BuildRequires:  %package_name-devel = %{version}
%endif

%description
MPICH is a high performance and widely portable implementation of the Message
Passing Interface (MPI) standard.

The goals of MPICH are:

 * to provide an MPI implementation that efficiently supports different
   computation and communication platforms including commodity clusters
   (desktop systems, shared-memory systems, multicore architectures),
   high-speed networks and proprietary high-end computing systems
   (Blue Gene, Cray)
 * to enable cutting-edge research in MPI through an easy-to-extend modular
   framework for other derived implementations

%if 0%{!?testsuite:1}

%package devel
Summary:        SDK for MPICH version %{version}
Group:          Development/Libraries/Parallel
Requires:       %{name} = %{version}
Requires:       %{name} = %{version}
Requires:       libstdc++-devel

%description devel
MPICH is a freely available, portable implementation of MPI, the
Standard for message-passing libraries. This package contains manpages,
headers and libraries needed for developing MPI applications.

This RPM contains all the wrappers necessary to compile, link, and run
Open MPI jobs.

%if 0%{?build_static_devel}
%package        devel-static
Summary:        Static libraries for MPICH  version %{version}
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}

%description devel-static
MPICH is a freely available, portable implementation of MPI, the
Standard for message-passing libraries. This package contains manpages,
headers and libraries needed for developing MPI applications.

This RPM contains the static library files, which are packaged separately from
the dynamic library and headers.
%endif

%endif # ! testsuite

%prep
echo FLAVOR %{flavor}
%autosetup -p0 -n mpich-%{version}%{?rc_ver}

# Make sure prebuilt dependencies are used and not mpich submodules
rm -R modules/{ucx,libfabric,json-c}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

# GCC10 needs an extra flag to allow badly passed parameters
%if 0%{?suse_version} > 1500
export FFLAGS="-fallow-argument-mismatch %{optflags}"
export FCFLAGS="-fallow-argument-mismatch %{optflags}"
%endif
%ifarch aarch64
# For some reason, configure has random issue with defining this
# on aarch64 only. Set it to avoid random failure
export CROSS_F77_SIZEOF_INTEGER=4
%endif
autoreconf -fi
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
    --sysconfdir=%{p_sysconfdir} \
    --disable-rpath      \
    --disable-wrapper-rpath      \
    --with-hwloc \
%if "%{build_flavor}" == "ofi"
   --with-ofi \
   --with-device=ch4:ofi \
%endif
%if "%{build_flavor}" == "ucx"
   --with-ucx \
   --with-device=ch4:ucx \
%endif
	CFLAGS="%optflags -fPIC"			\
	CXXLAGS="%optflags -fPIC"			\
	MPICHLIB_CFLAGS="%{optflags}"			\
	MPICHLIB_CXXFLAGS="%{optflags}"

%if 0%{?testsuite}
%install
rm -rf %{buildroot}/*

%check
# Disable CMA. Modern kernels require specific ptrace capabilities
# that are not available in OBS
export MPIR_CVAR_CH4_CMA_ENABLE=0
for dir in src/mpl src/mpi/romio/test; do
  (
      cd $dir &&  make check
  )
done

%else
make %{?_smp_mflags} VERBOSE=1

%install
make DESTDIR=%{buildroot} install

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
# sanitize .la files
%if !0%{?build_static_devel}
find %{buildroot} -name "*.a" -delete
%endif

%fdupes %{buildroot}%{p_mandir}
%fdupes %{buildroot}%{p_datadir}
%fdupes %{buildroot}%{p_libdir}/pkgconfig

# make and install mpivars files
install -m 0755 -d %{buildroot}%{_bindir}
sed -e 's,prefix,%p_prefix,g' -e 's,libdir,%{p_libdir},g' %{S:1} > %{buildroot}%{p_bindir}/mpivars.sh
sed -e 's,prefix,%p_prefix,g' -e 's,libdir,%{p_libdir},g' %{S:2} > %{buildroot}%{p_bindir}/mpivars.csh

mkdir -p %{buildroot}%{_moduledir}

cat << EOF > %{buildroot}%{_moduledir}/%{version}
#%%Module
proc ModulesHelp { } {
        global dotversion
        puts stderr "\tLoads the gnu - mpich %{version}  Environment"
}

module-whatis  "Loads the gnu mpich %{version} Environment."
conflict gnu-mpich
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

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%fdupes -s %{buildroot}

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
%defattr(-,root,root)
%doc CHANGES COPYRIGHT README README.envvar
%dir /usr/%_lib/mpi
%dir /usr/%_lib/mpi/gcc
%dir /usr/share/modules
%doc %{_datadir}/doc/*
%dir %{p_prefix}
%dir %{p_bindir}
%dir %{p_datadir}
%dir %{p_includedir}
%dir %{p_mandir}
%dir %{p_mandir}/man1
%dir %{p_mandir}/man3
%dir %{p_libdir}
%{_moduledir}
%{p_bindir}/*
%{p_mandir}/man1/*
%{p_libdir}/*.so.*
%{p_sysconfdir}

%files devel
%defattr(-,root,root)
%dir %{p_libdir}/pkgconfig
%{p_mandir}/man3/*
%{p_includedir}
%{p_libdir}/*.so
%{p_libdir}/pkgconfig/mpich.pc

%if 0%{?build_static_devel}
%files devel-static
%defattr(-,root,root)
%{p_libdir}/*.a
%endif

%endif # !testsuite

%changelog
