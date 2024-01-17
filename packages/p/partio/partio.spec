#
# spec file for package partio
#
# Copyright (c) 2021 SUSE LLC
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


%define sover 1
%define libname libpartio%{sover}
%define pyver python3

Name:           partio
Version:        1.14.6
Release:        1
Summary:        Library for reading/writing/manipulating common animation particle
License:        BSD-3-Clause
URL:            https://github.com/wdas/%{name}
Source:         https://github.com/wdas/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  %{pyver}-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(zlib)

%description
C++ (with python bindings) library for easily reading/writing/manipulating
common animation particle formats such as PDB, BGEO, PTC.

%package devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
The %{name}-doc contains documentastion for the library.

%package -n %{libname}
Summary:        Core %{name} libraries

%description -n %{libname}
C++ (with python bindings) library for easily reading/writing/manipulating
common animation particle formats such as PDB, BGEO, PTC.

%package -n %{pyver}-%{name}
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}

%description -n %{pyver}-%{name}
The %{pyver}-%{name} contains Python 3 binding for the library.

%prep
%autosetup -p1
# provide a sane library version
sed -i 's:SOVERSION ${PARTIO_VERSION_MAJOR}: SOVERSION ${PARTIO_VERSION_MAJOR} VERSION %{version}:' src/lib/CMakeLists.txt
# fix shebangs
sed -i 's:^#!/usr/bin/env python:#!%{_bindir}/%{pyver}:' src/tools/*.py

%build
%cmake \
 -DCMAKE_PREFIX_PATH=%{_prefix} \
 -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name} \
 -DCXXFLAGS_STD=c++17
%cmake_build

%install
%cmake_install
# Remove files from python directory, that land in %%{_bindir} as well
rm -vf %{buildroot}%{python3_sitearch}/{partedit,partinspect,partjson}.py
# Remove tests
rm -vrf %{buildroot}%{_datadir}/%{name}/test
%fdupes %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_bindir}/part*
%{_datadir}/swig/%{name}.i
%dir %{_datadir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files doc
%doc %{_defaultdocdir}/%{name}/html

%files -n %{libname}
%license LICENSE
%{_libdir}/*.so.*

%files -n %{pyver}-%{name}
%{python3_sitearch}/_%{name}.so
%{python3_sitearch}/*.py

%changelog
