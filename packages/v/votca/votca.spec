#
# spec file for package votca
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021-2022 Christoph Junghans
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

%global with_xtp 1
# libint2 used by xtp is broken on 32-bit archs
# https://github.com/evaleev/libint/issues/196
# https://github.com/votca/xtp/issues/652
%ifarch %ix86 %arm
%global with_xtp 0
%endif

Name:           votca
Version:        2022.1
Release:        0
%define         uversion %{version}
%define         sover 2022
Summary:        Versatile Object-oriented Toolkit for Coarse-graining Applications
License:        Apache-2.0
Group:          Productivity/Scientific/Chemistry
URL:            https://www.votca.org
Source0:        https://github.com/votca/votca/archive/v%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz

BuildRequires:  cmake >= 3.13
BuildRequires:  eigen3-devel
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  gnuplot
# gromacs is not available on 32-bit arm
%ifnarch %{arm}
BuildRequires:  gromacs-devel
BuildRequires:  gromacs-openmpi
%endif
BuildRequires:  hdf5-devel
BuildRequires:  lammps
BuildRequires:  libboost_filesystem-devel >= 1.71.0
BuildRequires:  libboost_program_options-devel >= 1.71.0
BuildRequires:  libboost_regex-devel >= 1.71.0
BuildRequires:  libboost_serialization-devel >= 1.71.0
BuildRequires:  libboost_system-devel >= 1.71.0
BuildRequires:  libboost_test-devel >= 1.71.0
BuildRequires:  libboost_timer-devel >= 1.71.0
BuildRequires:  libecpint-devel
BuildRequires:  libexpat-devel
%if %{with_xtp}
BuildRequires:  libint-devel
%endif
BuildRequires:  libxc-devel
BuildRequires:  memory-constraints
BuildRequires:  openmpi-macros-devel
BuildRequires:  pkg-config
BuildRequires:  procps
BuildRequires:  psmisc
BuildRequires:  python3-cma
# only needed for testing
%ifarch x86_64
BuildRequires:  python3-espressomd
%endif
BuildRequires:  python3-lxml
BuildRequires:  python3-pytest
# for hdf5
BuildRequires:  zlib-devel

Obsoletes:      votca-tools <= 2022~rc1
Provides:       votca-tools = %version-%release
Obsoletes:      votca-csg <= 2022~rc1
Provides:       votca-csg = %version-%release
Obsoletes:      votca-csg-apps <= 2022~rc1
Provides:       votca-csg-apps = %version-%release
Obsoletes:      votca-xtp <= 2022~rc1
Provides:       votca-xtp = %version-%release

%global votca_desc \
VOTCA is a software package which focuses on the analysis of molecular \
dynamics data, the development of systematic coarse-graining techniques as \
well as methods used for simulating microscopic charge (and exciton) transport \
in disordered semiconductors.

%description
%{votca_desc}

%package -n libvotca%sover
Summary:        VOTCA tools library
Group:          System/Libraries
Obsoletes:      libvotca_tools2022 <= 2022~rc1
Provides:       libvotca_tools2022 = %version-%release
Obsoletes:      libvotca_csg2022 <= 2022~rc1
Provides:       libvotca_csg2022 = %version-%release
Obsoletes:      libvotca_xtp2022 <= 2022~rc1
Provides:       libvotca_xtp2022 = %version-%release

%description -n libvotca%sover
%{votca_desc}

This package contains the librares of VOTCA package.

%package devel
Summary:        Development headers and libraries for votca
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       eigen3-devel
Requires:       fftw3-devel
Requires:       libexpat-devel
Requires:       libvotca%sover = %{version}
Obsoletes:      votca-tools-devel <= 2022~rc1
Provides:       votca-tools-devel = %version-%release
Obsoletes:      votca-csg-devel <= 2022~rc1
Provides:       votca-csg-devel = %version-%release
Obsoletes:      votca-xtp-devel <= 2022~rc1
Provides:       votca-xtp-devel = %version-%release

%description devel
%{votca_desc}

This package contains development headers and libraries for votca.

%package common
Summary:        Architecture-independent data files for VOTCA
Group:          Productivity/Scientific/Chemistry
BuildArch:      noarch
Requires:       /usr/bin/awk
Requires:       bash
Requires:       perl
Obsoletes:      votca-csg-common <= 2022~rc1
Provides:       votca-csg-common = %version-%release
Obsoletes:      votca-xtp-common <= 2022~rc1
Provides:       votca-xtp-common = %version-%release

%description common
%{votca_desc}

This package contains the architecture-independent data files for VOTCA.

%package tutorials
Summary:        Tutorial documentation for VOTCA Coarse Graining Engine
Group:          Productivity/Scientific/Chemistry
BuildArch:      noarch
Requires:       /bin/bash
Obsoletes:      votca-csg-tutorials <= 2022~rc1
Provides:       votca-csg-tutorials = %version-%release

%description tutorials
%{votca_desc}

This package contains the tutorial documentation and sample data.

%package bash
Summary:        Bash completion for votca
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
BuildArch:      noarch
Obsoletes:      votca-csg-bash <= 2022~rc1
Provides:       votca-csg-bash = %version-%release

%description bash
%{votca_desc}

This package contains the bash completion support for votca.

%prep
%setup -n %{name}-%{uversion} -q

%build
%setup_openmpi

# save some memory
%limit_build -m 2400
%{cmake} -DINSTALL_RC_FILES=OFF -DCMAKE_SKIP_RPATH=OFF -DENABLE_TESTING=ON -DENABLE_REGRESSION_TESTING=ON \
         -DINJECT_MARCH_NATIVE=OFF -DBUILD_CSGAPPS=ON \
         -DBUILD_XTP=%{with_xtp} \
         ..
%cmake_build

%install
%cmake_install
sed -i '1s@env @@' %{buildroot}/%{_bindir}/votca_{compare,help2doc} \
  %{buildroot}/%{_datadir}/votca/scripts/inverse/{iie,cma_processor,table_smooth_at_cut_off}.py \
  %{buildroot}/%{_datadir}/votca/csg-tutorials/LJ1-LJ2/imc/svd.py \
  %{buildroot}/%{_datadir}/votca/csg-tutorials/spce/ibi*/spce.py

%if %{with_xtp}
sed -i '1s@env @@' %{buildroot}/%{_bindir}/xtp_* %{buildroot}/%{_datadir}/votca/xtp/benchmark/xtp_benchmark
%endif

# Move bash completion file to correct location
mkdir -p %{buildroot}%{_datadir}/bash_completion.d
cp %{buildroot}%{_datadir}/votca/rc/csg-completion.bash %{buildroot}%{_datadir}/bash_completion.d/votca

%fdupes %{buildroot}%{_prefix}

%check
%setup_openmpi
%ctest

%files
%{_bindir}/{votca,csg,xtp}_*
%{_mandir}/man1/*
%{_mandir}/man7/*

%post -n libvotca%sover -p /sbin/ldconfig
%postun -n libvotca%sover -p /sbin/ldconfig

%files -n libvotca%sover
%doc NOTICE.rst README.rst CHANGELOG.rst
%license LICENSE
%{_libdir}/libvotca_*.so.%{sover}

%files devel
%{_includedir}/votca/
%{_libdir}/libvotca_*.so
%{_libdir}/cmake/VOTCA_*

%files tutorials
%{_datadir}/votca/{csg,xtp}-tutorials

%files common
%{_datadir}/votca
%exclude %{_datadir}/votca/{csg,xtp}-tutorials

%files bash
%dir %{_datadir}/bash_completion.d
%{_datadir}/bash_completion.d/votca

%changelog
