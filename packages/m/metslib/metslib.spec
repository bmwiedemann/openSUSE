#
# spec file for package metslib
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


Name:           metslib
Version:        0.5.3
Release:        0
Summary:        Metaheuristic modeling framework and optimization toolkit in modern C++
License:        CPL-1.0 OR GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://projects.coin-or.org/metslib
Source0:        http://www.coin-or.org/download/source/%{name}/%{name}-%{version}.tgz
# Removes all "libdir" paths from .pc file (which are unneeded).  Not upstream
Patch0:         %{name}-0.5.3-noarch.patch
# Port metslib to use boost random functionality instead of outdated tr1
# Based on https://github.com/PointCloudLibrary/pcl/commit/57ace9a92d1667eaa6193262032ff688e222ce0f
# Not upstream
Patch1:         %{name}-0.5.3-boost.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  pkg-config
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_random-devel
%else
BuildRequires:  boost-devel
%endif
BuildArch:      noarch

%description
METSlib is a metaheuristic modeling framework and optimization
toolkit in C++.

This package has no binary, but consists only of the header files and documentation.

%package        devel
Summary:        Metaheuristic modeling framework and optimization toolkit in modern C++
Group:          Development/Libraries/C and C++

%description    devel
METSlib is a metaheuristic modeling framework and optimization
toolkit in C++.

Model and algorithms are modular: any search algorithm can be applied
to the same model. On the other hand, no assumption is made on the
model, any problem type can be worked on: timetabling, assignment
problems, vehicle routing, bin-packing and so on.

Once the model is implemented in the problem framework, the library
allows testing of different Taboo Search strategies or even different
algorithms (Simulated Annealing or other local search based
algorithms) with a few lines of code.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML

%description doc
The %{name}-doc package provides documentation for the %{name} library.

%prep
%setup -q
%patch0
%patch1

# Disable -O3 optimization for unit tests
sed -i 's| -O3||g' configure

%build
export CXXFLAGS="%{optflags} -std=c++14"
%configure
%make_build
doxygen doxydoc/doxygen.conf

%install
%make_install
# Move pkgconfig file to /usr/share/pkgconfig (since package is noarch)
mkdir -p %{buildroot}%{_datadir}
mv %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_datadir}
%fdupes -s doxydoc/html

%check
make %{?_smp_mflags} test

%files devel
%doc AUTHORS NEWS README
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif

%{_includedir}/*
%{_datadir}/pkgconfig/*.pc

%files doc
%doc doxydoc/html
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif

%changelog
