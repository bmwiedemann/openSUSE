#
# spec file for package HepMC
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           HepMC
%define lname	libHepMC3-1
Version:        3.1.1
Release:        0
Summary:        An event record for High Energy Physics Monte Carlo Generators in C++
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
Url:            http://hepmc.web.cern.ch/hepmc/
Source:         http://hepmc.web.cern.ch/hepmc/releases/%{name}3-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  graphviz-gd
BuildRequires:  ghostscript-fonts-std
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported.

%package -n %{lname}
Summary:        An event record for High Energy Physics Monte Carlo Generators
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
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported.

This package provides the source and header files required for
developing with HepMC.

%prep
%setup -q -n %{name}3-%{version}

%build
%cmake -DHEPMC3_ENABLE_ROOTIO:BOOL=OFF \
       -DCONFIG_INSTALL_DIR:PATH=%{_libdir}/HepMC/ \
       -DHEPMC3_BUILD_EXAMPLES:BOOL=OFF

%cmake_build
pushd ../doc/doxygen
make %{?_smp_mflags}
popd

%install
%cmake_install
# REMOVE STATIC LIBRARIES
rm -f %{buildroot}%{_libdir}/*.a

# Weird duplicated installation dir
rm -fr %{buildroot}%{_builddir}

chmod +x %{buildroot}%{_bindir}/HepMC3-config

#Install examples manually so that fdupes can be run on them
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -pr examples %{buildroot}%{_docdir}/%{name}/
%fdupes %{buildroot}%{_docdir}/%{name}/examples

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/libHepMC3.so.*
%{_libdir}/libHepMC3search.so.*

%files devel
%doc README* ChangeLog DESIGN doc/doxygen/html
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/examples
%{_bindir}/HepMC3-config
%{_libdir}/libHepMC3.so
%{_libdir}/libHepMC3search.so
%{_includedir}/%{name}3/
%{_datadir}/%{name}3/

%changelog
