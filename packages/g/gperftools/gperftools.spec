#
# spec file for package gperftools
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


Name:           gperftools
Version:        2.10
Release:        0
Summary:        Performance Tools for C++
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/gperftools/gperftools
Source0:        %{url}/releases/download/gperftools-%{version}/gperftools-%{version}.tar.gz
Patch1:         %{name}_fix_unassigned_malloc_in_unittest.patch
Patch2:         %{name}_gcc46.patch
BuildRequires:  autoconf >= 2.59
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
Provides:       google-perftools = %{version}
Obsoletes:      google-perftools < %{version}
Requires:       pprof
# based on basictypes.h in the source tree
ExclusiveArch:  %{ix86} x86_64 ppc ppc64 ppc64le %{arm} aarch64 mips s390x riscv64
%ifnarch s390x s390
BuildRequires:  pkgconfig(libunwind)
%ifarch %{ix86} x86_64 %{arm} aarch64 mips riscv64
BuildRequires:  pkgconfig(libunwind-coredump)
%endif
BuildRequires:  pkgconfig(libunwind-generic)
BuildRequires:  pkgconfig(libunwind-ptrace)
BuildRequires:  pkgconfig(libunwind-setjmp)
%endif
%ifnarch s390 riscv64
BuildRequires:  pkgconfig(valgrind)
%endif

%description
The gperftools package contains some utilities to improve and analyze the
performance of C++ programs.  This includes an optimized thread-caching
malloc() and cpu and heap profiling utilities.

%package -n libprofiler0
Summary:        CPU and Heap profiling library
Group:          System/Libraries

%description -n libprofiler0
This subpackage contains a library with cpu and heap profiling.

%package -n libtcmalloc4
Summary:        Thread-caching malloc library
Group:          System/Libraries

%description -n libtcmalloc4
This subpackage contains a library with optimized thread-caching
malloc().

%package -n libtcmalloc_debug4
Summary:        Thread-caching malloc library
Group:          System/Libraries

%description -n libtcmalloc_debug4
This subpackage contains a library with optimized thread-caching
malloc().

%package -n libtcmalloc_minimal4
Summary:        Thread-caching malloc library
Group:          System/Libraries

%description -n libtcmalloc_minimal4
This subpackage contains a library with optimized thread-caching
malloc().

%package -n libtcmalloc_minimal_debug4
Summary:        Thread-caching malloc library
Group:          System/Libraries

%description -n libtcmalloc_minimal_debug4
This subpackage contains a library with optimized thread-caching
malloc().

%package -n libtcmalloc_and_profiler4
Summary:        Thread-caching malloc library
Group:          System/Libraries

%description -n libtcmalloc_and_profiler4
This subpackage contains a library with optimized thread-caching
malloc().

%package devel
Summary:        Performance tools for C++
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libprofiler0 = %{version}
Requires:       libstdc++-devel
Requires:       libtcmalloc4 = %{version}
Requires:       libtcmalloc_and_profiler4 = %{version}
Requires:       libtcmalloc_debug4 = %{version}
Requires:       libtcmalloc_minimal4 = %{version}
Requires:       libtcmalloc_minimal_debug4 = %{version}
Provides:       google-perftools-devel = %{version}
Obsoletes:      google-perftools-devel < %{version}

%description devel
The gperftools-devel package contains static and debug libraries and header
files for developing applications that use the gperftools package.

%package devel-static
Summary:        Static libraries for performance tools for C++
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description devel-static
The gperftools-devel-static package contains static libraries for developing
applications that use the gperftools package.

%package doc
Summary:        Documentation for performance tools for C++
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
Documentation for gperftools package which contains some utilities to improve and analyze the
performance of C++ programs

%prep
%autosetup -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
autoreconf -fi
%ifnarch s390 riscv64
VALGRIND_FL=`pkg-config --cflags valgrind`
%endif
export CPPFLAGS="$VALGRIND_FL"
export CXXFLAGS="%{optflags} -fno-strict-aliasing $VALGRIND_FL"
export CFLAGS="%{optflags} -fno-strict-aliasing $VALGRIND_FL"
%configure \
  --with-gnu-ld \
  --with-pic \
  --disable-deprecated-pprof \
  --docdir=%{_defaultdocdir}/%{name}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libprofiler0 -p /sbin/ldconfig
%postun -n libprofiler0 -p /sbin/ldconfig
%post   -n libtcmalloc4 -p /sbin/ldconfig
%postun -n libtcmalloc4 -p /sbin/ldconfig
%post   -n libtcmalloc_debug4 -p /sbin/ldconfig
%postun -n libtcmalloc_debug4 -p /sbin/ldconfig
%post   -n libtcmalloc_minimal4 -p /sbin/ldconfig
%postun -n libtcmalloc_minimal4 -p /sbin/ldconfig
%post   -n libtcmalloc_minimal_debug4 -p /sbin/ldconfig
%postun -n libtcmalloc_minimal_debug4 -p /sbin/ldconfig
%post   -n libtcmalloc_and_profiler4 -p /sbin/ldconfig
%postun -n libtcmalloc_and_profiler4 -p /sbin/ldconfig

%files
%{_bindir}/pprof-symbolize

%files -n libprofiler0
%{_libdir}/libprofiler.so.0*

%files -n libtcmalloc4
%{_libdir}/libtcmalloc.so.4*

%files -n libtcmalloc_debug4
%{_libdir}/libtcmalloc_debug.so.4*

%files -n libtcmalloc_minimal4
%{_libdir}/libtcmalloc_minimal.so.4*

%files -n libtcmalloc_minimal_debug4
%{_libdir}/libtcmalloc_minimal_debug.so.4*

%files -n libtcmalloc_and_profiler4
%{_libdir}/libtcmalloc_and_profiler.so.4*

%files devel
%{_includedir}/google
%{_includedir}/gperftools
%{_libdir}/libprofiler.so
%{_libdir}/libtcmalloc.so
%{_libdir}/libtcmalloc_debug.so
%{_libdir}/libtcmalloc_minimal.so
%{_libdir}/libtcmalloc_minimal_debug.so
%{_libdir}/libtcmalloc_and_profiler.so
%{_libdir}/pkgconfig/*.pc

%files devel-static
%{_libdir}/libprofiler.a
%{_libdir}/libtcmalloc.a
%{_libdir}/libtcmalloc_debug.a
%{_libdir}/libtcmalloc_minimal.a
%{_libdir}/libtcmalloc_minimal_debug.a
%{_libdir}/libtcmalloc_and_profiler.a

%files doc
%{_docdir}/%{name}

%changelog
