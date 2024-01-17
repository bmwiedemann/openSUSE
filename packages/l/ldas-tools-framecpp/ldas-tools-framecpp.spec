#
# spec file for package ldas-tools-framecpp
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


%define _lto_cflags %{nil}
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
BuildRequires:  pkgconfig(ldastoolsal)
BuildRequires:  pkgconfig(ldastoolscmake)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
LDAS (LIGO Data Analysis System) is a collection of libraries and executables
aid in the processing of gravitation wave data sets. %{name} provides the
tools abstraction toolkit for LDAS.

This package provides C++ bindings for libframe for dealing with frame files.

%package -n libframecpp12
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n libframecpp12
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n libframecpp3-6
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n libframecpp3-6
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n libframecpp4-8
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n libframecpp4-8
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n libframecpp6-8
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n libframecpp6-8
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n libframecpp7-4
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n libframecpp7-4
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n libframecpp8-7
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n libframecpp8-7
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package -n libframecppc3
Summary:        C bindings for ldas-tools
Group:          System/Libraries

%description -n libframecppc3
This package provides a shared library for %{name} - a toolkit providing C
bindings for working with frame data.

%package -n libframecppcmn11
Summary:        C++ bindings for ldas-tools
Group:          System/Libraries
Conflicts:      libframecpp

%description -n libframecppcmn11
This package provides a shared library for %{name} - a toolkit providing C++
bindings for working with frame data.

%package devel
Summary:        Headers and source files for developing with %{name}
Group:          Development/Libraries/C and C++
Requires:       libboost_program_options-devel
Requires:       libframecpp12 = %{version}-%{release}
Requires:       libframecpp3-6 = %{version}-%{release}
Requires:       libframecpp4-8 = %{version}-%{release}
Requires:       libframecpp6-8 = %{version}-%{release}
Requires:       libframecpp7-4 = %{version}-%{release}
Requires:       libframecpp8-7 = %{version}-%{release}
Requires:       libframecppc3 = %{version}-%{release}
Requires:       libframecppcmn11 = %{version}-%{release}
Requires:       pkgconfig(ldastoolsal)
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(zlib)

%description devel
This package provides the headers and sources needed for developing programs
using %{name} - a toolkit providing C++ bindings for libframe.

%package c-devel
Summary:        Headers and source files for developing with %{name}'s in C
Group:          Development/Libraries/C and C++
Requires:       libframecppc3 = %{version}-%{release}

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

%fdupes %{buildroot}/%{_prefix}

%post   -n libframecpp12 -p /sbin/ldconfig
%postun -n libframecpp12 -p /sbin/ldconfig
%post   -n libframecpp3-6 -p /sbin/ldconfig
%postun -n libframecpp3-6 -p /sbin/ldconfig
%post   -n libframecpp4-8 -p /sbin/ldconfig
%postun -n libframecpp4-8 -p /sbin/ldconfig
%post   -n libframecpp6-8 -p /sbin/ldconfig
%postun -n libframecpp6-8 -p /sbin/ldconfig
%post   -n libframecpp7-4 -p /sbin/ldconfig
%postun -n libframecpp7-4 -p /sbin/ldconfig
%post   -n libframecpp8-7 -p /sbin/ldconfig
%postun -n libframecpp8-7 -p /sbin/ldconfig
%post   -n libframecppc3 -p /sbin/ldconfig
%postun -n libframecppc3 -p /sbin/ldconfig
%post   -n libframecppcmn11 -p /sbin/ldconfig
%postun -n libframecppcmn11 -p /sbin/ldconfig

%files -n libframecpp12
%{_libdir}/libframecpp.so.*

%files -n libframecppcmn11
%{_libdir}/libframecppcmn.so.*

%files -n libframecpp3-6
%{_libdir}/libframecpp3.so.*

%files -n libframecpp4-8
%{_libdir}/libframecpp4.so.*

%files -n libframecpp6-8
%{_libdir}/libframecpp6.so.*

%files -n libframecpp7-4
%{_libdir}/libframecpp7.so.*

%files -n libframecpp8-7
%{_libdir}/libframecpp8.so.*

%files -n libframecppc3
%{_libdir}/libframecppc.so.*

%files -n libframecppcmn11
%{_libdir}/libframecppcmn.so.*

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

%files c-devel
%{_includedir}/framecppc/
%{_libdir}/libframecppc.so
%{_libdir}/pkgconfig/framecppc.pc

%files utils
%{_bindir}/*

%files doc
%doc %{_docdir}/%{name}

%changelog
