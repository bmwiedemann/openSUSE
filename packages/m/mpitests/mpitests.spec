#
# spec file
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


%global flavor @BUILD_FLAVOR@%nil

%if "%{flavor}" == ""
%define pack_suff %{nil}
%else
%define pack_suff -%{flavor}

#
# Returns where MPI home is.
# Looks in the RPM based on the arg name for bin/mpicc
# and extracts mpihome from there.
# This handles mpicc being in the main RPM, in a -devel
# or in a dependency (when the top is an HPC meta RPM).
# However all the necessary packages MUST be installed.
%define hpc_mpi_home %( \
   check_package(){ (rpm -ql $1 | grep -E -q 'bin/mpicc$') && echo $1;};                \
   get_linked_pack(){ rpm -qR $1 | grep -v rpmlib | grep -v /sh | awk '{print $1}';}; \
   dirname $(dirname $(rpm -ql $(check_package %flavor || check_package %{flavor}-devel ||        \
   check_package $(get_linked_pack %flavor) || check_package $(get_linked_pack %{flavor}-devel)) | \
   grep -E 'bin/mpicc$')))

%endif

%define osu_ver  6.1
%define imb_ver  2021.3
%define imb_dir  mpi-benchmarks-IMB-v%{imb_ver}
%define osu_dir  osu-micro-benchmarks-%{osu_ver}

%define mpi_home %{hpc_mpi_home %flavor}
%define implem_list_dir %{_datadir}/mpitests/implem.d/
%define sles_pre_15 (0%{?sle_version} > 120000 && 0%{?sle_version} < 150000)
%define sles_pre_or_15 (0%{?sle_version} > 120000 && 0%{?sle_version} <= 150000)

Name:           mpitests%{pack_suff}
%if "%{flavor}" == ""
Summary:        MPI Benchmarks common files
License:        BSD-3-Clause AND CPL-1.0
Group:          Development/Languages/Other
%else
Summary:        MPI Benchmarks and tests for %{flavor}
License:        BSD-3-Clause AND CPL-1.0
Group:          Development/Languages/Other
%endif
Version:        3.2
Release:        0
URL:            http://www.openfabrics.org/downloads.htm
Source0:        http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-%{osu_ver}.tar.gz
Source1:        https://github.com/intel/mpi-benchmarks/archive/IMB-v%{imb_ver}.tar.gz
Source3:        mpitests-runtests.sh
Source4:        mpitests-run.sh
Source100:      mpitests-rpmlintrc
Source101:      _multibuild
Patch1:         osu-fix-bad-return-values.patch
Patch2:         imb-cpp-flags.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
# suse-hpc is not available for SLE < 15
%if 0%{?is_opensuse} || 0%{?sle_version} >= 150000
BuildRequires:  suse-hpc
%endif
%if "%{flavor}" != ""
BuildRequires:  %{flavor}
BuildRequires:  %{flavor}-devel
Requires:       %{flavor}
BuildRequires:  mpitests = %{version}
Requires:       mpitests = %{version}
%endif

%if "%{flavor}" == "mvapich2"
ExcludeArch:    %{arm}
%endif

%if  "%{flavor}" == "mvapich2-gnu-hpc"
%if %{sles_pre_15}
# Disable hpc builds for SLE12
ExclusiveArch:  do_not_build
%endif
ExcludeArch:    i586 %arm s390
%endif

%if "%{flavor}" == "mvapich2-psm2"
ExclusiveArch:  x86_64
%endif

%if "%{flavor}" == "mvapich2-psm2-gnu-hpc"
%if %{sles_pre_15}
# Disable hpc builds for SLE12
ExclusiveArch:  do_not_build
%else
ExclusiveArch:  x86_64
%endif
%endif

%if "%{flavor}" == "openmpi1-gnu-hpc"
%if %{sles_pre_15}
# Disable hpc builds for SLE12
ExclusiveArch:  do_not_build
%endif
%endif

%if "%{flavor}" == "openmpi4"
%if %{sles_pre_or_15}
# Disable openmpi4 builds for SLES up to (including) 15
ExclusiveArch:  do_not_build
%else
ExcludeArch:    ppc64
%endif
%endif

%if "%{flavor}" == "openmpi4-gnu-hpc"
%if %{sles_pre_or_15}
# Disable openmpi4 builds for SLES up to (including) 15
ExclusiveArch:  do_not_build
%else
ExcludeArch:    i586 %arm s390 ppc64
%endif
%endif

# Disable mpich builds for SLE12 as it is not available
%if "%{flavor}" == "mpich-ofi" || "%{flavor}" == "mpich"
%if %{sles_pre_15}
ExclusiveArch:  do_not_build
%endif
%endif

# Disable mpich builds for SLE12 as it is not available
%if "%{flavor}" == "mpich-ofi-gnu-hpc" || "%{flavor}" == "mpich-gnu-hpc"
%if %{sles_pre_15}
ExclusiveArch:  do_not_build
%endif
ExcludeArch:    i586 %arm s390
%endif

%description
Set of popular MPI benchmarks: IMB v%{imb_ver} OSU benchmarks ver %{osu_ver}

%prep
%setup -c -q
%setup -T -D -a 1 -q
%patch -P 1 -p0
%patch -P 2 -p0

%if "%{flavor}" != ""
%build
echo echo %{mpi_home}
. %{mpi_home}/bin/mpivars.sh

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{optflags}"

# IMB Build
make  CC=%{mpi_home}/bin/mpicc CXX=%{mpi_home}/bin/mpicxx \
     -C %{imb_dir}/ all

# OSU Build
( cd %{osu_dir} && \
  ./configure CC=%{mpi_home}/bin/mpicc CXX=%{mpi_home}/bin/mpicxx &&
  make all )

%install
# IMB
for imb_test in IMB-EXT IMB-IO IMB-MPI1 IMB-NBC IMB-RMA; do \
	install -D -m0755  %{imb_dir}/$imb_test %{buildroot}%{mpi_home}/tests/IMB/$imb_test;\
done
# OSU
make -C %{osu_dir} install prefix=%{buildroot}/usr libexecdir=%{buildroot}%{mpi_home}/tests

# Run script
sed -e s/@IMPLEM@/%{flavor}/g -e 's&@MPI_HOME@&%{mpi_home}&g' %{S:3}  > %{buildroot}%{mpi_home}/tests/runtests.sh
chmod 0755 %{buildroot}%{mpi_home}/tests/runtests.sh
mkdir -p %{buildroot}%{implem_list_dir}
echo %{mpi_home}/tests/runtests.sh > %{buildroot}%{implem_list_dir}/%{flavor}

%check
%bcond_with mpitests_check
%if %{with mpitests_check}
export SHORT=%{short}
export IMPLEM_LIST_DIR=%{implem_list_dir}
export BUILDROOT=%{buildroot}
%{_datadir}/mpitests/runtests.sh
%else
echo "Skipping tests"
%endif

%else

%build

%install
install -D -m0755 %{S:4} %{buildroot}%{_datadir}/%{name}/runtests.sh
mkdir -p %{buildroot}%{_datadir}/mpitests/implem.d/

%endif

%files
%defattr(-, root, root)
%dir %{_datadir}/mpitests/
%dir %{_datadir}/mpitests/implem.d/
%if "%{flavor}" == ""
%{_datadir}/%{name}/runtests.sh
%else
%doc %{imb_dir}/license/license.txt
%doc %{imb_dir}/license/use-of-trademark-license.txt
%doc %{osu_dir}/COPYRIGHT
%{mpi_home}/tests
%{_datadir}/mpitests/implem.d/%{flavor}
%endif

%changelog
