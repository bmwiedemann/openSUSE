#
# spec file for package adios
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


%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

%global mpi_flavor @BUILD_FLAVOR@%{nil}

%define pname adios

%if "%{mpi_flavor}" == ""
ExclusiveArch:  do_not_build
%global p_suffix %{nil}
%else
%global p_suffix -%{mpi_flavor}
%endif

# No netcdf on s390 and 32bit platforms
ExcludeArch:    s390 s390x i586 %arm

%if "%{mpi_flavor}" == "openmpi5"
%if 0%{?suse_version} < 1600
ExclusiveArch:  do_not_build
%else
ExcludeArch:    %{ix86} %{arm}
%endif
%endif

%define p_prefix %{_libdir}/mpi/gcc/%{mpi_flavor}

%define p_bindir %{p_prefix}/bin/
%define p_libdir %{p_prefix}/%{_lib}/
%define p_incdir %{p_prefix}/include/
%define p_datadir %{p_prefix}/share/
%define p_sysconfdir %{p_prefix}/etc/
%define p_skeldir %{p_prefix}/etc/skel/

%if 0%{?suse_version} >= 1500
%define my_py_version 3
%endif

Name:           adios%{?p_suffix}
Version:        1.13.1
Release:        0
Summary:        The Adaptable IO System (ADIOS)
License:        BSD-2-Clause AND BSD-3-Clause AND LGPL-2.1-or-later
Group:          Productivity/Scientific/Other
URL:            https://www.olcf.ornl.gov/center-projects/adios/
Source0:        https://users.nccs.gov/~pnorbert/adios-%{version}.tar.gz
Patch0:         adios-correct-func-ret.patch
Patch1:         Fix-code-to-be-python3-compliant.patch
BuildRequires:  %{mpi_flavor}-devel
BuildRequires:  autoconf
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5%{?p_suffix}-devel
BuildRequires:  libbz2-devel
BuildRequires:  liblz4-devel
BuildRequires:  netcdf%{?p_suffix}-devel
BuildRequires:  python%{?my_py_version}
BuildRequires:  zlib-devel
Requires:       python%{?my_py_version}-PyYAML
Requires:       python%{?my_py_version}-xml

%description
The Adaptable IO System (ADIOS) provides a way for scientists to
describe the data in their code that may need to be written, read, or
processed outside of the running simulation. By providing an external
to the code XML file describing the various elements, their types,
and how one wishes to process them for a particular run, the routines
in the host code (either FORTRAN or C) can transparently change how
they process the data.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{name} = %{version}
Requires:       %{name}-devel-static = %{version}
Requires:       hdf5%{?p_suffix}-devel
Requires:       netcdf%{?p_suffix}-devel

%description devel
The Adaptable IO System (ADIOS) provides a way for scientists to
describe the data in their code that may need to be written, read, or
processed outside of the running simulation.

This package contains all files needed to create projects that use
the %{flavor} version of ADIOS.

%package devel-static
Summary:        Static libraries for %{name}
Group:          Development/Libraries/Parallel

%description devel-static
The Adaptable IO System (ADIOS) provides a way for scientists to
describe the data in their code that may need to be written, read, or
processed outside of the running simulation.

This package contains all the static libraries needed to create projects
that use the %{flavor} version of ADIOS.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build

export CC=gcc
export CXX=g++
export F77=gfortran
export F9X=gfortran
export FC=gfortran
export MPICC=mpicc
export MPICXX=mpicxx
export MPIFC=mpif90
export CFLAGS="-fPIC %{optflags} -std=gnu11"
%if 0%{?suse_version} >= 1550
# https://github.com/ornladios/ADIOS/issues/206
export FCFLAGS="-fPIC %{optflags} -fallow-argument-mismatch"
%else
export FCFLAGS="-fPIC %{optflags}"
%endif
export LDFLAGS="-pie"

export MPICC="%{p_bindir}/mpicc"
export MPIFC="%{p_bindir}/mpif90"
export PATH=${PATH}:%{p_bindir}
export LDFLAGS="${LDFLAGS} -L%{p_libdir}"
export LD_LIBRARY_PATH="%{p_libdir}"
%configure \
  --prefix=%{p_prefix} \
  --exec-prefix=%{_prefix} \
  --bindir=%{p_bindir} \
  --libdir=%{p_libdir} \
  --includedir=%{p_incdir} \
  --sysconfdir=%{p_sysconfdir} \
  --datadir=%{p_datadir} \
  --docdir=%{_docdir}/%{name} \
  --enable-fortran \
  --with-phdf5="%{p_prefix}" \
  --with-netcdf="%{p_prefix}" \
  --with-zlib="%{_prefix}" \
  --with-bzip2="%{_libdir}" \
  --with-lz4="%{_libdir}" \
  --without-evpath \
  --without-fastbit \
  --without-ffs \

%make_build

%install
%make_install
for i in %{buildroot}/%{p_bindir}/{skel,*.py} %{buildroot}/%{p_libdir}/python/*.py; do
    sed -e '1s@^\(#!.*\)\(python\)[23]*\( *.*\)@\1\2%{?my_py_version}\3@' -e '1s@/\env @/@' -i $i
done
%fdupes -s %{buildroot}/%{p_skeldir}/templates

%files
%{p_bindir}
%config %{p_sysconfdir}/*
%dir %{p_prefix}/etc
%{p_skeldir}
%{p_libdir}/python
%license COPYING
%doc AUTHORS KNOWN_BUGS NEWS README.md TODO

%files devel
%{p_incdir}

%files devel-static
%{p_libdir}/*.a

%changelog
