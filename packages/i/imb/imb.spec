#
# spec file for package imb
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


%global flavor @BUILD_FLAVOR@%{nil}

# Base package name
%define pname imb
%define PNAME IMB

%if "%flavor" == ""
%define package_name %{pname}
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "openmpi4" 
%global mpi_flavor openmpi
%define mpi_vers 4
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%else
%if "%{flavor}" == "openmpi5"
%global mpi_flavor openmpi
%define mpi_vers 5
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%else
# Anything but openmpi[45]
%global mpi_flavor %{flavor}
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif
%endif

%define p_bindir /usr/%_lib/mpi/gcc/%{flavor}/bin
%if "%{flavor}" == ""
%define package_name  %{pname}
%else
%define package_name  %{pname}-%{flavor}
%endif

Name:           %{package_name}
Version:        2021.10
Release:        0
Summary:        Intel MPI Benchmarks (IMB)
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://software.intel.com/en-us/articles/intel-mpi-benchmarks
Source0:        https://github.com/intel/mpi-benchmarks/archive/IMB-v%{version}.tar.gz#/%{pname}_%{version}.tar.gz
Source100:      README.md
Patch0:         imb-remove-Werror-flag.patch
Patch1:         src_c-Fix-multiple-size_t-issues-on-32b-systems.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
Obsoletes:      imb < %{version}
# Do not bother with 32b versions.
ExcludeArch:    %{ix86} %{arm}

%description
The Intel MPI Benchmarks (IMB) perform a set of MPI performance
measurements for point-to-point and global communication operations for
a range of message sizes.

%prep
%autosetup -p1 -n mpi-benchmarks-IMB-v%{version}

%build

%define makeargs CC=/usr/%_lib/mpi/gcc/%{flavor}/bin/mpicc CXX=/usr/%_lib/mpi/gcc/%{flavor}/bin/mpic++
. /usr/%_lib/mpi/gcc/%{flavor}/bin/mpivars.sh
for target in $(echo %{?buildtarget}) ; do
echo "building $target"
make $target %{?makeargs} %{?_smp_mflags}
done
cd -

%install
%{__mkdir} -p %{buildroot}%{p_bindir}
cp IMB-*  %{buildroot}%{p_bindir}
mkdir -p %{buildroot}%{docdir}/%{name}
cat <<EOF > %{buildroot}%{docdir}/%{name}/README.SUSE
Product documentation is now available online only at: https://software.intel.com/en-us/imb-user-guide.
EOF
cd -

%files
%doc ReadMe_IMB.txt
%license license/license.txt license/use-of-trademark-license.txt
%{p_bindir}

%changelog
