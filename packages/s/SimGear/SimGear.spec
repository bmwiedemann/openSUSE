#
# spec file for package SimGear
#
# Copyright (c) 2022 SUSE LLC
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


# We want specific versions of the devel and plugins OpenSceneGraph subpackages
# in our requirements, i.e. the same version we have built against
%define openscenegraph_version %(rpm -qa --nosignature --nodigest libOpenSceneGraph\*-devel | sed 's/.*-devel-\\(.*\\)-.*/\\1/')

%define libname libSimGearCore-2020_3_17
%define main_version 2020.3
Name:           SimGear
Version:        %{main_version}.17
Release:        0
Summary:        Simulator Construction Gear
# https://sourceforge.net/p/flightgear/codetickets/1940/
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT
Group:          Amusements/Games/3D/Simulation
URL:            https://www.flightgear.org/
Source0:        https://sourceforge.net/projects/flightgear/files/release-%{main_version}/simgear-%{version}.tar.bz2
Source99:       SimGear-rpmlintrc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libOpenSceneGraph-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
BuildRequires:  udns-devel
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(zlib)

%description
SimGear is a set of open-source libraries designed to be used as building
blocks for quickly assembling 3D simulations, games, and visualization
applications.

SimGear is developed as part of the FlightGear project and used by the
FlightGear flight simulator and many of its related utilities.

%package -n %{libname}
Summary:        Simulator Construction Gear
Group:          Amusements/Games/3D/Simulation
Requires:       OpenSceneGraph-plugins = %{openscenegraph_version}

%description -n %{libname}
SimGear is a set of open-source libraries designed to be used as building
blocks for quickly assembling 3D simulations, games, and visualization
applications.

SimGear is developed as part of the FlightGear project and used by the
FlightGear flight simulator and many of its related utilities.

%package devel
Summary:        Development libraries and headers for SimGear
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
BuildRequires:  libboost_headers-devel
Requires:       libOpenSceneGraph-devel = %{openscenegraph_version}
Requires:       udns-devel
Requires:       pkgconfig(liblzma)
Requires:       pkgconfig(openal)
Requires:       pkgconfig(zlib)

%description devel
Development headers and libraries for building applications against
SimGear.

%prep
%autosetup -p1 -n simgear-%{version}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
# configure to build shared simgear libraries
%cmake \
	-DSIMGEAR_SHARED:BOOL=ON \
	-DSYSTEM_EXPAT:BOOL=ON \
	-DSYSTEM_UDNS:BOOL=ON \
	-DENABLE_OPENMP:BOOL=ON \
	-DENABLE_TESTS:BOOL=OFF

%cmake_build

%install
%cmake_install
install -m 755 -d %{buildroot}%{_docdir}/%{name}
install -m 644 -t %{buildroot}%{_docdir}/%{name} AUTHORS ChangeLog NEWS README

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%{_libdir}/libSimGear*.so.*

%files devel
%doc %{_docdir}/%{name}
%{_includedir}/simgear/
%{_libdir}/libSimGear*.so
%{_libdir}/cmake/SimGear/

%changelog
