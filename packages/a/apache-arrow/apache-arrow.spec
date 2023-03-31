#
# spec file for package apache-arrow
#
# Copyright (c) 2023 SUSE LLC
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

%bcond_without tests
# Required for runtime dispatch, not yet packaged
%bcond_with xsimd

%define sonum   1100
# See git submodule /testing pointing to the correct revision
%define arrow_testing_commit ecab1162cbec872e17d949ecc86181670aee045c
# See git submodule /cpp/submodules/parquet-testing pointing to the correct revision
%define parquet_testing_commit 5b82793ef7196f7b3583e85669ced211cd8b5ff2
Name:           apache-arrow
Version:        11.0.0
Release:        0
Summary:        A development platform for in-memory data
License:        Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT
Group:          Development/Tools/Other
URL:            https://arrow.apache.org/
Source0:        https://github.com/apache/arrow/archive/apache-arrow-%{version}.tar.gz
Source1:        https://github.com/apache/arrow-testing/archive/%{arrow_testing_commit}.tar.gz#/arrow-testing-%{version}.tar.gz
Source2:        https://github.com/apache/parquet-testing/archive/%{parquet_testing_commit}.tar.gz#/parquet-testing-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  cmake >= 3.2
BuildRequires:  cmake(absl)
BuildRequires:  cmake(double-conversion) >= 3.1.5
BuildRequires:  cmake(re2)
BuildRequires:  cmake(Snappy) >= 1.1.7
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel >= 1.64.0
BuildRequires:  llvm-devel >= 7
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(bzip2) >= 1.0.8
BuildRequires:  pkgconfig(gflags) >= 2.2.0
BuildRequires:  pkgconfig(grpc++) >= 1.20.0
BuildRequires:  pkgconfig(libbrotlicommon) >= 1.0.7
BuildRequires:  pkgconfig(libbrotlidec) >= 1.0.7
BuildRequires:  pkgconfig(libbrotlienc) >= 1.0.7
BuildRequires:  pkgconfig(libcares) >= 1.15.0
BuildRequires:  pkgconfig(libglog) >= 0.3.5
BuildRequires:  pkgconfig(liblz4) >= 1.8.3
BuildRequires:  pkgconfig(libopenssl)
BuildRequires:  pkgconfig(liburiparser) >= 0.9.3
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(libzstd) >= 1.4.3
BuildRequires:  pkgconfig(protobuf) >= 3.7.1
BuildRequires:  pkgconfig(thrift) >= 0.11.0
BuildRequires:  pkgconfig(zlib) >= 1.2.11
%if %{with tests}
BuildRequires:  timezone
BuildRequires:  pkgconfig(gmock) >= 1.10
BuildRequires:  pkgconfig(gtest) >= 1.10
%endif


%description
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

%package     -n libarrow%{sonum}
Summary:        Development platform for in-memory data - shared library
Group:          System/Libraries

%description -n libarrow%{sonum}
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the shared library for Apache Arrow.

%package     -n libarrow_dataset%{sonum}
Summary:        Development platform for in-memory data - shared library
Group:          System/Libraries

%description -n libarrow_dataset%{sonum}
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the shared library for Dataset API support.

%package     -n libparquet%{sonum}
Summary:        Development platform for in-memory data - shared library
Group:          System/Libraries

%description -n libparquet%{sonum}
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the shared library for the Parquet format.

%package     -n libplasma%{sonum}
Summary:        Development platform for in-memory data - shared library
Group:          System/Libraries

%description -n libplasma%{sonum}
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the shared library for the
Plasma Shared Memory Object Store.

%package        devel
Summary:        Development platform for in-memory data - development files
Group:          Development/Libraries/C and C++
Requires:       libarrow%{sonum} = %{version}
Requires:       libarrow_dataset%{sonum} = %{version}

%description    devel
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the development libraries and headers for
Apache Arrow.

%package     -n apache-parquet-devel
Summary:        Development platform for in-memory data - development files
Group:          Development/Libraries/C and C++
Requires:       libparquet%{sonum} = %{version}

%description -n apache-parquet-devel
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the development libraries and headers for
the Parquet format.

%package     -n apache-plasma-devel
Summary:        Development platform for in-memory data - development files
Group:          Development/Libraries/C and C++
Requires:       libplasma%{sonum} = %{version}

%description -n apache-plasma-devel
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the development libraries and headers for
the Plasma component.

%package        devel-static
Summary:        Development platform for in-memory data - development files
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description    devel-static
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the static library

%package        dataset-devel-static
Summary:        Development platform for in-memory data - development files
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description    dataset-devel-static
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the static library for Dataset API support


%package     -n apache-parquet-devel-static
Summary:        Development platform for in-memory data - development files
Group:          Development/Libraries/C and C++
Requires:       apache-parquet-devel = %{version}

%description -n apache-parquet-devel-static
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the static library for the Parquet format.

%package     -n apache-plasma-devel-static
Summary:        Development platform for in-memory data - development files
Group:          Development/Libraries/C and C++
Requires:       apache-plasma-devel = %{version}

%description -n apache-plasma-devel-static
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the static plasma library

%package     -n apache-parquet-utils
Summary:        Development platform for in-memory data - development files
Group:          Productivity/Scientific/Math

%description -n apache-parquet-utils
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides utilities for working with the Parquet format.

%package     -n apache-plasma-server
Summary:        Development platform for in-memory data - development files
Group:          Productivity/Scientific/Math

%description -n apache-plasma-server
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides utilities for working with the Parquet format.

%prep
%setup -q -n arrow-apache-arrow-%{version} -a1 -a2

%build
export CFLAGS="%{optflags} -ffat-lto-objects"
export CXXFLAGS="%{optflags} -ffat-lto-objects"

pushd cpp
%cmake \
   -DARROW_BUILD_EXAMPLES:BOOL=ON \
   -DARROW_BUILD_SHARED:BOOL=ON \
   -DARROW_BUILD_STATIC:BOOL=ON \
   -DARROW_BUILD_TESTS:BOOL=%{?with_tests:ON}%{!?with_tests:OFF} \
   -DARROW_BUILD_UTILITIES:BOOL=ON \
   -DARROW_DEPENDENCY_SOURCE=SYSTEM \
   -DARROW_BUILD_BENCHMARKS:BOOL=OFF \
%ifarch aarch64
   -DARROW_SIMD_LEVEL:STRING=%{?with_xsimd:NEON}%{!?with_xsimd:NONE} \
%else
   -DARROW_SIMD_LEVEL:STRING="NONE" \
%endif
   -DARROW_RUNTIME_SIMD_LEVEL:STRING=%{?with_xsimd:MAX}%{!?with_xsimd:NONE} \
   -DARROW_COMPUTE:BOOL=ON \
   -DARROW_CSV:BOOL=ON \
   -DARROW_DATASET:BOOL=ON \
   -DARROW_FILESYSTEM:BOOL=ON \
   -DARROW_FLIGHT:BOOL=OFF \
   -DARROW_GANDIVA:BOOL=OFF \
   -DARROW_HDFS:BOOL=ON \
   -DARROW_HIVESERVER2:BOOL=OFF \
   -DARROW_IPC:BOOL=ON \
   -DARROW_JEMALLOC:BOOL=OFF \
   -DARROW_JSON:BOOL=ON \
   -DARROW_ORC:BOOL=OFF \
   -DARROW_PARQUET:BOOL=ON \
   -DARROW_PLASMA:BOOL=ON \
   -DARROW_USE_GLOG:BOOL=ON \
   -DARROW_USE_OPENSSL:BOOL=ON \
   -DARROW_WITH_BACKTRACE:BOOL=ON \
   -DARROW_WITH_BROTLI:BOOL=ON \
   -DARROW_WITH_BZ2:BOOL=ON \
   -DARROW_WITH_LZ4:BOOL=ON \
   -DARROW_WITH_SNAPPY:BOOL=ON \
   -DARROW_WITH_ZLIB:BOOL=ON \
   -DARROW_WITH_ZSTD:BOOL=ON \
   -DPARQUET_BUILD_EXAMPLES:BOOL=ON \
   -DPARQUET_BUILD_EXECUTABLES:BOOL=ON \
   -DPARQUET_REQUIRE_ENCRYPTION:BOOL=ON \
   -DARROW_VERBOSE_THIRDPARTY_BUILD:BOOL=ON \
   -DARROW_CUDA:BOOL=OFF \
   -DARROW_PLASMA_JAVA_CLIENT:BOOL=OFF \
   -DARROW_GANDIVA_JAVA:BOOL=OFF

%cmake_build
popd

%install
pushd cpp
%cmake_install
popd
%if %{with tests}
rm %{buildroot}%{_libdir}/libarrow_testing.so*
rm %{buildroot}%{_libdir}/libarrow_testing.a
rm %{buildroot}%{_libdir}/pkgconfig/arrow-testing.pc
rm -Rf %{buildroot}%{_includedir}/arrow/testing
%endif
rm -r %{buildroot}%{_datadir}/doc/arrow/
%fdupes %{buildroot}%{_libdir}/cmake

%check
%if %{with tests}
export PARQUET_TEST_DATA="${PWD}/parquet-testing-%{parquet_testing_commit}/data"
export ARROW_TEST_DATA="${PWD}/arrow-testing-%{arrow_testing_commit}/data"
pushd cpp
export PYTHON=%{_bindir}/python3
%ifarch %ix86 %arm32
GTEST_failing="TestDecimalFromReal*"
GTEST_failing="${GTEST_failing}:*TestDecryptionConfiguration.TestDecryption*"
%endif
%ifnarch x86_64
GTEST_failing="${GTEST_failing}:Jemalloc.GetAllocationStats"
%endif
if [ -n "${GTEST_failing}" ]; then
  export GTEST_FILTER=${GTEST_failing}
  %ctest --label-regex unittest || true
  export GTEST_FILTER=*:-${GTEST_failing}
fi
%ctest --label-regex unittest
popd
%endif

%post   -n libarrow%{sonum}   -p /sbin/ldconfig
%postun -n libarrow%{sonum}   -p /sbin/ldconfig
%post   -n libarrow_dataset%{sonum}   -p /sbin/ldconfig
%postun -n libarrow_dataset%{sonum}   -p /sbin/ldconfig
%post   -n libparquet%{sonum} -p /sbin/ldconfig
%postun -n libparquet%{sonum} -p /sbin/ldconfig
%post   -n libplasma%{sonum}  -p /sbin/ldconfig
%postun -n libplasma%{sonum}  -p /sbin/ldconfig

%files
%license LICENSE.txt NOTICE.txt header
%{_bindir}/arrow-file-to-stream
%{_bindir}/arrow-stream-to-file

%files -n libarrow%{sonum}
%license LICENSE.txt NOTICE.txt header
%{_libdir}/libarrow.so.*

%files -n libarrow_dataset%{sonum}
%license LICENSE.txt NOTICE.txt header
%{_libdir}/libarrow_dataset.so.*

%files -n libparquet%{sonum}
%license LICENSE.txt NOTICE.txt header
%{_libdir}/libparquet.so.*

%files -n libplasma%{sonum}
%license LICENSE.txt NOTICE.txt header
%{_libdir}/libplasma.so.*

%files devel
%doc README.md
%license LICENSE.txt NOTICE.txt header
%{_includedir}/arrow/
%{_libdir}/cmake/Arrow*
%{_libdir}/libarrow.so
%{_libdir}/libarrow_dataset.so
%{_libdir}/pkgconfig/arrow*.pc
%dir %{_datadir}/arrow
%{_datadir}/arrow/gdb
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load/%{_prefix}
%dir %{_datadir}/gdb/auto-load/%{_libdir}
%{_datadir}/gdb/auto-load/%{_libdir}/libarrow.so.*.py

%files -n apache-parquet-devel
%doc README.md
%license LICENSE.txt NOTICE.txt header
%{_includedir}/parquet/
%{_libdir}/cmake/Parquet
%{_libdir}/libparquet.so
%{_libdir}/pkgconfig/parquet.pc

%files -n apache-plasma-devel
%doc README.md
%license LICENSE.txt NOTICE.txt header
%{_includedir}/plasma/
%{_libdir}/libplasma.so
%{_libdir}/pkgconfig/plasma.pc
%{_libdir}/cmake/Plasma

%files devel-static
%license LICENSE.txt NOTICE.txt header
%{_libdir}/libarrow.a

%files dataset-devel-static
%license LICENSE.txt NOTICE.txt header
%{_libdir}/libarrow_dataset.a

%files -n apache-parquet-devel-static
%license LICENSE.txt NOTICE.txt header
%{_libdir}/libparquet.a

%files -n apache-plasma-devel-static
%license LICENSE.txt NOTICE.txt header
%{_libdir}/libplasma.a

%files -n apache-parquet-utils
%doc README.md
%license LICENSE.txt NOTICE.txt header
%{_bindir}/parquet-*

%files -n apache-plasma-server
%doc README.md
%license LICENSE.txt NOTICE.txt header
%{_bindir}/plasma-store-server

%changelog
