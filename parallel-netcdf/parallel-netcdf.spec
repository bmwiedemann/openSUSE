#
# spec file for package parallel-netcdf
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%if 0%{?sles_version}
%define _mvapich2 1
%endif
%if 0%{?suse_version}
%define _openmpi 1
%endif

%define _mpi %{?_openmpi:openmpi} %{?_mvapich2:mvapich2}

Name:           parallel-netcdf
%define libname libpnetcdf
Version:        1.7.0
Release:        0
%define sonum   1
Summary:        High-performance parallel I/O with the NetCDF scientific data format
License:        NetCDF
Group:          Productivity/Scientific/Other
Url:            http://cucis.ece.northwestern.edu/projects/PnetCDF/index.html
Source0:        http://cucis.ece.northwestern.edu/projects/PnetCDF/Release/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE parallel-netcdf-1.6.1-destdir.patch Fix install directories
Patch0:         parallel-netcdf-1.6.1-destdir.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  pkg-config
%if 0%{?_openmpi}
BuildRequires:  openmpi-devel
%endif
%if 0%{?_mvapich2}
BuildRequires:  mvapich2-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

Parallel netCDF (PnetCDF) is a library providing high-performance I/O while
still maintaining file-format compatibility with Unidata's NetCDF.

%package openmpi
Summary:        High-performance parallel I/O with the NetCDF scientific data format
Group:          Productivity/Scientific/Other
Requires:       %{libname}%{sonum}-openmpi = %{version}

%description openmpi
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

This package contains the openmpi version of utility functions for
working with NetCDF files.

%package mvapich2
Summary:        High-performance parallel I/O with the NetCDF scientific data format
Group:          Productivity/Scientific/Other
Requires:       %{libname}%{sonum}-mvapich2 = %{version}

%description mvapich2
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

Parallel netCDF (PnetCDF) is a library providing high-performance I/O while
still maintaining file-format compatibility with Unidata's NetCDF.

This package contains the mvapich2 version of utility functions for
working with NetCDF files.

%package -n %{libname}%{sonum}-openmpi
Summary:        High-performance parallel I/O with the NetCDF scientific data format
Group:          Productivity/Scientific/Other
Provides:       %{libname}-openmpi = %{version}

%description -n %{libname}%{sonum}-openmpi
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

Parallel netCDF (PnetCDF) is a library providing high-performance I/O while
still maintaining file-format compatibility with Unidata's NetCDF.

This package contains the openmpi version of the PnetCDF runtime
libraries.

%package -n %{libname}%{sonum}-mvapich2
Summary:        High-performance parallel I/O with the NetCDF scientific data format
Group:          Productivity/Scientific/Other
Provides:       %{libname}-mvapich2 = %{version}

%description -n %{libname}%{sonum}-mvapich2
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

Parallel netCDF (PnetCDF) is a library providing high-performance I/O while
still maintaining file-format compatibility with Unidata's NetCDF.

This package contains the mvapich2 version of the PnetCDF runtime
libraries.

%package devel-data
Summary:        Development data files for %{name}
Group:          Development/Libraries/Parallel

%description devel-data
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

Parallel netCDF (PnetCDF) is a library providing high-performance I/O while
still maintaining file-format compatibility with Unidata's NetCDF.

This package contains generic files needed to create projects that use
any version of PnetCDF.

%package openmpi-devel
Summary:        Development files for %{name}-openmpi
Group:          Development/Libraries/Parallel
Requires:       %{libname}%{sonum}-openmpi = %{version}
Requires:       openmpi-devel

%description openmpi-devel
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

Parallel netCDF (PnetCDF) is a library providing high-performance I/O while
still maintaining file-format compatibility with Unidata's NetCDF.

This package contains all files needed to create projects that use
the openmpi version of PnetCDF.

%package mvapich2-devel
Summary:        Development files for %{name}-mvapich2
Group:          Development/Libraries/Parallel
Requires:       %{libname}%{sonum}-mvapich2 = %{version}
Requires:       mvapich2-devel

%description mvapich2-devel
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

Parallel netCDF (PnetCDF) is a library providing high-performance I/O while
still maintaining file-format compatibility with Unidata's NetCDF.

This package contains all files needed to create projects that use
the mvapich2 version of PnetCDF.

%package openmpi-devel-static
Summary:        Static development files for %{name}-openmpi
Group:          Development/Libraries/Parallel
Requires:       %{name}-openmpi-devel = %{version}

%description openmpi-devel-static
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

Parallel netCDF (PnetCDF) is a library providing high-performance I/O while
still maintaining file-format compatibility with Unidata's NetCDF.

This package contains the openmpi versions of the static libraries 
for PnetCDF.

%package mvapich2-devel-static
Summary:        Static development files for %{name}-mvapich2
Group:          Development/Libraries/Parallel
Requires:       %{name}-mvapich2-devel = %{version}

%description mvapich2-devel-static
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

Parallel netCDF (PnetCDF) is a library providing high-performance I/O while
still maintaining file-format compatibility with Unidata's NetCDF.

This package contains the mvapich2 versions of the static libraries 
for PnetCDF.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

set -- *
for mpi in %_mpi; do
 mkdir $mpi
 mkdir $mpi/shared
 cp -ap "$@" $mpi
done

%build
for mpi in %_mpi; do
pushd $mpi
%configure --prefix=%{_libdir}/mpi/gcc/$mpi \
           --libdir=%{_libdir}/mpi/gcc/$mpi/%{_lib} \
           --with-mpi=%{_libdir}/mpi/gcc/$mpi
make

pushd shared
%{_libdir}/mpi/gcc/$mpi/bin/mpif77 -shared -Wl,-soname=libpnetcdf.so.%{sonum} -o ../libpnetcdf.so.%{version}
popd

popd
done

%install
for mpi in %_mpi; do
pushd $mpi
%make_install

%if %{_lib} != lib
mv %{buildroot}%{_libdir}/mpi/gcc/$mpi/lib %{buildroot}%{_libdir}/mpi/gcc/$mpi/%{_lib}
%endif

install -m 755 libpnetcdf.so.%{version} %{buildroot}%{_libdir}/mpi/gcc/$mpi/%{_lib}
pushd %{buildroot}%{_libdir}/mpi/gcc/$mpi/%_lib
ln -s libpnetcdf.so.%{version} libpnetcdf.so.%{sonum}
ln -s libpnetcdf.so.%{version} libpnetcdf.so
popd

find %{buildroot} -name '*.la' -delete
popd
done

# rpm macro for version checking
mkdir -p %{buildroot}%{_sysconfdir}/rpm
cat > %{buildroot}%{_sysconfdir}/rpm/macros.pnetcdf <<EOF
#
# RPM macros for hdf5 packaging
#
%_pnetcdf_sonum  %{sonum}
%_pnetcdf_version  %{version}
EOF

%if 0%{?_openmpi}
%post -n libpnetcdf1-openmpi -p /sbin/ldconfig
%postun -n libpnetcdf1-openmpi -p /sbin/ldconfig
%endif

%if 0%{?_mvapich2}
%post -n libpnetcdf1-mvapich2 -p /sbin/ldconfig
%postun -n libpnetcdf1-mvapich2 -p /sbin/ldconfig
%endif

%files devel-data
%defattr(-,root,root)
%{_sysconfdir}/rpm/macros.pnetcdf

%if 0%{?_openmpi}
%files openmpi
%defattr(-,root,root)
%{_libdir}/mpi/gcc/openmpi/bin/*
%dir %{_libdir}/mpi/gcc/openmpi/man/
%{_libdir}/mpi/gcc/openmpi/man/*

%files -n %{libname}%{sonum}-openmpi
%defattr(-,root,root)
%doc COPYRIGHT CREDITS RELEASE_NOTES
%doc README README.LINUX README.large_files 
%{_libdir}/mpi/gcc/openmpi/%{_lib}/*.so.*

%files openmpi-devel
%defattr(-,root,root)
%{_libdir}/mpi/gcc/openmpi/include/*
%{_libdir}/mpi/gcc/openmpi/%{_lib}/*.so
%{_libdir}/mpi/gcc/openmpi/%{_lib}/pkgconfig/pnetcdf.pc

%files openmpi-devel-static
%defattr(-,root,root)
%{_libdir}/mpi/gcc/openmpi/%{_lib}/*.a
%endif

%if 0%{?_mvapich2}
%files mvapich2
%defattr(-,root,root)
%{_libdir}/mpi/gcc/mvapich2/bin/*
%dir %{_libdir}/mpi/gcc/mvapich2/man/
%{_libdir}/mpi/gcc/mvapich2/man/*

%files -n %{libname}%{sonum}-mvapich2
%defattr(-,root,root,-)
%doc COPYRIGHT CREDITS RELEASE_NOTES
%doc README README.LINUX README.large_files 
%{_libdir}/mpi/gcc/mvapich2/%{_lib}/*.so.*

%files mvapich2-devel
%defattr(-,root,root,-)
%{_libdir}/mpi/gcc/mvapich2/include/*
%{_libdir}/mpi/gcc/mvapich2/%{_lib}/*.so
%{_libdir}/mpi/gcc/mvapich2/%{_lib}/pkgconfig/pnetcdf.pc

%files mvapich2-devel-static
%defattr(-,root,root,-)
%{_libdir}/mpi/gcc/mvapich2/%{_lib}/*.a
%endif

%changelog
