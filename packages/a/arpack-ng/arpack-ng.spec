#
# spec file for package arpack-ng
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


%define libname libarpack2
%define plibname libparpack2
%define major 	3
%define minor 	0
%define ompi_ver openmpi2

%if 0%{?sles_version}
%define _mpi %ompi_ver mvapich2
%else
%define _mpi %ompi_ver
%endif
Name:           arpack-ng
Version:        3.5.0
Release:        0
Summary:        Fortran77 subroutines for solving large scale eigenvalue problems
License:        BSD-3-Clause
Group:          System/Libraries
Url:            https://github.com/opencollab/arpack-ng
Source0:        https://github.com/opencollab/arpack-ng/archive/%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  %{ompi_ver}-devel
BuildRequires:  autoconf
BuildRequires:  blas-devel
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
Obsoletes:      arpack < %{version}
Provides:       arpack = %{version}
%if 0%{?sles_version}
BuildRequires:  mvapich2-devel
%endif

%description
ARPACK is a collection of Fortran77 subroutines designed to solve
large scale eigenvalue problems.

Arpack-ng is the successor of the legacy Arpack. It is fully compatible
with Arpack.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}-%{release}
Requires:       blas-devel
Requires:       gcc-fortran
Requires:       lapack-devel
Requires:       pkgconfig
Obsoletes:      arpack-devel < %{version}
Provides:       arpack-devel = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n %{libname}
Summary:        Files needed for developing arpack based applications
Group:          System/Libraries
Provides:       %{libname}_%{major}_%{minor} = %{version}
Obsoletes:      %{libname}_%{major}_%{minor} < %{version}

%description -n %{libname}
ARPACK is a collection of Fortran77 subroutines designed to solve
large scale eigenvalue problems. This package contains the so
library links used for building arpack based applications.

%package     -n parpack-openmpi
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{plibname}-openmpi = %{version}

%description -n parpack-openmpi
ARPACK is a collection of Fortran77 subroutines designed to solve
large scale eigenvalue problems.

Arpack-ng is the successor of the legacy Arpack. It is fully compatible
with Arpack.

%package     -n parpack-openmpi-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{plibname}-openmpi = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       openmpi-devel

%description     -n parpack-openmpi-devel
The %{name}-openmpi-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n %{plibname}-openmpi
Summary:        Files needed for developing arpack based applications
Group:          System/Libraries
Provides:       %{plibname}_%{major}_%{minor} = %{version}
Obsoletes:      %{plibname}_%{major}_%{minor} < %{version}
Requires:       %{ompi_ver}-libs

%description -n %{plibname}-openmpi
ARPACK is a collection of Fortran77 subroutines designed to solve
large scale eigenvalue problems. This package contains the so
library links used for building arpack based applications.

%if 0%{?sles_version}
%package     -n parpack-mvapich2
Summary:        Development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{plibname}-mvapich2 = %{version}
Requires:       mvapich2

%description     -n parpack-mvapich2
ARPACK is a collection of Fortran77 subroutines designed to solve
large scale eigenvalue problems.

Arpack-ng is the successor of the legacy Arpack. It is fully compatible
with Arpack.

%package     -n parpack-mvapich2-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{plibname}-mvapich2 = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       mvapich2-devel

%description -n parpack-mvapich2-devel
The %{name}-mvapich2-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n %{plibname}-mvapich2
Summary:        Files needed for developing arpack based applications
Group:          System/Libraries
Provides:       %{plibname}_%{major}_%{minor} = %{version}
Obsoletes:      %{plibname}_%{major}_%{minor} < %{version}

%description -n %{plibname}-mvapich2
ARPACK is a collection of Fortran77 subroutines designed to solve
large scale eigenvalue problems. This package contains the so
library links used for building arpack based applications.
%endif

%prep
%setup -q
set -- *

cp -r EXAMPLES examples

for i in %{_mpi}
do
    mkdir arpack-ng-$i
    cp -ap "$@" arpack-ng-$i
done

%build
sh bootstrap
%configure --disable-static

make %{?_smp_mflags}

for i in %{_mpi}
do
    pushd arpack-ng-$i

    export F77=%{_libdir}/mpi/gcc/$i/bin/mpif77
    export MPIF77=%{_libdir}/mpi/gcc/$i/bin/mpif77
    export LD_LIBRARY_PATH=%{_libdir}/mpi/gcc/$i/%{_lib}
    %define _prefix /usr/%{_lib}/mpi/gcc/\$i

    sh bootstrap
    %configure --disable-static \
               --enable-mpi
    make %{?_smp_mflags}

    # `make check` is necessary to build the test programs for PARPACK.
    # TODO: Verify if we really want to include those tests in the package.
    make check

    popd
done

# Set prefix to default value
%define _prefix /usr

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

for i in %{_mpi}
do
    pushd arpack-ng-$i

    make %{?_smp_mflags} DESTDIR=%{buildroot} install
    rm -rf %{buildroot}%{_libdir}/mpi/gcc/$i/%{_lib}/libarpack.*

    # Install the test programs.
    mkdir -p %{buildroot}%{_libdir}/mpi/gcc/$i/bin/

    pushd PARPACK/EXAMPLES/MPI

    libtool --mode=install install -Dm755 pcndrv1 %{buildroot}%{_libdir}/mpi/gcc/$i/bin/
    libtool --mode=install install -Dm755 pdndrv1 %{buildroot}%{_libdir}/mpi/gcc/$i/bin/
    libtool --mode=install install -Dm755 pdndrv3 %{buildroot}%{_libdir}/mpi/gcc/$i/bin/
    libtool --mode=install install -Dm755 pdsdrv1 %{buildroot}%{_libdir}/mpi/gcc/$i/bin/
    libtool --mode=install install -Dm755 psndrv1 %{buildroot}%{_libdir}/mpi/gcc/$i/bin/
    libtool --mode=install install -Dm755 psndrv3 %{buildroot}%{_libdir}/mpi/gcc/$i/bin/
    libtool --mode=install install -Dm755 pssdrv1 %{buildroot}%{_libdir}/mpi/gcc/$i/bin/
    libtool --mode=install install -Dm755 pzndrv1 %{buildroot}%{_libdir}/mpi/gcc/$i/bin/

    popd

    popd
done

%check
make %{?_smp_mflags} check

for i in %{_mpi}
do
    pushd arpack-ng-$i
    make check
    popd
done

%post   -n %{libname}           -p /sbin/ldconfig
%postun -n %{libname}           -p /sbin/ldconfig
%post   -n %{plibname}-openmpi  -p /sbin/ldconfig
%postun -n %{plibname}-openmpi  -p /sbin/ldconfig

%if 0%{?sles_version}
%post   -n %{plibname}-mvapich2 -p /sbin/ldconfig
%postun -n %{plibname}-mvapich2 -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root,-)
%doc CHANGES COPYING README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc examples
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n parpack-openmpi
%defattr(-,root,root,-)
%{_libdir}/mpi/gcc/%{ompi_ver}/bin/p??drv?

%files -n %{plibname}-openmpi
%defattr(-,root,root,-)
%{_libdir}/mpi/gcc/%{ompi_ver}/%{_lib}/lib*arpack.so.*

%files -n parpack-openmpi-devel
%defattr(-,root,root,-)
%{_libdir}/mpi/gcc/%{ompi_ver}/%{_lib}/libparpack.so
%{_libdir}/mpi/gcc/%{ompi_ver}/%{_lib}/libparpack.la
%dir %{_libdir}/mpi/gcc/%{ompi_ver}/%{_lib}/pkgconfig
%{_libdir}/mpi/gcc/%{ompi_ver}/%{_lib}/pkgconfig/*.pc

%if 0%{?sles_version}
%files -n parpack-mvapich2
%defattr(-,root,root,-)
%{_libdir}/mpi/gcc/mvapich2/bin/p??drv?

%files -n %{plibname}-mvapich2
%defattr(-,root,root,-)
%{_libdir}/mpi/gcc/mvapich2/%{_lib}/libparpack.so.*

%files -n parpack-mvapich2-devel
%defattr(-,root,root,-)
%{_libdir}/mpi/gcc/mvapich2/%{_lib}/libparpack.so
%{_libdir}/mpi/gcc/mvapich2/%{_lib}/libparpack.la
%dir %{_libdir}/mpi/gcc/%{ompi_ver}/%{_lib}/pkgconfig
%{_libdir}/mpi/gcc/mvapich2/%{_lib}/pkgconfig/*.pc
%endif

%changelog
