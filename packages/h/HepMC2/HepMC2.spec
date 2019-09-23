#
# spec file for package HepMC
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%define srcname HepMC
Name:           HepMC2
Version:        2.06.09
Release:        0
Summary:        An event record for High Energy Physics Monte Carlo Generators in C++
License:        GPL-2.0
Group:          Development/Libraries/C and C++ 
Url:            http://lcgapp.cern.ch/project/simu/HepMC/
Source:         http://lcgapp.cern.ch/project/simu/HepMC/download/HepMC-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported.

%package -n libHepMC4
Summary:        Shared libraries for HepMC
Group:          System/Libraries

%description -n libHepMC4
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

This package provides the shared libraries for HepMC.

%package -n HepMC2-devel
Summary:        Header files for HepMC
Group:          Development/Libraries/C and C++
Requires:       libHepMC4 = %{version}
Conflicts:      HepMC-devel >= 3.0
Provides:       HepMC-devel = %{version}

%description -n HepMC2-devel
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported.

This package provides the source and header files required for
developng with HepMC.

%prep
%setup -q -n %{srcname}-%{version}
# CORRECT EXEC PERMISSIONS IN ChangeLog
chmod 0644 ChangeLog

%build
mkdir ../BUILD
pushd ../BUILD
cmake ../%{srcname}-%{version} \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_BUILD_TYPE=Release \
       -Dmomentum:STRING="GEV" \
       -Dlength:STRING="MM" \
       -Dbuild_docs:BOOL=OFF 

make %{?_smp_mflags}
popd

%install
pushd ../BUILD
%make_install
# REMOVE STATIC LIBRARIES
rm -f %{buildroot}%{_prefix}/lib/*.a

# MOVE SHARED LIBS TO LIBDIR
mkdir -p %{buildroot}%{_libdir}
%if "%{_lib}" != "lib"
    mv %{buildroot}%{_prefix}/lib/*.so* %{buildroot}%{_libdir}/
%endif
popd

# MOVE EXAMPLES AND DOCUMENTATION TO DOCDIR
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/%{srcname}/examples %{buildroot}%{_docdir}/%{name}/examples
mv %{buildroot}%{_datadir}/%{srcname}/doc/*.pdf %{buildroot}%{_docdir}/%{name}/

%post -n libHepMC4 -p /sbin/ldconfig

%postun -n libHepMC4 -p /sbin/ldconfig

%files -n libHepMC4
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING
%{_libdir}/*.so.*

%files -n HepMC2-devel
%defattr(-,root,root)
%{_docdir}/%{name}/
%{_includedir}/%{srcname}/
%{_libdir}/*.so

%changelog
