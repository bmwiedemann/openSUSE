#
# spec file for package zxing-cpp
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover 4

# for now, use the bundled zint for Factory/TW as well,
# to avoid unnecessary dependencies (qt, etc.)
%bcond_without  bundled_zint
# avoid unnecessary dependencies with 32-bit components
%ifarch %{arm} %{ix86}
%bcond_with     examples
%else
%bcond_without  examples
%endif
# examples-qt could cause circular dependencies
%bcond_with     examples_qt

Name:           zxing-cpp
Version:        3.1.1
Release:        0
Summary:        Library for processing 1D and 2D barcodes
License:        Apache-2.0 AND Zlib AND LGPL-2.1-with-Qt-Company-Qt-exception-1.1
URL:            https://github.com/zxing-cpp/zxing-cpp
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/test_samples.tar.gz
Source99:       baselibs.conf
# PATCH-FEATURE-OPENSUSE fix-install-examples.patch munix9@googlemail.com -- install ZXingOpenCV
Patch0:         fix-install-examples.patch
BuildRequires:  cmake >= 3.16
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(stb)
%if 0%{?suse_version} < 1600
BuildRequires:  gcc13-PIE
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif

%description
ZXing ("zebra crossing") is an multi-format 1D/2D barcode image
processing library. This package provides a C++ implementation.

%package -n libZXing%{sover}
Summary:        Library for processing 1D and 2D barcodes
%if %{with bundled_zint}
Provides:       bundled(zint) = 2.16.0
%else
BuildRequires:  cmake(zint) >= 2.16.0
%endif

%description -n libZXing%{sover}
ZXing ("zebra crossing") is an multi-format 1D/2D barcode image
processing library. This package provides a C++ implementation.

%package devel
Summary:        Header files for zxing, a library for processing 1D and 2D barcodes
Requires:       libZXing%{sover} = %{version}

%description devel
ZXing ("zebra crossing") is an multi-format 1D/2D barcode image
processing library. This package provides header files to use ZXing in
other applications.

%if %{with examples}
%package examples
Summary:        Commandline examples for %{name}
BuildRequires:  cmake(OpenCV)

%description examples
This package holds the commandline examples for %{name}.
%endif

%if %{with examples_qt}
%package examples-qt
Summary:        Qt examples for %{name}
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)

%description examples-qt
This package holds the Qt examples for %{name}.
%endif

%prep
%autosetup -a1 -p1
# remove hidden/backup files
find test/samples -type f -name ".*" -delete -print

%build
%define __builder ninja
%cmake \
%if 0%{?suse_version} < 1600
	-DCMAKE_C_COMPILER=gcc-13	\
	-DCMAKE_CXX_COMPILER=g++-13	\
%endif
	-DZXING_BLACKBOX_TESTS=ON	\
	-DZXING_UNIT_TESTS=ON		\
	-DZXING_C_API=ON		\
	-DZXING_DEPENDENCIES=LOCAL	\
%if %{with examples}
	-DZXING_EXAMPLES=ON		\
	-DZXING_EXAMPLES_USE_WEBP=ON	\
%else
	-DZXING_EXAMPLES=OFF		\
%endif
%if %{with examples_qt}
	-DZXING_EXAMPLES_QT=ON		\
%endif
%if %{without bundled_zint}
	-DZXING_USE_BUNDLED_ZINT=OFF	\
%endif
	-DZXING_WRITERS=BOTH
%cmake_build

%install
%cmake_install

%check
%ctest --parallel 1 --timeout 120 --verbose

%ldconfig_scriptlets -n libZXing%{sover}

%files -n libZXing%{sover}
%doc README.md
%license LICENSE
%{_libdir}/libZXing.so.*

%files devel
%license LICENSE
%{_includedir}/ZXing
%{_libdir}/cmake/ZXing
%{_libdir}/libZXing.so
%{_libdir}/pkgconfig/zxing.pc

%if %{with examples}
%files examples
%{_bindir}/ZXingOpenCV
%{_bindir}/ZXingReader
%{_bindir}/ZXingWriter
%endif

%if %{with examples_qt}
%files examples-qt
%{_bindir}/ZXingQtCamReader
%endif

%changelog
