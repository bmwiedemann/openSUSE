#
# spec file for package itpp
#
# Copyright (c) 2024 SUSE LLC
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


%define sover   8
%define libname lib%{name}%{sover}
Name:           itpp
Version:        4.3.1
Release:        0
Summary:        C++ library of math, signal processing and communication routines
License:        GPL-3.0-only
URL:            https://itpp.sourceforge.net/
Source:         https://sourceforge.net/projects/itpp/files/itpp/%{version}/itpp-%{version}.tar.bz2
Patch0:         libitpp-4.0.7-namespace.patch
Patch1:         gtest_support.patch
#PATCH-FIX-UPSTREAM memmove.patch [deb#741814] cristeab@gmail.com -- Corrected multilateration algorithm
Patch2:         itpp-4.3.1_memmove.patch
# PATCH-FIX-UPSTREAM itpp-respect_dlib_suffix.diff mardnh@gmx.de -- http://sourceforge.net/p/itpp/bugs/236/
Patch3:         itpp-respect_dlib_suffix.diff
# PATCH-FIX-UPSTREAM itpp-reproducible.patch bmwiedemann -- https://sourceforge.net/p/itpp/git/merge-requests/3/
Patch4:         itpp-reproducible.patch
# build with the C++17 standard (required by current googletest headers)
Patch5:         itpp-set-cxx17-standard.patch
# PATCH-FIX-UPSTREAM itpp-cxx17-any-ambiguity.patch -- qualify itpp::any() in the tests to avoid clashing with std::any under C++17
Patch6:         itpp-cxx17-any-ambiguity.patch
BuildRequires:  blas-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fftw3-threads
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  googletest-devel
BuildRequires:  lapack-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fftw3)

%description
IT++ is a C++ library of mathematical, signal processing and
communication classes and functions. Its main use is in simulation of
communication systems and for performing research in the area of
communications. The kernel of the library consists of generic vector and
matrix classes, and a set of accompanying routines. Such a kernel makes
IT++ similar to MATLAB or GNU Octave.

%package -n %{libname}
Summary:        C++ library of math, signal processing and communication routines

%description -n %{libname}
IT++ is a C++ library of mathematical, signal processing and
communication classes and functions. Its main use is in simulation of
communication systems and for performing research in the area of
communications. The kernel of the library consists of generic vector and
matrix classes, and a set of accompanying routines. Such a kernel makes
IT++ similar to MATLAB or GNU Octave.

%package devel
Summary:        Header files for %{name}
Requires:       %{libname} = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       pkgconfig(fftw3)
Provides:       %{libname}-devel = %{version}
Obsoletes:      %{libname}-devel < %{version}

%description devel
This package contains the header files for the IT++ library contained in %{libname}

IT++ is a C++ library of mathematical, signal processing and
communication classes and functions. Its main use is in simulation of
communication systems and for performing research in the area of
communications. The kernel of the library consists of generic vector and
matrix classes, and a set of accompanying routines. Such a kernel makes
IT++ similar to MATLAB or GNU Octave.

%package doc
Summary:        Documentation for %{name}
Requires:       %{libname} = %{version}
Recommends:     mathjax
BuildArch:      noarch

%description doc
This package contains the documentation for the IT++ as html and man pages.

IT++ is a C++ library of mathematical, signal processing and
communication classes and functions. Its main use is in simulation of
communication systems and for performing research in the area of
communications. The kernel of the library consists of generic vector and
matrix classes, and a set of accompanying routines. Such a kernel makes
IT++ similar to MATLAB or GNU Octave.

%prep
%autosetup -N
%patch -P 0
%autopatch -m 1 -p1

# Doxygen fixup
# MATHJAX: {_datadir}/doc/packages/<name>/html/ -> {_datadir}/javascript/mathjax/
sed -i -e "/^HTML_TIMESTAMP / s/.*/TIMESTAMP = NO/" \
       -e "/HTML_HEADER/ d" \
       -e "/HTML_FOOTER/ d" \
       -e "$ a USE_MATHJAX = YES" \
       -e "$ a MATHJAX_RELPATH = \"../../../../javascript/mathjax/\"" \
    doc/doxygen_html.cfg.cmake.in

%build
%cmake \
  -DGTEST_DIR=%{_includedir}/gtest \
  -DLAPACK_LIBRARIES=%{_libdir}/liblapack.so.3 \
  -DCMAKE_BUILD_TYPE=Release
%cmake_build

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
build/gtests/itpp_gtests

%install
%cmake_install
# move docs to /usr/share/doc/packages
mkdir -p %{buildroot}%{_docdir}
mv -t %{buildroot}%{_docdir}/ %{buildroot}%{_datadir}/doc/%{name}
# find dupes in docs
%fdupes -s %{buildroot}%{_docdir}

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%{_bindir}/%{name}-config
%{_mandir}/man1/%{name}-config*
%{_datadir}/%{name}
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%files doc
%{_docdir}/%{name}

%changelog
