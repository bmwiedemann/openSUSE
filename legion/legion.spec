#
# spec file for package legion
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016-2017 Christoph Junghans
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


%define git_ver .0.1ebd2fdc0da1
%ifarch ppc64
%define mpi_implem openmpi
%else
%define mpi_implem openmpi2
%endif

Name:           legion
Version:        18.05.0
Release:        0
Summary:        A data-centric parallel programming system
License:        Apache-2.0
Group:          Productivity/Networking/Other
Url:            http://legion.stanford.edu/
Source0:        %{name}-%{version}%{git_ver}.tar.gz
Patch0:         legion-fix-potential-return-of-random-data.patch
Patch1:         gcc-8.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  %{mpi_implem}
BuildRequires:  %{mpi_implem}-devel
BuildRequires:  cmake
BuildRequires:  gasnet-devel
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel
%ifarch x86_64 %{ix86}
BuildRequires:  libfabric-devel
%endif
%ifarch x86_64
BuildRequires:  libpsm2-devel
%endif

%description
Legion is a data-centric parallel programming system for writing portable
high performance programs targeted at distributed heterogeneous architectures.

%package -n liblegion1
Summary:        Data-centric parallel programming system
Group:          System/Libraries

%description -n liblegion1
Legion is a data-centric parallel programming system for writing portable
high performance programs targeted at distributed heterogeneous architectures.
Legion presents abstractions which allow programmers to describe properties of
program data (e.g. independence, locality). By making the Legion programming
system aware of the structure of program data, it can automate many of the
tedious tasks programmers currently face, including correctly extracting task-
and data-level parallelism and moving data around complex memory hierarchies.
A novel mapping interface provides explicit programmer controlled placement of
data in the memory hierarchy and assignment of tasks to processors in a way that
is orthogonal to correctness, thereby enabling easy porting and tuning of Legion
applications to new architectures.

This package contains shared libraries for the legion library.

%package devel
Summary:        Development headers and libraries for the legion library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}1 = %{version}

%description devel
Legion is a data-centric parallel programming system for writing portable
high performance programs targeted at distributed heterogeneous architectures.
Legion presents abstractions which allow programmers to describe properties of
program data (e.g. independence, locality). By making the Legion programming
system aware of the structure of program data, it can automate many of the
tedious tasks programmers currently face, including correctly extracting task-
and data-level parallelism and moving data around complex memory hierarchies.
A novel mapping interface provides explicit programmer controlled placement of
data in the memory hierarchy and assignment of tasks to processors in a way that
is orthogonal to correctness, thereby enabling easy porting and tuning of Legion
applications to new architectures.

This package contains development headers and libraries for the legion library.

%prep
%setup -q -n  %{name}-%{version}%{git_ver}
%patch0
%if 0%{suse_version} > 1500
# Workaround GCC8 bug in TW
%patch1 -p1
%endif

%build
. %{_libdir}/mpi/gcc/%{mpi_implem}/bin/mpivars.sh
%{cmake} -DLegion_USE_HWLOC=ON \
         -DLegion_USE_GASNet=ON \
         -DCOMPILER_SUPPORTS_MARCH=OFF \
         -DCOMPILER_SUPPORTS_MCPU=OFF \
         -DLegion_BUILD_EXAMPLES=ON \
         -DLegion_BUILD_TESTS=ON \
         -DLegion_ENABLE_TESTING=ON \
         -DGASNet_CONDUIT=mpi \
         -DLegion_BUILD_TUTORIAL=ON
make

%install
. %{_libdir}/mpi/gcc/%{mpi_implem}/bin/mpivars.sh
make -C build install DESTDIR=%{buildroot}

%check
. %{_libdir}/mpi/gcc/%{mpi_implem}/bin/mpivars.sh
LD_LIBRARY_PATH="%{buildroot}/%{_libdir}:${LD_LIBRARY_PATH}" make -C build %{?_smp_mflags} test ARGS='-V'

%post -n liblegion1 -p /sbin/ldconfig
%postun -n liblegion1 -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%doc LICENSE.txt README.md CHANGES.txt
%{_includedir}/*
%{_libdir}/lib*.so
%{_datadir}/Legion

%files -n liblegion1
%defattr(-,root,root,-)
%doc LICENSE.txt README.md CHANGES.txt
%{_libdir}/lib*.so.1

%changelog
