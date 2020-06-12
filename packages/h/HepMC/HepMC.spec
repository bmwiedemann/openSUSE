#
# spec file for package HepMC
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


%bcond_with rootio
%bcond_without pythia

Name:           HepMC
%define lname	libHepMC3-1
Version:        3.2.1
Release:        0
Summary:        An event record for High Energy Physics Monte Carlo Generators in C++
# Python bindings are BSD-3-Clause, packaged separately
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://hepmc.web.cern.ch/hepmc/
Source:         http://hepmc.web.cern.ch/hepmc/releases/%{name}3-%{version}.tar.gz
# PATCH-FIX-UPSTREAM HepMC-type-mismatch-error.patch badshah400@gmail.com -- Fix type mismatch between function definition and function call flagged by GCC 10
Patch0:         HepMC-type-mismatch-error.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz-gd
%if %{with pythia}
BuildRequires:  pythia-devel
%endif
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported.

%package -n %{lname}
Summary:        An event record for High Energy Physics Monte Carlo Generators
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported: the number of entries
is unlimited, spin density matrices can be stored with each vertex,
flow patterns (such as color) can be stored and traced, integers
representing random number generator states can be stored, and an
arbitrary number of event weights can be included. Particles and
vertices are kept separate in a graph structure, physically similar to
a physics event. The added information supports the modularisation of
event generators. Event information is accessed by means of iterators
supplied with the package.

%package devel
Summary:        Header files for HepMC
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Recommends:     %{name}-doc = %{version}

%description devel
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported.

This package provides the source and header files required for
developing with HepMC.

%package doc
Summary:        API documentation for HepMC
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++

%description doc
This package provides the API documentation for the HepMC library.

%package -n python3-HepMC
Summary:        Python bindings for HepMC
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Requires:       python3

%description -n python3-HepMC
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported.

This package provides the python module for coding with HepMC.

%prep
%autosetup -p1 -n %{name}3-%{version}

%build
%cmake -DHEPMC3_ENABLE_ROOTIO:BOOL=%{?with_rootio:ON}%{!?with_rootio:OFF} \
       -DHEPMC3_BUILD_DOCS:BOOL=ON \
       -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
       -DHEPMC3_BUILD_STATIC_LIBS:BOOL=OFF \
       -DHEPMC3_PYTHON_VERSIONS:STRING="%{py3_ver}" \
       -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
       -DHEPMC3_BUILD_EXAMPLES:BOOL=ON

%cmake_build

%install
%cmake_install

%fdupes %{buildroot}%{_docdir}/%{name}/

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/libHepMC3.so.*
%{_libdir}/libHepMC3search.so.*

%files devel
%license LICENCE COPYING
%doc README* ChangeLog DESIGN
%{_bindir}/HepMC3-config
%{_libdir}/libHepMC3.so
%{_libdir}/libHepMC3search.so
%{_includedir}/%{name}3/
%{_datadir}/%{name}3/

%files doc
%doc %{_docdir}/%{name}/

%files -n python3-HepMC
%license python/include/LICENSE
%{python3_sitearch}/pyHepMC3/
%{python3_sitearch}/pyHepMC3-%{version}-py%{py3_ver}.egg-info
%{python3_sitearch}/pyHepMC3.search-%{version}-py%{py3_ver}.egg-info

%changelog
