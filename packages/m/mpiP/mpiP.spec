#
# spec file for package mpiP
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

%define pname mpiP

%if 0%{?sle_version:1} && 0%{?sle_version} < 150300
%define DisOMPI4 ExclusiveArch:  do_not_build
%endif
%if 0%{?sle_version:1} && 0%{?sle_version} < 160000
%define DisOMPI5 ExclusiveArch:  do_not_build
%endif

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%define p_suffix %{nil}
%else
%define p_suffix -%{flavor}
%endif

%if "%{flavor}" == "openmpi4"
%{?DisOMPI4}
%endif

%if "%{flavor}" == "openmpi5"
ExcludeArch:    %{ix86} %{arm}
%{?DisOMPI5}
%endif

%define package_name %{pname}%{p_suffix}
%define p_prefix %{_libdir}/mpi/gcc/%{flavor}

%define p_bindir %{p_prefix}/bin
%define p_datadir %{p_prefix}/share
%define p_incdir %{p_prefix}/include/
%define p_libdir %{p_prefix}/%{_lib}/
%define p_libexecdir %{p_prefix}/%{_lib}
%define p_mandir %{p_prefix}/share/man

Name:           %{package_name}
Summary:        A profiling library for MPI applications
License:        BSD-3-Clause
Group:          Development/Tools/Debuggers
Version:        3.5
Release:        0
ExcludeArch:    i586 %arm s390
URL:            https://github.com/LLNL/mpiP
Source0:        https://github.com/LLNL/mpiP/releases/download/%{version}/mpip-%{version}.tgz#/%{pname}-%{version}.tgz
Source100:      README.md
Patch1:         mpip.unwinder.patch
Patch2:         Add-return-value-to-non-void-function.patch
Patch3:         pc_lookup-replace-PTR-with-void.patch
Patch4:         configure-fix-compilation-error-for-GCC-14.patch
Patch5:         arch-add-generic-arch-using-GCC-builtins.patch
Patch6:         reproducible.patch
Patch7:         configure-fix-fPIC-on-aarch64.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  binutils-devel
BuildRequires:  dejagnu
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libunwind-devel
BuildRequires:  python3
Requires:       %{flavor}

%description
mpiP is a profiling library for MPI applications.
It only collects statistical information about MPI functions, so mpiP
generates less overhead and much less data than tracing
tools. All the information captured by mpiP is task-local. It only
uses communication during report generation, typically at the end of
the experiment, to merge results from all of the tasks into one output
file.

%package devel
Summary:        Headers for profiling library for MPI applications
Group:          Development/Libraries/C and C++

%description devel
mpiP is a profiling library for MPI applications. This packages contains
the build headers.

%package devel-static
Summary:        Static version of profiling library for MPI applications
Group:          Development/Libraries/C and C++

%description devel-static
mpiP is a profiling library for MPI applications.

This package contains the static libraries.

%package doc
Summary:        Documentation for the mpiP profiling library
Group:          Documentation/Other

%description doc
mpiP is a profiling library for MPI applications.

This contains the documentation.

%prep
%setup -q -n %{pname}-%{version}
%autopatch -p0
sed -i -e "/-shared -o \$@/s#\(\${LDFLAGS}\)#\1 -Wl,-soname,\$@#" Makefile.in

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CC=gcc
source %{p_bindir}/mpivars.sh

export CC=mpicc
export CXX=mpicxx
export FC=mpifort
export F77=$FC
export CFLAGS="-D__DATE__=\\\"NODATE\\\" -D__TIME__=\\\"NOTIME\\\""
export FFLAGS="-std=legacy"
export HAVE_PYTHON="python3"
%configure \
  --prefix=%{p_prefix} \
  --exec-prefix=%{p_prefix} \
  --datadir=%{p_datadir} \
  --bindir=%{p_bindir} \
  --includedir=%{p_incdir} \
  --libdir=%{p_libdir} \
  --libexecdir=%{p_libexecdir} \
  --mandir=%{p_mandir} \
    --enable-demangling \
%ifarch aarch64
    --enable-setjmp \
%endif
    --docdir=%{_docdir}/%{name}

make %{?_smp_mflags} PYTHON="python3" shared

%install
source %{p_bindir}/mpivars.sh

make install-all DESTDIR=%{?buildroot}
find "%{buildroot}" -type f -name "*.a" -exec chmod a-x {} +
find "%{buildroot}/%{_docdir}" -type f -exec chmod a-x {} +
find "%{buildroot}/%{p_incdir}" -type f -exec chmod a-x {} +
for i in mpirun-mpip srun-mpip; do
    sed -i \
	-e "s@\(MPIP_DIR=\).*@\1%{?p_prefix}@" \
	-e "s@\(LD_PRELOAD=\).*:\(.*\)@\1\2@" \
	-e "s@\(ADDTL_RT_LIBS=.*\)@#\1@" \
	-e "s@/lib/libmpiP.so@/%{_lib}/libmpiP.so@" %{buildroot}%{p_bindir}/$i
done

%check
source %{p_bindir}/mpivars.sh
export CC=mpicc
export CXX=mpicxx
export FC=mpifort
export F77=$FC
export FFLAGS="-std=legacy"
LD_LIBRARY_PATH=$(pwd)${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make FFLAGS+=${FFLAGS} check || exit 0

%files
%{p_libdir}/*so
%{p_bindir}

%files doc
%{_docdir}/%{name}/

%files devel
%{p_incdir}

%files devel-static
%{p_libdir}/*.a

%changelog
