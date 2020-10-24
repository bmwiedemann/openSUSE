#
# spec file for package ldas-tools-framecpp
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define _lto_cflags %{nil}
%define shlib   libframecpp
%define shlibc  libframecppc3
Name:           ldas-tools-framecpp
Version:        2.7.0
Release:        0
Summary:        Toolkit providing C++ bindings for dealing with frame data
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            http://software.ligo.org
Source:         http://software.ligo.org/lscsoft/source/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ldas-tools-framecpp-no-return-from-nonvoid-func.patch badshah400@gmail.com -- Fix a non-void function not returning any value
Patch0:         ldas-tools-framecpp-no-return-from-nonvoid-func.patch
# PATCH-FIX-UPSTREAM ldas-tools-framecpp-fix-pkgconfig.patch badshah400@gmail.com -- Fix paths in pkgconfig file when absolute paths to LIBDIR and INCLUDEDIR are specified to cmake
Patch1:         ldas-tools-framecpp-fix-pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ldastoolscmake)
BuildRequires:  pkgconfig(ldastoolsal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
LDAS (LIGO Data Analysis System) is a collection of libraries and executables
aid in the processing of gravitation wave data sets. %{name} provides the
tools abstraction toolkit for LDAS.

This package provides C++ bindings for libframe for dealing with frame files.

%package -n %{shlib}
Summary:        Shared lib for %{name} - C++ bindings for dealing with frame data
Group:          Productivity/Scientific/Physics

%description -n %{shlib}
This package provides the shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package devel
Summary:        Headers and source files for developing with %{name}
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Requires:       libboost_program_options-devel
Requires:       pkgconfig(ldastoolsal)
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(zlib)

%description devel
This package provides the headers and sources needed for developing programs
using %{name} - a toolkit providing C++ bindings for libframe.

%package -n %{shlibc}
Summary:        Shared lib for C bindings for %{name}
Group:          Productivity/Scientific/Physics

%description -n %{shlibc}
This package provides the shared library for the C wrappers of %{name}.

%package c-devel
Summary:        Headers and source files for developing with %{name}'s in C
Group:          Development/Libraries/C and C++
Requires:       %{shlibc} = %{version}

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

%description doc
This package provides the API documentation for %{name} in HTML format.

%prep
%autosetup -p1

%build
%limit_build -m 2000
# Out-of-source builds using %%cmake macros don't work
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \\\
      -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \\\
      -DLIB_INSTALL_DIR:PATH=%{_libdir} \\\
      -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
      -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
      -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \\\
      -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \\\
      -DCMAKE_C_FLAGS="${CFLAGS:-%optflags} -DNDEBUG" \\\
      -DCMAKE_CXX_FLAGS="${CXXFLAGS:-%optflags} -DNDEBUG" \\\
      -DCMAKE_Fortran_FLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -DNDEBUG" \\\
      -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
      -DBUILD_SHARED_LIBS:BOOL=ON \\\
      -DBUILD_STATIC_LIBS:BOOL=OFF \\\
      -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \\\
      -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \\\
      -DCMAKE_MODULES_INSTALL_DIR=%{_datadir}/cmake/Modules \\\
      -DCMAKE_EXPORT_COMPILE_COMMANDS=1 \\\
      -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \\\
      .
make VERBOSE=1 %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot}%{_libdir} -name "*.a" -delete -print

%fdupes %{buildroot}%{_docdir}/%{name}

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig
%post -n %{shlibc} -p /sbin/ldconfig
%postun -n %{shlibc} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/libframecpp.so.*
%{_libdir}/libframecppcmn.so.*
%{_libdir}/libframecpp3.so.*
%{_libdir}/libframecpp4.so.*
%{_libdir}/libframecpp6.so.*
%{_libdir}/libframecpp7.so.*
%{_libdir}/libframecpp8.so.*

%files devel
%{_includedir}/framecpp/
%{_libdir}/libframecpp.so
%{_libdir}/libframecppcmn.so
%{_libdir}/libframecpp3.so
%{_libdir}/libframecpp4.so
%{_libdir}/libframecpp6.so
%{_libdir}/libframecpp7.so
%{_libdir}/libframecpp8.so
%exclude %{_libdir}/pkgconfig/framecppc.pc
%{_libdir}/pkgconfig/*.pc

%files -n %{shlibc}
%{_libdir}/libframecppc.so.*

%files c-devel
%{_includedir}/framecppc/
%{_libdir}/libframecppc.so
%{_libdir}/pkgconfig/framecppc.pc

%files utils
%{_bindir}/*

%files doc
%doc %{_docdir}/%{name}

%changelog
