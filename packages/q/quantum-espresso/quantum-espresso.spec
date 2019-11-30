#
# spec file for package quantum-espresso
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


%if 0%{?sles_version}
%define _mvapich2 1
%endif
%if 0%{?suse_version}
%define _openmpi 1
%endif

%if 0%{?suse_version} >= 1550
%define omp_ver 1
%else
%define omp_ver %{nil}
%endif

%define _mpi %{?_openmpi:openmpi}%{omp_ver} %{?_mvapich2:mvapich2}

Name:           quantum-espresso
Version:        6.4.1
Release:        0
Summary:        A suite for electronic-structure calculations and materials modeling
License:        GPL-2.0-only
Group:          Productivity/Scientific/Physics
Url:            http://www.quantum-espresso.org
Source0:        https://gitlab.com/QEF/q-e/-/archive/qe-%{version}/q-e-qe-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM backports-6.4.1.git-diff badshah400@gmail.com -- Backported fixes for version 6.4.1 from upstream
Patch0:         https://gitlab.com/QEF/q-e/wikis/uploads/3e4b6d3844989c02d0ebb03a935e1976/backports-6.4.1.git-diff
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
%if 0%{?_openmpi}
BuildRequires:  openmpi%{omp_ver}-devel
%endif
%if 0%{?_mvapich2}
BuildRequires:  mvapich2-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64

%description
Quantum ESPRESSO is an integrated suite of Open-Source computer codes for
electronic-structure calculations and materials modeling at the nanoscale.
It is based on density-functional theory, plane waves, and pseudopotentials.

%package doc
Summary:        Documentation files for Quantum Espresso
Group:          Documentation/Other

%description doc
This package contains the documentation files for Quantum Espresso.

Quantum ESPRESSO is an integrated suite of Open-Source computer codes for
electronic-structure calculations and materials modeling at the nanoscale.
It is based on density-functional theory, plane waves, and pseudopotentials.

%package openmpi
Summary:        A suite for electronic-structure calculations and materials modeling
Group:          Productivity/Scientific/Physics

%description openmpi
Quantum ESPRESSO is an integrated suite of Open-Source computer codes for
electronic-structure calculations and materials modeling at the nanoscale.
It is based on density-functional theory, plane waves, and pseudopotentials.

This package contains the nespresso binary compiled with openmpi support.

%if 0%{?sles_version}
%package mvapich2
Summary:        A suite for electronic-structure calculations and materials modeling
Group:          Productivity/Scientific/Physics

%description mvapich2
Quantum ESPRESSO is an integrated suite of Open-Source computer codes for
electronic-structure calculations and materials modeling at the nanoscale.
It is based on density-functional theory, plane waves, and pseudopotentials.

This package contains the nespresso binary compiled with mvapich2 support.
%endif

%prep
%autosetup -p1 -n q-e-qe-%{version}

echo "prepare parallel builds: %_mpi"
set -- *
for i in %_mpi
do
    mkdir espresso-$i
    cp -ap "$@" espresso-$i
done

%build
%configure --disable-parallel
make all

for mpi in %_mpi;
do
cd espresso-$mpi
export CC="%{_libdir}/mpi/gcc/$mpi/bin/mpicc"
export FC="%{_libdir}/mpi/gcc/$mpi/bin/mpif90"
export F77="%{_libdir}/mpi/gcc/$mpi/bin/mpif77"
%configure --enable-parallel
make all
cd ..
done

%install
mkdir -p %{buildroot}%{_bindir}
cd bin
for bin in *.x; do
    install -m 755 $bin %{buildroot}%{_bindir}/qe_$bin
done
cd ..

for mpi in %_mpi;
do
 mkdir -p %{buildroot}%{_libdir}/mpi/gcc/$mpi/bin
 cd espresso-$mpi/bin
   for bin in *.x; do
     install -m 755 $bin %{buildroot}%{_libdir}/mpi/gcc/$mpi/bin/qe_$bin
   done
 cd ../..
done

%fdupes -s Doc/

%files
%defattr(-,root,root)
%doc README.md
%license License
%{_bindir}/*.x

%files openmpi
%defattr(-,root,root)
%doc README.md
%license License
%{_libdir}/mpi/gcc/openmpi%{omp_ver}/bin/*.x

%if 0%{?sles_version}
%files mvapich2
%defattr(-,root,root)
%doc README.md
%license License
%{_libdir}/mpi/gcc/mvapich2/bin/*.x
%endif

%files doc
%defattr(-,root,root)
%doc Doc/*

%changelog
