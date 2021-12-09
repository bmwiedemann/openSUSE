#
# spec file for package votca-xtp
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2018-2021 Christoph Junghans
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


Name:           votca-xtp
Version:        2022~rc1
Release:        0
%define         uversion 2022-rc.1
%define         sover 2022
Summary:        VOTCA excitation and charge properties module
License:        Apache-2.0
Group:          Productivity/Scientific/Chemistry
URL:            http://www.votca.org
Source0:        https://github.com/votca/votca/archive/v%{uversion}.tar.gz#/votca-%{uversion}.tar.gz

BuildRequires:  cmake >= 2.8.4
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  libboost_filesystem-devel >= 1.48.0
BuildRequires:  libboost_program_options-devel >= 1.48.0
BuildRequires:  libboost_serialization-devel >= 1.48.0
BuildRequires:  libboost_system-devel >= 1.48.0
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_timer-devel >= 1.48.0
BuildRequires:  libxc-devel
BuildRequires:  libint-devel
BuildRequires:  libecpint-devel
BuildRequires:  pkg-config
BuildRequires:  votca-csg-devel = %{version}
# for hdf5
BuildRequires:  zlib-devel

#exact same version is needed
Requires:       %{name}-common = %{version}
Requires:       libvotca_xtp%sover = %{version}

Obsoletes:      votca-xtp-doc < %{version}
Provides:       votca-xtp-doc < %{version}

# libint2 is broken on 32-bit archs
# https://github.com/evaleev/libint/issues/196
# https://github.com/votca/xtp/issues/652
ExcludeArch: %ix86 %arm

%description
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the excitation and charge properties module for VOTCA.

%package -n libvotca_xtp%sover
Summary:        VOTCA excitation and charge properties module
Group:          System/Libraries

%description -n libvotca_xtp%sover
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the libraries for the excitation and charge
properties module for VOTCA.

%package devel
Summary:        Development headers and libraries for VOTCA XTP
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libvotca_xtp%sover = %{version}
Requires:       votca-csg-devel = %{version}

%description devel
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the development headers and libraries for the
excitation and charge properties module engine for VOTCA.

%package common
Summary:        Architecture-independent data files for VOTCA XTP
Group:          Productivity/Scientific/Chemistry
BuildArch:      noarch

%description common
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the architecture-independent data files for VOTCA XTP.

%prep
%setup -n votca-%{uversion} -q

FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" xtp/src/libxtp/version.cc

%build
%{cmake} -DCMAKE_SKIP_RPATH=OFF -DBUILD_MANPAGES=ON -DENABLE_TESTING=ON ../xtp
# save some memory
%define _smp_mflags -j1
%cmake_build

%install
%cmake_install
sed -i -e '1s@env @@'  %{buildroot}/%{_bindir}/xtp_* %{buildroot}/%{_datadir}/votca/xtp/benchmark/xtp_benchmark

%fdupes %{buildroot}%{_prefix}

%check
%ctest

%post -n libvotca_xtp%sover -p /sbin/ldconfig
%postun -n libvotca_xtp%sover -p /sbin/ldconfig

%files
%doc CHANGELOG.rst xtp/NOTICE.rst README.rst
%{_bindir}/xtp_*
%{_mandir}/man1/xtp_*

%files common
%license xtp/LICENSE.rst
%{_datadir}/votca

%files -n libvotca_xtp%sover
%{_libdir}/libvotca_xtp.so.%{sover}

%files devel
%{_includedir}/votca/xtp/
%{_libdir}/libvotca_xtp.so
%{_libdir}/cmake/VOTCA_XTP

%changelog
