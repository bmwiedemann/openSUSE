#
# spec file for package votca-csg
#
# Copyright (c) 2020-2021 SUSE LLC
# Copyright (c) 2013-2021 Christoph Junghans
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


Name:           votca-csg
Version:        2022~rc1
Release:        0
%define         uversion 2022-rc.1
%define         sover 2022
Summary:        VOTCA coarse-graining engine
License:        Apache-2.0
Group:          Productivity/Scientific/Chemistry
URL:            http://www.votca.org
Source0:        https://github.com/votca/votca/archive/v%{uversion}.tar.gz#/votca-%{uversion}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  cmake >= 3.12
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gromacs-devel
BuildRequires:  hdf5-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_test-devel
BuildRequires:  pkg-config
BuildRequires:  python3-txt2tags
BuildRequires:  votca-tools-devel = %{version}
# for hdf5
BuildRequires:  zlib-devel

#exact same version is needed
Requires:       %{name}-common = %{version}
Requires:       libvotca_csg%sover = %{version}
# The developer man page was wrongly shipped in the library package until votca 1.6
Conflicts:      libvotca_csg5
# no more pdf manual
Obsoletes:      votca-csg-doc < 2021
Provides:       votca-csg-doc = %version-%release

%description
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the Coarse Graining Engine of VOTCA.

%package -n libvotca_csg%sover
Summary:        Libraries for the VOTCA coarse graining engine
Group:          System/Libraries

%description -n libvotca_csg%sover
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains libraries for the Coarse Graining Engine of VOTCA.

%package devel
Summary:        Development headers and libraries for the VOTCA Coarse Graining Engine
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libvotca_csg%sover = %{version}
Requires:       votca-tools-devel = %{version}

%description devel
This package contains development headers and libraries for the VOTCA
Coarse Graining Engine.

%package common
Summary:        Architecture-independent data files for VOTCA CSG
Group:          Productivity/Scientific/Chemistry
BuildArch:      noarch
Requires:       /usr/bin/awk
Requires:       bash
Requires:       perl

%description common
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the architecture-independent data files for VOTCA CSG.

%package tutorials
Summary:        Tutorial documentation for VOTCA Coarse Graining Engine
Group:          Productivity/Scientific/Chemistry
BuildArch:      noarch
Requires:       /bin/bash

%description tutorials
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the tutorial documentation and sample data.

%package apps
Summary:        VOTCA coarse-graining engine applications
Group:          Productivity/Scientific/Chemistry
Obsoletes:      votca-csgapps < 2021
Provides:       votca-csgapps = %version-%release

%description apps
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains sample applications of the VOTCA Coarse Graining Engine.
Previously packages as votca-csgapps.

%package bash
Summary:        Bash completion for votca
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
BuildArch:      noarch

%description bash
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++. Iterative
methods are implemented using bash + perl.

This package contains the bash completion support for votca-csg.

%prep
%setup -n votca-%{uversion} -q

FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" csg/src/libcsg/version.cc

%build
%{cmake} -DCMAKE_SKIP_RPATH=OFF -DBUILD_CSGAPPS=ON -DENABLE_TESTING=ON ../csg
#-DINTEGRATIONTEST_TOLERANCE="2.1e-5"
%cmake_build

%install
%cmake_install
sed -i '1s@env @@' %{buildroot}/%{_datadir}/votca/scripts/inverse/cma_processor.py 

# Move bash completion file to correct location
mkdir -p %{buildroot}%{_datadir}/bash_completion.d
cp %{buildroot}%{_datadir}/votca/rc/csg-completion.bash %{buildroot}%{_datadir}/bash_completion.d/votca

%define pkgdocdir %{_docdir}/%{name}
mkdir -p %{buildroot}%{pkgdocdir}/examples
pwd
cp -r csg-tutorials/* %{buildroot}%{pkgdocdir}/examples
sed -i '1s@env @@' %{buildroot}%{pkgdocdir}/examples/LJ1-LJ2/imc/svd.py

%fdupes %{buildroot}%{_prefix}

#check
%ctest

%post -n libvotca_csg%sover -p /sbin/ldconfig
%postun -n libvotca_csg%sover -p /sbin/ldconfig

%files
%doc CHANGELOG.rst csg/NOTICE.rst README.rst 
%license csg/LICENSE.rst
%{_bindir}/csg_*
%exclude %{_bindir}/csg_{fluctuations,orientcorr,part_dist,partial_rdf,radii,sphericalorder,traj_force}
%{_mandir}/man1/*
%{_mandir}/man7/*
%exclude %{pkgdocdir}/examples

%files apps
%{_bindir}/csg_{fluctuations,orientcorr,part_dist,partial_rdf,radii,sphericalorder,traj_force}

%files tutorials
%{pkgdocdir}/examples

%files common
%{_datadir}/votca

%files -n libvotca_csg%sover
%license csg/LICENSE.rst
%{_libdir}/libvotca_csg.so.%{sover}

%files devel
%{_includedir}/votca/csg/
%{_libdir}/libvotca_csg.so
%{_libdir}/cmake/VOTCA_CSG

%files bash
%dir %{_datadir}/bash_completion.d
%{_datadir}/bash_completion.d/votca

%changelog
