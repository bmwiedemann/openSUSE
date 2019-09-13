#
# spec file for package llcbench
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           llcbench
Version:        1.10
Release:        0
Summary:        Low Level Architectural Characterization Benchmark Suite
License:        GPL-3.0+
Group:          System/Benchmark
Url:            http://icl.cs.utk.edu/llcbench/
Source:         http://icl.cs.utk.edu/llcbench/llcbench.tar.gz
# PATCH-FIX-UPSTREAM llcbench-gfortran.patch -- fix building with gfortran
Patch0:         llcbench-gfortran.patch
# PATX-FIX-OPENSUSE llcbench-noinline.patch -- fix building with gcc7
Patch1:         llcbench-noinline.patch
BuildRequires:  blas-devel
BuildRequires:  gcc-fortran
BuildRequires:  openmpi2-devel
Requires:       openmpi2
Suggests:       gnuplot
Provides:       blasbench
Provides:       cachebench
Provides:       mpbench

%description
LLCbench (Low-Level Characterization Benchmarks) was created by combining
MPBench, CacheBench, and BLASBench into a single benchmark package.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
ln -sf conf/sys.linux-lam sys.def
sed -i \
  -e "s|gcc|cc %{optflags}|g" \
  -e "s|g77|gfortran|g" \
  -e "s|-O3|-O2|g" \
  -e "s|mpicc|%{_libdir}/mpi/gcc/openmpi2/bin/mpicc|g" \
  sys.def
make %{?_smp_mflags} compile

%install
chmod -x cachebench/scripts/run_em
install -D -p -m 0755 mpbench/mpi_bench \
  %{buildroot}%{_bindir}/mpi_bench
install -D -p -m 0755 cachebench/cachebench \
  %{buildroot}%{_bindir}/cachebench
install -D -p -m 0755 blasbench/vblasbench \
  %{buildroot}%{_bindir}/vblasbench

%files
%doc CHANGES COPYING README
%doc doc/mpbench/mpbench.README
%doc mpbench/make_graphs.sh
%doc mpbench/make_templates.sh
%doc doc/cachebench/cachebench.README
%doc cachebench/cachegraph.gp
%doc cachebench/scripts/run_em
%doc doc/blasbench/blasbench.README
%{_bindir}/mpi_bench
%{_bindir}/cachebench
%{_bindir}/vblasbench

%changelog
