#
# spec file for package votca-csg
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2013-2020 Christoph Junghans
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
Version:        1.6.1
Release:        0
%define         uversion %{version}
%define         sover 6
Summary:        VOTCA coarse-graining engine
License:        Apache-2.0
Group:          Productivity/Scientific/Chemistry
URL:            http://www.votca.org
Source0:        https://github.com/votca/csg/archive/v%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz
Source1:        https://github.com/votca/csg-tutorials/archive/v%{uversion}.tar.gz#/%{name}-tutorials-%{uversion}.tar.gz
Source2:        https://github.com/votca/csg-manual/releases/download/v%{uversion}/votca-csg-manual-%{uversion}.pdf

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  cmake >= 2.8.4
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gromacs-devel
BuildRequires:  hdf5-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  memory-constraints
BuildRequires:  pkg-config
 #for hdf5
BuildRequires:  python3-txt2tags
BuildRequires:  votca-tools-devel = %{version}
BuildRequires:  zlib-devel

#exact same version is needed
Requires:       %{name}-common = %{version}
Requires:       libvotca_csg%sover = %{version}
# The developer man page was wrongly shipped in the library package until votca 1.6
Conflicts:      libvotca_csg5

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

%package doc
Summary:        Manual for VOTCA Coarse Graining Engine
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the PDF manual.

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
%setup -n csg-%{uversion} -q

FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" src/libcsg/version.cc
tar -xzf %{S:1}

%build
%{cmake} -DWITH_RC_FILES=OFF -DCMAKE_SKIP_RPATH:BOOL=OFF -DWITH_H5MD=ON -DWITH_GMX=ON -DENABLE_TESTING=ON -DREGRESSIONTEST_TOLERANCE="2e-5"
%limit_build -m 2000
%cmake_build

%install
%cmake_install
sed -i '1s@env @@' %{buildroot}/%{_datadir}/votca/scripts/inverse/cma_processor.py 

# Move bash completion file to correct location
mkdir -p %{buildroot}%{_datadir}/bash_completion.d
cp %{buildroot}%{_datadir}/votca/rc/csg-completion.bash %{buildroot}%{_datadir}/bash_completion.d/votca

%define pkgdocdir %{_docdir}/%{name}
mkdir -p %{buildroot}%{pkgdocdir}
cp %{S:2} %{buildroot}%{pkgdocdir}

mkdir -p %{buildroot}%{pkgdocdir}/examples
cp -r csg-tutorials-%{uversion}/* %{buildroot}%{pkgdocdir}/examples
sed -i '1s@env @@' %{buildroot}%{pkgdocdir}/examples/LJ1-LJ2/imc/svd.py

%fdupes %{buildroot}%{_prefix}

#check
make -C build test CTEST_OUTPUT_ON_FAILURE=1 %{?testargs}

%post -n libvotca_csg%sover -p /sbin/ldconfig
%postun -n libvotca_csg%sover -p /sbin/ldconfig

%files
%doc CHANGELOG.md NOTICE README.md LICENSE
%{_bindir}/csg_*
%{_mandir}/man1/*
%{_mandir}/man7/*
%exclude %{pkgdocdir}/examples
%exclude %{pkgdocdir}/*.pdf

%files doc
%{pkgdocdir}/*.pdf

%files tutorials
%{pkgdocdir}/examples

%files common
%{_datadir}/votca

%files -n libvotca_csg%sover
%doc LICENSE
%{_libdir}/libvotca_csg.so.%{sover}

%files devel
%{_includedir}/votca/csg/
%{_libdir}/libvotca_csg.so
%{_libdir}/cmake/VOTCA_CSG

%files bash
%dir %{_datadir}/bash_completion.d
%{_datadir}/bash_completion.d/votca

%changelog
