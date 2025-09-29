#
# spec file for package apache-arrow
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


%bcond_without tests
%bcond_without flight

# Remove static build due to devel-static packages being required by the generated CMake Targets
%bcond_with static
# Required for runtime dispatch, not yet packaged
%bcond_with xsimd

%if %{suse_version} <= 1500
# requires __has_builtin with keywords
%define gccver 13
%endif

%define sonum   2100
# See git submodule /testing pointing to the correct revision
%define arrow_testing_commit fbf6b703dc93d17d75fa3664c5aa2c7873ebaf06
# See git submodule /cpp/submodules/parquet-testing pointing to the correct revision
%define parquet_testing_commit 18d17540097fca7c40be3d42c167e6bfad90763c
# See cpp/thirdparty/versions.txt, replace by BuildRequires: pkgconfig(mimalloc) as soon as gh#apache/arrow#42211 is resolved
%define arrow_mimalloc_build_version v2.2.4
Name:           apache-arrow
Version:        21.0.0
Release:        0
Summary:        A development platform for in-memory data
License:        Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT
Group:          Development/Tools/Other
URL:            https://arrow.apache.org/
# SourceRepository: https://github.com/apache/arrow
Source0:        https://github.com/apache/arrow/archive/apache-arrow-%{version}.tar.gz
Source1:        https://github.com/apache/arrow-testing/archive/%{arrow_testing_commit}.tar.gz#/arrow-testing-%{version}.tar.gz
Source2:        https://github.com/apache/parquet-testing/archive/%{parquet_testing_commit}.tar.gz#/parquet-testing-%{version}.tar.gz
Source3:        https://github.com/microsoft/mimalloc/archive/%{arrow_mimalloc_build_version}.tar.gz#/mimalloc-%{arrow_mimalloc_build_version}.tar.gz
# PATCH-FIX-OPENSUSE arrow-boost-system-1.89-boo1249599.patch gh#boostorg/system#132, boo#1249599
Patch1:         arrow-boost-system-1.89-boo1249599.patch
BuildRequires:  bison
BuildRequires:  cmake >= 3.25
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc%{?gccver}-c++
BuildRequires:  libboost_context-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_process-devel
%if 0%{?suse_version} < 1699
BuildRequires:  libboost_system-devel
%endif
%if %{with static}
BuildRequires:  libzstd-devel-static
%endif
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
BuildRequires:  (cmake(lz4) >= 1.10 or (pkgconfig(liblz4) >= 1.8.3 with pkgconfig(liblz4) < 1.10))
BuildRequires:  cmake(Snappy) >= 1.2.2
BuildRequires:  cmake(absl)
BuildRequires:  cmake(double-conversion) >= 3.1.5
BuildRequires:  cmake(re2)
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(bzip2) >= 1.0.8
BuildRequires:  pkgconfig(gflags) >= 2.2.2
BuildRequires:  pkgconfig(grpc++) >= 1.46.3
BuildRequires:  pkgconfig(libbrotlicommon) >= 1.0.9
BuildRequires:  pkgconfig(libbrotlidec) >= 1.0.9
BuildRequires:  pkgconfig(libbrotlienc) >= 1.0.9
BuildRequires:  pkgconfig(libcares) >= 1.17.2
BuildRequires:  pkgconfig(libglog) >= 0.5.0
BuildRequires:  pkgconfig(libopenssl)
BuildRequires:  pkgconfig(liburiparser) >= 0.9.3
BuildRequires:  pkgconfig(libutf8proc) >= 2.10.0
BuildRequires:  pkgconfig(libzstd) >= 1.5.7
BuildRequires:  pkgconfig(protobuf) >= 21.3
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(thrift) >= 0.22.0
BuildRequires:  pkgconfig(zlib) >= 1.3.1
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

%package     -n libarrow_acero%{sonum}
Summary:        Development platform for in-memory data - shared library
Group:          System/Libraries

%description -n libarrow_acero%{sonum}
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the shared library for the Acero streaming execution engine

%package     -n libarrow_compute%{sonum}
Summary:        Development platform for in-memory data - shared library
Group:          System/Libraries

%description -n libarrow_compute%{sonum}
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the shared library for the C++ Compute module

%package     -n libarrow_flight%{sonum}
Summary:        Development platform for in-memory data - shared library
Group:          System/Libraries

%description -n libarrow_flight%{sonum}
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the shared library for Arrow Flight

%package     -n libarrow_flight_sql%{sonum}
Summary:        Development platform for in-memory data - shared library
Group:          System/Libraries

%description -n libarrow_flight_sql%{sonum}
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the shared library for Arrow Flight SQL

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

%package        devel
Summary:        Development platform for in-memory data - development files
Group:          Development/Libraries/C and C++
Requires:       libarrow%{sonum} = %{version}
Requires:       libarrow_acero%{sonum} = %{version}
Requires:       libarrow_compute%{sonum} = %{version}
Requires:       libarrow_dataset%{sonum} = %{version}
%if %{with flight}
Requires:       libarrow_flight%{sonum} = %{version}
Requires:       libarrow_flight_sql%{sonum} = %{version}
%endif
%if %{with static}
Suggests:       %{name}-devel-static = %{version}
Suggests:       %{name}-acero-devel-static = %{version}
Suggests:       %{name}-compute-devel-static = %{version}
Suggests:       %{name}-dataset-devel-static = %{version}
%if %{with flight}
Suggests:       %{name}-flight-devel-static = %{version}
Suggests:       %{name}-flight-sql-devel-static = %{version}
%endif
%endif

%description    devel
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the development libraries and headers for
Apache Arrow.

%if %{with static}
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

%package        acero-devel-static
Summary:        Development platform for in-memory data - development files
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description    acero-devel-static
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the static library for the Acero streaming execution engine

%package        compute-devel-static
Summary:        Development platform for in-memory data - development files
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description    compute-devel-static
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the static library for the C++ Compute module

%package        flight-devel-static
Summary:        Development platform for in-memory data - development files
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description    flight-devel-static
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the static library for Arrow Flight

%package        flight-sql-devel-static
Summary:        Development platform for in-memory data - development files
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description    flight-sql-devel-static
Apache Arrow is a cross-language development platform for in-memory
data. It specifies a standardized language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware. It also provides computational
libraries and zero-copy streaming messaging and interprocess
communication.

This package provides the static library for Arrow Flight SQL

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
%endif

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

%if %{with static}
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
%endif

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

%prep
%setup -q -n arrow-apache-arrow-%{version} -a1 -a2
%if 0%{?suse_version} >= 1699
%patch -P1 -p1
%endif
# https://github.com/protocolbuffers/protobuf/issues/12292
sed -i 's/find_package(Protobuf/find_package(Protobuf CONFIG/' cpp/cmake_modules/FindProtobufAlt.cmake

%build
%{?gccver:export CXX=g++-%{gccver}}
%{?gccver:export CC=gcc-%{gccver}}
export CFLAGS="%{optflags} -ffat-lto-objects"
export CXXFLAGS="%{optflags} -ffat-lto-objects"
export ARROW_MIMALLOC_URL=%{SOURCE3}

pushd cpp
%cmake \
   -DARROW_BUILD_EXAMPLES:BOOL=ON \
   -DARROW_BUILD_SHARED:BOOL=ON \
   -DARROW_BUILD_STATIC:BOOL=%{?with_static:ON}%{!?with_static:OFF} \
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
%if %{with flight}
   -DARROW_FLIGHT:BOOL=ON \
   -DARROW_FLIGHT_SQL:BOOL=ON \
%endif
   -DARROW_GANDIVA:BOOL=OFF \
   -DARROW_SKYHOOK:BOOL=OFF \
   -DARROW_HDFS:BOOL=ON \
   -DARROW_HIVESERVER2:BOOL=OFF \
   -DARROW_IPC:BOOL=ON \
   -DARROW_JSON:BOOL=ON \
   -DARROW_ORC:BOOL=OFF \
   -DARROW_PARQUET:BOOL=ON \
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
   -DARROW_GANDIVA_JAVA:BOOL=OFF

%cmake_build
popd

%install
pushd cpp
%cmake_install
popd
%if %{with tests}
rm %{buildroot}%{_libdir}/libarrow_testing.so*
rm %{buildroot}%{_libdir}/pkgconfig/arrow-testing.pc
rm -Rf %{buildroot}%{_libdir}/cmake/ArrowTesting
rm -Rf %{buildroot}%{_includedir}/arrow/testing
%if %{with flight}
rm %{buildroot}%{_libdir}/libarrow_flight_testing.so*
rm %{buildroot}%{_libdir}/pkgconfig/arrow-flight-testing.pc
rm -Rf %{buildroot}%{_libdir}/cmake/ArrowFlightTesting
%endif
%if %{with static}
rm %{buildroot}%{_libdir}/libarrow_testing.a
%if %{with flight}
rm %{buildroot}%{_libdir}/libarrow_flight_testing.a
%endif
%endif
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
%ifarch s390x
# bsc#1218592
exclude_regex='--exclude-regex (arrow-dataset-file-parquet-test|parquet-internals-test|parquet-reader-test|parquet-arrow-test|parquet-arrow-internals-test|parquet-encryption-test|parquet-encryption-key-management-test)'
%endif
%ctest --label-regex unittest $exclude_regex
popd
%endif

%post   -n libarrow%{sonum}   -p /sbin/ldconfig
%postun -n libarrow%{sonum}   -p /sbin/ldconfig
%post   -n libarrow_acero%{sonum}  -p /sbin/ldconfig
%postun -n libarrow_acero%{sonum}  -p /sbin/ldconfig
%post   -n libarrow_compute%{sonum}  -p /sbin/ldconfig
%postun -n libarrow_compute%{sonum}  -p /sbin/ldconfig
%if %{with flight}
%post   -n libarrow_flight%{sonum}  -p /sbin/ldconfig
%postun -n libarrow_flight%{sonum}  -p /sbin/ldconfig
%post   -n libarrow_flight_sql%{sonum}  -p /sbin/ldconfig
%postun -n libarrow_flight_sql%{sonum}  -p /sbin/ldconfig
%endif
%post   -n libarrow_dataset%{sonum}   -p /sbin/ldconfig
%postun -n libarrow_dataset%{sonum}   -p /sbin/ldconfig
%post   -n libparquet%{sonum} -p /sbin/ldconfig
%postun -n libparquet%{sonum} -p /sbin/ldconfig

%files
%license LICENSE.txt NOTICE.txt
%{_bindir}/arrow-file-to-stream
%{_bindir}/arrow-stream-to-file

%files -n libarrow%{sonum}
%license LICENSE.txt NOTICE.txt
%{_libdir}/libarrow.so.*

%files -n libarrow_acero%{sonum}
%license LICENSE.txt NOTICE.txt
%{_libdir}/libarrow_acero.so.*

%files -n libarrow_compute%{sonum}
%license LICENSE.txt NOTICE.txt
%{_libdir}/libarrow_compute.so.*

%if %{with flight}
%files -n libarrow_flight%{sonum}
%license LICENSE.txt NOTICE.txt
%{_libdir}/libarrow_flight.so.*

%files -n libarrow_flight_sql%{sonum}
%license LICENSE.txt NOTICE.txt
%{_libdir}/libarrow_flight_sql.so.*
%endif

%files -n libarrow_dataset%{sonum}
%license LICENSE.txt NOTICE.txt
%{_libdir}/libarrow_dataset.so.*

%files -n libparquet%{sonum}
%license LICENSE.txt NOTICE.txt
%{_libdir}/libparquet.so.*

%files devel
%doc README.md
%license LICENSE.txt NOTICE.txt
%{_includedir}/arrow/
%{_libdir}/cmake/Arrow*
%{_libdir}/libarrow.so
%{_libdir}/libarrow_acero.so
%{_libdir}/libarrow_compute.so
%{_libdir}/libarrow_dataset.so
%if %{with flight}
%{_libdir}/libarrow_flight.so
%{_libdir}/libarrow_flight_sql.so
%endif
%{_libdir}/pkgconfig/arrow*.pc
%dir %{_datadir}/arrow
%{_datadir}/arrow/gdb
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load/%{_prefix}
%dir %{_datadir}/gdb/auto-load/%{_libdir}
%{_datadir}/gdb/auto-load/%{_libdir}/libarrow.so.*.py

%if %{with static}
%files devel-static
%license LICENSE.txt NOTICE.txt
%{_libdir}/libarrow.a

%files acero-devel-static
%license LICENSE.txt NOTICE.txt
%{_libdir}/libarrow_acero.a

%files compute-devel-static
%license LICENSE.txt NOTICE.txt
%{_libdir}/libarrow_compute.a

%files dataset-devel-static
%license LICENSE.txt NOTICE.txt
%{_libdir}/libarrow_dataset.a

%if %{with flight}
%files flight-devel-static
%license LICENSE.txt NOTICE.txt
%{_libdir}/libarrow_flight.a

%files flight-sql-devel-static
%license LICENSE.txt NOTICE.txt
%{_libdir}/libarrow_flight_sql.a
%endif
%endif

%files -n apache-parquet-devel
%doc README.md
%license LICENSE.txt NOTICE.txt
%{_includedir}/parquet/
%{_libdir}/cmake/Parquet
%{_libdir}/libparquet.so
%{_libdir}/pkgconfig/parquet.pc

%if %{with static}
%files -n apache-parquet-devel-static
%license LICENSE.txt NOTICE.txt
%{_libdir}/libparquet.a
%endif

%files -n apache-parquet-utils
%doc README.md
%license LICENSE.txt NOTICE.txt
%{_bindir}/parquet-*

%changelog
