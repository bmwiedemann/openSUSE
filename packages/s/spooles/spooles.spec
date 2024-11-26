#
# spec file for package spooles
#
# Copyright (c) 2024 SUSE LLC
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

%define libname libspooles2_2

%if "%{flavor}" == ""
%define my_prefix %_prefix
%define my_bindir %_bindir
%define my_libdir %_libdir
%define my_incdir %_includedir
%define my_datadir %_datadir
%endif

%if "%{flavor}" == "openmpi"
%define my_suffix  -openmpi
%define mpi_flavor  openmpi
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}

%if %{with mpi}
%define my_prefix %{openmpi_prefix}
%define my_bindir %{my_prefix}/bin
%define my_libdir %{my_prefix}/%{_lib}/
%define my_incdir %{my_prefix}/include/
%define my_datadir %{my_prefix}/share/
%endif

Name:           spooles%{?my_suffix}
Version:        2.2
Release:        0
Summary:        A sparse matrix library
# SPOOLES: Public Domain
# SPOOLES: Utilities/src/iohb.c: BSD 2-Clause style
License:        BSD-2-Clause AND SUSE-Public-Domain
Group:          Development/Libraries/C and C++
URL:            https://www.netlib.org/linalg/spooles/spooles.2.2.html
Source0:        https://www.netlib.org/linalg/spooles/spooles.2.2.tgz
Patch0:         patch-spooles-shared
Patch1:         patch-spooles-shared-mpi
Patch2:         patch-spooles-I2Ohash-from-debian
Patch3:         0001-Fix-compile-error-due-to-apparent-invalid-cast.patch
%if %{with mpi}
# By pulling openmpi-macros-devel,
# we always get the current "default" implementation
BuildRequires:  openmpi-macros-devel
%endif

%description
SPOOLES is a library for solving sparse real and complex linear systems
of equations, written in the C language using object oriented design.

%{with mpi:This package has been built with %{mpi_flavor} support.}

%package -n %{libname}%{?my_suffix}
Summary:        A sparse matrix library
Group:          System/Libraries
%if %{with mpi}
%openmpi_requires
%endif

%description -n %{libname}%{?my_suffix}
SPOOLES is a library for solving sparse real and complex linear systems
of equations, written in the C language using object oriented design.

%{with mpi:This package has been built with %{mpi_flavor} support.}

%package devel
Summary:        Header files for the SPOOLES library
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{?my_suffix} = %{version}-%{release}
%if %{with mpi}
%openmpi_devel_requires
%endif

%description devel
%{name}-devel provides the header file for the SPOOLES library.

%prep
%setup -c -q
%autopatch -p1

%build
%set_build_flags
%if %{without mpi}
%make_build -f makeRPM all

%else
# openmpi
%setup_openmpi
%make_build -f makeRPM-mpi all \
   CC=%{my_bindir}/mpicc \
   MPI_INSTALL_DIR=%{my_prefix} \
   MPI_LIB_PATH=-L%{my_libdir}/
%endif

%install
mkdir -p %{buildroot}/%{my_libdir}
cp -P libspooles* %{buildroot}/%{my_libdir}
chmod 755 %{buildroot}/%{my_libdir}/libspooles.so.%{version}

# header files: use same convention as debian spooles package:
# all headers under /usr/include/spooles

mkdir -p %{buildroot}/%{my_incdir}/spooles
find . -name \*.h -print -exec \
  install -m 644 -D '{}' %{buildroot}%{my_incdir}/spooles/\{\} \;

%post -n %{libname}%{?my_suffix} -p /sbin/ldconfig
%postun -n %{libname}%{?my_suffix} -p /sbin/ldconfig

%files -n %{libname}%{?my_suffix}
%{my_libdir}/libspooles.so.2.2

%files devel
%{my_incdir}/spooles/
%{my_libdir}/libspooles.so
%doc spooles.2.2.html

%changelog
