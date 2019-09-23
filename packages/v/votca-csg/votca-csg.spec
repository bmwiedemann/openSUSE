#
# spec file for package votca-csg
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013-2019 Christoph Junghans
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

Name:           votca-csg
Version:        1.5
%define         uversion %{version}
%define         sover 5
Release:        0
Summary:        VOTCA coarse-graining engine
License:        Apache-2.0
Group:          Productivity/Scientific/Chemistry
Url:            http://www.votca.org
Source0:        https://github.com/votca/csg/archive/v%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz
Source1:        https://github.com/votca/csg-tutorials/archive/v%{uversion}.tar.gz#/%{name}-tutorials-%{uversion}.tar.gz
Source2:        https://github.com/votca/csg-manual/releases/download/v%{uversion}/votca-csg-manual-%{uversion}.pdf

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gcc-c++
BuildRequires:  pkg-config
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_test-devel
%else
BuildRequires:  boost-devel >= 1.39.0
%endif
BuildRequires:  cmake >= 2.8.4
BuildRequires:  fdupes
BuildRequires:  gromacs-devel
BuildRequires:  hdf5-devel
 #for hdf5
BuildRequires:  zlib-devel
BuildRequires:  txt2tags
BuildRequires:  votca-tools-devel = %{version}

#exact same version is needed
Requires:       %{name}-common = %{version}
Requires:       libvotca_csg%sover = %{version}

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
Requires:       libvotca_csg%sover = %{version}
Requires:       votca-tools-devel = %{version}
Requires:       %{name} = %{version}

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
make %{?_smp_mflags}

%install
make -C build install DESTDIR=%{buildroot}
sed -i '1s@env @@' %{buildroot}/%{_datadir}/votca/scripts/inverse/*.py
# Move bash completion file to correct location
mkdir -p %{buildroot}%{_datadir}/bash_completion.d
cp scripts/csg-completion.bash %{buildroot}%{_datadir}/bash_completion.d/votca

%define pkgdocdir %{_docdir}/%{name}
mkdir -p %{buildroot}%{pkgdocdir}
cp %{S:2} %{buildroot}%{pkgdocdir}

mkdir -p %{buildroot}%{pkgdocdir}/examples
cp -r csg-tutorials-%{uversion}/* %{buildroot}%{pkgdocdir}/examples
%fdupes %{buildroot}%{_prefix}

#check
# https://github.com/votca/csg/issues/313
%ifarch i586
%global testargs ARGS='-E \\(Compare_csg_fmatch_3body_output1\\|Compare_csg_fmatch_output\\)'
%endif
make -C build test CTEST_OUTPUT_ON_FAILURE=1 %{?testargs:%{testargs}}

%post -n libvotca_csg%sover -p /sbin/ldconfig
%postun -n libvotca_csg%sover -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md NOTICE README.md LICENSE
%{_bindir}/csg_*
%{_mandir}/man1/*
%exclude %{pkgdocdir}/examples
%exclude %{pkgdocdir}/*.pdf

%files doc
%defattr(-,root,root,-)
%{pkgdocdir}/*.pdf

%files tutorials
%defattr(-,root,root,-)
%{pkgdocdir}/examples

%files common
%defattr(-,root,root,-)
%{_datadir}/votca

%files -n libvotca_csg%sover
%defattr(-,root,root,-)
%doc LICENSE
%{_libdir}/libvotca_csg.so.*
%{_mandir}/man7/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/votca/csg/
%{_libdir}/libvotca_csg.so
%{_libdir}/pkgconfig/libvotca_csg.pc

%files bash
%defattr(-,root,root,-)
%dir %{_datadir}/bash_completion.d
%{_datadir}/bash_completion.d/votca

%changelog
