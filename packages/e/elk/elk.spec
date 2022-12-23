#
# spec file for package elk
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

%define pname elk

# SECTION multibuild definitions

%if "%{flavor}" == "openmpi1"
%global mpi_flavor openmpi
 %if 0%{?suse_version} >= 1550
 %define mpi_vers 1
 %else
 %define mpi_vers %{nil}
 %endif
%endif

%if "%{flavor}" == "openmpi2"
%global mpi_flavor openmpi
%define mpi_vers 2
%endif

%if "%{flavor}" == "openmpi3"
%global mpi_flavor openmpi
%define mpi_vers 3
%endif

%if "%{flavor}" == "openmpi4"
%global mpi_flavor openmpi
%define mpi_vers 4
%endif

%if "%{flavor}" == "openmpi5"
%if 0%{?suse_version} < 1550
ExclusiveArch: do_not_build
%endif
%global mpi_flavor openmpi
%define mpi_vers 5
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_mpi:%{!?mpi_flavor:error "No MPI family specified!"}}

# For compatibility package names
%define mpi_ext %{?mpi_vers}

%if %{without mpi}
 %define my_prefix %{_prefix}
 %define my_bindir %{_bindir}
%else
 %define my_prefix %{_libdir}/mpi/gcc/%{mpi_flavor}%{?mpi_ext}
 %define my_bindir %{my_prefix}/bin
 %define my_suffix -%{mpi_flavor}%{?mpi_ext}
%endif
# /SECTION

Name:           %{pname}%{?my_suffix}
Version:        8.6.7
Release:        0
Summary:        An all-electron full-potential linearised augmented-planewave code
License:        GPL-3.0-or-later
URL:            https://elk.sourceforge.net
Source0:        https://download.sf.net/project/%{pname}/%{pname}-%{version}.tgz
Source1:        %{pname}.rpmlintrc
BuildRequires:  fdupes
BuildRequires:  blas-devel
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libxc)
BuildRequires:  wannier90%{?my_suffix}-devel
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{mpi_vers}-devel
BuildRequires:  %{mpi_flavor}%{mpi_vers}-macros-devel
%openmpi_requires
%endif
# Needed to break degeneracies between multiple openmpi flavours
Requires:       wannier90%{?my_suffix}-devel

%description
An all-electron full-potential linearised augmented-plane wave
(FP-LAPW) code with many features. The code is designed to be as
simple as possible so that new developments in the field of density
functional theory (DFT) can be added quickly and reliably.

%if %{with mpi}
This flavour of elk is built with %{mpi_flavor}%{mpi_vers}
parallelisation support.
%endif

%package -n %{pname}-data
Summary:        Common data files for use with %{pname}
BuildArch:      noarch

%description -n %{pname}-data
This package provides common data files for use with any flavour of
elk.

%package -n %{pname}-utils
Summary:        Utilities used to analyse results from elk
Requires:       %{pname}-data = %{version}
Requires:       awk
Requires:       gnuplot
BuildArch:      noarch

%description -n %{pname}-utils
This package provides utilities useful for analysis elk outputs.

%prep
%autosetup -n %{pname}-%{version}

# Remove pre-configured make.inc
rm make.inc

sed -Ei "1{s@/usr/bin/python@%{_bindir}/python3@}" \
  utilities/blocks2columns/blocks2columns.py \
  utilities/elk-optics/elk-optics.py

%build
%if %{with mpi}
%setup_openmpi
%endif

# Generate the make.inc file (based on setup and make.defs scripts)
cat << EOF | tee make.inc
MAKE      = make
AR        = ar
%if %{with mpi}
F90       = mpif90
SRC_MPI   =
%else
F90       = gfortran
SRC_MPI   = mpi_stub.f90
%endif
%if 0%{?suse_version} >= 1550
F90_OPTS  = %{optflags} %{?_fmoddir:-I%{_fmoddir}} -fallow-argument-mismatch -fopenmp
%else
F90_OPTS  = %{optflags} %{?_fmoddir:-I%{_fmoddir}} -fopenmp
%endif
F90_LIB   = -llapack -lblas -lfftw3 -lfftw3f
SRC_FFT   = zfftifc_fftw.f90 cfftifc_fftw.f90
LIB_LIBXC = -lxc -lxcf90
SRC_LIBXC = libxcf90.f90 libxcifc.f90
LIB_W90   = -lwannier
SRC_W90S  =

# We do not use MKL, BLIS, or OBLAS
SRC_MKL   = mkl_stub.f90
SRC_BLIS  = blis_stub.f90
SRC_OBLAS = oblas_stub.f90
EOF

# Parallel make unsupported!
pushd src
%make_build -j1 elk
popd
for d in eos spacegroup
do
  pushd src/${d}
  %make_build -j1 ${d}
  popd
done

%install
install -d %{buildroot}/%{my_bindir}
install -m 0755 src/elk %{buildroot}/%{my_bindir}/
install -m 0755 src/eos/eos %{buildroot}/%{my_bindir}/
install -m 0755 src/spacegroup/spacegroup %{buildroot}/%{my_bindir}/

%if %{without mpi}
# Only for common flavour
mkdir -p %{buildroot}/%{_datadir}/%{pname}

# Common data
cp -a species tests examples %{buildroot}/%{_datadir}/%{pname}/

# Different utilities
install -m 0755 utilities/elk-bands/elk-bands %{buildroot}%{_bindir}/
install -m 0755 utilities/blocks2columns/blocks2columns.py %{buildroot}%{_bindir}/elk-blocks2columns
install -m 0755 utilities/elk-optics/elk-optics.py %{buildroot}%{_bindir}/elk-optics
install -m 0755 utilities/wien2k-elk/se.pl %{buildroot}%{_bindir}/wien2k-elk

%fdupes %{buildroot}%{_datadir}/
%endif

%check
pushd tests

%if %{with mpi}
%setup_openmpi
%endif

# Based on tests/test{,-mpi}.sh script
for d in test_*
do
  cd ${d}
  export OMP_NUM_THREADS=`echo %{?_smp_mflags} | sed "s/-j//"`
  export OMP_STACKSIZE=20M

  # Note that some tests run for upwards of 30 mins, slowing the build down
  # considerably; so timeout each test within 2 mins at a maximum and move on
  #
  timeout 120 %{?with_mpi:mpirun -n 1} \
    %{buildroot}%{my_bindir}/elk > test.log || { echo "Test $d timed out after 120s."; true; }

  # If test.log mentions 'Error', print log and abort build
  grep -E "\<Error\>" > test.log \
    && { cat test.log; exit 1; } \
    || { true; rm -f *.OUT test.log fort.* gmon.out; }

  cd -
done
popd

%files
%license COPYING
%doc README release_notes.txt
%{my_bindir}/elk
%{my_bindir}/eos
%{my_bindir}/spacegroup

%if %{without mpi}
%files data
%{_datadir}/%{pname}/

%files utils
%{_bindir}/elk-bands
%{_bindir}/elk-blocks2columns
%{_bindir}/elk-optics
%{_bindir}/wien2k-elk
%endif

%changelog
