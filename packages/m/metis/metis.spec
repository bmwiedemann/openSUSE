#
# spec file for package metis
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


%define somajor 5
%define libname lib%{name}%{somajor}

Name:           metis
Version:        5.1.0
Release:        0
Summary:        Serial Graph Partitioning and Fill-reducing Matrix Ordering
License:        Apache-2.0
Group:          Productivity/Scientific/Math
URL:            http://glaros.dtc.umn.edu/gkhome/metis/metis/overview
Source0:        %{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE metis-cmake.patch
Patch1:         metis-cmake.patch
# PATCH-FIX-OPENSUSE metis-programs-no-compilation-time.patch -- Fix W: file-contains-date-and-time
Patch2:         metis-programs-no-compilation-time.patch
Patch3:         metis-makefile-c-directives.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc
BuildRequires:  gcc-c++

Recommends:     %{name}-doc = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
METIS is a family of programs for partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. The underlying algorithms
used by METIS are based on a multilevel paradigm that, at the time, had been
shown to produce quality results and scale to large problems.

%package     -n %{libname}
Summary:        Serial Graph Partitioning and Fill-reducing Matrix Ordering library
Group:          System/Libraries
Obsoletes:      %libname < %{version}

%description -n %{libname}
METIS library provides to partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. The underlying algorithms
used by METIS are based on a multilevel paradigm that, at the time, had been
shown to produce quality results and scale to large problems.

%package        devel
Summary:        Metis development files
Group:          Development/Libraries/C and C++
Requires:       %libname = %{version}

%description    devel
METIS library provides to partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. The underlying algorithms
used by METIS are based on a multilevel paradigm that, at the time, had been
shown to produce quality results and scale to large problems.

This package provides development files.

%package        doc
Summary:        Metis documentation
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
METIS is a family of programs for partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. The underlying algorithms
used by METIS are based on a multilevel paradigm that, at the time, had been
shown to produce quality results and scale to large problems.

%package        examples
Summary:        Metis examples
Group:          Documentation/Other
BuildArch:      noarch

%description    examples
METIS library provides to partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. This package provides
graph files you can use to test Metis.

%prep
%autosetup -p1 -n %{name}-%{version}

# set width (32 or 64 bits) of the elementary data type, see Install.txt
sed -i 's|#define IDXTYPEWIDTH 32|#define IDXTYPEWIDTH %{__isa_bits}|' include/metis.h

%build

make config shared=1 prefix=%{_prefix} cflags="%{optflags} -fopenmp -pthread -fpie -pie" ldflags="-pie"
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
pushd graphs
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH %{buildroot}%{_bindir}/ndmetis mdual.graph
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH %{buildroot}%{_bindir}/mpmetis metis.mesh 2
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH %{buildroot}%{_bindir}/gpmetis test.mgraph 4
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH %{buildroot}%{_bindir}/gpmetis copter2.graph 4
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH %{buildroot}%{_bindir}/graphchk 4elt.graph
popd
cd graphs # cleanup after tests:
rm test.mgraph.part.4 metis.mesh.epart.2 metis.mesh.npart.2 copter2.graph.part.4 mdual.graph.iperm

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files
%doc Changelog
%license LICENSE.txt
%{_bindir}/*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{somajor}*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files doc
%doc manual/manual.pdf

%files examples
%doc graphs

%changelog
