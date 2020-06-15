#
# spec file for package votca-tools
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


Name:           votca-tools
Version:        1.6
Release:        0
%define         uversion %{version}
%define         sover 6
Summary:        VOTCA tools library
License:        Apache-2.0
Group:          Productivity/Scientific/Chemistry
URL:            http://www.votca.org
Source0:        https://github.com/votca/tools/archive/v%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libexpat-devel
BuildRequires:  pkg-config
Conflicts:      libvotca_tools5 < %{version}

%description
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

%package -n libvotca_tools%sover
Summary:        VOTCA tools library
Group:          System/Libraries

%description -n libvotca_tools%sover
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the basic tools library of VOTCA package.

%package devel
Summary:        Development headers and libraries for votca-tools
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       eigen3-devel
Requires:       fftw3-devel
Requires:       libexpat-devel
Requires:       libvotca_tools%sover = %{version}

%description devel
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains development headers and libraries for votca-tools.

%prep
%setup -n tools-%{uversion} -q

# Avoid unnecessary rebuilds of the package
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" src/libtools/version.cc

%build
%{cmake} -DWITH_RC_FILES=OFF -DCMAKE_SKIP_RPATH=OFF -DENABLE_TESTING=ON
%cmake_build

%install
%cmake_install
sed -i '1s@env @@' %{buildroot}/%{_bindir}/votca_compare

%check
make -C build test CTEST_OUTPUT_ON_FAILURE=1 %{?testargs}

%files
%{_bindir}/votca_*
%{_mandir}/man1/*
%{_mandir}/man7/*

%post -n libvotca_tools%sover -p /sbin/ldconfig
%postun -n libvotca_tools%sover -p /sbin/ldconfig

%files -n libvotca_tools%sover
%doc LICENSE NOTICE
%{_libdir}/libvotca_tools.so.%{sover}

%files devel
%{_includedir}/votca/
%{_libdir}/libvotca_tools.so
%{_libdir}/cmake/VOTCA_TOOLS

%changelog
