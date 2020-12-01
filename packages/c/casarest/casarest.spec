#
# spec file for package casacore
#
# Copyright (c) 2020 SUSE LLC
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


# ninja too old on openSUSE Leap 15.1
%if 0%{?suse_version} == 1500 && 0%{?sle_version} == 150100
%bcond_with ninja
%else
%bcond_without ninja
%endif

%if %{with ninja}
%global __builder ninja
%endif

Name:           casarest
Version:        1.7.0
Release:        0
Summary:        A suite of C++ libraries for radio astronomy data processing
License:        GPL-3.0-or-later
URL:            https://github.com/casacore/casarest
Source0:        https://github.com/casacore/casarest/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/casacore/casarest/master/LICENSE
# PATCH-FIX-UPSTREAM casarest-no-return-in-non-void.patch badshah400@gmail.com -- Fix non-void functions function not returning anything
Patch0:         casarest-no-return-in-non-void.patch
BuildRequires:  casacore-devel
BuildRequires:  cmake
BuildRequires:  fftw3-threads-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(wcslib)
BuildRequires:  pkgconfig(zlib)
%if %{with ninja}
BuildRequires:  ninja
%endif

%description
The casarest package is the remainder of the AIPS++ libraries over and above
the casacore library. It consists of the libraries: msvis, calibration,
synthesis, flagging, simulators, and ionosphere.

The prorgram lwimager (part of synthesis) is the main deliverable.

%package libs
Summary:        Shared libraries for casarest

%description libs
The casarest package is the remainder of the AIPS++ libraries over and above
the casacore library. It consists of the libraries: msvis, calibration,
synthesis, flagging, simulators, and ionosphere.

This package provides the shared libraries for casarest.

%package devel
Summary:        Headers and sources for developing with casarest
Requires:       hdf5-devel
Requires:       pkgconfig(cfitsio)
Requires:       pkgconfig(wcslib)
Requires:       casacore-devel
Requires:       %{name}-libs = %{version}

%description devel
The casarest package is the remainder of the AIPS++ libraries over and above
the casacore library. It consists of the libraries: msvis, calibration,
synthesis, flagging, simulators, and ionosphere.

This package provides the headers and sources for developing software with
casarest.

%prep
%autosetup -p1
cp %{SOURCE1} ./

%build
%cmake -DLIBRARY_INSTALL_DIR=%{_lib} \
       -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON

%cmake_build

%install
%cmake_install

%post -n %{name}-libs -p %run_ldconfig
%postun -n %{name}-libs -p %run_ldconfig

%files
%license LICENSE
%{_bindir}/lwimager

%files libs
%license LICENSE
%{_libdir}/*.so

%files devel
%doc README.md
%license LICENSE
%{_includedir}/casarest/

%changelog
