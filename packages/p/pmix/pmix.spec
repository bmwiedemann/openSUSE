#
# spec file for package pmix
#
# Copyright (c) 2020 SUSE LLC
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


#

Name:           pmix
Version:        3.1.4
Release:        0
Summary:        Process Management Interface for MPI
License:        BSD-3-Clause
Group:          Development/Libraries/Parallel 
URL:            https://pmix.org/
Source0:        https://github.com/openpmix/openpmix/archive/v%{version}.tar.gz#/openpmix-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  hwloc-devel
BuildRequires:  libevent-devel
%ifarch x86_64
BuildRequires:  libpsm2-devel
%endif
BuildRequires:  libtool
BuildRequires:  munge-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       pmix-runtime-config
Recommends:     pmix-mca-params

%description
The Process Management Interface (PMI) has been used for quite some time as a
means of exchanging wireup information needed for interprocess communication. Two
versions (PMI-1 and PMI-2) have been released as part of the MPICH effort. While
PMI-2 demonstrates better scaling properties than its PMI-1 predecessor, attaining
rapid launch and wireup of the roughly 1M processes executing across 100k nodes
expected for exascale operations remains challenging.

This RPM contains all the tools necessary to compile and link against PMIx.
%package -n libpmix2
Summary:        PMI-X lib version 1
Group:          hpc mpi

%description  -n libpmix2
This package contains the shared library used by the PMI-X standard

%package -n libmca_common_dstore1
Summary:        Communication library used by PMI-X
Group:          hpc mpi

%description  -n libmca_common_dstore1
This package contains the communication library used by the PMI

%package devel
Summary:        Process Management Interface for MPI
Group:          hpc mpi devel
Requires:       %{name}-headers = %{version}
Requires:       libpmix2 = %{version}

%description devel
This Package contains necessary files for development and building PMI-X
aware applications.

%package headers
Summary:        Process Management Interface for MPI
Group:          hpc mpi devel

%description headers
This Package contains necessary the headers for PMI-X.

%package -n pmix-mca-params
Summary:        Settings for the Module Component Architecure
Group:          hpc mpi devel
Provides:       pmix-runtime-config = %{version}
Conflicts:      otherproviders(pmix-runtime-config)

%description -n pmix-mca-params
PMIX is part of the Module Component Architecure and needs so to have its
parameters configured.


%prep
%setup -q -n openpmix-%{version}

%build
./autogen.pl --force
%configure \
  --with-munge \
  --with-devel-headers \
  --disable-pmi-backward-compatibility \
%ifarch x86_64
  --with-psm2 \
%endif
  --with-hwloc \

make %{?_smp_mflags}

%install
%make_install
# removed static libaries
rm -v %{buildroot}/%{_libdir}/*.la %{buildroot}/%{_libdir}/pmix/*.la
%fdupes %{buildroot}/%{_datadir} 

%post -n libpmix2 -p /sbin/ldconfig
%postun -n libpmix2 -p /sbin/ldconfig

%post -n libmca_common_dstore1 -p /sbin/ldconfig
%postun -n libmca_common_dstore1 -p /sbin/ldconfig

%files
%doc README.md NEWS AUTHORS
%license LICENSE
%dir %{_libdir}/pmix
%{_libdir}/pmix/mca_*.so
%{_datadir}/pmix
%{_bindir}/pevent
%{_bindir}/plookup
%{_bindir}/pmix_info
%{_bindir}/pps

%files -n pmix-mca-params
%config %{_sysconfdir}/pmix-mca-params.conf

%files -n libpmix2
%{_libdir}/libpmix.so.*

%files -n libmca_common_dstore1
%{_libdir}/libmca_common_dstore.so.*

%files devel
%{_libdir}/libpmix.so
%{_libdir}/libmca_common_dstore.so

%files headers
%dir %{_includedir}/pmix
%{_includedir}/pmix*.h
%{_includedir}/pmix/*

%changelog
