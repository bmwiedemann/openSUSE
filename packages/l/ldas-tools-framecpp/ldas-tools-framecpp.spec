#
# spec file for package ldas-tools-framecpp
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define shlib       libframecpp16
%define shlib_c     libframecppc4
%define shlib_cmn   libframecppcmn12
%define shlib_fcpp3 libframecpp3-8
%define shlib_fcpp4 libframecpp4-10
%define shlib_fcpp6 libframecpp6-10
%define shlib_fcpp7 libframecpp7-6
%define shlib_fcpp8 libframecpp8-11
%define shlib_fcpp9 libframecpp9-0

Name:           ldas-tools-framecpp
Version:        3.0.4
Release:        0
Summary:        Toolkit providing C++ bindings for dealing with frame data
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://software.ligo.org
Source:         https://software.ligo.org/lscsoft/source/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ldas-tools-framecpp-fix-pkgconfig.patch badshah400@gmail.com -- Fix paths in pkgconfig file when absolute paths to LIBDIR and INCLUDEDIR are specified to cmake
Patch1:         ldas-tools-framecpp-fix-pkgconfig.patch
# PATCH-FIX-UPSTREAM ldas-tools-framecpp-cmake-no-boost-system.patch badshah400@gmail.com -- Drop "system" from list of boost components searched in CMake
Patch2:         ldas-tools-framecpp-cmake-no-boost-system.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  gtest
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel >= 1.67.0
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ldastoolsal)
BuildRequires:  pkgconfig(ldastoolscmake)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
# Build failures for 32 bit archs: `long long unsigned int` vs `size_t` types mismatch
ExcludeArch:    %{ix86} %{arm32}

%description
LDAS (LIGO Data Analysis System) is a collection of libraries and executables
aid in the processing of gravitation wave data sets. %{name} provides the
tools abstraction toolkit for LDAS.

This package provides C++ bindings for libframe for dealing with frame files.

%package -n %{shlib}
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n %{shlib}
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n %{shlib_fcpp3}
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n %{shlib_fcpp3}
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n %{shlib_fcpp4}
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n %{shlib_fcpp4}
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n %{shlib_fcpp6}
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n %{shlib_fcpp6}
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n %{shlib_fcpp7}
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n %{shlib_fcpp7}
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n %{shlib_fcpp8}
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n %{shlib_fcpp8}
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n %{shlib_fcpp9}
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n %{shlib_fcpp9}
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n %{shlib_c}
Summary:        C bindings for ldas-tools
Group:          System/Libraries

%description -n %{shlib_c}
This package provides a shared library for %{name} - a toolkit providing C
bindings for working with frame data.

%package -n %{shlib_cmn}
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n %{shlib_cmn}
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package devel
Summary:        Headers and source files for developing with %{name}
Group:          Development/Libraries/C and C++
Requires:       %{shlib_cmn} = %{version}-%{release}
Requires:       %{shlib_c} = %{version}-%{release}
Requires:       %{shlib_fcpp3} = %{version}-%{release}
Requires:       %{shlib_fcpp4} = %{version}-%{release}
Requires:       %{shlib_fcpp6} = %{version}-%{release}
Requires:       %{shlib_fcpp7} = %{version}-%{release}
Requires:       %{shlib_fcpp8} = %{version}-%{release}
Requires:       %{shlib_fcpp9} = %{version}-%{release}
Requires:       %{shlib} = %{version}-%{release}
Requires:       libboost_program_options-devel
Requires:       pkgconfig(ldastoolsal)
Requires:       pkgconfig(libzstd)
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(zlib)

%description devel
This package provides the headers and sources needed for developing programs
using %{name} - a toolkit providing C++ bindings for libframe.

%package c-devel
Summary:        Headers and source files for developing with %{name}'s in C
Group:          Development/Libraries/C and C++
Requires:       %{shlib_c} = %{version}-%{release}

%description c-devel
This package provides the headers and sources needed for developing programs
with %{name} in C.

%package utils
Summary:        Command line tools for use with framecpp
Group:          Productivity/Scientific/Physics

%description utils
This package provides command line tools  for use with framecpp.

%package doc
Summary:        HTML documentation for %{name} API
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package provides the API documentation for %{name} in HTML format.

%prep
%autosetup -p1

%build
%limit_build -m 2000
%cmake \
  -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install

find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot}%{_libdir} -name "*.a" -delete -print

%fdupes %{buildroot}%{_docdir}/%{name}/
%fdupes %{buildroot}%{_includedir}/framecpp/

%post   -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig
%post   -n %{shlib_c} -p /sbin/ldconfig
%postun -n %{shlib_c} -p /sbin/ldconfig
%post   -n %{shlib_cmn} -p /sbin/ldconfig
%postun -n %{shlib_cmn} -p /sbin/ldconfig
%post   -n %{shlib_fcpp3} -p /sbin/ldconfig
%postun -n %{shlib_fcpp3} -p /sbin/ldconfig
%post   -n %{shlib_fcpp4} -p /sbin/ldconfig
%postun -n %{shlib_fcpp4} -p /sbin/ldconfig
%post   -n %{shlib_fcpp6} -p /sbin/ldconfig
%postun -n %{shlib_fcpp6} -p /sbin/ldconfig
%post   -n %{shlib_fcpp7} -p /sbin/ldconfig
%postun -n %{shlib_fcpp7} -p /sbin/ldconfig
%post   -n %{shlib_fcpp8} -p /sbin/ldconfig
%postun -n %{shlib_fcpp8} -p /sbin/ldconfig
%post   -n %{shlib_fcpp9} -p /sbin/ldconfig
%postun -n %{shlib_fcpp9} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/libframecpp.so.*

%files -n %{shlib_cmn}
%{_libdir}/libframecppcmn.so.*

%files -n %{shlib_fcpp3}
%{_libdir}/libframecpp3.so.*

%files -n %{shlib_fcpp4}
%{_libdir}/libframecpp4.so.*

%files -n %{shlib_fcpp6}
%{_libdir}/libframecpp6.so.*

%files -n %{shlib_fcpp7}
%{_libdir}/libframecpp7.so.*

%files -n %{shlib_fcpp8}
%{_libdir}/libframecpp8.so.*

%files -n %{shlib_fcpp9}
%{_libdir}/libframecpp9.so.*

%files -n %{shlib_c}
%{_libdir}/libframecppc.so.*

%files devel
%license COPYING
%doc ChangeLog.md README
%{_includedir}/framecpp/
%{_libdir}/libframecpp.so
%{_libdir}/libframecppcmn.so
%{_libdir}/libframecpp3.so
%{_libdir}/libframecpp4.so
%{_libdir}/libframecpp6.so
%{_libdir}/libframecpp7.so
%{_libdir}/libframecpp8.so
%{_libdir}/libframecpp9.so
%exclude %{_libdir}/pkgconfig/framecppc.pc
%{_libdir}/pkgconfig/*.pc

%files c-devel
%license COPYING
%{_includedir}/framecppc/
%{_libdir}/libframecppc.so
%{_libdir}/pkgconfig/framecppc.pc

%files utils
%license COPYING
%{_bindir}/*

%files doc
%doc %{_docdir}/%{name}

%changelog
