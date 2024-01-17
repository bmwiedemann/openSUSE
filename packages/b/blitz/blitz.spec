#
# spec file for package blitz
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


%define   sonum 0
# Conditionals
# PAPI >= 6.0 is unsupported [https://github.com/blitzpp/blitz/issues/162]
%bcond_with papi
# Issue with make doc causing failed builds for openSUSE Leap 15.2
%if 0%{?suse_version} >= 1550
%bcond_without doc
%else
%bcond_with doc
%endif
# /Conditionals
Name:           blitz
Version:        1.0.2
Release:        0
Summary:        Blitz++ Multi-Dimensional Array Library for C++
License:        LGPL-3.0-or-later OR BSD-3-Clause OR Artistic-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/blitzpp/blitz/
Source:         https://github.com/blitzpp/blitz/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix_cmake_file_dir.patch -- https://github.com/blitzpp/blitz/pull/155
Patch0:         fix_cmake_file_dir.patch
BuildRequires:  cmake >= 3.12
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  graphviz-gnome
BuildRequires:  libboost_serialization-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  pkgconfig(openlibm)
%if %{with papi}
BuildRequires:  pkgconfig(papi)
%endif
%if %{with doc}
BuildRequires:  texi2html
BuildRequires:  texinfo
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
%endif

%description
Blitz++ is a C++ template class library that provides high-performance
multidimensional array containers for scientific computing.

%package     -n libblitz%{sonum}
Summary:        Blitz++ Multi-Dimensional Array Library for C++
Group:          Development/Libraries/C and C++

%description -n libblitz%{sonum}
Blitz++ is a C++ template class library that provides high-performance
multidimensional array containers for scientific computing.

This package provides shared libraries with blitz.

%package        devel
Summary:        Libraries, includes, etc. used to develop an application with %{name}
Group:          Development/Libraries/C and C++
Requires:       libblitz%{sonum} = %{version}

%description    devel
Blitz++ is a C++ template class library that provides high-performance
multidimensional array containers for scientific computing.

This package provides the header files and libraries needed to develop a blitz
application.

%package        doc
Summary:        The Blitz html docs
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
Blitz++ is a C++ class library for scientific computing which provides
performance on par with Fortran 77/90. It uses template techniques to achieve
high performance. Blitz++ provides dense arrays and vectors, random number
generators, and small vectors.

This package provides documentation files for the Blitz Library.

%prep
%autosetup -p1

%build
%cmake \
    -DBUILD_DOC=%{?with_doc:ON}%{!?with_doc:OFF} \
    -DBUILD_TESTING=ON \
    -DDISABLE_REFMAN_PDF=ON \
    -DENABLE_SERIALISATION=ON \
    -DSIMD_EXTENSION=ON \
    -DCMAKE_INSTALL_DOCDIR=%{_docdir}/blitz

%if %{with doc}
%make_build blitz-doc
%endif
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}/%{_libdir}/libblitz.a
%fdupes %{buildroot}%{_docdir}/blitz/

%post   -n libblitz%{sonum} -p /sbin/ldconfig
%postun -n libblitz%{sonum} -p /sbin/ldconfig

%files -n libblitz%{sonum}
%license COPYING COPYING.LESSER COPYRIGHT LEGAL LICENSE
%{_libdir}/libblitz.so.%{sonum}
%{_libdir}/libblitz.so.%{version}

%files devel
%license COPYING COPYING.LESSER COPYRIGHT LEGAL LICENSE
%if %{with doc}
%{_infodir}/blitz.info%{?ext_info}
%endif
%{_libdir}/libblitz.so
%{_libdir}/pkgconfig/blitz.pc
%{_libdir}/cmake/blitz*.cmake
%{_includedir}/blitz/
%{_includedir}/random/

%files doc
%doc ChangeLog ChangeLog.*
%if %{with doc}
%license %{_docdir}/blitz/COPYING
%license %{_docdir}/blitz/COPYING.LESSER
%license %{_docdir}/blitz/COPYRIGHT
%license %{_docdir}/blitz/LEGAL
%license %{_docdir}/blitz/LICENSE
%else
%license COPYING COPYING.LESSER COPYRIGHT LEGAL LICENSE
%endif
%{_docdir}/blitz/

%changelog
